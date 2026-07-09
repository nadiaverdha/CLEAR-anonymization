import json
from pathlib import Path

from rulechef.core import Rule, RuleFormat, TaskType
from rulechef.executor import RuleExecutor

from clear_anonymization.evaluation.evaluator import classify_fp
from data_quality.patch_missing_annotations.span_tagging import (
    _tag_pattern_span,
    _token_spans,
)


def _apply_rule_predictions(
    data, rules_json_paths, rule_ids
) -> tuple[list[Rule], list[dict]]:
    """Load rules from --rules-json, apply them to data, and tag any prediction
    that doesn't match a gold label as a missing annotation. Returns the loaded
    rules and the list of annotations added (used later for the changelog)."""
    rules = []
    for rules_path in rules_json_paths:
        saved = json.loads(Path(rules_path).read_text())
        rules += [
            Rule(
                id=r["id"],
                name=r["name"],
                description=r["description"],
                format=RuleFormat(r["format"]),
                content=r["content"],
                output_template=r.get("output_template"),
                output_key=r.get("output_key"),
            )
            for r in saved["rules"]
        ]
    if rule_ids:
        ids = set(rule_ids)
        rules = [r for r in rules if r.id in ids]
        missing = ids - {r.id for r in rules}
        if missing:
            print(f"WARNING: rule ID(s) not found: {', '.join(missing)}")
        print(f"Applying {len(rules)} rule(s): {', '.join(r.id for r in rules)}")

    if not rules:
        return rules, []

    rule_changes = []
    executor = RuleExecutor()
    for s in data.samples:
        for sent in s.sentences:
            if not sent.text:
                continue
            result = executor.apply_rules(rules, {"text": sent.text}, TaskType.NER)
            predictions = sorted(
                result.get("entities", []),
                key=lambda p: int(p["end"]) - int(p["start"]),
                reverse=True,
            )
            if not predictions:
                continue
            gold = list(sent.labels or [])
            token_spans = _token_spans(sent)
            for pred in predictions:
                reason = classify_fp(pred, gold)
                if not reason.startswith("no gold match"):
                    continue
                entity_type = pred.get("type")
                if not entity_type:
                    continue
                ps, pe = int(pred["start"]), int(pred["end"])
                print(f"  PRED: '{pred.get('text')}' [{ps}:{pe}] → {reason}")
                new_labels = _tag_pattern_span(
                    sent, ps, pe, entity_type, token_spans=token_spans
                )
                if new_labels is None:
                    continue
                gold = sent.labels = new_labels
                print(f"  TAGGED [{sent.sent_id}]: '{pred['text']}' → {entity_type}")
                rule_changes.append(
                    {
                        "sent_id": sent.sent_id,
                        "text": pred.get("text"),
                        "type": entity_type,
                        "start": ps,
                        "end": pe,
                        "rule_id": pred.get("rule_id"),
                        "rule_name": pred.get("rule_name"),
                    }
                )

    return rules, rule_changes
