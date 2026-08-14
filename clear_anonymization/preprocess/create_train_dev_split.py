import argparse
import random
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from iterstrat.ml_stratifiers import MultilabelStratifiedShuffleSplit

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.ner_datasets.ner_dataset import NERData
from clear_anonymization.ner_datasets.util import recreate_sent_relations


def split_dev_set(data, dev_ratio=0.2, seed=42):
    rng = random.Random(seed)

    samples = list(data.samples)
    rng.shuffle(samples)
    print(len(samples))

    split_idx = int(len(samples) * (1 - dev_ratio))

    train_samples = samples[:split_idx]
    train_ids = {s.doc_id.split("/")[-1] for s in train_samples}
    print(train_ids)
    dev_samples = samples[split_idx:]
    dev_samples = [
        sample
        for sample in dev_samples
        if sample.doc_id.split("/")[-1] not in train_ids
    ]
    dev_samples = [
        sample
        for sample in dev_samples
        if sample.doc_id.split("/")[0]
        not in {
            "findok-manually-annotated-filtered-higher-courts_TRAIN",
            "findok-manually-annotated-filtered-higher-courts_VALIDATE",
        }
    ]
    dev_ids = {s.doc_id.split("/")[-1] for s in dev_samples}
    print(dev_ids)
    print(f"Train: {len(train_samples)}, Test: {len(dev_samples)}")

    i = 0
    for s in dev_samples:
        # print(s.doc_id.split("/")[0])
        if (
            s.doc_id.split("/")[0]
            == "findok-manually-annotated-filtered-higher-courts_TRAIN"
            or s.doc_id.split("/")[0]
            == "findok-manually-annotated-filtered-higher-courts_VALIDATE"
        ):
            i += 1
    print(i)
    return (NERData(samples=train_samples), NERData(samples=dev_samples))


def label_distribution_doc(samples) -> Counter:
    return Counter(
        label["type"] for s in samples for sent in s.sentences for label in sent.labels
    )


def label_distribution_sent(samples) -> Counter:
    return Counter(label["type"] for sample in samples for label in sample["entities"])


def print_distribution(samples, name: str, fn=label_distribution_doc) -> None:
    dist = fn(samples)
    total = sum(dist.values())
    print(f"\n{name} ({len(samples)} sentences, {total} entities):")
    for label, count in sorted(dist.items()):
        print(f"  {label}: {count} ({count / total:.1%})")


def split_dev_set_stratified(data, dev_ratio=0.2, seed=42):
    samples = list(data.samples)

    samples.sort(key=lambda s: s.doc_id)  # matches sorted zip folder order

    all_types = sorted(
        {
            label["type"]
            for s in samples
            for sent in s.sentences
            for label in sent.labels
        }
    )
    type_to_idx = {t: i for i, t in enumerate(all_types)}

    y = np.zeros((len(samples), len(all_types)), dtype=int)
    for i, s in enumerate(samples):
        for sent in s.sentences:
            for label in sent.labels:
                y[i, type_to_idx[label["type"]]] = 1

    cv = MultilabelStratifiedShuffleSplit(
        test_size=dev_ratio, train_size=1 - dev_ratio, random_state=seed
    )
    train_idx, dev_idx = next(cv.split(X=samples, y=y))

    train_samples = [samples[i] for i in train_idx]
    dev_samples = [samples[i] for i in dev_idx]

    print_distribution(samples, "Full dataset")
    print_distribution(train_samples, "Train")
    print_distribution(dev_samples, "Dev")
    return NERData(samples=train_samples), NERData(samples=dev_samples)


def label_distribution_relations(samples) -> Counter:
    counts = Counter()
    for sample in samples:
        relations_by_sent = recreate_sent_relations(sample.sentences)
        for sent in sample.sentences:
            for rel in relations_by_sent[sent.sent_id]:
                counts[rel["label"]] += 1
    return counts


