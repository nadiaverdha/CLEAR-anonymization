from data_quality.patch_missing_annotations.span_tagging import (
    _find_all,
    _tag_pattern_span,
    _token_boundaries,
    _token_spans,
)


def _apply_patterns(data, pattern_strs: list[str]) -> list[dict]:
    """Parse 'text:type' patterns and tag every matching span that isn't already
    annotated. Returns the list of annotations actually added."""

    text_patterns = []
    for p in pattern_strs:
        if ":" not in p:
            raise ValueError(f"Pattern '{p}' must be in format 'text:type'")
        text, etype = p.rsplit(":", 1)
        text_patterns.append((text.strip(), etype.strip()))
    text_patterns.sort(key=lambda p: len(p[0]), reverse=True)
    changes = []
    for s in data.samples:
        for sent in s.sentences:
            if not sent.text:
                continue
            token_spans = _token_spans(sent)
            token_starts, token_ends = _token_boundaries(token_spans)
            for pattern_text, entity_type in text_patterns:
                for ps, pe in _find_all(
                    sent.text, pattern_text, token_starts, token_ends
                ):
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
