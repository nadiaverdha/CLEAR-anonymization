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
        "The threshold represents the minimum confidence score required for a "
        "predicted entity span to be considered correct.\n"
        "**Examples:**\n\n"
        "- A threshold of **1.0** means that each predicted span is considered correct "
        "only if it has **100% overlap** with the gold span.\n"
        "- A threshold of **0.5** means that each predicted span is considered correct "
        "if it has at least **50% overlap** with the gold span.\n\n"
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
        

def append_eval_table(file_path, table_title, headers, results):
    with file_path.open("a") as f:
        f.write(f"## {table_title}\n\n")
        f.write("| " + " | ".join(headers) + " |\n")
        f.write("|" + "|".join(["-" * len(h) for h in headers]) + "|\n")

        for result in results:
            f.write("| " + " | ".join(map(str, result)) + " |\n")
        f.write("\n")
