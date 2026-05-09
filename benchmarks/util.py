import json
import tempfile
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from rulechef.core import Dataset, Example, Feedback, Rule, RuleFormat
from rulechef.evaluation import evaluate_dataset, evaluate_rules_individually
from rulechef.training_logger import TrainingDataLogger

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.preprocess.create_train_dev_split import (
    label_distribution_sent,
    print_distribution,
)
from clear_anonymization.preprocess.sampling import sample_few_shot

# ── Experiment data ──────────────────────────────────────────


@dataclass
class DataSplit:
    """Sampled, train/eval/dev-split data ready for a learning phase."""

    name: str
    train: list
    eval: list
    dev: list
    counter_examples: list
    selected_classes: set
    n_train_docs: int
    n_eval_docs: int
    n_test_docs: int


@dataclass
class BenchmarkRun:
    args: Any
    train_data: list
    eval_data: list
    test_data: list
    train_size: int
    eval_size: int
    test_size: int
    train_annotations: int
    eval_annotations: int
    test_annotations: int
    iteration_metrics: list
    batch_test_metrics: list
    eval_results: Any
    t_learn: float
    t_eval: float
    rules: list
    selected_classes: set[str] | list[str]
    metadata: dict = field(default_factory=dict)


def prepare_split(
    args,
    *,
    name: str,
    train_dir: str,
    test_dir: str | None = None,
    classes: str | None = None,
    fallback_dev: list | None = None,
) -> DataSplit:
    """Load and sample one dataset into a DataSplit ready for training."""
    print(f"\nLoading {name} dataset...")
    train_all = load_ner_dataset_from_conll(train_dir)

    dev_all = load_ner_dataset_from_conll(test_dir) if test_dir else None

    class_list = [c.strip() for c in classes.split(",")] if classes else None

    (
        train,
        eval_,
        counter_examples,
        selected_classes,
        n_train_docs,
        n_eval_docs,
    ) = sample_few_shot(
        train_data=train_all.samples,
        seed=args.seed,
        num_classes=args.num_classes,
        classes=class_list,
        pool_size=args.pool_size,
        train_ratio=args.train_ratio,
    )
    if dev_all:
        dev = [
            {
                "doc_id": s.doc_id,
                "sent_id": sent.sent_id,
                "text": sent.text,
                "entities": sent.labels,
            }
            for s in dev_all.samples
            for sent in s.sentences
        ]
        n_test_docs = len(dev_all.samples)
        dev_label = f"{n_test_docs} source docs"
    elif fallback_dev is not None:
        dev = fallback_dev
        n_test_docs = len(dev)
        dev_label = "reusing phase 1 dev"
    else:
        raise ValueError(f"prepare_split({name!r}): provide test_dir or fallback_dev")

    print(f"{'─' * 70}")
    print(f"Source docs — train: {len(train_all.samples)}, dev: {dev_label}")
    print(f"Sampled     — train docs: {n_train_docs}, eval docs: {n_eval_docs}")
    print(f"Sentences   — train: {len(train)}, eval: {len(eval_)}, dev: {len(dev)}")
    print_distribution(train, "TRAIN", fn=label_distribution_sent)
    print_distribution(eval_, "EVAL", fn=label_distribution_sent)
    print(
        f"Classes     — {len(selected_classes)}: {', '.join(sorted(selected_classes))}"
    )
    print(f"{'─' * 70}")

    return DataSplit(
        name=name,
        train=train,
        eval=eval_,
        dev=dev,
        counter_examples=counter_examples,
        selected_classes=selected_classes,
        n_train_docs=n_train_docs,
        n_eval_docs=n_eval_docs,
        n_test_docs=n_test_docs,
    )


def setup_output_paths(args, selected_classes):
    storage_dir = tempfile.mkdtemp(prefix="rulechef_bench_")

    model_name = args.model.replace("/", "_")
    date_str = datetime.now().strftime("%Y-%m-%d")
    selected_classes_str = "_".join(
        c.replace(" ", "") for c in selected_classes
    ).strip()
    num_classes = len(selected_classes)

    base_dir = Path(f"reports/{args.dataset_name}/{model_name}") / selected_classes_str
    base_name = date_str

    output_dir = base_dir / base_name
    if output_dir.exists():
        version = 1
        while (base_dir / f"{base_name}_v{version}").exists():
            version += 1
        output_dir = base_dir / f"{base_name}_v{version}"

    output_dir.mkdir(parents=True, exist_ok=True)

    out_name = Path(args.output)
    if args.rules_json:
        out_name = out_name.with_stem(out_name.stem + "_refined")

    log_path = (output_dir / out_name).with_suffix(".training.jsonl")
    logger = TrainingDataLogger(
        str(log_path),
        run_metadata={
            "benchmark": args.dataset_name,
            "model": args.model,
            "format": args.format,
            "num_classes": num_classes,
        },
    )
    print(f"Training log: {log_path}")

    config_path = output_dir / "config.yaml"
    config_dict = {
        k.replace("_", "-"): v for k, v in vars(args).items() if k not in ("config",)
    }
    with open(config_path, "w") as f:
        yaml.dump(config_dict, f, default_flow_style=False, allow_unicode=True)
    print(f"Config saved to {config_path}")

    return storage_dir, output_dir, out_name, logger


