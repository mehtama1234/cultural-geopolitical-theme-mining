#!/usr/bin/env python3
"""Fetch the New York Fed household debt and credit dashboard snapshot."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-household-financial-pressure/data"
URL = "https://www.newyorkfed.org/householdcredit/hhdc-iframe"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(URL, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    data = urllib.request.urlopen(request, timeout=30).read()
    path = OUT / "new-york-fed-hhdc-current.html"
    path.write_bytes(data)
    manifest = {"filename": path.name, "url": URL, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
    (OUT / "new-york-fed-hhdc-current-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{path.name}: sha256:{manifest['sha256']} ({manifest['bytes']} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
