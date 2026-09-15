#!/usr/bin/env python3
"""Fetch official BLS CES average hourly earnings for selected industries."""

from __future__ import annotations

import hashlib
import json
import argparse
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/ai-work-control/data"
SERIES = {
    "CES3000000003": "manufacturing",
    "CES6000000003": "professional_and_business_services",
    "CES6500000003": "education_and_health_services",
    "CES7000000003": "leisure_and_hospitality",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--end-year", default="2025", help="last BLS year to request")
    args = parser.parse_args()
    end_year = str(args.end_year)
    OUT.mkdir(parents=True, exist_ok=True)
    body = {"seriesid": list(SERIES), "startyear": "2022", "endyear": end_year}
    encoded = json.dumps(body, separators=(",", ":")).encode()
    request = urllib.request.Request("https://api.bls.gov/publicAPI/v2/timeseries/data/", data=encoded, headers={"Content-Type": "application/json", "User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    try:
        response = urllib.request.urlopen(request, timeout=30).read()
        payload = json.loads(response)
        if not payload.get("Results", {}).get("series"):
            raise RuntimeError("BLS API returned no series")
        digest = hashlib.sha256(response).hexdigest()
        (OUT / f"bls-ces-industry-earnings-2022-{end_year}-api.json").write_bytes(response)
        raw_sources = {series: digest for series in SERIES}
    except Exception as exc:
        if end_year != "2026":
            raise
        # The public API can throttle unauthenticated requests.  BLS series
        # pages expose the same official monthly table and are retained as
        # raw, separately hashed source artifacts for the current partial year.
        payload = {"Results": {"series": []}}
        raw_sources = {}
        for series in SERIES:
            url = f"https://data.bls.gov/timeseries/{series}"
            page = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"}), timeout=30).read()
            page_digest = hashlib.sha256(page).hexdigest()
            raw_sources[series] = page_digest
            (OUT / f"bls-ces-{SERIES[series]}-2026-series-page.html").write_bytes(page)
            match = re.search(rb'<TH scope="row">2026</TH>(.*?)</TR>', page, re.S)
            if not match:
                raise RuntimeError(f"2026 row not found for {series}; API error was {exc}")
            values = re.findall(rb'<TD>([^<]+)</TD>', match.group(1))
            payload["Results"]["series"].append({"seriesID": series, "data": [{"year": "2026", "period": f"M{i + 1:02d}", "value": value.decode().replace("(P)", "")} for i, value in enumerate(values) if value not in (b"&nbsp;", b"")]})
        digest = "; ".join(f"{series}:{value}" for series, value in raw_sources.items())
    annual: dict[str, dict[str, list[float]]] = {}
    for series in payload["Results"]["series"]:
        for row in series["data"]:
            if row["period"].startswith("M"):
                annual.setdefault(series["seriesID"], {}).setdefault(row["year"], []).append(float(row["value"]))
    means = {SERIES[series]: {year: round(sum(values) / len(values), 4) for year, values in sorted(years.items())} for series, years in annual.items()}
    derived = {"format": "bls-ces-industry-earnings-annual-derivation-v1", "source_url": "https://api.bls.gov/publicAPI/v2/timeseries/data/", "request": body, "raw_response_sha256": digest, "raw_series_page_sha256": raw_sources, "series": SERIES, "annual_mean_of_monthly_dollars_per_hour": means, "method": "Arithmetic mean of available monthly, seasonally adjusted average hourly earnings of all employees for each selected private-industry series; the final year may be partial."}
    (OUT / f"bls-ces-industry-earnings-2022-{end_year}-derived.json").write_text(json.dumps(derived, indent=2) + "\n")
    print(f"raw_response_sha256: {digest}")
    print(json.dumps(means, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
