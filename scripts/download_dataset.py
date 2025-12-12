import argparse
import json
import logging
from pathlib import Path

from datasets import load_dataset


def download_dataset(repository_id: str) -> None:
    dataset_dict = load_dataset(repository_id)

    samples = []

    for split_name, split_dataset in dataset_dict.items():
        for sample in split_dataset:
            samples.append(
                {
                    "tokens": sample["tokens"],
                    "text": " ".join(str(tokens) for tokens in sample["tokens"]),
                    "ner_labels": sample["ner"],
                    "coarse_ner_labels": sample["coarse-ner"],
                    "split": split_name,
                }
            )

    return samples
