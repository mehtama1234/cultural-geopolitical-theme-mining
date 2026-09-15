#!/usr/bin/env python3
"""Fetch and audit the public NBER W35677 task-adoption index sheets."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from datetime import date
from pathlib import Path
from urllib.request import Request, urlopen


SHEET_ID = "17OI5xRALkN4lDZ1fHw2R9xPJUdDgWyFU"
SHEETS = {
    "DWA": {"gid": "416182935", "id_column": "dwaid", "name_column": "dwatitle"},
    "IWA": {"gid": "1821519318", "id_column": "iwaid", "name_column": "iwatitle"},
    "BWA": {"gid": "646067329", "id_column": "bwaid", "name_column": "bwatitle"},
}


def fetch(level: str) -> tuple[bytes, list[dict[str, str]]]:
    spec = SHEETS[level]
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&gid={spec['gid']}"
    request = Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    with urlopen(request, timeout=60) as response:
        raw = response.read()
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig", errors="replace"))))
    return raw, rows


def audit_level(level: str) -> dict[str, object]:
    spec = SHEETS[level]
    raw, rows = fetch(level)
    required = {spec["id_column"], spec["name_column"], "adoption_rate", "number_observations"}
    columns = set(rows[0]) if rows else set()
    missing = sorted(required - columns)
    if missing:
        raise ValueError(f"{level}: missing columns: {missing}")
    rated = []
    for row in rows:
        rate = (row.get("adoption_rate") or "").strip()
        if not rate:
            continue
        observations = int(row["number_observations"])
        if observations < 20:
            raise ValueError(f"{level}: unsuppressed row below 20 observations: {row}")
        rated.append({
            "id": row[spec["id_column"]],
            "name": row[spec["name_column"]],
            "rate_percent": float(rate.rstrip("%")),
            "number_observations": observations,
        })
    if not rated:
        raise ValueError(f"{level}: no rated rows")
    ordered = sorted(rated, key=lambda item: (item["rate_percent"], item["name"]))
    return {
        "level": level,
        "gid": spec["gid"],
        "url": f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&gid={spec['gid']}",
        "retrieval_sha256": hashlib.sha256(raw).hexdigest(),
        "row_count": len(rows),
        "rated_row_count": len(rated),
        "minimum_unweighted_observations_checked": 20,
        "top_five": ordered[-5:][::-1],
        "bottom_five": ordered[:5],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("analysis/projects/ai-work-control/data/nber-w35677-index-audit-2026-09-13.json"),
    )
    args = parser.parse_args()
    result = {
        "source": "https://sites.google.com/view/covid-rps/data",
        "paper": "https://www.nber.org/papers/w35677",
        "checked": str(date.today()),
        "survey_waves": ["August 2025", "November 2025", "February 2026", "May 2026"],
        "levels": [audit_level(level) for level in SHEETS],
        "boundary": "Public survey-weighted activity indexes only; no worker-level microdata, subgroup estimates, causal workplace outcomes, or verified O*NET release metadata are included.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "levels": len(result["levels"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
