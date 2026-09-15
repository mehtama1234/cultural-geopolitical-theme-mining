#!/usr/bin/env python3
"""Cross-tab SHED 2025 cost-related care foregoing with financial outcomes."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from pathlib import Path


CARE_FIELDS = ["E1_a", "E1_b", "E1_c", "E1_d", "E1_e"]
METRICS = {
    "medical_debt": ("E2B", {"Yes"}),
    "unexpected_major_medical_expense": ("E2", {"Yes"}),
    "three_month_emergency_funds": ("EF1", {"Yes"}),
    "used_less_or_stopped_products": ("INF3_b", {"Yes"}),
    "reduced_savings": ("INF3_c", {"Yes"}),
    "increased_borrowing": ("INF3_d", {"Yes"}),
    "delayed_major_purchase": ("INF3_e", {"Yes"}),
    "worked_more_or_got_job": ("INF3_f", {"Yes"}),
}


def clean(value: str | None) -> str:
    return (value or "").strip()


def read_rows(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"expected one CSV in {path}, found {names}")
        with archive.open(names[0]) as handle:
            return list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))


def weighted_share(rows: list[dict[str, str]], field: str, yes_values: set[str]) -> dict[str, object]:
    valid = [row for row in rows if clean(row.get(field))]
    denominator = sum(float(row.get("weight") or 0) for row in valid)
    numerator = sum(float(row.get("weight") or 0) for row in valid if clean(row.get(field)) in yes_values)
    return {
        "percent": round(100 * numerator / denominator, 3) if denominator else None,
        "weighted_denominator": round(denominator, 3),
        "nonmissing_rows": len(valid),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = read_rows(args.input)
    required = {"shedid", "weight", *CARE_FIELDS} | {field for field, _ in METRICS.values()}
    missing = sorted(required - set(rows[0] if rows else {}))
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))

    care_rows = []
    for row in rows:
        answers = [clean(row.get(field)) for field in CARE_FIELDS]
        if not all(answer in {"Yes", "No"} for answer in answers):
            continue
        row = dict(row)
        row["care_skipped_any"] = "Yes" if "Yes" in answers else "No"
        care_rows.append(row)

    result: dict[str, object] = {
        "format": "us-shed-2025-care-skipping-adaptation-association-v1",
        "source_unit": "US adult SHED 2025 respondent",
        "source_file": str(args.input),
        "weight": "weight (single-year cross-section)",
        "care_foregoing_fields": CARE_FIELDS,
        "method": "All five E1 care-foregoing fields must be observed; any Yes defines cost-related care foregoing. Outcomes are weighted same-respondent cross-sectional comparisons, not dated bill outcomes or causal estimates.",
        "rows": len(rows),
        "complete_care_foregoing_rows": len(care_rows),
        "groups": {},
        "limitation": "Care foregoing, debt, medical expense, and price adaptations share a prior-12-month or current cross-sectional frame. The data do not identify the same bill, clinical need, timing, alternative, payment obligation, or whether care foregoing caused the financial outcome.",
    }
    for group in ["Yes", "No"]:
        subset = [row for row in care_rows if row["care_skipped_any"] == group]
        result["groups"]["care_skipped_any_" + group.lower()] = {
            "rows": len(subset),
            "weighted_share_of_complete_care_foregoing_sample": round(
                100 * sum(float(row.get("weight") or 0) for row in subset) /
                sum(float(row.get("weight") or 0) for row in care_rows), 3
            ) if care_rows else None,
            "outcomes": {
                name: weighted_share(subset, field, yes_values)
                for name, (field, yes_values) in METRICS.items()
            },
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
