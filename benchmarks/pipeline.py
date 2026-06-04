import json
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, replace
from datetime import datetime
from pathlib import Path
from typing import Any

from rulechef.core import Dataset

from benchmarks.data import BenchmarkRun, DataSplit, load_human_feedback, make_dataset
from benchmarks.io import save_checkpoint, serialize_rules
from benchmarks.reporting import evaluate_test, make_oniteration_callback
from clear_anonymization.models.nerlearner import NERLearner

CHECKPOINT_FILE = "checkpoint.json"


@dataclass
class StepContext:
    rules: list
    split: DataSplit
    learner: NERLearner
    eval_dataset: Dataset
    dev_dataset: Dataset
    batch_metrics: list = field(default_factory=list)
    iteration_metrics: list = field(default_factory=list)
    best_rules: list = field(default_factory=list)
    best_f1: float = 0.0
    best_batch_idx: int = -1
    t_learn: float = 0.0
    t_eval: float = 0.0
    eval_results: Any = None
    history: list = field(default_factory=list)
    checkpoint_path: Path | None = None


class Step(ABC):
    @abstractmethod
    def run(self, context: StepContext) -> StepContext:
        pass


class LearningPipeline:
    def __init__(self, steps: list[Step]):
        self.steps = steps

    def run(self, ctx: StepContext) -> StepContext:
        for step in self.steps:
            ctx = step.run(ctx)
        return ctx


class SynthesisStep(Step):
    def __init__(
        self,
        *,
        batch_size,
        refine_per_batch,
        refine_every,
        audit_interval,
        start_batch,
        phase,
        synthesis_strategy,
        seed=42,
    ):
        self.batch_size = batch_size
        self.refine_per_batch = refine_per_batch
        self.refine_every = refine_every
        self.audit_interval = audit_interval
        self.start_batch = start_batch
        self.phase = phase
        self.seed = seed
        self.synthesis_strategy = synthesis_strategy

    def run(self, ctx: StepContext) -> StepContext:
        if self.synthesis_strategy != "bulk":
            train_for_chef = ctx.split.train + ctx.split.counter_examples
            random.Random(self.seed).shuffle(train_for_chef)
        else:
            train_for_chef = ctx.split.train
        batch_metrics = list(ctx.batch_metrics)  # copy to avoid mutating context
        iteration_metrics = list(ctx.iteration_metrics)
        rules_snapshot = []
        on_iteration = make_oniteration_callback(iteration_metrics)
        best = {
            "f1": ctx.best_f1,
            "rules": list(ctx.best_rules) if ctx.best_rules else [],
            "batch_idx": ctx.best_batch_idx,
        }

        def on_batch(batch_idx, rules):
            rules_snapshot.append({"batch": batch_idx, "rules": serialize_rules(rules)})
            result, _ = evaluate_test(ctx.dev_dataset, rules, ctx.learner)
            batch_metrics.append(
                {
                    "batch": batch_idx,
                    "num_rules": len(rules),
                    "exact_match": result.exact_match,
                    "micro_f1": result.micro_f1,
                    "micro_precision": result.micro_precision,
                    "micro_recall": result.micro_recall,
                    "macro_f1": result.macro_f1,
                    "per_class": [
                        {
                            "label": cm.label,
                            "f1": cm.f1,
                            "precision": cm.precision,
                            "recall": cm.recall,
                        }
                        for cm in (result.per_class or [])
                    ],
                }
            )
            if result.micro_f1 > best["f1"]:
                best["f1"] = result.micro_f1
                best["rules"] = list(rules)
                best["batch_idx"] = batch_idx
            print(
                f"  [batch {batch_idx}] dev micro_f1={result.micro_f1:.3f}"
                f"  P={result.micro_precision:.3f}  R={result.micro_recall:.3f}"
            )
            if ctx.checkpoint_path:
                save_checkpoint(
                    ctx.checkpoint_path,
                    {
                        "phase": self.phase,
                        "completed_batches": batch_idx + 1,
                        "rules": serialize_rules(rules),
                        "best_rules": serialize_rules(best["rules"])
                        if best["rules"]
                        else [],
                        "best_f1": best["f1"],
                        "best_batch_idx": best["batch_idx"],
                        "batch_metrics": batch_metrics,
                        "iteration_metrics": iteration_metrics,
                        "rules_snapshot": rules_snapshot,
                        "timestamp": datetime.now().isoformat(),
                    },
                )

        fit_result = ctx.learner.fit_batched(
            train_for_chef,
            batch_size=self.batch_size,
            eval_dataset=ctx.eval_dataset if self.refine_per_batch > 0 else None,
            refine_per_batch=self.refine_per_batch,
            refine_every=self.refine_every,
            iteration_callback=on_iteration,
            batch_callback=on_batch,
            audit_interval=self.audit_interval,
            seed_rules=ctx.rules or None,
            start_batch=self.start_batch,
        )
        if fit_result is None:
            return replace(
                ctx,
                batch_metrics=batch_metrics,
                iteration_metrics=iteration_metrics,
                best_f1=best["f1"],
                best_rules=best["rules"],
                best_batch_idx=best["batch_idx"],
            )

        rules, new_t_learn = fit_result
        history_entry = {
            "phase": "train",
            "dataset": ctx.split.name,
            "num_rules": len(rules),
            "t_learn": round(ctx.t_learn + new_t_learn, 1),
            "timestamp": datetime.now().isoformat(),
            "num_train_docs": len(ctx.split.train),
            "num_eval_docs": len(ctx.split.eval),
            "num_train_annotations": sum(len(s["entities"]) for s in ctx.split.train),
            "num_eval_annotations": sum(len(s["entities"]) for s in ctx.split.eval),
            "batch_metrics": batch_metrics,
            "iteration_metrics": iteration_metrics,
            "rules_snapshot": rules_snapshot,
        }

        return replace(
            ctx,
            rules=rules,
            batch_metrics=batch_metrics,
            iteration_metrics=iteration_metrics,
            best_f1=best["f1"],
            best_rules=best["rules"],
            best_batch_idx=best["batch_idx"],
            t_learn=ctx.t_learn + new_t_learn,
            history=ctx.history + [history_entry],
        )


