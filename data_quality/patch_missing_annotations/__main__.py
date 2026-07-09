import argparse
import json
from pathlib import Path

from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from data_quality.patch_missing_annotations.apply_corrections import _apply_corrections
from data_quality.patch_missing_annotations.apply_extend_prev import _apply_extend_prev
from data_quality.patch_missing_annotations.apply_patterns import _apply_patterns
from data_quality.patch_missing_annotations.apply_rules import _apply_rule_predictions
from data_quality.patch_missing_annotations.changelog import _append_changelog


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Markdown report from a saved rules JSON and test data"
    )
    parser.add_argument(
        "--rules-json",
        type=str,
        nargs="*",
        default=[],
        help="Path to results JSON containing rules",
    )
    parser.add_argument(
        "--rule-id",
        type=str,
        nargs="*",
        default=[],
        help="Apply only rules with these IDs (from --rules-json)",
    )
    parser.add_argument(
        "--input-dir", type=str, required=True, help="Path to data (CONLLU format)"
    )
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument(
        "--dataset-name",
        type=str,
        required=True,
        help="Dataset name, used to pick the changelog file: data_quality/<dataset-name>/CHANGELOG.md",
    )
    parser.add_argument(
        "--patterns",
        type=str,
        nargs="*",
        default=[],
        help="Text patterns to annotate, format: 'text:type' e.g. 'Bezirksgericht Wien:organisation'",
    )
    parser.add_argument(
        "--corrections",
        type=str,
        nargs="*",
        default=[],
        help="Correct existing annotations by sent_id, format: 'sent_id:text:new_type' (use new_type=O to remove)",
    )
    parser.add_argument(
        "--extend-prev",
        type=str,
        nargs="*",
        default=[],
        help="Tag a word and its preceding token as the same entity, format: 'sent_id:text:type'",
    )
    parser.add_argument(
        "--patterns-file",
        default=None,
        help="JSON file with ['text:type', ...] patterns",
    )
    args = parser.parse_args()

    data = load_ner_dataset_from_conll(args.input_dir)
    if args.patterns_file:
        extra = json.loads(Path(args.patterns_file).read_text())
        args.patterns = args.patterns + extra

    rules, rule_changes = _apply_rule_predictions(data, args.rules_json, args.rule_id)
    pattern_changes = _apply_patterns(data, args.patterns)

    sent_index = {sent.sent_id: sent for s in data.samples for sent in s.sentences}
    correction_changes = _apply_corrections(data, sent_index, args.corrections)
    extend_prev_changes = _apply_extend_prev(data, sent_index, args.extend_prev)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(data.to_conll(), encoding="utf-8")
    print(f"Written to {out_path}")

    _append_changelog(
        args,
        out_path,
        pattern_changes,
        correction_changes,
        extend_prev_changes,
        rules,
        rule_changes,
    )


if __name__ == "__main__":
    main()
