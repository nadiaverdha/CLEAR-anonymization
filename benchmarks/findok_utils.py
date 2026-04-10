import argparse
import datetime
import json
import os
import random
import tempfile
import time
import uuid
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Optional

import yaml
from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rulechef import RuleChef
from rulechef.coordinator import AgenticCoordinator
from rulechef.core import (
    Dataset,
    Example,
    Feedback,
    RuleFormat,
    Task,
    TaskType,
)
from rulechef.evaluation import evaluate_dataset, evaluate_rules_individually
from rulechef.training_logger import TrainingDataLogger

from benchmarks.findok_utils import *
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERDataset, NERSample
from clear_anonymization.utils.utils import *


# ── BenchmarkRun dataclass ─────────────────────────────────────────
@dataclass
class BenchmarkRun:
    args: Any
    train_data: list
    eval_data: list
    test_data: list
    train_annotations: int
    eval_annotations: int
    test_annotations: int
    iteration_metrics: list
    eval_results: Any
    t_learn: float
    t_eval: float
    rules: list


# ── Dataset loading ─────────────────────────────────────────


def load_findok(train_dir, val_dir):
    """Load Findok dataset(train, test, label_names)."""

    train_data = NERData.from_json(json.loads(Path(train_dir).read_text()))
    val_data = NERData.from_json(json.loads(Path(val_dir).read_text()))

    train = [sample for sample in train_data.samples]
    val = [sample for sample in val_data.samples]

    entity_definitions = get_dataset_class_definitions("findok")
    entity_names = set(entity_definitions.keys())

    return train, val, entity_names


def select_windows(text, entities, window_size=20):
    merged_windows = []
    for ent in entities:
        start = max(0, ent["start"] - window_size)
        end = min(len(text), ent["end"] + window_size)
        if merged_windows and start <= merged_windows[-1][1]:
            merged_windows[-1][1] = max(end, merged_windows[-1][1])
            merged_windows[-1][2].append(ent)
        else:
            merged_windows.append([start, end, [ent]])
    return merged_windows


def build_examples(text, merged_windows):
    examples = []
    for start, end, window_entities in merged_windows:
        snippet = text[start:end]
        adjusted_entities = [
            {
                "text": e["text"],
                "start": e["start"] - start,
                "end": e["end"] - start,
                "type": e["type"],
            }
            for e in window_entities
        ]
        examples.append({"text": snippet, "entities": adjusted_entities})
    return examples


def build_task(selected_classes):
    active_labels = sorted(selected_classes)
    task = Task(
        name="German Legal Named Entity Recognition",
        description=f"Recognize named entities in German legal text. Entities to look for: {', '.join(active_labels)}.",
        input_schema={"text": "str"},
        output_schema=NEROutput,
        type=TaskType.NER,
        text_field="text",
    )
    return task


def setup_rulechef(
    args, task, storage_dir, logger, train_data, counter_examples, dataset_name
):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY") or "EMPTY",
        base_url=args.base_url,
    )
    coordinator = None
    if args.agentic:
        coordinator = AgenticCoordinator(
            client,
            model=args.model,
            prune_after_learn=args.enable_prune,
            audit_interval=args.audit_interval,
            enable_critic=args.enable_critic,
            critic_interval=args.critic_interval,
            verbose=True,
        )
        print("Agentic coordinator: enabled")

    if args.synthesis_strategy != "bulk":
        train_for_chef = train_data + counter_examples
        random.Random(args.seed).shuffle(train_for_chef)
    else:
        train_for_chef = train_data

    chef = RuleChef(
        task=task,
        client=client,
        dataset_name=dataset_name,
        storage_path=storage_dir,
        allowed_formats=[RuleFormat.REGEX],
        model=args.model,
        use_grex=not args.no_grex,
        max_rules=args.max_rules,
        max_samples=args.max_samples,
        max_counter_examples=args.max_counter_examples,
        coordinator=coordinator,
        training_logger=logger,
        sampling_strategy=args.sampling_strategy,
        synthesis_strategy=args.synthesis_strategy,
    )

    return chef, train_for_chef


def setup_output_dir(args, selected_classes):
    storage_dir = tempfile.mkdtemp(prefix="rulechef_bench_")

    model_name = args.model.replace("/", "_")
    date_str = datetime.now().strftime("%Y-%m-%d")
    selected_classes_str = "_".join(
        c.replace(" ", "") for c in selected_classes
    ).strip()

    if args.rules_json:
        output_dir = Path(args.rules_json).parent
    else:
        base_dir = Path(f"benchmarks/findok/{model_name}") / selected_classes_str
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
            "benchmark": "findok",
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


def sample_few_shot(
    train_data,
    windows,
    seed=42,
    num_classes=None,
    classes=None,
    window_size=200,
    pool_size=None,
    shots_per_class=None,
    train_ratio=0.7,
    counter_examples_ratio=0.2,
):
    rng = random.Random(seed)

    use_filter = classes is not None

    if not classes:
        all_labels = sorted({l["type"] for sample in train_data for l in sample.labels})
        if num_classes and num_classes < len(all_labels):
            rng.shuffle(all_labels)
            classes = set(all_labels[:num_classes])
            use_filter = True
        else:
            classes = set(all_labels)

    classes = set(classes)

    all_examples = []
    negatives = []
    seen_texts = set()

    for sample in train_data:
        text = sample.text

        if use_filter:
            entities = sorted(
                [l for l in sample.labels if l["type"] in classes],
                key=lambda x: x["start"],
            )
        else:
            entities = list(sample.labels)

        if text in seen_texts:
            continue
        seen_texts.add(text)

        if not entities:
            other_entities = (
                [l for l in sample.labels if l["type"] not in classes]
                if use_filter
                else []
            )
            negatives.append({"text": text, "entities": other_entities})
            continue

        if windows:
            for ex in build_examples(text, select_windows(text, entities, window_size)):
                if ex["text"] not in seen_texts:
                    seen_texts.add(ex["text"])
                    all_examples.append(ex)
        else:
            all_examples.append({"text": text, "entities": entities})

    print(f"Total positives: {len(all_examples)}, negatives: {len(negatives)}")

    rng.shuffle(all_examples)
    rng.shuffle(negatives)
    pool = all_examples[:pool_size] if pool_size else all_examples

    split_idx = int(len(pool) * train_ratio)
    train_examples = pool[:split_idx]
    eval_examples = pool[split_idx:]

    print(f"Train: {len(train_examples)}, Eval: {len(eval_examples)}")

    return train_examples, eval_examples, negatives, classes


# ── Iteration callback ─────────────────────────────────────────


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


# ── Feedback ─────────────────────────────────────────
def add_feedback(eval_dataset, text, level="task", target=""):

    eval_dataset.structured_feedback.append(
        Feedback(
            id=str(uuid.uuid4())[:8],
            text=text,
            level=level,
            target_id=target,
        )
    )


# ── Evaluation ─────────────────────────────────────────


def evaluate_test(
    test_data, test_dataset, rules, chef, task, mode="text", iou_threshold=1
):
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
        },
        "results": {
            "accuracy": run.eval_results.exact_match,
            "coverage": run.eval_results.coverage,
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
            for cm in (run.test_eval.per_class or [])
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
