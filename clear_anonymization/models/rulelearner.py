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
    ):
        self.model = model
        self.client = self._get_openai_client()
        self.dataset = dataset

        self.allowed_classes: set[str] = set()
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
            self.allowed_classes = all_classes
            self.allowed_classes_def = ", ".join(
                f"{c}: {class_definitions[c]}" for c in class_definitions
            )
        print(os.getenv("OPENAI_API_KEY"))
        print(os.getenv("OPENAI_BASE_URL"))
        print(self.allowed_classes)
        print(f"Extract {self.allowed_classes_def} from text")

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
            dataset_name=self.dataset + "_" + self.model + "2",
            allowed_formats=[RuleFormat.SPACY],
            model=self.model,
            use_spacy_ner=False,
        )

    def _get_openai_client(self) -> OpenAI:
        """Get OpenAI client configured from environment variables."""
        api_key = os.getenv("OPENAI_API_KEY") or "EMPTY"
        base_url = (
            os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1"
        )  # "http://localhost:8000/v1"
        return OpenAI(api_key=api_key, base_url=base_url)

    def fit(self, samples):
        for sample in samples:
            positive_spans = []
            negative_spans = []
            for label in sample.labels:
                if label["class"] in self.allowed_classes:
                    # positive spans
                    positive_spans.append(
                        {
                            "text": label["text"],
                            "start": label["start"],
                            "end": label["end"],
                            "type": label["class"],
                        }
                    )
                else:
                    # negative spans
                    negative_spans.append(
                        {
                            "text": label["text"],
                            "start": label["start"],
                            "end": label["end"],
                            "type": label["class"],
                        }
                    )
            if positive_spans:
                # positive example
                self.chef.add_example(
                    {"text": sample.text}, {"entities": positive_spans}
                )
            if negative_spans:
                # negative example
                self.chef.add_negative_example(
                    {"text": sample.text}, {"entities": negative_spans}
                )

            if not sample.labels:
                self.chef.add_negative_example(
                    {"text": sample.text}, {"entities": []}, source="human_negative"
                )

        self.chef.learn_rules()


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

    rule_learner = RuleChefLearner(
        model=args.model,
        dataset=args.dataset,
        allowed_classes=args.allowed_classes,
    )

    train_samples = [s for s in data.samples if s.split == "train"]
    rule_learner.fit(train_samples[:100])


if __name__ == "__main__":
    main()
