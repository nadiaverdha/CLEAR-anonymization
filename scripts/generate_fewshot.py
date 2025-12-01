import random
import argparse
import json
from pathlib import Path
from clear_anonymization.ner_datasets.ler_dataset import LERSample, LERData


def gen_fewshot_samples(train_samples, fewshots_path, k=5, seed=123):
    random.seed(seed)
    candidates = []
    for s in train_samples:
        if s.labels:
            candidates.append(s)
    selected = random.sample(candidates, k)
    fewshots = []
    for s in selected:
        print(s.labels)
        print([s.labels[0]["text"]])
        fewshots.append({"text": s.sentences, "labels": [s.labels[0]]})

    Path(fewshots_path).write_text(json.dumps(fewshots, ensure_ascii=False, indent=2))

    return fewshots


def main(
    input_dir: str,
    fewshots_path: str,
    dataset: str = "ler",
):
    input_dir = Path(input_dir)
    data = LERData.from_json(json.loads(input_dir.read_text()))
    train_samples = [s for s in data.samples if s.split == "train"]
    gen_fewshot_samples(train_samples, fewshots_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="User the LLM for a named entitiy recognition task"
    )
    parser.add_argument(
        "--input_dir", type=str, required=True, help="Path to the input data files"
    )

    parser.add_argument(
        "--fewshots_path", type=str, required=True, help="Path to the prompt file"
    )

    parser.add_argument(
        "--dataset", type=str, default="ler", help="Name of the dataset"
    )
    args = parser.parse_args()

    main(
        Path(args.input_dir),
        args.fewshots_path,
        args.dataset,
    )
