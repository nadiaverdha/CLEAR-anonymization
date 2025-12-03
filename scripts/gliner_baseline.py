import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from gliner2 import GLiNER2
from clear_anonymization.extractors import factory

from clear_anonymization.extractors.base import BaseExtractor
from clear_anonymization.ner_datasets.ler_dataset import LERData, LERSample


__all__ = ["GlinerExtractor"]


def predict(text, extractor,definitions):
    entities = extractor.extract_entities(
            text,
            definitions,
        )
    to_spans(entities)
    return entities
    

def to_spans(entities):
    print(entities)
    keys = entities['entities'].keys()
    
    for key in keys:
        print(entities['entities'][key])
    spans = []
    #print(entities['entities'].keys())
    print("________________")
    #for entity_type, values in entities['entities'].items():
     #   print(entity_type, values)

    
def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a named entity recognition model based on LLM"
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Path to the evaluation data (JSON format)",
    )

    args = parser.parse_args()

    data = LERData.from_json(json.loads(Path(args.input_dir).read_text()))
    samples = [s for s in data.samples if s.split == "validation"]
    print(f"\nEvaluating model on test samples: {len(samples)}")

    definitions = {
        "PERS": "Personen (Familien, Vor-, Beinamen und Pseudonymen)",
        "LOC": "Ortsnamen, geographische Bezeichnungen (Land, Stadt, Region)",
        "ORG": "Organisationsnamen (Parteien, Vereine, Institutionen, Unternehmen)",
        "NRM": "Rechtsnormen(Europäische Normen, Gesetze, Rechtsverordungen)",
        "RS": "Rechtsprechungen (keine Namen sondern Zitate von Entscheidungen)",
        "LIT": "Rechtsliteratur (Rechtsliteratur, Gesetzgebungsmaterialien)",
        "REG": "Einzelfallregelungen (Vorschriften, Verträge)",
    }

    extractor = GLiNER2.from_pretrained("fastino/gliner2-base-v1")

    results = []

    samples = [s for s in data.samples if s.split == "validation"]
    for i in samples[:2]:
        predict(i.sentences, extractor,definitions)



if __name__ == "__main__":
    main()
