import argparse
import json
import re
from pathlib import Path
from types import SimpleNamespace

from rulechef.core import Rule, RuleFormat, TaskType
from rulechef.executor import RuleExecutor

from benchmarks.create_md_report_rules import _classify_fp
from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.preprocess.preprocess_data import assign_bio_tag


def _parse_misc(misc):
    if not misc or misc == "_":
        return {}
    return {p.split("=")[0]: p.split("=")[1] for p in misc.split("|") if "=" in p}


def _set_ner_in_misc(misc, new_ner, force=False):
    parts = misc.split("|") if misc and misc != "_" else []
    if not force and any(
        p.startswith("NER=") and not p.startswith("NER=O") for p in parts
    ):
        return misc
    updated = [f"NER={new_ner}" if p.startswith("NER=") else p for p in parts]
    if not any(p.startswith("NER=") for p in parts):
        updated.append(f"NER={new_ner}")
    return "|".join(updated)


def _token_spans(sent):
    """Tokens with their (start_char, end_char) offsets, in document order."""
    spans = []
    for tok in sent.tokens:
        m = _parse_misc(tok.get("misc", "_"))
        if "SentStart" in m and "SentEnd" in m:
            spans.append((int(m["SentStart"]), int(m["SentEnd"]), tok))
    return spans


def _find_all(text, pattern):
    """Yield (start, end) for every (possibly overlapping) occurrence of pattern in text."""
    start = 0
    while True:
        idx = text.find(pattern, start)
        if idx == -1:
            return
        yield idx, idx + len(pattern)
        start = idx + 1


