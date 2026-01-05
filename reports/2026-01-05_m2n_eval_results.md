# Evaluation Results - m2n

Generated on: 2026-01-05T14:50:15.407081

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
| account | 0.310 | 0.900 | 0.462 |
| address | 0.159 | 0.733 | 0.262 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.660 | 0.608 | 0.633 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.818 | 0.750 | 0.783 |
| Overall | 0.566 | 0.624 | 0.594 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.310 | 0.900 | 0.462 |
| address | 0.159 | 0.733 | 0.262 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.660 | 0.608 | 0.633 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.818 | 0.750 | 0.783 |
| Overall | 0.566 | 0.624 | 0.594 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.276 | 0.800 | 0.410 |
| address | 0.159 | 0.733 | 0.262 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.660 | 0.608 | 0.633 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.818 | 0.750 | 0.783 |
| Overall | 0.563 | 0.620 | 0.590 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.241 | 0.700 | 0.359 |
| address | 0.159 | 0.733 | 0.262 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.514 | 0.500 | 0.507 |
| person | 0.644 | 0.569 | 0.604 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.545 | 0.600 | 0.571 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.241 | 0.700 | 0.359 |
| address | 0.145 | 0.667 | 0.238 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.514 | 0.500 | 0.507 |
| person | 0.644 | 0.569 | 0.604 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.535 | 0.590 | 0.561 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.103 | 0.300 | 0.154 |
| address | 0.043 | 0.200 | 0.071 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.500 | 0.474 | 0.486 |
| person | 0.609 | 0.549 | 0.577 |
| phone_number | 0.688 | 0.611 | 0.647 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.495 | 0.546 | 0.519 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.103 | 0.300 | 0.154 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.500 | 0.474 | 0.486 |
| person | 0.565 | 0.510 | 0.536 |
| phone_number | 0.500 | 0.444 | 0.471 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.471 | 0.519 | 0.494 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.069 | 0.200 | 0.103 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.500 | 0.474 | 0.486 |
| person | 0.543 | 0.490 | 0.515 |
| phone_number | 0.375 | 0.333 | 0.353 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.443 | 0.488 | 0.465 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.069 | 0.200 | 0.103 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.500 | 0.474 | 0.486 |
| person | 0.543 | 0.490 | 0.515 |
| phone_number | 0.188 | 0.167 | 0.176 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.434 | 0.478 | 0.455 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.069 | 0.200 | 0.103 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.811 | 0.577 | 0.674 |
| email_address | 0.778 | 0.583 | 0.667 |
| organisation | 0.444 | 0.421 | 0.432 |
| person | 0.609 | 0.549 | 0.577 |
| phone_number | 0.000 | 0.000 | 0.000 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.818 | 1.000 | 0.900 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.333 | 0.333 | 0.333 |
| website | 0.636 | 0.583 | 0.609 |
| Overall | 0.428 | 0.471 | 0.448 |

## Evaluation Results of google/gemma-3-27b-it - one_step -  ['person', 'organisation']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.639 | 0.605 | 0.622 |
| person | 0.625 | 0.588 | 0.606 |
| Overall | 0.631 | 0.596 | 0.613 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.639 | 0.605 | 0.622 |
| person | 0.625 | 0.588 | 0.606 |
| Overall | 0.631 | 0.596 | 0.613 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.629 | 0.579 | 0.603 |
| person | 0.612 | 0.588 | 0.600 |
| Overall | 0.619 | 0.584 | 0.601 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.583 | 0.553 | 0.568 |
| person | 0.604 | 0.569 | 0.586 |
| Overall | 0.595 | 0.562 | 0.578 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.583 | 0.553 | 0.568 |
| person | 0.604 | 0.569 | 0.586 |
| Overall | 0.595 | 0.562 | 0.578 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.571 | 0.549 | 0.560 |
| Overall | 0.571 | 0.539 | 0.555 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.531 | 0.510 | 0.520 |
| Overall | 0.548 | 0.517 | 0.532 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.510 | 0.490 | 0.500 |
| Overall | 0.536 | 0.506 | 0.520 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.571 | 0.526 | 0.548 |
| person | 0.510 | 0.490 | 0.500 |
| Overall | 0.536 | 0.506 | 0.520 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.514 | 0.474 | 0.493 |
| person | 0.612 | 0.588 | 0.600 |
| Overall | 0.571 | 0.539 | 0.555 |

