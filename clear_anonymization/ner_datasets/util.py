def _parse_misc(misc: str) -> dict:
    misc_parts = {p.split("=")[0]: p.split("=")[1] for p in misc.split("|") if "=" in p}
    return misc_parts


def recreate_sent_labels_from_tokens(tokens, sent):

    tagged = []
    for tok in tokens:
        misc_parts = _parse_misc(tok.get("misc", ""))
        ner = misc_parts.get("NER", "O")
        sent_start = misc_parts.get("SentStart", "_")
        sent_end = misc_parts.get("SentEnd", "_")
        tagged.append((tok["text"], ner, sent_start, sent_end))
    labels = []
    current_span = None
    for _, tag, sent_start, sent_end in tagged:
        if tag.startswith("B-"):
            if current_span:
                labels.append(current_span)
            current_span = {
                "text": sent[int(sent_start) : int(sent_end)],
                "type": tag[2:],
                "start": int(sent_start),
                "end": int(sent_end),
            }
        elif tag.startswith("I-") and current_span:
            current_span["end"] = int(sent_end)
            current_span["text"] = sent[current_span["start"] : int(sent_end)]
        else:
            if current_span:
                labels.append(current_span)
            current_span = None
    if current_span:
        labels.append(current_span)
    return labels


def _entity_span_at(sent: str, sent_offset: int) -> dict | None:
    for label in sent.labels or []:
        if label["start"] <= sent_offset < label["end"]:
            return label
    return None


def _find_token_by_doc_start(sentences, doc_start: int):
    for sent in sentences:
        for tok in sent.tokens:
            misc = _parse_misc(tok.get("misc", ""))
            if misc.get("DocStart") == str(doc_start):
                return tok, sent, misc
    return None, None, None


def recreate_sent_relations(sentences):
    relations_by_sent = {}
    for sent in sentences:
        sent_relations = []
        for tok in sent.tokens:
            misc = _parse_misc(tok.get("misc", ""))
            if "Rel" not in misc:
                continue
            for entry in misc["Rel"].split(";"):
                label, role, partner_doc_start = entry.split(":")
                if role != "governor":
                    continue
                gov_offset = int(misc["SentStart"])
                governor_span = _entity_span_at(sent, gov_offset)

                dep_token, dep_sent, dep_misc = _find_token_by_doc_start(
                    sentences, int(partner_doc_start)
                )

                if dep_token is None:
                    continue
                dependent_span = _entity_span_at(dep_sent, int(dep_misc["SentStart"]))
                if governor_span and dependent_span:
                    sent_relations.append(
                        {
                            "governor": {**governor_span, "sent_id": sent.sent_id},
                            "dependent": {
                                **dependent_span,
                                "sent_id": dep_sent.sent_id,
                            },
                            "label": label,
                        }
                    )

        relations_by_sent[sent.sent_id] = sent_relations
    # print(relations_by_sent)
    return relations_by_sent
