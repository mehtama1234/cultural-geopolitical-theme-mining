#!/usr/bin/env python3
"""Fetch national JOLTS monthly rates and derive transparent annual means."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/ai-work-control/data"
SERIES = {
    "JTS000000000000000JOR": "job_openings_rate",
    "JTS000000000000000HIR": "hires_rate",
    "JTS000000000000000QUR": "quits_rate",
    "JTS000000000000000LDR": "layoffs_and_discharges_rate",
    "JTS000000000000000TSR": "total_separations_rate",
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    request_body = {"seriesid": list(SERIES), "startyear": "2020", "endyear": "2025"}
    encoded = json.dumps(request_body, separators=(",", ":")).encode()
    request = urllib.request.Request(
        "https://api.bls.gov/publicAPI/v2/timeseries/data/",
        data=encoded,
        headers={"Content-Type": "application/json", "User-Agent": "cultural-geopolitical-theme-mining/1.0"},
    )
    response = urllib.request.urlopen(request, timeout=30).read()
    raw_hash = hashlib.sha256(response).hexdigest()
    raw_path = OUT / "bls-jolts-national-rates-2020-2025-api.json"
    raw_path.write_bytes(response)
    payload = json.loads(response)
    annual: dict[str, dict[str, float]] = {}
    for series in payload["Results"]["series"]:
        name = SERIES[series["seriesID"]]
        for row in series["data"]:
            if row["period"].startswith("M"):
                annual.setdefault(row["year"], {})
                annual[row["year"]].setdefault(name, []).append(float(row["value"]))
    means = {
        year: {name: round(sum(values) / len(values), 4) for name, values in metrics.items()}
        for year, metrics in sorted(annual.items())
    }
    derived = {
        "format": "bls-jolts-annual-rate-derivation-v1",
        "source_url": "https://api.bls.gov/publicAPI/v2/timeseries/data/",
        "request": request_body,
        "raw_response_sha256": raw_hash,
        "annual_mean_of_monthly_rates_percent": means,
        "method": "Arithmetic mean of the twelve monthly, seasonally adjusted national JOLTS rates returned for each calendar year; no annual rate is interpreted as a stock or individual transition probability.",
    }
    (OUT / "bls-jolts-national-rates-2020-2025-derived.json").write_text(json.dumps(derived, indent=2) + "\n")
    print(f"raw_response_sha256: {raw_hash}")
    print(json.dumps(means, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
