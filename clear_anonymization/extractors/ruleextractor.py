import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Literal
from typing import Dict, List, Any, Optional

import rulechef
from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rulechef import RuleChef, Task, TaskType, Rule
from rulechef.executor import RuleExecutor
from rulechef.core import RuleFormat

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.base import BaseExtractor
from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample

__all__ = ["RuleChefExtractor"]


class RuleExtractor(BaseExtractor):
    """RuleChef-powered Named Entity Recognition"""

    def __init__(
        self,
        rules: List[Rule],
        use_spacy_ner=False,
        dataset: str = "ler",
        task_type: TaskType = TaskType.NER,
        text_field: Optional[str] = None,
    ):
        self.dataset = dataset
        self.chefexecutor = RuleExecutor(use_spacy_ner)
        self.rules = rules
        self.task_type = task_type
        self.text_field = text_field

    def _predict(self, text):
        return self.chefexecutor.apply_rules(
            self.rules, text, self.task_type, self.text_field
        )

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

    parser.add_argument(
        "--rules_file",
        type=str,
        help="Path to the rules data (JSON format)",
    )

    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )

    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    data = NERData.from_json(json.loads(input_dir.read_text()))

    rules_file = Path(args.rules_file)
    if not rules_file.exists():
        raise FileNotFoundError(f"Rules file not found: {rules_file}")

    rules_data = json.loads(rules_file.read_text())

    rules = [Rule.from_dict(r) for r in rules_data.get("rules")]
    print(rules)

    RuleChefExtractor = factory.make_extractor(
        "rulechef",
        dataset=args.dataset,
        rules=rules,
    )

    test_samples = [s for s in data.samples if s.split == "validation"]

    for test in test_samples:
        result = RuleChefExtractor.predict({"text": test.text})
        print(f"Output: {result}")


if __name__ == "__main__":
    main()
