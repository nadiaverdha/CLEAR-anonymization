import argparse
import json
import random
import shutil
import time
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from create_md_report_rules import create_md_report

from benchmarks.util import (
    BenchmarkRun,
    evaluate_test,
    load_human_feedback,
    load_rules_from_json,
    make_dataset,
    make_oniteration_callback,
    print_per_class_breakdown,
    print_results,
    print_rule_summary,
    save_results,
    setup_output_paths,
)
from clear_anonymization.models.nerlearner import NERLearner
from clear_anonymization.ner_datasets import (
    get_dataset_class_definitions,
    load_ner_dataset_from_conll,
)
from clear_anonymization.preprocess.create_train_dev_split import (
    label_distribution_sent,
    print_distribution,
)
from clear_anonymization.preprocess.sampling import sample_few_shot

# ── Benchmark runner ────────────────────────────────────────


def run_benchmark(args):

    # 1. Load data
    print(f"Loading {args.dataset_name} dataset...")
    train_all = load_ner_dataset_from_conll(
        args.train_dir,
    )
    dev_all = load_ner_dataset_from_conll(
        args.val_dir,
    )

    if args.extra_train_dir:
        extra_train = load_ner_dataset_from_conll(
            args.extra_train_dir,
        )

    entity_names = set(get_dataset_class_definitions(args.dataset_name).keys())

    extra_count = len(extra_train.samples) if args.extra_train_dir else 0

    # 2. Sample data

    classes = [c.strip() for c in args.classes.split(",")] if args.classes else None

    (
        train_data,
        eval_data,
        counter_examples,
        selected_classes,
        n_manually_annotated,
        n_train_docs,
        n_eval_docs,
    ) = sample_few_shot(
        train_data=train_all.samples,
        seed=args.seed,
        num_classes=args.num_classes,
        classes=classes,
        pool_size=args.pool_size,
        train_ratio=args.train_ratio,
        extra_data=extra_train.samples if args.extra_train_dir else None,
    )

    dev_data = [
        {
            "doc_id": s.doc_id,
            "sent_id": sent.sent_id,
            "text": sent.text,
            "entities": sent.labels,
        }
        for s in dev_all.samples
        for sent in s.sentences
    ]

    # sizes = number of documents; annotations = number of annotated sentences
    train_annotations = len(train_data)
    eval_annotations = len(eval_data)

    print(f"{'─' * 70}")
    print(
        f"Full data   — train docs: {len(train_all.samples)}, dev docs: {len(dev_all.samples)}, extra docs: {extra_count}"
    )
    print(
        f"Sampled     — train docs: {n_train_docs}, eval docs: {n_eval_docs}, dev docs: {len(dev_all.samples)}"
    )
    print_distribution(train_data, "TRAIN", fn=label_distribution_sent)
    print_distribution(eval_data, "EVAL", fn=label_distribution_sent)
    print_distribution(dev_data, "DEV", fn=label_distribution_sent)
    print(
        f"Sentences   — train: {train_annotations}, eval: {eval_annotations}, dev: {len(dev_data)}"
    )
    print(
        f"Classes     — {len(selected_classes)} selected: {', '.join(sorted(selected_classes))}"
    )
    print(f"Counter examples: {len(counter_examples)}")
    print(f"{'─' * 70}")

    # 3. Setup output
    storage_dir, output_dir, out_name, logger = setup_output_paths(
        args, selected_classes
    )

    # 4. Build train_for_chef
    if args.synthesis_strategy != "bulk":
        train_for_chef = train_data + counter_examples
        random.Random(args.seed).shuffle(train_for_chef)
    else:
        train_for_chef = train_data

    # 5. Create learner
    learner = NERLearner(
        model=args.model,
        dataset_name=args.dataset_name,
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
        selected_classes=selected_classes,
    )

    # 6. Build eval and dev dataset
    eval_dataset = make_dataset(f"{args.dataset_name}_eval", eval_data, learner.task)
    dev_dataset = make_dataset(f"{args.dataset_name}_dev", dev_data, learner.task)

    # 7. Load or synthesize rules
    iteration_metrics = []
    batch_dev_metrics = []
    on_iteration = make_oniteration_callback(iteration_metrics)

    n_auto = len(train_data) - n_manually_annotated
    first_manual_batch = (
        (n_auto // args.batch_size) if n_manually_annotated > 0 else None
    )

    def on_batch(batch_idx, rules):
        result, _ = evaluate_test(dev_data, dev_dataset, rules, learner)
        examples_seen = (batch_idx + 1) * args.batch_size
        includes_manual = n_manually_annotated > 0 and examples_seen > n_auto
        batch_dev_metrics.append(
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
                "train_manually_anno": n_manually_annotated,
                "includes_manual_anno": includes_manual,
            }
        )
        manual_tag = " [+manual]" if includes_manual else ""
        print(
            f"[batch {batch_idx}{manual_tag}] dev micro_f1={result.micro_f1:.3f}  dev micro_precision={result.micro_precision:.3f}  micro_recall={result.micro_recall:.3f}"
        )

    t_learn = 0.0
    if args.rules_json:
        print(f"\nLoading rules from {args.rules_json}")
        rules = load_rules_from_json(Path(args.rules_json))
        print(f"Loaded {len(rules)} rules")
        if args.feedback:
            load_human_feedback(args.feedback, rules, eval_dataset, learner)
        if not args.skip_synthesis:
            rules, t_learn = learner.fit_batched(
                train_for_chef,
                eval_dataset=eval_dataset if args.refine_per_batch > 0 else None,
                batch_size=args.batch_size,
                refine_per_batch=args.refine_per_batch,
                refine_every=args.refine_every,
                iteration_callback=on_iteration,
                batch_callback=on_batch,
                audit_interval=args.audit_interval,
                seed_rules=rules,
            )
    else:
        rules, t_learn = learner.fit_batched(
            train_for_chef,
            eval_dataset=eval_dataset if args.refine_per_batch > 0 else None,
            batch_size=args.batch_size,
            refine_per_batch=args.refine_per_batch,
            refine_every=args.refine_every,
            iteration_callback=on_iteration,
            batch_callback=on_batch,
            audit_interval=args.audit_interval,
        )

    # 8. Refine rules — patches old rules or polishes fresh synthesis
    if args.max_iterations > 0:
        print(
            f"\nRefining against eval set ({len(eval_data)} examples, max {args.max_iterations} iterations)..."
        )
        t0_refine = time.time()
        rules, refine_eval = learner.refine(
            rules,
            eval_dataset,
            max_iterations=args.max_iterations,
            iteration_callback=on_iteration,
        )
        t_refine = time.time() - t0_refine
        t_learn += t_refine
        print(f"Refinement complete ({t_refine:.1f}s)")
        if refine_eval:
            print(
                f"  Eval accuracy: {refine_eval.exact_match:.1%}, eval micro F1: {refine_eval.micro_f1:.1%}"
            )

    # 9. Print rule summary
    print_rule_summary(rules)

    # 10. Evaluate on held-out dev set
    dev_eval, t_eval = evaluate_test(dev_data, dev_dataset, rules, learner)
    benchmark_run = BenchmarkRun(
        args=args,
        train_data=train_data,
        eval_data=eval_data,
        test_data=dev_data,
        train_size=n_train_docs,
        eval_size=n_eval_docs,
        test_size=len(dev_all.samples),
        train_annotations=train_annotations,
        eval_annotations=eval_annotations,
        test_annotations=len(dev_data),
        iteration_metrics=iteration_metrics,
        batch_test_metrics=batch_dev_metrics,
        eval_results=dev_eval,
        t_learn=t_learn,
        t_eval=t_eval,
        rules=rules,
        selected_classes=sorted(selected_classes),
        manually_annotated_size=n_manually_annotated,
        first_manual_batch=first_manual_batch,
    )

    # 11. Per-class breakdown
    print_per_class_breakdown(dev_eval)

    # 12. Save results
    print_results(benchmark_run)
    output_path = output_dir / out_name
    save_results(output_path, benchmark_run)

    # 13. Generate per-rule Markdown report
    if not args.no_mdreport:
        md_path = output_path.with_suffix(".rules_report.md")
        create_md_report(
            md_path,
            chef=learner,
            run=benchmark_run,
            test_dataset=dev_dataset,
            results_folder=output_dir,
            title=f"Rule Evaluation Report — {args.model}",
        )

    # Cleanup temp storage
    shutil.rmtree(storage_dir, ignore_errors=True)


