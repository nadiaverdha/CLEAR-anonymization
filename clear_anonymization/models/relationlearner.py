import os
import signal
import time
import uuid
from pathlib import Path
from typing import Literal

from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rulechef import RuleChef, Task, TaskType
from rulechef.coordinator import AgenticCoordinator
from rulechef.core import Dataset, Example, RuleFormat
from rulechef.executor import RuleExecutor
from rulechef.training_logger import TrainingDataLogger

from benchmarks.schemas import RelationOutput
from clear_anonymization.ner_datasets import load_ner_dataset_from_conll
from clear_anonymization.ner_datasets.util import recreate_sent_relations

RULE_FORMATS = {
    "regex": [RuleFormat.REGEX],
    "code": [RuleFormat.CODE],
    "spacy": [RuleFormat.SPACY],
}


class RelationLearner(RuleChef):
    def __init__(
        self,
        model,
        dataset_name="relations",
        base_url="http://localhost:8000/v1",
        use_grex: bool = True,
        max_rules: int = 100,
        max_samples: int = 50,
        max_counter_examples: int = 50,
        logger: TrainingDataLogger | None = None,
        storage_path: str = ".",
        sampling_strategy: str = "balanced",
        synthesis_strategy: str = "bulk",
        selected_classes: list[str] | None = None,
        agentic: bool = False,
        enable_prune: bool = False,
        audit_interval: int = 0,
        enable_critic: bool = False,
        critic_interval: int = 0,
        rule_format: str = "regex",
        use_spacy_ner: bool = True,
        spacy_model: str = "de_core_news_sm",
        temperature: float = 0.0,
    ):
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
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY") or "EMPTY", base_url=base_url
        )
        coordinator = None
        if agentic:
            coordinator = AgenticCoordinator(
                client,
                model=model,
                prune_after_learn=enable_prune,
                audit_interval=audit_interval,
                enable_critic=enable_critic,
                critic_interval=critic_interval,
                verbose=True,
            )
        super().__init__(
            task=task,
            client=client,
            dataset_name=dataset_name,
            model=model,
            allowed_formats=RULE_FORMATS[rule_format],
            use_grex=use_grex,
            max_rules=max_rules,
            max_samples=max_samples,
            max_counter_examples=max_counter_examples,
            coordinator=coordinator,
            training_logger=logger,
            storage_path=storage_path,
            sampling_strategy=sampling_strategy,
            synthesis_strategy=synthesis_strategy,
            use_spacy_ner=use_spacy_ner,
            spacy_model=spacy_model,
            temperature=temperature,
        )

    def fit_batched(
        self,
        train_examples,
        eval_dataset,
        batch_size=40,
        refine_per_batch=1,
        refine_every=1,
        iteration_callback=None,
        batch_callback=None,
        seed_rules=None,
        start_batch=0,
        audit_interval=0,
        holdout_fraction=0.0,
        split_seed=42,
    ):
        if seed_rules is not None:
            self.dataset.rules = seed_rules
        batches = [
            train_examples[i : i + batch_size]
            for i in range(0, len(train_examples), batch_size)
        ]
        t0 = time.time()
        result = (list(seed_rules), None) if (seed_rules and start_batch > 0) else None
        for batch_idx, batch in enumerate(batches):
            if batch_idx < start_batch:
                continue
            for ex in batch:
                self.add_example({"text": ex["text"]}, {"label": ex["label"]})
            batch_result = self.learn_rules(
                run_evaluation=False,
                incremental_only=(batch_idx > 0 or seed_rules is not None),
            )
            if self.dataset.rules:
                MAX_EXAMPLES = batch_size * 2
                if len(self.dataset.examples) > MAX_EXAMPLES:
                    self.dataset.examples = self.dataset.examples[-MAX_EXAMPLES:]
            else:
                self.dataset.examples.clear()
            if batch_result:
                result = batch_result

                rules_so_far, _ = result

                print(
                    f"  Batch {batch_idx + 1}/{len(batches)}: {len(rules_so_far)} rules synthesized"
                )

                if refine_per_batch > 0 and batch_idx % refine_every == 0:
                    rules_so_far, refine_eval = self.refine(
                        rules_so_far,
                        eval_dataset,
                        max_iterations=refine_per_batch,
                        iteration_callback=iteration_callback,
                    )
                    self.dataset.rules = rules_so_far
                    result = (rules_so_far, _)
                    print(
                        f"  After refine: {len(rules_so_far)} rules, F1={refine_eval.micro_f1:.1%}"
                    )
                if batch_callback is not None:
                    batch_callback(batch_idx, rules_so_far)
        t_learn = time.time() - t0
        if result is None:
            print("ERROR: Learning failed!")
            return
        rules, _ = result
        print(f"\nSynthesis complete ({t_learn:.1f}s)")
        print(f"  Rules generated: {len(rules)}")
        return rules, t_learn

    def refine(
        self,
        rules,
        eval_dataset,
        max_iterations=3,
        iteration_callback=None,
        holdout_fraction=0.0,
        split_seed=42,
    ):
        return self.learner.evaluate_and_refine(
            rules,
            eval_dataset,
            max_iterations=max_iterations,
            coordinator=self.coordinator,
            iteration_callback=iteration_callback,
        )
