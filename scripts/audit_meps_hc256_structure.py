#!/usr/bin/env python3
"""Audit the structural surface of the MEPS HC-256 Stata public-use file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


REQUIRED_LABELS = [
    "PERWT24F", "VARSTR", "VARPSU", "TOTEXP24", "TOTSLF24",
    "INSURC24", "FAMINC24", "POVCAT24", "RTHLTH31", "RTHLTH42",
    "RTHLTH53", "EMPST31", "EMPST42", "EMPST53",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("stata_file", type=Path)
    parser.add_argument("--brr-file", type=Path)
    args = parser.parse_args()
    reader = pd.read_stata(args.stata_file, convert_categoricals=False, iterator=True)
    labels = reader.variable_labels()
    rows = 0
    positive_weight = 0
    nonmissing: dict[str, int] = {field: 0 for field in REQUIRED_LABELS}
    while True:
        try:
            frame = reader.get_chunk(5000)
        except StopIteration:
            break
        rows += len(frame)
        positive_weight += int((frame["PERWT24F"] > 0).sum())
        for field in REQUIRED_LABELS:
            nonmissing[field] += int(frame[field].notna().sum())
    result = {
        "file": str(args.stata_file),
        "rows": rows,
        "columns": len(labels),
        "positive_person_weights": positive_weight,
        "required_label_presence": {field: field in labels for field in REQUIRED_LABELS},
        "required_nonmissing_counts": nonmissing,
        "labels": {field: labels.get(field, "") for field in REQUIRED_LABELS},
    }
    if args.brr_file:
        brr_reader = pd.read_stata(args.brr_file, convert_categoricals=False, iterator=True)
        brr_labels = brr_reader.variable_labels()
        brr_ids: set[str] = set()
        while True:
            try:
                frame = brr_reader.get_chunk(10000)
            except StopIteration:
                break
            brr_ids.update(frame["DUPERSID"].astype(str))
        hc_ids: set[str] = set()
        hc_reader = pd.read_stata(args.stata_file, convert_categoricals=False, iterator=True)
        while True:
            try:
                frame = hc_reader.get_chunk(10000)
            except StopIteration:
                break
            hc_ids.update(frame["DUPERSID"].astype(str))
        result["brr_columns"] = len(brr_labels)
        result["brr_unique_person_ids"] = len(brr_ids)
        result["hc_person_ids_found_in_brr"] = len(hc_ids & brr_ids)
        result["hc_person_id_linkage_rate_percent"] = round(100 * len(hc_ids & brr_ids) / len(hc_ids), 6)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
