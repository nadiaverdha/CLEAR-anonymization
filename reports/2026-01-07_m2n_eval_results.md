# Evaluation Results - m2n

Generated on: 2026-01-07T09:26:25.103102

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

## Evaluation Results of google/gemma-3-27b-it - one_step -  all_classes


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.214 | 0.900 | 0.346 |
| address | 0.155 | 0.733 | 0.256 |
| business_register_number | 0.455 | 0.714 | 0.556 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.513 | 0.526 | 0.519 |
| person | 0.667 | 0.588 | 0.625 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.818 | 0.750 | 0.783 |
| Overall | 0.532 | 0.624 | 0.574 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.214 | 0.900 | 0.346 |
| address | 0.155 | 0.733 | 0.256 |
| business_register_number | 0.455 | 0.714 | 0.556 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.513 | 0.526 | 0.519 |
| person | 0.667 | 0.588 | 0.625 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.818 | 0.750 | 0.783 |
| Overall | 0.532 | 0.624 | 0.574 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.167 | 0.700 | 0.269 |
| address | 0.141 | 0.667 | 0.233 |
| business_register_number | 0.455 | 0.714 | 0.556 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.513 | 0.526 | 0.519 |
| person | 0.667 | 0.588 | 0.625 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.818 | 0.750 | 0.783 |
| Overall | 0.523 | 0.614 | 0.565 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.119 | 0.500 | 0.192 |
| address | 0.141 | 0.667 | 0.233 |
| business_register_number | 0.455 | 0.714 | 0.556 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.450 | 0.474 | 0.462 |
| person | 0.659 | 0.569 | 0.611 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.503 | 0.590 | 0.543 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.119 | 0.500 | 0.192 |
| address | 0.127 | 0.600 | 0.209 |
| business_register_number | 0.455 | 0.714 | 0.556 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.450 | 0.474 | 0.462 |
| person | 0.659 | 0.569 | 0.611 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.494 | 0.580 | 0.534 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.071 | 0.300 | 0.115 |
| address | 0.028 | 0.133 | 0.047 |
| business_register_number | 0.455 | 0.714 | 0.556 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.450 | 0.474 | 0.462 |
| person | 0.636 | 0.549 | 0.589 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.465 | 0.546 | 0.502 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.071 | 0.300 | 0.115 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.455 | 0.714 | 0.556 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.450 | 0.474 | 0.462 |
| person | 0.591 | 0.510 | 0.547 |
| phone_number | 0.500 | 0.444 | 0.471 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.445 | 0.522 | 0.480 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.048 | 0.200 | 0.077 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.450 | 0.474 | 0.462 |
| person | 0.545 | 0.471 | 0.505 |
| phone_number | 0.250 | 0.222 | 0.235 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.727 | 0.889 | 0.800 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.408 | 0.478 | 0.440 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.048 | 0.200 | 0.077 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.450 | 0.474 | 0.462 |
| person | 0.545 | 0.471 | 0.505 |
| phone_number | 0.062 | 0.056 | 0.059 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.727 | 0.889 | 0.800 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.399 | 0.468 | 0.431 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.048 | 0.200 | 0.077 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.824 | 0.587 | 0.685 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.400 | 0.421 | 0.410 |
| person | 0.591 | 0.510 | 0.547 |
| phone_number | 0.000 | 0.000 | 0.000 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.727 | 0.889 | 0.800 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.396 | 0.464 | 0.427 |

## Evaluation Results of google/gemma-3-27b-it - one_step -  ['person']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.369 | 0.608 | 0.459 |
| Overall | 0.369 | 0.608 | 0.459 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.369 | 0.608 | 0.459 |
| Overall | 0.369 | 0.608 | 0.459 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.369 | 0.608 | 0.459 |
| Overall | 0.369 | 0.608 | 0.459 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.357 | 0.588 | 0.444 |
| Overall | 0.357 | 0.588 | 0.444 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.357 | 0.588 | 0.444 |
| Overall | 0.357 | 0.588 | 0.444 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.333 | 0.549 | 0.415 |
| Overall | 0.333 | 0.549 | 0.415 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.310 | 0.510 | 0.385 |
| Overall | 0.310 | 0.510 | 0.385 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.286 | 0.471 | 0.356 |
| Overall | 0.286 | 0.471 | 0.356 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.286 | 0.471 | 0.356 |
| Overall | 0.286 | 0.471 | 0.356 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.345 | 0.569 | 0.430 |
| Overall | 0.345 | 0.569 | 0.430 |

## Evaluation Results of google/gemma-3-27b-it - one_step -  ['organisation']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.245 | 0.632 | 0.353 |
| Overall | 0.245 | 0.632 | 0.353 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.245 | 0.632 | 0.353 |
| Overall | 0.245 | 0.632 | 0.353 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.235 | 0.605 | 0.338 |
| Overall | 0.235 | 0.605 | 0.338 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.224 | 0.579 | 0.324 |
| Overall | 0.224 | 0.579 | 0.324 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.224 | 0.579 | 0.324 |
| Overall | 0.224 | 0.579 | 0.324 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.214 | 0.553 | 0.309 |
| Overall | 0.214 | 0.553 | 0.309 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.214 | 0.553 | 0.309 |
| Overall | 0.214 | 0.553 | 0.309 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.214 | 0.553 | 0.309 |
| Overall | 0.214 | 0.553 | 0.309 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.204 | 0.526 | 0.294 |
| Overall | 0.204 | 0.526 | 0.294 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.184 | 0.474 | 0.265 |
| Overall | 0.184 | 0.474 | 0.265 |

