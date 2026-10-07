import argparse
import copy
import json
import shutil
import tempfile
from dataclasses import replace
from pathlib import Path

import yaml

from benchmarks.create_md_report_rules import create_md_report
from benchmarks.data import (
    BenchmarkRun,
    load_human_feedback,
    prepare_relation_split,
    prepare_split,
)
from benchmarks.io import (
    deserialize_rules,
    load_checkpoint,
    load_rules_from_json,
    save_results,
    serialize_rules,
    setup_output_paths,
)
from benchmarks.pipeline import (
    CHECKPOINT_FILE,
    EvaluationStep,
    FeedbackStep,
    LearningPipeline,
    RefinementStep,
    SynthesisStep,
    build_context,
)
from benchmarks.plot_metrics import plot_by_sentences, plot_combined, plot_single
from benchmarks.reporting import (
    print_per_class_breakdown,
    print_results,
    print_rule_summary,
)


def _synthesis_step(args, phase, start_batch=0):
    return SynthesisStep(
        batch_size=args.batch_size,
        refine_per_batch=args.refine_per_batch,
        refine_every=args.refine_every,
        audit_interval=args.audit_interval,
        start_batch=start_batch,
        phase=phase,
        synthesis_strategy=args.synthesis_strategy,
        seed=args.seed,
        holdout_fraction=args.holdout_fraction,
        split_seed=args.seed,
    )


def _refinement_step(args, use_feedback=False):
    return RefinementStep(max_iterations=args.max_iterations, use_feedback=use_feedback)


def _run_phase(
    ctx,
    steps,
    make_run,
    output_path,
    output_dir,
    args,
    report_title,
    plot_label,
    plot_output_path,
):
    ctx = LearningPipeline(steps).run(ctx)
    print_rule_summary(ctx.rules)
    print_per_class_breakdown(ctx.eval_results)
    run = make_run(ctx)
    print_results(run)
    results = save_results(output_path, run)
    if not args.no_mdreport:
        md_path = output_path.with_suffix(".rules_report_dev.md")
        create_md_report(
            md_path,
            apply_rules_fn=ctx.learner.learner._apply_rules,
            run=run,
            test_dataset=ctx.dev_dataset,
            results_folder=output_dir,
            title=report_title,
        )
        md_path_test = output_path.with_suffix(".rules_report_test.md")
        create_md_report(
            md_path_test,
            apply_rules_fn=ctx.learner.learner._apply_rules,
            run=replace(
                run,
                test_size=ctx.split.n_test_docs,
                test_sentences=len(ctx.split.test),
            ),
            test_dataset=ctx.test_dataset,
            results_folder=output_dir,
            title=f"{report_title} (TEST)",
        )
    plot_single(results, label=plot_label, output_path=plot_output_path)
    plot_by_sentences(
        results,
        label=plot_label,
        output_path=plot_output_path.with_stem(plot_output_path.stem + "_sentences"),
    )
    return ctx, results


# ── Benchmark runner ─────────────────────────────────────────