def make_dataset(dataset_name, data, task):
    dataset = Dataset(name=dataset_name, task=task)
    for ex in data:
        dataset.examples.append(
            Example(
                id=str(uuid.uuid4())[:8],
                input={
                    "doc_id": ex.get("doc_id", ""),
                    "sent_id": ex.get("sent_id", ""),
                    "text": ex["text"],
                    "sentences": ex.get("sentences", []),
                },
                expected_output={"entities": ex["entities"]},
                source="benchmark",
            )
        )
    return dataset


def serialize_rules(rules) -> list:
    return [
        {
            "id": r.id,
            "name": r.name,
            "description": r.description,
            "format": r.format.value,
            "content": r.content,
            "priority": r.priority,
            "output_template": r.output_template,
            "output_key": r.output_key,
        }
        for r in rules
    ]


def deserialize_rules(rules_list: list) -> list:
    return [
        Rule(
            id=r["id"],
            name=r["name"],
            description=r.get("description", r["name"]),
            format=RuleFormat(r["format"]),
            content=r["content"],
            priority=r.get("priority", 5),
            output_template=r.get("output_template"),
            output_key=r.get("output_key"),
        )
        for r in rules_list
    ]


def save_checkpoint(path: Path, data: dict):
    tmp = path.with_suffix(".cp_tmp")
    tmp.write_text(json.dumps(data, indent=2))
    tmp.replace(path)


def load_checkpoint(path: Path) -> dict:
    return json.loads(path.read_text())


def load_rules_from_json(path: str | Path) -> list:
    saved = json.loads(Path(path).read_text())
    return deserialize_rules(saved["rules"])


def make_oniteration_callback(iteration_metrics: list):
    """
    Returns a callback function suitable for RuleChef's iteration_callback.
    Logs per-iteration metrics into the provided iteration_metrics list.
    """

    def on_iteration(iteration, iter_rules, eval_result):
        iteration_metrics.append(
            {
                "iteration": iteration,
                "num_rules": len(iter_rules),
                "exact_match": eval_result.exact_match,
                "micro_precision": eval_result.micro_precision,
                "micro_recall": eval_result.micro_recall,
                "micro_f1": eval_result.micro_f1,
                "macro_f1": eval_result.macro_f1,
                "per_class": [
                    {
                        "label": cm.label,
                        "f1": cm.f1,
                        "precision": cm.precision,
                        "recall": cm.recall,
                    }
                    for cm in (eval_result.per_class or [])
                ],
            }
        )

    return on_iteration


def load_human_feedback_v2(feedback_path, eval_dataset, learner, rules=None):
    def _norm(s):
        return s.replace("\u2011", "-").replace("\u2010", "-")

    feedback_items = json.loads(Path(feedback_path).read_text())
    print(f"  Loading {len(feedback_items)} human feedback items")
    for fb in feedback_items:
        level = fb.get("level", "task")
        text = fb["text"]
        target_id = ""
        if level == "rule" and rules is not None:
            rule_name = fb.get("rule_name", "")
            matched = next(
                (r for r in rules if _norm(r.name) == _norm(rule_name)), None
            )
            if matched:
                target_id = matched.id
            else:
                print(f"Rule not found: {rule_name} — treating as task-level")
                level = "task"
        eval_dataset.structured_feedback.append(
            Feedback(
                id=str(uuid.uuid4())[:8],
                text=text,
                level=level,
                target_id=target_id,
            )
        )
        learner.add_feedback(text, level, target_id)


def load_human_feedback(feedback_path, eval_dataset, learner, rules=None):
    def _norm(s):
        return s.replace("\u2011", "-").replace("\u2010", "-")

    feedback_items = json.loads(Path(feedback_path).read_text())
    print(f"  Loading {len(feedback_items)} human feedback items")
    for fb in feedback_items:
        level = fb.get("level", "task")
        text = fb["text"]
        target_id = ""
        eval_dataset.structured_feedback.append(
            Feedback(
                id=str(uuid.uuid4())[:8],
                text=text,
                level=level,
                target_id=target_id,
            )
        )
        learner.add_feedback(text, level, target_id)


def evaluate_test(test_dataset, rules, chef, mode="text", iou_threshold=1):
    t0 = time.time()
    eval_results = evaluate_dataset(
        rules,
        test_dataset,
        chef.learner._apply_rules,
        mode=mode,
        iou_threshold=iou_threshold,
    )
    t_eval = time.time() - t0

    return eval_results, t_eval


