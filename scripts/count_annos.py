import argparse
import json
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input", required=True, help="Path to conllu file or data folder or zip"
)
parser.add_argument("--classes", nargs="+", help="Filter by classes")
args = parser.parse_args()

input = Path(args.input)


def count_from_conllu(input: Path) -> Counter:
    data = load_ner_dataset_from_conll(input)
    counts = Counter()
    for doc in data.samples:
        for sent in doc.sentences:
            for label in sent.labels or []:
                etype = label.get("type", "")
                if args.classes and etype not in args.classes:
                    continue
                counts[etype] += 1
    return counts


def count_from_dir(input: Path) -> Counter:
    counts = Counter()
    for sub_f in input.glob("*"):
        annos = json.loads((sub_f / "annotations.json").read_text(encoding="utf-8"))
        for anno in annos:
            etype = anno.get("label", "")
            if args.classes and etype not in args.classes:
                continue
            counts[etype] += 1
    return counts


def count_from_zip(input: Path) -> Counter:
    counts = Counter()
    with ZipFile(input, "r") as zip:
        for file_info in zip.infolist():
            if not file_info.is_dir() and file_info.filename.endswith(".json"):
                with zip.open(file_info) as json_file:
                    annos = json.load(json_file)
                    for anno in annos:
                        etype = anno.get("label", "")
                        if args.classes and etype not in args.classes:
                            continue
                        counts[etype] += 1
    return counts


if input.name.endswith(".conllu"):
    counts = count_from_conllu(input)
elif input.name.endswith(".zip"):
    counts = count_from_zip(input)
elif input.is_dir():
    counts = count_from_dir(input)
else:
    raise Exception(f"Unsupported file type: {input.name}")

print(f"==== {input.name} ====")
for etype, n in counts.most_common():
    print(f"{etype}: {n}")
