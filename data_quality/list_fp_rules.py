"""Filter an evaluated rules JSON (from evaluate_rules.py) down to the rules
that produced false positives, sorted by FP count, for manual review.

Usage
-----
python data_quality/list_fp_rules.py \
    --rules-json data_quality/findok/rules/organisation_train_rules_evaluated.json \
    --output data_quality/findok/rules/organisation_train_rules_fp_review.json
"""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="List/export rules with false positives from an evaluated rules JSON, sorted by FP count."
    )
    parser.add_argument(
        "--rules-json", required=True, help="Path to evaluated rules JSON"
    )
    parser.add_argument(
        "--output", required=True, help="Output path for the filtered rules JSON"
    )
    args = parser.parse_args()

    src_path = Path(args.rules_json)
    rules = json.loads(src_path.read_text())["rules"]

    fp_rules = [r for r in rules if r.get("fp", 0) >= 1]
    fp_rules.sort(key=lambda r: -r["fp"])

    out = [
        {
            "id": r["id"],
            "name": r["name"],
            "description": r.get("description", ""),
            "content": r.get("content", ""),
            "precision": r.get("precision"),
            "tp": r.get("tp"),
            "fp": r.get("fp"),
            "total_predictions": r.get("total_predictions"),
            "examples_fp": r.get("examples_fp", []),
        }
        for r in fp_rules
    ]

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{len(rules)} total rules")
    print(f"{len(fp_rules)} rules have fp >= 1")
    print(f"written to {out_path}")
    print()
    for r in fp_rules:
        print(
            f"  fp={r['fp']:>6}  tp={r['tp']:>4}  prec={r.get('precision', 0):.2f}  {r['name']}"
        )


if __name__ == "__main__":
    main()
