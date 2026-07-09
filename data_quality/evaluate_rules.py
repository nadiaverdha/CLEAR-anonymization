"""Evaluate all rules on a labeled sample and save full metrics (precision, tp/fp, examples) as JSON.

  Usage
  -----
  python data_quality/evaluate_rules.py \
      --rules-json data_quality/findok/rules/organisation_rules.json \
      --data-dir /share/nverdha/data/bfg/final/findok_train_corrected.conllu \
      --output data_quality/findok/rules/organisation_rules_evaluated.json \
      --sample-size 50000 \
      --workers 2
"""

import argparse
import json
import random
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass, field
from pathlib import Path

from rulechef.executor import RuleExecutor

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from data_quality.worker import init_worker, process_sentence


@dataclass
class RuleStats:
    tp: int = 0
    fp: int = 0
    examples_tp: list = field(default_factory=list)
    examples_fp: list = field(default_factory=list)

    @property
    def total_predictions(self) -> int:
        return self.tp + self.fp

    @property
    def precision(self) -> float:
        if self.total_predictions == 0:
            return 0.0
        return self.tp / self.total_predictions


def _score_rules(
    rules_data: list[dict],
    sentences: list[dict],
    workers: int,
    rule_records: dict[str, RuleStats] | None = None,
    start: int = 0,
    checkpoint_path: Path | None = None,
    checkpoint_every: int = 2000,
) -> dict[str, RuleStats]:

    if rule_records is None:
        rule_records = {r["id"]: RuleStats() for r in rules_data}

    with ProcessPoolExecutor(
        max_workers=workers,
        initializer=init_worker,
        initargs=(rules_data,),
    ) as pool:
        for i, records in enumerate(
            pool.map(process_sentence, sentences, chunksize=100)
        ):
            processed = start + i + 1

            for rec in records:
                rid = rec["rule_id"]
                if rid not in rule_records:
                    continue

                entry = rule_records[rid]

                if rec["outcome"] == "tp":
                    entry.tp += 1
                    entry.examples_tp.append(
                        {
                            "text": rec["text"],
                            "predicted": rec["predicted"],
                            "reason": rec["reason"],
                            "gold_entities": rec["gold_entities"],
                        }
                    )
                else:
                    entry.fp += 1
                    entry.examples_fp.append(
                        {
                            "text": rec["text"],
                            "predicted": rec["predicted"],
                            "reason": rec["reason"],
                            "gold_entities": rec["gold_entities"],
                        }
                    )

            if processed % checkpoint_every == 0:
                print(f"processed {processed} sentences")

                if checkpoint_path is not None:
                    save_checkpoint(
                        checkpoint_path,
                        rule_records,
                        processed,
                    )

    if checkpoint_path is not None:
        save_checkpoint(
            checkpoint_path,
            rule_records,
            start + len(sentences),
        )

    return rule_records


def save_checkpoint(path: Path, rule_records, processed):
    payload = {
        "processed": processed,
        "rules": {rid: asdict(stats) for rid, stats in rule_records.items()},
    }
    path.write_text(json.dumps(payload, ensure_ascii=False))


def load_checkpoint(path: Path):
    payload = json.loads(path.read_text())

    records = {}
    for rid, d in payload["rules"].items():
        records[rid] = RuleStats(
            tp=d["tp"],
            fp=d["fp"],
            examples_tp=d["examples_tp"],
            examples_fp=d["examples_fp"],
        )

    return records, payload["processed"]


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate all rules on a labeled sample and save full metrics as JSON."
    )
    parser.add_argument("--rules-json", type=Path, required=True)
    parser.add_argument("--data-dir", type=str, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--sample-size",
        type=int,
        default=50000,
        help="Sentences to sample (default: 50000). 0 = all.",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=2000,
        help="Save progress every N sentences.",
    )
    args = parser.parse_args()

    saved = json.loads(args.rules_json.read_text())
    rules_data = saved["rules"]
    print(f"Loaded {len(rules_data)} rules")

    raw = load_ner_dataset_from_conll(args.data_dir)
    all_sentences = [
        {
            "text": sent.text,
            "entities": sent.labels or [],
            "sent_id": sent.sent_id,
            "doc_id": doc.doc_id,
        }
        for doc in raw.samples
        for sent in doc.sentences
        if sent.text and sent.text.strip()
    ]
    print(f"Loaded {len(all_sentences)} sentences")

    if args.sample_size and args.sample_size < len(all_sentences):
        rng = random.Random(args.seed)
        sentences = rng.sample(all_sentences, args.sample_size)
        print(f"Sampled {args.sample_size} sentences (seed={args.seed})")
    else:
        sentences = all_sentences

    checkpoint_path = args.output.with_suffix(".checkpoint.json")

    if args.resume and checkpoint_path.exists():
        rule_records, start = load_checkpoint(checkpoint_path)
        remaining = sentences[start:]
        print(f"Resuming from sentence {start}")
    else:
        rule_records = None
        start = 0
        remaining = sentences

    rule_records = _score_rules(
        rules_data,
        remaining,
        args.workers,
        rule_records=rule_records,
        start=start,
        checkpoint_path=checkpoint_path,
        checkpoint_every=args.checkpoint_every,
    )
    # Build evaluated rule list
    evaluated = []
    for r in rules_data:
        rid = r["id"]
        entry = rule_records[rid]
        evaluated.append(
            {
                **r,
                "precision": round(entry.precision, 4),
                "tp": entry.tp,
                "fp": entry.fp,
                "total_predictions": entry.total_predictions,
                "examples_tp": entry.examples_tp,
                "examples_fp": entry.examples_fp,
            }
        )

    fired = [r for r in evaluated if r["total_predictions"] > 0]
    high_precision = [r for r in fired if r["precision"] >= 0.7]
    print(f"\nTotal rules:                  {len(evaluated)}")
    print(f"Rules that fired:             {len(fired)}")
    print(f"High precision (≥70%, ≥1 TP): {len(high_precision)}")

    print("\nTop 10 by precision (with FPs):")
    print(f"  {'Prec':>6}  {'TP':>4}  {'FP':>4}  Name  ID")
    for r in sorted([x for x in fired if x["fp"] > 0], key=lambda x: -x["precision"])[
        :10
    ]:
        print(
            f"  {r['precision']:>6.1%}  {r['tp']:>4}  {r['fp']:>4}  {r['name']}  {r['id']}"
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(
            {"rules": evaluated, "config": saved.get("config", {})},
            indent=2,
            ensure_ascii=False,
        )
    )
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
