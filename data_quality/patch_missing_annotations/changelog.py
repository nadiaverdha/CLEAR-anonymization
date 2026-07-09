import sys
from datetime import date
from pathlib import Path


def _append_changelog(
    args,
    out_path,
    pattern_changes,
    correction_changes,
    extend_prev_changes,
    rules,
    rule_changes,
):
    changelog = Path(__file__).parent.parent / args.dataset_name / "CHANGELOG.md"
    cmd = " \\\n  ".join(
        ["python -m data_quality.patch_missing_annotations"] + sys.argv[1:]
    )

    lines = [f"\n## {date.today()} — {Path(args.input_dir).name} → {out_path.name}"]
    lines.append(f"**Input:** `{args.input_dir}`")
    lines.append(f"**Output:** `{args.output}`")
    lines.append(f"**Script:**\n```bash\n{cmd}\n```")
    lines.append("**Changes:**")
    if pattern_changes:
        lines.append(f"- {len(pattern_changes)} pattern annotation(s):")
        for ch in pattern_changes:
            lines.append(
                f"  - [{ch['sent_id']}] '{ch['text']}' [{ch['start']}:{ch['end']}] → {ch['type']}"
            )
    if correction_changes:
        lines.append(f"- {len(correction_changes)} correction(s):")
        for ch in correction_changes:
            lines.append(
                f"  - [{ch['sent_id']}] '{ch['text']}' [{ch['start']}:{ch['end']}] → {ch['type']}"
            )
    if extend_prev_changes:
        lines.append(f"- {len(extend_prev_changes)} extend-prev annotation(s):")
        for ch in extend_prev_changes:
            lines.append(
                f"  - [{ch['sent_id']}] '{ch['text']}' [{ch['start']}:{ch['end']}] → {ch['type']}"
            )
    if rules:
        lines.append(
            f"- {len(rules)} rule(s) applied from: {', '.join(args.rules_json)}"
        )
        counts_by_rule = {}
        for ch in rule_changes:
            counts_by_rule[ch["rule_id"]] = counts_by_rule.get(ch["rule_id"], 0) + 1
        for r in rules:
            n = counts_by_rule.get(r.id, 0)
            lines.append(
                f"  - `{r.id}` **{r.name}**: `{r.content}` — {n} annotation(s) added"
            )

    if not any([pattern_changes, correction_changes, extend_prev_changes, rules]):
        lines.append("- (no changes recorded)")

    changelog.parent.mkdir(parents=True, exist_ok=True)
    with changelog.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Changelog updated: {changelog}")
