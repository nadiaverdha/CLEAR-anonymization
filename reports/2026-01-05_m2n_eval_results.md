# Evaluation Results - m2n

Generated on: 2026-01-05T13:47:43.762034

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
