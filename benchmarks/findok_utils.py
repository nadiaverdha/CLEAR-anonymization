import argparse
import json
import os
import random
import time
import uuid
from collections import defaultdict
from pathlib import Path
from typing import List, Optional

from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rulechef import RuleChef
from rulechef.core import (
    Dataset,
    Example,
    Feedback,
    Rule,
    RuleFormat,
    Task,
    TaskType,
)
from rulechef.evaluation import evaluate_dataset, evaluate_rules_individually

from benchmarks.findok_utils import *
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERDataset, NERSample
from clear_anonymization.utils.utils import *

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


def select_windows(text, entities, window_size=200):
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


def sample_few_shot(
    train_data,
    shots_per_class,
    windows,
    seed=42,
    num_classes=None,
    classes=None,
    window_size=200,
):
    rng = random.Random(seed)
    if not classes:
        all_labels = sorted({l["type"] for sample in train_data for l in sample.labels})
        if num_classes and num_classes < len(all_labels):
            rng.shuffle(all_labels)
            classes = set(sorted(all_labels[:num_classes]))
        else:
            classes = set(all_labels)

    classes = set(classes)

    all_examples = []
    for sample in train_data:
        text = sample.text
        entities = sorted(
            [l for l in sample.labels if l["type"] in classes],
            key=lambda x: x["start"],
        )
        if not entities:
            continue
        if windows:
            all_examples.extend(
                build_examples(text, select_windows(text, entities, window_size))
            )
        else:
            all_examples.append({"text": text, "entities": entities})

    by_label = defaultdict(list)
    for ex in all_examples:
        for ent in ex["entities"]:
            by_label[ent["type"]].append(ex)
    labels = sorted(classes & set(by_label.keys()))
    missing = classes - set(by_label.keys())
    if missing:
        print(f"WARNING: classes not found in dataset: {missing}")

    sampled = []
    remaining = []

    for label in labels:
        examples = by_label[label]
        seen = set()
        unique = []
        for ex in examples:
            if ex["text"] not in seen:
                seen.add(ex["text"])
                unique.append(ex)
        rng.shuffle(unique)
        sampled.extend(unique[:shots_per_class])
        remaining.extend(unique[shots_per_class:])

    return sampled, remaining, classes


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


# ── Add Feedback ─────────────────────────────────────────
def add_feedback(eval_dataset, text, level="task", target=""):

    eval_dataset.structured_feedback.append(
        Feedback(
            id=str(uuid.uuid4())[:8],
            text=text,
            level=level,
            target_id=target,
        )
    )


# ── Test Eval ─────────────────────────────────────────


def evaluate_test(test_data, rules, chef, task):
    test_dataset = Dataset(name="findok_test", task=task)
    for ex in test_data:
        test_dataset.examples.append(
            Example(
                id=str(uuid.uuid4())[:8],
                input={"text": ex.text},
                expected_output={"entities": ex.labels},
                source="benchmark",
            )
        )

    print(f"\nEVALUATING ON HELD-OUT TEST SET ({len(test_data)} examples)...")
    t0 = time.time()
    test_eval = evaluate_dataset(
        rules,
        test_dataset,
        chef.learner._apply_rules,
    )
    t_eval = time.time() - t0

    # Coverage = what % of test queries got ANY prediction (TP + FP) / total
    coverage = (
        (test_eval.total_tp + test_eval.total_fp) / len(test_data) if test_data else 0
    )
    return test_eval, coverage, t_eval


# ── Save results ─────────────────────────────────────────
def save_results(
    output_path,
    shots,
    model,
    format,
    max_rules,
    max_samples,
    max_iterations,
    seed,
    train_sample,
    test_data,
    no_grex,
    agentic,
    test_eval,
    iteration_metrics,
    coverage,
    t_learn,
    t_eval,
    rules,
):
    results = {
        "config": {
            "shots": shots,
            "model": model,
            "format": format,
            "max_rules": max_rules,
            "max_samples": max_samples,
            "max_iterations": max_iterations,
            "seed": seed,
            "train_size": len(train_sample),
            "test_size": len(test_data),
            "use_grex": not no_grex,
            "agentic": agentic,
        },
        "results": {
            "accuracy": test_eval.exact_match,
            "coverage": coverage,
            "micro_precision": test_eval.micro_precision,
            "micro_recall": test_eval.micro_recall,
            "micro_f1": test_eval.micro_f1,
            "macro_f1": test_eval.macro_f1,
            "num_rules": len(rules),
            "learning_time_s": round(t_learn, 1),
            "eval_time_s": round(t_eval, 3),
            "per_query_ms": round(t_eval / len(test_data) * 1000, 2),
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
            for cm in (test_eval.per_class or [])
        ],
        "iteration_metrics": iteration_metrics,
        "rules": [
            {
                "id": r.id,
                "name": r.name,
                "format": r.format.value,
                "content": r.content,
                "priority": r.priority,
                "output_template": r.output_template,
                "output_key": r.output_key,
            }
            for r in rules
        ],
    }
    output_path.write_text(json.dumps(results, indent=2))
    print(f"\nResults saved to {output_path}")
