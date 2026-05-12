"""
Evaluate a single rule and print unique TPs / FPs to the terminal.

Usage:
    python scripts/inspect_rule.py \
        --rules-json path/to/results.json \
        --test-dir   path/to/test/conll \
        --rule-name  "My Rule Name"

    # or match by partial name (case-insensitive):
    python scripts/inspect_rule.py ... --rule-name "gmbh"
"""

import argparse
import json
import sys
from logging import getLogger
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rulechef.core import Rule
from rulechef.evaluation import evaluate_rules_individually

from benchmarks.util import load_rules_from_json, make_dataset
from clear_anonymization.models.nerlearner import NERLearner
from clear_anonymization.ner_datasets import load_ner_dataset_from_conll


def _print_rule(rule: Rule) -> None:
    print(f"\n{'═' * 70}")
    print(f"  Rule : {rule.name}")
    print(f"  ID   : {rule.id}")
    print(f"  Fmt  : {rule.format.value}")
    print(f"  Desc : {rule.description}")
    print(f"  Pattern:\n    {rule.content}")
    print(f"{'═' * 70}\n")


def _print_metrics(m) -> None:
    print(
        f"Precision: {m.precision:.1%}  "
        f"Recall: {m.recall:.1%}  "
        f"F1: {m.f1:.1%}  "
        f"| Predicted: {m.matches}  TP: {m.true_positives}  FP: {m.false_positives}\n"
    )


def _classify_fp(pred: dict, gold_entities: list[dict]) -> str:
    pt = pred["text"].lower()
    ps, pe = pred.get("start"), pred.get("end")
    for g in gold_entities:
        gt = g["text"].lower()
        gs, ge = g.get("start"), g.get("end")
        text_similar = pt == gt or pt in gt or gt in pt
        pos_overlap = None not in (ps, pe, gs, ge) and ps < ge and pe > gs
        if text_similar or pos_overlap:
            return "truefp"
    return "missingan"


def _print_per_sentence(label: str, rows: list[tuple[str, str, str]]) -> None:
    """rows: (sent_id, pred_text, gold_text)"""
    print(f"── {label} ({len(rows)}) ──")
    for sent_id, pred, start, gold in rows:
        if pred == gold:
            print(f"  [{sent_id}]  {pred}")
        else:
            print(f"  [{sent_id}]  pred: {pred}  →  gold: {gold}")
    print()


def _extract_gold_from_reason(pred: dict, gold_entities: list[dict]) -> str:
    pt = pred["text"].lower()
    for g in gold_entities:
        gt = g["text"].lower()
        if pt in gt or gt in pt:
            return g["text"]
        ps, pe = pred.get("start"), pred.get("end")
        gs, ge = g.get("start"), g.get("end")
        if None not in (ps, pe, gs, ge) and ps < ge and pe > gs:
            return g["text"]
    return ""


def _print_fp_classified(rows: list[tuple]) -> None:
    """rows: (sent_id, pred_dict, gold_entities)"""
    partial: dict[str, str] = {}
    missing: list[str] = []

    for _sent_id, pred_dict, gold_entities in rows:
        reason = _classify_fp(pred_dict, gold_entities)
        if reason == "truefp":
            partial[pred_dict["text"]] = _extract_gold_from_reason(
                pred_dict, gold_entities
            )
        else:
            missing.append(pred_dict["text"])

    print(
        f"── FP partial ({len(partial)}): {'\n'.join(repr(t) + ' → ' + repr(g) for t, g in sorted(partial.items()))}"
    )
    print()
    print(
        f"── FP missing annotation ({len(missing)}): {'\n '.join(repr(t) for t in sorted(missing))}"
    )
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect a single rule's TP / FP")
    parser.add_argument(
        "--rules-json", required=True, help="Path to results JSON with rules"
    )
    parser.add_argument(
        "--test-dir", required=True, help="Path to test CoNLL data directory"
    )
    parser.add_argument("--rule-id", required=True, help="Rule Id")
    parser.add_argument("--dataset-name", default="findok")
    parser.add_argument("--max-samples", type=int, default=500)
    args = parser.parse_args()

    # Load rules
    rules = load_rules_from_json(args.rules_json)

    args.rule_name = "7e1bbfcb"

    matched = [r for r in rules if args.rule_name in r.id]
    if not matched:
        print(f"No rule matching '{args.rule_name}'. Available rules:")
        for r in rules:
            print(f"  {r.name}")
        sys.exit(1)
    if len(matched) > 1:
        print(f"Multiple rules match '{args.rule_name}':")
        for r in matched:
            print(f"  {r.name}")
        print("Refine --rule-name to match exactly one.")
        sys.exit(1)

    rule = matched[0]
    _print_rule(rule)

    # Load config so we can build NERLearner (needed for _apply_rules)
    saved = json.loads(Path(args.rules_json).read_text())
    config = saved.get("config", {})
    learner = NERLearner(
        model=config.get("model"),
        dataset_name=config.get("dataset_name", args.dataset_name),
        base_url=config.get("base_url", "http://localhost:8000/v1"),
        use_grex=not config.get("no_grex", False),
        max_rules=config.get("max_rules"),
        max_samples=config.get("max_samples"),
        max_counter_examples=config.get("max_counter_examples"),
        logger=getLogger(__name__),
        sampling_strategy=config.get("sampling_strategy"),
        synthesis_strategy=config.get("synthesis_strategy"),
        selected_classes=config.get("selected_classes", ["organisation"]),
    )

    # Load test data
    test_raw = load_ner_dataset_from_conll(args.test_dir)
    test_data = [
        {
            "text": sent.text,
            "entities": sent.labels,
            "sent_id": sent.sent_id,
            "doc_id": s.doc_id,
        }
        for s in test_raw.samples
        for sent in s.sentences
    ]
    test_dataset = make_dataset(f"{args.dataset_name}_eval", test_data, learner.task)
    print(
        f"Loaded {len(test_data)} sentences from {len(test_raw.samples)} documents.\n"
    )

    # Evaluate only this one rule
    metrics_list = evaluate_rules_individually(
        rules=[rule],
        dataset=test_dataset,
        apply_rules_fn=learner.learner._apply_rules,
        mode="text",
        max_samples=args.max_samples,
        iou_threshold=1,
    )
    m = metrics_list[0]
    _print_metrics(m)

    tp_rows: list[tuple[str, str, str]] = []
    fp_rows: list[tuple] = []
    seen_tp: set[tuple[str, str, str]] = set()
    seen_fp: set[tuple[str, str]] = set()

    for sample in m.sample_matches:
        sent_id = sample.input.get("sent_id", "")
        for pred, gold in sample.matched_pairs:
            key = (sent_id, pred["text"], pred.get("start"), gold["text"])
            if key not in seen_tp:
                seen_tp.add(key)
                tp_rows.append(key)
        for e in sample.false_positives:
            key = (sent_id, e["text"])
            if key not in seen_fp:
                seen_fp.add(key)
                fp_rows.append((sent_id, e, sample.expected))

    _print_per_sentence("True Positives  (pred → gold)", tp_rows)
    _print_fp_classified(fp_rows)


if __name__ == "__main__":
    main()
