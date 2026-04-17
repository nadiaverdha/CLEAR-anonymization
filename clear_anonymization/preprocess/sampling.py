import random
import re


def select_windows(text, entities, window_size=20):
    merged_windows = []
    for ent in entities:
        start = max(0, ent["start"] - window_size)
        end = min(len(text), ent["end"] + window_size)
        if merged_windows and start <= merged_windows[-1][1]:
            merged_windows[-1][1] = max(end, merged_windows[-1][1])
            merged_windows[-1][2].append(ent)
        else:
            merged_windows.append([start, end, [ent]])
    return merged_windows


def build_examples(text, merged_windows):
    examples = []
    for start, end, window_entities in merged_windows:
        snippet = text[start:end]
        adjusted_entities = [
            {
                "text": e["text"],
                "start": e["start"] - start,
                "end": e["end"] - start,
                "type": e["type"],
            }
            for e in window_entities
        ]
        examples.append({"text": snippet, "entities": adjusted_entities})
    return examples


def sample_few_shot(
    train_data,
    windows,
    seed=42,
    num_classes=None,
    classes=None,
    window_size=200,
    pool_size=None,
    train_ratio=0.7,
):
    rng = random.Random(seed)
    use_filter = classes is not None

    doc_samples = [
        sent
        for s in train_data.samples
        for sent in (s.sentences if s.sentences else [s])
    ]
    if not classes:
        all_labels = sorted({l["type"] for s in doc_samples for l in s.labels})
        if num_classes and num_classes < len(all_labels):
            rng.shuffle(all_labels)
            classes = set(all_labels[:num_classes])
            use_filter = True
        else:
            classes = set(all_labels)

    classes = set(classes)
    all_examples = []
    negatives = []
    seen_texts = set()

    for sample in doc_samples:
        text = sample.text
        if use_filter:
            entities = sorted(
                [l for l in sample.labels if l["type"] in classes],
                key=lambda x: x["start"],
            )
        else:
            entities = list(sample.labels)

        if text in seen_texts:
            continue
        seen_texts.add(text)

        if not entities:
            other_entities = (
                [l for l in sample.labels if l["type"] not in classes]
                if use_filter
                else []
            )
            negatives.append({"text": text, "entities": other_entities})
            continue

        if windows:
            for ex in build_examples(text, select_windows(text, entities, window_size)):
                if ex["text"] not in seen_texts:
                    seen_texts.add(ex["text"])
                    all_examples.append(ex)
        else:
            all_examples.append({"text": text, "entities": entities})

    # print(f"Total positives: {len(all_examples)}, negatives: {len(negatives)}")

    rng.shuffle(all_examples)
    rng.shuffle(negatives)
    pool = all_examples[:pool_size] if pool_size else all_examples

    split_idx = int(len(pool) * train_ratio)
    train_examples = pool[:split_idx]
    eval_examples = pool[split_idx:]
    for i in train_examples[:3]:
        print(i)

    return train_examples, eval_examples, negatives, classes
