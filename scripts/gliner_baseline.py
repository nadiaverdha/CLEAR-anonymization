import argparse
import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from gliner2 import GLiNER2

from clear_anonymization.extractors import factory
from clear_anonymization.extractors.base import BaseExtractor
from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.ner_datasets.ler_dataset import LERData, LERSample


def to_spans(predicted, text):
    spans = []
    # print(predicted)
    entities = predicted["entities"]
    # print(entities)
    if entities:
        for label, subs in entities.items():
            for sub in subs:
                match = re.search(re.escape(sub), text)
                if match:
                    spans.append(
                        {
                            "start": match.start(),
                            "end": match.end(),
                            "text": sub,
                            "class": label,
                        }
                    )
    return spans


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a named entity recognition model based on LLM"
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path to the evaluation data (JSON format)",
    )
    parser.add_argument("--model", type=str, required=True, help="GliNER model ")
    parser.add_argument("--cache_file", type=str, default=None)

    args = parser.parse_args()

    definitions = {
        "PERS": "Personen (Familien, Vor-, Beinamen und Pseudonymen)",
        "LOC": "Ortsnamen, geographische Bezeichnungen (Land, Stadt, Region)",
        "ORG": "Organisationsnamen (Parteien, Vereine, Institutionen, Unternehmen)",
        "NRM": "Rechtsnormen(Europäische Normen, Gesetze, Rechtsverordungen)",
        "RS": "Rechtsprechungen (keine Namen sondern Zitate von Entscheidungen)",
        "LIT": "Rechtsliteratur (Rechtsliteratur, Gesetzgebungsmaterialien)",
        "REG": "Einzelfallregelungen (Vorschriften, Verträge)",
    }
    if args.cache_file is None:
        cache_file = (
            Path(__file__).parent.parent
            / "clear_anonymization"
            / f"cache"
            / "gliner"
            / "cache.json"
        )
        print(f"Using default cache file: {cache_file}")
    else:
        print(f"Using provided cache file: {cache_file}")

    cache = CacheManager(cache_file)

    data = LERData.from_json(json.loads(Path(args.input_dir).read_text()))
    samples = [s for s in data.samples if s.split == "validation"]
    print(f"\nEvaluating model on test samples: {len(samples)}")
    texts = [s.sentences for s in samples]
    extractor = GLiNER2.from_pretrained(args.model).to("cuda")
    results = extractor.batch_extract_entities(texts, definitions, batch_size=8)
    print(results)
    formatted_results = []

    with ThreadPoolExecutor() as ex:
        formatted_results = list(
            ex.map(
                lambda pair: {"text": pair[0], "spans": to_spans(pair[1], pair[0])},
                zip(texts, results),
            )
        )

    # for text, predicted in zip(texts, results):
    #    formatted_results.append({"text": text, "spans": to_spans(predicted, text)})

    output_path = Path("gliner_results.json")

    output_path.write_text(json.dumps(formatted_results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
