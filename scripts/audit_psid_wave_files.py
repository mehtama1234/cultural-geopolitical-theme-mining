#!/usr/bin/env python3
"""Audit locally downloaded PSID wave files against the field-map manifest.

This is an acquisition gate, not an estimator.  It checks that the supplied
wave files expose the mapped variables and requested identifiers before any
merge or estimate is attempted.  It supports delimited text directly and
uses pandas opportunistically for Stata, SAS, and SPSS files.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests/us-psid-material-time-care-field-map-v1.json"
TOKEN_RE = re.compile(r"^(ER\d+)-(ER\d+)$")


def file_sha256(path: Path) -> str:
    """Return a streaming SHA-256 digest for an inspected source file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expand_token(token: str) -> list[str]:
    """Expand a manifest range such as ER82820-ER82831."""
    match = TOKEN_RE.match(token)
    if not match:
        return [token]
    start, end = (int(match.group(1)[2:]), int(match.group(2)[2:]))
    if end < start:
        raise ValueError(f"descending PSID variable range: {token}")
    return [f"ER{number}" for number in range(start, end + 1)]


def manifest_variables(manifest: dict, year: int) -> set[str]:
    variables: set[str] = set()
    for field in manifest["fields"]:
        raw = field.get("variables", {})
        values = raw.get(str(year), []) if isinstance(raw, dict) else []
        for token in values:
            variables.update(expand_token(token))
    return variables


def read_columns(path: Path) -> tuple[set[str], str]:
    suffix = path.suffix.lower()
    if suffix in {".dta", ".sas7bdat", ".sav", ".por", ".xpt", ".sas"}:
        try:
            import pandas as pd  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                f"{path.name} requires pandas for {suffix}; install it or provide a delimited export"
            ) from exc
        if suffix == ".dta":
            frame = pd.read_stata(path, iterator=True)
            return {str(column).strip() for column in frame.varlist}, "pandas-stata"
        if suffix in {".sas7bdat", ".sas"}:
            frame = pd.read_sas(path, iterator=True)
            return {str(column).strip() for column in frame.columns}, "pandas-sas"
        if suffix in {".xpt", ".sav", ".por"}:
            reader = pd.read_sas(path, format="xport", iterator=True) if suffix == ".xpt" else pd.read_spss(path)
            columns = reader.columns if hasattr(reader, "columns") else reader.varlist
            return {str(column).strip() for column in columns}, "pandas-statistical"

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        sample = handle.read(8192)
        handle.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters="\t,;|")
        except csv.Error:
            dialect = csv.excel_tab
        reader = csv.reader(handle, dialect)
        header = next(reader, [])
    return {column.strip() for column in header if column.strip()}, f"delimited-{repr(dialect.delimiter)}"


def parse_wave(value: str) -> tuple[int, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("wave file must be YEAR=PATH")
    year_text, path_text = value.split("=", 1)
    try:
        year = int(year_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("wave year must be an integer") from exc
    return year, Path(path_text).expanduser()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", dest="files", action="append", type=parse_wave, required=True,
                        help="wave file as YEAR=PATH; repeat for each downloaded wave")
    parser.add_argument("--identifier", action="append", default=[],
                        help="identifier column expected in every supplied file; repeat as needed")
    parser.add_argument("--out", type=Path, help="write JSON audit report to this path")
    args = parser.parse_args()
    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    report = {
        "format": "us-psid-wave-file-audit-v1",
        "manifest": str(MANIFEST.relative_to(ROOT)),
        "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "status": "pass",
        "waves": [],
        "required_identifiers": args.identifier,
    }
    failures: list[str] = []
    files_by_year: dict[int, list[Path]] = defaultdict(list)
    for year, path in args.files:
        files_by_year[year].append(path)
    for year, paths in sorted(files_by_year.items()):
        expected = manifest_variables(manifest, year)
        wave_entry = {
            "year": year,
            "status": "pass",
            "expected_variable_count": len(expected),
            "files": [],
        }
        observed_union: set[str] = set()
        identifier_union: set[str] = set()
        for path in paths:
            entry = {"path": str(path), "status": "pass"}
            if not path.exists():
                failures.append(f"{year}: file not found: {path}")
                entry["status"] = "fail"
                wave_entry["status"] = "fail"
                wave_entry["files"].append(entry)
                continue
            try:
                columns, reader = read_columns(path)
                digest = file_sha256(path)
            except (OSError, RuntimeError, ValueError, StopIteration) as exc:
                failures.append(f"{year}: could not inspect {path}: {exc}")
                entry["status"] = "fail"
                wave_entry["status"] = "fail"
                wave_entry["files"].append(entry)
                continue
            observed_union.update(columns)
            identifier_union.update(set(args.identifier) & columns)
            entry.update({
                "reader": reader,
                "size_bytes": path.stat().st_size,
                "sha256": digest,
                "observed_column_count": len(columns),
                "observed_columns": sorted(columns),
            })
            wave_entry["files"].append(entry)
        missing = sorted(expected - observed_union)
        identifiers_missing = sorted(set(args.identifier) - identifier_union)
        wave_entry.update({
            "observed_union_column_count": len(observed_union),
            "missing_mapped_variables": missing,
            "missing_identifiers": identifiers_missing,
        })
        if missing:
            failures.append(f"{year}: {len(missing)} mapped variables missing across supplied files")
            wave_entry["status"] = "fail"
        if identifiers_missing:
            failures.append(f"{year}: identifiers missing across supplied files: {', '.join(identifiers_missing)}")
            wave_entry["status"] = "fail"
        report["waves"].append(wave_entry)

    expected_years = set(manifest["target_waves"])
    seen_years = set(files_by_year)
    absent_years = sorted(expected_years - seen_years)
    if absent_years:
        failures.append(f"target waves not supplied: {', '.join(map(str, absent_years))}")
    if failures:
        report["status"] = "fail"
        report["failures"] = failures
    else:
        report["message"] = "All target waves expose the mapped variables and requested identifiers; proceed to universe, missingness, retention, weight, and merge checks."
    encoded = json.dumps(report, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
