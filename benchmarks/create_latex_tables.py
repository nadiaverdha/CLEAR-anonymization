import argparse
import json
from pathlib import Path

import latextable
from texttable import Texttable


def load_results(results_path: Path) -> dict:
    data = json.loads(results_path.read_text())
    results = data.get("results", {})
    config = data.get("config", {})
    return {
        "train_data": config.get("train_name", "Unknown"),
        "test_data": config.get("test_name", "Unknown"),
        "transfer_data": config.get("transfer_name", "null"),
        "f1": f"{results.get('micro_f1', 0):.1%}".replace("%", r"\%"),
        "precision": f"{results.get('micro_precision', 0):.1%}".replace("%", r"\%"),
        "recall": f"{results.get('micro_recall', 0):.1%}".replace("%", r"\%"),
        "num_rules": results.get("num_rules", 0),
        "max_rules": config.get("max_rules", 0),
        "iterations": config.get("max_iterations", 0),
        "model": config.get("model", "Unknown"),
    }


def build_table(rows: list[dict]) -> Texttable:
    has_transfer = any(r["transfer_data"] not in (None, "null", "") for r in rows)

    table = Texttable()
    table.set_deco(Texttable.HEADER)

    if has_transfer:
        table.set_cols_align(["l", "l", "l", "l", "r", "r", "r", "r"])
        table.set_cols_dtype(["t", "t", "t", "t", "i", "t", "t", "t"])
        header = [
            "Train Data",
            "Additional Train Data",
            "Test Data",
            "Model",
            r"\# Rules",
            "F1",
            "Precision",
            "Recall",
        ]
        data_rows = [
            [
                r["train_data"],
                r["transfer_data"],
                r["test_data"],
                r["model"],
                r["num_rules"],
                r["f1"],
                r["precision"],
                r["recall"],
            ]
            for r in rows
        ]
    else:
        table.set_cols_align(["l", "l", "l", "r", "r", "r", "r"])
        table.set_cols_dtype(["t", "t", "t", "i", "t", "t", "t"])
        header = [
            "Train Data",
            "Test Data",
            "Model",
            r"\# Rules",
            "F1",
            "Precision",
            "Recall",
        ]
        data_rows = [
            [
                r["train_data"],
                r["test_data"],
                r["model"],
                r["num_rules"],
                r["f1"],
                r["precision"],
                r["recall"],
            ]
            for r in rows
        ]

    table.add_rows([header] + data_rows)
    return table


def main():
    parser = argparse.ArgumentParser(description="Create LaTeX tables from results")
    parser.add_argument(
        "--results-files",
        type=Path,
        nargs="+",
        help="One or more JSON result files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file for LaTeX table (optional)",
    )

    parser.add_argument(
        "--caption", default="Benchmark Results", help="LaTeX table caption"
    )

    args = parser.parse_args()

    rows = [load_results(p) for p in args.results_files]

    table = build_table(rows)
    latex_code = latextable.draw_latex(
        table, caption=args.caption, label="tab:results", position="h"
    )
    latex_code = latex_code.replace(r"\begin{table}", r"\begin{table*}").replace(
        r"\end{table}", r"\end{table*}"
    )

    if args.output:
        args.output.write_text(latex_code)
        print(f"LaTeX table saved to {args.output}")
    else:
        print(latex_code)


if __name__ == "__main__":
    main()
