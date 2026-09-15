#!/usr/bin/env python3
"""Audit baseline-expense to later outcome cells in linked 2025 HTOPS data."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


OUTCOMES = {
    "food_insufficiency": ("CURFOODSUF", lambda x: x in (3, 4)),
    "unable_to_pay_energy_bill": ("HSE16", lambda x: x == 1),
    "recent_household_job_loss": ("WRKLOSSRV", lambda x: x == 1),
    "high_confidence_in_congress": ("TRUST2_CONGRESS", lambda x: x in (1, 2)),
}


def number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def valid(row, variable):
    value = number(row.get(variable))
    weight = number(row.get("PWEIGHT"))
    return value is not None and weight is not None and value not in (-88, -99) and weight > 0


def estimate(pairs, outcome_variable, outcome_predicate, exposure_predicate, rep_by_id):
    selected = [(before, after) for before, after in pairs if valid(before, "EXPNS_DIF") and valid(after, outcome_variable) and exposure_predicate(number(before["EXPNS_DIF"]))]
    denominator = sum(number(before["PWEIGHT"]) for before, _ in selected)
    numerator = sum(number(before["PWEIGHT"]) for before, after in selected if outcome_predicate(number(after[outcome_variable])))
    point = numerator / denominator if denominator else None
    rep_points = []
    for index in range(1, 81):
        den = 0.0
        num = 0.0
        for before, after in selected:
            weight = number(rep_by_id[before["SCRAMID"]].get(f"PWEIGHT{index}"))
            den += weight
            if outcome_predicate(number(after[outcome_variable])):
                num += weight
        rep_points.append(num / den if den else 0.0)
    variance = 4 / 80 * sum((x - point) ** 2 for x in rep_points) if point is not None else None
    return {
        "value": round(point * 100, 1) if point is not None else None,
        "standard_error": round((variance ** 0.5) * 100, 2) if variance is not None else None,
        "unit": "percent of baseline-weighted valid linked respondents in exposure cell",
        "value_type": "cross_lagged_share",
        "unweighted_valid_n": len(selected),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--baseline-rep", type=Path, required=True)
    parser.add_argument("--followup", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    baseline = {row["SCRAMID"]: row for row in read(args.baseline)}
    followup = {row["SCRAMID"]: row for row in read(args.followup)}
    rep_by_id = {row["SCRAMID"]: row for row in read(args.baseline_rep)}
    ids = sorted(set(baseline) & set(followup) & set(rep_by_id))
    pairs = [(baseline[scramid], followup[scramid]) for scramid in ids]
    measures = {}
    exposures = {"baseline_expense_difficulty": lambda x: x in (2, 3, 4), "baseline_expense_not_difficult": lambda x: x == 1}
    for outcome_name, (variable, predicate) in OUTCOMES.items():
        for exposure_name, exposure_predicate in exposures.items():
            measures[f"{exposure_name}_{outcome_name}"] = estimate(pairs, variable, predicate, exposure_predicate, rep_by_id)
    result = {
        "format": "htops-cross-lagged-panel-audit-v1",
        "period": "April 15–29 to June 16–25, 2025",
        "linked_ids": len(ids),
        "measures": measures,
        "baseline_puf_sha256": "sha256:" + sha256(args.baseline),
        "followup_puf_sha256": "sha256:" + sha256(args.followup),
        "boundary": "Baseline expense exposure is self-reported and the follow-up cells are descriptive among selected linked respondents. April weights and replicate weights are not documented as attrition-adjusted longitudinal weights; cells are associative and do not establish a dated causal effect.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(ids)} linked IDs")


if __name__ == "__main__":
    main()
