import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Literal

import rulechef
from openai import OpenAI
from pydantic import BaseModel, Field
from rulechef import RuleChef, Task, TaskType
from rulechef.core import RuleFormat

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.base import BaseExtractor
from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample

__all__ = ["RuleChefExtractor"]


class RuleChefExtractor(BaseExtractor):
    """RuleChef-powered Named Entity Recognition"""

    def __init__(
        self,
        model: str,
        dataset: str = "ler",
        allowed_classes: str | None = None,
    ):
        self.model = model
        #  self.rule_format = rule_format

        self.client = self._get_openai_client()
        print(self.client)
        self.dataset = dataset
        # Allowed classes
        class_definitions = get_dataset_class_definitions(self.dataset)
        all_classes = list(class_definitions.keys())

        self.allowed_classes = ""
        if allowed_classes:
            allowed_classes_list = [c.strip() for c in allowed_classes.split(",")]
            unknown_class = set(allowed_classes_list) - set(all_classes)
            if unknown_class:
                raise ValueError(
                    f"Unknown entity classes for dataset '{dataset}': {unknown}"
                )

            self.allowed_classes = ", ".join(
                f"{c}: {class_definitions[c]}" for c in allowed_classes_list
            )

            self.classes_str = "_".join(allowed_classes_list)

        else:
            self.allowed_classes = ", ".join(
                f"{c}: {class_definitions[c]}" for c in class_definitions
            )

            self.classes_str = "all_classes"

        task = Task(
            name="Named Entity Recognition",
            description=f"Extract {self.classes_str} entities from text",
            input_schema={"question": "str", "context": "str"},
            output_schema={"spans": "List[Span]"},
        )
        self.chef = RuleChef(
            task,
            self.client,
            dataset_name=self.dataset,
            allowed_formats=[RuleFormat.SPACY],
            model=self.model,
            use_spacy_ner=False,
        )

    def _get_openai_client(self) -> OpenAI:
        """Get OpenAI client configured from environment variables.

        :return: Configured OpenAI client
        :raises ValueError: If API key is not set
        """
        api_key = os.getenv("OPENAI_API_KEY") or "EMPTY"
        print(api_key)
        base_url = (
            os.getenv("OPENAI_BASE_URL") or "http://localhost:8000/v1"
        )  # "https://api.openai.com/v1"

        return OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def fit(self, samples):
        spans = []
        for i, sample in enumerate(samples):
            for label in sample.labels:
                if label["class"] in self.classes_str:
                    spans.append(label)
            print(spans)
            print("adding example  ", i)
            self.chef.add_example(
                {
                    "question": f"Extract {self.classes_str} entities",
                    "context": sample.text,
                },
                {"spans": spans},
            )
        self.chef.learn_rules()
        print(self.chef.dataset.rules)

    def _predict(self, text):
        return self.chef.extract(
            {"question": f"Detect {self.classes_str} mentions", "context": text}
        )["spans"]

    def predict(self, text):
        return self._predict(text)

    def predict_batch(self, samples):
        return [self.predict(s.text) for s in samples]


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a named entity recognition model based on LLM"
    )

    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path to the evaluation data (JSON format)",
    )

    parser.add_argument("--model", type=str, required=True, help="Model used for NER")
    ##  parser.add_argument(
    ##      "--cache_file", type=str, required=False, help="Path to the cache file" )

    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )
    parser.add_argument(
        "--allowed_classes",
        type=str,
        required=False,
        help="Comma-separated list of entity classes to extract (e.g. person,email_address)",
    )

    args = parser.parse_args()
    print(args.model)
    input_dir = Path(args.input_dir)
    data = NERData.from_json(json.loads(input_dir.read_text()))

    RuleChefExtractor = factory.make_extractor(
        "rulechef",
        model=args.model,
        dataset=args.dataset,
        allowed_classes=args.allowed_classes,
    )

    samples = [s for s in data.samples if s.split == "train"]
    RuleChefExtractor.fit(samples[10:30])
    test_samples = [s for s in data.samples if s.split == "validation"]

    for test in test_samples:
        result = RuleChefExtractor.predict(test)
        print(f"Output: {result}")


if __name__ == "__main__":
    main()
