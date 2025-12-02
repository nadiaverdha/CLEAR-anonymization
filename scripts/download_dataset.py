"""Script to download datasets from Hugging Face Hub to JSON format."""

import argparse
import json
import logging
from pathlib import Path

from datasets import load_dataset


def download_dataset(repository_id: str, output_path: Path) -> None:
    dataset_dict = load_dataset(repository_id)

    samples = []

    for split_name, split_dataset in dataset_dict.items():
        for sample in split_dataset:
            samples.append(
                {
                    "tokens": sample["tokens"],
                    "sentences": " ".join(str(tokens) for tokens in sample["tokens"]),
                    "ner_labels": sample["ner"],
                    "coarse_ner_labels": sample["coarse-ner"],
                    "split": split_name,
                }
            )

    # Save to JSON (as a list of samples, not wrapped in a "samples" field)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(samples, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description="Download a dataset from the Hugging Face Hub"
    )
    parser.add_argument(
        "--repository_id",
        type=str,
        required=True,
        help="Repository ID on Hugging Face (e.g., 'username/dataset-name')",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        required=True,
        help="Path where to save the JSON file",
    )

    args = parser.parse_args()

    download_dataset(
        repository_id=args.repository_id,
        output_path=Path(args.output_path),
    )


if __name__ == "__main__":
    main()
