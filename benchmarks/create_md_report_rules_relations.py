import argparse
import json
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

from rulechef.core import Task, TaskType
from rulechef.evaluation import evaluate_dataset, evaluate_rules_individually
from rulechef.executor import RuleExecutor

from benchmarks.data import make_relation_dataset
from benchmarks.io import deserialize_rules
from clear_anonymization.models.relationlearner import (
    RelationOutput,
)
from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.ner_datasets.util import (
    build_relation_examples,
)


# ok
def _details_block(f, summary: str):
    @contextmanager
    def _cm():
        f.write(f"<details>\n<summary>{summary}</summary>\n\n")
        yield
        f.write("</details>\n\n---\n\n")

    return _cm()


# ok
def _write_table(f, headers: list[str], rows: list[list[str]]) -> None:
    f.write("| " + " | ".join(headers) + " |\n")
    f.write("|" + "|".join("---" for _ in headers) + "|\n")
    for row in rows:
        f.write("| " + " | ".join(str(c) for c in row) + " |\n")
    f.write("\n")


def append_overall_metrics(file_path: Path, overall: dict, n_docs: int) -> None:
    with file_path.open("a", encoding="utf-8") as f, _details_block(f, "Results"):
        _write_table(
            f,
            ["Metric", "Value"],
            [
                ["Documents evaluated", n_docs],
                ["True Positives", overall.total_tp],
                ["False Positives", overall.total_fp],
                ["False Negatives", overall.total_fn],
                ["Total Gold Relations", overall.total_tp + overall.total_fn],
                ["Precision", f"{overall.micro_precision:.1%}"],
                ["Recall", f"{overall.micro_recall:.1%}"],
                ["F1", f"{overall.micro_f1:.1%}"],
            ],
        )


# ok
def write_summary_table(file_path: Path, metrics_list) -> None:
    sorted_metrics = sorted(metrics_list, key=lambda m: m.precision, reverse=True)
    rows = [
        [
            f"`{m.rule_name}`",
            f"{m.f1:.1%}",
            f"{m.precision:.1%}",
            f"{m.recall:.1%}",
            m.matches,
            m.true_positives,
            m["false_positives"],
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


def _classify_rules(metrics_list, top_n=10):
    with_matches = [
        m for m in metrics_list if (m.true_positives + m["false_positives"]) > 0
    ]
    no_matches_ids = {
        m.rule_id
        for m in metrics_list
        if (m.true_positives + m["false_positives"]) == 0
    }
    best = sorted(
        [m for m in with_matches if m.true_positives >= 1],
        key=lambda m: (m.precision, m.true_positives),
        reverse=True,
    )[:top_n]
    best_ids = {m.rule_id for m in best}
    worst = sorted(
        [m for m in with_matches if m.rule_id not in best_ids],
        key=lambda m: (-m["false_positives"], m.precision),
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


def _header(f, sample):
    inp = sample["input"]
    f.write(
        f"(doc_id: `{inp.get('doc_id', '')}`) (gov_sent: `{inp.get('gov_sent_id', '')}`, dep_sent: `{inp.get('dep_sent_id', '')}`)\n\n"
    )
    f.write(f"\n{inp.get('display_text', inp.get('text', ''))}\n\n")
    pred_label = sample["rule_output"][0]["label"] if sample["rule_output"] else ""
    gold_label = sample["expected"][0]["label"] if sample["expected"] else ""
    f.write(f"\n{inp.get('text', inp.get('text', ''))}\n\n")
    f.write(f"**Predicted:** `{pred_label}`  **Gold:** `{gold_label}`\n\n")


def _write_sample_blocks(f, metric, top_n: int):
    hits = [m for m in metric.sample_matches if m["matched_pairs"]][:top_n]
    fps = [m for m in metric.sample_matches if m["false_positives"]][:top_n]

    def _block(title, entries):
        if not entries:
            return
        with _details_block(f, title):
            for i, entry in enumerate(entries):
                f.write(f"**Example {i}** ")
                _header(f, entry)

    _block("✅ Worked", hits)
    _block("⚠️ False Positives", fps)


# ok
def _write_rule_detail(f, metric, top_n_examples: int = 30, badge: str = "") -> None:
    f.write(f"## `{metric.rule_name}` {badge}\n\n")
    f.write(
        f"**F1:** {metric.f1:.3f} | **Precision:** {metric.precision:.3f} | **Recall:** {metric.recall:.3f}  \n\n"
    )
    f.write(f"**Format:** `{metric.rule_format}`  \n")
    f.write(f"**Rule ID:** `{metric.rule_id}`  \n")
    f.write(f"**Description:**\n{metric.rule_description}\n\n")
    f.write(f"**Content:**\n```\n{metric.rule_content}\n```\n\n")

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
                    metric["false_positives"],
                ]
            ],
        )

    if metric.sample_matches:
        _write_sample_blocks(f, metric, top_n_examples)


