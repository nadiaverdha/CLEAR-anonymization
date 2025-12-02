import argparse
import json
from pathlib import Path

from clear_anonymization.extractors import factory
from clear_anonymization.models.evaluator import evaluate_char_level
from clear_anonymization.ner_datasets.ler_dataset import LERData, LERSample


def evaluate_samples_llm(samples: list[LERSample], evaluation_type: str, extractor):
    print(f"\nEvaluating model on {len(samples)} samples")

    if evaluation_type == "char_level":
        print("\n---- Character-Level Evaluation ----")
        metrics = evaluate_char_level(extractor, samples)
        print(f"  Precision: {metrics['precision']:.4f}")
        print(f"  Recall:    {metrics['recall']:.4f}")
        print(f"  F1:        {metrics['f1']:.4f}")
        return metrics

    else:
        raise ValueError("Use 'char_level'")


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
        help="Evaluation type (char_level)",
    )

    parser.add_argument("--prompt_path", type=str, default=None)
    parser.add_argument("--cache_file", type=str, default=None)

    args = parser.parse_args()

    data = LERData.from_json(json.loads(Path(args.input_dir).read_text()))
    test_samples = [s for s in data.samples if s.split == "test"]

    print(f"\nEvaluating model on test samples: {len(test_samples)}")

    LLMExtractor = factory.make_extractor(
        "llm",
        model=args.model,
        prompt_path=args.prompt_path,
        cache_file=args.cache_file,
    )

    evaluate_samples_llm(test_samples, args.evaluation_type, LLMExtractor)


if __name__ == "__main__":
    main()
