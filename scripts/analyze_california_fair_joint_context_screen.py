#!/usr/bin/env python3
"""Run a transparent joint ZIP screen across California insurance context axes."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from openpyxl import load_workbook
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/us-housing-insurance-risk/data"
OUT = DATA / "california-fair-joint-context-2022-screen.json"


def read_fair() -> dict[str, float]:
    text = "\n".join(page.extract_text() or "" for page in PdfReader(DATA / "california-fair-plan-vs-voluntary-2022.pdf").pages)
    pat = re.compile(r"^(.*?)\s+(\d{5})\s+(.*?)\s+([\d,]+|-|—)\s+([\d,]+|-|—)\s+([\d.]+)%\s*$")
    return {m.group(2): float(m.group(6)) for line in text.splitlines() if (m := pat.match(line))}


def read_acs() -> dict[str, dict[str, float]]:
    income = {}
    with (DATA / "acs2022-b19013.dat").open() as fh:
        headers = next(fh).rstrip().split("|")
        for line in fh:
            row = dict(zip(headers, line.rstrip().split("|")))
            geo = row.get("GEO_ID", "")
            if geo.startswith("860Z200US"):
                try: income[geo[-5:]] = int(row["B19013_E001"])
                except (TypeError, ValueError): pass
    result = {}
    with (DATA / "acs2022-b25024.dat").open() as fh:
        headers = next(fh).rstrip().split("|")
        for line in fh:
            row = dict(zip(headers, line.rstrip().split("|")))
            geo = row.get("GEO_ID", "")
            z = geo[-5:] if geo.startswith("860Z200US") else ""
            try:
                total, detached = int(row["B25024_E001"]), int(row["B25024_E002"])
            except (TypeError, ValueError): continue
            if z in income and income[z] >= 0 and total > 0:
                result[z] = {"income": income[z], "detached_share": detached / total * 100}
    return result


def summarize(rows: list[dict], label: str) -> dict:
    renew = sum(r["renewed"] for r in rows)
    nonrenew = sum(r["nonrenewed"] for r in rows)
    return {"group": label, "zip_rows": len(rows), "renewed": renew, "nonrenewed": nonrenew, "nonrenewal_rate": round(nonrenew / (renew + nonrenew), 6) if renew + nonrenew else None, "mean_fair_share": round(sum(r["fair_share"] for r in rows) / len(rows), 3) if rows else None}


def main() -> int:
    fair, acs = read_fair(), read_acs()
    risk = {r["county"]: r["high_very_high_share"] for r in json.loads((DATA / "california-doi-wildfire-county-context-2022-join.json").read_text())["joined_rows"]}
    ws = load_workbook(DATA / "california-residential-insurance-zip-2020-2023.xlsx", read_only=True, data_only=True).active
    rows = []
    for county, z, year, _new, renewed, nonrenewed in ws.iter_rows(min_row=2, values_only=True):
        z = str(z).zfill(5)
        county = str(county).strip()
        if year == 2022 and z in fair and z in acs and county in risk:
            rows.append({"zip": z, "county": county, "fair_share": fair[z], "renewed": renewed or 0, "nonrenewed": nonrenewed or 0, **acs[z], "risk_share": risk[county]})
    rows.sort(key=lambda r: (r["income"], r["detached_share"], r["risk_share"]))
    q = len(rows) // 4
    rows_income = sorted(rows, key=lambda r: r["income"])
    rows_detached = sorted(rows, key=lambda r: r["detached_share"])
    income_cut = rows_income[q - 1]["income"]
    detached_cut = rows_detached[q - 1]["detached_share"]
    cells = defaultdict(list)
    for r in rows:
        cells[("low_income" if r["income"] <= income_cut else "high_income", "high_risk" if r["risk_share"] >= 12.1 else "low_risk")].append(r)
    result = {
        "format": "california-fair-joint-context-2022-screen-v1",
        "period": "2022 FAIR share and voluntary decisions; ACS 2022 5-year ZCTA context; CDI county exposure context",
        "joined_zip_rows": len(rows),
        "cut_points": {"income_quartile_boundary_dollars": income_cut, "detached_share_quartile_boundary_percent": round(detached_cut, 3), "risk_threshold_percent": 12.1},
        "joint_income_by_risk": [summarize(v, f"{k[0]}__{k[1]}") for k, v in sorted(cells.items())],
        "low_high_income_by_risk_summary": {"low_income_high_risk": summarize(cells[("low_income", "high_risk")], "low_income_high_risk"), "high_income_low_risk": summarize(cells[("high_income", "low_risk")], "high_income_low_risk")},
        "classification": "Descriptive cross-source ZIP screen; not a regression, causal adjustment, or household transition estimate.",
        "limits": ["ZIPs are approximated by ACS ZCTAs and assigned county risk using the available county field; within-county variation is hidden.", "The CDI risk share uses a 2015 dwelling-unit base while voluntary decisions are from 2022.", "Income and structure are five-year place estimates; FAIR structures and voluntary policy decisions have different universes.", "Cut points and cells are unweighted by population, structures, or policies; small cells remain sensitive to composition."],
        "joined_rows": rows,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("joined_zip_rows", "cut_points", "joint_income_by_risk", "low_high_income_by_risk_summary")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
