#!/usr/bin/env python3
"""Analyze 2024 ACS PUMS household-resource and commute subgroups."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile


INCOME_BANDS = [("under_35k", lambda x: x < 35000), ("35k_to_74k", lambda x: 35000 <= x < 75000), ("75k_plus", lambda x: x >= 75000)]
RACE = {"1": "white", "2": "black", "3": "american_indian_alaska_native", "4": "american_indian_alaska_native", "5": "american_indian_alaska_native", "6": "asian", "7": "native_hawaiian_pacific_islander", "8": "other_or_multiple", "9": "other_or_multiple"}


def num(value: str):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def band(value: str):
    income = num(value)
    if income is None or income < 0:
        return None
    for label, predicate in INCOME_BANDS:
        if predicate(income):
            return label
    return "other"


def update_share(bucket: dict, weight: float, yes: bool):
    bucket["total_weight"] += weight
    bucket["yes_weight"] += weight if yes else 0
    bucket["records"] += 1


def finalize(bucket: dict):
    total = bucket["total_weight"]
    return {"share_percent": round(100 * bucket["yes_weight"] / total, 2) if total else None, "weighted_total": round(total, 2), "records": bucket["records"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--housing-zip", type=Path, required=True)
    parser.add_argument("--person-file", action="append", required=True, help="extracted psam_pusa.csv or psam_pusb.csv")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    household_by_file: dict[str, dict[str, tuple[str, float, str]]] = {}
    with ZipFile(args.housing_zip) as archive:
        for member in ("psam_husa.csv", "psam_husb.csv"):
            housing: dict[str, tuple[str, float, str]] = {}
            with archive.open(member) as raw:
                reader = csv.DictReader((line.decode("utf-8") for line in raw))
                for row in reader:
                    weight = num(row.get("WGTP", "")); income_band = band(row.get("HINCP", ""))
                    if weight is not None and weight > 0 and income_band is not None:
                        housing[row["SERIALNO"]] = (income_band, weight, row.get("VEH", ""))
            household_by_file[member.replace("psam_h", "psam_p")] = housing

    household_cells = {label: {"total_weight": 0.0, "yes_weight": 0.0, "records": 0} for label, _ in INCOME_BANDS}
    for housing in household_by_file.values():
        for income_band, weight, vehicles in housing.values():
            update_share(household_cells[income_band], weight, vehicles == "0")
    person_cells = defaultdict(lambda: {"total_weight": 0.0, "yes_weight": 0.0, "records": 0})
    person_rows = 0
    for person_path in args.person_file:
        person_path = Path(person_path)
        member_key = person_path.name.replace("_full", "")
        housing = household_by_file.get(member_key, {})
        with Path(person_path).open(encoding="utf-8", newline="") as source:
            for row in csv.DictReader(source):
                household = housing.get(row.get("SERIALNO", ""))
                if household is None:
                    continue
                income_band, household_weight, vehicles = household
                weight = num(row.get("PWGTP", "")); minutes = num(row.get("JWMNP", "")); age = num(row.get("AGEP", ""))
                if weight is None or weight <= 0 or minutes is None or minutes <= 0 or age is None or age < 16:
                    continue
                person_rows += 1
                race = RACE.get(row.get("RAC1P", ""), "other_or_multiple")
                disability = "with_disability" if row.get("DIS", "") == "1" else "without_disability"
                for subgroup in (("income", income_band), ("race", race), ("disability", disability)):
                    update_share(person_cells[subgroup], weight, minutes >= 30)

    result = {"format": "us-acs-pums-mobility-subgroups-v1", "source": "2024 ACS 1-year PUMS CSV", "household_measure": "HINCP income band crossed with VEH, weighted by WGTP", "commute_measure": "JWMNP >= 30 minutes among age 16+ workers with positive commute minutes, weighted by PWGTP; people working from home are excluded by the positive-minute universe", "household_cells": {label: finalize(value) for label, value in household_cells.items()}, "commute_cells": {f"{axis}:{label}": finalize(value) for (axis, label), value in sorted(person_cells.items())}, "valid_commute_records": person_rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