## Evaluation Results of google/gemma-3-27b-it - one_step -  ['person']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.574 | 0.529 | 0.551 |
| Overall | 0.574 | 0.529 | 0.551 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.574 | 0.529 | 0.551 |
| Overall | 0.574 | 0.529 | 0.551 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.574 | 0.529 | 0.551 |
| Overall | 0.574 | 0.529 | 0.551 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.574 | 0.529 | 0.551 |
| Overall | 0.574 | 0.529 | 0.551 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.574 | 0.529 | 0.551 |
| Overall | 0.574 | 0.529 | 0.551 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.532 | 0.490 | 0.510 |
| Overall | 0.532 | 0.490 | 0.510 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.489 | 0.451 | 0.469 |
| Overall | 0.489 | 0.451 | 0.469 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.468 | 0.431 | 0.449 |
| Overall | 0.468 | 0.431 | 0.449 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.468 | 0.431 | 0.449 |
| Overall | 0.468 | 0.431 | 0.449 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.574 | 0.529 | 0.551 |
| Overall | 0.574 | 0.529 | 0.551 |

## Evaluation Results of google/gemma-3-27b-it - two_step -  all_classes


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.237 | 0.900 | 0.375 |
| address | 0.159 | 0.733 | 0.262 |
| business_register_number | 0.714 | 0.714 | 0.714 |
| date | 0.835 | 0.635 | 0.721 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.545 | 0.632 | 0.585 |
| person | 0.659 | 0.569 | 0.611 |
| phone_number | 0.733 | 0.611 | 0.667 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.643 | 1.000 | 0.783 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.800 | 0.667 | 0.727 |
| Overall | 0.555 | 0.647 | 0.598 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.243 | 0.900 | 0.383 |
| address | 0.159 | 0.733 | 0.262 |
| business_register_number | 0.625 | 0.714 | 0.667 |
| date | 0.835 | 0.635 | 0.721 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.545 | 0.632 | 0.585 |
| person | 0.659 | 0.569 | 0.611 |
| phone_number | 0.733 | 0.611 | 0.667 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.643 | 1.000 | 0.783 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.800 | 0.667 | 0.727 |
| Overall | 0.555 | 0.647 | 0.598 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.167 | 0.600 | 0.261 |
| address | 0.145 | 0.667 | 0.238 |
| business_register_number | 0.556 | 0.714 | 0.625 |
| date | 0.835 | 0.635 | 0.721 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.523 | 0.605 | 0.561 |
| person | 0.659 | 0.569 | 0.611 |
| phone_number | 0.733 | 0.611 | 0.667 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.643 | 1.000 | 0.783 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.800 | 0.667 | 0.727 |
| Overall | 0.541 | 0.631 | 0.582 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.083 | 0.300 | 0.130 |
| address | 0.145 | 0.667 | 0.238 |
| business_register_number | 0.556 | 0.714 | 0.625 |
| date | 0.835 | 0.635 | 0.721 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.500 | 0.605 | 0.548 |
| person | 0.643 | 0.529 | 0.581 |
| phone_number | 0.733 | 0.611 | 0.667 |
| tax_number | 0.667 | 1.000 | 0.800 |
| vat_reg_no | 0.643 | 1.000 | 0.783 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.523 | 0.610 | 0.563 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.083 | 0.300 | 0.130 |
| address | 0.130 | 0.600 | 0.214 |
| business_register_number | 0.556 | 0.714 | 0.625 |
| date | 0.835 | 0.635 | 0.721 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.500 | 0.605 | 0.548 |
| person | 0.643 | 0.529 | 0.581 |
| phone_number | 0.733 | 0.611 | 0.667 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.600 | 1.000 | 0.750 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.515 | 0.600 | 0.554 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.083 | 0.300 | 0.130 |
| address | 0.029 | 0.133 | 0.048 |
| business_register_number | 0.556 | 0.714 | 0.625 |
| date | 0.823 | 0.625 | 0.710 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.489 | 0.579 | 0.530 |
| person | 0.628 | 0.529 | 0.574 |
| phone_number | 0.733 | 0.611 | 0.667 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.600 | 1.000 | 0.750 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.488 | 0.569 | 0.526 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.083 | 0.300 | 0.130 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.556 | 0.714 | 0.625 |
| date | 0.810 | 0.615 | 0.699 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.489 | 0.579 | 0.530 |
| person | 0.581 | 0.490 | 0.532 |
| phone_number | 0.533 | 0.444 | 0.485 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.600 | 1.000 | 0.750 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.465 | 0.542 | 0.501 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.056 | 0.200 | 0.087 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.810 | 0.615 | 0.699 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.489 | 0.579 | 0.530 |
| person | 0.558 | 0.471 | 0.511 |
| phone_number | 0.267 | 0.222 | 0.242 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.600 | 1.000 | 0.750 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.433 | 0.505 | 0.466 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.056 | 0.200 | 0.087 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.810 | 0.615 | 0.699 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.489 | 0.579 | 0.530 |
| person | 0.558 | 0.471 | 0.511 |
| phone_number | 0.067 | 0.056 | 0.061 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.600 | 1.000 | 0.750 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.424 | 0.495 | 0.457 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| account | 0.056 | 0.200 | 0.087 |
| address | 0.000 | 0.000 | 0.000 |
| business_register_number | 0.000 | 0.000 | 0.000 |
| date | 0.810 | 0.615 | 0.699 |
| email_address | 0.824 | 0.583 | 0.683 |
| organisation | 0.444 | 0.526 | 0.482 |
| person | 0.651 | 0.549 | 0.596 |
| phone_number | 0.000 | 0.000 | 0.000 |
| tax_number | 0.000 | 0.000 | 0.000 |
| vat_reg_no | 0.600 | 1.000 | 0.750 |
| vehicle_identification_number | 1.000 | 1.000 | 1.000 |
| vehicle_license | 0.500 | 0.333 | 0.400 |
| website | 0.700 | 0.583 | 0.636 |
| Overall | 0.427 | 0.498 | 0.460 |

