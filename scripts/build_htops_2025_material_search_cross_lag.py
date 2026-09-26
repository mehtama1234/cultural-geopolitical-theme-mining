#!/usr/bin/env python3
"""Build a bounded April-to-June HTOPS material-pressure/search screen.

The input files are already retained local public-use extracts.  The result is
descriptive: April expense difficulty is carried to June search, AI-use, and
Congress-confidence fields for the same SCRAMID, using April weights and
successive-difference replicate weights.  It is not a causal or recovery
estimate and does not treat search as a completed alternative.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


SEARCH_FIELDS = {
    "job_search": "AI4_2",
    "food_search": "AI4_4",
    "public_benefit_search": "AI4_6",
    "credit_search": "AI4_8",
    "housing_search": "AI4_1",
    "medical_search": "AI4_5",
}
AI_FIELDS = ["AI1_1", "AI1_2", "AI1_3", "AI1_4", "AI1_5", "AI1_6", "AI1_7", "AI1_9"]


def read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def number(value: str | None) -> float | None:
    try:
        return float(value) if value not in (None, "") else None
    except ValueError:
        return None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def valid_expense(value: str | None) -> bool:
    return number(value) in (1, 2, 3, 4)


def valid_binary(value: str | None) -> bool:
    return number(value) in (1, -99)


def outcome(row: dict[str, str], name: str) -> bool | None:
    if name == "any_ai_use":
        fields = [number(row.get(field)) for field in AI_FIELDS]
        no_use = number(row.get("AI1_8"))
        if all(value is None for value in fields) and no_use not in (1, -99):
            return None
        return any(value == 1 for value in fields)
    if name == "high_confidence_in_congress":
        value = number(row.get("TRUST2_CONGRESS"))
        return None if value not in (1, 2, 3, 4, 5, -99) else value in (1, 2)
    field = SEARCH_FIELDS[name]
    value = number(row.get(field))
    return None if value not in (1, -99) else value == 1


def estimate(rows: list[tuple[dict[str, str], dict[str, str], dict[str, str]]], exposure: str, name: str, rep_fields: list[str]) -> dict[str, int | float | None]:
    selected: list[tuple[dict[str, str], dict[str, str], dict[str, str]]] = []
    for before, after, reps in rows:
        exp = number(before.get("EXPNS_DIF"))
        if not valid_expense(before.get("EXPNS_DIF")):
            continue
        if exposure == "difficulty" and exp == 1:
            continue
        if exposure == "not_difficult" and exp != 1:
            continue
        if outcome(after, name) is None:
            continue
        if number(before.get("PWEIGHT")) is None or number(before.get("PWEIGHT")) <= 0:
            continue
        selected.append((before, after, reps))
    if not selected:
        return {"unweighted_valid_n": 0, "weighted_valid": 0, "estimate_pct": None, "se_pct_points": None}
    point_weights = [number(before["PWEIGHT"]) for before, _, _ in selected]
    values = [1.0 if outcome(after, name) else 0.0 for _, after, _ in selected]
    denominator = sum(weight for weight in point_weights if weight is not None)
    point = sum(weight * value for weight, value in zip(point_weights, values) if weight is not None) / denominator * 100
    replicate_points: list[float] = []
    for field in rep_fields:
        weights = [number(reps.get(field)) for _, _, reps in selected]
        rep_den = sum(weight for weight in weights if weight is not None and weight > 0)
        rep_num = sum(weight * value for weight, value in zip(weights, values) if weight is not None and weight > 0)
        if rep_den:
            replicate_points.append(rep_num / rep_den * 100)
    se = (sum((value - point) ** 2 for value in replicate_points) / len(rep_fields)) ** 0.5 if replicate_points else None
    return {
        "unweighted_valid_n": len(selected),
        "weighted_valid": round(denominator),
        "estimate_pct": round(point, 3),
        "se_pct_points": round(se, 3) if se is not None else None,
    }


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
    estimates = {
        exposure: {name: estimate(rows, exposure, name, rep_fields) for name in names}
        for exposure in ("difficulty", "not_difficult")
    }
    result = {
        "format": "htops-2025-material-search-cross-lag-v1",
        "period": "April 15-29 to June 16-25, 2025",
        "unit": "same SCRAMID respondent; April expense difficulty carried to June topical outcomes",
        "linked_ids": len(ids),
        "baseline_rows": len(baseline),
        "followup_rows": len(followup),
        "replicate_rows": len(replicate),
        "weight": "April PWEIGHT and April PWEIGHT1-PWEIGHT80 successive-difference replicate weights",
        "estimates": estimates,
        "source_sha256": {
            "baseline": "sha256:" + sha256(args.baseline),
            "baseline_replicate": "sha256:" + sha256(args.baseline_replicate),
            "followup": "sha256:" + sha256(args.followup),
        },
        "boundary": "The exposure is self-reported April expense difficulty, and June search, AI-use, and Congress-confidence fields are descriptive follow-up outcomes among linked respondents. April weights are not documented as attrition-adjusted longitudinal weights. Search is navigation effort, not a completed alternative, remedy, recovery, or exit; no causal effect is estimated.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(ids)} linked IDs")


if __name__ == "__main__":
    main()
