import json
import shutil
from collections import Counter
from pathlib import Path

from rulechef import Task, TaskType
from rulechef.evaluation import (
    evaluate_dataset,
    evaluate_rules_individually,
    print_eval_result,
)
from rulechef.executor import RuleExecutor

from benchmarks.data import make_relation_dataset
from benchmarks.io import serialize_rules
from benchmarks.schemas import RelationOutput
from clear_anonymization.models.relationlearner import RelationLearner
from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.ner_datasets.util import build_relation_examples
from clear_anonymization.preprocess.sampling import (
    _doc_examples,
    sample_relation_few_shot,
    sample_relation_stratified,
)
from scripts.create_md_report_rules_relations import create_md_report

task = Task(
    name="German Relation Extraction",
    description=(
        "The input text contains two marked entities: <GOV>...</GOV> and <DEP>...</DEP>. "
        "The text between the tags is the entity TYPE (e.g. 'person' or 'organisation') and "
        "varies per example; it is not a fixed keyword. "
        "The task is to identify the relationship between the GOV entity and the DEP entity, "
        "where GOV is the governor/source entity and DEP is the dependent/target entity. "
        "Infer the relation from the linguistic context connecting the two marked entities. "
        "When the relation's cue phrase does not depend on entity type, write patterns that "
        "generalize across types (e.g. <GOV>\\w+</GOV> or <DEP>\\w+</DEP>) rather than "
        "hardcoding a literal entity type. "
        "Patterns should capture the relevant relation cue and the two marked entities, "
        "including necessary intervening text, while avoiding unnecessary restrictions "
        "on the entity types."
    ),
    input_schema={"text": "str"},
    output_schema=RelationOutput,
    type=TaskType.CLASSIFICATION,
    text_field="text",
)

train_data = load_ner_dataset_from_conll(
    Path("/share/nverdha/data/findok/findok_manual_train_including_relations.conllu")
)
test_data_raw = load_ner_dataset_from_conll(
    Path("/share/nverdha/data/findok/findok_manual_val_including_relations.conllu")
)
# train_data = load_ner_dataset_from_conll(Path("toy_relations.conllu"))
# test_data_raw = load_ner_dataset_from_conll(Path("toy_relations_test.conllu"))

train_examples, held_out, relation_labels = sample_relation_stratified(
    train_data.samples,
    shots_per_class=10,
    seed=42,
)
print(
    f"train={len(train_examples)} held_out={len(held_out)} labels={sorted(relation_labels)}"
)
print(f"train examples: {train_examples[:2]}")

print(train_examples[:2])

storage_dir = Path("findok_relation_learner_storage")
shutil.rmtree(storage_dir, ignore_errors=True)

eval_dataset = make_relation_dataset("test", held_out, task)
learner = RelationLearner(
    model="Qwen/Qwen3.5-35B-A3B",
    dataset_name="try",
    storage_path=storage_dir,
)

for ex in train_examples:
    learner.add_example({"text": ex["text"]}, {"label": ex["label"]})

result = learner.learn_rules(run_evaluation=False)
if result is None:
    raise RuntimeError("Learning failed!")
rules, _ = result

rules, refine_eval = learner.refine(rules, eval_dataset, max_iterations=3)
print(f"After refine: {len(rules)} rules, F1={refine_eval.micro_f1:.1%}")

rules_path = Path("reports/relations/findok_relations.json")
rules_path.parent.mkdir(parents=True, exist_ok=True)
rules_path.write_text(json.dumps({"rules": serialize_rules(rules)}, indent=2))
print(f"Saved {len(rules)} rules to {rules_path}")

for rule in rules:
    label = rule.output_template.get("label") if rule.output_template else None
    print(f"{rule.name} -> label={label!r}  pattern={rule.content}")

executor = RuleExecutor()

test_data = [
    ex for doc in test_data_raw.samples for ex in _doc_examples(doc, relation_labels)
]

test_dataset = make_relation_dataset("findok_test", test_data, task)


result = evaluate_dataset(rules, test_dataset, executor.apply_rules)
per_rule = evaluate_rules_individually(
    rules, test_dataset, executor.apply_rules, in_context=True
)
print_eval_result(result, name="held-out pairs")
print(
    f"TP={result.total_tp} FP={result.total_fp} FN={result.total_fn} "
    f"P={result.micro_precision:.1%} R={result.micro_recall:.1%} F1={result.micro_f1:.1%}"
)

create_md_report(
    Path("reports/relations/findok_relations_report.md"),
    result,
    per_rule,
    len(test_data_raw.samples),
)