def doc_relation_labels(sample):
    labels = set()
    relations_by_sent = recreate_sent_relations(sample.sentences)
    for sent in sample.sentences:
        for rel in relations_by_sent[sent.sent_id]:
            labels.add(rel["label"])
    return labels


def split_dev_set_stratified_relations(data, dev_ratio=0.2, seed=42):
    samples = list(data.samples)
    samples.sort(key=lambda s: s.doc_id)

    all_types = sorted(
        {
            label["type"]
            for s in samples
            for sent in s.sentences
            for label in sent.labels
        }
    )
    type_to_idx = {t: i for i, t in enumerate(all_types)}

    all_rel_labels = sorted({l for s in samples for l in doc_relation_labels(s)})
    rel_to_idx = {l: i for i, l in enumerate(all_rel_labels)}

    y_types = np.zeros((len(samples), len(all_types)), dtype=int)
    y_rels = np.zeros((len(samples), len(all_rel_labels)), dtype=int)
    for i, s in enumerate(samples):
        for sent in s.sentences:
            for label in sent.labels:
                y_types[i, type_to_idx[label["type"]]] = 1
        for l in doc_relation_labels(s):
            y_rels[i, rel_to_idx[l]] = 1

    y = np.hstack([y_types, y_rels])

    cv = MultilabelStratifiedShuffleSplit(
        test_size=dev_ratio, train_size=1 - dev_ratio, random_state=seed
    )
    train_idx, dev_idx = next(cv.split(X=samples, y=y))

    train_samples = [samples[i] for i in train_idx]
    dev_samples = [samples[i] for i in dev_idx]

    print_distribution(samples, "Full dataset", fn=label_distribution_relations)
    print_distribution(train_samples, "Train", fn=label_distribution_relations)
    print_distribution(dev_samples, "Dev", fn=label_distribution_relations)
    return NERData(samples=train_samples), NERData(samples=dev_samples)


def main():
    parser = argparse.ArgumentParser(
        description=" Named Entity Recognition Benchmark for RuleChef"
    )
    parser.add_argument(
        "--train-file",
        type=str,
        help="Path to the train data (JSON format)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="/share/nverdha/data/bfg/",
        help="Path to the output directory",
    )
    parser.add_argument(
        "--dev-ratio",
        type=float,
        default=0.2,
        help="Ratio of dev data (default: 0.2)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed (default: 42)",
    )
    parser.add_argument(
        "--dataset-name",
        type=str,
        default="findok",
        help="Name of the dataset (default: ris)",
    )
    parser.add_argument(
        "--stratified",
        action="store_true",
        default=True,
        help="Use stratified splitting",
    )

    parser.add_argument(
        "--relations",
        action="store_true",
        default=False,
        help="Use stratified splitting",
    )

    args = parser.parse_args()
    print("loading data")
    full_train_data = load_ner_dataset_from_conll(Path(args.train_file))
    print("loading finished.")

    if args.stratified:
        train_data, dev_data = split_dev_set_stratified(
            full_train_data, dev_ratio=args.dev_ratio, seed=args.seed
        )

        if args.relations:
            train_data, dev_data = split_dev_set_stratified_relations(
                full_train_data, dev_ratio=args.dev_ratio, seed=args.seed
            )

    else:
        train_data, dev_data = split_dev_set(
            full_train_data, dev_ratio=args.dev_ratio, seed=args.seed
        )

    print(
        f"Train: {len(train_data.samples)} samples, Test: {len(dev_data.samples)} samples"
    )
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.relations:
        train_path = output_dir / f"{args.dataset_name}_train_relations_training.conllu"
        dev_path = output_dir / f"{args.dataset_name}_train_relations_dev.conllu"
    else:
        train_path = output_dir / f"{args.dataset_name}_train_training.conllu"
        dev_path = output_dir / f"{args.dataset_name}_train_dev.conllu"

    print("Writing the splits to:", train_path, " & ", dev_path)

    train_path.write_text(train_data.to_conll())
    dev_path.write_text(dev_data.to_conll())


if __name__ == "__main__":
    main()
