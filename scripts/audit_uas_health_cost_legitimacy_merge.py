#!/usr/bin/env python3
"""Audit respondent overlap before joining UAS health-cost files.

The audit measures key-level overlap only. It does not assume that overlap
means usable longitudinal exposure, because module eligibility, wave timing,
weights, and item missingness still require the file-level audit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import pandas as pd
import pyreadstat


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


def columns(path: Path) -> list[str]:
    if path.suffix.lower() in {".dta", ".tab"}:
        _, meta = pyreadstat.read_dta(path, metadataonly=True, encoding="latin1")
        return list(meta.column_names)
    return list(pd.read_csv(path, nrows=0).columns)


def read_ids(
    path: Path, available: list[str]
) -> tuple[set[str] | None, str | None, str | None, set[str], set[tuple[str, str]]]:
    lookup = {name.lower(): name for name in available}
    key = lookup.get("uasid")
    wave = lookup.get("wave")
    if key is None:
        return None, None, wave, set(), set()
    selected = [key] + ([wave] if wave else [])
    if path.suffix.lower() in {".dta", ".tab"}:
        frame, _ = pyreadstat.read_dta(path, usecols=selected, encoding="latin1")
    else:
        frame = pd.read_csv(path, usecols=selected)
    values = frame[key].dropna().map(normalize_id)
    wave_values = set(frame[wave].dropna().map(lambda value: str(value).strip())) if wave else set()
    person_wave_keys: set[tuple[str, str]] = set()
    if wave:
        valid = frame[[key, wave]].dropna()
        person_wave_keys = {
            (normalize_id(person), normalize_id(wave_value))
            for person, wave_value in zip(valid[key], valid[wave])
        }
    return set(values), key, wave, wave_values, person_wave_keys


def normalize_id(value: object) -> str:
    """Make integral numeric IDs comparable across CSV and Stata imports."""
    text = str(value).strip()
    match = re.fullmatch(r"([+-]?\d+)\.0+", text)
    return match.group(1) if match else text


def audit(name: str, path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"name": name, "path": str(path), "status": "missing"}
    available = columns(path)
    ids, key, wave, wave_values, person_wave_keys = read_ids(path, available)
    result: dict[str, Any] = {
        "name": name,
        "path": str(path),
        "status": "readable" if ids is not None else "missing_uasid",
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "format": "stata" if path.suffix.lower() in {".dta", ".tab"} else "csv",
        "columns": len(available),
        "uasid_column": key,
        "wave_column": wave,
        "unique_persons": len(ids) if ids is not None else None,
        "unique_waves": len(wave_values) if wave else None,
        "wave_values": sorted(wave_values) if wave else [],
        "unique_person_wave_keys": len(person_wave_keys) if wave else None,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", action="append", required=True, help="Named input NAME=PATH; repeatable")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        files = parse_files(args.file)
        audits = [audit(name, path) for name, path in files]
        id_sets: dict[str, set[str]] = {}
        person_wave_sets: dict[str, set[tuple[str, str]]] = {}
        for name, path in files:
            if path.is_file():
                ids, _, _, _, person_wave_keys = read_ids(path, columns(path))
                if ids is not None:
                    id_sets[name] = ids
                    person_wave_sets[name] = person_wave_keys
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        parser.error(str(exc))

    overlap: dict[str, Any] = {}
    names = list(id_sets)
    for index, left in enumerate(names):
        for right in names[index + 1 :]:
            left_count = len(id_sets[left])
            right_count = len(id_sets[right])
            intersection = len(id_sets[left] & id_sets[right])
            left_person_waves = person_wave_sets.get(left, set())
            right_person_waves = person_wave_sets.get(right, set())
            person_wave_intersection = len(left_person_waves & right_person_waves)
            overlap[f"{left}__{right}"] = {
                "left_unique_persons": left_count,
                "right_unique_persons": right_count,
                "intersection_unique_persons": intersection,
                "intersection_share_of_left": intersection / left_count if left_count else None,
                "intersection_share_of_right": intersection / right_count if right_count else None,
                "intersection_unique_person_wave_keys": person_wave_intersection,
                "person_wave_intersection_share_of_left": (
                    person_wave_intersection / len(left_person_waves) if left_person_waves else None
                ),
                "person_wave_intersection_share_of_right": (
                    person_wave_intersection / len(right_person_waves) if right_person_waves else None
                ),
                "left_only_unique_persons": left_count - intersection,
                "right_only_unique_persons": right_count - intersection,
            }
    output = {
        "schema": "uas-health-cost-legitimacy-merge-audit-v1",
        "method": "File hashes, case-insensitive uasid discovery, unique respondent counts, and pairwise respondent-set overlap; no episode estimate or causal inference.",
        "files": audits,
        "overlap": overlap,
        "status": "ready_for_wave_and_item_audit" if len(id_sets) == len(files) else "not_ready_missing_uasid",
        "boundary": "Respondent overlap does not establish module eligibility, wave alignment, item co-occurrence, weights, missingness, or a valid exposure-to-outcome sequence.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
