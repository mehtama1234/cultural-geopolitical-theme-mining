#!/usr/bin/env python3
"""Fetch California FAIR Plan public policy, exposure, and context sources."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-housing-insurance-risk/data"
SOURCES = {
    "california-fair-plan-key-statistics.html": "https://www.cfpnet.com/key-statistics-data/",
    "california-fair-plan-pif-county-fy25.pdf": "https://www.cfpnet.com/wp-content/uploads/2025/11/CFP-5-yr-PIF-County-FY25-All-251114.pdf",
    "california-fair-plan-tiv-fy25.pdf": "https://www.cfpnet.com/wp-content/uploads/2025/11/CFP-5-yr-TIV-County-FY25-All-251114.pdf",
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
    (OUT / "california-fair-plan-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
