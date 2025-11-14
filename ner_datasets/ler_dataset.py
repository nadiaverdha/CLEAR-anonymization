from dataclasses import dataclass
from typing import Literal

import torch
from torch.utils.data import Dataset


@dataclass
class LERSample:
    tokens: list[str]
    sentences: str
    ner_labels: list[str]
    coarse_ner_labels: list[str]
    split: str

    @classmethod
    def from_json(cls, json_dict: dict) -> "LERSample":
        return cls(
            tokens=json_dict["tokens"],
            sentences=json_dict["sentences"],
            ner_labels=json_dict["ner_labels"],
            coarse_labels=json_dict["coarse_ner_labels"],
            split=json_dict["split"],
        )


@dataclass
class LERData:
    samples = list[LERSample]

    @classmethod
    def from_json(cls, json_dict: list[dict]) -> "LERData":
        return cls(
            samples=[LERSample.from_json(sample) for sample in json_dict],
        )


class LERDataset(Dataset):
    def __init__(self, samples: list[LERSample]):
        self.samples = samples

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int):
        return self.samples[idx]
