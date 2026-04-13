import json
import tempfile
import time
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from rulechef.core import Dataset, Example, Feedback
from rulechef.evaluation import evaluate_dataset
from rulechef.training_logger import TrainingDataLogger


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
    eval_results: Any
    t_learn: float
    t_eval: float
    rules: list
    selected_classes: set[str] | list[str]


def setup_output_paths(args, selected_classes):
    storage_dir = tempfile.mkdtemp(prefix="rulechef_bench_")

    model_name = args.model.replace("/", "_")
    date_str = datetime.now().strftime("%Y-%m-%d")
    selected_classes_str = "_".join(
        c.replace(" ", "") for c in selected_classes
    ).strip()
    num_classes = len(selected_classes)

    if args.rules_json:
        output_dir = Path(args.rules_json).parent
    else:
        base_dir = (
            Path(f"benchmarks/{args.dataset_name}/{model_name}") / selected_classes_str
        )
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
                input={"text": ex["text"]},
                expected_output={"entities": ex["entities"]},
                source="benchmark",
            )
        )
    return dataset


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


def add_feedback(eval_dataset, text, level="task", target=""):

    eval_dataset.structured_feedback.append(
        Feedback(
            id=str(uuid.uuid4())[:8],
            text=text,
            level=level,
            target_id=target,
        )
    )


def evaluate_test(test_data, test_dataset, rules, chef, mode="text", iou_threshold=1):
    print(f"\nEVALUATING ON HELD-OUT TEST SET ({len(test_data)} examples)...")
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


def print_results(run: BenchmarkRun):
    args = run.args
    # 9. Print results
    print(f"\n{'=' * 70}")
    print(f"German {args.dataset_name} Results")
    print(f"{'=' * 70}")
    print("  Configuration:")
    print(f"    Shots per class:          {args.shots}")
    print(f"    Training examples:        {len(run.train_data)}")
    print(f"    Test examples:            {len(run.test_data)}")
    print(f"    Model:                    {args.model}")
    print(f"    Max rules:                {args.max_rules}")
    print(f"    Max samples in prompt:    {args.max_samples}")
    print(f"    Refinement iterations:    {args.max_iterations}")
    print(f"    Seed:                     {args.seed}")
    print()
    print("  Results:")
    print(f"    Accuracy (exact match):   {run.eval_results.exact_match:.1%}")

    print(f"    Micro Precision:          {run.eval_results.micro_precision:.1%}")
    print(f"    Micro Recall:             {run.eval_results.micro_recall:.1%}")
    print(f"    Micro F1:                 {run.eval_results.micro_f1:.1%}")
    print(f"    Macro F1:                 {run.eval_results.macro_f1:.1%}")
    print()
    print("  Timing:")
    print(f"    Learning:                 {run.t_learn:.1f}s")
    print(f"    Evaluation:               {run.t_eval:.1f}s")
    print(
        f"    Per-query:                {run.t_eval / len(run.test_data) * 1000:.2f}ms"
    )
    print()
    print(f"  Rules:                      {len(run.rules)} total")
    print(f"{'=' * 70}")


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
            "train_size": len(run.train_data),
            "eval_size": len(run.eval_data),
            "test_size": len(run.test_data),
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
        },
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
