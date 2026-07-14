import random
from collections import Counter, defaultdict

import numpy as np
from tuw_nlp.text.patterns.de import ABBREV
from tuw_nlp.text.segmentation import SsplitFixer

from clear_anonymization.ner_datasets.ner_dataset import NERData
from clear_anonymization.ner_datasets.util import recreate_sent_labels_from_tokens


def preprocess_text(text):
    text = text.replace("\xa0", " ")
    return text


def validate_docu_annotations(text, labels, verbose=False):
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
    if not verbose and not all_ok:
        print("❌ Annotation check failed!")
    return all_ok


def validate_sentence_annotations(sample, error_file, verbose=False):
    all_ok = True
    errors = []

    for sent in sample.sentences:
        labels = recreate_sent_labels_from_tokens(sent.tokens, sent.text)
        for label in sent.labels or []:
            matched = any(
                span["start"] == label["start"] and span["end"] == label["end"]
                for span in labels
            )
            if not matched:
                all_ok = False
                msg = f"{sample.doc_id} | {sent.sent_id} | ❌ '{label['text']}' ({label['start']}:{label['end']})"
                errors.append(msg)
                if verbose:
                    print(
                        f"❌ missed: '{label['text']}' ({label['start']}:{label['end']})"
                    )
            elif verbose:
                print(f"{sent.sent_id} - ✓ '{label['text']}' ")

    if not verbose and not all_ok:
        print("❌ Sentence annotation check failed!")

    if error_file and errors:
        with open(error_file, "a") as f:
            for e in errors:
                f.write(e + "\n")


def assign_bio_tag(token, labels, offset=0) -> str:
    start = token.start_char - offset
    end = token.end_char - offset
    for label in labels:
        if start < label["end"] and end > label["start"]:
            if start <= label["start"]:
                return f"B-{label['type']}"
            return f"I-{label['type']}"
    return "O"


TITLES = {
    "Bakk. techn.",
    "B. Sc.",
    "Hon. Prof.in",
    "Priv. Doz.in",
    "Techn.R.",
    "B. A.",
    "LL.M.",
    "Univ. Prof.",
    "Bakk.iur.",
    "B. Ed.",
    "Priv. Doz.",
    "M.Sc.",
    "Dr.",
    "Mag.a",
    "Priv.-Doz.",
    "Bakk. art.",
    "OSR.",
    "KmzlR.",
    "Univ Prof.in",
    "VetR.",
    "LL.B.",
    "Techn.R",
    "Ing.",
    "Univ.-Prof.in",
    "Dr.in",
    "ÖkR.",
    "Dipl. Kfm.",
    "KommR.",
    "Bakk. rer. nat.",
    "Bakk. iur.",
    "Hon. Prof.",
    "LL. M.",
    "Bakk.rer.nat.",
    "Univ. Prof.in",
    "Univ.-Prof.",
    "Dipl.-Ing.",
    "OStR.",
    "B.Sc.",
    "RegR.",
    "KzlR.",
    "MedR.",
    "Prof.in",
    "Mag.",
    "Bakk.art.",
    "B.Ed.",
    "Hon Prof.in",
    "Bakk.phil.",
    "Dipl. Kff.",
    "Bakk. phil.",
    "Bakk.techn.",
    "Hon.-Prof.in",
    "M. Sc.",
    "M.A.",
    "M. A.",
    "StR.",
    "B.A.",
    " LL. B.",
    "DDr.in",
    "Prof.",
    "Priv.-Doz.in",
    "OmedR.",
    "DDr.",
    "Hon.-Prof.",
    "Dipl. Ing.",
    "Dipl.",
    "Kfm.",
    "Kff.",
}

TOB = {"e.U.", "e.U", "e.G.", "e.G"}
ROMAN_NUMBERING = {
    "I.",
    "II.",
    "III.",
    "IV.",
    "V.",
}

MISC = {
    "lfd.",
    "u.",
    "St.Nr.",
    "Nr.",
    "nr.",
    "Tel.",
    "abz.",
    "Bmst.",
    "UID-Nr.",
    "Uid-Nr.",
    "UlD-Nr.",
    "DVR-Nr.",
    "abzugi.",
    "Kunden-Nr.",
    "Kunden:Nr.",
    "Kunden-nr.",
    "Rechnung-Nr.",
    "Telefon-Nr.",
    "Dot.",
    "Pos.",
    "Bel.",
    "Bundesstr.",
    "Zuschl.",
    "Abg.",
    "gem.",
    "SV-NR.",
    "SV-Nr.",
    "Wr.",
    "elektr.",
    "GZ.",
    "exkl.",
    "inkl.",
    "Erl.",
    "bez.",
    "ca.",
    "lt.",
    "Einh.",
    "Inc.",
    "Art.",
    "BGBl.",
    "geb.",
    "Geb.",
    "Pos.",
    "Pos.Nr.",
    "Kto-Nr.",
    "Art.-nr.",
    "Angebots-Nr.",
    "zzgl.",
    "HR.",
    "Hr.",
    "z.Hd.",
    "Arb.",
    "Art.Nr.",
    "Eht.",
}

_original_is_err = SsplitFixer.is_err


def _is_err_patch(self, sen1, sen2):
    res1, res2 = _original_is_err(self, sen1, sen2)

    if res1 and res2:
        return res1, res2

    for abr in ABBREV:
        if abr == sen1.text or sen1.text.endswith(abr):
            return True, True
        if " " in abr:
            split = abr.split(" ")
            if sen1.text.endswith(split[0]) and sen2.text.startswith(split[1]):
                return True, True

    return False, None
