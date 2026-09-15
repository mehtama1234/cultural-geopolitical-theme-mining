#!/usr/bin/env python3
"""Fetch official 2022 ACS table-based ZCTA structure context."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/us-housing-insurance-risk/data"
OUT = DATA / "acs2022-b25024.dat"
MANIFEST = DATA / "california-acs-2022-zcta-property-context-manifest.json"
URL = "https://www2.census.gov/programs-surveys/acs/summary_file/2022/table-based-SF/data/5YRData/acsdt5y2022-b25024.dat"


def main() -> int:
    req = Request(URL, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    payload = urlopen(req, timeout=60).read()
    OUT.write_bytes(payload)
    MANIFEST.write_text(json.dumps({"url": URL, "retrieved": "2026-09-13", "sha256": hashlib.sha256(payload).hexdigest(), "variables": {"B25024_E001": "units in structure total", "B25024_E002": "1-unit detached", "B25024_E010": "mobile home"}, "income_input": "acs2022-b19013.dat"}, indent=2) + "\n")
    print(json.dumps({"path": str(OUT), "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
