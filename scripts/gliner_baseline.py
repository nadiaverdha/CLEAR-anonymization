import argparse
import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from gliner import GLiNER

from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample


def to_spans(predicted, text):
    spans = []
    for entity in predicted:
        spans.append(
            {
                "start": entity["start"],
                "end": entity["end"],
                "text": entity["text"],
                "class": entity["label"],
            }
        )
    return spans


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a named entity recognition model based on LLM"
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path to the evaluation data (JSON format)",
    )
    parser.add_argument("--model", type=str, required=True, help="GliNER model ")
    parser.add_argument("--output_file", type=str, default=None)

    args = parser.parse_args()

    definitions = ["PERS", "LOC", "ORG", "NRM", "RS", "LIT", "REG"]

    data = NERData.from_json(json.loads(Path(args.input_dir).read_text()))
    samples = [s for s in data.samples if s.split == "validation"]
    texts = [s.sentences for s in samples]
    extractor = GLiNER.from_pretrained(args.model, max_length=1024).to("cuda")
    results = extractor.inference(
        texts,
        definitions,
    )
    print("Arrived here")
    formatted_results = []
    with ThreadPoolExecutor() as ex:
        formatted_results = list(
            ex.map(
                lambda pair: {
                    "sentences": pair[0],
                    "labels": to_spans(pair[1], pair[0]),
                },
                zip(texts, results),
            )
        )
    if not args.output_file:
        output_file = Path("results_gliner_.json")
    else:
        output_file = Path(args.output_file)

    output_file.write_text(json.dumps(formatted_results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
