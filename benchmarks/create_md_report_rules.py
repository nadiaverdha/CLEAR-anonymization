import argparse
import json
import os
import re
import tempfile
import uuid
from asyncio import run
from asyncio.log import logger
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

from openai import OpenAI
from rulechef import RuleChef
from rulechef.core import (
    Dataset,
    Example,
    Rule,
    RuleFormat,
    Task,
    TaskType,
)
from rulechef.evaluation import evaluate_dataset, evaluate_rules_individually
from rulechef.executor import RuleExecutor

from benchmarks.util import BenchmarkRun, make_dataset
from clear_anonymization.models.nerlearner import NERLearner, NEROutput
from clear_anonymization.ner_datasets import (
    get_dataset_class_definitions,
    load_ner_dataset_from_conll,
    load_ner_dataset_from_json,
)
from clear_anonymization.ner_datasets.ner_dataset import NERData
from clear_anonymization.preprocess.sampling import sample_few_shot


@contextmanager
def _details_block(f, summary: str):
    f.write(f"<details>\n<summary>{summary}</summary>\n\n")
    yield
    f.write("</details>\n\n---\n\n")


@contextmanager
def _normal_block(f, summary: str):
    f.write(f"\n<summary>{summary}</summary>\n\n")
    yield
    f.write("\n\n---\n\n")


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


def append_overall_metrics(md_path, chef, test_dataset, run, results_folder):
    config = run.args

    test_eval = evaluate_dataset(
        run.rules,
        test_dataset,
        chef.learner._apply_rules,
        mode="text",
    )
    with md_path.open("a", encoding="utf-8") as f:
        with _details_block(f, "Configuration"):
            f.write("Results can be reproduced by running this command: \n")
            f.write(
                f"```\n python benchmark.py --config {results_folder}/config.yaml \n```\n"
            )
            _write_table(
                f,
                ["Parameter", "Value"],
                [
                    ["Pool size", config.pool_size],
                    ["Train ratio", f"{config.train_ratio:.2f}"],
                    ["Validation ratio", f"{1.0 - config.train_ratio:.2f}"],
                    ["Shots per class", config.shots],
                    ["Training examples", run.train_size],
                    ["Validation examples", run.eval_size],
                    ["Test examples", run.test_size],
                    ["Train annotations", run.train_annotations],
                    ["Validation annotations", run.eval_annotations],
                    ["Test annotations", run.test_annotations],
                    ["Model", config.model],
                    ["Max rules", config.max_rules],
                    ["Max samples in prompt", config.max_samples],
                    ["Refinement iterations", config.max_iterations],
                    ["Seed", config.seed],
                    ["Agentic", config.agentic],
                    ["Enable Critic", config.enable_critic],
                    ["Enable Prune", config.enable_prune],
                    ["Critic Interval", config.critic_interval],
                    ["Audit Interval", config.audit_interval],
                    [
                        "Use GREX",
                        not config.no_grex,
                    ],
                ],
            )

        with _details_block(f, "Results"):
            _write_table(
                f,
                ["Metric", "Value"],
                [
                    ["Accuracy (exact match)", f"{test_eval.exact_match:.1%}"],
                    ["True Positives", test_eval.total_tp],
                    ["False Positives", test_eval.total_fp],
                    ["Micro Precision", f"{test_eval.micro_precision:.1%}"],
                    ["Micro Recall", f"{test_eval.micro_recall:.1%}"],
                    ["Micro F1", f"{test_eval.micro_f1:.1%}"],
                    ["Macro F1", f"{test_eval.macro_f1:.1%}"],
                ],
            )


def _write_rule_detail(f, metric, rules_by_id: dict, top_n_examples: int = 5) -> None:
    f.write(f"## `{metric.rule_name}`\n\n")
    f.write(
        f"**F1:** {metric.f1:.3f} | "
        f"**Precision:** {metric.precision:.3f} | "
        f"**Recall:** {metric.recall:.3f}  \n\n"
    )

    rule = rules_by_id.get(metric.rule_id)
    if rule:
        f.write(f"**Format:** `{rule.format.value}`  \n")
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

    # f.write("---\n\n")


