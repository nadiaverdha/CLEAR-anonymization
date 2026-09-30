import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from rulechef.core import Correction, Dataset, Example, Feedback, Rule, RuleFormat
from rulechef.training_logger import TrainingDataLogger

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.ner_datasets.util import build_relation_examples
from clear_anonymization.preprocess.create_train_dev_split import (
    label_distribution_sent,
    print_distribution,
)
from clear_anonymization.preprocess.sampling import (
    sample_few_shot,
    sample_relation_stratified,
)


def make_dataset(dataset_name, data, task):
    dataset = Dataset(name=dataset_name, task=task)
    for ex in data:
        dataset.examples.append(
            Example(
                id=str(uuid.uuid4())[:8],
                input={
                    "doc_id": ex.get("doc_id", ""),
                    "sent_id": ex.get("sent_id", ""),
                    "text": ex["text"],
                    "sentences": ex.get("sentences", []),
                },
                expected_output={"entities": ex["entities"]},
                source=dataset_name,
            )
        )
    return dataset


def make_relation_dataset(dataset_name, examples, task):
    dataset = Dataset(name=dataset_name, task=task)
    for ex in examples:
        dataset.examples.append(
            Example(
                id=str(uuid.uuid4())[:8],
                input={
                    "text": ex["text"],
                    "display_text": ex["display_text"],
                    "doc_id": ex["doc_id"],
                    "gov_sent_id": ex["gov_sent_id"],
                    "dep_sent_id": ex["dep_sent_id"],
                },
                expected_output={"label": ex["label"]},
                source=dataset_name,
            )
        )
    return dataset


def _n_annotations(examples):
    return sum(len(s["entities"]) if "entities" in s else 1 for s in examples)


def conll_to_sentences(dataset) -> list[dict]:
    return [
        {
            "doc_id": s.doc_id,
            "sent_id": sent.sent_id,
            "text": sent.text,
            "entities": list(sent.labels),
        }
        for s in dataset.samples
        for sent in s.sentences
    ]


@dataclass
class DataSplit:
    """Sampled, train/eval/dev-split data ready for a learning phase."""

    name: str
    train: list
    eval: list
    dev: list
    test: list
    counter_examples: list
    selected_classes: set
    n_train_docs: int
    n_eval_docs: int
    n_dev_docs: int
    n_test_docs: int


@dataclass
class BenchmarkRun:
    args: Any
    train_data: list
    eval_data: list
    test_data: list
    train_size: int
    eval_size: int
    dev_size: int
    test_size: int
    train_sentences: int
    eval_sentences: int
    dev_sentences: int
    test_sentences: int
    iteration_metrics: list
    batch_test_metrics: list
    eval_results: Any
    test_eval_results: Any
    t_learn: float
    t_eval: float
    rules: list
    selected_classes: set[str] | list[str]
    metadata: dict = field(default_factory=dict)


def prepare_split(
    args,
    *,
    name: str,
    train_dir: str,
    dev_dir: str | None = None,
    test_dir: str | None = None,
    classes: str | None = None,
    fallback_dev: list | None = None,
    fallback_test: list | None = None,
) -> DataSplit:
    """Load and sample one dataset into a DataSplit ready for training."""
    print(f"\nLoading {name} dataset...")

    train_all = load_ner_dataset_from_conll(train_dir)

    dev_all = load_ner_dataset_from_conll(dev_dir) if dev_dir else None

    test_all = load_ner_dataset_from_conll(test_dir) if test_dir else None

    class_list = [c.strip() for c in classes.split(",")] if classes else None

    (
        train,
        eval_,
        counter_examples,
        selected_classes,
        n_train_docs,
        n_eval_docs,
    ) = sample_few_shot(
        train_data=train_all.samples,
        seed=args.seed,
        num_classes=args.num_classes,
        classes=class_list,
        pool_size=args.pool_size,
        train_ratio=args.train_ratio,
    )

    if dev_all:
        dev = conll_to_sentences(dev_all)
        n_dev_docs = len(dev_all.samples)
        dev_label = f"{n_dev_docs} source docs"
    elif fallback_dev is not None:
        dev = fallback_dev
        n_dev_docs = len({s["doc_id"] for s in dev})
        dev_label = "reusing phase 1 dev"
    else:
        raise ValueError(f"prepare_split({name!r}): provide dev_dir or fallback_dev")

    if test_all:
        test = conll_to_sentences(test_all)
        n_test_docs = len(test_all.samples)
        test_label = f"{n_test_docs} source docs"
    elif fallback_test is not None:
        test = fallback_test
        n_test_docs = len({s["doc_id"] for s in test})
        test_label = "reusing phase 1 test"
    else:
        raise ValueError(f"prepare_split({name!r}): provide test_dir or fallback_test")

    print(f"{'─' * 70}")
    print(
        f"Source docs — train: {len(train_all.samples)}, dev: {dev_label}, test: {test_label}"
    )
    print(f"Sampled     — train docs: {n_train_docs}, eval docs: {n_eval_docs}")
    print(
        f"Sentences   — train: {len(train)}, eval: {len(eval_)}, dev: {len(dev)}, test: {len(test)}"
    )
    print_distribution(train, "TRAIN", fn=label_distribution_sent)
    print_distribution(eval_, "EVAL", fn=label_distribution_sent)
    print(
        f"Classes     — {len(selected_classes)}: {', '.join(sorted(selected_classes))}"
    )
    print(f"{'─' * 70}")

    return DataSplit(
        name=name,
        train=train,
        eval=eval_,
        dev=dev,
        test=test,
        counter_examples=counter_examples,
        selected_classes=selected_classes,
        n_train_docs=n_train_docs,
        n_eval_docs=n_eval_docs,
        n_dev_docs=n_dev_docs,
        n_test_docs=n_test_docs,
    )


