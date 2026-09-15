#!/usr/bin/env python3
"""Fetch selected official BLS JOLTS industry rates and derive annual means."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/ai-work-control/data"
INDUSTRIES = {
    "300000": "manufacturing",
    "540099": "professional_and_business_services",
    "600000": "education_and_health_services",
    "700000": "leisure_and_hospitality",
}
ELEMENTS = {"JOR": "job_openings_rate", "HIR": "hires_rate", "QUR": "quits_rate", "LDR": "layoffs_and_discharges_rate", "TSR": "total_separations_rate"}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    series_ids = [f"JTS{industry}000000000{element}" for industry in INDUSTRIES for element in ELEMENTS]
    body = {"seriesid": series_ids, "startyear": "2020", "endyear": "2025"}
    encoded = json.dumps(body, separators=(",", ":")).encode()
    request = urllib.request.Request("https://api.bls.gov/publicAPI/v2/timeseries/data/", data=encoded, headers={"Content-Type": "application/json", "User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    response = urllib.request.urlopen(request, timeout=30).read()
    raw_hash = hashlib.sha256(response).hexdigest()
    (OUT / "bls-jolts-selected-industries-2020-2025-api.json").write_bytes(response)
    payload = json.loads(response)
    annual: dict[str, dict[str, dict[str, list[float]]]] = {}
    for series in payload["Results"]["series"]:
        code = series["seriesID"]
        industry = code[3:9]
        element = code[-3:]
        for row in series["data"]:
            if row["period"].startswith("M"):
                annual.setdefault(industry, {}).setdefault(row["year"], {}).setdefault(ELEMENTS[element], []).append(float(row["value"]))
    means = {industry: {year: {name: round(sum(values) / len(values), 4) for name, values in metrics.items()} for year, metrics in sorted(years.items())} for industry, years in annual.items()}
    derived = {"format": "bls-jolts-industry-annual-rate-derivation-v1", "source_url": "https://api.bls.gov/publicAPI/v2/timeseries/data/", "request": body, "raw_response_sha256": raw_hash, "industries": INDUSTRIES, "annual_mean_of_monthly_rates_percent": means, "method": "Arithmetic mean of twelve monthly, seasonally adjusted national JOLTS rates for each selected industry and calendar year; each rate retains its BLS-specific denominator."}
    (OUT / "bls-jolts-selected-industries-2020-2025-derived.json").write_text(json.dumps(derived, indent=2) + "\n")
    print(f"raw_response_sha256: {raw_hash}")
    print(json.dumps(means, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
