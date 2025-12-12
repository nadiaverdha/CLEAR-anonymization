import argparse
import json
import logging
import re
import unicodedata
import zipfile
from pathlib import Path
import string

from datasets import load_dataset


def check_mismatch(idx, dataset):
    print(f"==== Document {idx} ====")
    sample = dataset[idx]
    text = sample["text"]
    labels = sample["labels"]

    for ann in labels:
        start = ann["start"]
        end = ann["end"]

        actual = text[start:end]
        expected = ann["text"]

        print(f"{start}:{end}   '{actual}'  ---->  '{expected}'")
        if actual != expected:
            print("❌ Mismatch in offsets")
            # print(text)
            # inspect_string(actual)
            # print("-----------")
            # inspect_string(expected)
        else:
            print("✓ Correct ")
    print("--------------------------------\n")


def inspect_string(s, start=0, end=None):
    if end is None:
        end = len(s)
    for i, c in enumerate(s[start:end], start=start):
        print(f"{i}: {repr(c)} | ord: {ord(c)}")


def validate_annotations_per_page(pages, annotations):
    for page_idx, page_text in enumerate(pages):
        print(f"\n=== VALIDATING PAGE {page_idx} ===")

        for ann in annotations:
            sp = ann["startPage"]
            ep = ann["endPage"]

            rs = ann["pageRelativeStart"]
            re = ann["pageRelativeEnd"]

            if sp != page_idx:
                continue
            actual = page_text[rs:re]
            expected = ann["text"]
            print("ACTUAAAAL", repr(actual))
            print("EXPECTEDDD", repr(expected))
            if actual == expected:
                print(f"✓ '{expected}' matches exactly at [{rs}:{re}]")
            else:
                print(f"❌ Mismatch '{expected}' at [{rs}:{re}]")
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

        # sorting the files inside a folder
        for folder, txt_files in folders.items():
            txt_files_sorted = sorted(txt_files, key=lambda p: int(Path(p).stem))
            print(folder)

            # opening each of the file
            pages = []
            for txt_path in txt_files_sorted:
                with archive.open(txt_path) as f:
                    content = f.read().decode("utf-8-sig")
                    content = content.replace("\r\n", "\n").replace("\r", "\n")
                    content = content.replace("\xa0", " ")
                    pages.append(content)

            # removing the extra character introduced in all pages except for page 0
            #  for i in range(1, len(pages)):
            #     pages[i] = pages[i][1:]

            full_text = "".join(pages)
            page_offsets = []

            # calculating the offset of each page depending on the previous page length
            current_offset = 0
            for i, p in enumerate(pages):
                page_offsets.append(current_offset)
                print(f" Folder {folder} Page {i} offset: {current_offset}")
                current_offset += len(p)

            # the annotations file
            ann_path = f"{folder}/annotations.json"
            annotations = None
            if ann_path in archive.namelist():
                with archive.open(ann_path) as f:
                    annotations = json.loads(f.read().decode("utf-8"))

            annotations = sorted(annotations, key=lambda x: (x["startPage"]))
            labels = []

            # function for validating whether the annotations per page are correct

            # validate_annotations_per_page(pages, annotations)
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

            dataset.append({"text": full_text, "labels": labels})

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
    for i, data in enumerate(dataset):
        check_mismatch(i, dataset)


if __name__ == "__main__":
    main()
