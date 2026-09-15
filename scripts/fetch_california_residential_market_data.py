#!/usr/bin/env python3
"""Fetch California DOI public residential insurance market files."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-housing-insurance-risk/data"
SOURCES = {
    "california-residential-insurance-zip-2020-2023.xlsx": "https://www.insurance.ca.gov/01-consumers/200-wrr/upload/Residential-Insurance-Voluntary-Market-New-Renew-NonRenew-by-ZIP-2020-2023.xlsx",
    "california-residential-insurance-county-2020-2023.pdf": "https://www.insurance.ca.gov/01-consumers/200-wrr/upload/Residential-Insurance-Policy-Analysis-by-County-2020-to-2023-2.pdf",
    "california-fair-plan-vs-voluntary-2022.pdf": "https://www.insurance.ca.gov/01-consumers/200-wrr/upload/Number-of-Residential-Dwelling-Units-Insured-in-2022-FAIR-Plan-vs-Voluntary.pdf",
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
    (OUT / "california-residential-market-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
