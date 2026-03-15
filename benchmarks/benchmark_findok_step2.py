import argparse
import json
import os
import random
import uuid
from collections import defaultdict
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field

from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData

from openai import OpenAI
from rulechef import RuleChef
from rulechef.core import Dataset, Example, Feedback, Rule, RuleFormat, Task, TaskType
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERDataset, NERSample
from rulechef.evaluation import evaluate_rules_individually
from clear_anonymization.utils.utils import *
from benchmarks.benchmark_findok import (
    load_findok,
    select_windows,
    build_examples,
    sample_few_shot,
)


# ─────────────────────────────────────────────────────────────
# Refinement
# ─────────────────────────────────────────────────────────────


def run_refine(args):

    print(f"Loading previous run: {args.rules_json}")

    saved = json.loads(Path(args.rules_json).read_text())
    config = saved["config"]

    # Rebuild rules
    rules = []

    for r in saved["rules"]:
        rules.append(
            Rule(
                id=str(uuid.uuid4())[:8],
                name=r["name"],
                description=r.get("description", r["name"]),
                format=RuleFormat(r["format"]),
                content=r["content"],
                priority=r.get("priority", 5),
                output_template=r.get("output_template"),
                output_key=r.get("output_key"),
            )
        )

    print(f"Loaded {len(rules)} rules")

    # 1. Load data
    print("Loading FinDok dataset...")
    train_all, test_all, entity_names = load_findok(args.train_dir, args.val_dir)
    entity_definitions = get_dataset_class_definitions("findok")
    print(
        f"  Train: {len(train_all)}, Test: {len(test_all)}, Classes: {len(entity_names)}"
    )

    # 2. Few-shot sample (optionally limited to N classes)

    classes = [c.strip() for c in args.classes.split(",")] if args.classes else None
    train_sample, train_remaining, selected_classes = sample_few_shot(
        train_all,
        shots_per_class=args.shots,
        seed=42,
        num_classes=args.num_classes,
        classes=classes,
        windows=False,
    )

    num_classes = len(selected_classes)
    print(
        f"  Few-shot: {args.shots}-shot x {num_classes} classes = {len(train_sample)} examples"
    )
    print(f"  Eval pool (unused train): {len(train_remaining)} examples")
    if args.num_classes:
        print(f"  Selected classes: {', '.join(sorted(selected_classes))}")

    # Filter test set to only selected classes (held out — never seen during learning)
    filtered = []
    for ex in test_all:
        kept_labels = [
            label for label in ex.labels if label["type"] in selected_classes
        ]
        if kept_labels:
            filtered.append(NERSample(text=ex.text, split=ex.split, labels=kept_labels))

    # 3. Configure rulechef
    active_labels = sorted(selected_classes)
    task = Task(
        name="German LER Named Entity Recognition",
        description=f"Recognize named entities in German legal text. Entities: {', '.join(active_labels)}.",
        input_schema={"text": "str"},
        output_schema=NEROutput,
        type=TaskType.NER,
        text_field="text",
    )

    # Build eval dataset
    eval_dataset = Dataset(name="findok_eval", task=task)

    for ex in train_remaining:
        eval_dataset.examples.append(
            Example(
                id=str(uuid.uuid4())[:8],
                input={"text": ex["text"]},
                expected_output={"entities": ex["entities"]},
                source="benchmark",
            )
        )

    # Feedback helper
    def add_feedback(text, level="task", target=""):

        eval_dataset.structured_feedback.append(
            Feedback(
                id=str(uuid.uuid4())[:8],
                text=text,
                level=level,
                target_id=target,
            )
        )

    # Load human feedback
    if args.feedback:
        feedback_items = json.loads(Path(args.feedback).read_text())

        print(f"Loading {len(feedback_items)} feedback items")

        for fb in feedback_items:
            level = fb.get("level", "task")
            text = fb["text"]
            target_id = ""

            if level == "rule":
                rule_name = fb.get("rule_name", "")

                def _norm(s):
                    return s.replace("\u2011", "-").replace("\u2010", "-")

                matched = next(
                    (r for r in rules if _norm(r.name) == _norm(rule_name)), None
                )

                if matched:
                    target_id = matched.id
                else:
                    print(f"Rule not found: {rule_name}")
                    level = "task"

            add_feedback(text, level, target_id)

    # RuleChef
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY") or "EMPTY",
        base_url=args.base_url,
    )

    chef = RuleChef(
        task=task,
        client=client,
        dataset_name="findok_refine",
        storage_path="./rulechef_storage",
        allowed_formats=[RuleFormat.REGEX],
        model=args.model,
        max_rules=config["max_rules"],
        max_samples=config["max_samples"],
    )

    # Evaluate rules for auto feedback
    print("Analyzing rules...")

    rule_metrics = evaluate_rules_individually(
        rules=rules,
        dataset=eval_dataset,
        apply_rules_fn=chef.learner._apply_rules,
        mode="text",
        max_samples=5,
    )

    for rm in rule_metrics:
        rule = next((r for r in rules if r.id == rm.rule_id), None)

        if not rule:
            continue

        if rm.matches > 0 and rm.precision == 0.0:
            add_feedback(
                f"Rule '{rule.name}' is pure noise ({rm.false_positives} false positives). Remove or tighten.",
                level="rule",
                target=rule.id,
            )

        elif rm.matches > 3 and rm.precision < 0.2:
            add_feedback(
                f"Rule '{rule.name}' is too broad (precision {rm.precision:.0%}). Tighten it.",
                level="rule",
                target=rule.id,
            )

        elif rm.matches == 0:
            add_feedback(
                f"Rule '{rule.name}' never fires. Check regex.",
                level="rule",
                target=rule.id,
            )

    # Run refinement
    print(f"Refining rules (max {args.max_iterations} iterations)...")

    rules, refine_eval = chef.learner.evaluate_and_refine(
        rules,
        eval_dataset,
        max_iterations=args.max_iterations,
    )

    if refine_eval:
        print(f"Eval micro F1: {refine_eval.micro_f1:.1%}")

    # Save
    output = {
        "config": config,
        "rules": [
            {
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

    Path(args.output).write_text(json.dumps(output, indent=2))

    print(f"Saved to {args.output}")


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--rules-json", required=True)
    parser.add_argument("--train_dir", required=True)
    parser.add_argument("--val_dir", required=True)
    parser.add_argument(
        "--shots",
        type=int,
        default=20,
        help="Examples per intent class for training (default: 5)",
    )

    parser.add_argument(
        "--model",
        type=str,
        default="openai/gpt-oss-120b",  # "google/gemma-3-27b-it",
        help="LLM model for rule synthesis (default: openai/gpt-oss-120b)",
    )
    parser.add_argument("--base-url", default="http://localhost:8000/v1")
    parser.add_argument(
        "--format",
        type=str,
        default="regex",
        choices=["regex", "code", "both"],
        help="Rule format (default: regex)",
    )
    parser.add_argument(
        "--num-classes",
        type=int,
        default=None,
        help="Limit to N random classes (default: all 7)",
    )
    parser.add_argument(
        "--classes",
        type=str,
        default=None,
        help="Comma-separated list of specific class names to use (overrides --num-classes)",
    )

    parser.add_argument("--max-iterations", type=int, default=3)
    parser.add_argument("--feedback", default=None)

    parser.add_argument("--output", default="benchmarks/results_findok_refined.json")

    args = parser.parse_args()

    run_refine(args)


if __name__ == "__main__":
    main()
