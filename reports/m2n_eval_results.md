# Evaluation Results - m2n

Generated on: 2025-12-16T15:36:41.643531

**Thresholds explanation:**

Each model is evaluated on different thresholds.The threshold represents the minimum confidence score required for a predicted entity span to be considered correct.
**Examples:**

- A threshold of **1.0** means that each predicted span is considered correct only if it has **100% overlap** with the gold span.
- A threshold of **0.5** means that each predicted span is considered correct if it has at least **50% overlap** with the gold span.

Before evaluating the models, the prediction result files must be generated. First, start the local vLLM server using this example command:
```bash
python -m vllm.entrypoints.openai.api_server--model google/gemma-3-27b-it--host 0.0.0.0--port 8000 

```

Next, run the following command on a another terminal:

```bash
python clear_anonymization/extractors/llm.py --input_dir data/m2n/m2n_data.json --model {MODEL_NAME} --mode {one_step or two_step} --dataset m2n --zero_shot```

```bash
python clear_anonymization/extractors/llm.py --input_dir data/m2n/m2n_data.json --model {MODEL_NAME} --mode {one_step or two_step} --dataset m2n --zero_shot```

Evaluating of the model results can be done by running the following example bash command:

```bash
python scripts/evaluate_llm.py--model {MODEL_NAME}--input_dir data/m2n/m2n_data.json--evaluation_type span_level--dataset m2n--mode {one_step or two_step}--zero_shot```

## Evaluation Results of google/gemma-3-27b-it - NERMode.ONE_STEP

| Threshold | Precision | Recall | F1 |
|---------|---------|------|--|
| 0.1 | 0.6959 | 0.6581 | 0.6765 |
| 0.2 | 0.6926 | 0.6571 | 0.6743 |
| 0.3 | 0.6824 | 0.6516 | 0.6667 |
| 0.4 | 0.6351 | 0.6246 | 0.6298 |
| 0.5 | 0.6081 | 0.6081 | 0.6081 |
| 0.6 | 0.5709 | 0.5709 | 0.5709 |
| 0.7 | 0.5405 | 0.5405 | 0.5405 |
| 0.8 | 0.5034 | 0.5034 | 0.5034 |
| 0.9 | 0.4899 | 0.4915 | 0.4907 |
| 1 | 0.4797 | 0.4814 | 0.4805 |

## Evaluation Results of google/gemma-3-27b-it - NERMode.TWO_STEP

| Threshold | Precision | Recall | F1 |
|---------|---------|------|--|
| 0.1 | 0.6398 | 0.6540 | 0.6468 |
| 0.2 | 0.6304 | 0.6506 | 0.6404 |
| 0.3 | 0.6025 | 0.6319 | 0.6169 |
| 0.4 | 0.5652 | 0.6047 | 0.5843 |
| 0.5 | 0.5404 | 0.5878 | 0.5631 |
| 0.6 | 0.5124 | 0.5574 | 0.5340 |
| 0.7 | 0.4907 | 0.5338 | 0.5113 |
| 0.8 | 0.4565 | 0.4966 | 0.4757 |
| 0.9 | 0.4441 | 0.4847 | 0.4635 |
| 1 | 0.4503 | 0.4915 | 0.4700 |

## Evaluation Results of mistralai/Ministral-3-8B-Instruct-2512 - NERMode.ONE_STEP

| Threshold | Precision | Recall | F1 |
|---------|---------|------|--|
| 0.1 | 0.5141 | 0.6390 | 0.5698 |
| 0.2 | 0.5141 | 0.6390 | 0.5698 |
| 0.3 | 0.5039 | 0.6302 | 0.5600 |
| 0.4 | 0.4679 | 0.6047 | 0.5275 |
| 0.5 | 0.4447 | 0.5864 | 0.5058 |
| 0.6 | 0.4113 | 0.5424 | 0.4678 |
| 0.7 | 0.3882 | 0.5119 | 0.4415 |
| 0.8 | 0.3522 | 0.4644 | 0.4006 |
| 0.9 | 0.3445 | 0.4542 | 0.3918 |
| 1 | 0.3445 | 0.4542 | 0.3918 |

## Evaluation Results of google/gemma-3-27b-it - NERMode.TWO_STEP

| Threshold | Precision | Recall | F1 |
|---------|---------|------|--|
| 0.1 | 0.6398 | 0.6540 | 0.6468 |
| 0.2 | 0.6304 | 0.6506 | 0.6404 |
| 0.3 | 0.6025 | 0.6319 | 0.6169 |
| 0.4 | 0.5652 | 0.6047 | 0.5843 |
| 0.5 | 0.5404 | 0.5878 | 0.5631 |
| 0.6 | 0.5124 | 0.5574 | 0.5340 |
| 0.7 | 0.4907 | 0.5338 | 0.5113 |
| 0.8 | 0.4565 | 0.4966 | 0.4757 |
| 0.9 | 0.4441 | 0.4847 | 0.4635 |
| 1 | 0.4503 | 0.4915 | 0.4700 |

