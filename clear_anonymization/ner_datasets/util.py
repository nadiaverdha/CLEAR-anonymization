def recreate_sent_labels_from_tokens(tokens, sent):

    tagged = []
    for tok in tokens:
        misc_parts = {
            p.split("=")[0]: p.split("=")[1]
            for p in tok.get("misc", "").split("|")
            if "=" in p
        }
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
