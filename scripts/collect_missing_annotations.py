import argparse
import json
from asyncio.log import logger
from collections import defaultdict
from pathlib import Path

from rulechef.core import Rule, RuleFormat
from rulechef.evaluation import evaluate_rules_individually

from benchmarks.util import make_dataset
from clear_anonymization.models.nerlearner import NERLearner
from clear_anonymization.ner_datasets import load_ner_dataset
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample


def collect_missing_annotation_samples(
    metrics_list, text_to_doc_id: dict
) -> list[NERSample]:
    doc_fps: dict[str, set] = defaultdict(set)
    doc_meta: dict[str, dict] = {}

    for metric in metrics_list:
        for sample in metric.sample_matches or []:
            text = sample.input["text"]
            doc_id = text_to_doc_id.get(text)
            key = (doc_id, text)
            if key not in doc_meta:
                doc_meta[key] = {
                    "text": text,
                    "doc_id": doc_id,
                    "gold_labels": sample.expected,
                }
            for e in sample.false_positives:
                doc_fps[key].add((e["start"], e["end"], e["text"], e.get("type", "")))

    samples = []
    for key, spans in doc_fps.items():
        meta = doc_meta[key]

        gold_labels = [{**label, "source": "gold"} for label in meta["gold_labels"]]

        gold_spans = {(l["start"], l["end"]) for l in meta["gold_labels"]}
        suggested_labels = [
            {
                "text": span_text,
                "start": start,
                "end": end,
                "type": label_type,
                "source": "suggested",
            }
            for start, end, span_text, label_type in sorted(spans)
            if (start, end) not in gold_spans
        ]

        if not suggested_labels:
            continue

        samples.append(
            NERSample(
                text=meta["text"],
                split="review",
                labels=gold_labels + suggested_labels,
                doc_id=meta["doc_id"],
            )
        )

    return samples


def main():
    parser = argparse.ArgumentParser(
        description="Collect likely missing annotations by running rules over the full dataset"
    )
    parser.add_argument(
        "--rules-json",
        type=str,
        required=True,
        help="Path to results JSON containing rules",
    )
    parser.add_argument(
        "--data-dir", type=str, required=True, help="Path to data (JSON format)"
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Output path for missing annotations JSON",
    )

    parser.add_argument("--dataset-name", type=str, default="findok")
    parser.add_argument("--base-url", type=str, default="http://localhost:8000/v1")
    args = parser.parse_args()

    # Load rules
    saved = json.loads(Path(args.rules_json).read_text())
    rules = [
        Rule(
            id=r["id"],
            name=r["name"],
            description=r["description"],
            format=RuleFormat(r["format"]),
            content=r["content"],
            output_template=r.get("output_template"),
            output_key=r.get("output_key"),
        )
        for r in saved["rules"]
    ]
    print(f"Loaded {len(rules)} rules")

    config = saved.get("config", {})

    learner = NERLearner(
        model=config.get("model"),
        dataset_name=config.get("dataset_name"),
        base_url=config.get("base_url"),
        use_grex=not config.get("no_grex"),
        max_rules=config.get("max_rules"),
        max_samples=config.get("max_samples"),
        max_counter_examples=config.get("max_counter_examples"),
        logger=logger,
        sampling_strategy=config.get("sampling_strategy"),
        synthesis_strategy=config.get("synthesis_strategy"),
        selected_classes=config.get("selected_classes", "organisation"),
    )

    data = load_ner_dataset(
        args.data_dir,
    )

    text_to_doc_id = {s.text: s.doc_id for s in data.samples}

    full_data = [
        {
            "text": s.text,
            "entities": s.labels,
            "sentences": [
                {"text": sent.text, "labels": sent.labels}
                for sent in (s.sentences or [])
            ],
        }
        for s in data.samples
    ]
    full_dataset = make_dataset(f"{args.dataset_name}_full", full_data, learner.task)

    rule_metrics = evaluate_rules_individually(
        rules=rules,
        dataset=full_dataset,
        apply_rules_fn=learner.learner._apply_rules,
        mode="text",
        max_samples=config.get("max_samples"),
        iou_threshold=0.5,
    )

    missing = collect_missing_annotation_samples(rule_metrics, text_to_doc_id)
    print(f"Found {len(missing)} documents with potential missing annotations")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(NERData(samples=missing).to_json(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
