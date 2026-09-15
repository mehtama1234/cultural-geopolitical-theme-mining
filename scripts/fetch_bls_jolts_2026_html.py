#!/usr/bin/env python3
"""Fetch the BLS public series pages and derive a transparent 2026 JOLTS YTD mean."""

from __future__ import annotations

import hashlib
import html
import json
import re
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


def clean(value: str) -> str:
    value = html.unescape(re.sub(r"<[^>]+>", "", value))
    return " ".join(value.split())


def fetch(series_id: str) -> tuple[bytes, dict[str, float], list[str]]:
    url = f"https://data.bls.gov/timeseries/{series_id}"
    request = urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    raw = urllib.request.urlopen(request, timeout=30).read()
    row = re.search(r"<tr[^>]*>\s*<th[^>]*>2026</th>(.*?)</tr>", raw.decode("utf-8", "replace"), re.S | re.I)
    if not row:
        raise RuntimeError(f"2026 row not found for {series_id}")
    cells = [clean(x) for x in re.findall(r"<td[^>]*>(.*?)</td>", row.group(1), re.S | re.I)]
    values: dict[str, float] = {}
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month, cell in zip(months, cells):
        if cell and cell not in {"&nbsp;", "-"}:
            values[month] = float(cell.replace("(P)", ""))
    return raw, values, cells


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    monthly: dict[str, dict[str, float]] = {}
    raw_hashes: dict[str, str] = {}
    preliminary: dict[str, list[str]] = {}
    source_urls: dict[str, str] = {}
    for series_id, name in SERIES.items():
        raw, values, cells = fetch(series_id)
        raw_path = OUT / f"bls-jolts-{name}-2026-series-page.html"
        raw_path.write_bytes(raw)
        raw_hashes[series_id] = hashlib.sha256(raw).hexdigest()
        source_urls[series_id] = f"https://data.bls.gov/timeseries/{series_id}"
        monthly[name] = values
        preliminary[name] = [m for m, c in zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], cells) if "(P)" in c]

    means = {
        name: round(sum(values.values()) / len(values), 4)
        for name, values in monthly.items()
    }
    derived = {
        "format": "bls-jolts-2026-ytd-html-derivation-v1",
        "source_urls": source_urls,
        "retrieval_hashes": raw_hashes,
        "months_observed": sorted({m for values in monthly.values() for m in values}, key=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index),
        "monthly_rates_percent": monthly,
        "preliminary_months": preliminary,
        "ytd_mean_of_monthly_rates_percent": means,
        "method": "Arithmetic mean of the seven available January-July 2026 seasonally adjusted national JOLTS rates; July is marked preliminary on the BLS series pages. This is a partial-year context measure, not a 2026 annual estimate or individual transition probability.",
    }
    (OUT / "bls-jolts-national-rates-2026-ytd-derived.json").write_text(json.dumps(derived, indent=2) + "\n")
    print(json.dumps(derived, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
