#!/usr/bin/env python3
"""Validate key CES medical-affordability/action reproduction values."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CHECKS = {
    ("2018", "adjusted_screen", "part_contact", "odds_ratio"): ("2018", "adjusted_contact_odds_ratio"),
    ("2020", "adjusted_screen", "part_contact", "odds_ratio"): ("2020", "adjusted_contact_odds_ratio"),
    ("2020", "adjusted_screen", "part_contact", "interval_95_model_robust"): ("2020", "adjusted_contact_odds_ratio"),
}


def close(actual: float | list[float], expected: float | list[float]) -> bool:
    if isinstance(actual, list) and isinstance(expected, list):
        return len(actual) == len(expected) and all(abs(a - e) < 0.002 for a, e in zip(actual, expected))
    return isinstance(actual, (int, float)) and isinstance(expected, (int, float)) and abs(actual - expected) < 0.002


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rerun", type=Path, required=True)
    parser.add_argument(
        "--record",
        type=Path,
        default=root / "analysis/records/us-cces-medical-affordability-political-participation-2018-2020.json",
    )
    args = parser.parse_args()
    rerun = json.loads(args.rerun.read_text(encoding="utf-8"))
    record = json.loads(args.record.read_text(encoding="utf-8"))
    expected = {str(row["period"][:4]): row["measures"] for row in record["observations"]}

    for (year, section, field, subfield), (record_year, record_key) in CHECKS.items():
        actual_value = rerun["years"][year][section][field][subfield]
        expected_value = expected[record_year][record_key]["value"]
        if field == "part_contact" and subfield == "interval_95_model_robust":
            expected_value = [1.106, 2.593] if year == "2018" else [1.023, 3.164]
        if not close(actual_value, expected_value):
            raise AssertionError(f"{year} {section}.{field}.{subfield}: {actual_value!r} != {expected_value!r}")

    for year, expected_rows in (("2018", 1000), ("2020", 1000)):
        if rerun["years"][year]["descriptive"]["records"] != expected_rows:
            raise AssertionError(f"{year}: unexpected valid row count")
    print("VALID CES medical-affordability reproduction: key action/attribution values and row counts match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
