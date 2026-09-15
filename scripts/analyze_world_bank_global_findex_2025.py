#!/usr/bin/env python3
"""Fetch the public World Bank Global Findex 2025 country-level API slice.

The 2025 release is a country/demographic aggregate layer.  This script keeps
the API responses and their hashes explicit, and treats indicators that are
structurally unavailable in a country's questionnaire as unavailable rather
than as zero.
"""

from __future__ import annotations

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-financial-intermediation/data/world-bank-global-findex-2025-api-extract.json"
BASE = "https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=100"

COUNTRIES = ["USA", "CAN", "DEU", "CHN", "IND", "ZAF", "MEX", "BRA", "GBR"]
INDICATORS = [
    "account.t.d", "account.t.d.1", "account.t.d.2",
    "con1", "con1.1", "con1.2", "con9a",
    "g20.any", "fin24aP", "fin24aN", "save.any.t.d", "fin26a", "fin22a",
]


def fetch(url: str) -> tuple[bytes, dict]:
    raw = urlopen(url, timeout=45).read()
    return raw, json.loads(raw.decode("utf-8"))


def main() -> None:
    payload: dict = {
        "format": "world-bank-global-findex-2025-api-extract-v1",
        "release": "Global Findex Database 2025; survey fielded 2024",
        "api_source": "World Bank API source 14",
        "retrieved": "2026-09-15",
        "indicator_definitions": {},
        "responses": {},
        "values": {},
    }

    # Retrieve the indicator catalog once so the output carries the exact
    # public labels used to interpret the short indicator identifiers.
    catalog_url = "https://api.worldbank.org/v2/indicator?format=json&per_page=2000&source=14"
    catalog_raw, catalog = fetch(catalog_url)
    payload["catalog_url"] = catalog_url
    payload["catalog_hash"] = "sha256:" + hashlib.sha256(catalog_raw).hexdigest()
    for item in catalog[1]:
        if item["id"] in INDICATORS:
            payload["indicator_definitions"][item["id"]] = item["name"]

    def get_one(item: tuple[str, str]) -> tuple[str, str, dict, dict]:
        country, indicator = item
        url = BASE.format(country=country, indicator=indicator)
        raw, response = fetch(url)
        rows = response[1] if len(response) > 1 else []
        values = {
            str(row["date"]): row.get("value")
            for row in rows
            if row.get("date") in {"2011", "2014", "2017", "2021", "2024"}
        }
        meta = {"url": url, "sha256": hashlib.sha256(raw).hexdigest(), "lastupdated": response[0].get("lastupdated")}
        return country, indicator, meta, values

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(get_one, [(c, i) for c in COUNTRIES for i in INDICATORS])
        for country, indicator, meta, values in results:
            payload["responses"][f"{country}/{indicator}"] = meta
            payload["values"].setdefault(country, {})[indicator] = values

    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {OUT.relative_to(ROOT)}")
    print(f"countries={len(COUNTRIES)} indicators={len(INDICATORS)} responses={len(payload['responses'])}")


if __name__ == "__main__":
    main()
