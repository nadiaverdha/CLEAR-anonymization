import json
from pathlib import Path
from datetime import datetime
from pathlib import Path
from rulechef.core import Rule, TaskType
from rulechef.core import RuleFormat, Dataset

from rulechef.executor import RuleExecutor
from clear_anonymization.extractors import factory
from rulechef.evaluation import evaluate_rules_individually, print_rule_metrics
from clear_anonymization.utils.utils import *
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample


def create_md_report(file_path: Path, title="Rule Evaluation Report"):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Generated on: {datetime.now().isoformat()}\n\n")
        
def append_rule_metrics(
    file_path: Path, rule , rule_metrics: dict, top_n_examples=5
):
    with file_path.open("a", encoding="utf-8") as f:
        for metric in rule_metrics:
            f.write(f"## Rule: {metric.rule_name}\n\n")
            f.write(f"**Pattern:** `{rule.pattern}`\n\n")
            f.write("| Precision | Recall | F1 |\n")
            f.write("|-----------|-------|----|  \n")
            f.write(
                f"| {metric.precision:.3f} | {metric.recall:.3f} | {metric.f1:.3f} |\n\n"
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
        "--data_file", type=str, required=True, help="JSON file with evaluation data"
    )
    parser.add_argument(
        "--output_md", type=str, default=None, help="Path to save Markdown report"
    )
    args = parser.parse_args()

    data = json.loads(Path(args.rules_file).read_text())
    dataset = Dataset.from_dict(data)
    data_file = Path(args.data_file)
    all_data = NERData.from_json(json.loads(data_file.read_text()))
    train_samples = [s for s in all_data.samples if s.split == "train"]

    if args.output_md:
        md_path = Path(args.output_md)
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
        md_path = Path(f"reports/{date_str}_rule_eval.md")

    create_md_report(md_path)

    executor = RuleExecutor()

    for rule in dataset.rules:
        metrics_per_rule = evaluate_rules_individually(
            rules=[rule],
            dataset=dataset,
            apply_rules_fn=executor.apply_rules,
        )
    
        append_rule_metrics(md_path, rule, metrics_per_rule,)

    print(f"✅ Markdown rule evaluation report saved to: {md_path}")


if __name__ == "__main__":
    main()
