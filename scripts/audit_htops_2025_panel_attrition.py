#!/usr/bin/env python3
"""Audit April-to-June 2025 HTOPS linked-panel retention by baseline cells."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


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


def cell(rows, predicate):
    eligible = [row for row in rows if predicate(row) and number(row.get("PWEIGHT")) and number(row["PWEIGHT"]) > 0]
    linked = [row for row in eligible if row["_linked"]]
    total_weight = sum(number(row["PWEIGHT"]) for row in eligible)
    linked_weight = sum(number(row["PWEIGHT"]) for row in linked)
    return {
        "baseline_unweighted_n": len(eligible),
        "linked_unweighted_n": len(linked),
        "unweighted_retention_percent": round(100 * len(linked) / len(eligible), 1) if eligible else None,
        "baseline_weighted_retention_percent": round(100 * linked_weight / total_weight, 1) if total_weight else None,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--followup", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.baseline.open(newline="", encoding="utf-8-sig") as handle:
        baseline = list(csv.DictReader(handle))
    with args.followup.open(newline="", encoding="utf-8-sig") as handle:
        followup_ids = {row["SCRAMID"] for row in csv.DictReader(handle)}
    for row in baseline:
        row["_linked"] = row["SCRAMID"] in followup_ids

    cells = {
        "all": lambda r: True,
        "income_under_50k": lambda r: number(r.get("RFAM_INCOME")) in (1, 2, 3),
        "income_100k_plus": lambda r: number(r.get("RFAM_INCOME")) in (6, 7),
        "female": lambda r: number(r.get("ESEX1")) == 2,
        "male": lambda r: number(r.get("ESEX1")) == 1,
        "children_in_household": lambda r: (number(r.get("THHLD_NUMKID_TOPICAL")) or 0) > 0,
        "no_children_in_household": lambda r: number(r.get("THHLD_NUMKID_TOPICAL")) == 0,
        "food_insufficient": lambda r: number(r.get("CURFOODSUF")) in (3, 4),
        "food_sufficient_or_preferred": lambda r: number(r.get("CURFOODSUF")) in (1, 2),
        "expense_difficulty": lambda r: number(r.get("EXPNS_DIF")) in (2, 3, 4),
        "expense_not_difficult": lambda r: number(r.get("EXPNS_DIF")) == 1,
    }
    divisions = {}
    for division in range(1, 10):
        divisions[f"census_division_{division}"] = lambda r, division=division: number(r.get("DIVISION")) == division
    cells.update(divisions)
    result = {
        "format": "htops-panel-attrition-audit-v1",
        "baseline": "April 15–29, 2025",
        "followup": "June 16–25, 2025",
        "baseline_puf_sha256": "sha256:" + sha256(args.baseline),
        "followup_puf_sha256": "sha256:" + sha256(args.followup),
        "linked_ids": len(followup_ids & {row["SCRAMID"] for row in baseline}),
        "cells": {name: cell(baseline, predicate) for name, predicate in cells.items()},
        "boundary": "Retention is descriptive. Baseline person weights are not documented as attrition-adjusted longitudinal weights; weighted retention is a diagnostic, not a population panel estimate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {result['linked_ids']} linked IDs")


if __name__ == "__main__":
    main()
