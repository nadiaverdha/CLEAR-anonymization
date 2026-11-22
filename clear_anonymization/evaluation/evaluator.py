import time

from rulechef.evaluation import evaluate_dataset


def evaluate_test(
    test_dataset, rules, chef, target_labels, mode="exact", iou_threshold=1
):
    t0 = time.time()
    eval_results = evaluate_dataset(
        rules,
        test_dataset,
        chef.learner._apply_rules,
        mode=mode,
        iou_threshold=iou_threshold,
        scope_to_rule_labels=True,
        target_labels=target_labels,
    )
    return eval_results, time.time() - t0


def check_overlap(pred, gold, threshold=1):
    pred_start, pred_end = pred["start"], pred["end"]
    gold_start, gold_end = gold["start"], gold["end"]

    if threshold == 1:
        return pred["text"] == gold["text"]

    overlap_start = max(pred_start, gold_start)

    overlap_end = min(pred_end, gold_end)

    # no overlap
    if overlap_end <= overlap_start:
        return False

    overlap = overlap_end - overlap_start
    # print(pred["text"], gold["text"],overlap)
    union = max(pred_end, gold_end) - min(pred_start, gold_start)
    iou = overlap / union
    # print(iou,"->>>>",threshold,iou >= threshold)

    return iou >= threshold


def classify_fp(pred: dict, gold_entities: list[dict]) -> str:
    pt = pred["text"].lower()
    ps, pe = pred.get("start"), pred.get("end")
    ps = int(ps) if ps not in (None, "") else None
    pe = int(pe) if pe not in (None, "") else None
    for g in gold_entities:
        gt = g["text"].lower()
        gs, ge = g.get("start"), g.get("end")
        gs = int(gs) if gs not in (None, "") else None
        ge = int(ge) if ge not in (None, "") else None
        pos_overlap = None not in (ps, pe, gs, ge) and ps < ge and pe > gs
        if pos_overlap:
            if pt == gt:
                return f"type mismatch — same span as gold: `{g['text']}`"
            if pt in gt:
                return f"partial — pred is substring of gold: `{g['text']}`"
            if gt in pt:
                return f"partial — gold is substring of pred: `{g['text']}`"
            return f"positional overlap with gold: `{g['text']}`"
        if pt == gt or pt in gt or gt in pt:
            return f"similar text (different position): `{g['text']}`"
    return "no gold match — likely missing annotation"
