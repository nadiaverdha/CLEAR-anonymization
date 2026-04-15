import os
import time
from typing import List, Literal

from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from rulechef import RuleChef, Task, TaskType
from rulechef.coordinator import AgenticCoordinator
from rulechef.core import RuleFormat
from rulechef.training_logger import TrainingDataLogger


class Entity(BaseModel):
    text: str = Field(description="The matched text span")
    start: int = Field(description="Start character offset")
    end: int = Field(description="End character offset")
    type: str = Field(description="Entity label")


class NEROutput(BaseModel):
    entities: List[Entity]


class NERLearner(RuleChef):
    def __init__(
        self,
        model: str,
        dataset_name: str = "ler",
        base_url: str = "http://localhost:8000/v1",
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
    ):

        task = Task(
            name="German Legal Named Entity Recognition",
            description=f"Recognize named entities in German legal text. Entities to look for: {', '.join(sorted(selected_classes))}.",
            input_schema={"text": "str"},
            output_schema=NEROutput,
            type=TaskType.NER,
            text_field="text",
        )
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY") or "EMPTY",
            base_url=base_url,
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
            allowed_formats=[RuleFormat.REGEX],
            use_grex=use_grex,
            max_rules=max_rules,
            max_samples=max_samples,
            max_counter_examples=max_counter_examples,
            coordinator=coordinator,
            training_logger=logger,
            storage_path=storage_path,
            sampling_strategy=sampling_strategy,
            synthesis_strategy=synthesis_strategy,
        )

    def fit_batched(
        self,
        train_data,
        eval_dataset,
        batch_size=40,
        refine_per_batch=1,
        iteration_callback=None,
        audit_interval=0,
        seed_rules=None,
    ):
        if seed_rules is not None:
            self.dataset.rules = seed_rules
        batches = [
            train_data[i : i + batch_size]
            for i in range(0, len(train_data), batch_size)
        ]
        t0 = time.time()
        result = None
        for batch_idx, batch in enumerate(batches):
            for ex in batch:
                self.add_example({"text": ex["text"]}, {"entities": ex["entities"]})
            batch_result = self.learn_rules(
                run_evaluation=False,
                incremental_only=(batch_idx > 0 or seed_rules is not None),
            )
            # Clear so next batch only sees its own examples
            self.dataset.examples.clear()
            if batch_result:
                result = batch_result
                rules_so_far, _ = result
                print(
                    f"  Batch {batch_idx + 1}/{len(batches)}: {len(rules_so_far)} rules synthesized"
                )

                if refine_per_batch > 0:
                    rules_so_far, refine_eval = self.refine(
                        rules_so_far,
                        eval_dataset,
                        max_iterations=refine_per_batch,
                        iteration_callback=iteration_callback,
                        audit_interval=audit_interval,
                    )
                    self.dataset.rules = rules_so_far
                    result = (rules_so_far, _)
                    print(
                        f"  After refine: {len(rules_so_far)} rules, F1={refine_eval.micro_f1:.1%}"
                    )
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
        audit_interval=0,
    ):
        return self.learner.evaluate_and_refine(
            rules,
            eval_dataset,
            max_iterations=max_iterations,
            coordinator=self.coordinator,
            iteration_callback=iteration_callback,
        )
