import argparse
import json
import os
from concurrent.futures import ProcessPoolExecutor
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

from rulechef.core import Rule, RuleFormat, Task, TaskType
from rulechef.evaluation import evaluate_dataset, evaluate_rules_individually
from rulechef.executor import RuleExecutor

from benchmarks.data import BenchmarkRun, make_dataset
from benchmarks.io import deserialize_rules
from clear_anonymization.evaluation.evaluator import classify_fp
from clear_anonymization.models.nerlearner import NERLearner, NEROutput
from clear_anonymization.ner_datasets import (
    get_dataset_class_definitions,
    load_ner_dataset_from_conll,
)


@contextmanager
def _details_block(f, summary: str):
    f.write(f"<details>\n<summary>{summary}</summary>\n\n")
    yield
    f.write("</details>\n\n---\n\n")


def _write_table(f, headers: list[str], rows: list[list[str]]) -> None:
    f.write("| " + " | ".join(headers) + " |\n")
    f.write("|" + "|".join("---" for _ in headers) + "|\n")
    for row in rows:
        f.write("| " + " | ".join(str(c) for c in row) + " |\n")
    f.write("\n")


def write_summary_table(file_path: Path, metrics_list):
    sorted_metrics = sorted(metrics_list, key=lambda m: m.precision, reverse=True)
    rows = [
        [
            f"`{m.rule_name}`",
            f"{m.f1:.1%}",
            f"{m.precision:.1%}",
            f"{m.recall:.1%}",
            m.matches,
            m.true_positives,
            m.false_positives,
        ]
        for m in sorted_metrics
    ]
    with file_path.open("a", encoding="utf-8") as f:
        with _details_block(f, "📊 Summary"):
            _write_table(
                f,
                [
                    "Rule",
                    "F1",
                    "Precision",
                    "Recall",
                    "Total Predicted",
                    "True Positives",
                    "False Positives",
                ],
                rows,
            )


def append_overall_metrics(
    md_path, apply_rules_fn, test_dataset, run, results_folder, rules=None
):
    config = run.args
    if rules is None:
        rules = run.rules

    test_eval = evaluate_dataset(
        rules,
        test_dataset,
        apply_rules_fn,
        mode="text",
    )
    with md_path.open("a", encoding="utf-8") as f:
        with _details_block(f, "Configuration"):
            f.write("Results can be reproduced by running this command: \n")
            f.write(
                f"```\n python benchmark.py --config {results_folder}/config.yaml \n```\n"
            )
            train_ratio = getattr(config, "train_ratio", None)
            _write_table(
                f,
                ["Parameter", "Value"],
                [
                    ["Pool size", getattr(config, "pool_size", "N/A")],
                    [
                        "Train ratio",
                        f"{train_ratio:.2f}" if train_ratio is not None else "N/A",
                    ],
                    [
                        "Validation ratio",
                        f"{1.0 - train_ratio:.2f}"
                        if train_ratio is not None
                        else "N/A",
                    ],
                    ["Shots per class", getattr(config, "shots", "N/A")],
                    ["Training documents", run.train_size],
                    ["Validation documents", run.eval_size],
                    ["Test documents", run.test_size],
                    ["Train sentences", run.train_annotations],
                    ["Validation sentences", run.eval_annotations],
                    ["Test sentences", run.test_annotations],
                    ["Model", getattr(config, "model", "N/A")],
                    ["Max rules", getattr(config, "max_rules", "N/A")],
                    ["Max samples in prompt", getattr(config, "max_samples", "N/A")],
                    [
                        "Refinement iterations",
                        getattr(config, "max_iterations", "N/A"),
                    ],
                    ["Seed", getattr(config, "seed", "N/A")],
                    ["Agentic", getattr(config, "agentic", "N/A")],
                    ["Enable Critic", getattr(config, "enable_critic", "N/A")],
                    ["Enable Prune", getattr(config, "enable_prune", "N/A")],
                    ["Critic Interval", getattr(config, "critic_interval", "N/A")],
                    ["Audit Interval", getattr(config, "audit_interval", "N/A")],
                    ["Use GREX", not getattr(config, "no_grex", False)],
                    ["Format", getattr(config, "format", "N/A")],
                    [
                        "Synthesis strategy",
                        getattr(config, "synthesis_strategy", "N/A"),
                    ],
                    [
                        "Sampling strategy",
                        getattr(config, "sampling_strategy", "N/A"),
                    ],
                    ["Batch size", getattr(config, "batch_size", "N/A")],
                    [
                        "Refine per batch",
                        getattr(config, "refine_per_batch", "N/A"),
                    ],
                    [
                        "Manually annotated examples",
                        getattr(run, "manually_annotated_size", 0),
                    ],
                    [
                        "First batch with manual data",
                        getattr(run, "first_manual_batch", None),
                    ],
                ],
            )

        if "seeded_from" in run.metadata:
            f.write("**Transfer Learning**\n\n")
            _write_table(
                f,
                ["Property", "Value"],
                [[k.replace("_", " ").title(), v] for k, v in run.metadata.items()],
            )

        with _details_block(f, "Results"):
            _write_table(
                f,
                ["Metric", "Value"],
                [
                    ["Accuracy (exact match)", f"{test_eval.exact_match:.1%}"],
                    ["True Positives", test_eval.total_tp],
                    ["False Positives", test_eval.total_fp],
                    ["False Negatives", test_eval.total_fn],
                    ["Total Gold Entities", test_eval.total_tp + test_eval.total_fn],
                    ["Micro Precision", f"{test_eval.micro_precision:.1%}"],
                    ["Micro Recall", f"{test_eval.micro_recall:.1%}"],
                    ["Micro F1", f"{test_eval.micro_f1:.1%}"],
                    ["Macro F1", f"{test_eval.macro_f1:.1%}"],
                ],
            )


