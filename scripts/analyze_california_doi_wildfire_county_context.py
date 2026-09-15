#!/usr/bin/env python3
"""Condition California's 2022 voluntary-market panel on CDI wildfire exposure."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from openpyxl import load_workbook
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/us-housing-insurance-risk/data"
OUT = DATA / "california-doi-wildfire-county-context-2022-join.json"


def read_risk() -> dict[str, dict[str, float]]:
    text = "\n".join(page.extract_text() or "" for page in PdfReader(DATA / "california-doi-wildfire-risk-appendix-c.pdf").pages)
    # pypdf preserves the two-column table as one line with repeated headers.
    pattern = re.compile(r"^([A-Za-z .'-]+?)\s+([\d,]+)\s+([\d,]+)\s+([\d.]+)%\s+([A-Za-z .'-]+?)\s+([\d,]+)\s+([\d,]+)\s+([\d.]+)%$")
    result: dict[str, dict[str, float]] = {}
    for line in text.splitlines():
        match = pattern.match(" ".join(line.split()))
        if not match:
            continue
        for name, units, high_units, share in (match.group(1), match.group(2), match.group(3), match.group(4)), (match.group(5), match.group(6), match.group(7), match.group(8)):
            result[name.strip()] = {"dwelling_units": int(units.replace(",", "")), "high_very_high_units": int(high_units.replace(",", "")), "high_very_high_share": float(share)}
    return result


def main() -> int:
    risk = read_risk()
    ws = load_workbook(DATA / "california-residential-insurance-zip-2020-2023.xlsx", read_only=True, data_only=True).active
    counties: dict[str, dict[str, int]] = defaultdict(lambda: {"new": 0, "renewed": 0, "nonrenewed": 0, "zip_rows": 0})
    for county, _zip, year, new, renewed, nonrenewed in ws.iter_rows(min_row=2, values_only=True):
        if year != 2022 or not str(county).strip():
            continue
        a = counties[str(county).strip()]
        a["zip_rows"] += 1
        a["new"] += new or 0
        a["renewed"] += renewed or 0
        a["nonrenewed"] += nonrenewed or 0

    joined = []
    for county, counts in counties.items():
        if county not in risk:
            continue
        row = {"county": county, **counts, **risk[county]}
        row["nonrenewal_rate_among_renewal_decisions"] = round(counts["nonrenewed"] / (counts["renewed"] + counts["nonrenewed"]), 6) if counts["renewed"] + counts["nonrenewed"] else None
        joined.append(row)
    joined.sort(key=lambda x: x["high_very_high_share"])

    def summarize(rows: list[dict]) -> dict:
        renewed = sum(r["renewed"] for r in rows)
        nonrenewed = sum(r["nonrenewed"] for r in rows)
        return {"counties": len(rows), "renewed": renewed, "nonrenewed": nonrenewed, "weighted_nonrenewal_rate": round(nonrenewed / (renewed + nonrenewed), 6) if renewed + nonrenewed else None, "mean_high_very_high_share": round(sum(r["high_very_high_share"] for r in rows) / len(rows), 3) if rows else None}

    q = len(joined) // 4
    result = {
        "format": "california-doi-wildfire-county-context-2022-v1",
        "period": "2022 voluntary-market counts; CDI wildfire exposure appendix dated to 2015 dwelling-unit base",
        "voluntary_input": "california-residential-insurance-zip-2020-2023.xlsx",
        "risk_input": "california-doi-wildfire-risk-appendix-c.pdf",
        "risk_rows": len(risk),
        "voluntary_counties": len(counties),
        "joined_counties": len(joined),
        "join_rate_against_nonblank_voluntary_counties": round(len(joined) / len(counties), 6) if counties else None,
        "quartile_comparison": {"lowest_exposure_quartile": summarize(joined[:q]), "highest_exposure_quartile": summarize(joined[-q:])},
        "statewide_exposure_threshold_comparison": {"below_12_1_percent": summarize([r for r in joined if r["high_very_high_share"] < 12.1]), "at_or_above_12_1_percent": summarize([r for r in joined if r["high_very_high_share"] >= 12.1])},
        "classification": "County-level descriptive context join; not a causal estimate and not a direct FAIR-share adjustment.",
        "limits": ["CDI's exposure appendix uses Department of Finance dwelling-unit estimates as of January 1, 2015, while the voluntary counts are 2022.", "The voluntary workbook is aggregated from ZIP rows and its county field has 35 blank 2022 rows excluded.", "The risk share is a modelers' weighted average, not observed loss or household risk.", "The voluntary counts cover policy forms and decisions that do not share an identical denominator with the FAIR residential-structure share."],
        "joined_rows": joined,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("risk_rows", "voluntary_counties", "joined_counties", "join_rate_against_nonblank_voluntary_counties", "quartile_comparison", "statewide_exposure_threshold_comparison")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
