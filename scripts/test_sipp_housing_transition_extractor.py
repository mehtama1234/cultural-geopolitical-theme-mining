#!/usr/bin/env python3
"""Smoke-test the additive SIPP housing-transition extraction profile."""

from __future__ import annotations

import csv
import json
import tempfile
from pathlib import Path

from extract_sipp_household_calendar_slice import HOUSING_TRANSITION_FIELDS, extract


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="sipp-housing-profile-") as temp:
        root = Path(temp)
        source = root / "synthetic-sipp.csv"
        output = root / "slice.csv"
        report = root / "report.json"

        rows = []
        for month in ("1", "2"):
            row = {field: "" for field in HOUSING_TRANSITION_FIELDS}
            row.update({
                "SSUID": "sample-1",
                "SHHADID": "household-1",
                "PNUM": "1",
                "MONTHCODE": month,
                "WPFINWGT": "1",
                "EHOUSE_ANY": "1" if month == "1" else "2",
                "EEHC_RENTSUB": "1" if month == "1" else "2",
                "EEHC_WHY": "3",
                "TRENTMORT": "1200",
                "EAWBMORT": "2" if month == "1" else "1",
                "THTOTINC": "3000",
                "TPEARN": "2200",
                "RMNUMJOBS": "1",
            })
            rows.append(row)

        with source.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=HOUSING_TRANSITION_FIELDS, delimiter="|")
            writer.writeheader()
            writer.writerows(rows)

        result = extract(
            str(source),
            output,
            report,
            max_rows=None,
            profile="housing-transition",
        )
        payload = json.loads(report.read_text(encoding="utf-8"))
        assert result["profile"] == "housing-transition"
        assert result["rows_written"] == 2
        assert "EHOUSE_ANY" in payload["fields"]
        assert "TRENTMORT" in payload["fields"]
        assert payload["monthcode_counts"] == {"1": 1, "2": 1}
        assert output.read_text(encoding="utf-8").count("sample-1") == 2

    print("PASS SIPP housing-transition extractor smoke test")


if __name__ == "__main__":
    main()
