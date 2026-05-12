import io
import os
import signal
import sys
import time
from contextlib import contextmanager
from typing import List, Literal


@contextmanager
def _suppress_stdout():
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = old


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
        self._patch_regex_timeout()

    def _patch_regex_timeout(self, timeout_secs: int = 5) -> None:
        original = self.learner.executor._execute_regex_rule
        timed_out_rules: set[str] = set()

        def _execute_with_timeout(rule, input_data, text_field=None):
            if rule.id in timed_out_rules:
                return []

            def _handler(s, f):
                raise TimeoutError()

            old = signal.signal(signal.SIGALRM, _handler)
            signal.alarm(timeout_secs)
            try:
                return original(rule, input_data, text_field)
            except TimeoutError:
                timed_out_rules.add(rule.id)
                print(f"   ⚠ Regex timeout ({timeout_secs}s): {rule.name} — skipping")
                return []
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old)

        self.learner.executor._execute_regex_rule = _execute_with_timeout

    def fit_batched(
        self,
        train_data,
        eval_dataset,
        batch_size=40,
        refine_per_batch=1,
        refine_every=1,
        iteration_callback=None,
        batch_callback=None,
        audit_interval=0,
        seed_rules=None,
        start_batch=0,
        synthesize_per_batch=False,
    ):
        if seed_rules is not None:
            self.dataset.rules = seed_rules
        batches = [
            train_data[i : i + batch_size]
            for i in range(0, len(train_data), batch_size)
        ]
        t0 = time.time()
        result = (list(seed_rules), None) if (seed_rules and start_batch > 0) else None
        for batch_idx, batch in enumerate(batches):
            if batch_idx < start_batch:
                continue
            for ex in batch:
                self.add_example({"text": ex["text"]}, {"entities": ex["entities"]})
            if synthesize_per_batch:
                existing_rules = list(self.dataset.rules) if self.dataset.rules else []
                batch_result = self.learn_rules(
                    run_evaluation=False, incremental_only=False
                )
                if batch_result:
                    new_rules, _ = batch_result
                    merged = self.learner._merge_patch(existing_rules, new_rules)
                    self.dataset.rules = merged
                    batch_result = (merged, _)
                    print(
                        f"  Merged: {len(existing_rules)} existing + {len(new_rules)} new = {len(merged)} rules"
                    )
            else:
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

                if refine_per_batch > 0 and batch_idx % refine_every == 0:
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

    def apply_feedback_patch(self, rules, eval_dataset):
        eval_result = self.learner._evaluate_rules(rules, eval_dataset)
        f1_before = eval_result.micro_f1 if eval_result else 0.0
        failures = eval_result.failures if eval_result and eval_result.failures else []
        # Only send rules that have feedback to keep the prompt small and focused
        targeted_ids = {
            f.target_id
            for f in eval_dataset.structured_feedback
            if f.level == "rule" and f.target_id
        }
        rules_for_prompt = (
            [r for r in rules if r.id in targeted_ids] if targeted_ids else rules
        )

        print(
            f"  Feedback patch: {len(rules_for_prompt)} targeted rule(s), "
            f"{len(failures)} failures, F1 before={f1_before:.1%}"
        )
        patch = self.learner.synthesize_patch_ruleset(
            rules_for_prompt,
            failures=failures,
            dataset=eval_dataset,
        )
        if isinstance(patch, tuple):
            patch = patch[0]
        if not patch:
            print("No feedback patches generated.")
            return rules
        merged = self.learner._merge_patch(rules, patch)
        original_by_name = {r.name: r.id for r in rules}
        for r in merged:
            if r.name in original_by_name:
                r.id = original_by_name[r.name]
        after_result = self.learner._evaluate_rules(merged, eval_dataset)
        f1_after = after_result.micro_f1 if after_result else 0.0
        if f1_after < f1_before:
            print(
                f"  Feedback patch rejected (F1 {f1_before:.1%} → {f1_after:.1%}), keeping original"
            )
            return rules
        print(
            f"  Feedback patch accepted: {len(rules)} → {len(merged)} rules, F1 {f1_before:.1%} → {f1_after:.1%}"
        )
        return merged

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
