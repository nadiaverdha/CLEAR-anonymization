""" "
python clear_anonymization/preprocess/preprocess_relations.py /
   --input-path /share/nverdha/data/findok/curated-docs-admin-2026-03-31-093327.zip /
   --conllu-path /share/nverdha/data/findok/findok_train_corrected.conllu /
   --output-path /share/nverdha/data/findok/findok_including_relations.conllu
"""

import argparse
import json
import zipfile
from os.path import commonprefix
from pathlib import Path

from stanza.utils.conll import CoNLL

from clear_anonymization.ner_datasets import NERData

rellabel_corrections = {
    "149868.1": "legal_representation_of",
    "149280.1": "address_of",
    "149768.1": "address_of",
}


def list_folders(zip_path):
    with zipfile.ZipFile(zip_path, "r") as archive:
        folders = set()
        for file_name in archive.namelist():
            if "/" in file_name:
                folder = "/".join(file_name.split("/")[:-1])
                folders.add(folder)
        prefix = commonprefix(list(folders))
        # filter out root folder
        if prefix in folders:
            folders.remove(prefix)
        return sorted(folders)


def process_folder(zip_path, folder_name, split, error_file, verbose):
    pages = []
    annotations = None
    with zipfile.ZipFile(zip_path, "r") as archive:
        folder_files = [f for f in archive.namelist() if folder_name in f]
        try:
            ann_file = [f for f in folder_files if f.endswith(".json")][0]
            with archive.open(ann_file) as f:
                features = json.loads(f.read().decode("utf-8"))["%FEATURE_STRUCTURES"]
                entities = {
                    fs["%ID"]: fs
                    for fs in features
                    if fs["%TYPE"] == "clear.NamedEntity"
                }

                relations = [fs for fs in features if fs["%TYPE"] == "clear.Relation"]
        except Exception:
            entities = None
            relations = None

    return entities, relations


def get_doc_id_from_folder(folder_name):
    doc_id = folder_name.split("/")[-1].removesuffix(".json")
    return doc_id


def get_doc_span(token):
    misc = dict(p.split("=", 1) for p in token["misc"].split("|") if "=" in p)
    return (
        int(misc["DocStart"]) if "DocStart" in misc else None,
        int(misc["DocEnd"]) if "DocEnd" in misc else None,
    )


def find_anchor_token(tokens, begin):
    for token in tokens:
        start, end = get_doc_span(token)
        if start is not None and end is not None and start <= begin < end:
            if begin != start:
                print(
                    f"  ⚠️  non-exact anchor match: begin={begin} → token span=[{start},{end})"
                )
            return token
    return None


def add_relation_misc(token, entry):
    misc = token.get("misc", "")
    parts = misc.split("|") if misc else []
    for i, p in enumerate(parts):
        if p.startswith("Rel="):
            existing = p.split("=", 1)[1]
            parts[i] = f"Rel={existing};{entry}"
            break
    else:
        parts.append(f"Rel={entry}")
    token["misc"] = "|".join(parts)


def add_relations(sample, entities, relations, doc_id):
    tokens = [tok for sent in sample.sentences for tok in sent.tokens]
    n_attached = 0
    unmatched = []
    for relation in relations:
        print(f"Processing relation {relation['%ID']} in doc {doc_id}")

        rel_label = relation.get("relLabel") or rellabel_corrections.get(doc_id)
        if rel_label is None:
            print(
                f"⚠️ Relation {relation['%ID']} in doc {doc_id} has no relLabel, skipping"
            )

            unmatched.append(f"{doc_id}: relation {relation['%ID']} missing relLabel")
            continue
        governor = entities.get(relation["@Governor"])
        dependent = entities.get(relation["@Dependent"])
        if not governor or not dependent:
            unmatched.append(
                f"{doc_id}: relation {relation['%ID']} references a missing entity"
            )
            continue
        gov_token = find_anchor_token(tokens, governor["begin"])
        dep_token = find_anchor_token(tokens, dependent["begin"])
        if not gov_token or not dep_token:

            def doc_span(tok):
                misc = dict(p.split("=", 1) for p in tok["misc"].split("|") if "=" in p)
                return int(misc.get("DocStart", -1)), int(misc.get("DocEnd", -1))

            spans = [doc_span(t) for t in tokens]
            doc_min = min(s for s, _ in spans)
            doc_max = max(e for _, e in spans)
            print(
                f"{doc_id} relation {relation['%ID']}: "
                f"gov_begin={governor['begin']} (found={gov_token is not None}) "
                f"dep_begin={dependent['begin']} (found={dep_token is not None}) "
                f"| doc token span=[{doc_min}, {doc_max}]"
            )
            unmatched.append(
                f"{doc_id}: relation {relation['%ID']} references a missing token"
            )
            continue
        add_relation_misc(gov_token, f"{rel_label}:governor:{dependent['begin']}")
        add_relation_misc(dep_token, f"{rel_label}:dependent:{governor['begin']}")
        n_attached += 1

    return n_attached, unmatched


def normalize_doc_id(doc_id):
    return doc_id.split("/")[-1]


def main():
    parser = argparse.ArgumentParser(description="Load a dataset from M2N zip file ")
    parser.add_argument(
        "--input-path",
        type=str,
        nargs="+",
        help="Path(s) to zip file(s)",
    )
    parser.add_argument(
        "--conllu-path",
        type=str,
        help="Path to the CoNLL-U file",
    )

    parser.add_argument(
        "--output-path",
        type=str,
        help="Path where to save the CoNLL-U file with relations attached",
        default="data/ner_dataset_with_relations.conllu",
    )

    parser.add_argument(
        "--split",
        type=str,
        help="Give information whether data is from train/validation/test split",
        default="train",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Whether to show detailed annotations check.",
    )

    args = parser.parse_args()
    ner_data = NERData.from_conll(Path(args.conllu_path).read_text())
    samples_by_doc_id = {normalize_doc_id(s.doc_id): s for s in ner_data.samples}

    total_attached = 0
    total_unmatched = []
    doc_ids_in_zip = set()

    for zip_path in args.input_path:
        folders = list_folders(zip_path)
        for folder in folders:
            doc_id = get_doc_id_from_folder(folder)
            sample = samples_by_doc_id.get(doc_id)

            if not sample:
                print(f"❌ No sample found for {doc_id}")
                continue
            doc_ids_in_zip.add(doc_id)
            entities, relations = process_folder(
                zip_path, folder, args.split, None, args.verbose
            )
            if not relations:
                print(f"❌ No relations found for {doc_id}")
                continue
            n_attached, unmatched = add_relations(sample, entities, relations, doc_id)
            total_attached += n_attached
            total_unmatched += unmatched

    print(
        f"✅\n{total_attached} relations attached in total, {len(total_unmatched)} unmatched relations"
    )
    ner_data.samples = [
        s for s in ner_data.samples if normalize_doc_id(s.doc_id) in doc_ids_in_zip
    ]
    Path(args.output_path).write_text(ner_data.to_conll())
    print(f"Wrote {args.output_path}")


if __name__ == "__main__":
    main()
