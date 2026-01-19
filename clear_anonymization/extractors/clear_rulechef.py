import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Literal

import rulechef
from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rulechef import RuleChef, Task, TaskType
from rulechef.core import RuleFormat

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.base import BaseExtractor
from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample

__all__ = ["RuleChefExtractor"]


class Entity(BaseModel):
    text: str = Field(description="The matched text span")
    start: int = Field(description="Start character offset")
    end: int = Field(description="End character offset")
    type: str = Field(description="Entity label")


class NEROutput(BaseModel):
    entities: List[Entity]


class RuleChefExtractor(BaseExtractor):
    """RuleChef-powered Named Entity Recognition"""

    def __init__(
        self,
        model: str,
        dataset: str = "ler",
        allowed_classes: str | None = None,
    ):
        self.model = model
        self.client = self._get_openai_client()
        self.dataset = dataset

        self.allowed_classes = ""
        class_definitions = get_dataset_class_definitions(self.dataset)
        all_classes = set(class_definitions.keys())
        print(all_classes)

        if allowed_classes:
            allowed_list = [c.strip() for c in allowed_classes.split(",")]
            unknown = set(allowed_list) - all_classes
            if unknown:
                raise ValueError(f"Unknown entity classes: {unknown}")
            self.allowed_classes = set(allowed_list)
            self.allowed_classes_def = ", ".join(
                f"{c}: {class_definitions[c]}" for c in allowed_list
            )

        else:
            self.allowed_classes_def = ", ".join(
                f"{c}: {class_definitions[c]}" for c in class_definitions
            )
            self.allowed_classes = all_classes
        task = Task(
            name="Named Entity Recognition",
            description=f"Extract {self.allowed_classes_def} from text",
            input_schema={"text": "str"},
            output_schema=NEROutput,
            type=TaskType.NER,
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
        base_url = os.getenv("OPENAI_BASE_URL") or "http://localhost:8000/v1"

        return OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def fit(self, samples):
        for i, sample in enumerate(samples):
            spans = []
            for label in sample.labels:
                if label["class"] in self.allowed_classes:
                    spans.append(
                        {
                            "text": label["text"],
                            "start": label["start"],
                            "end": label["end"],
                            "type": label["class"],
                        }
                    )
            if spans:
                self.chef.add_example({"context": sample.text}, {"entities": spans})
        self.chef.learn_rules()
        print(self.chef.dataset.rules)

    def _predict(self, text):
        return self.chef.extract(text)

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
    input_dir = Path(args.input_dir)
    data = NERData.from_json(json.loads(input_dir.read_text()))

    RuleChefExtractor = factory.make_extractor(
        "rulechef",
        model=args.model,
        dataset=args.dataset,
        allowed_classes=args.allowed_classes,
    )

    samples = [s for s in data.samples if s.split == "train"]
    RuleChefExtractor.fit(samples)
    test_samples = [s for s in data.samples if s.split == "validation"]

    for test in test_samples:
        result = RuleChefExtractor.predict(test)
        print(f"Output: {result}")


if __name__ == "__main__":
    main()
