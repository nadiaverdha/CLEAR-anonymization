import random
from collections import Counter, defaultdict

from tuw_nlp.text.patterns.de import ABBREV
from tuw_nlp.text.segmentation import SsplitFixer

from clear_anonymization.ner_datasets.ner_dataset import NERData
from clear_anonymization.ner_datasets.util import recreate_sent_labels_from_tokens


def split_test(data, test_ratio=0.2, seed=42):
    rng = random.Random(seed)
    samples = list(data.samples)

    class_counts = defaultdict(int)
    for sample in samples:
        
        for l in sample.labels:
            print(l)
            class_counts[l["type"]] += 1

    print("Full distribution:", dict(class_counts))
    print("--------------------------------------")
    test_quota = {
        label: max(1, int(cnt * test_ratio)) for label, cnt in class_counts.items()
    }
    print("Target test quota:", test_quota)
    print("--------------------------------------")

    test_filled = defaultdict(int)

    rng.shuffle(samples)

    samples.sort(
        key=lambda s: min(
            (class_counts[l["type"]] for l in s.labels), default=float("inf")
        )
    )

    test_samples = []
    train_samples = []

    max_test_size = int(len(samples) * test_ratio)
    print(max_test_size)

    for sample in samples:
        sample_labels = [l["type"] for l in sample.labels]
        print(sample_labels)
        if (
            len(test_samples) < max_test_size
            and sample_labels
            and any(test_filled[label] < test_quota[label] for label in sample_labels)
        ):  
            
            test_samples.append(sample)
            print(test_samples)
            for label in sample_labels:
                test_filled[label] += 1
        else:
            train_samples.append(sample)

    rng.shuffle(train_samples)
    rng.shuffle(test_samples)

    print(f"Train: {len(train_samples)} samples, Test: {len(test_samples)} samples")
    print("--------------------------------------")
    print("Test class distribution:", dict(test_filled))

    return NERData(train_samples), NERData(test_samples)


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


def validate_sentence_annotations(sample, verbose=False):
    all_ok = True
    for sent in sample.sentences:
        labels = recreate_sent_labels_from_tokens(sent.tokens, sent.text)
        for label in sent.labels or []:
            # print(labels)
            matched = any(
                span["start"] == label["start"] and span["end"] == label["end"]
                for span in labels
            )
            if not matched:
                all_ok = False
                if verbose:
                    print(
                        f"❌ missed: '{label['text']}' ({label['start']}:{label['end']})"
                    )
            elif verbose:
                print(f"{sent.sent_id} - ✓ '{label['text']}' ")

    if not verbose and not all_ok:
        print("❌ Sentence annotation check failed!")


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
        if abr == sen1.text or sen1.text.endswith(f"\n{abr}"):
            return True, True

    return False, None
