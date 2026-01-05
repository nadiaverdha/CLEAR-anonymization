import argparse
import json
from datetime import datetime
from pathlib import Path


def create_md_eval_report(file_path: str | Path, title: str = "Evaluation Results"):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        return
    threshold_explanation = (
        "**Thresholds explanation:**\n\n"
        "Each model is evaluated on different thresholds."
        "The threshold represents the minimum overlap required for a "
        "predicted entity span to be considered correct.\n"
        "**Examples:**\n\n"
        "- A threshold of **1.0** means that each predicted span is considered correct "
        "only if it has a **100% overlap** with the gold span.\n"
        "- A threshold of **0.5** means that each predicted span is considered correct "
        "if it has at least a **50% overlap** with the gold span.\n\n"
    )

    model_command = (
        "Before evaluating the models, the prediction result files must be generated. "
        "First, start the local vLLM server using this example command:\n"
        "```bash\n"
        "python -m vllm.entrypoints.openai.api_server "
        "--model google/gemma-3-27b-it "
        "--host 0.0.0.0 "
        "--port 8000 \n\n"
        "```\n\n"
        "Next, run the following command on another terminal:\n\n"
        "```bash\n"
        "python clear_anonymization/extractors/llm.py "
        "--input_dir data/m2n/m2n_data.json "
        "--model {MODEL_NAME} "
        "--mode {one_step or two_step} "
        "--dataset m2n "
        "--zero_shot \n\n"
        "```\n\n"
    )

    eval_command = (
        "Evaluation of the model results can be done by running the following example bash command:\n\n"
        "```bash\n"
        "python scripts/evaluate_llm.py "
        "--model {MODEL_NAME} "
        "--input_dir data/m2n/m2n_data.json "
        "--evaluation_type span_level "
        "--dataset m2n "
        "--mode {one_step or two_step} "
        "--zero_shot \n\n"
        "```\n\n"
    )

    with file_path.open("w") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Generated on: {datetime.now().isoformat()}\n\n")
        f.write(threshold_explanation)
        f.write(model_command)
        f.write(eval_command)


def append_eval_table(file_path, meta_data, thresholds_data):
    headers = ["Class", "Precision", "Recall", "F1"]

    table_title = f"## Evaluation Results of {meta_data['model']} - {meta_data['mode']} -  {meta_data['allowed_classes']}"

    existing_content = ""
    if file_path.exists():
        existing_content = file_path.read_text(encoding="utf-8")
    if f"{table_title}" in existing_content:
        print(f"⚠️ Skipping table '{table_title}' because it already exists")
        return

    with file_path.open("a") as f:
        f.write(f"{table_title}\n\n")
        for threshold_str, data in thresholds_data.items():
            f.write("\n")
            f.write(f"### Threshold {threshold_str}\n\n")

            overall = data["overall"]
            per_class = data["per_class"]

            f.write("| " + " | ".join(headers) + " |\n")
            f.write("|" + "|".join(["-" * len(h) for h in headers]) + "|\n")

            # per class
            for cls in per_class:
                row = [
                    f"{cls}",
                    f"{per_class[cls]['precision']:.3f}",
                    f"{per_class[cls]['recall']:.3f}",
                    f"{per_class[cls]['f1']:.3f}",
                ]
                f.write("| " + " | ".join(row) + " |")
                f.write("\n")

            # overall
            row = [
                "Overall",
                f"{overall['precision']:.3f}",
                f"{overall['recall']:.3f}",
                f"{overall['f1']:.3f}",
            ]
            f.write("| " + " | ".join(row) + " |")
            f.write("\n")
            f.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Save results of in a markdown file")
    parser.add_argument(
        "--results_file",
        type=str,
        help="Path to the results file (JSON format)",
    )
    args = parser.parse_args()

    results_file = Path(args.results_file)
    if not results_file.exists():
        raise FileNotFoundError(f"⚠️ Results file not found: {results_file}")

    with results_file.open("r", encoding="utf-8") as f:
        results_json = json.load(f)

    meta_data = results_json["metadata"]
    thresholds_data = results_json["thresholds"]

    date_str = datetime.now().strftime("%Y-%m-%d")
    output_md = Path(f"reports/{date_str}_{meta_data['dataset']}_eval_results.md")
    create_md_eval_report(output_md, f"Evaluation Results - {meta_data['dataset']}")

    append_eval_table(output_md, meta_data, thresholds_data)
    print(f"\nResults saved to {output_md}")


if __name__ == "__main__":
    main()
