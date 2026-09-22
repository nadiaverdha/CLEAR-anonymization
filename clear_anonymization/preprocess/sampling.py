import random
import re
from collections import defaultdict

from clear_anonymization.ner_datasets.util import (
    build_relation_examples,
    recreate_sent_relations,
)


def _doc_sentences(
    doc,
    classes,
):
    for sent in doc.sentences:
        entities = sorted(
            [l for l in sent.labels if l["type"] in classes],
            key=lambda x: x["start"],
        )
        yield {"text": sent.text, "entities": entities}


def sample_few_shot(
    train_data,
    seed=42,
    num_classes=None,
    classes=None,
    pool_size=None,
    train_ratio=0.7,
    shuffle=True,
):
    """
    train_data: list of NERSample (document level).
    Shuffle and train/eval split are at document level so sentences
    from the same document are never split across sets.
    Returns (train, eval, counter_examples, selected_classes, n_train_docs, n_eval_docs).
    """
    rng = random.Random(seed)
    if not classes:
        all_labels = sorted(
            {
                l["type"]
                for doc in train_data
                for sent in doc.sentences
                for l in sent.labels
            }
        )
        if num_classes and num_classes < len(all_labels):
            rng.shuffle(all_labels)
            classes = set(all_labels[:num_classes])
        else:
            classes = set(all_labels)

    classes = set(classes)
    pos_docs = []
    neg_docs = []
    for doc in train_data:
        sents = list(_doc_sentences(doc, classes))
        if any(s["entities"] for s in sents):
            pos_docs.append(sents)
        else:
            neg_docs.append(sents)

    if shuffle:
        rng.shuffle(pos_docs)
        rng.shuffle(neg_docs)

    pool = pos_docs[:pool_size] if pool_size else pos_docs
    split_idx = int(len(pool) * train_ratio)

    n_train_docs = split_idx
    n_eval_docs = len(pool) - split_idx

    train_examples = [s for doc in pool[:split_idx] for s in doc if s["entities"]]
    eval_examples = [s for doc in pool[split_idx:] for s in doc if s["entities"]]
    negatives = [s for doc in neg_docs for s in doc] + [
        s for doc in pool for s in doc if not s["entities"]
    ]

    return (
        train_examples,
        eval_examples,
        negatives,
        classes,
        n_train_docs,
        n_eval_docs,
    )


def sample_relation_stratified(
    train_data,
    shots_per_class,
    seed=42,
    num_classes=None,
    classes=None,
):
    rng = random.Random(seed)
    by_label = defaultdict(list)
    for doc in train_data:
        for ex in build_relation_examples(doc):
            by_label[ex["label"]].append(ex)

    labels = sorted(by_label.keys())
    if classes:
        missing = set(classes) - set(labels)
        if missing:
            print(f"WARNING: classes not found in dataset: {missing}")
        labels = sorted(c for c in classes if c in by_label)
    elif num_classes and num_classes < len(labels):
        rng.shuffle(labels)
        labels = sorted(labels[:num_classes])

    sampled = []
    remaining = []
    for label in labels:
        examples = by_label[label]
        rng.shuffle(examples)
        sampled.extend(examples[:shots_per_class])
        remaining.extend(examples[shots_per_class:])

    return sampled, remaining, set(labels)
