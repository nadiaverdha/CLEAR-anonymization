import argparse
import json
import sys
from datetime import date
from pathlib import Path
from types import SimpleNamespace

from rulechef.core import Rule, RuleFormat, TaskType
from rulechef.executor import RuleExecutor

from clear_anonymization.evaluation.evaluator import classify_fp
from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.preprocess.util import assign_bio_tag


def _parse_misc(misc):
    if not misc or misc == "_":
        return {}
    return {p.split("=")[0]: p.split("=")[1] for p in misc.split("|") if "=" in p}


def _set_ner_in_misc(misc, new_ner, force=False):
    """Returns (new_misc, changed) — changed is False if an existing non-O tag
    blocked the write (force=False) or the value was already new_ner."""
    parts = misc.split("|") if misc and misc != "_" else []
    if not force and any(
        p.startswith("NER=") and not p.startswith("NER=O") for p in parts
    ):
        return misc, False
    updated = [f"NER={new_ner}" if p.startswith("NER=") else p for p in parts]
    if not any(p.startswith("NER=") for p in parts):
        updated.append(f"NER={new_ner}")
    new_misc = "|".join(updated)
    return new_misc, new_misc != misc


def _has_non_o_tag(misc):
    parts = misc.split("|") if misc and misc != "_" else []
    return any(p.startswith("NER=") and not p.startswith("NER=O") for p in parts)


def _token_spans(sent):
    """Tokens with their (start_char, end_char) offsets, in document order."""
    spans = []
    for tok in sent.tokens:
        m = _parse_misc(tok.get("misc", "_"))
        if "SentStart" in m and "SentEnd" in m:
            spans.append((int(m["SentStart"]), int(m["SentEnd"]), tok))
    return spans


def _find_all(text, pattern, token_span_set):
    """Yield (start, end) for every occurrence of pattern in text whose span
    exactly matches one of token_span_set. This ensures 'BFG' matches only
    the standalone token 'BFG' and never a substring of 'BFGG' or 'BFG-GV'.

    token_span_set: precomputed {(start, end), ...} for the sentence's tokens
    — pass it in (computed once per sentence) rather than recomputing it on
    every call, since callers loop this over many patterns per sentence.
    """
    start = 0
    while True:
        idx = text.find(pattern, start)
        if idx == -1:
            return
        end = idx + len(pattern)
        if (idx, end) in token_span_set:
            yield idx, end
        start = idx + 1


def _tag_pattern_span(
    sent,
    ps,
    pe,
    entity_type,
    force=False,
    drop_overlaps=False,
    skip_existing=False,
    token_spans=None,
):
    """Tag tokens overlapping [ps, pe) with entity_type and return the updated
    labels list, or None if skip_existing and [ps, pe) is already annotated,
    or if the span can't be tagged atomically (force=False and some overlapping
    token already carries a different non-O tag).

    Tagging is all-or-nothing: partially tagging a span (e.g. only its later
    tokens, because an earlier token was already tagged by something else)
    would write a stray I- tag with no B- of its own, which silently merges
    into the neighboring entity when spans are reconstructed from BIO tags.

    force: overwrite existing non-O NER tags on overlapping tokens.
    drop_overlaps: remove any existing labels overlapping [ps, pe) from sent.labels.
    entity_type="O" clears NER on overlapping tokens instead of tagging.
    token_spans: precomputed _token_spans(sent) — pass it in (computed once
    per sentence) rather than recomputing it on every call.
    """
    gold = list(sent.labels or [])
    if skip_existing and (ps, pe) in {(l["start"], l["end"]) for l in gold}:
        return None
    if drop_overlaps:
        gold = [l for l in gold if not (l["start"] < pe and l["end"] > ps)]

    if token_spans is None:
        token_spans = _token_spans(sent)
    is_remove = entity_type.upper() == "O"
    overlapping = [(ts, te, tok) for ts, te, tok in token_spans if ts < pe and te > ps]
    if not overlapping:
        return None
    if (
        not force
        and not is_remove
        and any(_has_non_o_tag(tok["misc"]) for _, _, tok in overlapping)
    ):
        return None

    changed = False
    for ts, te, tok in overlapping:
        if is_remove:
            tok["misc"], tok_changed = _set_ner_in_misc(tok["misc"], "O", force=True)
            changed = changed or tok_changed
            continue
        tok_ns = SimpleNamespace(start_char=ts, end_char=te)
        new_tag = assign_bio_tag(
            tok_ns, [{"start": ps, "end": pe, "type": entity_type}]
        )
        tok["misc"], tok_changed = _set_ner_in_misc(tok["misc"], new_tag, force=force)
        changed = changed or tok_changed

    if not changed:
        return None
    if is_remove:
        return gold
    return gold + [
        {"text": sent.text[ps:pe], "type": entity_type, "start": ps, "end": pe}
    ]


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


