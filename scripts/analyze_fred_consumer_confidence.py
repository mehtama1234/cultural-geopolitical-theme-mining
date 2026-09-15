#!/usr/bin/env python3
"""Reproduce the bounded FRED sentiment/price/labor comparison.

The script intentionally emits the downloaded input hash and selected monthly
points rather than committing a mutable FRED export to the repository.
"""

from __future__ import annotations

import csv
import hashlib
import io
import urllib.request

URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=UMCSENT,CPIAUCSL,UNRATE"
DATES = {"2024-01-01", "2024-12-01", "2025-12-01", "2026-07-01"}

request = urllib.request.Request(URL, headers={"User-Agent": "theme-mining-reproduction/1.0"})
with urllib.request.urlopen(request, timeout=40) as response:
    payload = response.read()

print(f"source_url={URL}")
print(f"retrieval_hash=sha256:{hashlib.sha256(payload).hexdigest()}")
for row in csv.DictReader(io.StringIO(payload.decode("utf-8"))):
    if row["observation_date"] in DATES:
        print(
            row["observation_date"],
            "UMCSENT=" + row["UMCSENT"],
            "CPIAUCSL=" + row["CPIAUCSL"],
            "UNRATE=" + row["UNRATE"],
        )
