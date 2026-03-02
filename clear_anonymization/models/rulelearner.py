import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path

import rulechef
from openai import OpenAI
from rulechef import RuleChef, Task, TaskType
from rulechef.core import RuleFormat, Dataset

from rulechef.evaluation import evaluate_rules_individually, print_rule_metrics
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample
from clear_anonymization.utils.utils import *


class RuleChefLearner:
    def __init__(
        self,
        model: str,
        dataset: str = "ler",
        allowed_classes: str | None = None,
        rule_file: str = "default",
    ):
        self.model = model
        self.client = self._get_openai_client()
        self.dataset = dataset

        date_str = datetime.now().strftime("%Y-%m-%d")
        classes_str, allowed_classes_def = get_class_def("bfg", [allowed_classes])
        task = Task(
            name="Named Entity Recognition",
            description=f"Extract {allowed_classes_def} from text ",
            input_schema={"text": "str"},
            output_schema=NEROutput,
            type=TaskType.NER,
            text_field="text",
        )
        self.chef = RuleChef(
            task,
            self.client,
            dataset_name=f"{date_str}_findok_{classes_str}",
            storage_path=".",
            model=self.model,
            allowed_formats=[RuleFormat.REGEX],  # regex-only for transparency
            use_grex=True,  # use grex to suggest regex patterns from examples
        )

    def _get_openai_client(self) -> OpenAI:
        """Get OpenAI client configured from environment variables."""
        api_key = os.getenv("OPENAI_API_KEY") or "EMPTY"
        base_url = os.getenv("OPENAI_BASE_URL") or "http://localhost:8000/v1"

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
        type=lambda s: s.split(",") if s else None,
        required=False,
        help="Comma-separated list of entity classes to extract (e.g. person,email_address)",
    )

    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    data = NERData.from_json(json.loads(input_dir.read_text()))

    rule_learner = RuleChefLearner(
        model=args.model,
        dataset=args.dataset,
        rule_file=args.rule_file,
        allowed_classes=args.allowed_classes,
    )

    sampled = sample_data(data.samples, rule_learner.allowed_classes)

    rule_learner.fit(sampled, None)


if __name__ == "__main__":
    main()