## Evaluation Results of google/gemma-3-27b-it - two_step -  ['person', 'organisation']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.469 | 0.605 | 0.529 |
| person | 0.588 | 0.588 | 0.588 |
| Overall | 0.530 | 0.596 | 0.561 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.469 | 0.605 | 0.529 |
| person | 0.588 | 0.588 | 0.588 |
| Overall | 0.530 | 0.596 | 0.561 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.469 | 0.605 | 0.529 |
| person | 0.588 | 0.588 | 0.588 |
| Overall | 0.530 | 0.596 | 0.561 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.429 | 0.553 | 0.483 |
| person | 0.588 | 0.588 | 0.588 |
| Overall | 0.510 | 0.573 | 0.540 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.429 | 0.553 | 0.483 |
| person | 0.588 | 0.588 | 0.588 |
| Overall | 0.510 | 0.573 | 0.540 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.429 | 0.553 | 0.483 |
| person | 0.549 | 0.549 | 0.549 |
| Overall | 0.490 | 0.551 | 0.519 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.429 | 0.553 | 0.483 |
| person | 0.510 | 0.510 | 0.510 |
| Overall | 0.470 | 0.528 | 0.497 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.429 | 0.553 | 0.483 |
| person | 0.471 | 0.471 | 0.471 |
| Overall | 0.450 | 0.506 | 0.476 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.429 | 0.553 | 0.483 |
| person | 0.471 | 0.471 | 0.471 |
| Overall | 0.450 | 0.506 | 0.476 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| organisation | 0.388 | 0.500 | 0.437 |
| person | 0.549 | 0.549 | 0.549 |
| Overall | 0.470 | 0.528 | 0.497 |

## Evaluation Results of google/gemma-3-27b-it - two_step -  ['person']


### Threshold 0.1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.622 | 0.549 | 0.583 |
| Overall | 0.622 | 0.549 | 0.583 |


### Threshold 0.2

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.622 | 0.549 | 0.583 |
| Overall | 0.622 | 0.549 | 0.583 |


### Threshold 0.3

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.622 | 0.549 | 0.583 |
| Overall | 0.622 | 0.549 | 0.583 |


### Threshold 0.4

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.622 | 0.549 | 0.583 |
| Overall | 0.622 | 0.549 | 0.583 |


### Threshold 0.5

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.622 | 0.549 | 0.583 |
| Overall | 0.622 | 0.549 | 0.583 |


### Threshold 0.6

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.600 | 0.529 | 0.562 |
| Overall | 0.600 | 0.529 | 0.562 |


### Threshold 0.7

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.556 | 0.490 | 0.521 |
| Overall | 0.556 | 0.490 | 0.521 |


### Threshold 0.8

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.511 | 0.451 | 0.479 |
| Overall | 0.511 | 0.451 | 0.479 |


### Threshold 0.9

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.511 | 0.451 | 0.479 |
| Overall | 0.511 | 0.451 | 0.479 |


### Threshold 1

| Class | Precision | Recall | F1 |
|-----|---------|------|--|
| person | 0.622 | 0.549 | 0.583 |
| Overall | 0.622 | 0.549 | 0.583 |

