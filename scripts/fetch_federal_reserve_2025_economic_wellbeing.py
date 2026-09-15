#!/usr/bin/env python3
"""Fetch official Federal Reserve 2025 economic-well-being pages."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-cost-trust-politics/data"
URLS = {
    "federal-reserve-2025-income-expenses.html": "https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-income-and-expenses.htm",
    "federal-reserve-2025-executive-summary.html": "https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm",
    "federal-reserve-2025-savings-investments.html": "https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-savings-investments.htm",
    "federal-reserve-2025-credit.html": "https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-credit.htm",
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
    (OUT / "federal-reserve-2025-economic-wellbeing-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for item in manifest:
        print(f"{item['filename']}: sha256:{item['sha256']} ({item['bytes']} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
