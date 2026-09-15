#!/usr/bin/env python3
"""Audit registration-gated UAS files for the health-cost legitimacy join.

The script intentionally performs an inventory and linkage audit only.  It
does not estimate a health-cost effect or infer that a trust variable follows
an exposure.  UAS files may be Stata or CSV and are supplied as NAME=PATH
arguments so the acquisition manifest remains explicit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import pandas as pd
import pyreadstat


FIELD_GROUPS = {
    "person_key": ("uasid",),
    "household_keys": ("uashhid", "survhhid"),
    "wave": ("wave", "uas_surv_num", "survey_source"),
    "weight": ("final_weight", "weight", "wt"),
    "medical_cost": (
        "avoidcare_cost",
        "hcb_ever",
        "n215",
        "n333",
        "n492",
        "n493",
        "ph001",
    ),
    "care_experience": ("n235", "n295", "experience_hco", "he004"),
    "trust": ("hrsntrust_hosp", "hrsntrust_ins", "trust"),
    "timing": (
        "start_month",
        "start_day",
        "end_date",
        "avoidcare",
        "when",
        "month",
        "year",
    ),
    "outcomes": (
        "_srh1",
        "le_hrs_p1",
        "le_hrs_s1",
        "meaning",
        "empl",
        "fin",
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_files(values: list[str]) -> list[tuple[str, Path]]:
    parsed = []
    for value in values:
        if "=" not in value:
            raise ValueError(f"--file must use NAME=PATH: {value}")
        name, raw_path = value.split("=", 1)
        if not name or not raw_path:
            raise ValueError(f"--file must use NAME=PATH: {value}")
        parsed.append((name, Path(raw_path).expanduser()))
    return parsed


def metadata(path: Path) -> tuple[list[str], dict[str, str], int | None, dict[str, dict[Any, Any]]]:
    suffix = path.suffix.lower()
    if suffix in {".dta", ".tab"}:
        _, meta = pyreadstat.read_dta(path, metadataonly=True, encoding="latin1")
        labels = {
            name: label
            for name, label in zip(meta.column_names, meta.column_labels)
        }
        return meta.column_names, labels, meta.number_rows, meta.variable_value_labels
    frame = pd.read_csv(path, nrows=0)
    return list(frame.columns), {name: "" for name in frame.columns}, None, {}


def candidates(columns: list[str]) -> dict[str, list[str]]:
    lowered = {column.lower(): column for column in columns}
    result: dict[str, list[str]] = {}
    for group, needles in FIELD_GROUPS.items():
        hits = []
        for column in columns:
            name = column.lower()
            if any(needle in name for needle in needles):
                hits.append(column)
        result[group] = sorted(dict.fromkeys(hits))
        # Exact identifiers are more useful than broad substring matches.
        exact = [lowered[needle] for needle in needles if needle in lowered]
        result[group] = sorted(dict.fromkeys(exact + result[group]))
    return result


def inspect_rows(path: Path, columns: list[str], groups: dict[str, list[str]]) -> dict[str, Any]:
    selected = sorted({column for values in groups.values() for column in values})
    if not selected:
        return {"row_count": None, "selected_column_diagnostics": {}}
    suffix = path.suffix.lower()
    if suffix in {".dta", ".tab"}:
        frame, _ = pyreadstat.read_dta(path, usecols=selected, encoding="latin1")
    else:
        frame = pd.read_csv(path, usecols=selected)
    diagnostics: dict[str, Any] = {}
    for column in selected:
        series = frame[column]
        diagnostics[column] = {
            "nonmissing": int(series.notna().sum()),
            "missing": int(series.isna().sum()),
            "unique_nonmissing": int(series.dropna().nunique()),
        }
    key = next((column for column in groups["person_key"] if column in frame), None)
    wave = next((column for column in groups["wave"] if column in frame), None)
    result: dict[str, Any] = {
        "row_count": int(len(frame)),
        "selected_column_diagnostics": diagnostics,
    }
    if key:
        result["unique_persons"] = int(frame[key].dropna().nunique())
        result["duplicate_person_rows"] = int(frame[key].duplicated(keep=False).sum())
    if wave:
        result["unique_waves"] = int(frame[wave].dropna().nunique())
        result["wave_values_sample"] = [str(value) for value in frame[wave].dropna().drop_duplicates().head(25)]
    return result


def audit(name: str, path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"name": name, "path": str(path), "status": "missing"}
    columns, labels, metadata_rows, value_labels = metadata(path)
    groups = candidates(columns)
    result: dict[str, Any] = {
        "name": name,
        "path": str(path),
        "status": "readable",
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "format": "stata" if path.suffix.lower() in {".dta", ".tab"} else "csv",
        "metadata_rows": metadata_rows,
        "columns": len(columns),
        "candidate_fields": groups,
        "candidate_labels": {
            column: labels.get(column, "")
            for values in groups.values()
            for column in values
        },
        "value_label_domains": {
            column: len(value_labels.get(column, {}))
            for values in groups.values()
            for column in values
            if column in value_labels
        },
    }
    result.update(inspect_rows(path, columns, groups))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", action="append", required=True, help="Named input in NAME=PATH form; repeatable")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        files = parse_files(args.file)
        audits = [audit(name, path) for name, path in files]
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        parser.error(str(exc))
    output = {
        "schema": "uas-health-cost-legitimacy-file-audit-v1",
        "method": "Metadata, hashes, candidate field inventory, key/wave uniqueness, and missingness diagnostics; no estimate or causal inference.",
        "files": audits,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