class RefinementStep(Step):
    def __init__(self, *, max_iterations, use_feedback=False):
        self.max_iterations = max_iterations
        self.use_feedback = use_feedback

    def run(self, ctx: StepContext) -> StepContext:
        rules_to_refine = ctx.best_rules or ctx.rules
        print(
            f"\nRefining best {len(rules_to_refine)} rules"
            f" ({len(ctx.split.eval)} eval examples,"
            f" max {self.max_iterations} iterations)..."
        )
        iteration_metrics = []
        on_iteration = make_oniteration_callback(iteration_metrics)
        dataset = ctx.dev_dataset if self.use_feedback else ctx.eval_dataset
        rules, refine_eval = ctx.learner.refine(
            rules_to_refine,
            dataset,
            max_iterations=self.max_iterations,
            iteration_callback=on_iteration,
        )
        if refine_eval:
            print(f"  Eval micro F1: {refine_eval.micro_f1:.1%}")

        history_entry = {
            "phase": "refine",
            "dataset": ctx.split.name,
            "num_rules": len(rules),
            "micro_f1": refine_eval.micro_f1 if refine_eval else None,
            "micro_precision": refine_eval.micro_precision if refine_eval else None,
            "micro_recall": refine_eval.micro_recall if refine_eval else None,
            "iteration_metrics": iteration_metrics,
            "timestamp": datetime.now().isoformat(),
        }
        return replace(ctx, rules=rules, history=ctx.history + [history_entry])


class FeedbackStep(Step):
    def __init__(self, *, feedback_path: str):
        self.feedback_path = feedback_path

    def run(self, ctx: StepContext) -> StepContext:
        items = json.loads(Path(self.feedback_path).read_text())
        load_human_feedback(
            self.feedback_path,
            eval_dataset=ctx.dev_dataset,
            learner=ctx.learner,
            rules=ctx.rules,
        )
        rules = ctx.learner.apply_feedback_patch(ctx.rules, ctx.dev_dataset)
        history_entry = {
            "phase": "feedback",
            "dataset": ctx.split.name,
            "feedback_path": str(self.feedback_path),
            "num_items": len(items),
            "task_level": sum(1 for f in items if f.get("level", "task") == "task"),
            "rule_level": sum(1 for f in items if f.get("level") == "rule"),
            "timestamp": datetime.now().isoformat(),
        }
        return replace(
            ctx, rules=rules, best_rules=rules, history=ctx.history + [history_entry]
        )


class EvaluationStep(Step):
    def run(self, ctx: StepContext) -> StepContext:
        eval_results, t_eval = evaluate_test(ctx.dev_dataset, ctx.rules, ctx.learner)
        return replace(ctx, eval_results=eval_results, t_eval=t_eval)


CHECKPOINT_FILE = "checkpoint.json"


def build_context(
    args,
    split: DataSplit,
    storage_dir: str,
    checkpoint_path: Path | None = None,
    logger=None,
    rules: list | None = None,
) -> StepContext:
    learner = NERLearner(
        model=args.model,
        dataset_name=split.name,
        base_url=args.base_url,
        use_grex=not args.no_grex,
        max_rules=args.max_rules,
        max_samples=args.max_samples,
        max_counter_examples=args.max_counter_examples,
        agentic=args.agentic,
        enable_prune=args.enable_prune,
        audit_interval=args.audit_interval,
        enable_critic=args.enable_critic,
        critic_interval=args.critic_interval,
        logger=logger,
        storage_path=storage_dir,
        sampling_strategy=args.sampling_strategy,
        synthesis_strategy=args.synthesis_strategy,
        selected_classes=list(split.selected_classes),
    )
    eval_dataset = make_dataset(f"{split.name}_eval", split.eval, learner.task)
    dev_dataset = make_dataset(f"{split.name}_dev", split.dev, learner.task)
    return StepContext(
        rules=rules or [],
        split=split,
        learner=learner,
        eval_dataset=eval_dataset,
        dev_dataset=dev_dataset,
        checkpoint_path=checkpoint_path,
    )
