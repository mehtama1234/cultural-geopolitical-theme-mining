#!/usr/bin/env python3
"""Fetch official 2022 ACS 5-year table-based ZCTA context files."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-housing-insurance-risk/data"
BASE = "https://www2.census.gov/programs-surveys/acs/summary_file/2022/table-based-SF/data/5YRData/"
SOURCES = {
    "acs2022-b19013.dat": BASE + "acsdt5y2022-b19013.dat",
    "acs2022-b17001.dat": BASE + "acsdt5y2022-b17001.dat",
    "acs2022-b25003.dat": BASE + "acsdt5y2022-b25003.dat",
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for filename, url in SOURCES.items():
        request = urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
        data = urllib.request.urlopen(request, timeout=120).read()
        digest = hashlib.sha256(data).hexdigest()
        (OUT / filename).write_bytes(data)
        manifest[filename] = {"url": url, "sha256": digest, "bytes": len(data)}
        print(f"{filename}: sha256:{digest} ({len(data)} bytes)")
    (OUT / "acs2022-zcta-context-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
