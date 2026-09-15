#!/usr/bin/env python3
"""Fetch FEMA NRI county data and the official Census ZCTA-county relation."""

from __future__ import annotations

import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis/projects/us-housing-insurance-risk/data"
REL_URL = "https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_county20_natl.txt"
NRI_QUERY = "https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Counties/FeatureServer/0/query"


def fetch(url: str, filename: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    data = urllib.request.urlopen(request, timeout=120).read()
    digest = hashlib.sha256(data).hexdigest()
    (OUT / filename).write_bytes(data)
    return {"url": url, "sha256": digest, "bytes": len(data)}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"census-2020-zcta-county-relationship.txt": fetch(REL_URL, "census-2020-zcta-county-relationship.txt")}
    params = {"where": "1=1", "outFields": "STCOFIPS,STATEABBRV,COUNTY,RISK_SCORE,EAL_VALB,EAL_RATNG", "returnGeometry": "false", "f": "json", "resultRecordCount": "2000"}
    for offset in (0, 2000):
        params["resultOffset"] = str(offset)
        url = NRI_QUERY + "?" + urllib.parse.urlencode(params)
        filename = f"fema-nri-counties-{offset}.json"
        manifest[filename] = fetch(url, filename)
    (OUT / "fema-nri-census-zcta-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for name, item in manifest.items():
        print(f"{name}: sha256:{item['sha256']} ({item['bytes']} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