def _classify_rules(metrics_list, top_n=10):
    with_matches = [m for m in metrics_list if m.matches > 10]
    no_matches_ids = {m.rule_id for m in metrics_list if m.matches == 0}
    best = sorted(
        [m for m in with_matches if m.true_positives >= 5],
        key=lambda m: (m.precision, m.true_positives),
        reverse=True,
    )[:top_n]
    best_ids = {m.rule_id for m in best}
    worst = sorted(
        [m for m in with_matches if m.rule_id not in best_ids],
        key=lambda m: (-m.false_positives, m.precision),
    )[:top_n]
    worst_ids = {m.rule_id for m in worst}
    return best_ids, worst_ids, no_matches_ids


def _rule_badge(rule_id, best_ids, worst_ids, no_matches_ids):
    if rule_id in best_ids:
        return "🏆"
    if rule_id in worst_ids:
        return "💣"
    if rule_id in no_matches_ids:
        return "🔇"
    return ""


def _write_rule_detail(
    f, metric, rules_by_id: dict, top_n_examples: int = 30, badge: str = ""
) -> None:
    f.write(f"## `{metric.rule_name}` {badge}\n\n")
    f.write(
        f"**F1:** {metric.f1:.3f} | "
        f"**Precision:** {metric.precision:.3f} | "
        f"**Recall:** {metric.recall:.3f}  \n\n"
    )

    rule = rules_by_id.get(metric.rule_id)
    if rule:
        f.write(f"**Format:** `{rule.format.value}`  \n")
        f.write(f"**Rule ID:** `{rule.id}`  \n")
        f.write(f"**Description:**\n{rule.description}\n\n")
        f.write(f"**Content:**\n```\n{rule.content}\n```\n\n")

    with _details_block(f, "📊 Detailed Metrics"):
        _write_table(
            f,
            ["Precision", "Recall", "F1", "Total Predicted", "TP", "FP"],
            [
                [
                    f"{metric.precision:.3f}",
                    f"{metric.recall:.3f}",
                    f"{metric.f1:.3f}",
                    metric.matches,
                    metric.true_positives,
                    metric.false_positives,
                ]
            ],
        )
        if metric.per_class:
            f.write("**Per-Class Breakdown**\n\n")
            _write_table(
                f,
                ["Class", "TP", "FP", "FN"],
                [[f"`{c.label}`", c.tp, c.fp, c.fn] for c in metric.per_class],
            )

    if metric.sample_matches:
        _write_sample_blocks(f, metric, top_n_examples)