def _apply_patterns(data, pattern_strs: list[str]) -> list[dict]:
    """Parse 'text:type' patterns and tag every matching span that isn't already
    annotated. Returns the list of annotations actually added."""
    text_patterns = []
    for p in pattern_strs:
        if ":" not in p:
            raise ValueError(f"Pattern '{p}' must be in format 'text:type'")
        text, etype = p.rsplit(":", 1)
        text_patterns.append((text.strip(), etype.strip()))

    changes = []
    for s in data.samples:
        for sent in s.sentences:
            if not sent.text:
                continue
            token_spans = _token_spans(sent)
            token_span_set = {(ts, te) for ts, te, _ in token_spans}
            for pattern_text, entity_type in text_patterns:
                for ps, pe in _find_all(sent.text, pattern_text, token_span_set):
                    new_labels = _tag_pattern_span(
                        sent,
                        ps,
                        pe,
                        entity_type,
                        skip_existing=True,
                        token_spans=token_spans,
                    )
                    if new_labels is not None:
                        sent.labels = new_labels
                        print(
                            f"  PATTERN: '{pattern_text}' [{ps}:{pe}] → {entity_type} in [{sent.sent_id}]"
                        )
                        changes.append(
                            {
                                "sent_id": sent.sent_id,
                                "text": pattern_text,
                                "type": entity_type,
                                "start": ps,
                                "end": pe,
                            }
                        )
    if text_patterns:
        print(f"Pattern annotations added: {len(changes)}")
    return changes


def _apply_corrections(data, sent_index, correction_strs: list[str]) -> list[dict]:
    """Parse 'sent_id:text:new_type' corrections and overwrite the matching span's
    label (new_type='O' removes it). Returns the list of corrections actually applied."""
    corrections = []
    for c in correction_strs:
        parts = c.split(":", 2)
        if len(parts) != 3:
            raise ValueError(
                f"Correction '{c}' must be in format 'sent_id:text:new_type'"
            )
        sent_id, text, new_type = parts
        corrections.append((sent_id.strip(), text.strip(), new_type.strip()))

    changes = []
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
        token_spans = _token_spans(sent)
        token_span_set = {(ts, te) for ts, te, _ in token_spans}
        for ps, pe in _find_all(sent.text, pattern_text, token_span_set):
            new_labels = _tag_pattern_span(
                sent,
                ps,
                pe,
                new_type,
                force=True,
                drop_overlaps=True,
                token_spans=token_spans,
            )
            if new_labels is None:
                continue
            sent.labels = new_labels
            print(
                f"  CORRECTION: '{pattern_text}' [{ps}:{pe}] → {new_type} in [{sent_id}]"
            )
            changes.append(
                {
                    "sent_id": sent_id,
                    "text": pattern_text,
                    "type": new_type,
                    "start": ps,
                    "end": pe,
                }
            )
    if corrections:
        print(f"Corrections applied: {len(changes)}")
    return changes


def _apply_extend_prev(data, sent_index, extend_prev_strs: list[str]) -> list[dict]:
    """Parse 'sent_id:text:type' entries and extend each matched span to include
    its preceding token. Returns the list of annotations actually added."""
    extend_prev_patterns = []
    for p in extend_prev_strs:
        parts = p.split(":", 2)
        if len(parts) != 3:
            raise ValueError(f"extend-prev '{p}' must be in format 'sent_id:text:type'")
        sent_id, text, etype = parts
        extend_prev_patterns.append((sent_id.strip(), text.strip(), etype.strip()))

    changes = []
    for sent_id, pattern_text, entity_type in extend_prev_patterns:
        sent = sent_index.get(sent_id)
        if sent is None:
            print(f"  EXTEND-PREV WARNING: sent_id '{sent_id}' not found")
            continue
        if not sent.text:
            continue
        tok_spans = _token_spans(sent)
        token_span_set = {(ts, te) for ts, te, _ in tok_spans}
        for ps, pe in _find_all(sent.text, pattern_text, token_span_set):
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

            new_labels = _tag_pattern_span(
                sent,
                new_ps,
                new_pe,
                entity_type,
                force=True,
                drop_overlaps=True,
                token_spans=tok_spans,
            )
            if new_labels is None:
                continue
            sent.labels = new_labels
            print(
                f"  EXTEND-PREV: '{full_text}' [{new_ps}:{new_pe}] → {entity_type} in [{sent_id}]"
            )
            changes.append(
                {
                    "sent_id": sent_id,
                    "text": full_text,
                    "type": entity_type,
                    "start": new_ps,
                    "end": new_pe,
                }
            )
    if extend_prev_patterns:
        print(f"Extend-prev annotations added: {len(changes)}")
    return changes