# ok
def append_rule_metrics(
    file_path: Path, metrics_list: list, top_n_examples: int = 15
) -> None:
    best_ids, worst_ids, no_matches_ids = _classify_rules(metrics_list)
    sorted_metrics = sorted(metrics_list, key=lambda m: m.precision, reverse=True)

    with file_path.open("a", encoding="utf-8") as f:
        with _details_block(f, "📋 All Rules"):
            for metric in sorted_metrics:
                badge = _rule_badge(metric.rule_id, best_ids, worst_ids, no_matches_ids)
                _write_rule_detail(f, metric, top_n_examples, badge=badge)


def create_md_report(
    file_path: Path,
    apply_rules_fn,
    run,
    test_dataset,
    results_folder=None,
    title="Relation Rule Evaluation Report",
    exclude_rule_ids: set[str] | None = None,
):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        f"# {title}\n\nGenerated on: {datetime.now().isoformat()}\n\n---\n\n",
        encoding="utf-8",
    )
    exclude = exclude_rule_ids or set()
    rules = [r for r in run.rules if r.id not in exclude]
    overall = evaluate_dataset(rules, test_dataset, apply_rules_fn)
    per_rule = evaluate_rules_individually(
        rules, test_dataset, apply_rules_fn, in_context=True
    )
    n_docs = len({ex["input"]["doc_id"] for ex in test_dataset.examples})
    append_overall_metrics(file_path, overall, n_docs)
    write_summary_table(file_path, per_rule)
    append_rule_metrics(file_path, per_rule, top_n_examples=100)
    print(f"Report saved to {file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate saved relation rules end-to-end (candidate generation + classification) against gold"
    )
    parser.add_argument("--rules-json", default="reports/relations/toy_relations.json")
    parser.add_argument(
        "--conllu",
        default="toy_relations_test.conllu",
    )
    parser.add_argument("--max-sentence-gap", type=int, default=1)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--dataset-name",
        type=str,
        default="findok",
        help="Name of the dataset",
    )
    args = parser.parse_args()
    task = Task(
        name="Relation Extraction",
        description=(
            "The input text contains two marked entity inside tags like <person>, <organization>, etc. "
            "Determine which relation holds between them."
        ),
        input_schema={"text": "str"},
        output_schema=RelationOutput,
        type=TaskType.CLASSIFICATION,
        text_field="text",
    )
    saved = json.loads(Path(args.rules_json).read_text())
    rules = deserialize_rules(saved["rules"])
    print(f"Loaded {len(rules)} rules from {args.rules_json}")

    test_data_raw = load_ner_dataset_from_conll(Path(args.conllu))
    test_data = [
        ex for doc in test_data_raw.samples for ex in build_relation_examples(doc)
    ]

    # print(f"Eval docs={n_eval_docs} labels={sorted(relation_labels)}")
    test_dataset = make_relation_dataset(f"{args.dataset_name}_eval", test_data, task)
    print(f"Loaded {len(test_data_raw.samples)} test documents")
    print(test_dataset[0])
    executor = RuleExecutor()
    create_md_report(
        Path(args.output),
        apply_rules_fn=executor.apply_rules,
        run=SimpleNamespace(rules=rules),
        test_dataset=len(test_data_raw.samples),
    )

    # create_md_report(Path(args.output), overall, per_rule, len(eval_docs))


if __name__ == "__main__":
    main()
