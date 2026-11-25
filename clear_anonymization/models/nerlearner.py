import inspect
import os
import tempfile
import time

from openai import OpenAI
from rulechef import RuleChef, Task, TaskType
from rulechef.coordinator import AgenticCoordinator
from rulechef.core import RuleFormat
from rulechef.training_logger import TrainingDataLogger

from benchmarks.schemas import NEROutput

RULE_FORMATS = {
    "regex": RuleFormat.REGEX,
    "code": RuleFormat.CODE,
    "spacy": RuleFormat.SPACY,
}


class NERLearner(RuleChef):
    def __init__(
        self,
        model: str,
        selected_classes: list[str],
        dataset_name: str = "ler",
        base_url: str = "http://localhost:8000/v1",
        use_grex: bool = True,
        max_rules: int = 10,
        max_samples: int = 50,
        max_counter_examples: int = 10,
        interleave_failures: bool = False,
        logger: TrainingDataLogger | None = None,
        storage_path: str | None = None,
        sampling_strategy: str = "balanced",
        synthesis_strategy: str = "bulk",
        agentic: bool = False,
        enable_prune: bool = False,
        audit_interval: int = 0,
        enable_critic: bool = False,
        critic_interval: int = 0,
        rule_format: str = "regex",
        use_spacy_ner: bool = True,
        spacy_model: str = "de_core_news_sm",
        temperature: float = 0.0,
        seed: int | None = 42,
        overlap_strategy: str | None = "longest",
        cross_type_overlaps: bool = True,
        scope_to_rule_labels: bool = True,
        max_rules_per_class: int = 5,
        concise_reasoning: bool = True,
        context_window: int | None = 64000,
        frequency_penalty: float | None = None,
    ):

        task = Task(
            name="German Legal Named Entity Recognition",
            description=f"Recognize named entities in German legal text. Entities to look for: {', '.join(sorted(selected_classes))}. German capitalizes all nouns, so rules must use strong context anchors ",
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
        if not agentic and (
            enable_prune or enable_critic or audit_interval or critic_interval
        ):
            print(
                "⚠ enable_prune / audit_interval / enable_critic / critic_interval "
                "have no effect without agentic=True"
            )
        extra_kwargs = {}
        if frequency_penalty is not None:
            if "frequency_penalty" in inspect.signature(RuleChef.__init__).parameters:
                extra_kwargs["frequency_penalty"] = frequency_penalty
            else:
                raise ValueError(
                    "frequency_penalty is set, but the installed rulechef does not support it"
                )
        super().__init__(
            task=task,
            client=client,
            dataset_name=dataset_name,
            model=model,
            allowed_formats=[RULE_FORMATS[r.strip()] for r in rule_format.split(",")],
            use_grex=use_grex,
            max_rules=max_rules,
            max_samples=max_samples,
            max_counter_examples=max_counter_examples,
            interleave_failures=interleave_failures,
            coordinator=coordinator,
            training_logger=logger,
            storage_path=storage_path or tempfile.mkdtemp(prefix="rulechef_"),
            sampling_strategy=sampling_strategy,
            synthesis_strategy=synthesis_strategy,
            use_spacy_ner=use_spacy_ner,
            spacy_model=spacy_model,
            temperature=temperature,
            seed=seed,
            overlap_strategy=overlap_strategy,
            cross_type_overlaps=cross_type_overlaps,
            scope_to_rule_labels=scope_to_rule_labels,
            target_labels=sorted(selected_classes),
            max_rules_per_class=max_rules_per_class,
            # frequency_penalty=frequency_penalty,
            concise_reasoning=concise_reasoning,
            # vLLM --max-model-len; lets rulechef pick a smaller patch prompt
            # variant instead of sending one the server rejects (HTTP 400).
            context_window=context_window,
            **extra_kwargs,
        )

    def _learn_batch(self, eval_dataset, incremental, guard_drop=None):
        """learn_rules for one batch; if guard_drop is set, reject patches that drop
        eval F1 by more than guard_drop and keep the previous rules."""
        prev_rules = list(self.dataset.rules)
        guard = guard_drop is not None and bool(prev_rules)
        if guard:
            prev_f1 = self.learner._evaluate_rules(prev_rules, eval_dataset).micro_f1
        batch_result = self.learn_rules(
            run_evaluation=False, incremental_only=incremental
        )
        if not batch_result:
            return None
        new_rules = batch_result[0]
        if guard:
            new_f1 = self.learner._evaluate_rules(new_rules, eval_dataset).micro_f1
            if prev_f1 - new_f1 > guard_drop:
                print(
                    f"  ⛔ Batch patch rejected: F1 {prev_f1:.1%} → {new_f1:.1%}, keeping previous rules"
                )
                self.dataset.rules = prev_rules
                return prev_rules
            print(f"  ✓ Batch patch accepted: F1 {prev_f1:.1%} → {new_f1:.1%}")
        return new_rules

    def fit_batched(
        self,
        train_data,
        eval_dataset,
        batch_size=40,
        past_batches=2,
        refine_per_batch=1,
        refine_every=1,
        iteration_callback=None,
        batch_callback=None,
        audit_interval=0,
        seed_rules=None,
        start_batch=0,
        holdout_fraction=0.0,
        split_seed=42,
        max_patch_f1_drop=None,
    ):
        if batch_size <= 0:
            raise ValueError(f"batch_size must be > 0, got {batch_size}")
        if refine_every <= 0:
            raise ValueError(f"refine_every must be > 0, got {refine_every}")
        if seed_rules is not None:
            self.dataset.rules = seed_rules
        batches = [
            train_data[i : i + batch_size]
            for i in range(0, len(train_data), batch_size)
        ]
        if not 0 <= start_batch <= len(batches):
            raise ValueError(
                f"start_batch must be in [0, {len(batches)}], got {start_batch}"
            )
        # on resume, restore the examples the skipped batches would have left
        # (same window as step 3 below: last `past_batches` batches, all if < 0)
        if start_batch > 0 and past_batches != 0:
            first = 0 if past_batches < 0 else max(0, start_batch - past_batches)
            for prev in batches[first:start_batch]:
                for ex in prev:
                    self.add_example({"text": ex["text"]}, {"entities": ex["entities"]})

        rules = list(seed_rules) if seed_rules is not None else None
        t0 = time.time()
        for batch_idx, batch in enumerate(batches):
            if batch_idx < start_batch:
                continue
            # 1. add this batch's examples
            for ex in batch:
                self.add_example({"text": ex["text"]}, {"entities": ex["entities"]})
            # 2. synthesize (batch 0 without seed rules) or patch (all later batches)
            batch_rules = self._learn_batch(
                eval_dataset,
                incremental=(batch_idx > 0 or seed_rules is not None),
                guard_drop=max_patch_f1_drop if batch_idx > 0 else None,
            )
            # 3. keep only the last `past_batches` batches for the next synthesis
            # (past_batches < 0: keep all, 0: next batch sees only its own examples)
            if past_batches >= 0:
                keep = batch_size * past_batches
                self.dataset.examples = (
                    self.dataset.examples[-keep:] if keep > 0 else []
                )

            if batch_rules is None:
                continue

            rules = batch_rules
            print(
                f"  Batch {batch_idx + 1}/{len(batches)}: {len(rules)} rules synthesized"
            )
            # 4. optional refinement on the eval set
            if refine_per_batch > 0 and batch_idx % refine_every == 0:
                rules, refine_eval = self.refine(
                    rules,
                    eval_dataset,
                    max_iterations=refine_per_batch,
                    iteration_callback=iteration_callback,
                    audit_interval=audit_interval,
                    holdout_fraction=holdout_fraction,
                    split_seed=split_seed,
                )
                self.dataset.rules = rules
                print(
                    f"  After refine: {len(rules)} rules, F1={refine_eval.micro_f1:.1%}"
                )
            # 5. report to the pipeline (dev/test eval, best-batch selection, checkpoint)
            if batch_callback is not None:
                batch_callback(batch_idx, rules)
        t_learn = time.time() - t0
        if rules is None:
            print("ERROR: Learning failed!")
            return

        print(f"\nSynthesis complete ({t_learn:.1f}s)")
        print(f"  Rules generated: {len(rules)}")
        return rules, t_learn

    def apply_feedback_patch(self, rules, eval_dataset):
        """Patch `rules` with the feedback/corrections in self.dataset. With rule-level
        feedback only the targeted rules may change. Rejected if eval F1 drops."""
        targeted_ids = {
            f.target_id for f in self.dataset.structured_feedback if f.level == "rule"
        }
        to_patch = [r for r in rules if r.id in targeted_ids] or rules
        other_names = {r.name for r in rules} - {r.name for r in to_patch}
        before = self.learner._evaluate_rules(rules, eval_dataset)
        f1_before = before.micro_f1
        failures = before.failures or []

        guidance = "Only modify or replace the given rule(s). Do NOT create new rules."
        for attempt in range(2):
            extra = (
                " Your previous answer contained an invalid regex. Close every [ and (, "
                "and escape backslashes and quotes correctly for JSON."
                if attempt > 0
                else ""
            )
            patch, deleted_names = self.learner.synthesize_patch_ruleset(
                to_patch,
                failures=failures,
                dataset=self.dataset,
                guidance=guidance + extra,
            )
            if patch or deleted_names:
                break

        # only the patched rules may change or be deleted
        patch = [p for p in patch if p.name not in other_names]
        deleted_names &= {r.name for r in to_patch}
        if not patch and not deleted_names:
            print("No feedback patches generated.")
            return rules

        merged = self.learner._merge_patch(rules, patch, deleted_names)
        f1_after = self.learner._evaluate_rules(merged, eval_dataset).micro_f1
        print(f"  Feedback patch: F1 {f1_before:.1%} → {f1_after:.1%}")
        if f1_after < f1_before:
            print("  Rejected, keeping original rules")
            return rules
        return merged

    def refine(
        self,
        rules,
        eval_dataset,
        max_iterations=3,
        iteration_callback=None,
        audit_interval=0,
        holdout_fraction=0.0,
        split_seed=42,
    ):
        return self.learner.evaluate_and_refine(
            rules,
            eval_dataset,
            max_iterations=max_iterations,
            coordinator=self.coordinator,
            iteration_callback=iteration_callback,
            audit_interval=audit_interval,
            holdout_fraction=holdout_fraction,
            split_seed=split_seed,
        )