def _dedup_samples(samples):
    seen = set()
    result = []
    for s in samples:
        key = s.input.get("sent_id") or s.input.get("text", "")
        if key not in seen:
            seen.add(key)
            result.append(s)
    return result


def _write_sample_blocks(f, metric, top_n: int):
    hits = _dedup_samples([s for s in metric.sample_matches if s.tp > 0])[:top_n]
    fps = _dedup_samples([s for s in metric.sample_matches if s.fp > 0])[:top_n]

    def _block(title, samples, render_fn):
        if not samples:
            return
        with _details_block(f, f"{title}"):
            for i, sample in enumerate(samples):
                render_fn(i, sample)

    def render_hit(i, sample):
        doc_id = sample.input.get("doc_id", "")
        sent_id = sample.input.get("sent_id", "")
        f.write(f"**Example {i}** (doc_id: `{doc_id}`) (sent_id: `{sent_id}`)\n\n")
        f.write(f"\n{sample.input['text']}\n\n")
        matched_gold_texts = {gold["text"] for _, gold in (sample.matched_pairs or [])}
        _write_table(
            f,
            ["Predicted", "Gold"],
            [
                [f"`{pred['text']}`", f"`{gold['text']}`"]
                for pred, gold in sample.matched_pairs
            ],
        )
        missed = [
            g for g in (sample.expected or []) if g["text"] not in matched_gold_texts
        ]
        if missed:
            f.write("**Missed by this rule (FN):**\n\n")
            for g in missed:
                f.write(f"- `{g['text']}` ({g.get('type', '')})\n")
            f.write("\n")

    def render_fp(i, sample):
        doc_id = sample.input.get("doc_id", "")
        sent_id = sample.input.get("sent_id", "")
        f.write(f"**Example {i}** (doc_id: `{doc_id}`) (sent_id: `{sent_id}`)\n\n")
        f.write(f"\n{sample.input['text']}\n\n")

        counts = {"overlap": 0, "missing annotation": 0}
        f.write("**False Positives:**\n\n")
        for e in sample.false_positives:
            reason = classify_fp(e, sample.expected)
            if reason.startswith("no gold match"):
                counts["missing annotation"] += 1
            else:
                counts["overlap"] += 1
            f.write(f"- `{e['text']}` — {reason}\n")

        f.write(
            f"\n> overlaps gold: {counts['overlap']}  |  "
            f"likely missing annotation: {counts['missing annotation']}\n\n"
        )

        matched_gold_texts = {gold["text"] for _, gold in (sample.matched_pairs or [])}
        if sample.expected:
            f.write("**Gold Entities:**\n\n")
            for g in sample.expected:
                f.write(f"- `{g['text']}`({g.get('type', '')})\n")
            f.write("\n")

    _block("✅ Worked", hits, render_hit)
    _block("⚠️ False Positives", fps, render_fp)


def append_rule_metrics(
    file_path: Path,
    metrics_list,
    rules=None,
    top_n_examples: int = 15,
) -> None:
    rules_by_id = {r.id: r for r in rules} if rules else {}
    best_ids, worst_ids, no_matches_ids = _classify_rules(metrics_list)
    sorted_metrics = sorted(metrics_list, key=lambda m: m.precision, reverse=True)

    with file_path.open("a", encoding="utf-8") as f:
        with _details_block(f, "📋 All Rules"):
            for metric in sorted_metrics:
                badge = _rule_badge(metric.rule_id, best_ids, worst_ids, no_matches_ids)
                _write_rule_detail(f, metric, rules_by_id, top_n_examples, badge=badge)


