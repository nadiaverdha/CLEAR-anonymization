#!/usr/bin/env python3
"""
convert_conllu_to_webanno_tsv_multi.py (TSV 3.3 VERSION)

Converts CoNLL-U format with multiple documents to WebAnno TSV 3.3.
Created separate output files for each document, organized by doc_id path.

WebAnno TSV 3.3 requirements:
  - All annotation layers declared in header must have corresponding columns
  - Every token must have values for ALL layers (use "_" if empty)
  - begin/end offsets are 0-based, end is exclusive
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class CoNLLUToken:
    def __init__(self):
        self.token_id: str = ""
        self.form: str = ""
        self.lemma: str = ""
        self.upos: str = ""
        self.xpos: str = ""
        self.feats: str = ""
        self.head: str = ""
        self.deprel: str = ""
        self.deps: str = ""
        self.misc: str = ""
        self.doc_start: int = -1
        self.doc_end: int = -1
        self.sent_start: int = -1
        self.sent_end: int = -1
        self.ner: str = "O"
        self.ner_type: str = ""
        self.ner_bio: str = "O"

    def parse_misc(self):
        if not self.misc or self.misc == "_":
            return
        pairs = self.misc.split("|")
        for pair in pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                key = key.strip()
                value = value.strip()
                if key == "NER":
                    self.ner = value
                    if value != "O":
                        parts = value.split("-", 1)
                        self.ner_bio = parts[0]
                        if len(parts) > 1:
                            self.ner_type = parts[1]
                elif key == "DocStart":
                    try:
                        self.doc_start = int(value)
                    except ValueError:
                        pass
                elif key == "DocEnd":
                    try:
                        self.doc_end = int(value)
                    except ValueError:
                        pass
                elif key == "SentStart":
                    try:
                        self.sent_start = int(value)
                    except ValueError:
                        pass
                elif key == "SentEnd":
                    try:
                        self.sent_end = int(value)
                    except ValueError:
                        pass

    def get_feats_dict(self) -> Dict[str, str]:
        if not self.feats or self.feats == "_":
            return {}
        result = {}
        for feat in self.feats.split("|"):
            if "=" in feat:
                k, v = feat.split("=", 1)
                result[k.strip()] = v.strip()
        return result


class CoNLLUSentence:
    def __init__(self):
        self.sent_id: str = ""
        self.text: str = ""
        self.tokens: List[CoNLLUToken] = []
        self.doc_id: str = ""
        self.split: str = ""

    def add_token(self, token: CoNLLUToken):
        self.tokens.append(token)


class Document:
    def __init__(self, doc_id: str):
        self.doc_id: str = doc_id
        self.sentences: List[CoNLLUSentence] = []


class CoNLLUFileParser:
    @staticmethod
    def parse(filepath: str) -> Dict[str, Document]:
        documents: Dict[str, Document] = {}
        current_document: Optional[Document] = None
        current_sentence: Optional[CoNLLUSentence] = None
        current_doc_id = ""

        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")

                if line.startswith("# doc_id"):
                    if current_sentence is not None and current_sentence.tokens:
                        current_document.sentences.append(current_sentence)
                        current_sentence = None
                    if current_document is not None:
                        documents[current_document.doc_id] = current_document

                    match = re.search(r"#\s*doc_id\s*=\s*(.+)", line)
                    if match:
                        current_doc_id = match.group(1).strip()
                        current_document = Document(current_doc_id)
                    continue

                if not line.strip():
                    if current_sentence is not None and current_sentence.tokens:
                        if current_document is not None:
                            current_document.sentences.append(current_sentence)
                        current_sentence = None
                    continue

                if line.startswith("#"):
                    if current_sentence is None:
                        current_sentence = CoNLLUSentence()
                        if current_document is not None:
                            current_sentence.doc_id = current_document.doc_id

                    stripped = line.lstrip("#").strip()
                    if "=" in stripped:
                        key, value = stripped.split("=", 1)
                        key = key.strip()
                        value = value.strip()

                        if key == "sent_id":
                            current_sentence.sent_id = value
                        elif key == "text":
                            current_sentence.text = value
                        elif key == "split":
                            current_sentence.split = value
                    continue

                if current_sentence is None:
                    current_sentence = CoNLLUSentence()
                    if current_document is not None:
                        current_sentence.doc_id = current_document.doc_id

                columns = line.split("\t")
                if len(columns) < 10:
                    continue

                if "-" in columns[0] and columns[0].replace("-", "").isdigit():
                    continue
                if "." in columns[0]:
                    continue

                token = CoNLLUToken()
                token.token_id = columns[0]
                token.form = columns[1]
                token.lemma = columns[2]
                token.upos = columns[3]
                token.xpos = columns[4]
                token.feats = columns[5]
                token.head = columns[6]
                token.deprel = columns[7]
                token.deps = columns[8]
                token.misc = columns[9]
                token.parse_misc()

                current_sentence.add_token(token)

            if current_sentence is not None and current_sentence.tokens:
                if current_document is not None:
                    current_document.sentences.append(current_sentence)
            if current_document is not None:
                documents[current_document.doc_id] = current_document

        return documents


class NamedEntitySpan:
    def __init__(self):
        self.start_token_idx: int = 0
        self.end_token_idx: int = 0
        self.entity_type: str = ""


def extract_ne_spans(tokens: List[CoNLLUToken]) -> List[NamedEntitySpan]:
    spans = []
    current_span = None

    for i, token in enumerate(tokens):
        bio = token.ner_bio
        etype = token.ner_type

        if bio == "B":
            if current_span is not None:
                spans.append(current_span)
            current_span = NamedEntitySpan()
            current_span.start_token_idx = i
            current_span.end_token_idx = i
            current_span.entity_type = etype
        elif bio == "I":
            if current_span is not None:
                if current_span.entity_type == etype:
                    current_span.end_token_idx = i
                else:
                    spans.append(current_span)
                    current_span = NamedEntitySpan()
                    current_span.start_token_idx = i
                    current_span.end_token_idx = i
                    current_span.entity_type = etype
            else:
                current_span = NamedEntitySpan()
                current_span.start_token_idx = i
                current_span.end_token_idx = i
                current_span.entity_type = etype
        else:
            if current_span is not None:
                spans.append(current_span)
                current_span = None

    if current_span is not None:
        spans.append(current_span)

    return spans


def compute_token_offsets(sentence: CoNLLUSentence) -> List[Tuple[int, int]]:
    offsets = []

    use_sent_offsets = False  # all(t.sent_start >= 0 for t in sentence.tokens)
    use_doc_offsets = all(t.doc_start >= 0 for t in sentence.tokens)

    if use_sent_offsets:
        for token in sentence.tokens:
            offsets.append((token.sent_start, token.sent_end))
    elif use_doc_offsets:
        for token in sentence.tokens:
            offsets.append((token.doc_start, token.doc_end))
    else:
        search_pos = 0
        for token in sentence.tokens:
            form = token.form
            idx = sentence.text.find(form, search_pos)
            if idx == -1:
                if offsets:
                    prev_end = offsets[-1][1]
                    start = prev_end + 1
                else:
                    start = 0
                end = start + len(form)
            else:
                start = idx
                end = idx + len(form)
            offsets.append((start, end))
            search_pos = end

    return offsets


def escape_tsv_value(value: str) -> str:
    if value is None:
        return "_"
    value = str(value)
    if not value:
        return "_"
    value = value.replace("\t", " ").replace("\n", " ").replace("\r", " ")
    return value


def escape_webanno_text(text: str) -> str:
    """
    Maskiert alle reservierten WebAnno-Zeichen in der richtigen Reihenfolge.
    """
    if not text:
        return "_"

    # 1. Zuerst den Backslash selbst maskieren, um Doppel-Maskierung zu verhindern
    text = text.replace("\\", "\\\\")

    # 2. Die restlichen reservierten Strukturzeichen maskieren
    reserved_chars = ["[", "]", "|", "_", ";", "*", "->"]
    for char in reserved_chars:
        text = text.replace(char, f"\\{char}")

    return text


def build_webanno_tsv_for_document(doc: Document) -> str:
    """Build WebAnno TSV 3.3 content for a single document.

    IMPORTANT:
    - Use WebAnno TSV 3.3 format
    - All tokens MUST have values for ALL declared layers
    - begin/end are 0-based, end is EXCLUSIVE (add 1 to make it exclusive)
    """
    lines: List[str] = []

    # ── Header ──────────────────────────────────────────────
    lines.append("#FORMAT=WebAnno TSV 3.3")

    # Declare annotation layers with their features
    # Each feature becomes ONE column after the base 4 columns (ID, begin, end, Form)
    lines.append(
        "#T_SP=de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Lemma|value"
    )
    lines.append(
        "#T_SP=de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS|PosValue|coarseValue"
    )
    lines.append("#T_SP=clear.NamedEntity|label")
    lines.append("")
    lines.append("")

    global_sentence_num = 0
    global_ne_idx_cnt = 0

    for sent_idx, sentence in enumerate(doc.sentences):
        global_sentence_num += 1

        # lines.append(f"== {global_sentence_num} ==")

        sent_text = (
            sentence.text
            if sentence.text
            else " ".join(t.form for t in sentence.tokens)
        )
        sent_text_escaped = sent_text.replace("\n", " ").replace("\r", "")
        lines.append(f"#Text={sent_text_escaped}")

        # if sentence.sent_id:
        #    lines.append(f"#sent_id={sentence.sent_id}")
        # if sentence.doc_id:
        #    lines.append(f"#doc_id={sentence.doc_id}")

        offsets = compute_token_offsets(sentence)
        ne_spans = extract_ne_spans(sentence.tokens)

        # Build NE lookup: token_idx -> [(span, is_start)]
        token_ne_info: Dict[int, List[Tuple[NamedEntitySpan, int]]] = {}
        for span in ne_spans:
            for t_idx in range(span.start_token_idx, span.end_token_idx + 1):
                is_start = t_idx == span.start_token_idx
                if t_idx not in token_ne_info:
                    token_ne_info[t_idx] = []
                token_ne_info[t_idx].append((span, global_ne_idx_cnt))
            global_ne_idx_cnt += 1

        # ── Token lines ────────────────────────────────────
        # Columns (8 total):
        # 0: Token ID
        # 1: begin offset (0-based, inclusive)
        # 2: end offset (0-based, EXCLUSIVE)
        # 3: Form
        # 4: Lemma.value
        # 5: POS.PosValue
        # 6: POS.coarseValue
        # 7: NamedEntity.value

        for i, token in enumerate(sentence.tokens):
            tid = str(i + 1)

            # Get offsets - end must be exclusive (add 1 to original end)
            start_off, end_off_inclusive = offsets[i]
            begin_str = str(start_off)
            end_str = str(end_off_inclusive)  # Make exclusive for WebAnno

            form = escape_webanno_text(escape_tsv_value(token.form))
            lemma_val = (
                escape_webanno_text(escape_tsv_value(token.lemma))
                if token.lemma != "_"
                else "_"
            )
            pos_fine = escape_tsv_value(token.upos) if token.upos != "_" else "_"
            pos_coarse = escape_tsv_value(token.xpos) if token.xpos != "_" else "_"

            # Named Entity annotation
            # For multi-token spans: first token gets entity type, others get "*"
            ne_cell = "_"
            if i in token_ne_info:
                spans_list = token_ne_info[i]
                ne_parts = []
                for span, ne_idx in spans_list:
                    entity_type = span.entity_type if span.entity_type else "ENTITY"
                    # if is_start:
                    #    ne_parts.append(entity_type + "[" + str(i) + "]")
                    # else:
                    #    ne_parts.append(entity_type + "[" + str(i) + "]")
                    ne_parts.append(entity_type + "[" + str(ne_idx) + "]")
                ne_cell = "|".join(ne_parts)

            # Assemble row with EXACTLY 8 columns
            row = [
                str(global_sentence_num) + "-" + tid,  # 0: Token ID
                begin_str + "-" + end_str,  # 1: begin offset (inclusive)
                # end_str,  # 2: end offset (EXCLUSIVE)
                form,  # 3: Form
                lemma_val,  # 4: Lemma.value
                pos_fine,  # 5: POS.PosValue
                pos_coarse,  # 6: POS.coarseValue
                ne_cell,  # 7: NamedEntity.value
            ]

            # Double-check column count
            if len(row) != 7:
                print(f"WARNING: Token row has {len(row)} columns instead of 8!")

            lines.append("\t".join(row))

        if sent_idx != len(doc.sentences) - 1:
            lines.append("")  # Blank line between sections

    return "\n".join(lines)


def safe_makedirs(directory: Path):
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(
            f"  Warning: Cannot create directory {directory}, may already exist or permission denied"
        )
    except OSError as e:
        print(f"  Warning: Could not create directory {directory}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert CoNLL-U (multi-document) to WebAnno TSV 3.3 format.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", help="Path to input CoNLL-U file")
    parser.add_argument(
        "output_dir", help="Base output directory for generated TSV files"
    )

    args = parser.parse_args()

    output_path = Path(args.output_dir)

    print(f"Parsing CoNLL-U file: {args.input}")
    documents = CoNLLUFileParser.parse(args.input)

    total_documents = len(documents)
    total_sentences = sum(len(d.sentences) for d in documents.values())
    total_tokens = sum(
        sum(len(s.tokens) for s in d.sentences) for d in documents.values()
    )
    total_ne = sum(
        sum(len(extract_ne_spans(s.tokens)) for s in d.sentences)
        for d in documents.values()
    )

    print(f"  Documents found: {total_documents}")
    print(f"  Sentences:       {total_sentences}")
    print(f"  Tokens:          {total_tokens}")
    print(f"  NE spans:        {total_ne}")
    print()

    safe_makedirs(output_path)

    processed_files: List[Path] = []
    failed_docs: List[str] = []

    for doc_id, document in documents.items():
        if "/" in doc_id:
            folder_name, file_basename = doc_id.rsplit("/", 1)
        else:
            folder_name = doc_id
            file_basename = f"{folder_name}_file"

        output_subdir = output_path / folder_name
        output_file = output_subdir / f"{file_basename}.tsv"

        print(f"Processing: {doc_id}")
        print(f"  → {output_file}")

        output_file = output_file.resolve()

        try:
            output_file.relative_to(output_path.resolve())
        except ValueError:
            print(f"  ERROR: Invalid path detected, skipping {doc_id}")
            failed_docs.append(doc_id)
            continue

        safe_makedirs(output_subdir)

        try:
            tsv_content = build_webanno_tsv_for_document(document)

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(tsv_content)
                f.write("\n")

            processed_files.append(output_file)

            stats = {
                "sentences": len(document.sentences),
                "tokens": sum(len(s.tokens) for s in document.sentences),
                "ne_spans": sum(
                    len(extract_ne_spans(s.tokens)) for s in document.sentences
                ),
            }
            print(
                f"  ✓ Written: {stats['sentences']} sentences, {stats['tokens']} tokens, {stats['ne_spans']} NE spans"
            )
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            failed_docs.append(doc_id)

    print()
    print("=" * 60)
    print(f"Conversion complete!")
    print(f"  Processed: {len(processed_files)} documents")
    if failed_docs:
        print(f"  Failed:    {len(failed_docs)} documents")
    print(f"  Output dir: {output_path.resolve()}")

    if processed_files:
        print("\nGenerated files:")
        for f in processed_files[:10]:
            print(f"  {f}")
        if len(processed_files) > 10:
            print(f"  ... and {len(processed_files) - 10} more")

    return 0 if not failed_docs else 1


if __name__ == "__main__":
    sys.exit(main())
