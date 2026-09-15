#!/usr/bin/env python3
"""Fetch and summarize the public IMF FAS US 2020--2024 SDMX slice."""

from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/us-financial-intermediation/data"
URL = "https://api.imf.org/external/sdmx/2.1/data/IMF.STA,FAS,5.0.0/USA?startPeriod=2020&endPeriod=2024"
HEADERS = {"Accept": "application/vnd.sdmx.data+csv;version=2.0.0"}
KEEP = [
    ("COMBANK", "Commercial banks, Number", "number"),
    ("CUCC", "Credit unions and credit cooperatives, Number", "number"),
    ("FA22_COMBANK", "Branches excluding headquarters, Commercial banks, Number", "number"),
    ("FA26N", "Number of commercial bank branches, Per 100,000 adults", "per_100k_adults"),
    ("OUTD_COMBANK_S14", "Outstanding deposits, Commercial banks, Households, Percent of GDP", "percent_gdp"),
    ("OUTL_COMBANK_S14", "Outstanding loans, Commercial banks, Households, Percent of GDP", "percent_gdp"),
]


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    raw = urlopen(Request(URL, headers=HEADERS), timeout=45).read()
    raw_path = DATA / "imf-fas-us-2020-2024.csv"
    raw_path.write_bytes(raw)
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))
    summary = {
        "format": "imf-fas-us-extract-v1",
        "dataflow": "IMF.STA:FAS(5.0.0)",
        "country": "USA",
        "period": "2020-2024",
        "query_url": URL,
        "retrieval_hash": "sha256:" + hashlib.sha256(raw).hexdigest(),
        "response_bytes": len(raw),
        "rows_returned": len(rows),
        "series": {},
    }
    for indicator, label, unit_type in KEEP:
        selected = [r for r in rows if r["INDICATOR"] == indicator and r["OBS_VALUE"] not in {"", None}]
        if indicator == "FA26N":
            selected = [r for r in selected if r["UNIT"] == "NUM" and r["TYPE_OF_TRANSFORMATION"] == "PHTADLT_NUM"]
        summary["series"][indicator] = {
            "label": label,
            "unit_type": unit_type,
            "unit": selected[0]["UNIT"] if selected else None,
            "transformation": selected[0]["TYPE_OF_TRANSFORMATION"] if selected else None,
            "values": {r["TIME_PERIOD"]: float(r["OBS_VALUE"]) for r in selected},
        }
    out = DATA / "imf-fas-us-2020-2024-summary.json"
    out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {raw_path.relative_to(ROOT)}")
    print(f"WROTE {out.relative_to(ROOT)}")
    print(f"rows={len(rows)} sha256={summary['retrieval_hash']}")


if __name__ == "__main__":
    main()
