import argparse
import json
import os
import random
import tempfile
import uuid
from collections import defaultdict
from pathlib import Path
from typing import List

from openai import OpenAI
from pydantic import BaseModel, Field
from rulechef import RuleChef
from rulechef.core import Dataset, Example, Feedback, Rule, RuleFormat, Task, TaskType
from rulechef.evaluation import evaluate_rules_individually
from rulechef.training_logger import TrainingDataLogger

from benchmarks.findok_utils import *
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERDataset, NERSample
from clear_anonymization.utils.utils import *
from reports.create_md_report_rules import append_rule_metrics, create_md_report

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
                id=r["id"],
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

    # Filter test set to only selected classes (held out — never seen during learning)
    filtered = []
    for ex in test_all:
        kept_labels = [
            label for label in ex.labels if label["type"] in selected_classes
        ]
        if kept_labels:
            filtered.append(NERSample(text=ex.text, split=ex.split, labels=kept_labels))
    test_data = filtered
    if args.test_limit:
        rng = random.Random(args.seed)
        test_data = list(test_data)
        rng.shuffle(test_data)
        test_data = test_data[: args.test_limit]
        print(f"  Test subset: {len(test_data)} (limited, held out)")
    else:
        print(f"  Test: {len(test_data)} (filtered to selected classes, held out)")

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

            add_feedback(eval_dataset, text, level, target_id)

    # RuleChef
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY") or "EMPTY",
        base_url=args.base_url,
    )

    storage_dir = tempfile.mkdtemp(prefix="rulechef_bench_")

    # Training logger
    model_name = args.model.replace("/", "_")
    log_path = Path(f"{args.output}_{model_name}").with_suffix(".training.jsonl")
    logger = TrainingDataLogger(
        str(log_path),
        run_metadata={
            "benchmark": "findok",
            "model": args.model,
            "format": args.format,
            "num_classes": num_classes,
        },
    )
    print(f"  Training log: {log_path}")

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
                eval_dataset,
                f"Rule '{rule.name}' is pure noise ({rm.false_positives} false positives). Remove or tighten.",
                level="rule",
                target=rule.id,
            )

        elif rm.matches > 3 and rm.precision < 0.2:
            add_feedback(
                eval_dataset,
                f"Rule '{rule.name}' is too broad (precision {rm.precision:.0%}). Tighten it.",
                level="rule",
                target=rule.id,
            )

        elif rm.matches == 0:
            add_feedback(
                eval_dataset,
                f"Rule '{rule.name}' never fires. Check regex.",
                level="rule",
                target=rule.id,
            )

    # Run refinement
    print(f"Refining rules (max {args.max_iterations} iterations)...")

    # 7. Refine against eval set (unused training data), test set stays held out
    iteration_metrics = []
    on_iteration = make_oniteration_callback(iteration_metrics)

    if args.max_iterations > 0:
        print(
            f"\nRefining against eval set ({len(train_remaining)} examples, max {args.max_iterations} iterations)..."
        )
        t0_refine = time.time()
        rules, refine_eval = chef.learner.evaluate_and_refine(
            rules,
            eval_dataset,
            max_iterations=args.max_iterations,
            coordinator=chef.coordinator,
            iteration_callback=on_iteration,
        )
        t_refine = time.time() - t0_refine
        t_learn = t_refine
        print(f"Refinement complete ({t_refine:.1f}s)")
        if refine_eval:
            print(
                f"  Eval accuracy: {refine_eval.exact_match:.1%}, eval micro F1: {refine_eval.micro_f1:.1%}"
            )

    # 8. Print rule summary
    print(f"\n{'─' * 70}")
    print("RULES LEARNED:")
    print(f"{'─' * 70}")
    for r in sorted(rules, key=lambda r: -r.priority):
        content_preview = r.content.replace("\n", " ")[:100]
        print(f"  [p={r.priority}] {r.name}: {content_preview}")
    print(f"{'─' * 70}")

    # Build held-out test Dataset for final evaluation
    test_eval, coverage, t_eval = evaluate_test(test_data, rules, chef, task)

    # 9. Print results
    print(f"\n{'=' * 70}")
    print("German FinDok Results - Refinement")
    print(f"{'=' * 70}")
    print("  Configuration:")
    print(f"    Shots per class:          {args.shots}")
    print(f"    Training examples:        {len(train_sample)}")
    print(f"    Test examples:            {len(test_data)}")
    print(f"    Model:                    {args.model}")
    print(f"    Max rules:                {args.max_rules}")
    print(f"    Max samples in prompt:    {args.max_samples}")
    print(f"    Refinement iterations:    {args.max_iterations}")
    print(f"    Seed:                     {args.seed}")
    print()
    print("  Results:")
    print(f"    Accuracy (exact match):   {test_eval.exact_match:.1%}")
    print(
        f"    Coverage:                 {coverage:.1%} ({test_eval.total_tp + test_eval.total_fp}/{len(test_data)} got a label)"
    )
    print(f"    Micro Precision:          {test_eval.micro_precision:.1%}")
    print(f"    Micro Recall:             {test_eval.micro_recall:.1%}")
    print(f"    Micro F1:                 {test_eval.micro_f1:.1%}")
    print(f"    Macro F1:                 {test_eval.macro_f1:.1%}")
    print()
    print("  Timing:")
    print(f"    Learning:                 {t_learn:.1f}s")
    print(f"    Evaluation:               {t_eval:.1f}s")
    print(f"    Per-query:                {t_eval / len(test_data) * 1000:.2f}ms")
    print()
    print(f"  Rules:                      {len(rules)} total")
    print(f"{'=' * 70}")

    # 10. Per-class breakdown
    if test_eval.per_class:
        sorted_classes = sorted(test_eval.per_class, key=lambda c: c.f1, reverse=True)

        print("\n  Top 10 classes by F1:")
        for cm in sorted_classes[:10]:
            print(
                f"    {cm.label:50s} F1={cm.f1:.0%} P={cm.precision:.0%} R={cm.recall:.0%} "
                f"(TP={cm.tp} FP={cm.fp} FN={cm.fn})"
            )

        print("\n  Bottom 10 classes by F1:")
        for cm in sorted_classes[-10:]:
            print(
                f"    {cm.label:50s} F1={cm.f1:.0%} P={cm.precision:.0%} R={cm.recall:.0%} "
                f"(TP={cm.tp} FP={cm.fp} FN={cm.fn})"
            )

        zero_recall = sum(1 for cm in sorted_classes if cm.recall == 0)
        covered = len(sorted_classes) - zero_recall
        print(
            f"\n  Intent coverage: {covered}/{len(sorted_classes)} intents have at least one correct match"
        )
        print(f"  Uncovered intents: {zero_recall}/{len(sorted_classes)}")

        # 11. Save results
        output_path = Path(args.output)
        save_results(
            output_path=output_path,
            shots=args.shots,
            model=args.model,
            format=args.format,
            max_rules=args.max_rules,
            max_samples=args.max_samples,
            max_iterations=args.max_iterations,
            seed=args.seed,
            train_sample=train_sample,
            test_data=test_data,
            no_grex=args.no_grex,
            agentic=False,
            test_eval=test_eval,
            iteration_metrics=iteration_metrics,
            coverage=coverage,
            t_learn=t_learn,
            t_eval=t_eval,
            rules=rules,
        )

    # 12. Generate per-rule Markdown report
    if not args.no_mdreport:
        md_path = output_path.with_suffix(".rules_report.md")
        create_md_report(
            md_path,
            title=f"RuleChef FinDok Benchmark - Rule Analysis- {args.model}",
        )
        rule_metrics = evaluate_rules_individually(
            rules=rules,
            dataset=eval_dataset,
            apply_rules_fn=chef.learner._apply_rules,
            mode="text",
            max_samples=10,
        )
        append_rule_metrics(md_path, rule_metrics, top_n_examples=5)
        print(f"Markdown report saved to {md_path}")

    # Cleanup temp storage
    import shutil

    shutil.rmtree(storage_dir, ignore_errors=True)


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

    parser.add_argument(
        "--max-samples",
        type=int,
        default=200,
        help="Max training examples in LLM prompt (default: 200)",
    )

    parser.add_argument(
        "--test-limit",
        type=int,
        default=100,
        help="Limit test set size for quick runs (default: full 3080)",
    )
    parser.add_argument(
        "--seed", type=int, default=42, help="Random seed (default: 42)"
    )
    parser.add_argument(
        "--max-rules",
        type=int,
        default=100,
        help="Max rules to generate per synthesis (default: 100)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=3,
        help="Max refinement iterations (default: 3)",
    )

    parser.add_argument(
        "--no-grex",
        action="store_true",
        help="Disable grex regex pattern suggestions (for ablation)",
    )
    parser.add_argument("--feedback", default=None)
    parser.add_argument(
        "--windows",
        action="store_true",
        help="Crop windows around entities instead of using full text",
    )

    parser.add_argument(
        "--no-mdreport",
        action="store_true",
        help="Disable markdown report generation",
    )
    parser.add_argument("--output", default="benchmarks/results_findok_refined.json")

    args = parser.parse_args()

    run_refine(args)


if __name__ == "__main__":
    main()
