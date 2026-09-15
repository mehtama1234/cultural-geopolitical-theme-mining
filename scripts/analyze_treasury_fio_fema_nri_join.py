#!/usr/bin/env python3
"""Join Treasury 2022 ZIP metrics to FEMA NRI county hazard context."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/us-housing-insurance-risk/data"
REL = DATA / "census-2020-zcta-county-relationship.txt"
OUT = DATA / "treasury-fio-fema-nri-2022-join.json"


def main() -> int:
    # A ZCTA can intersect multiple counties; use the county containing the
    # largest reported ZCTA land-area part, and retain ambiguity counts.
    zcta_counties = defaultdict(list)
    with REL.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="|"):
            zcta = row.get("GEOID_ZCTA5_20", "")
            county = row.get("GEOID_COUNTY_20", "")
            if not zcta or not county or not row.get("AREALAND_PART"):
                continue
            try:
                # GEOID_ZCTA5_20 is the five-digit code (for example 00601),
                # matching Treasury's five-digit ZIP value directly.
                zcta_counties[zcta].append((county, int(row["AREALAND_PART"])))
            except ValueError:
                continue
    primary_county = {z: max(parts, key=lambda x: x[1])[0] for z, parts in zcta_counties.items()}

    nri = {}
    for path in [DATA / "fema-nri-counties-0.json", DATA / "fema-nri-counties-2000.json"]:
        payload = json.loads(path.read_text())
        for feature in payload.get("features", []):
            attrs = feature.get("attributes", {})
            if attrs.get("STCOFIPS"):
                nri[attrs["STCOFIPS"]] = attrs

    groups = defaultdict(list)
    total = matched = 0
    ws = load_workbook(DATA / "treasury-fio-homeowners-insurance-2018-2022.xlsx", read_only=True, data_only=True)["Supporting Underlying Metrics"]
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[1] != 2022 or row[0] is None or row[6] is None or row[7] is None:
            continue
        total += 1
        zcta = str(int(row[0])).zfill(5)
        county = primary_county.get(zcta)
        n = nri.get(county)
        if n is None:
            continue
        matched += 1
        rating = n.get("EAL_RATNG") or "missing"
        groups[rating].append({"premium": float(row[6]), "nonrenewal": float(row[7]), "claim_severity": float(row[4]) if row[4] is not None else None})

    summaries = {}
    for rating, values in sorted(groups.items()):
        def mean(key):
            x = [v[key] for v in values if v[key] is not None]
            return round(sum(x) / len(x), 6) if x else None
        summaries[rating] = {"matched_zip_rows": len(values), "mean_premium_per_policy": mean("premium"), "mean_nonrenewal_rate": mean("nonrenewal"), "mean_claim_severity": mean("claim_severity")}
    result = {
        "format": "treasury-fio-fema-nri-join-v1",
        "period": "Treasury 2022 market rows; current FEMA NRI county baseline",
        "treasury_input": "treasury-fio-homeowners-insurance-2018-2022.xlsx",
        "fema_inputs": ["fema-nri-counties-0.json", "fema-nri-counties-2000.json"],
        "census_relationship_input": "census-2020-zcta-county-relationship.txt",
        "treasury_2022_rows_considered": total,
        "matched_2022_rows": matched,
        "match_rate": round(matched / total, 6) if total else None,
        "zcta_counties": len(zcta_counties),
        "classification": "Each ZCTA is assigned the county with the largest reported ZCTA land-area part; county-level FEMA EAL rating is then attached.",
        "summaries": summaries,
        "limits": ["ZCTA-to-county assignment is an area-based approximation and discards secondary county intersections.", "The FEMA NRI release/version is not a 2022 household or insurance-market observation and has temporal and modeled-risk limitations.", "Treasury metrics are not household-level, the workbook is not a complete insurer census, and results are unweighted means of ZIP rows.", "Joined differences are descriptive and do not identify hazard causation, affordability, nonrenewal mechanism, repairs, mobility, or politics."],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"treasury_2022_rows_considered": total, "matched_2022_rows": matched, "match_rate": result["match_rate"], "zcta_counties": len(zcta_counties), "summaries": summaries}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