def _append_changelog(
    args,
    out_path,
    pattern_changes,
    correction_changes,
    extend_prev_changes,
    rules,
    rule_changes,
):
    changelog = Path(__file__).parent / args.dataset_name / "CHANGELOG.md"
    cmd = " \\\n  ".join(
        ["python data_quality/patch_missing_annotations.py"] + sys.argv[1:]
    )

    lines = [f"\n## {date.today()} — {Path(args.input_dir).name} → {out_path.name}"]
    lines.append(f"**Input:** `{args.input_dir}`")
    lines.append(f"**Output:** `{args.output}`")
    lines.append(f"**Script:**\n```bash\n{cmd}\n```")
    lines.append("**Changes:**")
    if pattern_changes:
        lines.append(f"- {len(pattern_changes)} pattern annotation(s):")
        for ch in pattern_changes:
            lines.append(
                f"  - [{ch['sent_id']}] '{ch['text']}' [{ch['start']}:{ch['end']}] → {ch['type']}"
            )
    if correction_changes:
        lines.append(f"- {len(correction_changes)} correction(s):")
        for ch in correction_changes:
            lines.append(
                f"  - [{ch['sent_id']}] '{ch['text']}' [{ch['start']}:{ch['end']}] → {ch['type']}"
            )
    if extend_prev_changes:
        lines.append(f"- {len(extend_prev_changes)} extend-prev annotation(s):")
        for ch in extend_prev_changes:
            lines.append(
                f"  - [{ch['sent_id']}] '{ch['text']}' [{ch['start']}:{ch['end']}] → {ch['type']}"
            )
    if rules:
        lines.append(
            f"- {len(rules)} rule(s) applied from: {', '.join(args.rules_json)}"
        )
        counts_by_rule = {}
        for ch in rule_changes:
            counts_by_rule[ch["rule_id"]] = counts_by_rule.get(ch["rule_id"], 0) + 1
        for r in rules:
            n = counts_by_rule.get(r.id, 0)
            lines.append(
                f"  - `{r.id}` **{r.name}**: `{r.content}` — {n} annotation(s) added"
            )

    if not any([pattern_changes, correction_changes, extend_prev_changes, rules]):
        lines.append("- (no changes recorded)")

    changelog.parent.mkdir(parents=True, exist_ok=True)
    with changelog.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Changelog updated: {changelog}")


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
        "--rule-id",
        type=str,
        nargs="*",
        default=[],
        help="Apply only rules with these IDs (from --rules-json)",
    )
    parser.add_argument(
        "--input-dir", type=str, required=True, help="Path to data (CONLLU format)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--dataset-name",
        type=str,
        required=True,
        help="Dataset name, used to pick the changelog file: data_quality/<dataset-name>/CHANGELOG.md",
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
    parser.add_argument(
        "--patterns-file",
        default=None,
        help="JSON file with ['text:type', ...] patterns",
    )
    args = parser.parse_args()

    data = load_ner_dataset_from_conll(args.input_dir)
    if args.patterns_file:
        extra = json.loads(Path(args.patterns_file).read_text())
        args.patterns = args.patterns + extra

    rules, rule_changes = _apply_rule_predictions(data, args.rules_json, args.rule_id)
    pattern_changes = _apply_patterns(data, args.patterns)

    sent_index = {sent.sent_id: sent for s in data.samples for sent in s.sentences}
    correction_changes = _apply_corrections(data, sent_index, args.corrections)
    extend_prev_changes = _apply_extend_prev(data, sent_index, args.extend_prev)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(data.to_conll(), encoding="utf-8")
    print(f"Written to {out_path}")

    _append_changelog(
        args,
        out_path,
        pattern_changes,
        correction_changes,
        extend_prev_changes,
        rules,
        rule_changes,
    )


if __name__ == "__main__":
    main()
