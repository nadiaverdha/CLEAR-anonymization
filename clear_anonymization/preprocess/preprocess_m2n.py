import argparse
import json
import logging
import re
import unicodedata
import zipfile
from pathlib import Path

from datasets import load_dataset


def preprocess_text(raw):
    t = unicodedata.normalize("NFC", raw)

    t = t.strip()
    return t


def check_mismatch(idx, dataset):
    print(f"==== Document {idx} ====")
    # if idx == 7:
    sample = dataset[idx]
    text = sample["text"]
    labels = sample["labels"]
    print(text)

    for ann in labels:
        start = ann["start"]
        end = ann["end"]

        extracted = text[start:end]
        label_text = ann["text"]

        print(f"{start}:{end}   '{extracted}'  ---->  '{label_text}'")

        # optional mismatch check
        if extracted != label_text:
            print("⚠️ OFFSET MISMATCH!")
    print("--------------------------------\n")


def load_data(input_dir):
    dataset = []

    with zipfile.ZipFile(input_dir, "r") as archive:
        folders = {}
        # grouping files by folder
        for name in archive.namelist():
            if name.endswith(".txt"):
                folder = "/".join(name.split("/")[:-1])
                folders.setdefault(folder, []).append(name)

        for folder, txt_files in folders.items():
            txt_files_sorted = sorted(txt_files, key=lambda p: int(Path(p).stem))
            print(folder)
            # concatination of pages
            pages = []
            for txt_path in txt_files_sorted:
                with archive.open(txt_path) as f:
                    raw = f.read().decode("utf-8")
                    # content = preprocess_text(raw)
                    pages.append(raw)

            full_text = "".join(pages)
            page_offsets = []
            current_offset = 0
            for i, p in enumerate(pages):
                page_offsets.append(current_offset)
                current_offset += len(p)
                if i < len(pages) - 1:
                    current_offset += 0

            # annotations file
            ann_path = f"{folder}/annotations.json"
            annotations = None
            if ann_path in archive.namelist():
                with archive.open(ann_path) as f:
                    annotations = json.loads(f.read().decode("utf-8"))

            spans = []
            if annotations:
                for ann in annotations:
                    startpage = ann["startPage"]
                    endpage = ann["endPage"]

                    start = page_offsets[startpage] + ann["pageRelativeStart"]
                    end = page_offsets[endpage] + ann["pageRelativeEnd"]

                    spans.append(
                        {
                            "label": ann["label"],
                            "text": ann["text"],
                            "start": start,
                            "end": end,
                        }
                    )

            dataset.append({"text": full_text, "labels": spans})

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

    check_mismatch(5, dataset)


if __name__ == "__main__":
    main()