# ── Save results ─────────────────────────────────────────
def save_results(output_path: Path, run: BenchmarkRun):
    args = run.args
    results = {
        "config": {
            "shots": args.shots,
            "model": args.model,
            "format": args.format,
            "max_rules": args.max_rules,
            "max_samples": args.max_samples,
            "max_iterations": args.max_iterations,
            "seed": args.seed,
            "train_size": run.train_size,
            "eval_size": run.eval_size,
            "test_size": run.test_size,
            "train_annotations": run.train_annotations,
            "eval_annotations": run.eval_annotations,
            "test_annotations": run.test_annotations,
            "use_grex": not args.no_grex,
            "agentic": args.agentic,
            "enable_critic": args.enable_critic,
            "enable_prune": args.enable_prune,
            "critic_interval": args.critic_interval,
            "audit_interval": args.audit_interval,
            "windows": args.windows,
            "sampling_strategy": args.sampling_strategy,
            "train_ratio": args.train_ratio,
            "pool_size": args.pool_size,
            "batch_size": args.batch_size,
            "refine_per_batch": args.refine_per_batch,
            "synthesis_strategy": args.synthesis_strategy,
            "selected_classes": run.selected_classes,
            "dataset_name": args.dataset_name,
            "max_counter_examples": args.max_counter_examples,
            "refine_every": args.refine_every,
        },
        "metadata": run.metadata,
        "results": {
            "accuracy": run.eval_results.exact_match,
            "micro_precision": run.eval_results.micro_precision,
            "micro_recall": run.eval_results.micro_recall,
            "micro_f1": run.eval_results.micro_f1,
            "macro_f1": run.eval_results.macro_f1,
            "num_rules": len(run.rules),
            "learning_time_s": round(run.t_learn, 1),
            "eval_time_s": round(run.t_eval, 3),
            "per_query_ms": round(run.t_eval / len(run.test_data) * 1000, 2),
        },
        "per_class": [
            {
                "label": cm.label,
                "precision": cm.precision,
                "recall": cm.recall,
                "f1": cm.f1,
                "tp": cm.tp,
                "fp": cm.fp,
                "fn": cm.fn,
            }
            for cm in (run.eval_results.per_class or [])
        ],
        "iteration_metrics": run.iteration_metrics,
        "batch_test_metrics": run.batch_test_metrics,
        "rules": [
            {
                "id": r.id,
                "name": r.name,
                "description": r.description,
                "format": r.format.value,
                "content": r.content,
                "priority": r.priority,
                "output_template": r.output_template,
                "output_key": r.output_key,
                "created_at": r.created_at.isoformat(),
            }
            for r in run.rules
        ],
    }
    output_path.write_text(json.dumps(results, indent=2))
    print(f"\nResults saved to {output_path}")
    return results


def print_results(run: BenchmarkRun):
    args = run.args
    # 9. Print results
    print(f"\n{'=' * 70}")
    print(f"German {args.dataset_name} Results")
    print(f"{'=' * 70}")
    print("Configuration:")
    print(f"Shots per class:          {args.shots}")
    print(f"Training examples:        {len(run.train_data)} ")
    print(f"Test examples:            {len(run.test_data)}")
    print(f"Model:                    {args.model}")
    print(f"Max rules:                {args.max_rules}")
    print(f"Max samples in prompt:    {args.max_samples}")
    print(f"Refinement iterations:    {args.max_iterations}")
    print(f"Seed:                     {args.seed}")
    print()

    print("Results:")
    print(f"Accuracy (exact match):   {run.eval_results.exact_match:.1%}")

    print(f"Micro Precision:          {run.eval_results.micro_precision:.1%}")
    print(f"Micro Recall:             {run.eval_results.micro_recall:.1%}")
    print(f"Micro F1:                 {run.eval_results.micro_f1:.1%}")
    print(f"Macro F1:                 {run.eval_results.macro_f1:.1%}")
    print()
    print("Timing:")
    print(f"Learning:                 {run.t_learn:.1f}s")
    print(f"Evaluation:               {run.t_eval:.1f}s")
    print(f"Per-query:                {run.t_eval / len(run.test_data) * 1000:.2f}ms")
    print()
    print(f"Rules:                      {len(run.rules)} total")
    print(f"{'=' * 70}")


def print_rule_summary(rules):
    print(f"\n{'─' * 70}")
    print("RULES LEARNED:")
    print(f"{'─' * 70}")
    for r in sorted(rules, key=lambda r: -r.priority):
        content_preview = r.content.replace("\n", " ")[:100]
        print(f"  [p={r.priority}] {r.name}: {content_preview}")
    print(f"{'─' * 70}")


def print_per_class_breakdown(eval_results):
    if not eval_results.per_class:
        return
    sorted_classes = sorted(eval_results.per_class, key=lambda c: c.f1, reverse=True)
    print("\n  Top 10 classes by F1:")
    for cm in sorted_classes[:10]:
        print(
            f"    {cm.label:50s} F1={cm.f1:.0%} P={cm.precision:.0%} R={cm.recall:.0%} "
            f"(TP={cm.tp} FP={cm.fp})"
        )
    print("\n  Bottom 10 classes by F1:")
    for cm in sorted_classes[-10:]:
        print(
            f"    {cm.label:50s} F1={cm.f1:.0%} P={cm.precision:.0%} R={cm.recall:.0%} "
            f"(TP={cm.tp} FP={cm.fp})"
        )