def _tag_pattern_span(
    sent, ps, pe, entity_type, force=False, drop_overlaps=False, skip_existing=False
):
    """Tag tokens overlapping [ps, pe) with entity_type and return the updated
    labels list (or None if skip_existing and [ps, pe) is already annotated).

    force: overwrite existing non-O NER tags on overlapping tokens.
    drop_overlaps: remove any existing labels overlapping [ps, pe) from sent.labels.
    entity_type="O" clears NER on overlapping tokens instead of tagging.
    """
    gold = list(sent.labels or [])
    if skip_existing and (ps, pe) in {(l["start"], l["end"]) for l in gold}:
        return None
    if drop_overlaps:
        gold = [l for l in gold if not (l["start"] < pe and l["end"] > ps)]

    is_remove = entity_type.upper() == "O"
    for ts, te, tok in _token_spans(sent):
        if is_remove:
            if ts < pe and te > ps:
                tok["misc"] = _set_ner_in_misc(tok["misc"], "O", force=True)
            continue
        tok_ns = SimpleNamespace(start_char=ts, end_char=te)
        new_tag = assign_bio_tag(
            tok_ns, [{"start": ps, "end": pe, "type": entity_type}]
        )
        if new_tag != "O":
            tok["misc"] = _set_ner_in_misc(tok["misc"], new_tag, force=force)

    if is_remove:
        return gold
    return gold + [
        {"text": sent.text[ps:pe], "type": entity_type, "start": ps, "end": pe}
    ]


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Markdown report from a saved rules JSON and test data"
    )
    parser.add_argument(
        "--rules-json",
        type=str,
        nargs="*",
        default=[],
        help="Path to results JSON containing rules",
    )
    parser.add_argument(
        "--data-dir", type=str, required=True, help="Path to data (CONLLU format)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--patterns",
        type=str,
        nargs="*",
        default=[],
        help="Text patterns to annotate, format: 'text:type' e.g. 'Bezirksgericht Wien:organisation'",
    )
    parser.add_argument(
        "--corrections",
        type=str,
        nargs="*",
        default=[],
        help="Correct existing annotations by sent_id, format: 'sent_id:text:new_type' (use new_type=O to remove)",
    )
    parser.add_argument(
        "--extend-prev",
        type=str,
        nargs="*",
        default=[],
        help="Tag a word and its preceding token as the same entity, format: 'sent_id:text:type'",
    )
    args = parser.parse_args()

    data = load_ner_dataset_from_conll(args.data_dir)

    # ────── Add new annotation based on rule predictions ──────
    rules = []
    for rules_path in args.rules_json:
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
    executor = RuleExecutor()

    for s in data.samples if rules else []:
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
            for pred in predictions:
                reason = _classify_fp(pred, gold)
                if not reason.startswith("no gold match"):
                    continue
                entity_type = pred.get("type")
                if not entity_type:
                    continue
                ps, pe = int(pred["start"]), int(pred["end"])
                print(f"  PRED: '{pred.get('text')}' [{ps}:{pe}] → {reason}")
                gold = _tag_pattern_span(sent, ps, pe, entity_type)
                sent.labels = gold
                print(f"  TAGGED [{sent.sent_id}]: '{pred['text']}' → {entity_type}")

    # ────── Add new annotations based on given pattern ──────
    text_patterns = []
    for p in args.patterns:
        if ":" not in p:
            raise ValueError(f"Pattern '{p}' must be in format 'text:type'")
        text, etype = p.rsplit(":", 1)
        text_patterns.append((text.strip(), etype.strip()))
    print(text_patterns)
    pattern_count = 0
    for s in data.samples:
        for sent in s.sentences:
            if not sent.text:
                continue
            for pattern_text, entity_type in text_patterns:
                for ps, pe in _find_all(sent.text, pattern_text):
                    new_labels = _tag_pattern_span(
                        sent, ps, pe, entity_type, skip_existing=True
                    )
                    if new_labels is not None:
                        sent.labels = new_labels
                        print(
                            f"  PATTERN: '{pattern_text}' [{ps}:{pe}] → {entity_type} in [{sent.sent_id}]"
                        )
                        pattern_count += 1
    if text_patterns:
        print(f"Pattern annotations added: {pattern_count}")

    # ────── Adapt annotations based correction suggestions ──────
    corrections = []
    for c in args.corrections:
        parts = c.split(":", 2)
        if len(parts) != 3:
            raise ValueError(
                f"Correction '{c}' must be in format 'sent_id:text:new_type'"
            )
        sent_id, text, new_type = parts
        corrections.append((sent_id.strip(), text.strip(), new_type.strip()))

    correction_count = 0
    sent_index = {sent.sent_id: sent for s in data.samples for sent in s.sentences}
    for sent_id, pattern_text, new_type in corrections:
        print(
            f"Applying correction: sent_id='{sent_id}', text='{pattern_text}', new_type='{new_type}'"
        )
        sent = sent_index.get(sent_id)
        if sent is None:
            print(f"  CORRECTION WARNING: sent_id '{sent_id}' not found")
            continue
        if not sent.text:
            continue
        for ps, pe in _find_all(sent.text, pattern_text):
            sent.labels = _tag_pattern_span(
                sent, ps, pe, new_type, force=True, drop_overlaps=True
            )
            print(
                f"  CORRECTION: '{pattern_text}' [{ps}:{pe}] → {new_type} in [{sent_id}]"
            )
            correction_count += 1
    if corrections:
        print(f"Corrections applied: {correction_count}")

    # ────── Extend annotations to the previous word of a word given ──────
    extend_prev_patterns = []
    for p in args.extend_prev:
        parts = p.split(":", 2)
        if len(parts) != 3:
            raise ValueError(f"extend-prev '{p}' must be in format 'sent_id:text:type'")
        sent_id, text, etype = parts
        extend_prev_patterns.append((sent_id.strip(), text.strip(), etype.strip()))
    extend_prev_count = 0
    for sent_id, pattern_text, entity_type in extend_prev_patterns:
        sent = sent_index.get(sent_id)
        if sent is None:
            print(f"  EXTEND-PREV WARNING: sent_id '{sent_id}' not found")
            continue
        if not sent.text:
            continue
        for ps, pe in _find_all(sent.text, pattern_text):
            tok_spans = _token_spans(sent)
            matched = [
                i for i, (ts, te, _) in enumerate(tok_spans) if ts < pe and te > ps
            ]
            if not matched or matched[0] == 0:
                print(
                    f"  EXTEND-PREV WARNING: no previous token found for '{pattern_text}' in [{sent_id}]"
                )
                continue

            new_ps = tok_spans[matched[0] - 1][0]
            new_pe = pe
            full_text = sent.text[new_ps:new_pe]

            sent.labels = _tag_pattern_span(
                sent, new_ps, new_pe, entity_type, force=True, drop_overlaps=True
            )
            print(
                f"  EXTEND-PREV: '{full_text}' [{new_ps}:{new_pe}] → {entity_type} in [{sent_id}]"
            )
            extend_prev_count += 1
    if extend_prev_patterns:
        print(f"Extend-prev annotations added: {extend_prev_count}")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(data.to_conll(), encoding="utf-8")
    print(f"Written to {out_path}")


if __name__ == "__main__":
    main()
