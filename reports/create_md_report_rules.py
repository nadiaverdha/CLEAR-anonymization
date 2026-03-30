import json
import uuid
from datetime import datetime
from pathlib import Path

from rulechef import RuleChef
from rulechef.core import (
    Dataset,
    Example,
    RuleFormat,
    Task,
    TaskType,
)
from rulechef.evaluation import evaluate_dataset, evaluate_rules_individually
from rulechef.executor import RuleExecutor

from benchmarks.findok_utils import load_findok, sample_few_shot
from clear_anonymization.utils.utils import NEROutput


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


def append_overall_metrics(
    md_path,
    test_data,
    test_dataset,
    rules,
    chef,
    task,
    shots,
    train_sample,
    model,
    max_rules,
    max_samples,
    max_iterations,
    seed,
    agentic,
    enable_critic,
    enable_prune,
    critic_interval,
    audit_interval,
    use_grex,
    sampling_strategy,
    pool_size,
    train_ratio,
    test_ratio,
):

    test_eval = evaluate_dataset(
        rules,
        test_dataset,
        chef.learner._apply_rules,
    )
    # Coverage = what % of test queries got ANY prediction (TP + FP) / total
    coverage = (
        (test_eval.total_tp + test_eval.total_fp) / len(test_data) if test_data else 0
    )
    with md_path.open("a", encoding="utf-8") as f:
        # Configuration table
        f.write("### Configuration\n\n")
        f.write("| Parameter | Value |\n")
        f.write("|-----------|-------|\n")
        f.write(f"| Pool size | {pool_size} |\n")
        f.write(f"| Train ratio | {train_ratio:.2f} |\n")
        f.write(f"| Test ratio | {test_ratio:.2f} |\n")
        f.write(f"| Shots per class | {shots} |\n")
        f.write(f"| Training examples | {len(train_sample)} |\n")
        f.write(f"| Test examples | {len(test_data)} |\n")
        f.write(f"| Model | {model} |\n")
        f.write(f"| Max rules | {max_rules} |\n")
        f.write(f"| Max samples in prompt | {max_samples} |\n")
        f.write(f"| Refinement iterations | {max_iterations} |\n")
        f.write(f"| Seed | {seed} |\n")
        f.write(f"| Agentic | {agentic}|\n")
        f.write(f"| Enable Critic | {enable_critic} |\n")
        f.write(f"| Enable Prune | {enable_prune}|\n")
        f.write(f"| Critic Interval | {critic_interval} |\n")
        f.write(f"| Audit Interval | {audit_interval}|\n")
        f.write(f"| Use GREX | {use_grex} |\n\n")

        # Results table
        f.write("### Results\n\n")
        f.write("| Metric | Value |\n")
        f.write("|--------|-------|\n")
        f.write(f"| Accuracy (exact match) | {test_eval.exact_match:.1%} |\n")
        f.write(
            f"| Coverage | {coverage:.1%} ({test_eval.total_tp + test_eval.total_fp}/{len(test_data)} got a label) |\n"
        )
        f.write(f"| Micro Precision | {test_eval.micro_precision:.3f} |\n")
        f.write(f"| Micro Recall | {test_eval.micro_recall:.3f} |\n")
        f.write(f"| Micro F1 | {test_eval.micro_f1:.3f} |\n")
        f.write(f"| Macro F1 | {test_eval.macro_f1:.3f} |\n\n")

        f.write("---\n\n")


def append_rule_metrics(
    file_path: Path, metrics_list, top_n_examples: int = 5, rules=None
):
    with file_path.open("a", encoding="utf-8") as f:
        write_summary_table(f, metrics_list)

        metrics_list = sorted(metrics_list, key=lambda m: m.f1, reverse=True)

        rules_by_id = {r.id: r for r in rules} if rules else {}

        for metric in metrics_list:
            score = classify_rule(metric)
            f.write(f"## `{metric.rule_name}`\n\n")
            f.write(f"{score} rule\n\n")

            f.write(
                f"**F1:** {metric.f1:.3f} | "
                f"**Precision:** {metric.precision:.3f} | "
                f"**Recall:** {metric.recall:.3f}  \n\n"
            )

            rule = rules_by_id.get(metric.rule_id)
            if rule:
                f.write(f"**Format:** `{rule.format.value}`  \n")
                f.write(f"**Content:**\n```\n{rule.content}\n```\n\n")

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
                hits = [s for s in metric.sample_matches if s["tp"] > 0]
                misses = [
                    s
                    for s in metric.sample_matches
                    if len(s.get("expected", [])) - s["tp"] > 0
                ]
                f_p = [s for s in metric.sample_matches if s["fp"] > 0]

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
                    f.write(f"```\n{sample['input']['text']}\n```\n\n")
                    pred_texts = {e["text"] for e in sample["rule_output"]}
                    gold_texts = {e["text"] for e in sample["expected"]}
                    f.write("| Prediction | Gold |\n")
                    f.write("|------------|------|\n")
                    for t in pred_texts & gold_texts:
                        f.write(f"| `{t}` | `{t}` |\n")
                    f.write("\n")

                def render_miss(f, i, sample):
                    f.write(f"```\n{sample['input']['text']}\n```\n\n")
                    pred_texts = {e["text"] for e in sample["rule_output"]}
                    for e in sample["expected"]:
                        if e["text"] not in pred_texts:
                            f.write(
                                f"- Missed: `{e['text']}` ({e.get('type', '')})\n\n"
                            )
                    f.write("\n")

                def render_f_p(f, i, sample):
                    f.write(f"```\n{sample['input']['text']}\n```\n\n")
                    gold_texts = {e["text"] for e in sample["expected"]}
                    for e in sample["rule_output"]:
                        if e["text"] not in gold_texts:
                            f.write(f"- FP: `{e['text']}` ({e.get('type', '')})\n\n")
                    f.write("\n")

                write_block("✅ Worked", hits, render_hit)
                write_block("❌ Missed", misses, render_miss)
                write_block("⚠️ False Positives", f_p, render_f_p)

            f.write("---\n\n")
