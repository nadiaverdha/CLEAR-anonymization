from data_quality.patch_missing_annotations.span_tagging import (
    _find_all,
    _tag_pattern_span,
    _token_spans,
)


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
