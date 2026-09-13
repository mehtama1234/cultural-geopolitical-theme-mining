#!/usr/bin/env python3
"""Weighted SHED care-by-employment adaptation comparison."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from analyze_shed_care_health_year import METRICS, clean, metric_share, read_rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = read_rows(args.input)
    required = {"weight", "CG4", "ppemploy"} | {field for field, _ in METRICS.values()}
    missing = sorted(required - set(rows[0] if rows else {}))
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))

    cells: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        care, employment = clean(row.get("CG4")), clean(row.get("ppemploy"))
        if care and employment:
            cells[care][employment].append(row)
    result: dict[str, object] = {
        "format": "us-shed-care-work-distribution-v1",
        "source_unit": "US adult respondent, single SHED survey year",
        "weight": "weight",
        "variance_estimation": False,
        "causal_estimation": False,
        "rows": len(rows),
        "cells": {
            care: {
                employment: {metric: metric_share(group, field, yes_values)
                             for metric, (field, yes_values) in METRICS.items()}
                for employment, group in sorted(employment_groups.items())
            }
            for care, employment_groups in sorted(cells.items())
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
