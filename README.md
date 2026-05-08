# CLEAR-anonymization
## CLEAR: Comprehensible Learning for Entity Anonymization and Recognition 
![Alt text](assets/logo.png)


CLEAR learns interpretable regex-based extraction rules for Named Entity Recognition (NER) in German legal documents. It builds upon [RuleChef](https://github.com/KRLabsOrg/rulechef), an LLM-powered rule synthesis framework with an iterative refinement loop to produce rules that are human-readable, auditable, and accurate.


## How it works
1. **Synthesis** — given a batch of annotated sentences, an LLM generates regex rules covering the observed entity patterns
2. **Refinement** — rules are evaluated on a held-out set and iteratively improved based on false positives / false negatives
3. **Transfer** (optional) — rules learned on one dataset can be used as basis rules for training on a second dataset
### Installation
```bash
pip install -e .
```


Requires Python ≥ 3.8. Key dependencies: `rulechef`, `openai`, `pydantic`, `stanza`, `spacy`.

---
## Data preparation

### LER Dataset

To download the LER dataset from HuggingFace in a json format inside the `data` folder:
```bash
python clear_anonymization/preprocess/preprocess_ler.py \
 --repository_id elenanereiss/german-ler \ 
 --output_dir data/ler/ler_data.json \
```

### Other Datasets (Musterfall, FinDok)

To store the dataset in a ConLL format inside the `data` folder. 

```bash
python clear_anonymization/preprocess/preprocess_data.py \
--input_dir {datasetname}_TRAIN.zip \
--output_dir data/{datasetname}/{datasetname}_train.conllu \
--split train \
--verbose \

```

The train dataset is further split into a train and test set which will be used in our testing. The existing validation set is kept held-out for final evaluation. 

```bash
 python clear_anonymization/preprocess/create_train_dev_split.py \
--train-file data/{datasetname}/{datasetname}_train.conllu \
--output-dir  /share/nverdha/data/{dataset_name}/ \
--dev-ratio 0.2 \
--seed 42
```
---

## Running the benchmark

First, serve a model with [vLLM](https://docs.vllm.ai/):
```bash
vllm serve Qwen/Qwen3.5-35B-A3B \
  --port 8000 \
  --max-model-len 64000 \
  --reasoning-parser qwen3 \
  --language-model-only \
  --default-chat-template-kwargs '{"enable_thinking": false}'
```

Then run:
```bash
python -m benchmarks.benchmark \
  --train-dir data/findok/data/{dataset_name}/{dataset_name}_train.conllu \
  --test-dir data/findok//{dataset_name}/{dataset_name}_dev.conllu \
  --dataset-name findok \
  --classes organisation \
  --model Qwen/Qwen3.5-35B-A3B \
  --base-url http://localhost:8000/v1 \
  --max-rules 30 \
  --batch-size 30 \
  --max-iterations 1 \
  --output results_findok.json
```

Or use a config file (CLI flags override config values):
```bash
python -m benchmarks.benchmark --config benchmarks/config.yaml
```

### Key arguments

| Argument | Default | Description |
|---|---|---|
| `--train-dir` | — | CoNLL-U training data |
| `--test-dir` | — | CoNLL-U dev / test data |
| `--dataset-name` | `findok` | Dataset identifier |
| `--classes` | all | Comma-separated entity classes to learn |
| `--model` | `Qwen/Qwen3.5-35B-A3B` | vLLM model name |
| `--base-url` | `http://localhost:8000/v1` | OpenAI-compatible endpoint |
| `--max-rules` | 10 | Maximum number of rules to keep |
| `--batch-size` | 20 | Training sentences per batch |
| `--max-iterations` | 3 | Refinement iterations after synthesis |
| `--sampling-strategy` | `balanced` | How to sample training examples |
| `--synthesis-strategy` | `bulk` | `bulk` (all at once) or incremental |
| `--seed` | 42 | Random seed for reproducibility |
| `--rules-json` | — | Seed training with existing rules |
| `--skip-synthesis` | false | Skip synthesis, only run refinement |
| `--agentic` | false | Enable agentic LLM feedback loop |
| `--enable-critic` | false | Enable LLM-based rule critique |
| `--no-mdreport` | false | Skip generating the Markdown report |

### Resuming after a crash

If a run is interrupted, resume from the last completed batch:
```bash
python -m benchmarks.benchmark \
  --resume-from reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/{folder_you_want_to_resume_experiment}/
```

The checkpoint file (`checkpoint.json`) is written after every batch and deleted on clean completion. The output directory already contains `config.yaml` with all original settings, so no other flags are needed.

---

## Transfer learning

Train on a source dataset, then continue on a target dataset seeded with the learned rules:
```bash
python -m benchmarks.benchmark \
  --train-dir data/ler/split/train.conllu \
  --test-dir data/ler/split/dev.conllu \
  --dataset-name ler \
  --transfer-train-dir data/findok/split/train.conllu \
  --transfer-test-dir data/findok/split/dev.conllu \
  --transfer-dataset-name findok \
  --transfer-continuation synthesize_and_refine \
  --model Qwen/Qwen3.5-35B-A3B
```

`--transfer-continuation` choices: `synthesize_and_refine` (default) or `refine_only` (adapt existing rules without synthesizing new ones).

---

## Outputs

Results are written to `reports/{dataset}/{model}/{classes}/{date}/`:

| File | Contents |
|---|---|
| `results_findok.json` | Metrics, per-class breakdown, learned rules |
| `results_findok.rules_report.md` | Human-readable rule evaluation report |
| `results_findok.training.jsonl` | Per-iteration training log |
| `config.yaml` | Exact config used for this run |
| `session_summary.json` | Full training history across all phases |


---


## LLM Extractor

First, serve a model locally using [vLLM](https://docs.vllm.ai/):
```bash
python -m vllm.entrypoints.openai.api_server   --model google/gemma-3-27b-it  --host 0.0.0.0   --port 8000
```

Then run extraction:

```python

from clear_anonymization.extractors import factory

LLMExtractor = factory.make_extractor("llm", model="google/gemma-3-27b-it", prompt_path=clear_anonymization/prompts/ner_task_2.txt)
LLMExtractor.predict("Frau Müller arbeitet beim Bundesgericht.")

[{'start': 0, 'end': 11, 'text': 'Frau Müller', 'entity': 'PERS'}, {'start': 26, 'end': 39, 'text': 'Bundesgericht', 'entity': 'ORG'}]
```

---


## License

Apache 2.0
