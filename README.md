# CLEAR-anonymization
## CLEAR: Comprehensible Learning for Entity Anonymization and Recognition 
![Alt text](assets/logo.png)



### Installation
```bash
pip install -e .
```

### Getting the data 

#### LER Dataset

To download the LER dataset from HuggingFace in a json format inside the `data` folder:
```bash
python clear_anonymization/preprocess/preprocess_ler.py --repository_id elenanereiss/german-ler --output_dir data/ler/ler_data.json 
```

#### Other Datasets (Musterfall, FinDok)

To store the dataset in a ConLL format inside the `data` folder. 

```bash
python clear_anonymization/preprocess/preprocess_data.py --input_dir {datasetname}_TRAIN.zip --output_dir data/{datasetname}/{datasetname}_train.conllu --split train --verbose

```

The train dataset is further split into a train and test set which will be used in our testing. The existing validation set is kept held-out for final evaluation. 

```bash
 python clear_anonymization/preprocess/create_train_dev_split.py --train-file data/{datasetname}/{datasetname}_train.conllu --output-dir  /share/nverdha/data/{dataset_name}/ --dev-ratio 0.2 --seed 42
```


### NER Rules

We use [RuleChef](https://github.com/KRLabsOrg/rulechef) to automatically generate extraction rules.

First, serve a model locally using [vLLM](https://docs.vllm.ai/):
```bash
vllm serve Qwen/Qwen3.5-35B-A3B --port 8000 --max-model-len 64000 --reasoning-parser qwen3 --language-model-only --default-chat-template-kwargs '{"enable_thinking": false}'
```


### LLM Extractor

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
