import argparse
import json
import logging
import re
import unicodedata
import zipfile
from pathlib import Path

from datasets import load_dataset


def check_mismatch(idx, dataset):
    l = []

    print(f"==== Document {idx} ====")
    # if idx == 7:
    sample = dataset[idx]
    text = sample["text"]
    labels = sample["labels"]

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


def validate_annotations_per_page(pages, annotations):
    """
    For each page, check if all annotations that belong to it
    match the text exactly at their specified page-relative offsets.
    """

    for page_idx, page_text in enumerate(pages):
        print(f"\n=== VALIDATING PAGE {page_idx} ===")

        print(page_text)

        for ann in annotations:
            sp = ann["startPage"]
            ep = ann["endPage"]
            rs = ann["pageRelativeStart"]
            re = ann["pageRelativeEnd"]
            expected = ann["text"]

            actual = page_text[rs:re]
            print("ACTUAAAAL", actual)
            print("EXPECTEDDD", expected)
            if actual == expected:
                print(f"✓ '{expected}' matches exactly at [{rs}:{re}]")
            else:
                print(f"❌ MISMATCH '{expected}' at [{rs}:{re}]")
                found_pos = page_text.find(expected)
                if found_pos != -1:
                    print(
                        f" → Text found at position {found_pos} (offset diff: {found_pos - rs})"
                    )
                else:
                    print(" → Text not found on this page")

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
            print(folder)
            txt_files_sorted = sorted(txt_files, key=lambda p: int(Path(p).stem))

            if folder == "export_20251127_1826/9e8040b797939101bef412cbafeeb8f2":
                pages = []
                for txt_path in txt_files_sorted:
                    with archive.open(txt_path) as f:
                        pages.append(f.read().decode("utf-8"))

                full_text = "".join(pages)

                page_offsets = []
                current_offset = 0
                for i, p in enumerate(pages):
                    page_offsets.append(current_offset)
                    print(f"Page {i} offset: {current_offset}")
                    current_offset += len(p)

                # annotations file
                ann_path = f"{folder}/annotations.json"
                annotations = None
                if ann_path in archive.namelist():
                    with archive.open(ann_path) as f:
                        annotations = json.loads(f.read().decode("utf-8"))

                annotations = sorted(annotations, key=lambda x: (x["startPage"]))
                spans = []
                validate_annotations_per_page(pages, annotations)
                if annotations:
                    for ann in annotations:
                        startpage = ann["startPage"]
                        endpage = ann["endPage"]

                        start = page_offsets[startpage] + ann["pageRelativeStart"]
                        end = page_offsets[endpage] + ann["pageRelativeEnd"]

                        spans.append(
                            {
                                "text": ann["text"],
                                "start": start,
                                "end": end,
                                "class": ann["label"],
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
    set_ = set()
    labels = []


if __name__ == "__main__":
    main()