def _expand_to_word_boundary(text: str, left: int, right: int) -> tuple[int, int]:
    while left > 0 and text[left] not in " \n\t":
        left -= 1
    while right < len(text) and text[right - 1] not in " \n\t":
        right += 1

    return left, right


def _context_window(text: str, start: int, end: int, window: int = 60) -> str:
    left = max(0, start - window)
    right = min(len(text), end + window)
    left, right = _expand_to_word_boundary(text, left, right)

    snippet = text[left:right]

    entity = text[start:end]
    snippet = snippet.replace(entity, f"<<<{entity}>>>")

    if left > 0:
        snippet = "..." + snippet
    if right < len(text):
        snippet = snippet + "..."

    return snippet


def _write_sample_blocks(f, metric, top_n: int):

    hits = [s for s in metric.sample_matches if s.tp > 0]
    fps = [s for s in metric.sample_matches if s.fp > 0]

    def _block(title, samples, render_fn):
        if not samples:
            return
        with _details_block(f, f"{title}"):
            for i, sample in enumerate(samples[:top_n]):
                render_fn(i, sample)

    def render_hit(i, sample):
        doc_id = sample.input.get("doc_id", "")
        f.write(f"**Example {i}** (doc_id: `{doc_id}`)\n\n")
        text = sample.input["text"]

        for pred, gold in sample.matched_pairs[:top_n]:
            f.write(
                f"```\n{_context_window(text, pred['start'], pred['end'])}\n```\n\n"
            )
        _write_table(
            f,
            ["Predicted", "Gold"],
            [
                [f"`{pred['text']}`", f"`{gold['text']}`"]
                for pred, gold in sample.matched_pairs[:top_n]
            ],
        )

    def render_fp(i, sample):
        doc_id = sample.input.get("doc_id", "")
        f.write(f"**Example {i}** (doc_id: `{doc_id}`)\n\n")
        text = sample.input["text"]

        f.write("**False Positives:**\n\n")
        for e in sample.false_positives[:top_n]:
            f.write(f"```\n{_context_window(text, e['start'], e['end'])}\n```\n\n")

            f.write(f"FP: `{e['text']}` ({e.get('type', '')})\n\n")

        f.write("**✅ Gold Entities:**\n")
        for g in sample.expected:
            f.write(f"- `{g['text']}` ({g.get('type', '')})\n")

        f.write("\n")

    _block("✅ Worked", hits, render_hit)
    _block("⚠️ False Positives", fps, render_fp)


def append_influential_rules(
    md_path: Path, metrics_list, rules, top_n: int = 5
) -> None:
    rules_by_id = {r.id: r for r in rules} if rules else {}
    with_matches = [m for m in metrics_list if m.matches > 5]
    no_matches = [m for m in metrics_list if m.matches == 0][:top_n]

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

    with md_path.open("a", encoding="utf-8") as f:
        print(f"Best rules:  {[m.rule_name for m in best]}")
        with _details_block(f, "🏆 Most Precise Rules"):
            for m in best:
                _write_rule_detail(f, m, rules_by_id)

        print(f"Worst rules: {[m.rule_name for m in worst]}")
        with _details_block(f, "💣 Least Precise Rules"):
            for m in worst:
                _write_rule_detail(f, m, rules_by_id)

        print(f"Inactive rules: {[m.rule_name for m in no_matches]}")
        with _details_block(f, "🔇 Inactive Rules"):
            for m in no_matches:
                _write_rule_detail(f, m, rules_by_id)


def append_rule_metrics(
    file_path: Path,
    metrics_list,
    rules=None,
    top_n_examples: int = 5,
) -> None:
    rules_by_id = {r.id: r for r in rules} if rules else {}
    sorted_metrics = sorted(metrics_list, key=lambda m: m.f1, reverse=True)

    with file_path.open("a", encoding="utf-8") as f:
        with _details_block(f, "📋 All Rules"):
            for metric in sorted_metrics:
                _write_rule_detail(f, metric, rules_by_id, top_n_examples)


