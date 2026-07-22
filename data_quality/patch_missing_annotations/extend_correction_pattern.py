import argparse
from pathlib import Path
from typing import List, Tuple

from ner_datasets import NERSentence, load_ner_dataset_from_conll

from data_quality.patch_missing_annotations.span_tagging import (
    _find_all,
    _tag_pattern_span,
    _token_boundaries,
    _token_spans,
)


def main():
    """Extends annotations with the given corrections patterns.

    E.g. if for multiple organisations the subsequent part '... Versicherungs AG' was not captured by the annotation,
    we can add it for every annotation where this pattern follows via this script by providing the correction pattern.
    Each line contains one correction pattern, lines starting with # are ignored.
    """
    parser = argparse.ArgumentParser(
        description="Extend correction annotations by pattern"
    )

    parser.add_argument(
        "--input-dir", type=str, required=True, help="Path to data (CONLLU format)"
    )
    parser.add_argument(
        "--output-dir", type=str, required=True, help="Path to output (CONLLU format)"
    )
    parser.add_argument(
        "--corrections",
        type=str,
        required=True,
        help="Path to corrections file, correction per line",
    )
    parser.add_argument(
        "--type",
        type=str,
        required=False,
        help="The type of gold annotations we want to consider",
    )
    args = parser.parse_args()

    data = load_ner_dataset_from_conll(args.input_dir)
    corrections = Path(args.corrections).read_text(encoding="utf-8").splitlines()
    label_type = args.type

    for correction in corrections:
        if correction.startswith("#"):
            continue
        for sent in data.sentences:
            token_spans = _token_spans(sent)
            token_starts, token_ends = _token_boundaries(token_spans)
            for ps, pe in _find_all(sent.text, correction, token_starts, token_ends):
                golds_to_update = after_gold(sent, (ps, pe))
                for gold_to_update in golds_to_update:
                    if gold_to_update["type"] != label_type:
                        continue

                    # sent.labels.remove(gold_to_update)
                    new_label = {
                        "text": sent.text[gold_to_update["start"] : pe],
                        "type": gold_to_update["type"],
                        "start": gold_to_update["start"],
                        "end": pe,
                    }
                    # sent.labels.append(new_label)
                    new_labels = _tag_pattern_span(
                        sent,
                        new_label["start"],
                        new_label["end"],
                        new_label["type"],
                        True,
                        True,
                        False,
                        token_spans,
                    )
                    sent.labels = new_labels
                    print(f"Correction of {gold_to_update} --> {new_label}")

    Path(args.output_dir).write_text(data.to_conll(), encoding="utf-8")


def after_gold(sent: NERSentence, token_pos: Tuple[int, int]) -> List[dict]:
    golds = []
    for l in sent.labels:
        if l["end"] == token_pos[0] - 1:
            golds.append(l)
    return golds


if __name__ == "__main__":
    main()
