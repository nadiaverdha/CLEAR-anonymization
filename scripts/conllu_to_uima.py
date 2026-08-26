import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from clear_anonymization.ner_datasets import NERSentence, load_ner_dataset_from_conll


@dataclass
class Entity:
    start: int
    end: int
    text: str
    conceptId: str
    label: str


def parse_int(feat: str, key: str) -> int:
    return int(re.compile(key + r"=\d+").findall(feat)[0].removeprefix(key + "="))


def to_start(tokens: List[Dict], label: Dict) -> int:
    for tok in tokens:
        if label["start"] == parse_int(tok["misc"], "SentStart"):
            return parse_int(tok["misc"], "SentStart")
    raise Exception("No suitable DocStart found!")


def to_end(tokens: List[Dict], label: Dict) -> int:
    for tok in tokens:
        if label["end"] == parse_int(tok["misc"], "SentEnd"):
            return parse_int(tok["misc"], "SentEnd")
    raise Exception("No suitable DocStart found!")


def collect_labels(sents: List[NERSentence]) -> Tuple[List[Entity], str]:
    entities = []
    strings = []
    doc_len = 0
    for idx, sent in enumerate(sents):
        strings.append(sent.text)
        for label in sent.labels:
            doc_start = doc_len + to_start(sent.tokens, label)
            doc_end = doc_len + to_end(sent.tokens, label)
            entities.append(
                Entity(
                    doc_start,
                    doc_end,
                    label["text"],
                    label["text"],
                    label["type"],
                )
            )
        doc_len += len(sent.text + " ")
    return entities, " ".join(strings)


def to_uima_dict(text: str, entities: List[Entity]) -> Dict:
    main_dict = dict()
    main_dict["%TYPES"] = {
        "clear.NamedEntity": {
            "%NAME": "clear.NamedEntity",
            "%SUPER_TYPE": "uima.tcas.Annotation",
            "label": {"%NAME": "label", "%RANGE": "uima.cas.String"},
            "text": {"%NAME": "text", "%RANGE": "uima.cas.String"},
            "conceptId": {"%NAME": "conceptId", "%RANGE": "uima.cas.String"},
        },
        "clear.Relation": {
            "%NAME": "clear.Relation",
            "%SUPER_TYPE": "uima.tcas.Annotation",
            "relLabel": {"%NAME": "relLabel", "%RANGE": "uima.cas.String"},
            "Governor": {"%NAME": "Governor", "%RANGE": "clear.NamedEntity"},
            "Dependent": {"%NAME": "Dependent", "%RANGE": "clear.NamedEntity"},
        },
    }
    features_sturcts = []
    main_dict["%FEATURE_STRUCTURES"] = features_sturcts
    features_sturcts.append(
        {
            "%ID": 1,
            "%TYPE": "uima.cas.Sofa",
            "sofaNum": 1,
            "sofaID": "_InitialView",
            "mimeType": "text/plain",
            "sofaString": text,
        }
    )
    features_sturcts.append(
        {
            "%ID": 2,
            "%TYPE": "uima.tcas.DocumentAnnotation",
            "language": "de",
            "@sofa": 1,
        }
    )
    for idx, entity in enumerate(entities):
        features_sturcts.append(
            {
                "%ID": idx + 3,
                "%TYPE": "clear.NamedEntity",
                "begin": entity.start,
                "end": entity.end,
                "label": entity.label,
                "text": entity.text,
                "conceptId": entity.conceptId,
                "@sofa": 1,
            }
        )
    main_dict["%VIEWS"] = {
        "_InitialView": {
            "%SOFA": 1,
            "%MEMBERS": list(range(3, len(entities) + 3)),
        }
    }
    return main_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_conll", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)

    args = parser.parse_args()
    print("Loading NER dataset...")
    conllu_data = load_ner_dataset_from_conll(Path(args.input_conll))
    print("Loading finished")
    output_path = Path(args.output)
    for idx, sample in enumerate(conllu_data.samples):
        output_file = output_path / (sample.doc_id + ".json")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        labels, text = collect_labels(sample.sentences)
        uima_dict = to_uima_dict(text, labels)
        output_file.write_text(
            json.dumps(uima_dict, indent=2, ensure_ascii=False), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
