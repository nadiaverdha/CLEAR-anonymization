import argparse
import json
import logging
import re
import string
import unicodedata
import zipfile
from pathlib import Path

from datasets import load_dataset

from clear_anonymization.ner_datasets.ner_dataset import NERData, NERDataset, NERSample


def preprocess_text(text):
    text = text.replace("\xa0", " ")
    return text


def list_folders(zip_path):
    with zipfile.ZipFile(zip_path, "r") as archive:
        folders = set()
        for file_name in archive.namelist():
            if "/" in file_name:
                folder = "/".join(file_name.split("/")[:-1])
                folders.add(folder)
        return sorted(folders)


def validate_docu_annotations(folder, sample, verbose=False):
    text = sample.text
    labels = sample.labels
    all_ok = True
    for ann in labels:
        start = ann["start"]
        end = ann["end"]
        actual = text[start:end]
        expected = ann["text"]
        if actual != expected:
            all_ok = False

        if verbose:
            print(f"{start}:{end}  '{actual}'  ---->  '{expected}'")
            if actual != expected:
                print("❌ incorrect")
            else:
                print("✅ correct ")

    if not verbose:
        if all_ok:
            print("✅ Annotation check ok! ")
        else:
            print("❌ Annotation check failed!")


def process_folder(zip_path, folder_name, verbose):
    pages = []
    annotations = None
    with zipfile.ZipFile(zip_path, "r") as archive:
        folder_files = [f for f in archive.namelist() if folder_name in f]
        txt_files = sorted(
            [f for f in folder_files if f.endswith(".txt")],
            key=lambda p: int(Path(p).stem),
        )

        for txt_file in txt_files:
            with archive.open(txt_file) as f:
                content = f.read().decode("utf-8-sig")

                pages.append(preprocess_text(content))

        ann_file = [f for f in folder_files if f.endswith(".json")][0]
        if ann_file:
            with archive.open(ann_file) as f:
                annotations = json.loads(f.read().decode("utf-8"))
    annotations = sorted(annotations, key=lambda x: (x["startPage"]))
    sample = create_sample(pages, annotations)
    validate_docu_annotations(folder_name, sample, verbose)
    return sample


def create_sample(pages, annotations):
    full_text = "".join(pages)
    page_offsets = []

    current_offset = 0
    for i, p in enumerate(pages):
        page_offsets.append(current_offset)
        current_offset += len(p)

    labels = []
    if annotations:
        for ann in annotations:
            startpage = ann["startPage"]
            endpage = ann["endPage"]

            start = page_offsets[startpage] + ann["pageRelativeStart"]
            end = page_offsets[endpage] + ann["pageRelativeEnd"]
            actual = full_text[start:end]

            if startpage > 0:
                start += 1
                end += 1

            labels.append(
                {
                    "text": ann["text"],
                    "start": start,
                    "end": end,
                    "class": ann["label"],
                }
            )
    return NERSample(full_text, "validation", labels)


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
        "--verbose",
        action="store_true",
        help="Whether to show detailed annotations check.",
    )

    args = parser.parse_args()

    ner_data = NERData(samples=[])
    folders = list_folders(args.input_dir)
    for folder in folders:
        print(f"==== Document {folder} ====")
        sample = process_folder(args.input_dir, folder, args.verbose)
        ner_data.samples.append(sample)
        print("-----------------")
    output_path = Path(args.output_dir)
    output_path.write_text(json.dumps(ner_data.to_json(), indent=4))


if __name__ == "__main__":
    main()
