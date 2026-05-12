import argparse
import copy
import json
import shutil
import tempfile
from pathlib import Path

import yaml
from create_md_report_rules import create_md_report
from plot_metrics import plot_combined, plot_single

from benchmarks.plot_metrics import plot_single
from benchmarks.session import CHECKPOINT_FILE, TrainingSession
from benchmarks.util import (
    BenchmarkRun,
    deserialize_rules,
    load_checkpoint,
    load_rules_from_json,
    prepare_split,
    print_per_class_breakdown,
    print_results,
    print_rule_summary,
    save_results,
    setup_output_paths,
)

# ── Benchmark runner ─────────────────────────────────────────


def run_benchmark(args):

    # 1. Load and sample phase 1 data
    split = prepare_split(
        args,
        name=args.train_name,
        train_dir=args.train_dir,
        test_dir=args.test_dir,
        classes=args.classes,
    )

    # 2. Setup output paths (or restore from a previous run when resuming)
    resume_from = getattr(args, "resume_from", None)
    start_batch = 0
    cp = {}
    cp_phase = "phase1"
    if resume_from:
        cp_file = Path(resume_from) / CHECKPOINT_FILE
        cp = load_checkpoint(cp_file)
        cp_phase = cp.get("phase", "phase1")
        if cp_phase == "phase1":
            start_batch = cp.get("completed_batches", 0)
        storage_dir = tempfile.mkdtemp(prefix="rulechef_bench_")
        output_dir = Path(resume_from)
        out_name = Path(args.output)
        if args.rules_json:
            out_name = out_name.with_stem(out_name.stem + "_refined")
        logger = None
        print(
            f"\nResuming from {cp_file} (phase: {cp_phase}) — skipping to batch {cp.get('completed_batches', 0)}"
        )
    else:
        storage_dir, output_dir, out_name, logger = setup_output_paths(
            args, split.selected_classes
        )

    # 3. Create session, optionally seed with existing rules
    session = TrainingSession(
        args=args,
        storage_dir=storage_dir,
        checkpoint_path=output_dir / CHECKPOINT_FILE,
    )
    if resume_from and cp_phase == "phase1" and cp.get("rules"):
        session.rules = deserialize_rules(cp["rules"])
        print(f"  Restored {len(session.rules)} rules")
    elif args.rules_json and not (resume_from and cp_phase == "transfer"):
        print(f"\nLoading rules from {args.rules_json}")
        session.rules = load_rules_from_json(Path(args.rules_json))
        print(f"Loaded {len(session.rules)} rules")

    # 4. Phase 1: synthesise and refine
    if resume_from and cp_phase == "transfer":
        phase1_path = output_dir / out_name
        if not phase1_path.exists():
            raise RuntimeError(
                f"Cannot resume transfer phase: phase 1 results not found at {phase1_path}"
            )
        print(
            f"\nSkipping phase 1 (already completed). Loading rules from {phase1_path}"
        )
        results = json.loads(phase1_path.read_text())
        session.rules = deserialize_rules(results["rules"])
    else:
        batch_metrics, iteration_metrics, t_learn = session.train(
            split,
            logger=logger,
            skip_synthesis=args.skip_synthesis,
            synthesize_per_batch=args.synthesize_per_batch,
            start_batch=start_batch,
            prev_batch_metrics=cp.get("batch_metrics"),
            prev_iteration_metrics=cp.get("iteration_metrics"),
            prev_rules_snapshots=cp.get("rules_snapshots"),
            prev_t_learn=cp.get("t_learn"),
            phase="phase1",
        )
        if args.feedback and args.skip_synthesis:
            session.inject_feedback(args.feedback)
        if args.max_iterations > 0:
            session.refine(split)

        # 5. Evaluate on held-out dev set
        print_rule_summary(session.rules)
        dev_eval, t_eval = session.evaluate(split)

        benchmark_run = BenchmarkRun(
            args=args,
            train_data=split.train,
            eval_data=split.eval,
            test_data=split.dev,
            train_size=split.n_train_docs,
            eval_size=split.n_eval_docs,
            test_size=split.n_test_docs,
            train_annotations=len(split.train),
            eval_annotations=len(split.eval),
            test_annotations=len(split.dev),
            iteration_metrics=iteration_metrics,
            batch_test_metrics=batch_metrics,
            eval_results=dev_eval,
            t_learn=t_learn,
            t_eval=t_eval,
            rules=session.rules,
            selected_classes=sorted(split.selected_classes),
        )

        # 6. Print and save phase 1 results
        print_per_class_breakdown(dev_eval)
        print_results(benchmark_run)
        output_path = output_dir / out_name
        results = save_results(output_path, benchmark_run)

        # 7. Markdown report
        if not args.no_mdreport:
            md_path = output_path.with_suffix(".rules_report.md")
            create_md_report(
                md_path,
                chef=session._learner,
                run=benchmark_run,
                test_dataset=session._dev_dataset,
                results_folder=output_dir,
                title=f"Rule Evaluation Report — {args.model}",
            )

        # 8. Plots for phase 1 (and transfer phase if applicable)
        plot_suffix = "_refined" if (args.rules_json or args.feedback) else ""
        plot_single(
            results,
            label=f"phase1 {args.dataset_name}",
            output_path=output_dir / f"phase1_{args.dataset_name}{plot_suffix}.png",
        )

    # 8. Transfer phase (optional) — seeds with phase 1 rules automatically
    if args.transfer_train_dir:
        print(f"\n{'═' * 70}")
        print(f"TRANSFER PHASE  {args.dataset_name} → {args.transfer_dataset_name}")
        print(f"{'═' * 70}")

        transfer_classes = args.transfer_classes or ",".join(
            sorted(split.selected_classes)
        )
        transfer = prepare_split(
            args,
            name=args.transfer_dataset_name,
            train_dir=args.transfer_train_dir,
            test_dir=args.transfer_test_dir,
            classes=transfer_classes,
            fallback_dev=split.dev if not args.transfer_test_dir else None,
        )
        t_start_batch = 0
        t_prev_batch_metrics = None

        seed_rule_count = len(session.rules)
        if resume_from and cp_phase == "transfer":
            t_start_batch = cp.get("completed_batches", 0)
            t_prev_batch_metrics = cp.get("batch_metrics")
            session.rules = deserialize_rules(cp.get("rules", []))
            print(
                f"  Restored {len(session.rules)} transfer rules, resuming from batch {t_start_batch}"
            )

        skip_synth = args.transfer_continuation == "refine_only"
        t_batch_metrics, t_iteration_metrics, t_learn = session.train(
            transfer,
            skip_synthesis=skip_synth,
            synthesize_per_batch=(
                args.transfer_continuation == "synthesize_and_refine"
            ),
            start_batch=t_start_batch,
            prev_batch_metrics=t_prev_batch_metrics,
            prev_iteration_metrics=cp.get("iteration_metrics"),
            prev_rules_snapshots=cp.get("rules_snapshots"),
            prev_t_learn=cp.get("t_learn"),
            phase="transfer",
        )
        if args.feedback:
            session.inject_feedback(args.feedback)
        if args.max_iterations > 0:
            session.refine(transfer)

        print_rule_summary(session.rules)
        transfer_eval, t_eval = session.evaluate(transfer)

        transfer_args = copy.copy(args)
        transfer_args.dataset_name = args.transfer_dataset_name

        transfer_run = BenchmarkRun(
            args=transfer_args,
            train_data=split.train + transfer.train,
            eval_data=split.eval + transfer.eval,
            test_data=transfer.dev,
            train_size=split.n_train_docs + transfer.n_train_docs,
            eval_size=split.n_eval_docs + transfer.n_eval_docs,
            test_size=transfer.n_test_docs,
            train_annotations=len(split.train) + len(transfer.train),
            eval_annotations=len(split.eval) + len(transfer.eval),
            test_annotations=len(transfer.dev),
            iteration_metrics=t_iteration_metrics,
            batch_test_metrics=t_batch_metrics,
            eval_results=transfer_eval,
            t_learn=t_learn,
            t_eval=t_eval,
            rules=session.rules,
            selected_classes=sorted(transfer.selected_classes),
            metadata={
                "seeded_from": args.dataset_name,
                "seed_rule_count": seed_rule_count,
                "new_rules_added": len(session.rules) - seed_rule_count,
                "continuation": args.transfer_continuation,
                "phase1_train_sentences": len(split.train),
                "phase1_eval_sentences": len(split.eval),
                "transfer_train_sentences": len(transfer.train),
                "transfer_eval_sentences": len(transfer.eval),
            },
        )

        print_per_class_breakdown(transfer_eval)
        print_results(transfer_run)
        transfer_path = (
            output_dir / out_name.with_stem(out_name.stem + "_transfer").name
        )
        transfer_results = save_results(transfer_path, transfer_run)

        if not args.no_mdreport:
            md_path = transfer_path.with_suffix(".rules_report.md")
            create_md_report(
                md_path,
                chef=session._learner,
                run=transfer_run,
                test_dataset=session._dev_dataset,
                results_folder=output_dir,
                title=f"Rule Evaluation Report — {args.model} ({args.transfer_dataset_name})",
            )

        plot_single(
            transfer_results,
            label=f"transfer {args.transfer_dataset_name}",
            output_path=output_dir / f"transfer_{args.transfer_dataset_name}.png",
        )

        plot_combined(
            results,
            transfer_results,
            output_path=output_dir / f"combined.png",
        )

    # Session summary — full history across all phases
    phases = [args.dataset_name]
    if args.transfer_train_dir:
        phases.append(args.transfer_dataset_name)
    run_suffix = "_refined" if (args.rules_json or args.feedback) else ""
    summary_path = output_dir / f"session_summary{run_suffix}.json"
    summary_path.write_text(
        json.dumps(
            {
                "phases": phases,
                "history": session.history,
            },
            indent=2,
        )
    )
    print(f"Session summary saved to {summary_path}")

    # Cleanup
    shutil.rmtree(storage_dir, ignore_errors=True)
    cp_file = output_dir / CHECKPOINT_FILE
    if cp_file.exists():
        cp_file.unlink()


