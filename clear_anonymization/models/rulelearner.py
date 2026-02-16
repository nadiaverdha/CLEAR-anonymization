import argparse
import json
from datetime import datetime
import re
import os
import random
from datetime import datetime
from pathlib import Path
from typing import List, Literal

import rulechef
from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rulechef import RuleChef, Task, TaskType
from rulechef.core import RuleFormat
from rulechef.prompts import LANG_TO_FULL_NAME, Lang

from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample


class Entity(BaseModel):
    text: str = Field(description="The matched text span")
    start: int = Field(description="Start character offset")
    end: int = Field(description="End character offset")
    type: str = Field(description="Entity label")


class NEROutput(BaseModel):
    entities: List[Entity]


class RuleChefLearner:
    def __init__(
        self,
        model: str,
        dataset: str = "ler",
        allowed_classes: str | None = None,
        rule_file: str = "default",
        lang: Lang = "en",
    ):
        self.model = model
        self.client = self._get_openai_client()
        self.dataset = dataset
        self.lang = lang

        self.allowed_classes: set[str] = set()
        class_definitions = get_dataset_class_definitions(self.dataset)
        all_classes = set(class_definitions.keys())
        date_str = datetime.now().strftime("%Y-%m-%d")
        self.rule_file = rule_file
        if allowed_classes:
            allowed_list = [c.strip() for c in allowed_classes.split(",")]
            unknown = set(allowed_list) - all_classes
            if unknown:
                raise ValueError(f"Unknown entity classes: {unknown}")
            self.allowed_classes = set(allowed_list)
            self.allowed_classes_def = ", ".join(
                f"{c}: {class_definitions[c]}" for c in allowed_list
            )

            classes_str = "_".join(allowed_list)
        else:
            self.allowed_classes = all_classes
            self.allowed_classes_def = ", ".join(
                f"{c}: {class_definitions[c]}" for c in class_definitions
            )
            classes_str = "all_classes"

        task = Task(
            name="Named Entity Recognition",
            description=f"Extract {self.allowed_classes_def} from {LANG_TO_FULL_NAME.get(self.lang)} text ",
            input_schema={"text": "str"},
            output_schema=NEROutput,
            type=TaskType.NER,
        )
        model = self.model.replace("/", "_")

        self.chef = RuleChef(
            task,
            self.client,
            dataset_name=f"{date_str}_{model}_{self.dataset}_{classes_str}",
            allowed_formats=[RuleFormat.REGEX],
            model=self.model,
            use_spacy_ner=False,
            use_grex=True,
        )

    def _get_openai_client(self) -> OpenAI:
        """Get OpenAI client configured from environment variables."""
        api_key = os.getenv("OPENAI_API_KEY") or "EMPTY"
        base_url = os.getenv("OPENAI_BASE_URL") or "http://localhost:8000/v1"

        # "https://api.openai.com/v1"

        return OpenAI(api_key=api_key, base_url=base_url)

    def fit(self, samples, negative_samples):
        for sample in samples:
            self.chef.add_example(
                {"text": sample["text"]}, {"entities": sample["entities"]}
            )
        if negative_samples:
            for negative_sample in negative_samples:
                self.chef.add_negative_example(
                    {"text": negative_sample["text"]},
                    {"entities": negative_sample["entities"]},
                )

        self.chef.learn_rules(incremental_only=True)


def sample_data(samples, allowed_classes, k=50, seed=123, window_size=100):
    random.seed(seed)

    positive_samples = []
    for sample in samples:
        text = sample.text
        entities = sorted(
            [l for l in sample.labels if l["type"] in allowed_classes],
            key=lambda x: x["start"],
        )

        if not entities:
            continue
        merged_windows = []
        for ent in entities:
            start = max(0, ent["start"] - window_size)
            end = min(len(text), ent["end"] + window_size)
            if merged_windows and start <= merged_windows[-1][1]:
                merged_windows[-1][1] = max(end, merged_windows[-1][1])
                merged_windows[-1][2].append(ent)
            else:
                merged_windows.append([start, end, [ent]])

        for start, end, window_entities in merged_windows:
            snippet = text[start:end]
            adjusted_entities = []
            for e in window_entities:
                adjusted_entities.append(
                    {
                        "text": e["text"],
                        "start": e["start"] - start,
                        "end": e["end"] - start,
                        "type": e["type"],
                    }
                )

            positive_samples.append({"text": snippet, "entities": adjusted_entities})

    # Shuffle and limit number of examples
    if len(positive_samples) > k:
        positive_samples = random.sample(positive_samples, k)

    return positive_samples


def main():
    parser = argparse.ArgumentParser(description="Learn NER rules using a LLM")

    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path to the evaluation data (JSON format)",
    )
    parser.add_argument("--model", type=str, required=True, help="Model used for NER")
    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )

    parser.add_argument(
        "--lang", type=str, default="en", help="Language of the text (e.g. 'en','de')"
    )

    parser.add_argument(
        "--rule_file", type=str, default="ler", help="Name of the rule file"
    )
    parser.add_argument(
        "--allowed_classes",
        type=str,
        required=False,
        help="Comma-separated list of entity classes to extract (e.g. person,email_address)",
    )

    args = parser.parse_args()
    input_dir = Path(args.input_dir)

    # input_dir = Path(args.input_dir)
    # data = NERData.from_json(json.loads(input_dir.read_text(encoding="utf-8")))
    data = NERData.from_json(json.loads(input_dir.read_text()))

    rule_learner = RuleChefLearner(
        model=args.model,
        dataset=args.dataset,
        rule_file=args.rule_file,
        allowed_classes=args.allowed_classes,
        lang=args.lang,
    )

    # train_samples = [s for s in data.samples if s.split == "train"]
    sampled = sample_data(data.samples, rule_learner.allowed_classes)
    # print(sampled)
    rule_learner.fit(sampled, None)


if __name__ == "__main__":
    main()
