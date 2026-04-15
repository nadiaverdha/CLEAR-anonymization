import argparse
import json
import zipfile
from dataclasses import dataclass
from os.path import commonprefix
from pathlib import Path
from typing import List

import spacy
from tuw_nlp.text.patterns.de import ABBREV
from tuw_nlp.text.pipeline import CustomStanzaPipeline
from tuw_nlp.text.segmentation import SsplitFixer

from clear_anonymization.ner_datasets.ner_dataset import NERData, NERSample
from clear_anonymization.preprocess.util import (
    MISC,
    ROMAN_NUMBERING,
    TITLES,
    TOB,
    _is_err_patch,
)

ABBREV.extend(TITLES)
ABBREV.extend(TOB)
ABBREV.extend(MISC)
ABBREV.extend(ROMAN_NUMBERING)

# monkey patch for is_err
SsplitFixer.is_err = _is_err_patch

MAX_CHUNK_SIZE = 1000000

TUW_NLP = True

nlp = spacy.blank("de") if not TUW_NLP else CustomStanzaPipeline()
if not TUW_NLP:
    nlp.add_pipe("sentencizer")


@dataclass
class Sent:
    start_char: int
    end_char: int
    text: str


def preprocess_text(text):
    text = text.replace("\xa0", " ")
    return text


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


def collect_annos_in_sentence(annos, sent):
    collected = []
    for anno in annos:
        anno = dict(anno)
        if anno["start"] >= sent.start_char and anno["end"] <= sent.end_char:
            anno["start"] = anno["start"] - sent.start_char
            anno["end"] = anno["end"] - sent.start_char
            collected.append(anno)
    return collected


def iter_sentences_stanza(full_text: str):
    sents = nlp.tokenizer(full_text).sentences
    for sent in sents:
        yield Sent(sent.tokens[0].start_char, sent.tokens[-1].end_char, sent.text)


def iter_sentences_spacy(full_text: str):
    start = 0
    while start < len(full_text):
        end = min(start + MAX_CHUNK_SIZE, len(full_text))
        if end < len(full_text):
            snap = full_text.rfind("\n", start, end)
            if snap == -1:
                snap = full_text.rfind(".", start, end)
            if snap == -1:
                snap = full_text.rfind(" ", start, end)
            if snap != -1 and snap > start + MAX_CHUNK_SIZE * 0.8:
                end = snap
        chunk = full_text[start:end]

        doc = nlp(chunk)
        for sent in doc.sents:
            yield Sent(sent.start_char + start, sent.end_char + start, sent.text)
        start = end


def validate_docu_annotations(folder, samples: List[NERSample], verbose=False):
    for sample in samples:
        text = sample.text
        labels = sample.labels
        all_ok = True
        for ann in labels:
            start = ann["start"]
            end = ann["end"]
            actual = text[start:end]
            expected = ann["text"]
            if actual != expected:
                all_ok = False

            if verbose:
                print(f"{start}:{end}  '{actual}'  ---->  '{expected}'")
                if actual != expected:
                    print("❌ incorrect")
            # else:
            #  print("✅ correct ")

        if not verbose:
            # if all_ok:
            # print("✅ Annotation check ok! ")
            if not all_ok:
                print("❌ Annotation check failed!")


def process_folder(
    zip_path,
    folder_name,
    split,
    verbose,
) -> List[NERSample]:
    pages = []
    annotations = None
    with zipfile.ZipFile(zip_path, "r") as archive:
        folder_files = [f for f in archive.namelist() if folder_name in f]
        txt_files = sorted(
            [f for f in folder_files if f.endswith(".txt")],
            key=lambda p: int(Path(p).stem),
        )

        for txt_file in txt_files:
            with archive.open(txt_file) as f:
                content = f.read().decode("utf-8-sig")

                pages.append(preprocess_text(content))

        try:
            ann_file = [f for f in folder_files if f.endswith(".json")][0]
            if ann_file:
                with archive.open(ann_file) as f:
                    annotations = json.loads(f.read().decode("utf-8"))
            else:
                print("empty", folder_name)
            annotations = sorted(annotations, key=lambda x: x["startPage"])
        except:
            annotations = None

    samples = create_sample(
        folder_name,
        pages,
        annotations,
        split,
    )
    # print(samples)

    validate_docu_annotations(folder_name, samples, verbose)

    return samples


def create_sample(
    doc_id,
    pages,
    annotations,
    split,
) -> List[NERSample]:
    full_text = "".join(pages)

    page_offsets = []
    current_offset = 0
    for p in pages:
        page_offsets.append(current_offset)
        current_offset += len(p)

    labels = []
    if annotations:
        for ann in annotations:
            start = page_offsets[ann["startPage"]] + ann["pageRelativeStart"]
            end = page_offsets[ann["endPage"]] + ann["pageRelativeEnd"]
            labels.append(
                {"text": ann["text"], "start": start, "end": end, "type": ann["label"]}
            )

    iter_func = (
        iter_sentences_stanza(full_text) if TUW_NLP else iter_sentences_spacy(full_text)
    )
    ner_samples_sents = [
        NERSample(
            f"{doc_id}_s{i}",
            sent.text,
            split,
            collect_annos_in_sentence(labels, sent) if labels else [],
            None,
        )
        for i, sent in enumerate(iter_func)
    ]
    return [NERSample(doc_id, full_text, split, labels, sentences=ner_samples_sents)]


def main():
    parser = argparse.ArgumentParser(description="Load a dataset from M2N zip file ")
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path where to load the zip file from",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        help="Path where to save the JSON file",
    )

    parser.add_argument(
        "--split",
        type=str,
        help="Give information whether data is from train/validation/test split",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Whether to show detailed annotations check.",
    )

    args = parser.parse_args()
    ner_data = NERData(samples=[])
    folders = list_folders(args.input_dir)
    for folder in folders:
        # if folder == "deanon_BFG_TRAIN/100833.1":
        print(f"==== Document {folder} ====")

        sample = process_folder(args.input_dir, folder, args.split, args.verbose)

        ner_data.samples.extend(sample)
        print("-----------------")
    output_path = Path(args.output_dir)
    output_path.write_text(json.dumps(ner_data.to_json(), indent=4))


if __name__ == "__main__":
    main()
