import argparse
import json
from pathlib import Path

from sklearn.metrics import (
    auc,
    classification_report,
    precision_recall_fscore_support,
    roc_curve,
)
from tqdm.auto import tqdm

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.llm import LLMExtractor
from clear_anonymization.models.evaluator import check_overlap
from clear_anonymization.ner_datasets.ler_dataset import LERData, LERSample


def evaluate_gliner(ground_truth, gliner_baseline, threshold):
    tp = 0
    fp = 0
    fn = 0
    for i, sample in enumerate(tqdm(ground_truth, desc="Evaluating", leave=False)):
        text = sample.sentences
        gold_spans = sample.labels
        predicted_spans = gliner_baseline.samples[i].labels
        matched_gold = set()
        for pred in predicted_spans:
            found_match = False
            for j, gold in enumerate(gold_spans):
                if check_overlap(pred, gold, threshold):
                    tp += 1
                    matched_gold.add(j)
                    found_match = True
                    break
            if not found_match:
                fp += 1

        fn += len(gold_spans) - len(matched_gold)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    print(f"Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate GliNER model.")
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path to the evaluation data (JSON format)",
    )
    parser.add_argument("--model", type=str, required=True, help="GliNER model ")

    parser.add_argument(
        "--model_file",
        type=str,
        help="Path to the data predicted by the model (JSON format)",
    )

    parser.add_argument(
        "--threshold",
        type=float,
        help="Pick threshold if you want to perform span_level evaluation",
    )
    args = parser.parse_args()
    data = LERData.from_json(json.loads(Path(args.input_dir).read_text()))
    ground_truth = [s for s in data.samples if s.split == "validation"]
    gliner_data = LERData.from_json(json.loads(Path(args.model_file).read_text()))
    gliner_data = LERData.from_json(json.loads(Path("results_gliner.json").read_text()))
    evaluate_gliner(ground_truth, gliner_data, args.threshold)


if __name__ == "__main__":
    main()
