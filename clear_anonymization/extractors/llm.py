import argparse
import json
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from string import Template

from openai import OpenAI

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.base import BaseExtractor
from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets.ler_dataset import LERData, LERSample

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


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("LLM NER")


class LLMExtractor(BaseExtractor):
    """LLM-powered Named Entity Recognition"""

    def __init__(
        self,
        model: str,
        temperature: float = 0.0,
        lang: str = "de",
        zero_shot: bool = False,
        fewshot_path: str | None = None,
        prompt_path: str | None = None,
        cache_file: str | None = None,
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
        self.lang = lang
        self.zero_shot = zero_shot

        # self.client = self._get_openai_client()

        # Load few-shot examples

        if not self.zero_shot:
            if fewshot_path is None:
                fewshot_path = (
                    Path(__file__).parent.parent / "prompts" / "examples.json"
                )
            path = Path(fewshot_path)

            if not path.exists():
                print(f"Warning: Few-shot examples file not found at {path}")
            self.fewshot = (
                json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
            )

        # Load NER template
        if prompt_path is None:
            prompt_path = Path(__file__).parent.parent / "prompts" / "ner_task.txt"

        template_path = Path(prompt_path)
        if not template_path.exists():
            raise FileNotFoundError(f"Prompt template not found at {template_path}")
        self.template = Template(template_path.read_text(encoding="utf-8"))

        # Set up cache
        if cache_file is None:
            if not self.zero_shot:
                cache_file = (
                    Path(__file__).parent.parent
                    / f"cache"
                    / f"{model}_cache_fewshots.json"
                )
            else:
                cache_file = (
                    Path(__file__).parent.parent / f"cache" / f"{model}_cache.json"
                )
            print(f"Using default cache file: {cache_file}")
        else:
            print(f"Using provided cache file: {cache_file}")

        self.cache = CacheManager(cache_file)
        # print(self.cache)
        self.fewshot_block = self._fewshot_block()

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
            # print(ex["labels"][0])
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
    ) -> str:
        return self.template.substitute(text=text, fewshot_block=self._fewshot_block())

    @staticmethod
    def _to_spans(substrs: dict, sentence: str):
        spans = []
        for sub, label in substrs.items():
            if not sub:
                continue
            match = re.search(re.escape(sub), sentence)
            if match:
                spans.append(
                    {
                        "start": match.start(),
                        "end": match.end(),
                        "text": sub,
                        "class": label,
                    }
                )
        return spans

    def _predict(self, text: str) -> list[dict]:
        """

        :param text: The text where model needs to find named entities.
        :returns: List of labels.
        """

        # Build the full LLM prompt using the template

        llm_prompt = self._build_prompt(text)
        # print(llm_prompt)
        # Use the full LLM prompt for cache key calculation
        cache_key = self.cache._hash(text, self.model, str(self.temperature))

        cached = self.cache.get(cache_key)
        # print(cached)
        if cached is None:
            print("cache is nonee")
            resp = self._get_openai_client().chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an excellent linguistic for labelling named entities in given text.",
                    },
                    {"role": "user", "content": llm_prompt},
                ],
                response_format=NER_SCHEMA,
                temperature=self.temperature,
            )
            cached = resp.choices[0].message.content
            # print(cached)
            self.cache.set(cache_key, cached)
        try:
            payload = json.loads(cached)
            # print("Payload",payload)
            return self._to_spans(payload["labels"], text)
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing LLM response: {e}")
            print(f"Raw response: {cached}")
            return []

    def predict(self, text: str) -> list:
        """Recognize Named Entities for the provided text.
        :param text: The text where model needs to find named entities.
        :returns: List of labels.

        """

        return self._predict(text)

    def predict_batch(
        self,
        samples: list[LERSample],
    ) -> list:
        """Predict named entities  from the provided text.

        :param samples: .
        :returns: List of spans.
        """
        futs = []
        with ThreadPoolExecutor(max_workers=30) as pool:
            futs = [pool.submit(self._predict, s.sentences) for s in samples]
            return [f.result() for f in futs]


def main(
    input_dir: str,
    model: str,
    prompt_path: str,
    cache_file: str,
    lang: str = "de",
    dataset: str = "ler",
    zero_shot: bool = False,
):
    input_dir = Path(input_dir)
    prompt_path = Path(prompt_path)
    data = LERData.from_json(json.loads(input_dir.read_text()))
    LLMExtractor = factory.make_extractor(
        "llm",
        model=model,
        zero_shot=zero_shot,
        prompt_path=prompt_path,
        cache_file=cache_file,
    )
    print(zero_shot)
    samples = [s for s in data.samples if s.split == "validation"]
    print(len(samples))
    LLMExtractor.predict_batch(samples)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="User the LLM for a named entitiy recognition task"
    )
    parser.add_argument(
        "--input_dir", type=str, required=True, help="Path to the input data files"
    )

    parser.add_argument("--model", type=str, required=True, help="Model used for NER")

    parser.add_argument(
        "--prompt_path", type=str, required=True, help="Path to the prompt file"
    )
    parser.add_argument("--cache_file", type=str, help="Path to the cache file")

    parser.add_argument(
        "--lang", type=str, default="de", help="Language of the documents"
    )
    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )
    parser.add_argument(
        "--zero_shot", action="store_true", help="Whether to use zero-shot NER."
    )
    args = parser.parse_args()

    main(
        Path(args.input_dir),
        args.model,
        args.prompt_path,
        args.cache_file,
        args.lang,
        args.dataset,
        args.zero_shot,
    )