def create_md_report(
    file_path: Path,
    chef,
    run,
    test_dataset,
    results_folder,
    title="Rule Evaluation Report",
):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        f"# {title}\n\nGenerated on: {datetime.now().isoformat()}\n\n---\n\n",
        encoding="utf-8",
    )

    append_overall_metrics(file_path, chef, test_dataset, run, results_folder)

    rule_metrics = evaluate_rules_individually(
        rules=run.rules,
        dataset=test_dataset,
        apply_rules_fn=chef.learner._apply_rules,
        mode="text",
        max_samples=run.args.max_samples,
        iou_threshold=0.5,
    )
    write_summary_table(file_path, rule_metrics)
    append_influential_rules(file_path, rule_metrics, run.rules, top_n=5)

    append_rule_metrics(
        file_path,
        rule_metrics,
        top_n_examples=5,
        rules=run.rules,
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
        "--dataset_name",
        type=str,
        default="findok",
        help="Name of the dataset",
    )

    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1")
    args = parser.parse_args()

    # 1. Load rules

    saved = json.loads(Path(args.rules_json).read_text())
    rules = [
        Rule(
            id=r["id"],
            name=r["name"],
            description=r["description"],
            format=RuleFormat(r["format"]),
            content=r["content"],
            output_template=r.get("output_template"),
            output_key=r.get("output_key"),
        )
        for r in saved["rules"]
    ]
    print(f"Loaded {len(rules)} rules")

    config = saved.get("config", {})

    selected_classes = "organisation"
    learner = NERLearner(
        model=config.get("model"),
        dataset_name=config.get("dataset_name"),
        base_url=config.get("base_url"),
        use_grex=not config.get("no_grex"),
        max_rules=config.get("max_rules"),
        max_samples=config.get("max_samples"),
        max_counter_examples=config.get("max_counter_examples"),
        logger=logger,
        sampling_strategy=config.get("sampling_strategy"),
        synthesis_strategy=config.get("synthesis_strategy"),
        selected_classes=selected_classes,
    )

    results_folder = os.path.dirname(args.rules_json)
    test_data_raw = load_ner_dataset(
        args.test_dir,
    )

    test_data = [
        {
            "text": s.text,
            "entities": s.labels,
            "doc_id": s.doc_id,
            "sentences": [
                {"text": sent.text, "labels": sent.labels}
                for sent in (s.sentences or [])
            ],
        }
        for s in test_data_raw.samples
    ]
    test_dataset = make_dataset(f"{args.dataset_name}_eval", test_data, learner.task)
    print(f"Loaded {len(test_data)} test examples")

    md_path = (
        Path(args.output)
        if args.output
        else Path(args.rules_json).with_suffix(".rules_report.md")
    )

    run_args = SimpleNamespace(
        **{**config, "no_grex": not config.get("use_grex", True)}
    )
    test_annotations = sum(len(ex["entities"]) for ex in test_data)
    benchmark_run = BenchmarkRun(
        args=run_args,
        train_data=[],
        eval_data=[],
        test_data=test_data,
        train_size=config.get("train_size", 0),
        eval_size=config.get("eval_size", 0),
        test_size=len(test_data),
        train_annotations=config.get("train_annotations", 0),
        eval_annotations=config.get("eval_annotations", 0),
        test_annotations=test_annotations,
        iteration_metrics=[],
        eval_results=None,
        t_learn=0.0,
        t_eval=0.0,
        selected_classes=config.get("selected_classes", []),
        rules=rules,
    )

    create_md_report(
        md_path,
        chef=learner,
        run=benchmark_run,
        test_dataset=test_dataset,
        results_folder=results_folder,
        title=f"Rule Evaluation Report — {config.get('model', 'unknown')}",
    )


if __name__ == "__main__":
    main()
