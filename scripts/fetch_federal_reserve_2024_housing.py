#!/usr/bin/env python3
"""Fetch the official Federal Reserve 2024 housing page."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-housing-insurance-risk/data"
URL = "https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-housing.htm"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(URL, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    data = urllib.request.urlopen(request, timeout=30).read()
    digest = hashlib.sha256(data).hexdigest()
    (OUT / "federal-reserve-2024-housing.html").write_bytes(data)
    (OUT / "federal-reserve-2024-housing-manifest.json").write_text(
        json.dumps({"url": URL, "sha256": digest, "bytes": len(data)}, indent=2) + "\n"
    )
    print(f"sha256:{digest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
