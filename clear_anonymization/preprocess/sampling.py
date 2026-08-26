import random
import re
from itertools import combinations

from clear_anonymization.ner_datasets.util import (
    build_marked_text_relations,
    recreate_sent_relations,
)


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


def _doc_sentences(doc, classes):
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


def make_negative_examples(sample, relations_by_sent, seed=0):
    rng = random.Random(seed)
    negatives = []
    for sent in sample.sentences:
        entities = [{**label, "sent_id": sent.sent_id} for label in (sent.labels or [])]
        if len(entities) < 2:
            continue
        linked = {
            frozenset(
                [
                    (rel["governor"]["start"], rel["governor"]["sent_id"]),
                    (rel["dependent"]["start"], rel["dependent"]["sent_id"]),
                ]
            )
            for rel in relations_by_sent[sent.sent_id]
        }

        candidates = [
            (a, b)
            for a, b in combinations(entities, 2)
            if frozenset([(a["start"], a["sent_id"]), (b["start"], b["sent_id"])])
            not in linked
        ]

        n_pos = max(len(relations_by_sent[sent.sent_id]), 1)
        k = min(len(candidates), n_pos)
        negatives.extend(rng.sample(candidates, k))
    return negatives


def sample_relation_few_shot(
    train_data,
    seed=42,
    train_ratio=0.7,
    relation_labels=None,
    num_labels=None,
    pool_size=None,
    shuffle=True,
    include_negatives=True,
):
    """
    train_data: list of NERSample (document level).
    Shuffle and train/eval split are at document level so a document's
    relations never straddle both sets.
    Returns (train_examples, eval_examples, n_train_docs, n_eval_docs).
    """
    rng = random.Random(seed)
    relations_by_doc = {
        doc.doc_id: recreate_sent_relations(doc.sentences) for doc in train_data
    }
    if not relation_labels:
        all_labels = sorted(
            {
                rel["label"]
                for relations_by_sent in relations_by_doc.values()
                for rels in relations_by_sent.values()
                for rel in rels
            }
        )
        if num_labels and num_labels < len(all_labels):
            rng.shuffle(all_labels)
            relation_labels = set(all_labels[:num_labels])
        else:
            relation_labels = set(all_labels)
    pos_docs, neg_docs = [], []

    for doc in train_data:
        relations_by_sent = relations_by_doc[doc.doc_id]
        has_target = any(
            rel["label"] in relation_labels
            for rels in relations_by_sent.values()
            for rel in rels
        )
        (pos_docs if has_target else neg_docs).append(doc)
    if shuffle:
        rng.shuffle(pos_docs)
        rng.shuffle(neg_docs)
    pool = pos_docs[:pool_size] if pool_size else pos_docs
    split_idx = int(len(pool) * train_ratio)
    n_train_docs, n_eval_docs = split_idx, len(pool) - split_idx

    def _doc_examples(doc):
        relations_by_sent = relations_by_doc[doc.doc_id]
        examples = [
            (
                build_marked_text_relations(
                    doc.sentences, rel["governor"], rel["dependent"]
                ),
                rel["label"],
            )
            for rels in relations_by_sent.values()
            for rel in rels
            if rel["label"] in relation_labels
        ]
        if include_negatives:
            examples += [
                (build_marked_text_relations(doc.sentences, a, b), "")
                for a, b in make_negative_examples(doc, relations_by_sent, seed=seed)
            ]
        return examples

    train_examples = [ex for doc in pool[:split_idx] for ex in _doc_examples(doc)]
    eval_examples = [ex for doc in pool[split_idx:] for ex in _doc_examples(doc)]

    return train_examples, eval_examples, relation_labels, n_train_docs, n_eval_docs
