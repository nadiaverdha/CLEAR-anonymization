import argparse
import json
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


def _set_ner_in_misc(misc, new_ner):
    parts = misc.split("|")
    if any(p.startswith("NER=") and not p.startswith("NER=O") for p in parts):
        return misc
    updated = [f"NER={new_ner}" if p.startswith("NER=") else p for p in parts]
    if not any(p.startswith("NER=") for p in parts):
        updated.append(f"NER={new_ner}")
    return "|".join(updated)


def _force_set_ner_in_misc(misc, new_ner):
    parts = misc.split("|") if misc and misc != "_" else []
    updated = [f"NER={new_ner}" if p.startswith("NER=") else p for p in parts]
    if not any(p.startswith("NER=") for p in parts):
        updated.append(f"NER={new_ner}")
    return "|".join(updated)


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

    text_patterns = []
    for p in args.patterns:
        if ":" not in p:
            raise ValueError(f"Pattern '{p}' must be in format 'text:type'")
        text, etype = p.rsplit(":", 1)
        text_patterns.append((text.strip(), etype.strip()))
    print(text_patterns)
    corrections = []
    for c in args.corrections:
        parts = c.split(":", 2)
        if len(parts) != 3:
            raise ValueError(
                f"Correction '{c}' must be in format 'sent_id:text:new_type'"
            )
        sent_id, text, new_type = parts
        corrections.append((sent_id.strip(), text.strip(), new_type.strip()))

    extend_prev_patterns = []
    for p in args.extend_prev:
        parts = p.split(":", 2)
        if len(parts) != 3:
            raise ValueError(f"extend-prev '{p}' must be in format 'sent_id:text:type'")
        sent_id, text, etype = parts
        extend_prev_patterns.append((sent_id.strip(), text.strip(), etype.strip()))

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

    data = load_ner_dataset_from_conll(args.data_dir)

    executor = RuleExecutor()

    for s in data.samples if rules else []:
        for sent in s.sentences:
            if not sent.text:
                continue
            result = executor.apply_rules(rules, {"text": sent.text}, TaskType.NER)
            # predictions = result.get("entities", [])
            predictions = sorted(
                result.get("entities", []),
                key=lambda p: int(p["end"]) - int(p["start"]),
                reverse=True,
            )
            if not predictions:
                continue
            gold = list(sent.labels or [])
            for tok in sent.tokens:
                m = _parse_misc(tok.get("misc", "_"))
            for pred in predictions:
                reason = _classify_fp(pred, gold)

                if not reason.startswith("no gold match"):
                    continue
                print(
                    f"  PRED: '{pred.get('text')}' [{pred.get('start')}:{pred.get('end')}] → {reason}"
                )
                entity_type = pred.get("type")
                ps, pe = int(pred["start"]), int(pred["end"])
                if not entity_type:
                    continue
                for tok in sent.tokens:
                    m = _parse_misc(tok.get("misc", "_"))
                    if "SentStart" not in m or "SentEnd" not in m:
                        continue
                    tok_ns = SimpleNamespace(
                        start_char=int(m["SentStart"]), end_char=int(m["SentEnd"])
                    )
                    new_tag = assign_bio_tag(
                        tok_ns, [{"start": ps, "end": pe, "type": entity_type}]
                    )
                    if new_tag != "O":
                        print("----------------------------------------------")
                        print(sent.sent_id)
                        tok["misc"] = _set_ner_in_misc(tok["misc"], new_tag)
                        print(f"    TAGGED: '{tok['text']}' → {new_tag}")
                gold.append(
                    {"text": pred["text"], "type": entity_type, "start": ps, "end": pe}
                )
            sent.labels = gold

    pattern_count = 0
    for s in data.samples:
        for sent in s.sentences:
            if not sent.text:
                continue
            for pattern_text, entity_type in text_patterns:
                start = 0
                while True:
                    idx = sent.text.find(pattern_text, start)
                    if idx == -1:
                        break
                    ps, pe = idx, idx + len(pattern_text)
                    gold = list(sent.labels or [])
                    gold_spans = {(l["start"], l["end"]) for l in gold}
                    if (ps, pe) not in gold_spans:
                        for tok in sent.tokens:
                            m = _parse_misc(tok.get("misc", "_"))
                            if "SentStart" not in m or "SentEnd" not in m:
                                continue
                            tok_ns = SimpleNamespace(
                                start_char=int(m["SentStart"]),
                                end_char=int(m["SentEnd"]),
                            )
                            new_tag = assign_bio_tag(
                                tok_ns, [{"start": ps, "end": pe, "type": entity_type}]
                            )
                            if new_tag != "O":
                                tok["misc"] = _set_ner_in_misc(tok["misc"], new_tag)
                        sent.labels = gold + [
                            {
                                "text": pattern_text,
                                "type": entity_type,
                                "start": ps,
                                "end": pe,
                            }
                        ]
                        print(
                            f"  PATTERN: '{pattern_text}' [{ps}:{pe}] → {entity_type} in [{sent.sent_id}]"
                        )
                        pattern_count += 1
                    start = idx + 1
    if text_patterns:
        print(f"Pattern annotations added: {pattern_count}")

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
        start = 0
        while True:
            idx = sent.text.find(pattern_text, start)
            if idx == -1:
                break
            ps, pe = idx, idx + len(pattern_text)
            gold = [
                l
                for l in (sent.labels or [])
                if not (l["start"] < pe and l["end"] > ps)
            ]
            for tok in sent.tokens:
                m = _parse_misc(tok.get("misc", "_"))
                print(
                    f"  Checking token '{tok['text']}' [{m.get('SentStart')}:{m.get('SentEnd')}] against pattern '{pattern_text}' [{ps}:{pe}]"
                )
                if "SentStart" not in m or "SentEnd" not in m:
                    continue
                tok_ns = SimpleNamespace(
                    start_char=int(m["SentStart"]), end_char=int(m["SentEnd"])
                )
                print(tok_ns, ps, pe)
                if new_type.upper() == "O":
                    tok["misc"] = _force_set_ner_in_misc(tok.get("misc", "_"), "O")
                else:
                    new_tag = assign_bio_tag(
                        tok_ns, [{"start": ps, "end": pe, "type": new_type}]
                    )
                    if new_tag != "O":
                        tok["misc"] = _force_set_ner_in_misc(
                            tok.get("misc", "_"), new_tag
                        )
            if new_type.upper() != "O":
                gold.append(
                    {"text": pattern_text, "type": new_type, "start": ps, "end": pe}
                )
            sent.labels = gold
            print(
                f"  CORRECTION: '{pattern_text}' [{ps}:{pe}] → {new_type} in [{sent_id}]"
            )
            correction_count += 1
            start = idx + 1
    if corrections:
        print(f"Corrections applied: {correction_count}")

    extend_prev_count = 0
    for sent_id, pattern_text, entity_type in extend_prev_patterns:
        sent = sent_index.get(sent_id)
        if sent is None:
            print(f"  EXTEND-PREV WARNING: sent_id '{sent_id}' not found")
            continue
        if not sent.text:
            continue
        start = 0
        while True:
            idx = sent.text.find(pattern_text, start)
            if idx == -1:
                break
            ps, pe = idx, idx + len(pattern_text)

            # collect tokens with char offsets
            tok_spans = []
            for tok in sent.tokens:
                m = _parse_misc(tok.get("misc", "_"))
                if "SentStart" in m and "SentEnd" in m:
                    tok_spans.append((int(m["SentStart"]), int(m["SentEnd"]), tok))

            matched = [
                i for i, (ts, te, _) in enumerate(tok_spans) if ts < pe and te > ps
            ]
            if not matched or matched[0] == 0:
                print(
                    f"  EXTEND-PREV WARNING: no previous token found for '{pattern_text}' in [{sent_id}]"
                )
                start = idx + 1
                continue

            new_ps = tok_spans[matched[0] - 1][0]
            new_pe = pe
            full_text = sent.text[new_ps:new_pe]

            # remove any overlapping labels and force-retag the expanded span
            gold = [
                l
                for l in (sent.labels or [])
                if not (l["start"] < new_pe and l["end"] > new_ps)
            ]
            for tok in sent.tokens:
                m = _parse_misc(tok.get("misc", "_"))
                if "SentStart" not in m or "SentEnd" not in m:
                    continue
                tok_ns = SimpleNamespace(
                    start_char=int(m["SentStart"]), end_char=int(m["SentEnd"])
                )
                new_tag = assign_bio_tag(
                    tok_ns, [{"start": new_ps, "end": new_pe, "type": entity_type}]
                )
                if new_tag != "O":
                    tok["misc"] = _force_set_ner_in_misc(tok.get("misc", "_"), new_tag)
            gold.append(
                {"text": full_text, "type": entity_type, "start": new_ps, "end": new_pe}
            )
            sent.labels = gold
            print(
                f"  EXTEND-PREV: '{full_text}' [{new_ps}:{new_pe}] → {entity_type} in [{sent_id}]"
            )
            extend_prev_count += 1
            start = idx + 1
    if extend_prev_patterns:
        print(f"Extend-prev annotations added: {extend_prev_count}")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(data.to_conll(), encoding="utf-8")
    print(f"Written to {out_path}")


if __name__ == "__main__":
    main()
