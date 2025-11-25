import argparse
import json
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from string import Template

from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_inference.generate import generate
from mistral_inference.transformer import Transformer
from openai import OpenAI
from transformers import AutoModelForCausalLM, AutoTokenizer

from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets import ler_dataset
from clear_anonymization.ner_datasets.ler_dataset import *

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
        model: Transformer,  # "gpt-4.1-mini"
        tokenizer: MistralTokenizer,
        temperature: float = 0.0,
        lang: str = "de",
        zero_shot: bool = False,
        fewshot_path: str | None = None,
        prompt_path: str | None = None,
        cache_file: str | None = None,
    ):
        """Initialize the LLMNER.

        :param model: The model to use for NER.
        :param tokenizer: The model tokenizer to use for NER.
        :param temperature: The temperature to use for NER.
        :param lang: The language to use for NER.
        :param zero_shot: Whether to use zero-shot NER.
        :param fewshot_path: The path to the few-shot examples.
        :param prompt_path: The path to the prompt.
        :param cache_file: The path to the cache file.
        """

        self.model = model
        self.tokenizer = tokenizer
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
            cache_file = Path(__file__).parent.parent / "cache" / f"cache_mistral.json"
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

        # Use the full LLM prompt for cache key calculation
        cache_key = self.cache._hash(llm_prompt, "mistral", str(self.temperature))
        cached = self.cache.get(cache_key)
        if cached is None:
            completion_request = ChatCompletionRequest(
                messages=[UserMessage(content=llm_prompt)]
            )
            token_ids = self.tokenizer.encode_chat_completion(completion_request).tokens

            out_tokens, _ = generate(
                [token_ids],
                self.model,
                max_tokens=4500,
                temperature=self.temperature,
                eos_id=self.tokenizer.instruct_tokenizer.tokenizer.eos_id,
            )
            cached = self.tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])

            self.cache.set(cache_key, cached)
        try:
            payload = json.loads(cached)
            return self._to_spans(payload["labels"], tokens)
        # return payload
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing LLM response: {e}")
           # print(f"Raw response: {cached}")
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
                print("FFF",f.result())
            return [f.result() for f in futs]


def main(
    input_dir: Path,
    model_path: Path,
    lang: str = "de",
    dataset: str = "ler",
):
    input_dir = Path(input_dir)
    model_path = Path(model_path)
    prompt_path = Path(__file__).parent.parent / "prompts" / "ner_task_2.txt"

    input_file = input_dir / f"{dataset}_data.json"

    if not input_file.exists():
        logger.error(f"Input file not found: {input_file}")
        raise FileNotFoundError(f"Input file not found: {input_file}")

    try:
        data = LERData.from_json(json.loads(input_file.read_text()))
    except Exception as e:
        logger.error(f"Error loading input data: {e!s}")
        raise

    tokenizer = MistralTokenizer.from_file(f"{model_path}/tokenizer.model.v3")
    model = Transformer.from_folder(model_path)
    model.to(torch.device("cuda"))


    extractor = LLMExtractor(model=model, tokenizer=tokenizer, prompt_path=prompt_path)
    extractor.predict_batch(data.samples[:1])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="User the LLM for a named entitiy recognition task"
    )
    parser.add_argument(
        "--input_dir", type=str, required=True, help="Path to the input data files"
    )

    parser.add_argument(
        "--model_path", type=str, required=True, help="Path to the input data files"
    )

    parser.add_argument(
        "--lang", type=str,default="de", help="Language of the documents"
    )
    parser.add_argument(
        "--dataset", type=str, default= "ler",help="Name of the dataset"
    )
    args = parser.parse_args()

    main(
        Path(args.input_dir),
        Path(args.model_path),
        args.lang,
        args.dataset,
    )
