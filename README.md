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

To store the dataset in a json format inside the `data` folder. Add argument `--sentences´ if you want to keep only those sentences that contain annotations. 

```bash
python clear_anonymization/preprocess/preprocess_data.py --input_dir {datasetname}_TRAIN.zip --output_dir data/{datasetname}/{datasetname}_train.json --split train --sentences 

```

### LLM Extractor

First, serve a model locally using [vLLM] (https://docs.vllm.ai/):
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

### NER Rules

We use [RuleChef] (https://github.com/KRLabsOrg/rulechef) to automatically generate extraction rules.