def run_benchmark(args):
    split_fn = prepare_relation_split if args.task == "relation" else prepare_split
    # 1. Load phase 1 data
    split = split_fn(
        args,
        name=args.train_name,
        train_dir=args.train_dir,
        dev_dir=args.dev_dir,
        test_dir=args.test_dir,
        classes=args.classes,
    )
    if not getattr(args, "dataset_name", None):
        args.dataset_name = args.train_name

    # 2. Setup output paths (or restore from a previous run when resuming)
    resume_from = getattr(args, "resume_from", None)
    cp = {}
    cp_phase = "phase1"
    if resume_from:
        cp = load_checkpoint(Path(resume_from) / CHECKPOINT_FILE)
        cp_phase = cp.get("phase", "phase1")
        storage_dir = tempfile.mkdtemp(prefix="rulechef_bench_")
        output_dir = Path(resume_from)
        out_name = Path(args.output)
        if args.rules_json:
            out_name = out_name.with_stem(out_name.stem + "_refined")
        logger = None
        print(
            f"\nResuming from {resume_from}/{CHECKPOINT_FILE} (phase: {cp_phase}) — skipping to batch {cp.get('completed_batches', 0)}"
        )
    else:
        storage_dir, output_dir, out_name, logger = setup_output_paths(
            args, split.selected_classes
        )

    checkpoint_path = output_dir / CHECKPOINT_FILE
    run_suffix = "_refined" if args.rules_json else ""

    # 3. Phase 1
    phase1_history = []
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
        phase1_rules = deserialize_rules(results["rules"])
        phase1_history_path = output_dir / f"phase1_history{run_suffix}.json"
        if phase1_history_path.exists():
            phase1_history = json.loads(phase1_history_path.read_text())
    else:
        seed_rules = []
        if resume_from and cp_phase == "phase1" and cp.get("rules"):
            seed_rules = deserialize_rules(cp["rules"])
            print(
                f"  Restored {len(seed_rules)} rules from checkpoint, resuming phase 1 from batch {cp.get('completed_batches', 0)}"
            )
        elif args.rules_json:
            print(f"\nLoading rules from {args.rules_json}")
            seed_rules = load_rules_from_json(args.rules_json)
            print(f"Loaded {len(seed_rules)} rules")

        ctx = build_context(
            args, split, storage_dir, checkpoint_path, logger, rules=seed_rules
        )
        if args.guidance:
            print(f"Adding upfront guidance from {args.guidance}")
            load_human_feedback(args.guidance, ctx.eval_dataset, ctx.learner)
            guidance_items = json.loads(Path(args.guidance).read_text())
            ctx = replace(
                ctx,
                history=ctx.history
                + [
                    {
                        "phase": "guidance",
                        "guidance_path": str(args.guidance),
                        "guidance_items": guidance_items,
                    }
                ],
            )

        if resume_from and cp_phase == "phase1":
            ctx = replace(
                ctx,
                batch_metrics=cp.get("batch_metrics", []),
                iteration_metrics=cp.get("iteration_metrics", []),
                best_f1=cp.get("best_f1", 0.0),
                best_rules=deserialize_rules(cp["best_rules"]),
                best_batch_idx=cp.get("best_batch_idx", -1),
                t_learn=cp.get("t_learn", 0.0),
                rules_snapshot=cp.get("rules_snapshot", []),
            )
            if ctx.best_rules:
                print(
                    f"  Restored best rules (batch {ctx.best_batch_idx}, F1={ctx.best_f1:.3f})"
                )

        start_batch = (
            cp.get("completed_batches", 0)
            if resume_from and cp_phase == "phase1"
            else 0
        )

        steps = []
        if not args.skip_synthesis:
            steps.append(_synthesis_step(args, "phase1", start_batch))

        if args.feedback and args.skip_synthesis:
            steps.append(FeedbackStep(feedback_path=args.feedback))
        if args.max_iterations > 0:
            steps.append(_refinement_step(args, use_feedback=bool(args.feedback)))

        steps.append(EvaluationStep())

        ctx, results = _run_phase(
            ctx,
            steps,
            lambda c: BenchmarkRun(
                args=args,
                train_data=split.train,
                eval_data=split.eval,
                test_data=split.dev,
                train_size=split.n_train_docs,
                eval_size=split.n_eval_docs,
                dev_size=split.n_dev_docs,
                test_size=split.n_test_docs,
                train_sentences=len(split.train),
                eval_sentences=len(split.eval),
                dev_sentences=len(split.dev),
                test_sentences=len(split.test),
                iteration_metrics=c.iteration_metrics,
                batch_test_metrics=c.batch_metrics,
                eval_results=c.eval_results,
                test_eval_results=c.test_eval_results,
                t_learn=c.t_learn,
                t_eval=c.t_eval,
                rules=c.rules,
                selected_classes=sorted(split.selected_classes),
                metadata={
                    "best_batch_idx": c.best_batch_idx,
                    "best_batch_f1": c.best_f1,
                    "best_rules_serialized": serialize_rules(c.best_rules),
                },
            ),
            output_dir / out_name,
            output_dir,
            args,
            f"Rule Evaluation Report — {args.model}",
            f"phase1 {args.dataset_name}",
            output_dir / f"phase1_{args.dataset_name}{run_suffix}.png",
        )
        phase1_rules = ctx.rules
        phase1_history = ctx.history
        (output_dir / f"phase1_history{run_suffix}.json").write_text(
            json.dumps(phase1_history, indent=2)
        )

    # 4. Transfer phase (optional)
    transfer_history = []
    if args.transfer_train_dir:
        print(f"\n{'═' * 70}")
        print(f"TRANSFER PHASE  {args.dataset_name} → {args.transfer_name}")
        print(f"{'═' * 70}")

        transfer_classes = args.transfer_classes or ",".join(
            sorted(split.selected_classes)
        )
        transfer = prepare_split(
            args,
            name=args.transfer_name,
            train_dir=args.transfer_train_dir,
            dev_dir=args.transfer_dev_dir,
            test_dir=args.transfer_test_dir,
            classes=transfer_classes,
            fallback_dev=split.dev if not args.transfer_dev_dir else None,
            fallback_test=split.test if not args.transfer_test_dir else None,
        )
        seed_rule_count = len(phase1_rules)
        t_start_batch = 0
        transfer_ctx = build_context(
            args, transfer, storage_dir, checkpoint_path, logger, rules=phase1_rules
        )

        if resume_from and cp_phase == "transfer":
            t_start_batch = cp.get("completed_batches", 0)
            transfer_rules = deserialize_rules(cp.get("rules", []))
            transfer_ctx = replace(
                transfer_ctx,
                rules=transfer_rules,
                best_f1=cp.get("best_f1", 0.0),
                best_rules=deserialize_rules(cp.get("best_rules", [])),
                best_batch_idx=cp.get("best_batch_idx", -1),
                batch_metrics=cp.get("batch_metrics", []),
                iteration_metrics=cp.get("iteration_metrics", []),
                t_learn=cp.get("t_learn", 0.0),
                rules_snapshot=cp.get("rules_snapshot", []),
            )

            print(
                f"  Restored {len(transfer_rules)} transfer rules, resuming from batch {t_start_batch}"
            )

        skip_synth = args.transfer_continuation == "refine_only"
        t_steps = []
        if not skip_synth:
            t_steps.append(_synthesis_step(args, "transfer", t_start_batch))
        if args.feedback:
            t_steps.append(FeedbackStep(feedback_path=args.feedback))

        if args.max_iterations > 0:
            t_steps.append(_refinement_step(args, use_feedback=False))
        t_steps.append(EvaluationStep())

        transfer_args = copy.copy(args)
        transfer_args.dataset_name = args.transfer_name
        transfer_args.dev_dir = args.transfer_dev_dir or args.dev_dir
        transfer_args.test_dir = args.transfer_test_dir or args.test_dir

        transfer_ctx, transfer_results = _run_phase(
            transfer_ctx,
            t_steps,
            lambda c: BenchmarkRun(
                args=transfer_args,
                train_data=transfer.train,
                eval_data=transfer.eval,
                test_data=transfer.dev,
                train_size=transfer.n_train_docs,
                eval_size=transfer.n_eval_docs,
                dev_size=transfer.n_dev_docs,
                test_size=transfer.n_test_docs,
                train_sentences=len(transfer.train),
                eval_sentences=len(transfer.eval),
                dev_sentences=len(transfer.dev),
                test_sentences=len(transfer.test),
                iteration_metrics=c.iteration_metrics,
                batch_test_metrics=c.batch_metrics,
                eval_results=c.eval_results,
                test_eval_results=c.test_eval_results,
                t_learn=c.t_learn,
                t_eval=c.t_eval,
                rules=c.rules,
                selected_classes=sorted(transfer.selected_classes),
                metadata={
                    "seeded_from": args.dataset_name,
                    "seed_rule_count": seed_rule_count,
                    "new_rules_added": len(c.rules) - seed_rule_count,
                    "continuation": args.transfer_continuation,
                    "phase1_train_sentences": len(split.train),
                    "phase1_eval_sentences": len(split.eval),
                    "transfer_train_sentences": len(transfer.train),
                    "transfer_eval_sentences": len(transfer.eval),
                    "best_batch_idx": c.best_batch_idx,
                    "best_batch_f1": c.best_f1,
                    "best_rules_serialized": serialize_rules(c.best_rules),
                },
            ),
            output_dir / out_name.with_stem(out_name.stem + "_transfer").name,
            output_dir,
            args,
            f"Rule Evaluation Report — {args.model} ({args.transfer_name})",
            f"transfer {args.transfer_name}",
            output_dir / f"transfer_{args.transfer_name}{run_suffix}.png",
        )
        transfer_history = transfer_ctx.history
        plot_combined(
            results,
            transfer_results,
            output_path=output_dir / f"combined{run_suffix}.png",
        )

    # 5. Session summary
    phases = [args.dataset_name]
    if args.transfer_train_dir:
        phases.append(args.transfer_name)
    summary_path = output_dir / f"session_summary{run_suffix}.json"
    summary_path.write_text(
        json.dumps(
            {"phases": phases, "history": phase1_history + transfer_history},
            indent=2,
        )
    )
    print(f"Session summary saved to {summary_path}")

    # Cleanup
    shutil.rmtree(storage_dir, ignore_errors=True)
    if checkpoint_path.exists():
        checkpoint_path.unlink()


