import random
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from benchmarks.util import (
    evaluate_test,
    make_dataset,
    make_oniteration_callback,
    save_checkpoint,
    serialize_rules,
)
from clear_anonymization.models.nerlearner import NERLearner

CHECKPOINT_FILE = "checkpoint.json"


@dataclass
class TrainingSession:
    args: Any
    storage_dir: str
    rules: list = field(default_factory=list)
    history: list[dict] = field(default_factory=list)
    checkpoint_path: Path | None = None

    def __post_init__(self):
        self._learner = None
        self._eval_dataset = None
        self._dev_dataset = None
        self._split = None

    def _build_learner(self, split, logger=None) -> NERLearner:
        a = self.args
        return NERLearner(
            model=a.model,
            dataset_name=split.name,
            base_url=a.base_url,
            use_grex=not a.no_grex,
            max_rules=a.max_rules,
            max_samples=a.max_samples,
            max_counter_examples=a.max_counter_examples,
            agentic=a.agentic,
            enable_prune=a.enable_prune,
            audit_interval=a.audit_interval,
            enable_critic=a.enable_critic,
            critic_interval=a.critic_interval,
            logger=logger,
            storage_path=self.storage_dir,
            sampling_strategy=a.sampling_strategy,
            synthesis_strategy=a.synthesis_strategy,
            selected_classes=list(split.selected_classes),
        )

    def _prepare_split(self, split, logger=None):
        self._learner = self._build_learner(split, logger)
        self._split = split
        self._eval_dataset = make_dataset(
            f"{split.name}_eval", split.eval, self._learner.task
        )
        self._dev_dataset = make_dataset(
            f"{split.name}_dev", split.dev, self._learner.task
        )

    def train(
        self,
        split,
        *,
        logger=None,
        skip_synthesis=False,
        start_batch=0,
        prev_batch_metrics=None,
        prev_iteration_metrics=None,
        prev_t_learn=None,
        phase: str = "phase1",
    ):
        self._prepare_split(split, logger)
        a = self.args

        if a.synthesis_strategy != "bulk":
            train_for_chef = split.train + split.counter_examples
            random.Random(a.seed).shuffle(train_for_chef)
        else:
            train_for_chef = split.train

        batch_metrics = list(prev_batch_metrics) if prev_batch_metrics else []
        iteration_metrics = (
            list(prev_iteration_metrics) if prev_iteration_metrics else []
        )
        t_learn = prev_t_learn if prev_t_learn else 0.0
        on_iteration = make_oniteration_callback(iteration_metrics)

        def on_batch(batch_idx, rules):
            result, _ = evaluate_test(self._dev_dataset, rules, self._learner)
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
            print(
                f"  [batch {batch_idx}] dev micro_f1={result.micro_f1:.3f}"
                f"  P={result.micro_precision:.3f}  R={result.micro_recall:.3f}"
            )
            if self.checkpoint_path:
                save_checkpoint(
                    self.checkpoint_path,
                    {
                        "phase": phase,
                        "completed_batches": batch_idx + 1,
                        "rules": serialize_rules(rules),
                        "batch_metrics": batch_metrics,
                        "iteration_metrics": iteration_metrics,
                        "timestamp": datetime.now().isoformat(),
                    },
                )

        if skip_synthesis and self.rules:
            print(f"\nSkipping synthesis — using {len(self.rules)} existing rules.")
            rules = list(self.rules)
        else:
            fit_result = self._learner.fit_batched(
                train_for_chef,
                eval_dataset=self._eval_dataset if a.refine_per_batch > 0 else None,
                batch_size=a.batch_size,
                refine_per_batch=a.refine_per_batch,
                refine_every=a.refine_every,
                iteration_callback=on_iteration,
                batch_callback=on_batch,
                audit_interval=a.audit_interval,
                seed_rules=self.rules or None,
                start_batch=start_batch,
            )
            if fit_result is None:
                return batch_metrics, iteration_metrics, t_learn
            rules, new_t_learn = fit_result
            t_learn += new_t_learn

        self.rules = rules
        self.history.append(
            {
                "phase": "train",
                "dataset": split.name,
                "num_rules": len(rules),
                "t_learn": round(t_learn, 1),
                "timestamp": datetime.now().isoformat(),
                "num_train_docs": len(split.train),
                "num_eval_docs": len(split.eval),
                "num_train_annotations": sum(len(s["entities"]) for s in split.train),
                "num_eval_annotations": sum(len(s["entities"]) for s in split.eval),
                "batch_metrics": batch_metrics,
                "iteration_metrics": iteration_metrics,
            }
        )
        return batch_metrics, iteration_metrics, t_learn

    def refine(self, split=None):
        if split is not None and split is not self._split:
            self._prepare_split(split)

        if self._learner is None:
            raise RuntimeError("Call train() before refine().")

        a = self.args
        iteration_metrics = []
        on_iteration = make_oniteration_callback(iteration_metrics)

        print(
            f"\nRefining {len(self.rules)} rules"
            f" ({len(self._split.eval)} eval examples,"
            f" max {a.max_iterations} iterations)..."
        )
        rules, refine_eval = self._learner.refine(
            self.rules,
            self._eval_dataset,
            max_iterations=a.max_iterations,
            iteration_callback=on_iteration,
        )
        self.rules = rules
        self.history.append(
            {
                "phase": "refine",
                "dataset": self._split.name,
                "num_rules": len(rules),
                "micro_f1": refine_eval.micro_f1 if refine_eval else None,
                "micro_precision": refine_eval.micro_precision if refine_eval else None,
                "micro_recall": refine_eval.micro_recall if refine_eval else None,
                "iteration_metrics": iteration_metrics,
                "timestamp": datetime.now().isoformat(),
            }
        )

        if refine_eval:
            print(f"  Eval micro F1: {refine_eval.micro_f1:.1%}")

    def evaluate(self, split=None):
        if split is not None and split is not self._split:
            self._prepare_split(split)

        if self._learner is None:
            raise RuntimeError("Call train() before evaluate().")

        return evaluate_test(self._dev_dataset, self.rules, self._learner)
