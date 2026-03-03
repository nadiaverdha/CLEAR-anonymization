import random
from typing import List, Literal

from pydantic import BaseModel, Field, field_validator
from clear_anonymization.ner_datasets import get_dataset_class_definitions


class Entity(BaseModel):
    text: str = Field(description="The matched text span")
    start: int = Field(description="Start character offset")
    end: int = Field(description="End character offset")
    type: str = Field(description="Entity label")


class NEROutput(BaseModel):
    entities: List[Entity]


def get_class_def(
    dataset_name: str, allowed_classes: list[str] | None
) -> tuple[str, str]:
    class_definitions = get_dataset_class_definitions(dataset_name)
    all_classes = set(class_definitions.keys())

    if allowed_classes:
        classes = set(allowed_classes)
        unknown = classes - all_classes
        if unknown:
            raise ValueError(f"Unknown entity classes: {unknown}")
        classes_str = "_".join(sorted(classes))
    else:
        classes = all_classes
        classes_str = "all_classes"

    classes_def = ", ".join(f"{c}: {class_definitions[c]}" for c in classes)
    return classes_str, classes_def


def sample_data(samples, allowed_classes, k=50, seed=123, window_size=200):
    random.seed(seed)

    positive_samples = []
    for sample in samples:
        text = sample.text
        entities = sorted(
            [l for l in sample.labels if l["type"] in allowed_classes],
            key=lambda x: x["start"],
        )

        if not entities:
            continue
        merged_windows = []
        for ent in entities:
            start = max(0, ent["start"] - window_size)
            end = min(len(text), ent["end"] + window_size)
            if merged_windows and start <= merged_windows[-1][1]:
                merged_windows[-1][1] = max(end, merged_windows[-1][1])
                merged_windows[-1][2].append(ent)
            else:
                merged_windows.append([start, end, [ent]])

        for start, end, window_entities in merged_windows:
            snippet = text[start:end]
            adjusted_entities = []
            for e in window_entities:
                adjusted_entities.append(
                    {
                        "text": e["text"],
                        "start": e["start"] - start,
                        "end": e["end"] - start,
                        "type": e["type"],
                    }
                )
            positive_samples.append({"text": snippet, "entities": adjusted_entities})
    return positive_samples