def prepare_relation_split(
    args,
    *,
    name: str,
    train_dir: str,
    dev_dir: str | None = None,
    test_dir: str | None = None,
    classes: str | None = None,
    fallback_dev: list | None = None,
    fallback_test: list | None = None,
) -> DataSplit:

    print(f"\nLoading {name} relation dataset...")
    print(f"\nLoading {name} dataset...")

    train_all = load_ner_dataset_from_conll(train_dir)

    dev_all = load_ner_dataset_from_conll(dev_dir) if dev_dir else None

    test_all = load_ner_dataset_from_conll(test_dir) if test_dir else None

    class_list = [c.strip() for c in classes.split(",")] if classes else None

    train, eval_, labels = sample_relation_stratified(
        train_data=train_all.samples,
        shots_per_class=args.shots,
        seed=args.seed,
        num_classes=args.num_classes,
        classes=class_list,
    )

    def _examples(dataset):
        return [
            ex
            for doc in dataset.samples
            for ex in build_relation_examples(doc)
            if ex["label"] in labels
        ]

    dev, test = _examples(dev_all), _examples(test_all)
    print(f"{'─' * 70}")
    print(f"Source docs — train: {len(train_all.samples)}")
    print(
        f"Sentences   — train: {len(train)}, eval: {len(eval_)}, dev: {len(dev)}, test: {len(test)}"
    )
    print(f"{'─' * 70}")

    return DataSplit(
        name=name,
        train=train,
        eval=eval_,
        dev=dev,
        test=test,
        counter_examples=[],
        selected_classes=labels,
        n_train_docs=len({e["doc_id"] for e in train}),
        n_eval_docs=len({e["doc_id"] for e in eval_}),
        n_dev_docs=len(dev_all.samples),
        n_test_docs=len(test_all.samples),
    )


def load_human_feedback(feedback_path, eval_dataset, learner, rules=None):
    def _norm(s):
        return s.replace("\u2011", "-").replace("\u2010", "-")

    feedback_items = json.loads(Path(feedback_path).read_text())
    print(f"  Loading {len(feedback_items)} human feedback items")
    for fb in feedback_items:
        level = fb.get("level", "task")
        if level == "correction":
            correction = Correction(
                id=str(uuid.uuid4())[:8],
                input=fb["input"],
                model_output=fb.get("model_output", {}),
                expected_output=fb["expected_output"],
                feedback=fb.get("text"),
            )
            eval_dataset.corrections.append(correction)
            print(f"✓ Added correction to eval dataset")
            continue
        text = fb["text"]
        target_id = ""
        if level == "rule" and rules is not None:
            rule_name = fb.get("rule_name", "")
            rule_id = fb.get("rule_id", "")
            matched = next((r for r in rules if r.id == rule_id), None)
            if matched:
                target_id = matched.id
            else:
                print(f"Rule not found: {rule_name} — treating as task-level")
                level = "task"
        eval_dataset.structured_feedback.append(
            Feedback(
                id=str(uuid.uuid4())[:8],
                text=text,
                level=level,
                target_id=target_id,
            )
        )
        learner.add_feedback(text, level, target_id)
