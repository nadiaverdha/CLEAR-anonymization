import os

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import argparse
import json
import zipfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from os.path import commonprefix
from pathlib import Path

from tqdm import tqdm
from tuw_nlp.text.patterns.de import ABBREV
from tuw_nlp.text.segmentation import SsplitFixer

from clear_anonymization.preprocess.util import (
    MISC,
    ROMAN_NUMBERING,
    TITLES,
    TOB,
    _is_err_patch,
    assign_bio_tag,
    preprocess_text,
)

_worker_nlp = None


def _init_worker():
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    import torch
    from tuw_nlp.text.pipeline import CustomStanzaPipeline

    torch.set_num_threads(1)
    global _worker_nlp
    ABBREV.extend(TITLES)
    ABBREV.extend(TOB)
    ABBREV.extend(MISC)
    ABBREV.extend(ROMAN_NUMBERING)
    SsplitFixer.is_err = _is_err_patch
    _worker_nlp = CustomStanzaPipeline(lang="de", processors="tokenize,pos,lemma")


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


def annotate_sentence(full_text, labels, doc_id, split):
    from clear_anonymization.ner_datasets import NERSample, NERSentence

    nlp = _worker_nlp
    tokenized = nlp.tokenizer(full_text)
    ner_sentences = []

    for i, tok_sent in enumerate(tokenized.sentences):
        sent_start = tok_sent.tokens[0].start_char
        sent_end = tok_sent.tokens[-1].end_char
        analysed = nlp.additional(tok_sent.text)
        sent_labels = (
            collect_annos_in_sentence(labels, Sent(sent_start, sent_end, tok_sent.text))
            if labels
            else []
        )

        token_dicts = []
        tok_offset = 0

        for ann_sent in analysed.sentences:
            for token in ann_sent.tokens:
                tag = assign_bio_tag(token, sent_labels)
                doc_start = token.start_char + sent_start
                doc_end = token.end_char + sent_start
                token_dicts.append(
                    {
                        "id": (tok_offset + token.id[0],),
                        "text": token.text,
                        "lemma": token.words[0].lemma,
                        "upos": token.words[0].upos,
                        "xpos": token.words[0].xpos,
                        "feats": token.words[0].feats,
                        "misc": f"NER={tag}|DocStart={doc_start}|DocEnd={doc_end}|SentStart={token.start_char}|SentEnd={token.end_char}",
                    }
                )
            tok_offset += len(ann_sent.tokens)

        ner_sentences.append(
            NERSentence(
                sent_id=f"{doc_id}_{i}",
                text=tok_sent.text,
                tokens=token_dicts,
                labels=sent_labels,
            )
        )

    from clear_anonymization.ner_datasets import NERSample

    return NERSample(
        doc_id=doc_id,
        split=split,
        text=full_text,
        labels=labels,
        sentences=ner_sentences,
    )


def _collect_errors(sample, verbose=False):
    from clear_anonymization.ner_datasets.util import recreate_sent_labels_from_tokens

    errors = []
    for sent in sample.sentences:
        labels = recreate_sent_labels_from_tokens(sent.tokens, sent.text)
        for label in sent.labels or []:
            matched = any(
                s["start"] == label["start"] and s["end"] == label["end"]
                for s in labels
            )
            if not matched:
                msg = f"{sample.doc_id} | {sent.sent_id} | ❌ '{label['text']}' ({label['start']}:{label['end']})"
                errors.append(msg)
                if verbose:
                    print(
                        f"❌ missed: '{label['text']}' ({label['start']}:{label['end']})"
                    )
    return errors


def _process_folder_worker(args):
    zip_path, folder_name, split, error_file, verbose = args
    print(f"  Worker starting: {folder_name}", flush=True)
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
        except Exception:
            annotations = None

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

    sample = annotate_sentence(full_text, labels, folder_name, split)
    errors = _collect_errors(sample, verbose)
    print(f"  Worker done: {folder_name}", flush=True)
    return folder_name, sample.to_conll(), errors


def main():
    import multiprocessing

    multiprocessing.set_start_method("spawn", force=True)
    parser = argparse.ArgumentParser(description="Parallel CoNLL-U preprocessing")
    parser.add_argument("--input-path", type=str, nargs="+", required=True)
    parser.add_argument("--output-path", type=str, required=True)
    parser.add_argument("--split", type=str, required=True)
    parser.add_argument("--num-workers", type=int, default=2)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    output_path = Path(args.output_path)
    progress_path = output_path.with_suffix(".progress")
    error_path = output_path.with_suffix(".errors")

    processed = set()
    if progress_path.exists():
        with open(progress_path) as f:
            processed = set(line.strip() for line in f)
    print(f"Resuming: {len(processed)} already processed")

    tasks = [
        (zip_path, folder, args.split, error_path, args.verbose)
        for zip_path in args.input_path
        for folder in list_folders(zip_path)
        if folder not in processed
    ]
    print(f"Processing {len(tasks)} documents with {args.num_workers} workers")

    with (
        open(output_path, "a", encoding="utf-8") as out_f,
        open(progress_path, "a", encoding="utf-8") as prog_f,
        ProcessPoolExecutor(
            max_workers=args.num_workers, initializer=_init_worker
        ) as pool,
    ):
        futures = {pool.submit(_process_folder_worker, t): t[1] for t in tasks}
        for future in tqdm(as_completed(futures), total=len(tasks), desc="Processing"):
            folder = futures[future]
            try:
                folder, conll_str, errors = future.result()
                out_f.write(conll_str)
                out_f.write("\n")
                prog_f.write(folder + "\n")
                prog_f.flush()
                out_f.flush()
                if errors:
                    with open(error_path, "a", encoding="utf-8") as err_f:
                        for e in errors:
                            err_f.write(e + "\n")
            except Exception as e:
                print(f"❌ Failed on {folder}: {e}")


if __name__ == "__main__":
    main()
