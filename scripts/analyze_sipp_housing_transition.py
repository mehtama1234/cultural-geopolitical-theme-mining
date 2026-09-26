#!/usr/bin/env python3
"""Build an unweighted field/timing audit for the SIPP housing profile.

This deliberately reports raw-value coverage and adjacent-month diagnostics,
not population estimates. Annual/reference-period fields are never described
as monthly transitions by this script.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


KEYS = ("SSUID", "SHHADID", "PNUM")
FIELD_TIMING = {
    "EHOUSE_ANY": "reference_period",
    "EEHC_RENTSUB": "residence_spell",
    "EEHC_VOUCHER": "residence_spell",
    "EEHC_WHY": "residence_spell",
    "EEHC_MVMO": "residence_spell",
    "EEHC_TEN": "residence_spell",
    "EEHC_PVTEN": "residence_spell",
    "TEHC_MVYR": "residence_spell",
    "ERH_BMONTH": "residence_spell",
    "ERH_EMONTH": "residence_spell",
    "ERENTSUB": "interview_or_reference_period",
    "EVOUCHER": "interview_or_reference_period",
    "EOTHAS_MNYN": "monthly_assistance_indicator",
    "TRENTMORT": "December_reference_period",
    "EAWBMORT": "reference_period",
    "EAWBGAS": "reference_period",
    "ETENURE": "interview_or_reference_period",
    "THTOTINC": "monthly",
    "TPEARN": "monthly_or_reference_universe",
    "THINCPOV": "monthly",
    "RMNUMJOBS": "monthly",
    "RWKSPERM": "monthly",
}

STATUS_FOR = {
    "EHOUSE_ANY": "AHOUSE_ANY",
    "EEHC_RENTSUB": "AEHC_RENTSUB",
    "EEHC_VOUCHER": "AEHC_VOUCHER",
    "EEHC_WHY": "AEHC_WHY",
    "EEHC_MVMO": "AEHC_MVMO",
    "EEHC_TEN": "AEHC_TEN",
    "EEHC_PVTEN": "AEHC_PVTEN",
    "ERH_BMONTH": "ARH_BMONTH",
    "ERH_EMONTH": "ARH_EMONTH",
    "ERENTSUB": "ARENTSUB",
    "EVOUCHER": "AVOUCHER",
    "EOTHAS_MNYN": "AOTHAS_MNYN",
    "TRENTMORT": "ARENTMORT",
    "EAWBMORT": "AAWBMORT",
}

PROFILE_FIELDS = tuple(dict.fromkeys((*FIELD_TIMING, "EUTILITIES", "EAWBGAS", "ETENURE", "WPFINWGT")))
TRANSITION_FIELDS = ("EHOUSE_ANY", "EEHC_RENTSUB", "EEHC_VOUCHER", "ETENURE", "EAWBMORT", "EAWBGAS", "RMNUMJOBS", "THINCPOV")


def nonblank(value: str) -> bool:
    return value not in {"", None}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    people: dict[tuple[str, ...], dict[str, dict[str, str]]] = defaultdict(dict)
    field_values = {field: Counter() for field in PROFILE_FIELDS}
    status_values = {field: Counter() for field in STATUS_FOR.values()}
    row_count = 0
    months = Counter()

    with args.input.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in PROFILE_FIELDS if field not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("input is missing fields: " + ", ".join(missing))
        for row in reader:
            row_count += 1
            key = tuple(row[field] for field in KEYS)
            month = row["MONTHCODE"]
            months[month] += 1
            people[key][month] = row
            for field in PROFILE_FIELDS:
                value = row[field]
                if nonblank(value):
                    field_values[field][value] += 1
            for field in status_values:
                value = row[field]
                if nonblank(value):
                    status_values[field][value] += 1

    field_report = {}
    for field in PROFILE_FIELDS:
        nonblank_rows = sum(field_values[field].values())
        field_report[field] = {
            "timing": FIELD_TIMING.get(field, "not_classified"),
            "rows_nonblank": nonblank_rows,
            "rows_blank": row_count - nonblank_rows,
            "raw_value_counts": dict(field_values[field].most_common(20)),
        }
        if field in STATUS_FOR:
            field_report[field]["status_field"] = STATUS_FOR[field]
            field_report[field]["status_value_counts"] = dict(status_values[STATUS_FOR[field]].most_common(20))

    transitions = {}
    for field in TRANSITION_FIELDS:
        pairs = Counter()
        complete = 0
        changed = 0
        for by_month in people.values():
            for left in range(1, 12):
                a = by_month.get(str(left), {}).get(field, "")
                b = by_month.get(str(left + 1), {}).get(field, "")
                if not (nonblank(a) and nonblank(b)):
                    continue
                complete += 1
                pairs[(a, b)] += 1
                changed += a != b
        transitions[field] = {
            "timing": FIELD_TIMING.get(field, "not_classified"),
            "complete_adjacent_pairs": complete,
            "raw_code_changes": changed,
            "raw_code_change_share_of_complete_pairs": (changed / complete if complete else None),
            "top_raw_transitions": [
                {"from": a, "to": b, "count": count}
                for (a, b), count in pairs.most_common(20)
            ],
            "interpretation_boundary": (
                "Do not call this a monthly transition; the source field is annual, reference-period, residence-spell, or copied."
                if FIELD_TIMING.get(field) not in {"monthly", "monthly_or_reference_universe", "monthly_assistance_indicator"}
                else "Raw adjacent-month diagnostic; not a weighted estimate or causal transition."
            ),
        }

    report = {
        "schema": "us-sipp-housing-transition-timing-audit-v1",
        "source_reference_period": "2024",
        "input": str(args.input),
        "rows": row_count,
        "distinct_people": len(people),
        "distinct_households": len({key[:2] for key in people}),
        "month_counts": dict(sorted(months.items())),
        "weighted_estimate": False,
        "field_report": field_report,
        "adjacent_month_diagnostics": transitions,
        "boundary": "Raw-code coverage and transitions only. No SIPP universe, weight, replicate-weight, causality, assistance adequacy, or recovery claim is produced.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": row_count, "distinct_people": len(people), "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
