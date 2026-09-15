#!/usr/bin/env python3
"""Audit operational fields carried by current HRSA primary-care HPSA rows."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path


def number(raw: str) -> float | None:
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


FIELDS = {
    "fte": "HPSA FTE",
    "designation_population": "HPSA Designation Population",
    "estimated_underserved_population": "HPSA Estimated Underserved Population",
    "score": "HPSA Score",
    "shortage": "HPSA Shortage",
}


def stats(rows: list[dict[str, object]], key: str) -> dict[str, object]:
    values = [row[key] for row in rows if isinstance(row.get(key), float)]
    if not values:
        return {"available": 0, "rows": len(rows), "median": None, "p25": None, "p75": None}
    return {
        "available": len(values),
        "rows": len(rows),
        "median": round(statistics.median(values), 3),
        "p25": round(statistics.quantiles(values, n=4, method="inclusive")[0], 3) if len(values) > 1 else round(values[0], 3),
        "p75": round(statistics.quantiles(values, n=4, method="inclusive")[2], 3) if len(values) > 1 else round(values[0], 3),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hpsa", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    with args.hpsa.open(newline="", encoding="latin1") as handle:
        for raw in csv.DictReader(handle):
            if raw.get("HPSA Status") != "Designated" or raw.get("HPSA Discipline Class") != "Primary Care":
                continue
            state = raw.get("State Abbreviation", "")
            if state in {"PR", "VI", "GU", "AS", "MP", "PW"}:
                continue
            fips = raw.get("State and County Federal Information Processing Standard Code", "")
            if len(fips) != 5 or not fips.isdigit():
                continue
            row: dict[str, object] = {
                "fips": fips,
                "hpsa_type": raw.get("HPSA Type Code") or "Unknown",
                "component_type": raw.get("HPSA Component Type Code") or "Unknown",
                "population_type": raw.get("HPSA Population Type Code") or "Unknown",
            }
            for key, field in FIELDS.items():
                row[key] = number(raw.get(field, ""))
            rows.append(row)

    group_defs = {
        "all_designated_primary_care_rows": lambda row: True,
        "geographic_type": lambda row: row["hpsa_type"] in {"Hpsa Geo", "Hpsa Geo HN"},
        "population_type": lambda row: row["hpsa_type"] == "Hpsa Pop",
        "facility_or_site_type": lambda row: row["hpsa_type"] in {"RHC", "FQHC", "FQHC LAL", "ITU", "PRSN", "OFAC"},
        "census_tract_component": lambda row: row["component_type"] == "CT",
        "county_or_subdivision_component": lambda row: row["component_type"] in {"SCTY", "CSD"},
        "low_income_population_code": lambda row: row["population_type"] in {"LI", "LI-MFW", "LI-H-MFW"},
        "migrant_or_seasonal_population_code": lambda row: row["population_type"] in {"M", "MFW", "LI-MFW", "LI-H-MFW"},
    }
    summaries = {}
    for name, predicate in group_defs.items():
        selected = [row for row in rows if predicate(row)]
        summaries[name] = {
            "rows": len(selected),
            "unique_counties": len({row["fips"] for row in selected}),
            "fields": {key: stats(selected, key) for key in FIELDS},
        }

    result = {
        "format": "us-hrsa-hpsa-operational-fields-audit-v1",
        "source_unit": "Current designated primary-care HPSA row; row-level fields grouped by overlapping component/type/population categories",
        "geography": "United States 50 states and DC; territories and Palau excluded",
        "designated_rows": len(rows),
        "unique_counties": len({row["fips"] for row in rows}),
        "summaries": summaries,
        "method": "Row-level parsing of current HRSA CSV. Medians and quartiles are not population-weighted; overlapping HPSA rows are not summed into county totals.",
        "boundary": "FTE, shortage, designated population, underserved population, and score are designation-file fields, not observed appointments, active capacity, travel, quality, affordability, or household outcomes. Missing fields are retained as missing; overlapping components make national sums inappropriate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"designated_rows": len(rows), "unique_counties": result["unique_counties"], "summaries": summaries}, indent=2))


if __name__ == "__main__":
    main()
