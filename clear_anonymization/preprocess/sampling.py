import random
import re
from collections import defaultdict

from clear_anonymization.ner_datasets.util import (
    build_relation_examples,
    recreate_sent_relations,
)


def _doc_sentences(doc, classes=None):
    for sent in doc.sentences:
        labels = (
            sent.labels
            if classes is None
            else [l for l in sent.labels if l["type"] in classes]
        )
        yield {
            "doc_id": doc.doc_id,
            "sent_id": sent.sent_id,
            "text": sent.text,
            "entities": sorted(labels, key=lambda x: x["start"]),
        }


def _split_docs(docs, ratio):
    idx = int(len(docs) * ratio)
    return docs[:idx], docs[idx:]


def _cap(sents, n, rng):
    if n is None or len(sents) <= n:
        return sents
    return rng.sample(sents, n)


def sample_few_shot(
    train_data,
    seed=42,
    num_classes=None,
    classes=None,
    pool_size=None,
    train_ratio=0.7,
    shuffle=True,
    neg_ratio=None,
    eval_neg_ratio=None,
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

    train_all, eval_all = _split_docs(pos_docs, train_ratio)
    neg_train_docs, neg_eval_docs = _split_docs(neg_docs, train_ratio)

    if shuffle:
        rng.shuffle(train_all)
    train_docs = train_all[:pool_size] if pool_size is not None else train_all
    n_train_docs = len(train_docs)
    eval_docs = eval_all
    n_eval_docs = len(eval_docs)

    train_examples = [s for doc in train_docs for s in doc if s["entities"]]
    eval_examples = [s for doc in eval_docs for s in doc if s["entities"]]

    train_neg_pool = [
        s for doc in train_docs + neg_train_docs for s in doc if not s["entities"]
    ]
    eval_neg_pool = [
        s for doc in eval_docs + neg_eval_docs for s in doc if not s["entities"]
    ]
    if eval_neg_ratio is None:
        eval_neg_ratio = neg_ratio

    train_negatives = (
        _cap(train_neg_pool, int(neg_ratio * len(train_examples)), rng)
        if neg_ratio is not None
        else []
    )
    eval_negatives = (
        _cap(eval_neg_pool, int(eval_neg_ratio * len(eval_examples)), rng)
        if eval_neg_ratio is not None
        else []
    )
    if train_negatives:
        train_examples = train_examples + train_negatives
        rng.shuffle(train_examples)
    if eval_negatives:
        eval_examples = eval_examples + eval_negatives
        rng.shuffle(eval_examples)
    return (
        train_examples,
        eval_examples,
        [],
        classes,
        n_train_docs,
        n_eval_docs,
    )


def _doc_examples(doc, relation_labels, other_label="no_relation"):
    examples = []
    for ex in build_relation_examples(doc):
        if ex["label"] not in relation_labels:
            ex = {**ex, "label": other_label}
        examples.append(ex)
    return examples


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
