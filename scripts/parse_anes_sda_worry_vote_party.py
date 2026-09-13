#!/usr/bin/env python3
"""Parse an official ANES SDA controlled-table HTML export."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd


def row_percent(value: object) -> float | None:
    numbers = re.findall(r"[-+]?\d+(?:\.\d+)?", str(value))
    return float(numbers[1]) if len(numbers) >= 2 else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    tables = pd.read_html(args.html)
    results = {}
    for table in tables[2:9]:
        heading = str(table.columns[0])
        match = re.search(r"=\s*(\d+)\(([^)]+)\)", heading)
        if not match:
            continue
        party_code, party_label = match.groups()
        rows = {}
        for _, row in table.iloc[2:7].iterrows():
            worry = str(row.iloc[1]).split(": ", 1)[-1]
            rows[worry] = {
                "harris_row_percent": row_percent(row.iloc[2]),
                "trump_row_percent": row_percent(row.iloc[3]),
            }
        results[party_code] = {"party": party_label, "worry_rows": rows}
    result = {
        "format": "us-anes-sda-worry-vote-party-control-v1",
        "source_unit": "2016-2020-2024 ANES panel respondent in official SDA table",
        "row": "V241539 pre-election financial worry",
        "column": "V242067 post-election presidential vote",
        "control": "V241227x pre-election party identification",
        "weight": "V240106b post-election raked weight: panel alone",
        "filter": "V240003(1) 2016-2020-2024 panel",
        "percent_type": "row percent within party-identification control cell",
        "results": results,
        "causal_estimation": False,
        "variance_estimation": False,
        "boundary": "Official weighted descriptive SDA cross-tab; no design-based standard errors in this controlled export, and small cells require caution.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"party_controls": len(results), "worry_rows_per_control": 5}, indent=2))


if __name__ == "__main__":
    main()
