#!/usr/bin/env python3
"""Extract a comparable IMF FAS provider-side slice across selected economies."""

from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-financial-intermediation/data/imf-fas-cross-country-2020-2024-summary.json"
COUNTRIES = ["USA", "CAN", "DEU", "GBR", "CHN", "IND", "BRA", "ZAF", "MEX"]
INDICATORS = ["COMBANK", "FA22_COMBANK", "FA26N", "OUTD_COMBANK_S14", "OUTL_COMBANK_S14"]


def main() -> None:
    result = {
        "format": "imf-fas-cross-country-summary-v1",
        "dataflow": "IMF.STA:FAS(5.0.0)",
        "period": "2020-2024",
        "countries": {},
        "indicator_selection": {
            "FA26N": "retain UNIT=NUM and TYPE_OF_TRANSFORMATION=PHTADLT_NUM; commercial-bank branches per 100,000 adults",
            "other": "retain returned series and preserve missing country-year cells",
        },
    }
    for country in COUNTRIES:
        url = f"https://api.imf.org/external/sdmx/2.1/data/IMF.STA,FAS,5.0.0/{country}?startPeriod=2020&endPeriod=2024"
        cached = Path(f"/tmp/imf-fas-{country}.csv")
        if cached.exists() and cached.stat().st_size > 0:
            raw = cached.read_bytes()
        else:
            raw = urlopen(Request(url, headers={"Accept": "application/vnd.sdmx.data+csv;version=2.0.0"}), timeout=45).read()
        rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))
        values: dict[str, dict[str, float]] = {}
        for indicator in INDICATORS:
            selected = [row for row in rows if row["INDICATOR"] == indicator and row["OBS_VALUE"] not in {"", None}]
            if indicator == "FA26N":
                selected = [row for row in selected if row["UNIT"] == "NUM" and row["TYPE_OF_TRANSFORMATION"] == "PHTADLT_NUM"]
            values[indicator] = {
                row["TIME_PERIOD"]: float(row["OBS_VALUE"])
                for row in selected
                if row["TIME_PERIOD"] in {"2020", "2024"}
            }
        result["countries"][country] = {
            "query_url": url,
            "response_sha256": hashlib.sha256(raw).hexdigest(),
            "response_bytes": len(raw),
            "rows_returned": len(rows),
            "values": values,
        }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {OUT.relative_to(ROOT)}")
    print(f"countries={len(COUNTRIES)} indicators={len(INDICATORS)}")


if __name__ == "__main__":
    main()