# ── CLI ──────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="NER Benchmark with rule learning and cross-dataset transfer"
    )

    # ── Phase 1 dataset ───────────────────────────────────────
    parser.add_argument("--train-dir", type=str)
    parser.add_argument("--test-dir", type=str)
    parser.add_argument("--dev-dir", type=str)
    parser.add_argument("--dataset-name", type=str, default=None)
    parser.add_argument("--train-name", type=str, default="findok")
    parser.add_argument("--test-name", type=str, default="findok")
    parser.add_argument("--classes", type=str, default=None)

    # ── Transfer phase ────────────────────────────────────────
    parser.add_argument("--transfer-train-dir", type=str, default=None)
    parser.add_argument("--transfer-test-dir", type=str, default=None)
    parser.add_argument("--transfer-dev-dir", type=str, default=None)
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
        "--format", type=str, default="regex", choices=["regex", "code", "spacy"]
    )
    parser.add_argument("--task", choices=["ner", "relation"], default="ner")
    parser.add_argument("--max-rules", type=int, default=10)
    parser.add_argument("--max-samples", type=int, default=50)
    parser.add_argument("--max-counter-examples", type=int, default=10)
    parser.add_argument("--max-iterations", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--refine-per-batch", type=int, default=0)
    parser.add_argument("--refine-every", type=int, default=5)
    parser.add_argument("--holdout-fraction", type=float, default=0.0)
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
    parser.add_argument("--guidance", type=str, default=None)

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
    if not args.dev_dir:
        parser.error(
            "--dev-dir is required. Note: in configs before 2026-09-28, "
            "'test-dir' meant the DEV set — rename it to 'dev-dir'."
        )
    if not args.test_dir:
        parser.error("--test-dir (held-out test set) is required.")
    if Path(args.dev_dir).resolve() == Path(args.test_dir).resolve():
        parser.error("--dev-dir and --test-dir point to the same file.")
    if (
        args.transfer_dev_dir
        and args.transfer_test_dir
        and Path(args.transfer_dev_dir).resolve()
        == Path(args.transfer_test_dir).resolve()
    ):
        parser.error(
            "--transfer-dev-dir and --transfer-test-dir point to the same file."
        )

    if args.feedback:
        if not args.rules_json:
            parser.error(
                "--feedback requires --rules-json (feedback is added on top to improve the provided rules)."
            )
        if not args.skip_synthesis:
            parser.error("--feedback requires --skip-synthesis.")
        if args.max_iterations > 0:
            print(
                f"--feedback: setting max-iterations {args.max_iterations} → 0 (feedback only, no refinement)"
            )
            args.max_iterations = 0

    run_benchmark(args)


if __name__ == "__main__":
    main()
