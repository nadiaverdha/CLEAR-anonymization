import argparse
import json
import os
import random
import time
import uuid
from collections import defaultdict
from datetime import datetime
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

# ── Benchmark runner ────────────────────────────────────────


def run_benchmark(args):
    from openai import OpenAI
    from rulechef import RuleChef
    from rulechef.core import (
        Dataset,
        Example,
        RuleFormat,
        Task,
        TaskType,
    )
    from rulechef.evaluation import evaluate_dataset

    # 1. Load data
    print("Loading FinDok dataset...")
    train_all, test_all, entity_names = load_findok(args.train_dir, args.val_dir)
    print(
        f"  Train: {len(train_all)}, Test: {len(test_all)}, Classes: {len(entity_names)}"
    )

    # 2. Few-shot sample (optionally limited to N classes)

    classes = [c.strip() for c in args.classes.split(",")] if args.classes else None
    train_sample, train_remaining, test_data, selected_classes = sample_few_shot(
        train_all,
        shots_per_class=args.shots,
        test_shots=50,
        seed=args.seed,
        num_classes=args.num_classes,
        classes=classes,
        windows=args.windows,
    )

    for i in train_sample[:3]:
        print(i["text"])

    num_classes = len(selected_classes)
    print(
        f"  Few-shot: {args.shots}-shot x {num_classes} classes = {len(train_sample)} examples"
    )
    print(f"  Eval pool (unused train): {len(train_remaining)} examples")
    if args.num_classes:
        print(f"  Selected classes: {', '.join(sorted(selected_classes))}")

    print(f"  Test: {len(test_data)} (filtered to selected classes, held out)")

    # 3. Configure rulechef
    active_labels = sorted(selected_classes)
    task = Task(
        name="German Legal Named Entity Recognition",
        description=f"Recognize named entities in German legal text. Entities to look for: {', '.join(active_labels)}.",
        input_schema={"text": "str"},
        output_schema=NEROutput,
        type=TaskType.NER,
        text_field="text",
    )

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY") or "EMPTY",
        base_url=args.base_url,
    )

    import tempfile

    from rulechef.training_logger import TrainingDataLogger

    storage_dir = tempfile.mkdtemp(prefix="rulechef_bench_")

    # Training logger

    model_name = args.model.replace("/", "_")
    date_str = datetime.now().strftime("%Y-%m-%d")
    selected_classes_str = "_".join(
        c.replace(" ", "") for c in selected_classes
    ).strip()

    if args.rules_json:
        output_dir = Path(args.rules_json).parent
    else:
        base_dir = Path(f"benchmarks/{model_name}") / selected_classes_str
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
    print(f"  Training log: {log_path}")

    coordinator = None
    if args.agentic:
        from rulechef.coordinator import AgenticCoordinator

        coordinator = AgenticCoordinator(
            client,
            model=args.model,
            prune_after_learn=args.enable_prune,
            audit_interval=args.audit_interval,
            enable_critic=args.enable_critic,
            critic_interval=args.critic_interval,
            verbose=True,
        )
        print("  Agentic coordinator: enabled")

    chef = RuleChef(
        task=task,
        client=client,
        dataset_name="findok",
        storage_path=storage_dir,
        allowed_formats=[RuleFormat.REGEX],
        model=args.model,
        use_grex=not args.no_grex,
        max_rules=args.max_rules,
        max_samples=args.max_samples,
        coordinator=coordinator,
        training_logger=logger,
        sampling_strategy=args.sampling_strategy,
    )

    # 4. Add training examples (suppress per-example prints)
    print(f"\nAdding {len(train_sample)} training examples...")
    t0 = time.time()
    for ex in train_sample:
        chef.add_example(
            {"text": ex["text"]},
            {"label": ex["entities"]},
        )
    t_add = time.time() - t0
    print(f"  Done ({t_add:.1f}s)")

    # 5. Build eval Dataset from unused training data (for refinement)
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

    # 6. Learn rules — fresh synthesis or refinement from existing rules
    if args.rules_json:
        print(f"\nRefinement mode — loading rules from {args.rules_json}")
        saved = json.loads(Path(args.rules_json).read_text())
        rules = [
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
            for r in saved["rules"]
        ]
        print(f"  Loaded {len(rules)} rules")

        print("  Analyzing rules for auto-feedback...")
        rule_metrics = evaluate_rules_individually(
            rules=rules,
            dataset=eval_dataset,
            apply_rules_fn=chef.learner._apply_rules,
            mode="text",
            max_samples=args.max_samples,
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

        # Human feedback
        if args.feedback:
            feedback_items = json.loads(Path(args.feedback).read_text())
            print(f"  Loading {len(feedback_items)} human feedback items")

            def _norm(s):
                return s.replace("\u2011", "-").replace("\u2010", "-")

            for fb in feedback_items:
                level = fb.get("level", "task")
                text = fb["text"]
                target_id = ""
                if level == "rule":
                    rule_name = fb.get("rule_name", "")
                    matched = next(
                        (r for r in rules if _norm(r.name) == _norm(rule_name)), None
                    )
                    if matched:
                        target_id = matched.id
                    else:
                        print(f"  Rule not found: {rule_name} — treating as task-level")
                        level = "task"
                add_feedback(eval_dataset, text, level, target_id)

        print("\nLearning rules (incremental)...")
        t0 = time.time()
        result = chef.learn_rules(run_evaluation=False, incremental_only=True)
        t_learn = time.time() - t0

    else:
        print("\nLearning rules...")
        print(f"  model={args.model}")
        print(f"  format={args.format}")
        print(f"  max_rules={args.max_rules}")
        print(f"  max_samples={args.max_samples}")
        print(f"  max_iterations={args.max_iterations}")
        t0 = time.time()
        result = chef.learn_rules(
            run_evaluation=False,
        )
        t_learn = time.time() - t0

    if result is None:
        print("ERROR: Learning failed!")
        return

    rules, _ = result
    print(f"\nSynthesis complete ({t_learn:.1f}s)")
    print(f"  Rules generated: {len(rules)}")

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
            audit_interval=0,
        )
        t_refine = time.time() - t0_refine
        t_learn += t_refine
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

    test_dataset = Dataset(name="findok_test", task=task)
    for ex in test_data:
        test_dataset.examples.append(
            Example(
                id=str(uuid.uuid4())[:8],
                input={"text": ex["text"]},
                expected_output={"entities": ex["entities"]},
                source="benchmark",
            )
        )

    test_eval, coverage, t_eval = evaluate_test(
        test_data, test_dataset, rules, chef, task
    )

    # 9. Print results
    print(f"\n{'=' * 70}")
    print("German FinDok Results")
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

        output_path = output_dir / out_name
        save_results(
            output_path,
            args.shots,
            args.model,
            args.format,
            args.max_rules,
            args.max_samples,
            args.max_iterations,
            args.seed,
            train_sample,
            test_data,
            args.no_grex,
            args.agentic,
            test_eval,
            iteration_metrics,
            coverage,
            t_learn,
            t_eval,
            rules,
            args.enable_critic,
            args.enable_prune,
            args.critic_interval,
            args.audit_interval,
            args.windows,
            sampling_strategy=args.sampling_strategy,
        )

    # 12. Generate per-rule Markdown report
    if not args.no_mdreport:
        from reports.create_md_report_rules import (
            append_overall_metrics,
            append_rule_metrics,
            create_md_report,
        )

        md_path = output_path.with_suffix(".rules_report.md")
        create_md_report(
            md_path,
            title=f"RuleChef FinDok Benchmark - Rule Analysis- {args.model}",
        )

        append_overall_metrics(
            md_path=md_path,
            test_data=test_data,
            test_dataset=test_dataset,
            rules=rules,
            chef=chef,
            task=task,
            shots=args.shots,
            train_sample=train_sample,
            model=args.model,
            max_rules=args.max_rules,
            max_samples=args.max_samples,
            max_iterations=args.max_iterations,
            seed=args.seed,
            agentic=args.agentic,
            enable_critic=args.enable_critic,
            enable_prune=args.enable_prune,
            critic_interval=args.critic_interval,
            audit_interval=args.audit_interval,
            use_grex=not args.no_grex,
            sampling_strategy=args.sampling_strategy,
        )

        rule_metrics = evaluate_rules_individually(
            rules=rules,
            dataset=test_dataset,
            apply_rules_fn=chef.learner._apply_rules,
            mode="text",
            max_samples=args.max_samples,
        )
        append_rule_metrics(md_path, rule_metrics, top_n_examples=5)
        print(f"Markdown report saved to {md_path}")

    # Cleanup temp storage
    import shutil

    shutil.rmtree(storage_dir, ignore_errors=True)


