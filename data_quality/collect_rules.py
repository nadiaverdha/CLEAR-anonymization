"""Collect rules from a hand-picked list of experiment folders.

Usage
-----
python data_quality/collect_rules.py \
    --folders-file /home/nadia.verdha/CLEAR-anonymization/data_quality/findok/rules/organisation_experiments.txt \
    --classes organisation \
    --include-provenance \
    --output data_quality/findok/rules/organisation_rules.json

organisation_experiments.txt is a plain text file, one experiment folder per line
(blank lines and lines starting with # are ignored), e.g.:

    reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-15
    reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-21_v1
"""

import argparse
import json
import subprocess
from pathlib import Path

import yaml


def get_repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(result.stdout.strip())


def get_git_tracked_files(repo_root: Path) -> set[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )
    return {(repo_root / line).resolve() for line in result.stdout.splitlines()}


def read_folder_list(folders_file: Path) -> list[Path]:
    folders = []
    for line in folders_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            folders.append(Path(line))
    return folders


def load_config(config_path: Path) -> dict:
    with config_path.open() as f:
        return yaml.safe_load(f)


def _try_load(path: Path, loader):
    try:
        return loader(path)
    except Exception as e:
        print(f"  [skip] could not read {path}: {e}")
        return None


def rule_matches_classes(rule: dict, classes: list[str] | None) -> bool:
    if not classes:
        return True
    template = str(rule.get("output_template") or "").lower()
    name = str(rule.get("name") or "").lower()
    return any(c.lower() in template or c.lower() in name for c in classes)


def collect_rules(
    folders: list[Path],
    classes: list[str] | None = None,
    git_tracked_only: bool = True,
    dataset_name: str | None = None,
) -> tuple[list[dict], list[dict]]:
    seen_content: set[str] = set()
    rules: list[dict] = []
    provenance: list[dict] = []
    tracked_files = get_git_tracked_files(get_repo_root()) if git_tracked_only else None

    for folder in folders:
        config_path = folder / "config.yaml"
        if not config_path.exists():
            print(f"  [skip] no config.yaml in {folder}")
            continue

        if tracked_files is not None and config_path.resolve() not in tracked_files:
            print(f"  [skip] {config_path} is not tracked in git")
            continue

        config = _try_load(config_path, load_config)
        if config is None:
            continue

        output_file = config.get("output")
        if not output_file:
            print(f"  [skip] {config_path} has no 'output' field")
            continue

        if dataset_name is not None:
            expected_output_file = f"results_{dataset_name}.json"
            if output_file != expected_output_file:
                print(
                    f"  [skip] {config_path} has output '{output_file}', "
                    f"expected '{expected_output_file}'"
                )
                continue

        results_path = config_path.parent / output_file
        if not results_path.exists():
            print(f"  [skip] {results_path} does not exist")
            continue

        if tracked_files is not None and results_path.resolve() not in tracked_files:
            print(f"  [skip] {results_path} is not tracked in git")
            continue

        results = _try_load(results_path, lambda p: json.loads(p.read_text()))
        if results is None:
            continue

        run_rules = results.get("rules", [])
        if not run_rules:
            print(f"  [skip] {results_path} has no rules")
            continue

        new_count = 0
        for rule in run_rules:
            if not rule_matches_classes(rule, classes):
                continue
            key = rule.get("content", "")
            if key in seen_content:
                continue
            seen_content.add(key)
            rules.append(rule)
            new_count += 1

        provenance.append(
            {
                "config": str(config_path),
                "results": str(results_path),
                "total_rules_in_run": len(run_rules),
                "new_unique_rules_added": new_count,
            }
        )
        print(
            f"  {config_path.parent.name}: {len(run_rules)} rules "
            f"({new_count} new unique) — {results_path.name}"
        )

    return rules, provenance


def main():
    parser = argparse.ArgumentParser(
        description="Collect rules from a hand-picked list of experiment folders."
    )
    parser.add_argument(
        "--folders-file",
        type=Path,
        required=True,
        help="Text file listing experiment folder paths, one per line (# for comments)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output JSON file to save collected rules",
    )
    parser.add_argument(
        "--classes",
        type=str,
        nargs="+",
        default=None,
        help="Only collect rules for these entity classes, e.g. --classes organisation person",
    )
    parser.add_argument(
        "--dataset-name",
        type=str,
        default=None,
        help="If given, only collect from experiments whose output is results_<dataset-name>.json",
    )
    parser.add_argument(
        "--include-provenance",
        action="store_true",
        help="Also save a provenance log alongside the output file",
    )
    args = parser.parse_args()

    if not args.folders_file.exists():
        parser.error(f"Folders file not found: {args.folders_file}")

    folders = read_folder_list(args.folders_file)
    print(f"Loaded {len(folders)} folder(s) from {args.folders_file}")
    if args.classes:
        print(f"  classes filter: {args.classes}")
    if args.dataset_name:
        print(f"  dataset-name filter: {args.dataset_name}")
    print()

    rules, provenance = collect_rules(
        folders, args.classes, dataset_name=args.dataset_name
    )

    print(f"\nTotal unique rules collected: {len(rules)}")
    print(f"From {len(provenance)} experiment(s)")

    output = {"rules": rules}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Saved to: {args.output}")

    if args.include_provenance:
        prov_path = args.output.with_suffix(".provenance.json")
        prov_path.write_text(json.dumps(provenance, indent=2, ensure_ascii=False))
        print(f"Provenance saved to: {prov_path}")


if __name__ == "__main__":
    main()
