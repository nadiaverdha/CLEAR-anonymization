# Evaluation Results - m2n

Generated on: 2026-01-14T08:26:28.213241

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

## Evaluation Results of gpt-5-mini-2025-08-07 - one_step -  all_classes


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.900 | 0.900 | 0.900 |
| address | 0.310 | 0.867 | 0.456 |
| business_register_number | 1.000 | 0.714 | 0.833 |
| date | 0.981 | 0.510 | 0.671 |
| email_address | 1.000 | 0.583 | 0.737 |
| organisation | 0.828 | 0.632 | 0.716 |
| person | 0.875 | 0.549 | 0.675 |
| phone_number | 0.846 | 0.611 | 0.710 |
| tax_number | 1.000 | 0.500 | 0.667 |
| vat_reg_no | 1.000 | 0.889 | 0.941 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 1.000 | 0.333 | 0.500 |
| website | 1.000 | 0.667 | 0.800 |
| Overall | 0.808 | 0.600 | 0.689 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.600 | 0.900 | 0.720 |
| address | 0.271 | 0.867 | 0.413 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.964 | 0.519 | 0.675 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.714 | 0.658 | 0.685 |
| person | 0.698 | 0.588 | 0.638 |
| phone_number | 0.611 | 0.611 | 0.611 |
| tax_number | 1.000 | 1.000 | 1.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.900 | 0.750 | 0.818 |
| Overall | 0.676 | 0.624 | 0.649 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.600 | 0.900 | 0.720 |
| address | 0.271 | 0.867 | 0.413 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.911 | 0.490 | 0.637 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.686 | 0.632 | 0.658 |
| person | 0.698 | 0.588 | 0.638 |
| phone_number | 0.611 | 0.611 | 0.611 |
| tax_number | 1.000 | 1.000 | 1.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.900 | 0.750 | 0.818 |
| Overall | 0.662 | 0.610 | 0.635 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.600 | 0.900 | 0.720 |
| address | 0.271 | 0.867 | 0.413 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.911 | 0.490 | 0.637 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.667 | 0.632 | 0.649 |
| person | 0.690 | 0.569 | 0.624 |
| phone_number | 0.611 | 0.611 | 0.611 |
| tax_number | 1.000 | 1.000 | 1.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.651 | 0.600 | 0.624 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.600 | 0.900 | 0.720 |
| address | 0.250 | 0.800 | 0.381 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.857 | 0.462 | 0.600 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.657 | 0.605 | 0.630 |
| person | 0.698 | 0.588 | 0.638 |
| phone_number | 0.611 | 0.611 | 0.611 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.629 | 0.580 | 0.603 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.467 | 0.700 | 0.560 |
| address | 0.104 | 0.333 | 0.159 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.857 | 0.462 | 0.600 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.657 | 0.605 | 0.630 |
| person | 0.674 | 0.569 | 0.617 |
| phone_number | 0.611 | 0.611 | 0.611 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.592 | 0.546 | 0.568 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.467 | 0.700 | 0.560 |
| address | 0.062 | 0.200 | 0.095 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.839 | 0.452 | 0.587 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.657 | 0.605 | 0.630 |
| person | 0.605 | 0.510 | 0.553 |
| phone_number | 0.444 | 0.444 | 0.444 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.559 | 0.515 | 0.536 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.400 | 0.600 | 0.480 |
| address | 0.062 | 0.200 | 0.095 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.839 | 0.452 | 0.587 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.629 | 0.579 | 0.603 |
| person | 0.558 | 0.471 | 0.511 |
| phone_number | 0.389 | 0.389 | 0.389 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.522 | 0.481 | 0.501 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.400 | 0.600 | 0.480 |
| address | 0.062 | 0.200 | 0.095 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.839 | 0.452 | 0.587 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.629 | 0.579 | 0.603 |
| person | 0.558 | 0.471 | 0.511 |
| phone_number | 0.278 | 0.278 | 0.278 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.515 | 0.475 | 0.494 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.200 | 0.300 | 0.240 |
| address | 0.062 | 0.200 | 0.095 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.839 | 0.452 | 0.587 |
| email_address | 0.636 | 0.583 | 0.609 |
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.628 | 0.529 | 0.574 |
| phone_number | 0.000 | 0.000 | 0.000 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.489 | 0.451 | 0.469 |

## Evaluation Results of gpt-5-mini-2025-08-07 - one_step -  ['person']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.636 | 0.686 | 0.660 |
| Overall | 0.636 | 0.686 | 0.660 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.636 | 0.686 | 0.660 |
| Overall | 0.636 | 0.686 | 0.660 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.636 | 0.686 | 0.660 |
| Overall | 0.636 | 0.686 | 0.660 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.636 | 0.686 | 0.660 |
| Overall | 0.636 | 0.686 | 0.660 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.636 | 0.686 | 0.660 |
| Overall | 0.636 | 0.686 | 0.660 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.564 | 0.608 | 0.585 |
| Overall | 0.564 | 0.608 | 0.585 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.473 | 0.510 | 0.491 |
| Overall | 0.473 | 0.510 | 0.491 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.436 | 0.471 | 0.453 |
| Overall | 0.436 | 0.471 | 0.453 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.436 | 0.471 | 0.453 |
| Overall | 0.436 | 0.471 | 0.453 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.491 | 0.529 | 0.509 |
| Overall | 0.491 | 0.529 | 0.509 |

## Evaluation Results of gpt-5-mini-2025-08-07 - one_step -  ['organisation']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.414 | 0.632 | 0.500 |
| Overall | 0.414 | 0.632 | 0.500 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.414 | 0.632 | 0.500 |
| Overall | 0.414 | 0.632 | 0.500 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.397 | 0.605 | 0.479 |
| Overall | 0.397 | 0.605 | 0.479 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.397 | 0.605 | 0.479 |
| Overall | 0.397 | 0.605 | 0.479 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.397 | 0.605 | 0.479 |
| Overall | 0.397 | 0.605 | 0.479 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.397 | 0.605 | 0.479 |
| Overall | 0.397 | 0.605 | 0.479 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.397 | 0.605 | 0.479 |
| Overall | 0.397 | 0.605 | 0.479 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.397 | 0.605 | 0.479 |
| Overall | 0.397 | 0.605 | 0.479 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.397 | 0.605 | 0.479 |
| Overall | 0.397 | 0.605 | 0.479 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.362 | 0.553 | 0.438 |
| Overall | 0.362 | 0.553 | 0.438 |

