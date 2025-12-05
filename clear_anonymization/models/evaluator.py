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
from clear_anonymization.ner_datasets.ler_dataset import LERData, LERSample


def check_overlap(pred, gold, threshold=1):
    if threshold == 1:
        return pred["start"] == gold["start"] and pred["end"] == gold["end"]
    else:
        overlap_start = max(pred["start"], gold["start"])
        overlap_end = min(pred["end"], gold["end"])

        if overlap_end > overlap_start:
            sample_overlap = overlap_end - overlap_start

        else:
            return False

        gold_length = gold["end"] - gold["start"]
        overlap_ratio = sample_overlap / gold_length
        return overlap_ratio >= threshold


def evaluate_span_level(
    extractor: LLMExtractor, samples, threshold
) -> dict[str, float]:
    tp = 0
    fp = 0
    fn = 0
    for sample in tqdm(samples, desc="Evaluation", leave=False):
        text = sample.sentences
        gold_spans = sample.labels

        predicted_spans = extractor.predict(text)

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


def evaluate_char_level(extractor: LLMExtractor, samples) -> dict[str, float]:
    total_overlap = 0
    total_predicted = 0
    total_gold = 0

    for sample in tqdm(samples, desc="Evaluation", leave=False):
        text = sample.sentences
        gold_spans = sample.labels
        predicted_spans = extractor.predict(text)

        sample_predicted_length = sum(
            pred["end"] - pred["start"] for pred in predicted_spans
        )
        total_predicted += sample_predicted_length

        # Compute total gold span length once for this sample.
        sample_gold_length = sum(gold["end"] - gold["start"] for gold in gold_spans)
        total_gold += sample_gold_length

        sample_overlap = 0
        for pred in predicted_spans:
            for gold in gold_spans:
                overlap_start = max(pred["start"], gold["start"])
                overlap_end = min(pred["end"], gold["end"])
                if overlap_end > overlap_start:
                    sample_overlap += overlap_end - overlap_start
        total_overlap += sample_overlap
    precision = total_overlap / total_predicted if total_predicted > 0 else 0
    recall = total_overlap / total_gold if total_gold > 0 else 0
    f1 = (
        2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    )

    print({"precision": precision, "recall": recall, "f1": f1})
    return {"precision": precision, "recall": recall, "f1": f1}
