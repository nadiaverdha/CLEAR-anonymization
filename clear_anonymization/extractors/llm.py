import argparse
import json
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from string import Template

from openai import OpenAI

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.base import BaseExtractor
from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets import get_dataset_class_definitions
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample

__all__ = ["LLMExtractor"]


NER_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "NER",
        "schema": {
            "type": "object",
            "properties": {
                "labels": {"type": "object", "additionalProperties": {"type": "string"}}
            },
            "additionalProperties": False,
        },
        "strict": True,
    },
}


SPAN_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "SpanExtraction",
        "schema": {
            "type": "object",
            "properties": {"spans": {"type": "array", "items": {"type": "string"}}},
            "required": ["spans"],
            "additionalProperties": False,
        },
        "strict": True,
    },
}

LABEL_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "NER",
        "schema": {
            "type": "object",
            "properties": {
                "labels": {"type": "object", "additionalProperties": {"type": "string"}}
            },
            "required": ["labels"],
            "additionalProperties": False,
        },
        "strict": True,
    },
}


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("LLM NER")


@dataclass
class PromptConfig:
    one_step: Path | None = None
    span: Path | None = None
    label: Path | None = None


class NERMode(str, Enum):
    ONE_STEP = "one_step"
    TWO_STEP = "two_step"


class LLMExtractor(BaseExtractor):
    """LLM-powered Named Entity Recognition"""

    def __init__(
        self,
        model: str,
        temperature: float = 0.0,
        dataset: str = "ler",
        zero_shot: bool = False,
        mode: NERMode = NERMode.ONE_STEP,
        fewshot_path: str | None = None,
        prompts: PromptConfig | None = None,
        cache_file: str | None = None,
        cache_spans: str | None = None,
        allowed_classes: str | None = None,
    ):
        """Initialize the LLMExtractor.

        :param model: The model to use for NER.
        :param temperature: The temperature to use for NER.
        :param lang: The language to use for NER.
        :param zero_shot: Whether to use zero-shot NER.
        :param fewshot_path: The path to the few-shot examples.
        :param prompt_path: The path to the prompt.
        :param cache_file: The path to the cache file.
        """

        self.model = model
        self.temperature = temperature
        self.zero_shot = zero_shot
        self.dataset = dataset
        self.mode = mode

        # Load few-shot examples

        if not self.zero_shot:
            if fewshot_path is None:
                fewshot_path = (
                    Path(__file__).parent.parent
                    / "prompts"
                    / f"{dataset}_examples.json"
                )
            path = Path(fewshot_path)

            if not path.exists():
                print(f"Warning: Few-shot examples file not found at {path}")
            self.fewshot = (
                json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
            )

        self._fewshot_block_str = self._fewshot_block()

        # Loading templates based on mode
        if self.mode == NERMode.ONE_STEP:
            self.one_step_template = Template(prompts.one_step.read_text("utf-8"))
        else:
            self.span_template = Template(prompts.span.read_text("utf-8"))
            self.label_template = Template(prompts.label.read_text("utf-8"))

        # Allowed classes
        all_classes = list(get_dataset_class_definitions(self.dataset).keys())

        if allowed_classes:
            self.allowed_classes = [c.strip() for c in allowed_classes.split(",")]
            classes_str = "_".join(self.allowed_classes)
            unknown_class = set(self.allowed_classes) - set(all_classes)
            if unknown_class:
                raise ValueError(
                    f"Unknown entity classes for dataset '{dataset}': {unknown}"
                )

        else:
            self.allowed_classes = all_classes
            classes_str = "all_classes"

        if cache_file:
            cache_file = Path(cache_file)
            print(cache_file)
        else:
            model_name = model.replace("/", "_")
            date_str = datetime.now().strftime("%Y-%m-%d")
            cache_folder = (
                Path(__file__).parent.parent / "cache" / model_name / date_str
            )
            cache_folder.mkdir(parents=True, exist_ok=True)
            cache_file = (
                cache_folder
                / f"{dataset}_{mode}_{classes_str}_cache{'_fewshots' if not zero_shot else ''}.json"
            )

        if self.mode == NERMode.TWO_STEP:
            if not cache_spans:
                cache_spans = (
                    cache_folder
                    / f"{dataset}_{mode}_{classes_str}_cache_spans{'_fewshots' if not zero_shot else ''}.json"
                )
            self.cache_spans = CacheManager(cache_spans)

        print(f"Using cache file: {cache_file}")
        self.cache = CacheManager(cache_file)

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

    def _fewshot_block(self) -> str:
        if self.zero_shot or not self.fewshot:
            return ""
        lines = []
        for i, ex in enumerate(self.fewshot, 1):
            lines.append(
                f"""<example{i}>
                <text>{ex["text"]}</text>
                <target>{{"labels": {json.dumps(ex["labels"], ensure_ascii=False)} }}</target>
                </example{i}>"""
            )
        return "\n".join(lines)

    def _build_prompt(
        self,
        text,
        spans=None,
    ) -> str:
        # one step task
        if self.mode == NERMode.ONE_STEP:
            return self.one_step_template.substitute(
                allowed_classes=self.allowed_classes,
                text=text,
                fewshot_block=self._fewshot_block(),
            )
        # two step task
        if spans is None:
            return self.span_template.substitute(
                allowed_classes=self.allowed_classes,
                text=text,
                fewshot_block=self._fewshot_block(),
            )

        spans_block = "\n".join(f"- {s}" for s in spans)
        return self.label_template.substitute(
            allowed_classes=self.allowed_classes,
            text=text,
            spans=spans_block,
            fewshot_block=self._fewshot_block(),
        )

    def _cache_or_call(
        self,
        cache: CacheManager,
        text: str,
        content: str,
        llm_prompt: str,
        schema: dict,
    ):
        cache_key = cache._hash(llm_prompt, self.model, str(self.temperature))
        cached = cache.get(cache_key)
        if cached is None:
            print("cache is none")
            resp = self._get_openai_client().chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": content,
                    },
                    {"role": "user", "content": llm_prompt},
                ],
                response_format=schema,
                temperature=self.temperature,
            )
            cached = resp.choices[0].message.content
            # print(cached)
            cache.set(cache_key, cached)
        try:
            payload = json.loads(cached)

            if schema is SPAN_SCHEMA:
                # print(payload["spans"])
                return payload["spans"]

            else:
                # print(self._to_labels(payload["labels"], text))
                return self._to_labels(payload["labels"], text)

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing LLM response: {e}")
            print(f"Raw response: {cached}")
            return []

    def _predict_spans(self, text: str, *args) -> list[str]:
        llm_prompt = self._build_prompt(text)
        return self._cache_or_call(
            self.cache_spans,
            text,
            "You are an excellent linguistic for finding named entities spans in given text.",
            llm_prompt,
            SPAN_SCHEMA,
        )

    def _label_spans(self, text: str, spans: list[str]) -> dict:
        llm_prompt = self._build_prompt(text, spans)

        return self._cache_or_call(
            self.cache,
            text,
            "You are an excellent linguistic for labelling named entities in given text.",
            llm_prompt,
            LABEL_SCHEMA,
        )

    def _predict(self, text: str) -> list[dict]:
        """

        :param text: The text where model needs to find named entities.
        :returns: List of labels.
        """

        # Build the full LLM prompt using the template
        llm_prompt = self._build_prompt(text)

        if self.mode == NERMode.ONE_STEP:
            return self._cache_or_call(
                self.cache,
                text,
                "You are an excellent linguistic for labelling named entities in given text.",
                llm_prompt,
                NER_SCHEMA,
            )
        else:
            spans = self._predict_spans(text)
            labels = self._label_spans(text, spans)
            return labels

    @staticmethod
    def _to_labels(substrs: dict, sentence: str):
        labels = []
        for sub, label in substrs.items():
            if not sub:
                continue
            match = re.search(re.escape(sub), sentence)
            if match:
                labels.append(
                    {
                        "start": match.start(),
                        "end": match.end(),
                        "text": sub,
                        "class": label,
                    }
                )
        return labels

    def predict(self, text: str) -> list:
        """Recognize Named Entities for the provided text.
        :param text: The text where model needs to find named entities.
        :returns: List of labels.

        """

        return self._predict(text)

    def predict_batch(
        self,
        samples: list[NERSample],
    ) -> list:
        """Predict named entities  from the provided text.

        :param samples: .
        :returns: List of spans.
        """
        futs = []
        with ThreadPoolExecutor(max_workers=30) as pool:
            futs = [pool.submit(self._predict, s.text) for s in samples]
            return [f.result() for f in futs]


