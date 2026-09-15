#!/usr/bin/env python3
"""Fetch Treasury FIO homeowners-insurance market sources."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-housing-insurance-risk/data"
SOURCES = {
    "treasury-fio-2025-annual-report.pdf": "https://home.treasury.gov/system/files/311/Final%20FIO%202025%20Annual%20Report.pdf",
    "treasury-fio-homeowners-insurance-2018-2022.xlsx": "https://home.treasury.gov/system/files/311/Supporting_Underlying_Metrics_and_Disclaimer_for_Analyses_of_US_Homeowners_Insurance_Markets_2018-2022.xlsx",
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for filename, url in SOURCES.items():
        request = urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
        data = urllib.request.urlopen(request, timeout=60).read()
        digest = hashlib.sha256(data).hexdigest()
        (OUT / filename).write_bytes(data)
        manifest[filename] = {"url": url, "sha256": digest, "bytes": len(data)}
        print(f"{filename}: sha256:{digest} ({len(data)} bytes)")
    (OUT / "treasury-fio-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
