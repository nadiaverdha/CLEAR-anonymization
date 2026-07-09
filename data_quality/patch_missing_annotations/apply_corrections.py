from data_quality.patch_missing_annotations.span_tagging import (
    _find_all,
    _tag_pattern_span,
    _token_spans,
)


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
