#!/usr/bin/env python3
"""Extract a SIPP slice for the household-calendar design.

The Census pipe-delimited file is large. This extractor streams it, selects only
the fields named in the research note, and writes a small CSV plus a JSON
coverage report. Raw SIPP files are not written into this repository.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from contextlib import nullcontext
from pathlib import Path


FIELDS = [
    "SSUID",
    "SHHADID",
    "PNUM",
    "SPANEL",
    "SWAVE",
    "MONTHCODE",
    "WPFINWGT",
    "ETENURE",
    "EUTILITIES",
    "EENERGY_ASST",
    "EAWBMORT",
    "EAWBGAS",
    "THTOTINC",
    "TPEARN",
    "THTOTINCT2",
    "THINCPOV",
    "TAGE_EHC",
    "EOWN_SAV",
    "TOSAVVAL",
    "THDEBT_CC",
    "EDEBT_CC",
    "RFOODS",
    "RFOODR",
    "EFOOD1",
    "EFOOD3",
    "EFOOD6",
    "EPAY",
    "EPAYHELP",
    "EWORKMORE",
    "ETIMELOST",
    "RMNUMJOBS",
    "RWKSPERM",
    "EJB1_PVTRPRM",
    "TJB1_PVOTHRC",
]


def extract(input_path: str, output_path: Path, report_path: Path, max_rows: int | None) -> dict:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    row_count = 0
    sample_units: set[str] = set()
    households: set[str] = set()
    months: Counter[str] = Counter()

    source_context = (nullcontext(sys.stdin) if input_path == "-" else
                      Path(input_path).open("r", encoding="utf-8", newline=""))
    with source_context as source:
        reader = csv.DictReader(source, delimiter="|")
        if reader.fieldnames is None:
            raise ValueError("SIPP input has no header")
        missing = [field for field in FIELDS if field not in reader.fieldnames]
        if missing:
            raise ValueError("SIPP input is missing fields: " + ", ".join(missing))

        with output_path.open("w", encoding="utf-8", newline="") as target:
            writer = csv.DictWriter(target, fieldnames=FIELDS)
            writer.writeheader()
            for row in reader:
                selected = {field: row.get(field, "") for field in FIELDS}
                writer.writerow(selected)
                row_count += 1
                sample_units.add(selected["SSUID"])
                households.add(selected["SSUID"] + ":" + selected["SHHADID"])
                months[selected["MONTHCODE"]] += 1
                if max_rows is not None and row_count >= max_rows:
                    break

    report = {
        "format": "us-household-calendar-sipp-slice-v2",
        "source": "2025 SIPP public-use pipe-delimited file",
        "source_reference_period": "2024",
        "input": input_path,
        "output": str(output_path),
        "rows_written": row_count,
        "distinct_sample_units": len(sample_units),
        "distinct_household_ids": len(households),
        "monthcode_counts": dict(sorted(months.items())),
        "fields": FIELDS,
        "max_rows": max_rows,
        "raw_data_committed": False,
        "evidence_status": "observed_source_rows",
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="SIPP pipe-delimited CSV, or - for stdin")
    parser.add_argument("--output", type=Path, required=True, help="selected CSV output")
    parser.add_argument("--report", type=Path, required=True, help="JSON coverage report")
    parser.add_argument("--max-rows", type=int, default=None, help="optional smoke-test row limit")
    args = parser.parse_args()
    print(json.dumps(extract(args.input, args.output, args.report, args.max_rows), indent=2))


if __name__ == "__main__":
    main()
