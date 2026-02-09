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

#### Other Datasets (Musterfall, BFG)

To store the dataset in a json format inside the `data` folder:
```bash
python clear_anonymization/preprocess/preprocess_m2n.py --input_dir {datasetname}_TRAIN.zip --output_dir data/bfg/{datasetname}_train.json --split train 

```

### LLM Baseline

First, start running the LLM model, e.g. google/gemma-3-27b-it locally using a VLLM:

```bash
python -m vllm.entrypoints.openai.api_server   --model google/gemma-3-27b-it  --host 0.0.0.0   --port 8000
```

```python

from clear_anonymization.extractors import factory

LLMExtractor = factory.make_extractor("llm", model="google/gemma-3-27b-it", prompt_path=clear_anonymization/prompts/ner_task_2.txt)
LLMExtractor.predict("Frau Müller arbeitet beim Bundesgericht.")

[{'start': 0, 'end': 11, 'text': 'Frau Müller', 'entity': 'PERS'}, {'start': 26, 'end': 39, 'text': 'Bundesgericht', 'entity': 'ORG'}]
```

