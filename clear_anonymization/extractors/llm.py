import argparse
import json
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from string import Template

from clear_anonymization.extractors import factory

from openai import OpenAI
from transformers import AutoModelForCausalLM, AutoTokenizer

from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets import ler_dataset
from clear_anonymization.ner_datasets.ler_dataset import *

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


class LLMExtractor:
    """LLM-powered Named Entity Recognition"""

    def __init__(
        self,
        model: str = "google/gemma-3-27b-it",
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

        # Load few-shot examples

        if fewshot_path is None:
            fewshot_path = Path(__file__).parent.parent / "prompts" / "examples.json"
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
            cache_file = Path(__file__).parent.parent / "cache" / f"cache_{model}.json"
            print(f"Using default cache file: {cache_file}")
        else:
            print(f"Using provided cache file: {cache_file}")

        self.cache = CacheManager(cache_file)

    def _fewshot_block(self) -> str:
        if self.zero_shot or not self.fewshot:
            return ""
        lines = []
        for i, ex in enumerate(self.fewshot, 1):
            lines.append(
                f"""<example{i}>
                <tokens>{ex["tokens"]}</tokens>
                <target>{{"labels": {json.dumps(ex["labels"], ensure_ascii=False)} }}</target>
                </example{i}>"""
            )
        return "\n".join(lines)

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

    def _build_prompt(
        self,
        tokens,
    ) -> str:
        return self.template.substitute(
            tokens=tokens, fewshot_block=self._fewshot_block()
        )

    @staticmethod
    def _to_spans(substrs: dict, sentence: str):
        spans = []
        for sub in substrs:
            print(sub)
            if not sub:
                continue
            print(sub)
            match = re.search(re.escape(sub["token"]), sentence)
            if match:
                spans.append(
                    {
                        "start": match.start(),
                        "end": match.end(),
                        "text": sub["token"],
                        "entity": sub["label"],
                    }
                )
        return spans

    def _predict(self, tokens: list[str]) -> list[dict]:
        """Single tokens → labels.

        :param tokens: The tokens string.
        :returns: List of labels.
        """

        # Build the full LLM prompt using the template

        llm_prompt = self._build_prompt(tokens)
        client = self._get_openai_client()
        # Use the full LLM prompt for cache key calculation
        cache_key = self.cache._hash(llm_prompt, "mistral", str(self.temperature))
        cached = self.cache.get(cache_key)
        if cached is None:
            resp = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an excellent linguistic for labelling named entities in given tokens.",
                    },
                    # Use the full LLM prompt here, not the raw context
                    {"role": "user", "content": llm_prompt},
                ],
                response_format=NER_SCHEMA,
                temperature=self.temperature,
            )
            cached = resp.choices[0].message.content

            self.cache.set(cache_key, cached)
        try:
            payload = json.loads(cached)
            #return self._to_spans(payload["labels"], tokens)
            return payload
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing LLM response: {e}")
            print(f"Raw response: {cached}")
            return []

    def predict(self, tokens: list[str]) -> list:
        """Recognize Named Entities for the provided tokens.
        :param tokens: tokens of a passage.
        :returns: List of labels.

        """

        return self._predict(tokens)

    def predict_batch(self, tokens_list: list[list]) -> list:
        """Predict named entities  from the provided tokens.

        :param prompts: List of tokens.
        :returns: List of spans.
        """

        with ThreadPoolExecutor(max_workers=3) as pool:
            futs = [pool.submit(self._predict, t) for t in tokens_list]
            for f in futs:
                print("FFF", f.result())
            return [f.result() for f in futs]


def main(
    input_dir: Path,
    model_path: Path,
    lang: str = "de",
    dataset: str = "ler",
):
    input_dir = Path(input_dir)
    prompt_path = Path(__file__).parent.parent / "prompts" / "ner_task_2.txt"
    sentence = "In diesem machte er im Wege der Stufenklage Pflichtteils- und Pflichtteilsergänzungsansprüche gegen die Restitutionsbeklagte ( im Folgenden : Beklagte ) aus dem Erbfall nach dem am 26. Juni 2006 verstorbenen Erblasser geltend ."
    # sentence = "dd ) Art. 33 Abs. 5 GG würde demnach die Möglichkeit nicht ausschließen , unter den vorgenannten Bedingungen in Ausnahmefällen andere als Lebenszeitrichterverhältnisse zu begründen ."
    # tokens = sentence.split(" ")
    LLMExtractor = factory.make_extractor("llm", prompt_path=prompt_path)
    predicted = LLMExtractor.predict(sentence)
    print(predicted)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="User the LLM for a named entitiy recognition task"
    )
    parser.add_argument(
        "--input_dir", type=str, required=True, help="Path to the input data files"
    )

    parser.add_argument("--model", type=str, required=True, help="Model used for NER")

    parser.add_argument(
        "--lang", type=str, default="de", help="Language of the documents"
    )
    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )
    args = parser.parse_args()

    main(
        Path(args.input_dir),
        args.model,
        args.lang,
        args.dataset,
    )