def main(
    input_dir: str,
    model: str,
    mode: str,
    prompt_one_step: str,
    prompt_span: str,
    prompt_label: str,
    cache_file: str,
    dataset: str = "ler",
    fewshot_path=None,
    allowed_classes: str | None = None,
    zero_shot: bool = False,
):
    input_dir = Path(input_dir)
    data = NERData.from_json(json.loads(input_dir.read_text()))

    mode = NERMode(args.mode)

    prompts_dir = Path(__file__).parent.parent / "prompts"
    prompts = PromptConfig(
        one_step=Path(args.prompt_one_step)
        if args.prompt_one_step
        else prompts_dir / f"{dataset}_task.txt",
        span=Path(args.prompt_span)
        if args.prompt_span
        else prompts_dir / f"{dataset}_ner_extract_spans.txt",
        label=Path(args.prompt_label)
        if args.prompt_label
        else prompts_dir / f"{dataset}_ner_label_spans.txt",
    )

    LLMExtractor = factory.make_extractor(
        "llm",
        model=model,
        dataset=dataset,
        zero_shot=zero_shot,
        mode=mode,
        prompts=prompts,
        cache_file=cache_file,
        fewshot_path=fewshot_path,
        allowed_classes=allowed_classes,
    )
    samples = [s for s in data.samples if s.split == "validation"]

    LLMExtractor.predict_batch(samples)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="User the LLM for a named entitiy recognition task"
    )
    parser.add_argument(
        "--input_dir", type=str, required=True, help="Path to the input data files"
    )

    parser.add_argument("--model", type=str, required=True, help="Model used for NER")
    parser.add_argument("--mode", type=str, required=True, help="ONE_STEP or TWO_STEP")

    parser.add_argument("--prompt_one_step", type=str, required=False)
    parser.add_argument("--prompt_span", type=str, required=False)
    parser.add_argument("--prompt_label", type=str, required=False)

    parser.add_argument(
        "--cache_file", type=str, required=False, help="Path to the cache file"
    )

    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )
    parser.add_argument(
        "--fewshot_path", required=False, type=str, help="Path to the fewshot file"
    )

    parser.add_argument(
        "--allowed_classes",
        type=str,
        required=False,
        help="Comma-separated list of entity classes to extract (e.g. person,email_address)",
    )

    parser.add_argument(
        "--zero_shot",
        action="store_true",
        required=False,
        help="Whether to use zero-shot NER.",
    )

    args = parser.parse_args()

    main(
        Path(args.input_dir),
        args.model,
        args.mode,
        args.prompt_one_step,
        args.prompt_span,
        args.prompt_label,
        args.cache_file,
        args.dataset,
        args.fewshot_path,
        args.allowed_classes,
        args.zero_shot,
    )
