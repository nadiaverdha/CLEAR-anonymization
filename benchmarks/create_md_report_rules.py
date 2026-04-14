import argparse
import json
import tempfile
import uuid
from asyncio import run
from asyncio.log import logger
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

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
    load_ner_dataset,
)
from clear_anonymization.ner_datasets.ner_dataset import NERData
from clear_anonymization.preprocess.sampling import sample_few_shot


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
                    "Matches",
                    "True Positives",
                    "False Positives",
                ],
                rows,
            )


def append_overall_metrics(md_path, chef, test_dataset, run):
    config = run.args

    test_eval = evaluate_dataset(
        run.rules,
        test_dataset,
        chef.learner._apply_rules,
        mode="text",
    )
    with md_path.open("a", encoding="utf-8") as f:
        with _details_block(f, "Configuration"):
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
        f.write(f"**Content:**\n```\n{rule.content}\n```\n\n")

    with _details_block(f, "📊 Detailed Metrics"):
        _write_table(
            f,
            ["Precision", "Recall", "F1", "Matches", "TP", "FP"],
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

    f.write("---\n\n")


def _write_sample_blocks(f, metric, top_n: int) -> None:
    hits = [s for s in metric.sample_matches if s.tp > 0]
    misses = [s for s in metric.sample_matches if s.missed]
    fps = [s for s in metric.sample_matches if s.fp > 0]

    def _block(title, samples, render_fn):
        if not samples:
            return
        with _details_block(f, f"{title} ({min(len(samples), top_n)})"):
            for i, sample in enumerate(samples[:top_n], 1):
                render_fn(i, sample)

    def render_hit(i, sample):
        f.write(f"**Example {i}**\n\n```\n{sample.input['text']}\n```\n\n")
        pred = {e["text"] for e in sample.rule_output}
        gold = {e["text"] for e in sample.expected}
        _write_table(
            f, ["Prediction", "Gold"], [[f"`{t}`", f"`{t}`"] for t in pred & gold]
        )

    def render_miss(_, sample):
        f.write(f"```\n{sample.input['text']}\n```\n\n")
        pred = {e["text"] for e in sample.rule_output}
        for e in sample.missed:
            if e["text"] not in pred:
                f.write(f"- Missed: `{e['text']}` ({e.get('type', '')})\n\n")
        f.write("\n")

    def render_fp(_, sample):
        f.write(f"```\n{sample.input['text']}\n```\n\n")
        gold = {e["text"] for e in sample.expected}
        for e in sample.rule_output:
            if e["text"] not in gold:
                f.write(f"- FP: `{e['text']}` ({e.get('type', '')})\n\n")
        f.write("\n")

    _block("✅ Worked", hits, render_hit)
    _block("❌ Missed", misses, render_miss)
    _block("⚠️ False Positives", fps, render_fp)


def append_influential_rules(
    md_path: Path, metrics_list, rules, top_n: int = 5
) -> None:
    rules_by_id = {r.id: r for r in rules} if rules else {}
    with_matches = [m for m in metrics_list if m.matches > 0]

    best = sorted(with_matches, key=lambda m: m.precision, reverse=True)[:top_n]
    best_ids = {m.rule_id for m in best}
    worst = [
        m
        for m in sorted(with_matches, key=lambda m: m.precision)
        if m.rule_id not in best_ids
    ][:top_n]

    with md_path.open("a", encoding="utf-8") as f:
        print(f"Best rules:  {[m.rule_name for m in best]}")
        with _details_block(f, "🏆 Most Precise Rules"):
            for m in best:
                _write_rule_detail(f, m, rules_by_id)

        print(f"Worst rules: {[m.rule_name for m in worst]}")
        with _details_block(f, "💣 Least Precise Rules"):
            for m in worst:
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
    file_path: Path, chef, run, test_dataset, title="Rule Evaluation Report"
):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        f"# {title}\n\nGenerated on: {datetime.now().isoformat()}\n\n---\n\n",
        encoding="utf-8",
    )

    append_overall_metrics(file_path, chef, test_dataset, run)

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
    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1")
    args = parser.parse_args()

    # 1. Load rules

    saved = json.loads(Path(args.rules_json).read_text())
    rules = [
        Rule(
            id=r["id"],
            name=r["name"],
            description=r.get("description", ""),
            format=RuleFormat(r["format"]),
            content=r["content"],
            priority=r.get("priority", 5),
            output_template=r.get("output_template"),
            output_key=r.get("output_key"),
        )
        for r in saved["rules"]
    ]
    print(f"Loaded {len(rules)} rules")

    test_data_raw = load_ner_dataset(
        args.test_dir,
    )
    test_data = [{"text": s.text, "entities": s.labels} for s in test_data_raw.samples]
    test_dataset = make_dataset(f"{args.dataset_name}_eval", test_data, learner.task)

    print(f"Loaded {len(test_data)} test examples")
    config = saved.get("config", {})
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
        selected_classes=config.get("selected_classes"),
    )

    md_path = (
        Path(args.output)
        if args.output
        else Path(args.rules_json).with_suffix(".rules_report.md")
    )
    benchmark_run = (
        BenchmarkRun(
            args=config,
            test_data=test_data,
            rules=rules,
        ),
    )

    create_md_report(
        md_path,
        chef=learner,
        run=benchmark_run,
        test_dataset=test_dataset,
        title=f"Rule Evaluation Report — {config.get('model', 'unknown')}",
    )


if __name__ == "__main__":
    main()
