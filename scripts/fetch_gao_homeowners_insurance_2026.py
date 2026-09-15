#!/usr/bin/env python3
"""Fetch GAO's 2026 homeowners-insurance review."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-housing-insurance-risk/data"
URL = "https://files.gao.gov/reports/GAO-26-107867/index.html"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(URL, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    data = urllib.request.urlopen(request, timeout=60).read()
    digest = hashlib.sha256(data).hexdigest()
    (OUT / "gao-26-107867-full-report.html").write_bytes(data)
    (OUT / "gao-26-107867-manifest.json").write_text(json.dumps({"url": URL, "sha256": digest, "bytes": len(data)}, indent=2) + "\n")
    print(f"sha256:{digest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
