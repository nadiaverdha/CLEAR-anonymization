import argparse
import json
from pathlib import Path

import latextable
from texttable import Texttable


def load_results(results_path: Path, label: str | None = None) -> dict:
    data = json.loads(results_path.read_text())
    results = data["results_dev"]
    config = data["config"]
    best_rules = data["best_rules"]

    def pct(x):
        return f"{100 * x:.1f}"

    return {
        "setting": "",
        "class": ", ".join(config.get("selected_classes", [])),
        "f1": pct(results.get("micro_f1", 0)),
        "precision": pct(results.get("micro_precision", 0)),
        "recall": pct(results.get("micro_recall", 0)),
        "num_rules": len(data["rules"]),
    }


def build_table(rows: list[dict]) -> Texttable:
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_align(["l", "l", "r", "r", "r", "r"])
    table.set_cols_dtype(["t"] * 6)
    header = ["Setting", "Class", r"\# Rules", "P", "R", "F1"]
    data_rows = [
        [
            r["setting"],
            r["class"],
            str(r["num_rules"]),
            r["precision"],
            r["recall"],
            r["f1"],
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
