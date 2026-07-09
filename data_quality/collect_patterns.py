"""Collect frequency-counted annotation patterns from the dataset, optionally filtered by entity type.

Usage
-----
python data_quality/collect_patterns.py \
    --input-dir /share/nverdha/data/bfg/final/findok_train.conllu \
    --output data_quality/findok/existing_annotations/organisation_annotations.json \
    --classes organisation
"""

import argparse
import json
from collections import Counter
from pathlib import Path

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll

parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", required=True)
parser.add_argument("--output", default=None)
parser.add_argument("--classes", nargs="+", help="Filter by classes")

args = parser.parse_args()

data = load_ner_dataset_from_conll(args.input_dir)
counts = Counter()
for doc in data.samples:
    for sent in doc.sentences:
        for label in sent.labels or []:
            etype = label.get("type", "")
            if args.classes and etype not in args.classes:
                continue
            text = label.get("text", "").strip()
            if text:
                counts[(text, etype)] += 1

print(f"{'Count':>6}  {'Type':<16}  Text")
print("-" * 60)
for (text, etype), n in counts.most_common():
    print(f"{n:>6}  {etype:<16}  {text}")
print("-" * 60)
print(
    f"{sum(counts.values()):>6}  total annotation(s) across {len(counts)} unique pattern(s)"
)

if args.output:
    patterns = [f"{text}:{etype}" for (text, etype), n in counts.most_common()]
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        existing = json.loads(output_path.read_text())
        new_patterns = [p for p in patterns if p not in existing]
        patterns = existing + new_patterns
        print(
            f"Appending {len(new_patterns)} new pattern(s) to {len(existing)} existing"
        )
    output_path.write_text(json.dumps(patterns, ensure_ascii=False, indent=2))
    print(f"Saved {len(patterns)} patterns to {args.output}")
