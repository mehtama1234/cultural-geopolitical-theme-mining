#!/usr/bin/env python3
"""Weighted SHED 2024-2025 transitions in cost-related care foregoing."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from pathlib import Path


CARE_FIELDS = ["E1_a", "E1_b", "E1_c", "E1_d", "E1_e"]
INSURANCE_FIELDS = ["E4_a", "E4_b", "E4_c", "E4_d", "E4_e", "E4_f"]
OUTCOMES = {
    "fair_poor_health_2025": ("pph10001", {"Fair", "Poor"}),
    "not_working_2025": ("ppemploy", {"Not working"}),
    "medical_debt_2025": ("E2B", {"Yes"}),
    "unexpected_major_medical_expense_2025": ("E2", {"Yes"}),
    "outside_help_2025": ("FS21_c", {"Yes"}),
    "reduced_savings_2025": ("INF3_c", {"Yes"}),
    "increased_borrowing_2025": ("INF3_d", {"Yes"}),
    "delayed_major_purchase_2025": ("INF3_e", {"Yes"}),
    "worked_more_or_got_job_2025": ("INF3_f", {"Yes"}),
}


def read_zip(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"expected one CSV in {path}, found {names}")
        with archive.open(names[0]) as handle:
            return list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))


def clean(value: str | None) -> str:
    return (value or "").strip()


def care_status(row: dict[str, str]) -> str | None:
    answers = [clean(row.get(field)) for field in CARE_FIELDS]
    if not all(answer in {"Yes", "No"} for answer in answers):
        return None
    return "Yes" if "Yes" in answers else "No"


def insured_status(row: dict[str, str]) -> str | None:
    answers = [clean(row.get(field)) for field in INSURANCE_FIELDS]
    if not all(answer in {"Yes", "No"} for answer in answers):
        return None
    return "insured" if "Yes" in answers else "uninsured"


def weighted_share(rows: list[tuple[dict[str, str], dict[str, str], float]], selector) -> dict[str, object]:
    selected = [(item, selector(item)) for item in rows]
    valid = [item for item, value in selected if value is not None]
    denominator = sum(item[2] for item in valid)
    numerator = sum(item[2] for item, value in selected if value is True)
    return {
        "percent": round(100 * numerator / denominator, 3) if denominator else None,
        "weighted_denominator": round(denominator, 3),
        "pairs": len(valid),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    old_rows = read_zip(args.old)
    new_rows = read_zip(args.new)
    old = {clean(row.get("shedid")): row for row in old_rows}
    required_new = {"shedid", "panel_weight", *CARE_FIELDS, *INSURANCE_FIELDS}
    required_new |= {field for field, _ in OUTCOMES.values()}
    required_old = {"shedid", *CARE_FIELDS}
    missing = sorted(required_new - set(new_rows[0] if new_rows else {}))
    missing_old = sorted(required_old - set(old_rows[0] if old_rows else {}))
    if missing or missing_old:
        raise ValueError(f"missing new fields: {missing}; missing old fields: {missing_old}")

    pairs: list[tuple[dict[str, str], dict[str, str], float]] = []
    for new_row in new_rows:
        identifier = clean(new_row.get("shedid"))
        old_row = old.get(identifier)
        if old_row is None or not clean(new_row.get("panel_weight")):
            continue
        if care_status(old_row) is None or care_status(new_row) is None:
            continue
        pairs.append((old_row, new_row, float(new_row["panel_weight"])))

    result: dict[str, object] = {
        "format": "us-shed-panel-care-foregoing-paths-v1",
        "source_unit": "SHED respondent recontact panel, 2024 to 2025",
        "weight": "2025 panel_weight",
        "care_foregoing_fields": CARE_FIELDS,
        "paired_rows_with_care_path": len(pairs),
        "variance_estimation": False,
        "causal_estimation": False,
        "method": "Link 2024 and 2025 public-use records by shedid; require complete Yes/No answers on all five listed cost-related care fields in both years; any Yes defines care foregoing; use 2025 panel_weight.",
        "paths": {},
        "limitation": "Annual recontact identifies persistence, entry, and exit of reported care foregoing but not a dated bill, clinical need, amount, alternative, treatment continuity, or causal order. Panel attrition and item-specific valid universes remain relevant.",
    }

    for before in ["Yes", "No"]:
        for after in ["Yes", "No"]:
            path = f"{before.lower()}_to_{after.lower()}"
            path_pairs = [item for item in pairs if care_status(item[0]) == before and care_status(item[1]) == after]
            entry: dict[str, object] = {"pairs": len(path_pairs), "outcomes_2025": {}}
            for name, (field, yes_values) in OUTCOMES.items():
                def selector(item, field=field, yes_values=yes_values):
                    value = clean(item[1].get(field))
                    return None if not value else value in yes_values
                entry["outcomes_2025"][name] = weighted_share(path_pairs, selector)
            insured_valid = [item for item in path_pairs if insured_status(item[1]) is not None]
            entry["outcomes_2025"]["insured_2025"] = weighted_share(
                insured_valid, lambda item: insured_status(item[1]) == "insured"
            )
            result["paths"][path] = entry

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
