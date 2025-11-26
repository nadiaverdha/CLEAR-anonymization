from dataclasses import dataclass
from typing import Literal

import torch
from torch.utils.data import Dataset


def tokens_to_substrs(tokens, labels):
    substrs = {}
    current_tokens = []
    current_label = None
    for token, label in zip(tokens, labels):
        if label.startswith("B-"):
            if current_tokens:
                substr = " ".join(current_tokens)
                substrs[substr] = current_label
            current_tokens = [token]
            current_label = label[2:]
        elif label.startswith("I-") and current_label == label[2:]:
            current_tokens.append(token)
        else:
            if current_tokens:
                substr = " ".join(current_tokens)
                substrs[substr] = current_label
                current_tokens = []
                current_label = None

    if current_tokens:
        substr = " ".join(current_tokens)
        substrs[substr] = current_label

    return substrs


def _to_spans(substrs: dict, sentence: str):
    spans = []
    for sub, l in substrs.items():
        if not sub:
            continue
        match = re.search(re.escape(sub), sentence)
        if match:
            spans.append(
                {
                    "start": match.start(),
                    "end": match.end(),
                    "text": sub,
                    "entity": l,
                }
            )
    return spans


@dataclass
class LERSample:
    tokens: list[str]
    sentences: str
    ner_labels: list[str]
    coarse_ner_labels: list[str]
    split: str
    labels: list

    @classmethod
    def from_json(cls, json_dict: dict) -> "LERSample":
        substrs = tokens_to_substrs(json_dict["tokens"], json_dict["coarse_ner_labels"])
        return cls(
            tokens=json_dict["tokens"],
            sentences=json_dict["sentences"],
            ner_labels=json_dict["ner_labels"],
            coarse_ner_labels=json_dict["coarse_ner_labels"],
            split=json_dict["split"],
            labels=_to_spans(substrs, json_dict["sentences"]),
        )


@dataclass
class LERData:
    samples: list[LERSample]

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
