import json
from pathlib import Path

from sklearn.metrics import (
    auc,
    classification_report,
    precision_recall_fscore_support,
    roc_curve,
)
from tqdm.auto import tqdm
from collections import defaultdict

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.llm import LLMExtractor
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample


def check_overlap(pred, gold, threshold=1):
    pred_start, pred_end = pred["start"], pred["end"]
    gold_start, gold_end = gold["start"], gold["end"]

    if threshold == 1:
        return pred["text"] == gold["text"]

    overlap_start = max(pred_start, gold_start)

    overlap_end = min(pred_end, gold_end)

    # no overlap
    if overlap_end <= overlap_start:
        return False

    overlap = overlap_end - overlap_start
    # print(pred["text"], gold["text"],overlap)
    union = max(pred_end, gold_end) - min(pred_start, gold_start)
    iou = overlap / union
    # print(iou,"->>>>",threshold,iou >= threshold)

    return iou >= threshold


def filter_spans_by_class(spans, allowed_classes):
    if allowed_classes:
        return [s for s in spans if s["class"] in allowed_classes]
    else:
        return spans


def evaluate_span_level(
    extractor: LLMExtractor,
    samples,
    threshold,
    allowed_classes: list[str] | None = None,
) -> dict[str, float]:
    tp = defaultdict(int)
    fp = defaultdict(int)
    fn = defaultdict(int)

    labels = set()
    for sample in tqdm(samples, desc="Evaluation", leave=False):
        text = sample.text
        gold_spans = sample.labels
        #print(gold_spans)
        gold_spans = filter_spans_by_class(gold_spans, allowed_classes)
        #print(gold_spans)
        predicted_spans = extractor.predict(text)
        matched_gold = set()

        for g in gold_spans:
            labels.add(g["class"])
        for p in predicted_spans:
            labels.add(p["class"])

        for pred in predicted_spans:
            found_match = False
            pred_class = pred["class"]

            for j, gold in enumerate(gold_spans):
                if j in matched_gold:
                    continue
                if check_overlap(pred, gold, threshold):
                    tp[gold["class"]] += 1
                    matched_gold.add(j)
                    found_match = True
                    break

            if not found_match:
                fp[pred_class] += 1

        for j, gold in enumerate(gold_spans):
            if j not in matched_gold:
                fn[gold["class"]] += 1

    per_class = {}
    for label in sorted(labels):
        p = tp[label] / (tp[label] + fp[label]) if tp[label] + fp[label] else 0.0
        r = tp[label] / (tp[label] + fn[label]) if tp[label] + fn[label] else 0.0
        f1 = 2 * p * r / (p + r) if p + r else 0.0

        per_class[label] = {
            "precision": p,
            "recall": r,
            "f1": f1,
            "tp": tp[label],
            "fp": fp[label],
            "fn": fn[label],
        }

        print(label)
        print(f"Precision: {p:.4f}, Recall: {r:.4f}, F1: {f1:.4f}")
        

    TP = sum(tp.values())
    FP = sum(fp.values())
    FN = sum(fn.values())

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    print("-----------")
    print("Overall Metrics")
    print(f"Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")

    overall = {
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

    return overall, per_class


def evaluate_char_level(
    extractor: LLMExtractor,
    samples,
    allowed_classes: list[str] | None = None,
) -> dict[str, float]:
    total_overlap = 0
    total_predicted = 0
    total_gold = 0

    for sample in tqdm(samples, desc="Evaluation", leave=False):
        text = sample.text
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