def create_md_report(
    file_path: Path,
    apply_rules_fn,
    run,
    test_dataset,
    results_folder,
    title="Rule Evaluation Report",
    exclude_rule_ids: set[str] | None = None,
):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        f"# {title}\n\nGenerated on: {datetime.now().isoformat()}\n\n---\n\n",
        encoding="utf-8",
    )

    exclude = exclude_rule_ids or set()
    rules = [r for r in run.rules if r.id not in exclude]

    append_overall_metrics(
        file_path, apply_rules_fn, test_dataset, run, results_folder, rules=rules
    )
    rule_metrics = evaluate_rules_individually(
        rules,
        test_dataset,
        apply_rules_fn,
        mode="text",
        max_samples=100,
        in_context=True,
    )
    write_summary_table(file_path, rule_metrics)

    append_rule_metrics(
        file_path,
        rule_metrics,
        top_n_examples=100,
        rules=rules,
    )

    print(f"Report saved to {file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Markdown report from a saved rules JSON and test data"
    )
    parser.add_argument(
        "--rules-json",
        type=str,
        required=True,
        help="Path to results JSON containing rules",
    )
    parser.add_argument(
        "--test-dir", type=str, required=True, help="Path to test data (JSON format)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output .md path (default: <rules-json>.rules_report.md)",
    )
    parser.add_argument(
        "--dataset-name",
        type=str,
        default="findok",
        help="Name of the dataset",
    )

    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1")
    parser.add_argument(
        "--exclude-rule-ids",
        type=str,
        nargs="*",
        default=[],
        help="Rule IDs to exclude from the report",
    )
    args = parser.parse_args()

    # 1. Load rules

    saved = json.loads(Path(args.rules_json).read_text())
    rules = deserialize_rules(saved["rules"])
    print(f"Loaded {len(rules)} rules")

    config = saved.get("config", {})

    selected_classes = config.get("selected_classes", ["organisation"])
    task = Task(
        name="German Legal Named Entity Recognition",
        description=f"Recognize named entities in German legal text. Entities to look for: {', '.join(sorted(selected_classes))}. German capitalizes all nouns, so rules must use strong context anchors ",
        input_schema={"text": "str"},
        output_schema=NEROutput,
        type=TaskType.NER,
        text_field="text",
    )
    executor = RuleExecutor()

    results_folder = os.path.dirname(args.rules_json)
    test_data_raw = load_ner_dataset_from_conll(
        args.test_dir,
    )
    test_data = [
        {
            "text": sent.text,
            "entities": sent.labels,
            "sent_id": sent.sent_id,
            "doc_id": s.doc_id,
        }
        for s in test_data_raw.samples
        for sent in s.sentences
    ]

    test_dataset = make_dataset(f"{args.dataset_name}_eval", test_data, task)
    print(f"Loaded {len(test_data_raw.samples)} test documents")
    print(f"Loaded {len(test_data)} test annotations")
    gold_count = sum(len(item["entities"]) for item in test_data)
    print(f"Gold entities in test_data: {gold_count}")
    person_count = sum(
        1 for item in test_data for e in item["entities"] if e["type"] == "person"
    )
    print(f"Person entities in test_data: {person_count}")

    md_path = (
        Path(args.output)
        if args.output
        else Path(args.rules_json).with_suffix(".rules_report.md")
    )

    run_args = SimpleNamespace(
        **{**config, "no_grex": not config.get("use_grex", True)}
    )

    benchmark_run = BenchmarkRun(
        args=run_args,
        train_data=[],
        eval_data=[],
        test_data=test_data,
        train_size=config.get("train_size", 0),
        eval_size=config.get("eval_size", 0),
        test_size=len(test_data_raw.samples),
        train_annotations=config.get("train_annotations", 0),
        eval_annotations=config.get("eval_annotations", 0),
        test_annotations=len(test_data),
        iteration_metrics=[],
        batch_test_metrics=[],
        eval_results=None,
        t_learn=0.0,
        t_eval=0.0,
        selected_classes=config.get("selected_classes", []),
        rules=rules,
    )
    print("Creating now")

    create_md_report(
        md_path,
        apply_rules_fn=executor.apply_rules,
        run=benchmark_run,
        test_dataset=test_dataset,
        results_folder=results_folder,
        title=f"Rule Evaluation Report — {config.get('model', 'unknown')}",
        exclude_rule_ids=set(args.exclude_rule_ids),
    )


if __name__ == "__main__":
    main()