# ── CLI ─────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="findok Named Entity Recognition Benchmark for RuleChef"
    )
    parser.add_argument(
        "--train-dir",
        type=str,
        help="Path to the train data (JSON format)",
    )
    parser.add_argument(
        "--extra-train-dir",
        type=str,
        help="Path to the train data (JSON format)",
    )

    parser.add_argument(
        "--val-dir",
        type=str,
        help="Path to the dev data (JSON format)",
    )
    parser.add_argument(
        "--dataset-name",
        type=str,
        default="findok",
        help="Name of the dataset",
    )

    parser.add_argument(
        "--pool-size",
        type=int,
        default=None,
        help="Cap total examples drawn from train file (train + eval combined)",
    )
    parser.add_argument(
        "--shots",
        type=int,
        default=None,
        help="Per-class cap on training examples (default: auto = n_train // num_classes)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="google/gemma-3-27b-it",
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
        "--train-ratio",
        type=float,
        default=0.8,
        help="Ratio of training data to use (default: 0.8)",
    )
    parser.add_argument(
        "--max-rules",
        type=int,
        default=10,
        help="Max rules to generate per synthesis (default: 30)",
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        default=50,
        help="Max training examples in LLM prompt (default: 200)",
    )
    parser.add_argument(
        "--max-counter-examples",
        type=int,
        default=10,
        help="Max counter-examples to show in prompts (default: 10)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=3,
        help="Max refinement iterations (default: 3)",
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
        "--synthesis-strategy",
        type=str,
        default="bulk",
        help="Synthesis strategy to use",
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
        "--batch-size",
        type=int,
        default=20,
        help="Examples per batch for incremental synthesis (default: 20)",
    )
    parser.add_argument(
        "--refine-per-batch",
        type=int,
        default=0,
        help="Refinement iterations after each synthesis batch (default: 0 = disabled)",
    )
    parser.add_argument(
        "--refine-every",
        type=int,
        default=5,
        help="Run per-batch refinement every N batches (default: 5 )",
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
    parser.add_argument(
        "--skip-synthesis",
        action="store_true",
        help="Skip LLM synthesis and use the rules from --rules-json directly (go straight to refinement)",
    )
    parser.add_argument(
        "--config", type=str, help="Path to YAML config file", default=None
    )

    # if config file is provided, load it and set defaults accordingly
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument(
        "--config", type=str, help="Path to YAML config file", default=None
    )
    pre_args, _ = pre.parse_known_args()
    if pre_args.config:
        with open(pre_args.config) as f:
            config_args = yaml.safe_load(f)
        config_args = {k.replace("-", "_"): v for k, v in config_args.items()}
        parser.set_defaults(**config_args)

    # if no arguments are provided, use arguments from provided in CLI, otherwise defaults
    args = parser.parse_args()
    run_benchmark(args)


if __name__ == "__main__":
    main()
