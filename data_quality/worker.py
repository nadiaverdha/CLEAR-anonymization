"""ProcessPoolExecutor worker for parallel rule execution."""

from rulechef.core import Rule, RuleFormat, TaskType
from rulechef.executor import RuleExecutor

from clear_anonymization.evaluation.evaluator import classify_fp

_worker_state = {}


def init_worker(rules_data: list[dict]) -> None:
    _worker_state["rules"] = [
        Rule(
            id=r["id"],
            name=r["name"],
            description=r.get("description", ""),
            format=RuleFormat(r["format"]),
            content=r["content"],
            output_template=r.get("output_template"),
            output_key=r.get("output_key"),
        )
        for r in rules_data
    ]
    _worker_state["executor"] = RuleExecutor()


def _with_int_offsets(d: dict) -> dict:
    out = dict(d)
    for key in ("start", "end"):
        val = d.get(key)
        try:
            out[key] = int(val) if val not in (None, "") else None
        except (ValueError, TypeError):
            out[key] = None
    return out


def process_sentence(sentence: dict) -> list[dict]:
    """Apply all rules to one sentence, return per-prediction scoring records."""
    executor = _worker_state["executor"]
    rules = _worker_state["rules"]
    text = sentence["text"]
    gold = sentence.get("entities", [])
    try:
        result = executor.apply_rules(rules, {"text": text}, TaskType.NER)
        preds = result.get("entities", [])
    except Exception:
        return []

    records = []
    seen_spans = set()
    for pred in preds:
        span = (pred.get("rule_id", ""), pred.get("start"), pred.get("end"))
        if span in seen_spans:
            continue
        seen_spans.add(span)

        pred_norm = _with_int_offsets(pred)
        try:
            reason = classify_fp(pred_norm, gold)
        except (ValueError, TypeError):
            continue

        outcome = "fp" if reason.startswith("no gold match") else "tp"
        records.append(
            {
                "rule_id": pred.get("rule_id", ""),
                "rule_name": pred.get("rule_name", ""),
                "text": text,
                "predicted": pred.get("text", ""),
                "gold_entities": [g.get("text", "") for g in gold],
                "outcome": outcome,
                "reason": reason,
            }
        )
    return records
