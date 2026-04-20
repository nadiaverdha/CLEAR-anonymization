import argparse
import random
from collections import defaultdict
from pathlib import Path

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.ner_datasets.ner_dataset import NERData


def split_dev_set(data, dev_ratio=0.2, seed=42):
    rng = random.Random(seed)

    samples = list(data.samples)
    rng.shuffle(samples)

    split_idx = int(len(samples) * (1 - dev_ratio))

    train_samples = samples[:split_idx]
    dev_samples = samples[split_idx:]

    print(f"Train: {len(train_samples)}, Test: {len(dev_samples)}")

    return (NERData(samples=train_samples), NERData(samples=dev_samples))


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

    args = parser.parse_args()

    full_train_data = load_ner_dataset_from_conll(Path(args.train_file))
    train_data, dev_data = split_dev_set(
        full_train_data, dev_ratio=args.dev_ratio, seed=args.seed
    )

    print(
        f"Train: {len(train_data.samples)} samples, Test: {len(dev_data.samples)} samples"
    )
    train_path = Path(args.output_dir + "/" + "findok_train.conllu")
    dev_path = Path(args.output_dir + "/" + "findok_dev.conllu")
    print("Writing the splits to:", train_path, " & ", dev_path)
    train_path.write_text(train_data.to_conll())
    dev_path.write_text(dev_data.to_conll())


if __name__ == "__main__":
    main()
