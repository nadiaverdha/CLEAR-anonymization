import json
from datetime import datetime
from pathlib import Path

from rulechef.core import Dataset, Rule, RuleFormat, TaskType
from rulechef.evaluation import evaluate_rules_individually, print_rule_metrics
from rulechef.executor import RuleExecutor


def create_md_report(file_path: Path, title="Rule Evaluation Report"):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Generated on: {datetime.now().isoformat()}\n\n")
        f.write("---\n\n")


def append_rule_metrics(file_path: Path, metrics_list, top_n_examples: int = 5):
    with file_path.open("a", encoding="utf-8") as f:
        for metric in metrics_list:
            f.write(f"## Rule: `{metric.rule_name}`\n\n")

            if metric.rule_description:
                f.write(f"> {metric.rule_description}\n\n")

            f.write(
                f"**Format:** `{metric.rule_format}` | **Content:** `{metric.rule_content}`\n\n"
            )

            # Overall metrics table
            f.write("### Overall Metrics\n\n")
            f.write(
                "| Precision | Recall | F1 | Matches | TP | FP | Covered / Total Expected |\n"
            )
            f.write(
                "|-----------|--------|----|---------|----|----|---------------------------|\n"
            )
            f.write(
                f"| {metric.precision:.3f} | {metric.recall:.3f} | {metric.f1:.3f} "
                f"| {metric.matches} | {metric.true_positives} | {metric.false_positives} "
                f"| {metric.covered_expected} / {metric.total_expected} |\n\n"
            )

            # Per-class breakdown
            if metric.per_class:
                f.write("### Per-Class Breakdown\n\n")
                f.write("| Class | TP | FP | FN |\n")
                f.write("|-------|----|----|----|\n")
                for cls in metric.per_class:
                    f.write(f"| `{cls.label}` | {cls.tp} | {cls.fp} | {cls.fn} |\n")
                f.write("\n")

            if metric.sample_matches:
                hits = [s for s in metric.sample_matches if s.tp > 0]
                misses = [s for s in metric.sample_matches if s.fn > 0]
                overfired = [s for s in metric.sample_matches if s.fp > 0]

                if hits:
                    f.write(
                        f"### ✅ Examples Where Rule Worked (showing {min(len(hits), top_n_examples)})\n\n"
                    )
                    for i, sample in enumerate(hits[:top_n_examples], 1):
                        f.write(f"**Example {i}**\n\n")
                        f.write(f"```\n{str(sample.input['text'])}\n```\n\n")
                        f.write("| Matched Prediction | Gold Entity |\n")
                        f.write("|--------------------|-------------|\n")
                        for pred, gold in sample.matched_pairs:
                            f.write(f"| `{pred['text']}` | `{gold['text']}` |\n")
                        f.write("\n")

                if misses:
                    f.write(
                        f"### ❌ Examples Where Rule Missed (showing {min(len(misses), top_n_examples)})\n\n"
                    )
                    for i, sample in enumerate(misses[:top_n_examples], 1):
                        f.write(f"```\n{str(sample.input['text'])}\n```\n\n")
                        f.write(f"- **Missed entities:** `{sample.missed}`\n\n")

                if overfired:
                    f.write(
                        f"### ⚠️ Examples Where Rule Over-fired (showing {min(len(overfired), top_n_examples)})\n\n"
                    )
                    for i, sample in enumerate(overfired[:top_n_examples], 1):
                        f.write(f"**Example {i}**\n\n")
                        f.write(f"```\n{str(sample.input['text'])}\n```\n\n")
                        f.write(
                            f"- **Spurious predictions:** `{sample.false_positives}`\n"
                        )

            f.write("---\n\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Evaluate RuleChef rules and generate Markdown report"
    )
    parser.add_argument(
        "--rules_file", type=str, required=True, help="JSON file with rules"
    )
    parser.add_argument(
        "--data_file", type=str, required=False, help="JSON file with evaluation data"
    )
    parser.add_argument(
        "--output_md", type=str, default=None, help="Path to save Markdown report"
    )
    parser.add_argument(
        "--max_samples", type=int, default=5, help="Max sample matches per rule"
    )
    parser.add_argument(
        "--mode", type=str, default="text", choices=["text", "exact"], help="Match mode"
    )
    args = parser.parse_args()

    data = json.loads(Path(args.rules_file).read_text())
    dataset = Dataset.from_dict(data)

    if args.output_md:
        md_path = Path(args.output_md)
    else:
        date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        md_path = Path(f"reports/{date_str}_rule_eval.md")

    create_md_report(md_path, title=f"Rule Evaluation Report — {dataset.task.type}")

    executor = RuleExecutor()

    all_metrics = evaluate_rules_individually(
        rules=dataset.rules,
        dataset=dataset,
        apply_rules_fn=executor.apply_rules,
        mode=args.mode,
        max_samples=args.max_samples,
    )

    append_rule_metrics(md_path, all_metrics, top_n_examples=args.max_samples)

    print(f"✅ Markdown report saved to: {md_path.resolve()}")
    print(f"   Rules evaluated: {len(all_metrics)}")


if __name__ == "__main__":
    main()
