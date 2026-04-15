import argparse
import re
import json
import os
import random
import time
import uuid
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import List, Optional

from clear_anonymization.ner_datasets.ner_dataset import NERData


def split_test(train_data, test_ratio=0.2, seed=42):
    rng = random.Random(seed)
    samples = list(train_data.samples)

    class_counts = defaultdict(int)
    for sample in samples:
        print(sample.doc_id)
        for label in {l["type"] for l in sample.labels}:
            class_counts[label] += 1

    print("Full distribution:", dict(class_counts))
    print("--------------------------------------")

    test_quota = {
        label: max(1, int(cnt * test_ratio)) for label, cnt in class_counts.items()
    }

    print("Target test quota:", test_quota)
    print("--------------------------------------")

    test_filled = defaultdict(int)

    rng.shuffle(samples)

    samples.sort(
        key=lambda s: min(
            (class_counts[l["type"]] for l in s.labels), default=float("inf")
        )
    )

    test_samples = []
    train_samples = []

    for sample in samples:
        sample_labels = {l["type"] for l in sample.labels}
        if sample_labels and all(
            test_filled[label] < test_quota[label] for label in sample_labels
        ):
            test_samples.append(sample)

            for label in sample_labels:
                test_filled[label] += 1
        else:
            train_samples.append(sample)

    rng.shuffle(train_samples)
    rng.shuffle(test_samples)

    print(f"Train: {len(train_samples)} samples, Test: {len(test_samples)} samples")
    print("--------------------------------------")
    print("Test class distribution:", dict(test_filled))

    return NERData(samples=train_samples), NERData(samples=test_samples)


def save_conll(examples, path):
    with open(path, "w", encoding="utf-8") as f:
        for i, ex in enumerate(examples):
            sentences = ex.sentences if ex.sentences is not None else [ex]
            for sent in sentences:
                doc_id = getattr(sent, "doc_id", None)
                text = sent.text
                split = getattr(sent, "split", "")
                entities = sorted(sent.labels, key=lambda e: e["start"])

                f.write(f"# doc_id = {doc_id}\n")
                f.write(f"# sent = {text}\n")
                f.write(f"# split = {split}\n")
                f.write(f"# entities\n")

                """
                
                char_tag = {}
                for ent in entities:
                    for pos in range(ent["start"], ent["end"]):
                        char_tag[pos] = (ent["type"], pos == ent["start"])

                for m in re.finditer(r"\S+", text):
                    word = m.group()
                    start = m.start()
                    if start in char_tag:
                        etype, is_start = char_tag[start]
                        tag = f"B-{etype}" if is_start else f"I-{etype}"
                        f.write(f"{word} {tag}\n")
                    else:
                        tag = "O"
                    
                """
                for ent in entities:
                    f.write(f"{ent['text']} {ent['type']}\n")

                f.write("\n")


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
        "--test-ratio",
        type=float,
        default=0.2,
        help="Ratio of test data (default: 0.2)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed (default: 42)",
    )

    args = parser.parse_args()

    train_data = NERData.from_json(json.loads(Path(args.train_file).read_text()))
    train_split, test_split = split_test(
        train_data, test_ratio=args.test_ratio, seed=args.seed
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "train.json").write_text(json.dumps(train_split.to_json(), indent=2))
    (output_dir / "test.json").write_text(json.dumps(test_split.to_json(), indent=2))
    save_conll(train_split.samples, output_dir / "train.conll")
    save_conll(test_split.samples, output_dir / "test.conll")

    print(
        f"Train: {len(train_split.samples)} samples, Test: {len(test_split.samples)} samples"
    )


if __name__ == "__main__":
    main()
