import argparse
import json
import logging
import zipfile
from pathlib import Path

from datasets import load_dataset


def annotations_tospans(annotations):
    spans = []
    if annotations is None:
        return spans
    for ann in annotations:
        spans.append(
            {
                "label": ann["label"],
                "text": ann["text"],
                "start": ann["pageRelativeStart"],
                "end": ann["pageRelativeEnd"],
            }
        )
    return spans


def load_data(input_dir):
    dataset = []
    with zipfile.ZipFile(input_dir, "r") as archive:
        txt_files = [f for f in archive.namelist() if f.endswith(".txt")]
        for txt_path in txt_files:
            dir_path = "/".join(txt_path.split("/")[:-1])
            ann_path = f"{dir_path}/annotations.json"

            with archive.open(txt_path) as f:
                content = f.read().decode("utf-8")
            annotations = None
            if ann_path in archive.namelist():
                with archive.open(ann_path) as f:
                    annotations = json.loads(f.read().decode("utf-8"))

            spans = annotations_tospans(annotations)
            dataset.append({"text": content, "labels": spans})

    return dataset


def main():
    parser = argparse.ArgumentParser(description="Load a dataset from M2N zip file ")
    parser.add_argument(
        "--input_path",
        type=str,
        help="Path where to load the zip file from",
    )

    parser.add_argument(
        "--output_path",
        type=str,
        help="Path where to save the JSON file",
    )

    args = parser.parse_args()
    dataset = load_data(args.input_path)
    text = dataset[1]["text"]
    for ann in dataset[1]["labels"]:
        start = ann["start"]
        end   = ann["end"]

        extracted = text[start:end]
        label_text = ann["text"]

        print(extracted, label_text)

if __name__ == "__main__":
    main()
