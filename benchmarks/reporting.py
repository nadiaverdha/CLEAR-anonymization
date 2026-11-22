from benchmarks.data import BenchmarkRun


def make_oniteration_callback(iteration_metrics: list):
    """
    Returns a callback function suitable for RuleChef's iteration_callback.
    Logs per-iteration metrics into the provided iteration_metrics list.
    """

    def on_iteration(iteration, iter_rules, eval_result):
        iteration_metrics.append(
            {
                "iteration": iteration,
                "num_rules": len(iter_rules),
                **eval_metrics(eval_result),
            }
        )

    return on_iteration


def eval_metrics(result) -> dict:
    return {
        "exact_match": result.exact_match,
        "micro_f1": result.micro_f1,
        "micro_precision": result.micro_precision,
        "micro_recall": result.micro_recall,
        "macro_f1": result.macro_f1,
        "per_class": [
            {
                "label": cm.label,
                "f1": cm.f1,
                "precision": cm.precision,
                "recall": cm.recall,
            }
            for cm in (result.per_class or [])
        ],
    }


# added helper function
def _print_scores(title, r):
    print(f"{title}:")
    print(f"Accuracy (exact match):   {r.exact_match:.1%}")
    print(f"Micro Precision:          {r.micro_precision:.1%}")
    print(f"Micro Recall:             {r.micro_recall:.1%}")
    print(f"Micro F1:                 {r.micro_f1:.1%}")
    print(f"Macro F1:                 {r.macro_f1:.1%}")
    print()


def print_results(run: BenchmarkRun):
    args = run.args
    # 9. Print results
    print(f"\n{'=' * 70}")
    print(f"German {args.dataset_name} Results")
    print(f"{'=' * 70}")
    print("Configuration:")

    print(f"Classes:                  {', '.join(sorted(run.selected_classes))}")
    print(f"Train docs:               {run.train_size}")
    print(f"Train sentences:          {run.train_sentences}")
    print(f"Eval docs:                {run.eval_size}")
    print(f"Eval sentences:           {run.eval_sentences}")
    print(f"Dev docs:                 {run.dev_size}")
    print(f"Dev sentences:            {run.dev_sentences}")
    print(f"Test docs:                {run.test_size}")
    print(f"Test sentences:           {run.test_sentences}")
    print(f"Model:                    {args.model}")

    print()

    print("Dev Results:")
    print(f"Micro Precision:          {run.eval_results.micro_precision:.1%}")
    print(f"Micro Recall:             {run.eval_results.micro_recall:.1%}")
    print(f"Micro F1:                 {run.eval_results.micro_f1:.1%}")
    print(f"Macro F1:                 {run.eval_results.macro_f1:.1%}")
    print()
    print("Test results:")
    print(f"Micro Precision:          {run.test_eval_results.micro_precision:.1%}")
    print(f"Micro Recall:             {run.test_eval_results.micro_recall:.1%}")
    print(f"Micro F1:                 {run.test_eval_results.micro_f1:.1%}")
    print(f"Macro F1:                 {run.test_eval_results.macro_f1:.1%}")
    print()
    print("Timing:")
    print(f"Learning:                 {run.t_learn:.1f}s")
    print(f"Evaluation:               {run.t_eval:.1f}s")
    print(f"Per-query:                {run.t_eval / len(run.test_data) * 1000:.2f}ms")
    print()
    print(f"Rules:                      {len(run.rules)} total")
    print(f"{'=' * 70}")


def print_rule_summary(rules):
    print(f"\n{'─' * 70}")
    print("RULES LEARNED:")
    print(f"{'─' * 70}")
    for r in sorted(rules, key=lambda r: -r.priority):
        content_preview = r.content.replace("\n", " ")[:100]
        print(f"  [p={r.priority}] {r.name}: {content_preview}")
    print(f"{'─' * 70}")


def print_per_class_breakdown(eval_results):
    if not eval_results.per_class:
        return
    sorted_classes = sorted(eval_results.per_class, key=lambda c: c.f1, reverse=True)
    print("\n  Top 10 classes by F1:")
    for cm in sorted_classes[:10]:
        print(
            f"    {cm.label:50s} F1={cm.f1:.0%} P={cm.precision:.0%} R={cm.recall:.0%} "
            f"(TP={cm.tp} FP={cm.fp})"
        )
    print("\n  Bottom 10 classes by F1:")
    for cm in sorted_classes[-10:]:
        print(
            f"    {cm.label:50s} F1={cm.f1:.0%} P={cm.precision:.0%} R={cm.recall:.0%} "
            f"(TP={cm.tp} FP={cm.fp})"
        )
