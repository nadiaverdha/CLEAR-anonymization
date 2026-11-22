import random
from collections import defaultdict

from clear_anonymization.ner_datasets.util import (
    build_relation_examples,
)


def _doc_sentences(doc, classes):
    """Turn one document into a list of sentence dicts.
    Only labels of the target classes are kept, sorted by position."""
    return [
        {
            "doc_id": doc.doc_id,
            "sent_id": sent.sent_id,
            "text": sent.text,
            "entities": sorted(
                [l for l in sent.labels if l["type"] in classes],
                key=lambda l: l["start"],
            ),
        }
        for sent in doc.sentences
    ]


def _split_docs(docs, ratio):
    """First `ratio` of the docs -> train, rest -> eval."""
    idx = int(len(docs) * ratio)
    return docs[:idx], docs[idx:]


def _sentences_with_entities(docs):
    return [s for doc in docs for s in doc if s["entities"]]


def _sentences_without_entities(docs):
    return [s for doc in docs for s in doc if not s["entities"]]


def _take_random(sentences, n, rng):
    """Random subset of size n, or all sentences if there are not more than n."""
    if len(sentences) <= n:
        return sentences
    return rng.sample(sentences, n)


def _doc_examples(doc, relation_labels, other_label="no_relation"):
    examples = []
    for ex in build_relation_examples(doc):
        if ex["label"] not in relation_labels:
            ex = {**ex, "label": other_label}
        examples.append(ex)
    return examples


def sample_train_eval(
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
    Split the training documents into a train set and an internal eval set.

    train_data: list of NERSample (documents).
    The split is done per document, so sentences of one document never
    end up in both train and eval.

    Returns (train, eval, counter_examples, classes, n_train_docs, n_eval_docs).
    """
    rng = random.Random(seed)

    # 1. Decide which entity classes to learn. If none are given, use all classes (or a random subset of num_classes).
    if classes is None:
        all_classes = sorted(
            {
                l["type"]
                for doc in train_data
                for sent in doc.sentences
                for l in sent.labels
            }
        )
        if num_classes is not None and num_classes < len(all_classes):
            rng.shuffle(all_classes)
            all_classes = all_classes[:num_classes]
        classes = all_classes
    classes = set(classes)

    # 2. Group documents: with at least one target entity (positive) or without (negative).
    docs = [_doc_sentences(doc, classes) for doc in train_data]
    pos_docs = [doc for doc in docs if any(s["entities"] for s in doc)]
    neg_docs = [doc for doc in docs if not any(s["entities"] for s in doc)]

    # 3. Shuffle documents, then split each group into train and eval.
    if shuffle:
        rng.shuffle(pos_docs)
        rng.shuffle(neg_docs)
    pos_train_docs, pos_eval_docs = _split_docs(pos_docs, train_ratio)
    neg_train_docs, neg_eval_docs = _split_docs(neg_docs, train_ratio)

    if pool_size is not None:
        pos_train_docs = pos_train_docs[:pool_size]

    # 5. Positive examples = sentences that contain a target entity.
    train = _sentences_with_entities(pos_train_docs)
    eval_ = _sentences_with_entities(pos_eval_docs)

    # 6. Negative examples = sentences without a target entity,
    #    neg_ratio negatives per positive (None = no negatives).
    #    eval uses neg_ratio too, unless eval_neg_ratio is set.
    if eval_neg_ratio is None:
        eval_neg_ratio = neg_ratio

    train_negatives = []
    if neg_ratio is not None:
        pool = _sentences_without_entities(pos_train_docs + neg_train_docs)
        train_negatives = _take_random(pool, int(neg_ratio * len(train)), rng)

    eval_negatives = []
    if eval_neg_ratio is not None:
        pool = _sentences_without_entities(pos_eval_docs + neg_eval_docs)
        eval_negatives = _take_random(pool, int(eval_neg_ratio * len(eval_)), rng)

    # 7. Add the negatives and shuffle, so they are spread over the batches.
    #    (Keep this after step 6: changing the order of rng calls changes the split.)
    if train_negatives:
        train = train + train_negatives
        rng.shuffle(train)
    if eval_negatives:
        eval_ = eval_ + eval_negatives
        rng.shuffle(eval_)

    return train, eval_, [], classes, len(pos_train_docs), len(pos_eval_docs)


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
