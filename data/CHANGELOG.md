# Data Changelog

Each entry documents one data processing step: what was done, how, and why.
Commit the new output file and an update to this file together.

---

## Template

```
## YYYY-MM-DD — <dataset> <split> v<N>
**Input:** `path/to/input.conllu`
**Output:** `path/to/output.conllu`
**Script:**
\```bash
python scripts/patch_missing_annotations.py \
  --data-dir path/to/input.conllu \
  --output path/to/output.conllu \
  --patterns "text:type" \
  --corrections "sent_id:text:new_type"
\```
**Changes:**
- ...
```

---

## Prior to changelog — existing files

The following files existed before this changelog was introduced.
/share/nverdha/data/bfg/new_files/findok_train.conllu


---

## 2026-06-24 — <dataset> <split> v1
**Input:** ``
**Output:** ``
**Script:**
```bash

```
**Changes:**
-
## 2026-06-24 — findok_train.conllu → findok_train_corrected.conllu
**Input:** `/share/nverdha/data/bfg/new_files/findok_train.conllu`
**Output:** `/share/nverdha/data/bfg/new_files/findok_train_corrected.conllu`
**Script:**
```bash
python scripts/patch_missing_annotations.py \
  --data-dir \
  /share/nverdha/data/bfg/new_files/findok_train.conllu \
  --output \
  /share/nverdha/data/bfg/new_files/findok_train_corrected.conllu \
  --rules-json \
  reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-26_v2/results_findok.json \
  --rule-id \
  b11b6b1a
```
**Changes:**
- rules applied from: reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-26_v2/results_findok.json (IDs: b11b6b1a)
