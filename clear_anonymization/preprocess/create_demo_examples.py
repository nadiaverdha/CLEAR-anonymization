import argparse
import json
import logging
import re
import string
import unicodedata
import zipfile
from pathlib import Path
import random

from clear_anonymization.ner_datasets.ner_dataset import NERData, NERDataset, NERSample


def sample_data(samples,split, window_size=200,allowed_classes = None):
    ner_data = NERData(samples=[])
    positive_samples = []
    for sample in samples:
        text = sample.text

        if allowed_classes:
            entities = sorted(
                [l for l in sample.labels if l["type"] in allowed_classes],
                key=lambda x: x["start"],
            )
            if not entities:
                continue

        else:
            entities = sample.labels
        merged_windows = []
        for ent in entities:
            start = max(0, ent["start"] - window_size)
            end = min(len(text), ent["end"] + window_size)
            if merged_windows and start <= merged_windows[-1][1]:
                merged_windows[-1][1] = max(end, merged_windows[-1][1])
                merged_windows[-1][2].append(ent)
            else:
                merged_windows.append([start, end, [ent]])

        for start, end, window_entities in merged_windows:
            snippet = text[start:end]
            adjusted_entities = []
            for e in window_entities:
                adjusted_entities.append(
                    {
                        "text": e["text"],
                        "start": e["start"] - start,
                        "end": e["end"] - start,
                        "type": e["type"],
                    }
                )

               
            sample = NERSample(snippet, split, adjusted_entities)
            positive_samples.append(sample)
    ner_data.samples= positive_samples[:30] 
    return ner_data
    

def main():
    parser = argparse.ArgumentParser(description="Load a dataset from M2N zip file ")
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path where to load the zip file from",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        help="Path where to save the JSON file",
    )
    parser.add_argument(
        "--split",
        type=str,
        help="Give information whether data is from train/validation/test split",
    )
    parser.add_argument(
        "--allowed_classes",
        type=lambda s: s.split(",") if s else None,
        required=False,
        help="Comma-separated list of entity classes to extract (e.g. person,email_address)",
    )
    

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    data = NERData.from_json(json.loads(input_dir.read_text())) 
    sampled = sample_data(data.samples,split = args.split, allowed_classes = args.allowed_classes, window_size=1000, )

    output_path = Path(args.output_dir)
    output_path.write_text(json.dumps(sampled.to_json(), indent=4))


if __name__ == "__main__":
    main()
