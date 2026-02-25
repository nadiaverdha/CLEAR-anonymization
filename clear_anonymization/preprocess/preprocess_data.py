import argparse
import json
import logging
import re
import string
import unicodedata
import zipfile
from pathlib import Path
from typing import List
import spacy
from tuw_nlp.text.pipeline import CustomStanzaPipeline
from tuw_nlp.text.patterns.de import ABBREV
from dataclasses import dataclass
from os.path import commonprefix

from datasets import load_dataset

from clear_anonymization.ner_datasets.ner_dataset import NERData, NERDataset, NERSample
from clear_anonymization.preprocess.util import TITLES

ABBREV.extend(TITLES)

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

def validate_docu_annotations(folder, samples:List[NERSample], verbose=False):
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

def process_folder(zip_path, folder_name, split, verbose, sentences: bool) -> List[NERSample]:
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

    samples = create_sample(pages, annotations, split, sentences)

    validate_docu_annotations(folder_name, samples, verbose)

    return samples


def create_sample(pages, annotations, split, sentences:bool) -> List[NERSample]:
    full_text = "".join(pages)
    page_offsets = []

    current_offset = 0
    for i, p in enumerate(pages):
        page_offsets.append(current_offset)
        current_offset += len(p)

    labels = []
    if not annotations:
        return [NERSample(full_text, split, labels)]
    if not sentences:
        for ann in annotations:
            startpage = ann["startPage"]
            endpage = ann["endPage"]

            start = page_offsets[startpage] + ann["pageRelativeStart"]
            end = page_offsets[endpage] + ann["pageRelativeEnd"]
            actual = full_text[start:end]
            labels.append(
                {
                    "text": ann["text"],
                    "start": start,
                    "end": end,
                    "type": ann["label"],
                }
            )
        return [NERSample(full_text, split, labels)]
    else:
        # multiple annotations: [(start, end, type), ...]
        # collect annotations per sentence and combine to NERSample
        # remove sentence offset from start/end
        converted_annos = []
        for ann in annotations:
            startpage = ann["startPage"]
            endpage = ann["endPage"]

            start = page_offsets[startpage] + ann["pageRelativeStart"]
            end = page_offsets[endpage] + ann["pageRelativeEnd"]
            actual = full_text[start:end]
            converted_annos.append({"text": ann["text"], "start": start, "end": end, "class": ann["label"]})

        ner_samples = []
        iter_func = iter_sentences_spacy(full_text) if not TUW_NLP else iter_sentences_stanza(full_text)
        for sent in iter_func:
            relevant_annos = collect_annos_in_sentence(converted_annos, sent)
            if len(relevant_annos) != 0:
                ner_samples.append(NERSample(sent.text, split, relevant_annos))
        return ner_samples

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

    parser.add_argument(
        "--sentences",
        action="store_true",
        default=False,
        help="Whether to split the document text into sentences."
    )
    args = parser.parse_args()
    ner_data = NERData(samples=[])
    folders = list_folders(args.input_dir)
    for folder in folders:
        print(f"==== Document {folder} ====")

        sample = process_folder(args.input_dir, folder, args.split, args.verbose, args.sentences)

        ner_data.samples.extend(sample)
        print("-----------------")
    output_path = Path(args.output_dir)
    output_path.write_text(json.dumps(ner_data.to_json(), indent=4))


if __name__ == "__main__":
    main()
