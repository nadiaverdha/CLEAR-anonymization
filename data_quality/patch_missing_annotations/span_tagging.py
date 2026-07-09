from types import SimpleNamespace

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
    exactly matches one of token_span_set.
    - token_span_set: precomputed {(start, end), ...} for the sentence's tokens"""
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
