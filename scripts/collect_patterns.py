import argparse
import json
from collections import Counter
from pathlib import Path

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll

parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", required=True)
parser.add_argument("--min-count", type=int, default=0)
parser.add_argument("--output", default=None)
parser.add_argument("--entity-type", default=None, help="Filter by type, e.g. ORG")

args = parser.parse_args()

data = load_ner_dataset_from_conll(args.input_dir)
counts = Counter()
for doc in data.samples:
    for sent in doc.sentences:
        for label in sent.labels or []:
            etype = label.get("type", "")
            if args.entity_type and etype != args.entity_type:
                continue
            text = label.get("text", "").strip()
            if text:
                counts[(text, etype)] += 1

print(f"{'Count':>6}  {'Type':<16}  Text")
print("-" * 60)
for (text, etype), n in counts.most_common():
    if n >= args.min_count:
        print(f"{n:>6}  {etype:<16}  {text}")

if args.output:
    patterns = [
        f"{text}:{etype}"
        for (text, etype), n in counts.most_common()
        if n >= args.min_count
    ]
    Path(args.output).write_text(json.dumps(patterns, ensure_ascii=False, indent=2))
    print(f"Saved {len(patterns)} patterns to {args.output}")
