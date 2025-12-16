from pathlib import Path
from datetime import datetime
from py_markdown_table.markdown_table import markdown_table


def create_md_eval_report(
    file_path: str | Path, dataset: str, title: str = "Evaluation Results"
):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w") as f:
        f.write(f"Generated on: {datetime.now().isoformat()}\n\n")
        f.write(f"# {title} - {dataset} data\n\n")


def append_eval_table(file_path, markdown:markdown_table):
    with file_path.open("a") as f:
        f.write(markdown)


    return append_eval_table
