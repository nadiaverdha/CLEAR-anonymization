# Data Quality Pipeline

Tools for improving the gold NER annotations: mining
high-precision rules from RuleChef experiment runs, using them (plus manual
patterns/corrections) to fill in missing or wrong annotations, and tracking
every change in a per-dataset changelog.

## Pipeline overview

```
collect_patterns.py      → dump existing gold annotations as text:type patterns to the files

collect_rules.py        → gather candidate rules from experiment folders
        ↓
evaluate_rules.py        → score each rule's precision/tp/fp on labeled data
        ↓
list_fp_rules.py         → pull out the rules with false positives for manual review
        ↓
patch_missing_annotations/  → apply the reviewed rules (+ manual patterns/
                               corrections/extend-prev) to the .conllu file,
                               writing a CHANGELOG.md entry per run

```
`worker.py` is not run directly — it's the `ProcessPoolExecutor` worker used
internally by `evaluate_rules.py`.


## 1. `collect_patterns.py`

Dumps existing gold annotations from a `.conllu` file as `text:type` patterns

```bash
python data_quality/collect_patterns.py \
    --input-dir /path/to/findok_train.conllu \
    --output data_quality/findok/existing_annotations/organisation_annotations.json \
    --classes organisation
```

If `--output` already exists, new patterns are appended to it rather than
overwriting (existing entries are kept, duplicates skipped).

## 2. Collect rules — `collect_rules.py`

Reads a plain-text list of experiment folders (one path per line, `#` for
comments), pulls the `rules` list out of each folder's `results_<dataset>.json`
(as referenced by that folder's `config.yaml`), and merges them into one file,
deduplicated by rule content.

```bash
python data_quality/collect_rules.py \
    --folders-file data_quality/findok/rules/organisation_experiments.txt \
    --classes organisation \
    --include-provenance \
    --output data_quality/findok/rules/organisation_rules.json
```

- `--classes` filters to rules whose name/output template mentions the given
  entity classes.
- `--dataset-name` restricts to experiments whose config output matches
  `results_<dataset-name>.json`.
- `--include-provenance` also writes `<output>.provenance.json` recording
  which experiment folder each rule came from.
- Only rules from **git-tracked** config/results files are collected, so
  uncommitted/scratch experiment runs are skipped by default.

## 3. Evaluate rules — `evaluate_rules.py`

Runs every collected rule against a labeled `.conllu` sample and records
precision, true/false positive counts, and example predictions per rule.

```bash
python data_quality/evaluate_rules.py \
    --rules-json data_quality/findok/rules/organisation_rules.json \
    --data-dir /path/to/findok_train.conllu \
    --output data_quality/findok/rules/organisation_rules_evaluated.json \
    --sample-size 50000 \
    --workers 2
```

- Samples `--sample-size` sentences (0 = all), runs rules in parallel across
  `--workers` processes.
- Checkpoints progress to `<output>.checkpoint.json` every
  `--checkpoint-every` sentences; pass `--resume` to continue an interrupted
  run instead of starting over.
- A prediction is scored `tp`/`fp` by comparing against gold labels
  (`classify_fp` in `clear_anonymization/evaluation/evaluator.py`).

## 4. Review false positives — `list_fp_rules.py`

Filters the evaluated rules JSON down to rules with `fp >= 1`, sorted by FP
count, with their FP examples — the manual-review shortlist before trusting a
rule enough to auto-apply it.

```bash
python data_quality/list_fp_rules.py \
    --rules-json data_quality/findok/rules/organisation_rules_evaluated.json \
    --output data_quality/findok/rules/organisation_rules_fp_review.json
```

## 5. Patch the dataset — `patch_missing_annotations/`

The package that actually rewrites the `.conllu` file. Run as a module:

```bash
python -m data_quality.patch_missing_annotations   \
  --input-dir /share/nverdha/data/findok/findok_train.conllu   \   
  --output /share/nverdha/data/findok/findok_train_corrected.conllu   \  
  --dataset-name findok   \   
  --patterns-file data_quality/findok/existing_annotations/organisation_annotations.json
```


```bash
python -m data_quality.patch_missing_annotations \
    --input-dir /share/nverdha/data/findok/findok_train.conllu \
    --output /share/nverdha/data/findok/findok_train_corrected.conllu  \
    --dataset-name findok \
    --rules-json data_quality/findok/rules/organisation_rules_evaluated.json \
    --rule-id rule_12 rule_47 \
    --patterns-file data_quality/findok/new_annotations/organisation_annotations_fp.json \
    --corrections "sent_042:Finanzamt Graz:O" \
    --extend-prev "sent_042:Graz:organisation"
```

Four independent ways to change annotations, all combinable in one run if wanted. BUT can be ran also separately (more preferred!)

| Flag | Format | Effect |
|---|---|---|
| `--rules-json` / `--rule-id` | rules JSON path(s), optional ID filter | Applies rules; any prediction that doesn't match an existing gold label gets tagged as a new annotation |
| `--patterns` / `--patterns-file` | `"text:type"` strings, or a JSON list of them | Tags every exact-token-boundary match of `text` in the corpus as `type`, skipping spans already annotated |
| `--corrections` | `"sent_id:text:new_type"` | Overwrites an existing label in one sentence (`new_type=O` removes it) |
| `--extend-prev` | `"sent_id:text:type"` | Tags `text` plus its immediately preceding token as one entity |

`--dataset-name` picks which changelog to append to:
`data_quality/<dataset-name>/CHANGELOG.md`. Every run appends a dated entry
with the exact command, input/output paths, and every annotation
added/changed — that changelog is the audit trail, so always give a real
`--dataset-name`.

**Safety behavior worth knowing:**
- By default (`force=False`), a token that already carries a real (non-`O`)
  tag is never overwritten — pattern/rule matches that would touch an
  already-tagged token are skipped whole (atomically; see
  `patch_missing_annotations/span_tagging.py`), not partially applied.
  `--corrections` and `--extend-prev` pass `force=True` since they're meant
  to overwrite.
- A run only logs/counts a change if something was actually written to disk
  — a match that resolves to a no-op is silently skipped, not counted.
- Re-running the same patterns against an already-patched file is expected
  to report 0 new additions.



## Directory layout (per dataset)

```
data_quality/<dataset-name>/
├── CHANGELOG.md              # append-only log of every patch run
├── existing_annotations/     # collect_patterns.py output — current gold patterns
├── new_annotations/          # curated text:type patterns for --patterns-file
└── rules/
    ├── <class>_rules.json                 # collect_rules.py output
    ├── <class>_rules.provenance.json      # which experiment each rule came from
    ├── <class>_<dataset_split>_rules_evaluated.json       # evaluate_rules.py output
    └── <class>_<dataset_split>_rules_fp_review.json       # list_fp_rules.py output
```