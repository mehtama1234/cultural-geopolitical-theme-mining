#!/usr/bin/env python3
"""Build an income-stratified April-to-June HTOPS search screen.

This reuses the retained public-use April/June linked files and the existing
descriptive cross-lag estimator.  Income strata are baseline household-income
categories, not causal moderators or measures of available cash.  The output
is limited to the same-SCRAMID descriptive follow-up and preserves the
April-weight and attrition boundary.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_htops_2025_material_search_cross_lag import (
    SEARCH_FIELDS,
    estimate,
    number,
    outcome,
    read,
    sha256,
)


def income_band(value: str | None) -> str | None:
    code = number(value)
    if code in (1, 2, 3):
        return "under_50k"
    if code in (4, 5):
        return "50k_to_99k"
    if code in (6, 7):
        return "100k_or_more"
    return None


def search_count(row: dict[str, str]) -> int | None:
    values = [number(row.get(field)) for field in SEARCH_FIELDS.values()]
    if not all(value in (1, -99) for value in values):
        return None
    return sum(value == 1 for value in values)


def count_estimate(rows: list[tuple[dict[str, str], dict[str, str], dict[str, str]]], exposure: str, rep_fields: list[str]) -> dict[str, object]:
    selected = []
    for before, after, reps in rows:
        expense = number(before.get("EXPNS_DIF"))
        count = search_count(after)
        weight = number(before.get("PWEIGHT"))
        if expense not in (1, 2, 3, 4) or count is None or weight is None or weight <= 0:
            continue
        if exposure == "difficulty" and expense == 1:
            continue
        if exposure == "not_difficult" and expense != 1:
            continue
        selected.append((count, weight, reps))
    if not selected:
        return {"unweighted_valid_n": 0, "weighted_valid": 0}

    def value(count: int, metric: str) -> float:
        if metric == "mean_search_domains":
            return float(count)
        if metric == "two_or_more_domains":
            return float(count >= 2)
        if metric == "three_or_more_domains":
            return float(count >= 3)
        return float(count == 0)

    metrics = ["mean_search_domains", "two_or_more_domains", "three_or_more_domains", "zero_search_domains"]
    output: dict[str, object] = {
        "unweighted_valid_n": len(selected),
        "weighted_valid": round(sum(weight for _, weight, _ in selected)),
    }
    for metric in metrics:
        point = sum(weight * value(count, metric) for count, weight, _ in selected) / sum(weight for _, weight, _ in selected)
        replicate_points = []
        for field in rep_fields:
            rep_weights = [number(reps.get(field)) for _, _, reps in selected]
            denominator = sum(weight for weight in rep_weights if weight is not None and weight > 0)
            if denominator:
                numerator = sum(weight * value(count, metric) for (count, _, _), weight in zip(selected, rep_weights) if weight is not None and weight > 0)
                replicate_points.append(numerator / denominator)
        se = (sum((estimate - point) ** 2 for estimate in replicate_points) / len(rep_fields)) ** 0.5 if replicate_points else None
        if metric == "mean_search_domains":
            output[metric] = round(point, 3)
            output["se_domains"] = round(se, 3) if se is not None else None
        else:
            output[f"{metric}_pct"] = round(point * 100, 3)
            output[f"{metric}_se_pct_points"] = round(se * 100, 3) if se is not None else None
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--baseline-replicate", type=Path, required=True)
    parser.add_argument("--followup", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    baseline = {row["SCRAMID"]: row for row in read(args.baseline)}
    followup = {row["SCRAMID"]: row for row in read(args.followup)}
    replicate = {row["SCRAMID"]: row for row in read(args.baseline_replicate)}
    ids = sorted(set(baseline) & set(followup) & set(replicate))
    rows = [(baseline[key], followup[key], replicate[key]) for key in ids]
    rep_fields = [f"PWEIGHT{i}" for i in range(1, 81)]
    names = [*SEARCH_FIELDS, "any_ai_use", "high_confidence_in_congress"]

    strata: dict[str, dict[str, object]] = {}
    for band in ("under_50k", "50k_to_99k", "100k_or_more"):
        band_rows = [row for row in rows if income_band(row[0].get("RFAM_INCOME")) == band]
        strata[band] = {
            "linked_unweighted_n": len(band_rows),
            "search_load_among_expense_difficulty": count_estimate(band_rows, "difficulty", rep_fields),
            "search_load_among_not_difficult": count_estimate(band_rows, "not_difficult", rep_fields),
            "search_load_by_june_ai_use": {
                "ai_user": {
                    "expense_difficulty": count_estimate([row for row in band_rows if outcome(row[1], "any_ai_use") is True], "difficulty", rep_fields),
                    "not_difficult": count_estimate([row for row in band_rows if outcome(row[1], "any_ai_use") is True], "not_difficult", rep_fields),
                },
                "not_ai_user": {
                    "expense_difficulty": count_estimate([row for row in band_rows if outcome(row[1], "any_ai_use") is False], "difficulty", rep_fields),
                    "not_difficult": count_estimate([row for row in band_rows if outcome(row[1], "any_ai_use") is False], "not_difficult", rep_fields),
                },
            },
            "estimates_among_expense_difficulty": {
                name: estimate(band_rows, "difficulty", name, rep_fields) for name in names
            },
            "estimates_among_not_difficult": {
                name: estimate(band_rows, "not_difficult", name, rep_fields) for name in names
            },
        }

    result = {
        "format": "htops-2025-material-search-income-strata-v1",
        "period": "April 15-29 to June 16-25, 2025",
        "unit": "same SCRAMID respondent; April expense difficulty and household-income band carried to June topical outcomes",
        "income_field": "RFAM_INCOME; under $50,000 = codes 1-3, $50,000-$99,999 = codes 4-5, $100,000+ = codes 6-7",
        "linked_ids": len(ids),
        "weight": "April PWEIGHT and April PWEIGHT1-PWEIGHT80 successive-difference replicate weights",
        "strata": strata,
        "source_sha256": {
            "baseline": "sha256:" + sha256(args.baseline),
            "baseline_replicate": "sha256:" + sha256(args.baseline_replicate),
            "followup": "sha256:" + sha256(args.followup),
        },
        "boundary": "Income is a baseline household-income band, not available cash or a causal moderator. Expense difficulty is self-reported; June outcomes are descriptive follow-up among linked respondents. April weights are not documented as attrition-adjusted longitudinal weights. Search is navigation effort, not a completed alternative, remedy, recovery, or exit; no causal effect is estimated.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(ids)} linked IDs")


if __name__ == "__main__":
    main()
