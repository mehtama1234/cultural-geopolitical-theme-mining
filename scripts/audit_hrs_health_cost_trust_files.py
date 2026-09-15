#!/usr/bin/env python3
"""Audit acquired HRS files for health-cost/trust module overlap.

This utility inventories public-use files and computes only respondent-key
overlap.  It does not estimate rates, weights, causal effects, or trust change.
Supply inputs as NAME=PATH arguments; HRS releases may use HHIDPN or separate
HHID and PN identifiers.
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
    "person_key": ("hhidpn", "hhid", "pn"),
    "health_cost": (
        "n290",
        "n235",
        "n295",
        "n333",
        "a42_19",
        "a43_19",
        "a45_19",
        "w579_",
        "rcovw580m",
    ),
    "trust": ("rv557", "rv558", "rv559", "rv563", "rv555", "trust"),
    "weight": ("weight", "wt", "rwt", "rwgt"),
    "wave": ("wave", "iwyear", "iwmonth", "version"),
    "health_outcome": ("rc001", "health", "rthlth", "adl", "iadl"),
    "work_outcome": ("employment", "emp", "work", "job"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_files(values: list[str]) -> list[tuple[str, Path]]:
    result = []
    for value in values:
        if "=" not in value:
            raise ValueError(f"--file must use NAME=PATH: {value}")
        name, raw_path = value.split("=", 1)
        if not name or not raw_path:
            raise ValueError(f"--file must use NAME=PATH: {value}")
        result.append((name, Path(raw_path).expanduser()))
    return result


def read_metadata(path: Path) -> tuple[list[str], dict[str, str], int | None, dict[str, dict[Any, Any]]]:
    if path.suffix.lower() in {".dta", ".tab", ".sas7bdat", ".xpt"}:
        if path.suffix.lower() in {".dta", ".tab"}:
            _, meta = pyreadstat.read_dta(path, metadataonly=True, encoding="latin1")
        elif path.suffix.lower() == ".sas7bdat":
            _, meta = pyreadstat.read_sas7bdat(path, metadataonly=True, encoding="latin1")
        else:
            _, meta = pyreadstat.read_xport(path, metadataonly=True, encoding="latin1")
        labels = dict(zip(meta.column_names, meta.column_labels))
        return meta.column_names, labels, meta.number_rows, meta.variable_value_labels
    frame = pd.read_csv(path, nrows=0)
    return list(frame.columns), {column: "" for column in frame.columns}, None, {}


def field_candidates(columns: list[str]) -> dict[str, list[str]]:
    lowered = {column.lower(): column for column in columns}
    result = {}
    for group, needles in FIELD_GROUPS.items():
        hits = [column for column in columns if any(needle in column.lower() for needle in needles)]
        exact = [lowered[needle] for needle in needles if needle in lowered]
        result[group] = sorted(dict.fromkeys(exact + hits))
    return result


def read_columns(path: Path, columns: list[str]) -> pd.DataFrame:
    if path.suffix.lower() in {".dta", ".tab"}:
        frame, _ = pyreadstat.read_dta(path, usecols=columns, encoding="latin1")
        return frame
    if path.suffix.lower() == ".sas7bdat":
        frame, _ = pyreadstat.read_sas7bdat(path, usecols=columns, encoding="latin1")
        return frame
    if path.suffix.lower() == ".xpt":
        frame, _ = pyreadstat.read_xport(path, usecols=columns, encoding="latin1")
        return frame
    return pd.read_csv(path, usecols=columns)


def normalized(value: Any) -> str | None:
    if pd.isna(value):
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        number = float(text)
        if number.is_integer():
            return str(int(number))
    except ValueError:
        pass
    return text


def respondent_keys(path: Path, columns: list[str]) -> tuple[set[str], dict[str, Any]]:
    direct = next((column for column in columns if column.lower() == "hhidpn"), None)
    hhid = next((column for column in columns if column.lower() == "hhid"), None)
    pn = next((column for column in columns if column.lower() == "pn"), None)
    key_columns = [column for column in (direct, hhid, pn) if column]
    if not key_columns:
        return set(), {"status": "no_hhs_identifier", "key_columns": []}
    frame = read_columns(path, key_columns)
    if direct:
        keys = {key for key in (normalized(value) for value in frame[direct]) if key}
        return keys, {"status": "direct_hhidpn", "key_columns": [direct], "rows": len(frame)}
    if not (hhid and pn):
        return set(), {"status": "incomplete_hhid_pn", "key_columns": key_columns, "rows": len(frame)}
    keys = set()
    for left, right in zip(frame[hhid], frame[pn]):
        left_key, right_key = normalized(left), normalized(right)
        if left_key and right_key:
            keys.add(f"{left_key}|{right_key}")
    return keys, {"status": "composite_hhid_pn", "key_columns": [hhid, pn], "rows": len(frame)}


def audit(name: str, path: Path) -> tuple[dict[str, Any], set[str]]:
    if not path.is_file():
        return {"name": name, "path": str(path), "status": "missing"}, set()
    columns, labels, metadata_rows, value_labels = read_metadata(path)
    candidates = field_candidates(columns)
    keys, key_info = respondent_keys(path, columns)
    result = {
        "name": name,
        "path": str(path),
        "status": "readable",
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "metadata_rows": metadata_rows,
        "columns": len(columns),
        "candidate_fields": candidates,
        "candidate_labels": {
            column: labels.get(column, "")
            for values in candidates.values()
            for column in values
        },
        "value_label_domains": {
            column: len(value_labels.get(column, {}))
            for values in candidates.values()
            for column in values
            if column in value_labels
        },
        "key": {**key_info, "unique_respondents": len(keys)},
    }
    return result, keys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", action="append", required=True, help="Named input in NAME=PATH form; repeatable")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        parsed = parse_files(args.file)
        audits = []
        keys_by_name: dict[str, set[str]] = {}
        for name, path in parsed:
            result, keys = audit(name, path)
            audits.append(result)
            if keys:
                keys_by_name[name] = keys
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        parser.error(str(exc))
    overlap = {}
    names = list(keys_by_name)
    for index, left in enumerate(names):
        for right in names[index + 1 :]:
            overlap[f"{left}__{right}"] = {
                "shared_respondents": len(keys_by_name[left] & keys_by_name[right]),
                "left_unique": len(keys_by_name[left]),
                "right_unique": len(keys_by_name[right]),
            }
    output = {
        "schema": "hrs-health-cost-trust-file-audit-v1",
        "method": "File hashes, metadata and candidate field inventory, HRS respondent-key diagnostics, and pairwise key overlap; no estimates or causal inference.",
        "files": audits,
        "pairwise_overlap": overlap,
        "limitation": "Key overlap does not establish module eligibility, common field timing, valid weights, or a health-cost-to-trust sequence. Those require codebook and questionnaire review.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
