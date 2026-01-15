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

from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample
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
        cache_file: str,
        dataset: str = "ler",
        allowed_classes: str | None = None,
    ):
        self.model = model
      #  self.rule_format = rule_format

        self.client = self._get_openai_client()
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

        if cache_file:
            cache_file = Path(cache_file)
            print(cache_file)
        else:
            model_name = model.replace("/", "_")
            date_str = datetime.now().strftime("%Y-%m-%d")
            cache_folder = (
                Path(__file__).parent.parent
                / "cache"
                / "rulechef"
                / model_name
                / date_str
            )
            cache_folder.mkdir(parents=True, exist_ok=True)
            cache_file = cache_folder / f"{dataset}_{self.classes_str}_cache.json"
        print(f"Using cache file: {cache_file}")
        self.cache = CacheManager(cache_file)
        print(self.classes_str)
        task = Task(
            name="Named Entity Recognition",
            description=f"Extract {self.classes_str} entities from text",
            input_schema={"question": "str", "context": "str"},
            output_schema={"spans": "List[Span]"},
        )
        self.chef = RuleChef(
            task, self.client, allowed_formats=[RuleFormat.SPACY], model=self.model
        )

    def _get_openai_client(self) -> OpenAI:
        """Get OpenAI client configured from environment variables.

        :return: Configured OpenAI client
        :raises ValueError: If API key is not set
        """
        api_key = os.getenv("OPENAI_API_KEY") or "EMPTY"
        base_url = (
            os.getenv("OPENAI_BASE_URL") or "http://localhost:8000/v1"
        )  # "https://api.openai.com/v1"

        return OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def fit(self, samples):
        for sample in samples:
            spans = [label for label in sample.labels if label["class"] in self.allowed_classes]
            self.chef.add_example(
                {"question": f"Extract {self.classes_str} entities", "context": sample.text},
                {"spans": spans},
            )
        self.chef.learn_rules()

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
    parser.add_argument(
        "--cache_file", type=str, required=False, help="Path to the cache file"
    )

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

    LLMExtractor = factory.make_extractor(
        "rulechef",
        model=args.model,
        dataset=args.dataset,
        cache_file=args.cache_file,
        allowed_classes=args.allowed_classes,
    )

    samples = [s for s in data.samples if s.split == "validation"]
    LLMExtractor.fit(samples)

    


if __name__ == "__main__":
    main()
