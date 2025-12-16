import argparse
import json
from pathlib import Path

from clear_anonymization.extractors import factory
from clear_anonymization.models.evaluator import (
    evaluate_char_level,
    evaluate_span_level,
)
from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample

from clear_anonymization.extractors.llm import PromptConfig, NERMode


def evaluate_samples_llm(samples: list[NERSample], evaluation_type: str, extractor):
    print(f"\nEvaluating model on {len(samples)} samples")
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    if evaluation_type == "span_level":
        print("\n---- Span-Level Evaluation ----")
        for threshold in thresholds:
            print(f"\nThreshold {threshold}")
            metrics = evaluate_span_level(extractor, samples, threshold)

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

    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )

    parser.add_argument("--mode", type=str, required=True, help="ONE_STEP or TWO_STEP")

    parser.add_argument("--prompt_one_step", type=str, required=False)
    parser.add_argument("--prompt_span", type=str, required=False)
    parser.add_argument("--prompt_label", type=str, required=False)

    parser.add_argument("--cache_file", type=str, default=None)

    parser.add_argument(
        "--zero_shot", action="store_true", help="Whether to use zero-shot NER."
    )

    args = parser.parse_args()

    data = NERData.from_json(json.loads(Path(args.input_dir).read_text()))
    samples = [s for s in data.samples if s.split == "validation"]

    print(f"\nEvaluating model on test samples: {len(samples)}")
    prompts_dir = Path(__file__).parent.parent / "clear_anonymization" / "prompts"
    prompts = PromptConfig(
        one_step=Path(args.prompt_one_step)
        if args.prompt_one_step
        else prompts_dir / f"{args.dataset}_task.txt",
        span=Path(args.prompt_span)
        if args.prompt_span
        else prompts_dir / f"{args.dataset}_ner_extract_spans.txt",
        label=Path(args.prompt_label)
        if args.prompt_label
        else prompts_dir / f"{args.dataset}_ner_label_spans.txt",
    )
    mode = NERMode(args.mode)
    LLMExtractor = factory.make_extractor(
        "llm",
        model=args.model,
        dataset=args.dataset,
        zero_shot=args.zero_shot,
        prompts=prompts,
        cache_file=args.cache_file,
        mode=mode,
    )

    evaluate_samples_llm(samples, args.evaluation_type, LLMExtractor)


if __name__ == "__main__":
    main()