# ── CLI ─────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="findok Named Entity Recognition Benchmark for RuleChef"
    )
    parser.add_argument(
        "--train_dir",
        type=str,
        help="Path to the train data (JSON format)",
    )
    parser.add_argument(
        "--val_dir",
        type=str,
        help="Path to the test data (JSON format)",
    )
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
    parser.add_argument(
        "--base-url",
        type=str,
        default="http://localhost:8000/v1",
        help="OpenAI-compatible base URL (e.g. https://api.groq.com/openai/v1)",
    )
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
        "--max-rules",
        type=int,
        default=30,
        help="Max rules to generate per synthesis (default: 30)",
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        default=200,
        help="Max training examples in LLM prompt (default: 200)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=3,
        help="Max refinement iterations (default: 3)",
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
        "--output",
        type=str,
        default="results_findok.json",
        help="Save results to JSON file (default: benchmarks/results_findok.json)",
    )
    parser.add_argument(
        "--agentic",
        action="store_true",
        help="Use AgenticCoordinator for LLM-guided refinement",
    )

    parser.add_argument(
        "--enable-prune",
        action="store_true",
        help="Prune rules after each iteration based on eval set performance",
    )
    parser.add_argument(
        "--audit-interval",
        type=int,
        default=0,
        help="Interval for audit checks (default: 0)",
    )

    parser.add_argument(
        "--enable-critic",
        action="store_true",
        help="Use CriticAgent for LLM-guided refinement",
    )

    parser.add_argument(
        "--critic-interval",
        type=int,
        default=0,
        help="Interval for CriticAgent refinement (default: 0)",
    )
    parser.add_argument(
        "--no-grex",
        action="store_true",
        help="Disable grex regex pattern suggestions (for ablation)",
    )
    parser.add_argument(
        "--sampling-strategy",
        default="balanced",
        help="Use sampling strategy for selecting training examples",
    )
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
    parser.add_argument(
        "--rules-json",
        type=str,
        default=None,
        help="Path to a previous results JSON — enables refinement mode",
    )
    parser.add_argument(
        "--feedback",
        type=str,
        default=None,
        help="Path to a human feedback JSON file (only used with --rules-json)",
    )

    args = parser.parse_args()
    run_benchmark(args)


if __name__ == "__main__":
    main()
