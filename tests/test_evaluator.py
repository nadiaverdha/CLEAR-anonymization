import argparse
import json
from pathlib import Path

from clear_anonymization.extractors import factory
from clear_anonymization.models.evaluator import (
    evaluate_char_level,
    evaluate_span_level,
)

from py_markdown_table.markdown_table import markdown_table

from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample

from scripts.create_md_reports import create_md_eval_report, append_eval_table


class TestExtractor:
    def predict(self, text):
        if text == "Nadia lives in Vienna.":
            return [
                {"start": 0, "end": 6, "text": "Nadia", "class": "person"},
                {"start": 14, "end": 18, "text": "Vienna", "class": "location"},
            ]
        elif text == "Max Musterman emailed students@tuwien.com yesterday.":
            return [
                {"start": 0, "end": 12, "text": "Alice", "class": "person"},
                {
                    "start": 21,
                    "end": 39,
                    "text": "students@tuwien.com",
                    "class": "email",
                },
            ]
        return []


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a named entity recognition model based on LLM"
    )
    parser.add_argument(
        "--threshold",
        type=float,
        help="Pick threshold if you want to perform span_level evaluation",
    )

    args = parser.parse_args()

    ground_truth = [
        NERSample(
            text="Nadia lives in Vienna.",
            split="test",
            labels=[
                {"start": 0, "end": 5, "text": "Nadia", "class": "person"},
                {"start": 14, "end": 20, "text": "Vienna", "class": "location"},
            ],
        ),
        NERSample(
            text="Max Musterman emailed students@tuwien.com yesterday.",
            split="test",
            labels=[
                {"start": 0, "end": 12, "text": "Alice", "class": "person"},
                {
                    "start": 21,
                    "end": 39,
                    "text": "students@tuwien.com",
                    "class": "email",
                },
            ],
        ),
    ]
    output_md = Path("reports/test_eval_results.md")
    append_table = create_md_eval_report(
        output_md, title="Evaluation Results", dataset="test"
    )

    test_extractor = TestExtractor()
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    headers = ["Threshold", "Precision", "Recall", "F1"]
    print("\n---- Span-Level Evaluation ----")
    results = []
    for threshold in thresholds:
        print(f"\nThreshold {threshold}")
        metrics = evaluate_span_level(test_extractor, ground_truth, threshold)
        results.append(
            {
                "threshold": threshold,
                "precision": metrics["precision"],
                "recall": metrics["recall"],
                "f1": metrics["f1"],
            }
        )
    md_results = markdown_table(results).get_markdown()
    append_eval_table(output_md, md_results)

    print(f"\nResults saved to {output_md}")


if __name__ == "__main__":
    main()
