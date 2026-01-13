# Evaluation Results - m2n

Generated on: 2026-01-13T11:02:12.490488

**Thresholds explanation:**

Each model is evaluated on different thresholds.The threshold represents the minimum overlap required for a predicted entity span to be considered correct.
**Examples:**

- A threshold of **1.0** means that each predicted span is considered correct only if it has a **100% overlap** with the gold span.
- A threshold of **0.5** means that each predicted span is considered correct if it has at least a **50% overlap** with the gold span.

Before evaluating the models, the prediction result files must be generated. First, start the local vLLM server using this example command:
```bash
python -m vllm.entrypoints.openai.api_server --model google/gemma-3-27b-it --host 0.0.0.0 --port 8000 

```

Next, run the following command on another terminal:

```bash
python clear_anonymization/extractors/llm.py --input_dir data/m2n/m2n_data.json --model {MODEL_NAME} --mode {one_step or two_step} --dataset m2n --zero_shot 

```

Evaluation of the model results can be done by running the following example bash command:

```bash
python scripts/evaluate_llm.py --model {MODEL_NAME} --input_dir data/m2n/m2n_data.json --evaluation_type span_level --dataset m2n --mode {one_step or two_step} --zero_shot 

```

## Evaluation Results of google/gemma-3-27b-it - two_step -  all_classes


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.500 | 0.900 | 0.643 |
| address | 0.152 | 0.667 | 0.247 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.855 | 0.625 | 0.722 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.576 | 0.500 | 0.535 |
| person | 0.703 | 0.510 | 0.591 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.286 | 1.000 | 0.444 |
| vat_reg_no | 0.692 | 1.000 | 0.818 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.889 | 0.667 | 0.762 |
| Overall | 0.595 | 0.614 | 0.604 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.500 | 0.900 | 0.643 |
| address | 0.152 | 0.667 | 0.247 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.855 | 0.625 | 0.722 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.576 | 0.500 | 0.535 |
| person | 0.703 | 0.510 | 0.591 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.286 | 1.000 | 0.444 |
| vat_reg_no | 0.692 | 1.000 | 0.818 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.889 | 0.667 | 0.762 |
| Overall | 0.595 | 0.614 | 0.604 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.333 | 0.600 | 0.429 |
| address | 0.152 | 0.667 | 0.247 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.855 | 0.625 | 0.722 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.576 | 0.500 | 0.535 |
| person | 0.703 | 0.510 | 0.591 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.286 | 1.000 | 0.444 |
| vat_reg_no | 0.692 | 1.000 | 0.818 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.889 | 0.667 | 0.762 |
| Overall | 0.586 | 0.603 | 0.594 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.167 | 0.300 | 0.214 |
| address | 0.152 | 0.667 | 0.247 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.855 | 0.625 | 0.722 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.543 | 0.500 | 0.521 |
| person | 0.686 | 0.471 | 0.558 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.286 | 1.000 | 0.444 |
| vat_reg_no | 0.692 | 1.000 | 0.818 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.778 | 0.583 | 0.667 |
| Overall | 0.566 | 0.583 | 0.574 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.167 | 0.300 | 0.214 |
| address | 0.136 | 0.600 | 0.222 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.855 | 0.625 | 0.722 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.543 | 0.500 | 0.521 |
| person | 0.686 | 0.471 | 0.558 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.692 | 1.000 | 0.818 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.778 | 0.583 | 0.667 |
| Overall | 0.556 | 0.573 | 0.564 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.167 | 0.300 | 0.214 |
| address | 0.030 | 0.133 | 0.049 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.842 | 0.615 | 0.711 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.529 | 0.474 | 0.500 |
| person | 0.667 | 0.471 | 0.552 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.692 | 1.000 | 0.818 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.778 | 0.583 | 0.667 |
| Overall | 0.526 | 0.542 | 0.534 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.167 | 0.300 | 0.214 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.842 | 0.615 | 0.711 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.529 | 0.474 | 0.500 |
| person | 0.611 | 0.431 | 0.506 |
| phone_number | 0.500 | 0.444 | 0.471 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.692 | 1.000 | 0.818 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.778 | 0.583 | 0.667 |
| Overall | 0.503 | 0.519 | 0.511 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.111 | 0.200 | 0.143 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.842 | 0.615 | 0.711 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.529 | 0.474 | 0.500 |
| person | 0.611 | 0.431 | 0.506 |
| phone_number | 0.250 | 0.222 | 0.235 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.615 | 0.889 | 0.727 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.778 | 0.583 | 0.667 |
| Overall | 0.467 | 0.481 | 0.474 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.111 | 0.200 | 0.143 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.842 | 0.615 | 0.711 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.529 | 0.474 | 0.500 |
| person | 0.611 | 0.431 | 0.506 |
| phone_number | 0.062 | 0.056 | 0.059 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.615 | 0.889 | 0.727 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.778 | 0.583 | 0.667 |
| Overall | 0.457 | 0.471 | 0.464 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.111 | 0.200 | 0.143 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.842 | 0.615 | 0.711 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.471 | 0.421 | 0.444 |
| person | 0.639 | 0.451 | 0.529 |
| phone_number | 0.000 | 0.000 | 0.000 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.615 | 0.889 | 0.727 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.778 | 0.583 | 0.667 |
| Overall | 0.451 | 0.464 | 0.457 |

## Evaluation Results of google/gemma-3-27b-it - two_step -  ['person']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.614 | 0.529 | 0.568 |
| Overall | 0.614 | 0.529 | 0.568 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.614 | 0.529 | 0.568 |
| Overall | 0.614 | 0.529 | 0.568 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.614 | 0.529 | 0.568 |
| Overall | 0.614 | 0.529 | 0.568 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.614 | 0.529 | 0.568 |
| Overall | 0.614 | 0.529 | 0.568 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.614 | 0.529 | 0.568 |
| Overall | 0.614 | 0.529 | 0.568 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.591 | 0.510 | 0.547 |
| Overall | 0.591 | 0.510 | 0.547 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.545 | 0.471 | 0.505 |
| Overall | 0.545 | 0.471 | 0.505 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.523 | 0.451 | 0.484 |
| Overall | 0.523 | 0.451 | 0.484 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.500 | 0.431 | 0.463 |
| Overall | 0.500 | 0.431 | 0.463 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.614 | 0.529 | 0.568 |
| Overall | 0.614 | 0.529 | 0.568 |

## Evaluation Results of google/gemma-3-27b-it - two_step -  ['organisation']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.553 | 0.553 | 0.553 |
| Overall | 0.553 | 0.553 | 0.553 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.526 | 0.526 | 0.526 |
| Overall | 0.526 | 0.526 | 0.526 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.474 | 0.474 | 0.474 |
| Overall | 0.474 | 0.474 | 0.474 |

