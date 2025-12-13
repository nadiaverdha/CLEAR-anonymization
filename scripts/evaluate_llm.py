import argparse
import json
from pathlib import Path

from clear_anonymization.extractors import factory
from clear_anonymization.models.evaluator import (
    evaluate_char_level,
    evaluate_span_level,
)
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample


def evaluate_samples_llm(
    samples: list[NERSample], evaluation_type: str, extractor, threshold: float
):
    print(f"\nEvaluating model on {len(samples)} samples")

    if evaluation_type == "span_level":
        print("\n---- Span-Level Evaluation ----")
        metrics = evaluate_span_level(extractor, samples, threshold)

        return metrics
    else:
        raise ValueError("Use 'span_level'.")


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a named entity recognition model based on LLM"
    )

    parser.add_argument(
        "--model",
        type=str,
        help="Model name, e.g. google/gemma-3-27b-it",
    )

    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path to the evaluation data (JSON format)",
    )

    parser.add_argument(
        "--evaluation_type",
        type=str,
        help="Evaluation type (span_level or char_level)",
    )

    parser.add_argument("--prompt_path", type=str, default=None)
    parser.add_argument("--cache_file", type=str, default=None)
    parser.add_argument(
        "--threshold",
        type=float,
        help="Pick threshold if you want to perform span_level evaluation",
    )
    parser.add_argument(
        "--zero_shot", action="store_true", help="Whether to use zero-shot NER."
    )

    args = parser.parse_args()

    data = NERData.from_json(json.loads(Path(args.input_dir).read_text()))
    samples = [s for s in data.samples if s.split == "validation"]

    print(f"\nEvaluating model on test samples: {len(samples)}")

    LLMExtractor = factory.make_extractor(
        "llm",
        model=args.model,
        prompt_path=args.prompt_path,
        cache_file=args.cache_file,
        zero_shot=args.zero_shot,
    )

    evaluate_samples_llm(samples, args.evaluation_type, LLMExtractor, args.threshold)


if __name__ == "__main__":
    main()
