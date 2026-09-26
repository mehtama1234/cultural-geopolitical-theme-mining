#!/usr/bin/env python3
"""Analyze the July 2026 HTOPS material/social/authority cross-tab.

The July PUF is cross-sectional. This script produces respondent-weighted
conditional shares by household expense difficulty and standard errors from
the 80 successive-difference replicate weights. It does not estimate a
causal or longitudinal transition.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import zipfile
from collections import defaultdict
from pathlib import Path

GROUPS = ("1", "2", "3", "4")
OUTCOMES = {
    "lonely_always_or_usually": lambda r: r["SOC_LONELY"].split(".", 1)[0] in {"1", "2"},
    "support_always_or_usually": lambda r: r["SOC_SUPPORT"].split(".", 1)[0] in {"1", "2"},
    "club_12_or_more_times": lambda r: r["SOC_CLUBS"].split(".", 1)[0] == "4",
    "food_sometimes_or_often_not_enough": lambda r: r["FD_SUFF"].split(".", 1)[0] in {"3", "4"},
    "doctor_trust_great_deal_or_quite_lot": lambda r: r["HLTHTRUST_DR"].split(".", 1)[0] in {"1", "2"},
    "ai_trust_great_deal_or_quite_lot": lambda r: r["HLTHTRUST_AI"].split(".", 1)[0] in {"1", "2"},
    "federal_statistics_trust": lambda r: r["TRUST_FEDSTAT"].split(".", 1)[0] == "1",
    "congress_confidence_great_deal_or_quite_lot": lambda r: r["TRUST_CONGRESS"].split(".", 1)[0] in {"1", "2"},
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def summarize(cell: list[object]) -> dict[str, float]:
    numerator, denominator, rep_num, rep_den = cell
    point = 100.0 * numerator / denominator
    replicate = [100.0 * n / d for n, d in zip(rep_num, rep_den) if d]
    se = math.sqrt(sum((value - point) ** 2 for value in replicate) / 80.0)
    return {"pct": round(point, 3), "se_pct_points": round(se, 3)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--puf-member", default="HTOPS_HPS_2607_PUF.csv")
    parser.add_argument("--rep-member", default="HTOPS_HPS_2607_REPWGT_PUF.csv")
    args = parser.parse_args()

    rows: dict[str, dict[str, str]] = {}
    main_rows = 0
    with zipfile.ZipFile(args.zip) as archive:
        with archive.open(args.puf_member) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            for row in reader:
                main_rows += 1
                group = row["EXPENSE_DIFFICULT"].split(".", 1)[0]
                if group in GROUPS:
                    rows[row["SCRAMID"]] = row

        cells = {
            (group, name): [0.0, 0.0, [0.0] * 80, [0.0] * 80]
            for group in GROUPS
            for name in OUTCOMES
        }
        counts: defaultdict[str, int] = defaultdict(int)
        with archive.open(args.rep_member) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            for replicate_row in reader:
                row = rows.get(replicate_row["SCRAMID"])
                if row is None:
                    continue
                group = row["EXPENSE_DIFFICULT"].split(".", 1)[0]
                primary_weight = float(row["PWEIGHT"])
                replicate_weights = [float(replicate_row[f"PWEIGHT{i}"]) for i in range(1, 81)]
                counts[group] += 1
                for name, predicate in OUTCOMES.items():
                    value = 1.0 if predicate(row) else 0.0
                    cell = cells[group, name]
                    cell[0] += primary_weight * value
                    cell[1] += primary_weight
                    for index, weight in enumerate(replicate_weights):
                        cell[2][index] += weight * value
                        cell[3][index] += weight

    result = {
        "format": "htops-2026-july-same-respondent-material-social-authority-screen-v1",
        "field_window": "July 15-August 3, 2026",
        "main_rows": main_rows,
        "valid_expense_rows": sum(counts.values()),
        "unweighted_n_by_expense_group": dict(counts),
        "weight": "PWEIGHT with PWEIGHT1-PWEIGHT80 successive-difference replicate weights",
        "estimand": "Same-round descriptive respondent-weighted conditional shares by household-reported expense difficulty.",
        "outcomes": {
            name: {group: summarize(cells[group, name]) for group in GROUPS}
            for name in OUTCOMES
        },
        "input_sha256": sha256(args.zip),
        "boundary": "Cross-sectional association only; household expense difficulty and respondent outcomes share a record but no dated causal episode, remedy, recovery, political action, or exit is observed.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "valid_expense_rows": sum(counts.values())}))


if __name__ == "__main__":
    main()