# ── CLI ──────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="NER Benchmark with rule learning and cross-dataset transfer"
    )

    # ── Phase 1 dataset ───────────────────────────────────────
    parser.add_argument("--train-dir", type=str)
    parser.add_argument("--test-dir", type=str)
    parser.add_argument("--train-name", type=str, default="findok")
    parser.add_argument("--test-name", type=str, default="findok")
    parser.add_argument("--classes", type=str, default=None)

    # ── Transfer phase ────────────────────────────────────────
    parser.add_argument("--transfer-train-dir", type=str, default=None)
    parser.add_argument("--transfer-test-dir", type=str, default=None)
    parser.add_argument("--transfer-name", type=str, default=None)
    parser.add_argument("--transfer-test-name", type=str, default=None)
    parser.add_argument("--transfer-classes", type=str, default=None)
    parser.add_argument(
        "--transfer-continuation",
        choices=["synthesize_and_refine", "refine_only"],
        default="synthesize_and_refine",
    )

    # ── Sampling ──────────────────────────────────────────────
    parser.add_argument("--pool-size", type=int, default=None)
    parser.add_argument("--shots", type=int, default=None)
    parser.add_argument("--num-classes", type=int, default=None)
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--seed", type=int, default=42)

    # ── Learner ───────────────────────────────────────────────
    parser.add_argument("--model", type=str, default="google/gemma-3-27b-it")
    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1")
    parser.add_argument(
        "--format", type=str, default="regex", choices=["regex", "code", "both"]
    )
    parser.add_argument("--max-rules", type=int, default=10)
    parser.add_argument("--max-samples", type=int, default=50)
    parser.add_argument("--max-counter-examples", type=int, default=10)
    parser.add_argument("--max-iterations", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--refine-per-batch", type=int, default=0)
    parser.add_argument("--refine-every", type=int, default=5)
    parser.add_argument("--synthesis-strategy", type=str, default="bulk")
    parser.add_argument("--sampling-strategy", default="balanced")
    parser.add_argument("--agentic", action="store_true")
    parser.add_argument("--enable-prune", action="store_true")
    parser.add_argument("--audit-interval", type=int, default=0)
    parser.add_argument("--enable-critic", action="store_true")
    parser.add_argument("--critic-interval", type=int, default=0)
    parser.add_argument("--no-grex", action="store_true")
    parser.add_argument("--windows", action="store_true")

    # ── Rules / feedback ──────────────────────────────────────
    parser.add_argument("--rules-json", type=str, default=None)
    parser.add_argument("--feedback", type=str, default=None)
    parser.add_argument("--skip-synthesis", action="store_true")
    parser.add_argument(
        "--synthesize-per-batch",
        action="store_true",
        help="Per batch: full synthesis + patch pass (learn new patterns and adjust existing ones)",
    )

    # ── Output ────────────────────────────────────────────────
    parser.add_argument("--output", type=str, default="results_findok.json")
    parser.add_argument("--no-mdreport", action="store_true")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument(
        "--resume-from",
        type=str,
        default=None,
        help="Path to a previous run's output directory to resume from its checkpoint",
    )

    # Two-pass: YAML defaults first, CLI wins
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument("--config", type=str, default=None)
    pre.add_argument("--resume-from", type=str, default=None)
    pre_args, _ = pre.parse_known_args()
    config_path = pre_args.config
    if config_path is None and pre_args.resume_from:
        candidate = Path(pre_args.resume_from) / "config.yaml"
        if candidate.exists():
            config_path = str(candidate)
    if config_path:
        with open(config_path) as f:
            config_args = yaml.safe_load(f)
        parser.set_defaults(**{k.replace("-", "_"): v for k, v in config_args.items()})

    args = parser.parse_args()
    run_benchmark(args)


if __name__ == "__main__":
    main()
