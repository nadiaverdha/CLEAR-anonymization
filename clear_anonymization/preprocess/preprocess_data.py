import argparse
import json
import time
import zipfile
from dataclasses import dataclass
from os.path import commonprefix
from pathlib import Path
from typing import List

import spacy
from stanza.models.common.doc import Document
from stanza.utils.conll import CoNLL
from tuw_nlp.text.patterns.de import ABBREV
from tuw_nlp.text.pipeline import CachedStanzaPipeline, CustomStanzaPipeline
from tuw_nlp.text.segmentation import SsplitFixer

from clear_anonymization.ner_datasets import NERData, NERSample, NERSentence
from clear_anonymization.preprocess.util import (
    MISC,
    ROMAN_NUMBERING,
    TITLES,
    TOB,
    _is_err_patch,
    preprocess_text,
    split_test,
    validate_docu_annotations,
    validate_sentence_annotations,
)

ABBREV.extend(TITLES)
ABBREV.extend(TOB)
ABBREV.extend(MISC)
ABBREV.extend(ROMAN_NUMBERING)


# monkey patch for is_err
SsplitFixer.is_err = _is_err_patch

MAX_CHUNK_SIZE = 1000000

TUW_NLP = True

nlp = (
    spacy.blank("de")
    if not TUW_NLP
    else CustomStanzaPipeline(lang="de", processors="tokenize,pos,lemma")
)

if not TUW_NLP:
    nlp.add_pipe("sentencizer")


@dataclass
class Sent:
    start_char: int
    end_char: int
    text: str


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


def annotate_sentence(full_text: str, labels: list, doc_id: str, split: str):

    tokenized = nlp.tokenizer(full_text)

    ner_sentences = []
    sent_comments = []
    for i, tok_sent in enumerate(tokenized.sentences):
        sent_start = tok_sent.tokens[0].start_char
        sent_end = tok_sent.tokens[-1].end_char
        analysed = nlp.additional(tok_sent.text)
        ann_sent = analysed.sentences[0]
        sent_labels = (
            collect_annos_in_sentence(labels, Sent(sent_start, sent_end, tok_sent.text))
            if labels
            else []
        )

        token_dicts = []

        for token in ann_sent.tokens:
            tag = assign_bio_tag(token, sent_labels)
            doc_start = token.start_char + sent_start
            doc_end = token.end_char + sent_start
            token_dicts.append(
                {
                    "id": token.id,
                    "text": token.text,
                    "lemma": token.words[0].lemma,
                    "upos": token.words[0].upos,
                    "xpos": token.words[0].xpos,
                    "feats": token.words[0].feats,
                    "misc": f"NER={tag}|DocStart={doc_start}|DocEnd={doc_end}|SentStart={token.start_char}|SentEnd={token.end_char}",
                }
            )
        ner_sentences.append(
            NERSentence(
                sent_id=f"{doc_id}_{i}",
                text=tok_sent.text,
                tokens=token_dicts,
                labels=sent_labels,
            )
        )
    return NERSample(
        doc_id=doc_id,
        split=split,
        text=full_text,
        labels=labels,
        sentences=ner_sentences,
    )


def assign_bio_tag(token, labels, offset=0) -> str:
    start = token.start_char - offset
    end = token.end_char - offset
    for label in labels:
        if start < label["end"] and end > label["start"]:
            if start <= label["start"]:
                return f"B-{label['type']}"
            return f"I-{label['type']}"
    return "O"


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


def process_folder(zip_path, folder_name, split, verbose):
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
                pages.append(preprocess_text(f.read().decode("utf-8-sig")))
        try:
            ann_file = [f for f in folder_files if f.endswith(".json")][0]
            with archive.open(ann_file) as f:
                annotations = sorted(
                    json.loads(f.read().decode("utf-8")),
                    key=lambda x: x["startPage"],
                )
        except:
            annotations = None

    annotated, labels, full_text = create_sample(
        folder_name, pages, annotations, split, verbose
    )
    # validate_docu_annotations(full_text, labels, verbose)

    return annotated


def create_sample(doc_id, pages, annotations, split, verbose):
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

    annotated = annotate_sentence(full_text, labels, doc_id, split)
    validate_sentence_annotations(annotated, verbose)
    return annotated, labels, full_text


def main():
    parser = argparse.ArgumentParser(description="Load a dataset from M2N zip file ")
    parser.add_argument(
        "--input-path",
        type=str,
        help="Path where to load the zip file from",
    )

    parser.add_argument(
        "--output-path",
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
    folders = list_folders(args.input_path)
    all_samples = []
    output_path = Path(args.output_path)

    for folder in folders:
        print(f"==== Document {folder} ====")
        sample = process_folder(args.input_dir, folder, args.split, args.verbose)
        all_samples.append(sample)
    data = NERData(all_samples)
    print("Writing to:", output_path)
    output_path.write_text(data.to_conll())


if __name__ == "__main__":
    main()
