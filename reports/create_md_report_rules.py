import json
from pathlib import Path
from datetime import datetime

from rulechef.core import Rule, TaskType
from rulechef.executor import RuleExecutor
from clear_anonymization.extractors import factory
from rulechef.matching import evaluate_rules_individually_withexamp
from clear_anonymization.utils.utils import *
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample
def create_md_report(file_path: Path, title="Rule Evaluation Report"):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Generated on: {datetime.now().isoformat()}\n\n")
def append_rule_metrics(file_path: Path, rule_metrics: dict, threshold: float, top_n_examples=5):
    with file_path.open("a", encoding="utf-8") as f:
        
        for rule_name, info in rule_metrics.items():
            f.write(f"## Rule: {rule_name}\n\n")  
            f.write(f"### Threshold: {threshold}\n\n")  
            f.write(f"**Pattern:** `{info['pattern']}`\n\n")
            metrics = info["metrics"]
            f.write("| Precision | Recall | F1 |\n")
            f.write("|-----------|-------|----|  \n")
            f.write(f"| {metrics['precision']:.3f} | {metrics['recall']:.3f} | {metrics['f1']:.3f} |\n\n")
            if info.get("FP_examples"):
                f.write("### False Positives\n")
                for ex in info["FP_examples"][:top_n_examples]:
                    f.write(f"- `{ex}`\n")
                f.write("\n")
            if info.get("FN_examples"):
                f.write("### False Negatives\n")
                for ex in info["FN_examples"][:top_n_examples]:
                    f.write(f"- `{ex}`\n")
                f.write("\n")
        f.write("---\n\n")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate RuleChef rules and generate Markdown report")
    parser.add_argument("--rules_file", type=str, required=True, help="JSON file with rules")
    parser.add_argument("--data_file", type=str, required=True, help="JSON file with evaluation data")
    parser.add_argument("--output_md", type=str, default=None, help="Path to save Markdown report")
    args = parser.parse_args()
    rules_data = json.loads(Path(args.rules_file).read_text(encoding="utf-8"))
    rules_ = [Rule.from_dict(r) for r in rules_data.get("rules", [])]
    data_file = Path(args.data_file)
    all_data = NERData.from_json(json.loads(data_file.read_text()))
    train_samples = [s for s in all_data.samples if s.split == "train"]
    sampled = sample_data(train_samples, "organisation")

    if args.output_md:                                         
        md_path = Path(args.output_md)
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
        md_path = Path(f"reports/{date_str}_rule_eval.md")
    create_md_report(md_path)                                 

    create_md_report(md_path)

    for rule in rules_:
        for threshold in [0.5, 0.7, 1]:
            metrics_per_rule = evaluate_rules_individually_withexamp(
                all_data=sampled,
                rules=[rule],
                chef=None,
                task_type=TaskType.NER,
                threshold=threshold,
            )
            metric_info = metrics_per_rule[rule.name]
            report_data = {
                rule.name: {
                    "pattern": rule.content,
                    "metrics": metric_info["overall"],
                    "FP_examples": metric_info.get("FP_examples", []),
                    "FN_examples": metric_info.get("FN_examples", [])
                }
            }
            append_rule_metrics(md_path, report_data, threshold=threshold)

    print(f"✅ Markdown rule evaluation report saved to: {md_path}")

if __name__ == "__main__":
    main()
