from dataclasses import dataclass, field

import conllu
from stanza.models.common.doc import Document
from stanza.utils.conll import CoNLL
from torch.utils.data import Dataset


@dataclass
class NERSentence:
    sent_id: str
    text: str
    tokens: list
    labels: list = None

    @classmethod
    def from_json(cls, json_dict: dict) -> "NERSentence":
        return cls(
            sent_id=json_dict.get("sent_id"),
            text=json_dict.get("text"),
            labels=json_dict.get("labels", []),
            tokens=json_dict.get("tokens"),
        )

    def to_json(self) -> dict:
        d = {
            "sent_id": self.sent_id,
            "text": self.text,
            "labels": self.labels,
        }
        if self.tokens is not None:
            d["tokens"] = self.tokens
        return d

    @classmethod
    def from_conll(cls, lines: list[str]) -> "NERSentence":
        sent_id = None
        text = None
        tokens = []
        for line in lines:
            if line.startswith("# sent_id = "):
                sent_id = line.removeprefix("# sent_id = ")
            elif line.startswith("# text = "):
                text = line.removeprefix("# text = ")
            elif line and not line.startswith("#"):
                parts = line.split("\t")
                tokens.append(
                    {
                        "text": parts[0],
                        "lemma": parts[1],
                        "upos": parts[2],
                        "xpos": parts[3],
                        "tag": parts[4],
                    }
                )
        return cls(sent_id=sent_id, text=text, tokens=tokens)

    def to_conll(self) -> str:
        doc = Document([self.tokens])
        doc.sentences[0]._comments = [
            f"# sent_id = {self.sent_id}",
            f"# text = {self.text}",
        ]
        sent_lines = CoNLL.doc2conll(doc)[0]
        return "\n".join(sent_lines) + "\n"


@dataclass
class NERSample:
    doc_id: str
    split: str
    text: str
    labels: list
    sentences: list[NERSentence] = field(default_factory=list)

    @classmethod
    def from_json(cls, json_dict: dict) -> "NERSample":
        return cls(
            doc_id=json_dict.get("doc_id"),
            split=json_dict.get("split", "unknown"),
            text=json_dict.get("text", ""),
            labels=json_dict.get("labels", []),
            sentences=[
                NERSentence.from_json(s) for s in json_dict.get("sentences", [])
            ],
        )

    def to_json(self) -> dict:
        return {
            "doc_id": self.doc_id,
            "split": self.split,
            "text": self.text,
            "labels": self.labels,
            "sentences": [s.to_json() for s in self.sentences],
        }

    @classmethod
    def from_conll(cls, lines: list[str]) -> "NERSample":
        doc_id = None
        split = "unknown"
        sentences = []
        current_sent_lines = []
        for line in lines:
            if line.startswith("# doc_id = "):
                doc_id = line.removeprefix("# doc_id = ")
            elif line.startswith("# split = "):
                split = line.removeprefix("# split = ")
            elif line == "":
                if current_sent_lines:
                    sentences.append(NERSentence.from_conll(current_sent_lines))
                    current_sent_lines = []
            else:
                current_sent_lines.append(line)
        if current_sent_lines:
            sentences.append(NERSentence.from_conll(current_sent_lines))
        return cls(doc_id=doc_id, split=split, text="", labels=[], sentences=sentences)

    def to_conll(self) -> str:
        doc = Document([s.tokens for s in self.sentences])
        for i, (sent, ner_sent) in enumerate(zip(doc.sentences, self.sentences)):
            comments = []
            if i == 0:
                comments += [f"# doc_id = {self.doc_id}", f"# split = {self.split}"]
            comments += [f"# sent_id = {ner_sent.sent_id}", f"# text = {ner_sent.text}"]
            sent._comments = comments
        lines = []
        for sent_lines in CoNLL.doc2conll(doc):
            lines.append("\n".join(sent_lines))
            lines.append("")
        return "\n".join(lines)


@dataclass
class NERData:
    samples: list[NERSample]

    @classmethod
    def from_json(cls, json_dict: list[dict]) -> "NERData":
        return cls(
            samples=[NERSample.from_json(sample) for sample in json_dict],
        )

    def to_json(self) -> list[dict]:
        return [sample.to_json() for sample in self.samples]

    @classmethod
    def from_conll(cls, text: str) -> "NERData":
        blocks = []
        current_block = []
        for line in text.splitlines():
            if line.startswith("# doc_id = ") and current_block:
                blocks.append(current_block)
                current_block = [line]
            else:
                current_block.append(line)
        if current_block:
            blocks.append(current_block)
        return cls(samples=[NERSample.from_conll(block) for block in blocks])

    def to_conll(self) -> str:
        return "\n".join(sample.to_conll() for sample in self.samples)


class NERDataset(Dataset):
    def __init__(self, samples: list[NERSample]):
        self.samples = samples

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int):
        return self.samples[idx]
