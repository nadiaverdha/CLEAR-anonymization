# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-03-29T16:35:45.411651

### Legend
🟢 Strong (F1 ≥ 0.8)  
🟡 Medium (0.5 ≤ F1 < 0.8)  
🔴 Weak (F1 < 0.5)

---

### Configuration

| Parameter | Value |
|-----------|-------|
| Shots per class | 20 |
| Training examples | 20 |
| Test examples | 50 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 10 |
| Refinement iterations | 10 |
| Seed | 42 |
| Agentic | True|
| Enable Critic | False |
| Enable Prune | False|
| Critic Interval | 0 |
| Audit Interval | 0|
| Use GREX | True |

### Results

| Metric | Value |
|--------|-------|
| Accuracy (exact match) | 52.0% |
| Coverage | 118.0% (59/50 got a label) |
| Micro Precision | 0.678 |
| Micro Recall | 0.571 |
| Micro F1 | 0.620 |
| Macro F1 | 0.620 |

---

## 📊 Summary

| Rule | Score | F1 | Precision | Recall | Matches |
|------|-------|----|----------|--------|--------|
| `German_Org_GeneralWithSuffix` | 🔴 Weak | 0.347 | 0.607 | 0.243 | 28 |
| `German_Finanzamt_Full` | 🔴 Weak | 0.228 | 1.000 | 0.129 | 9 |
| `German_Org_NameSectorNoSuffix` | 🔴 Weak | 0.188 | 0.533 | 0.114 | 15 |
| `German_FA_Abbreviation` | 🔴 Weak | 0.156 | 0.857 | 0.086 | 7 |
| `German_Org_NameSector` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |
| `German_BG_Gericht` | 🔴 Weak | 0.000 | 0.000 | 0.000 | 0 |

---

## `German_Org_GeneralWithSuffix`

🔴 Weak rule

**F1:** 0.347 | **Precision:** 0.607 | **Recall:** 0.243  

