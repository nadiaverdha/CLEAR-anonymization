import json
from datetime import datetime
from pathlib import Path

from rulechef.core import Dataset
from rulechef.evaluation import evaluate_rules_individually
from rulechef.executor import RuleExecutor


def classify_rule(metric):
    if metric.f1 >= 0.8:
        return "🟢 Strong"
    elif metric.f1 >= 0.5:
        return "🟡 Medium"
    else:
        return "🔴 Weak"


def write_summary_table(f, metrics_list):
    f.write("## 📊 Summary\n\n")
    f.write("| Rule | Score | F1 | Precision | Recall | Matches |\n")
    f.write("|------|-------|----|----------|--------|--------|\n")

    sorted_metrics = sorted(metrics_list, key=lambda m: m.f1, reverse=True)

    for m in sorted_metrics:
        score = classify_rule(m)
        f.write(
            f"| `{m.rule_name}` | {score} | {m.f1:.3f} | "
            f"{m.precision:.3f} | {m.recall:.3f} | {m.matches} |\n"
        )

    f.write("\n---\n\n")


def create_md_report(file_path: Path, title="Rule Evaluation Report"):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Generated on: {datetime.now().isoformat()}\n\n")
        f.write("### Legend\n")
        f.write("🟢 Strong (F1 ≥ 0.8)  \n")
        f.write("🟡 Medium (0.5 ≤ F1 < 0.8)  \n")
        f.write("🔴 Weak (F1 < 0.5)\n\n")

        f.write("---\n\n")


def append_rule_metrics(file_path: Path, metrics_list, top_n_examples: int = 5):
    with file_path.open("a", encoding="utf-8") as f:
        write_summary_table(f, metrics_list)

        metrics_list = sorted(metrics_list, key=lambda m: m.f1, reverse=True)

        for metric in metrics_list:
            score = classify_rule(metric)
            f.write(f"## `{metric.rule_name}`\n\n")
            f.write(f"{score} rule\n\n")

            if metric.rule_description:
                f.write(f"> {metric.rule_description}\n\n")

            f.write(
                f"**F1:** {metric.f1:.3f} | "
                f"**Precision:** {metric.precision:.3f} | "
                f"**Recall:** {metric.recall:.3f}  \n\n"
            )

            f.write(
                f"**Format:** `{metric.rule_format}`  \n"
                f"**Content:** `{metric.rule_content}`\n\n"
            )

            f.write("<details>\n<summary>📊 Detailed Metrics</summary>\n\n")

            f.write("| Precision | Recall | F1 | Matches | TP | FP | Coverage |\n")
            f.write("|-----------|--------|----|---------|----|----|----------|\n")
            f.write(
                f"| {metric.precision:.3f} | {metric.recall:.3f} | {metric.f1:.3f} "
                f"| {metric.matches} | {metric.true_positives} | {metric.false_positives} "
                f"| {metric.covered_expected}/{metric.total_expected} |\n\n"
            )

            if metric.per_class:
                f.write("**Per-Class Breakdown**\n\n")
                f.write("| Class | TP | FP | FN |\n")
                f.write("|-------|----|----|----|\n")
                for cls in metric.per_class:
                    f.write(f"| `{cls.label}` | {cls.tp} | {cls.fp} | {cls.fn} |\n")
                f.write("\n")

            f.write("</details>\n\n")

            if metric.sample_matches:
                hits = [s for s in metric.sample_matches if s.tp > 0]
                misses = [s for s in metric.sample_matches if s.fn > 0]
                f_p = [s for s in metric.sample_matches if s.fp > 0]

                def write_block(title, samples, render_fn):
                    if not samples:
                        return

                    f.write(
                        f"<details>\n<summary>{title} ({min(len(samples), top_n_examples)})</summary>\n\n"
                    )

                    for i, sample in enumerate(samples[:top_n_examples], 1):
                        render_fn(f, i, sample)

                    f.write("</details>\n\n")

                def render_hit(f, i, sample):
                    f.write(f"**Example {i}**\n\n")
                    f.write(f"```\n{sample.input['text']}\n```\n\n")
                    f.write("| Prediction | Gold |\n")
                    f.write("|------------|------|\n")
                    for pred, gold in sample.matched_pairs:
                        f.write(f"| `{pred['text']}` | `{gold['text']}` |\n")
                    f.write("\n")

                def render_miss(f, i, sample):
                    f.write(f"```\n{sample.input['text']}\n```\n\n")
                    for miss in sample.missed:
                        f.write(f"- Missed: `{miss['text']}`\n\n")
                    f.write("\n")

                def render_f_p(f, i, sample):
                    f.write(f"```\n{sample.input['text']}\n```\n\n")
                    for false_p in sample.false_positives:
                        f.write(f"- FP: `{false_p['text']}`\n\n")
                    f.write("\n")

                write_block("✅ Worked", hits, render_hit)
                write_block("❌ Missed", misses, render_miss)
                write_block("⚠️ False Positives", f_p, render_f_p)

            f.write("---\n\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Evaluate RuleChef rules and generate Markdown report"
    )
    parser.add_argument("--rules_file", type=str, required=True)
    parser.add_argument("--dataset_name", default="FinD", type=str, required=True)
    parser.add_argument("--data_file", type=str, required=False)
    parser.add_argument("--output_md", type=str, default=None)
    parser.add_argument("--max_samples", type=int, default=10)
    parser.add_argument("--mode", type=str, default="text", choices=["text", "exact"])

    args = parser.parse_args()

    data = json.loads(Path(args.rules_file).read_text())
    dataset = Dataset.from_dict(data)

    if args.output_md:
        md_path = Path(args.output_md)
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
        md_path = Path(f"reports/{date_str}_{args.dataset_name}_rule_eval.md")

    create_md_report(md_path, title=f"Rule Evaluation Report — {args.dataset_name}")

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
