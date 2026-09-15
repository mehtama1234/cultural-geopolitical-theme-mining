#!/usr/bin/env python3
"""Audit a WBNS public-use file before route/outcome estimates are promoted."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


EXPECTED_ROUTE_FIELDS = [
    "Q53A", "Q110", "Q110A", "Q110B", "Q110C", "Q54", "Q54N", "Q54O",
    "Q54P", "Q54Q", "Q54R",
]
ROUTE_PREFIXES = ["Q110C_", "Q54Q_", "Q54R_"]


def read_data(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix in {".csv", ".txt"}:
        return pd.read_csv(path)
    if suffix in {".sav", ".zsav", ".por", ".dta", ".sas7bdat", ".xpt"}:
        try:
            import pyreadstat
        except ImportError as exc:
            raise RuntimeError("pyreadstat is required for non-CSV WBNS files") from exc
        if suffix in {".sav", ".zsav"}:
            frame, _ = pyreadstat.read_sav(path)
        elif suffix == ".por":
            frame, _ = pyreadstat.read_por(path)
        elif suffix == ".dta":
            frame, _ = pyreadstat.read_dta(path)
        elif suffix == ".sas7bdat":
            frame, _ = pyreadstat.read_sas7bdat(path)
        else:
            frame, _ = pyreadstat.read_xport(path)
        return frame
    raise ValueError(f"Unsupported data extension: {path.suffix}")


def field_audit(frame: pd.DataFrame, name: str) -> dict:
    series = frame[name]
    values = series.dropna()
    counts = values.value_counts(dropna=False).head(30)
    return {
        "column": name,
        "rows": int(len(series)),
        "nonmissing": int(values.shape[0]),
        "missing": int(series.isna().sum()),
        "distinct_nonmissing": int(values.nunique(dropna=True)),
        "top_values": [{"value": str(key), "count": int(value)} for key, value in counts.items()],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--weight-column", required=True)
    parser.add_argument("--route-fields", default=",".join(EXPECTED_ROUTE_FIELDS))
    args = parser.parse_args()

    frame = read_data(args.data)
    requested = [item.strip() for item in args.route_fields.split(",") if item.strip()]
    present = [name for name in requested if name in frame.columns]
    missing = [name for name in requested if name not in frame.columns]
    prefix_matches = {
        prefix: sorted(name for name in frame.columns if name.startswith(prefix))
        for prefix in ROUTE_PREFIXES
    }
    if args.weight_column not in frame.columns:
        raise ValueError(f"Weight column not found: {args.weight_column}")
    weight = pd.to_numeric(frame[args.weight_column], errors="coerce")
    result = {
        "format": "wbns-public-use-route-file-audit-v1",
        "data_file": str(args.data),
        "row_count": int(len(frame)),
        "column_count": int(len(frame.columns)),
        "weight_column": args.weight_column,
        "weight_nonmissing": int(weight.notna().sum()),
        "weight_positive": int((weight > 0).sum()),
        "weight_nonpositive": int((weight <= 0).sum()),
        "route_fields_requested": requested,
        "route_fields_present": present,
        "route_fields_missing": missing,
        "multiresponse_prefix_matches": prefix_matches,
        "route_field_audits": [field_audit(frame, name) for name in present],
        "promotion_gate": "pass_schema_only" if not missing and weight.notna().all() and (weight > 0).all() else "hold_for_schema_review",
        "boundary": "This audit verifies file shape, route-field availability, missingness, and raw code distributions. It does not establish questionnaire universes, weight validity, variance estimation, or substantive estimates; those require the versioned codebook and survey design documentation.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
