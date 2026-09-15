#!/usr/bin/env python3
"""Fetch the official Federal Reserve 2024 household well-being pages."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-consumer-fraud-trust/data"
URLS = {
    "federal-reserve-household-wellbeing-2024-banking-credit.html":
        "https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm",
    "federal-reserve-household-wellbeing-2024-accessibility-tables.html":
        "https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-accessibility-tables.htm",
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for filename, url in URLS.items():
        request = urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
        data = urllib.request.urlopen(request, timeout=30).read()
        path = OUT / filename
        path.write_bytes(data)
        manifest.append({"filename": filename, "url": url, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    (OUT / "federal-reserve-household-wellbeing-2024-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for item in manifest:
        print(f"{item['filename']}: sha256:{item['sha256']} ({item['bytes']} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
