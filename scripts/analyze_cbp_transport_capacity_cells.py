#!/usr/bin/env python3
"""Compare county health-sector capacity with vehicle and commute context."""

from __future__ import annotations

import argparse
import csv
import io
import json
import statistics
from pathlib import Path
from zipfile import ZipFile


def read_acs(path: Path, prefix: str) -> dict[str, dict[str, int]]:
    out: dict[str, dict[str, int]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="|"):
            geo = row.get("GEO_ID", "")
            if not geo.startswith("0500000US"):
                continue
            values: dict[str, int] = {}
            for key, value in row.items():
                if key.startswith(prefix + "_E"):
                    try:
                        values[key] = int(value)
                    except (TypeError, ValueError):
                        pass
            if values:
                out[geo[-5:]] = values
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--vehicle", type=Path, required=True)
    parser.add_argument("--commute", type=Path, required=True)
    parser.add_argument("--hpsa", type=Path, required=True)
    parser.add_argument("--rucc", type=Path, required=True)
    parser.add_argument("--rent", type=Path)
    parser.add_argument("--crowding", type=Path)
    parser.add_argument("--language", type=Path)
    parser.add_argument("--income", type=Path)
    parser.add_argument("--vacancy", type=Path)
    parser.add_argument("--qcew", type=Path)
    parser.add_argument("--permits", type=Path)
    parser.add_argument("--mode", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    population: dict[str, int] = {}
    with args.population.open(encoding="latin1", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("SUMLEV") == "050" and row.get("POPESTIMATE2023"):
                population[row["STATE"] + row["COUNTY"]] = int(row["POPESTIMATE2023"])

    vehicle = read_acs(args.vehicle, "B08201")
    commute = read_acs(args.commute, "B08303")
    rent = read_acs(args.rent, "B25064") if args.rent else {}
    crowding = read_acs(args.crowding, "B25014") if args.crowding else {}
    language = read_acs(args.language, "C16001") if args.language else {}
    income = read_acs(args.income, "B19013") if args.income else {}
    vacancy = read_acs(args.vacancy, "B25002") if args.vacancy else {}
    qcew_wage: dict[str, float] = {}
    if args.qcew:
        with ZipFile(args.qcew) as archive:
            member = next(name for name in archive.namelist() if name.endswith(".csv"))
            with archive.open(member) as raw:
                for row in csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8")):
                    if row.get("agglvl_code") != "70" or row.get("industry_code") != "10":
                        continue
                    area = row.get("area_fips", "")
                    try:
                        qcew_wage[area] = float(row["annual_avg_wkly_wage"])
                    except (KeyError, TypeError, ValueError):
                        pass
    permits: dict[str, dict[str, int]] = {}
    if args.permits:
        with args.permits.open(encoding="utf-8", newline="") as handle:
            for row in csv.reader(handle):
                if len(row) < 18 or not row[1].isdigit() or not row[2].isdigit():
                    continue
                key = f"{int(row[1]):02d}{int(row[2]):03d}"
                try:
                    buildings = sum(int(row[i]) for i in (6, 9, 12, 15))
                    units = sum(int(row[i]) for i in (7, 10, 13, 16))
                except (IndexError, TypeError, ValueError):
                    continue
                permits[key] = {"buildings": buildings, "units": units}
    mode = read_acs(args.mode, "B08301") if args.mode else {}
    rucc: dict[str, int] = {}
    with args.rucc.open(encoding="latin1", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("Attribute") == "RUCC_2023":
                try:
                    rucc[row["FIPS"]] = int(row["Value"])
                except (KeyError, ValueError):
                    pass

    hpsa: set[str] = set()
    with args.hpsa.open(encoding="latin1", newline="") as handle:
        for row in csv.DictReader(handle):
            key = row.get("State and County Federal Information Processing Standard Code", "")
            if row.get("HPSA Status") == "Designated" and len(key) == 5 and key.isdigit():
                hpsa.add(key)

    capacity: dict[str, dict[str, int]] = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                key = row.get("fipstate", "") + row.get("fipscty", "")
                if row.get("naics") not in {"62----", "44----", "72----"}:
                    continue
                try:
                    establishments = int(row.get("est", ""))
                except ValueError:
                    establishments = 0
                capacity.setdefault(key, {})[row["naics"]] = establishments

    rows: list[dict[str, float | int | bool]] = []
    required_keys = set(population) & set(capacity) & set(vehicle) & set(commute) & set(rucc)
    for optional in (rent, crowding, language, income, vacancy, qcew_wage, permits, mode):
        if optional:
            required_keys &= set(optional)
    for key in sorted(required_keys):
        v, c = vehicle[key], commute[key]
        if not v.get("B08201_E001") or not c.get("B08303_E001"):
            continue
        health = 10_000 * capacity[key].get("62----", 0) / population[key]
        zero_vehicle = 100 * v.get("B08201_E002", 0) / v["B08201_E001"]
        long_commute = 100 * sum(c.get(f"B08303_E{i:03d}", 0) for i in range(8, 14)) / c["B08303_E001"]
        rent_value = rent.get(key, {}).get("B25064_E001")
        crowd = crowding.get(key, {})
        crowd_total = crowd.get("B25014_E001")
        crowded_value = None
        if crowd_total:
            crowded_value = 100 * sum(crowd.get(f"B25014_E{i:03d}", 0) for i in (5, 6, 7, 11, 12, 13)) / crowd_total
        lang = language.get(key, {})
        lang_total = lang.get("C16001_E001")
        limited_english_value = None
        if lang_total:
            limited_english_value = 100 * sum(lang.get(f"C16001_E{i:03d}", 0) for i in (5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38)) / lang_total
        income_value = income.get(key, {}).get("B19013_E001")
        vacancy_row = vacancy.get(key, {})
        vacancy_total = vacancy_row.get("B25002_E001")
        vacancy_value = None
        if vacancy_total:
            vacancy_value = 100 * vacancy_row.get("B25002_E003", 0) / vacancy_total
        qcew_wage_value = qcew_wage.get(key)
        permit_row = permits.get(key, {})
        permit_units_per_1000 = 1000 * permit_row.get("units", 0) / population[key] if permit_row else None
        permit_buildings_per_1000 = 1000 * permit_row.get("buildings", 0) / population[key] if permit_row else None
        mode_row = mode.get(key, {})
        mode_total = mode_row.get("B08301_E001")
        public_transit_pct = 100 * mode_row.get("B08301_E010", 0) / mode_total if mode_total else None
        walked_pct = 100 * mode_row.get("B08301_E019", 0) / mode_total if mode_total else None
        worked_home_pct = 100 * mode_row.get("B08301_E021", 0) / mode_total if mode_total else None
        rows.append({
            "fips": key,
            "population": population[key],
            "health_est_per_10k": health,
            "retail_est_per_10k": 10_000 * capacity[key].get("44----", 0) / population[key],
            "food_est_per_10k": 10_000 * capacity[key].get("72----", 0) / population[key],
            "zero_vehicle_pct": zero_vehicle,
            "long_commute_pct": long_commute,
            "median_gross_rent": rent_value,
            "crowded_units_pct": crowded_value,
            "limited_english_pct": limited_english_value,
            "median_household_income": income_value,
            "vacancy_pct": vacancy_value,
            "qcew_avg_weekly_wage": qcew_wage_value,
            "permit_units_per_1000": permit_units_per_1000,
            "permit_buildings_per_1000": permit_buildings_per_1000,
            "public_transit_commute_pct": public_transit_pct,
            "walk_commute_pct": walked_pct,
            "worked_from_home_pct": worked_home_pct,
            "hpsa": key in hpsa,
            "nonmetro": rucc[key] >= 4,
        })

    capacity_cut = statistics.median(row["health_est_per_10k"] for row in rows)
    vehicle_cut = statistics.median(row["zero_vehicle_pct"] for row in rows)
    cells: dict[str, dict[str, object]] = {}
    for capacity_high in (False, True):
        for vehicle_high in (False, True):
            label = f"{'high' if capacity_high else 'low'}_health_capacity__{'high' if vehicle_high else 'low'}_zero_vehicle_share"
            selected = [row for row in rows if (row["health_est_per_10k"] >= capacity_cut) == capacity_high and (row["zero_vehicle_pct"] >= vehicle_cut) == vehicle_high]
            pop = sum(int(row["population"]) for row in selected)
            cells[label] = {
                "counties": len(selected),
                "population": pop,
                "population_weighted_hpsa_share_percent": 100 * sum(int(row["population"]) for row in selected if row["hpsa"]) / pop if pop else None,
                "nonmetro_share_percent": 100 * sum(int(row["population"]) for row in selected if row["nonmetro"]) / pop if pop else None,
                "median_health_est_per_10k": statistics.median(row["health_est_per_10k"] for row in selected) if selected else None,
                "median_retail_est_per_10k": statistics.median(row["retail_est_per_10k"] for row in selected) if selected else None,
                "median_food_est_per_10k": statistics.median(row["food_est_per_10k"] for row in selected) if selected else None,
                "median_zero_vehicle_pct": statistics.median(row["zero_vehicle_pct"] for row in selected) if selected else None,
                "median_long_commute_pct": statistics.median(row["long_commute_pct"] for row in selected) if selected else None,
                "median_gross_rent": statistics.median([row["median_gross_rent"] for row in selected if row["median_gross_rent"] is not None]) if any(row["median_gross_rent"] is not None for row in selected) else None,
                "median_crowded_units_pct": statistics.median([row["crowded_units_pct"] for row in selected if row["crowded_units_pct"] is not None]) if any(row["crowded_units_pct"] is not None for row in selected) else None,
                "median_limited_english_pct": statistics.median([row["limited_english_pct"] for row in selected if row["limited_english_pct"] is not None]) if any(row["limited_english_pct"] is not None for row in selected) else None,
                "median_household_income": statistics.median([row["median_household_income"] for row in selected if row["median_household_income"] is not None]) if any(row["median_household_income"] is not None for row in selected) else None,
                "median_vacancy_pct": statistics.median([row["vacancy_pct"] for row in selected if row["vacancy_pct"] is not None]) if any(row["vacancy_pct"] is not None for row in selected) else None,
                "median_qcew_avg_weekly_wage": statistics.median([row["qcew_avg_weekly_wage"] for row in selected if row["qcew_avg_weekly_wage"] is not None]) if any(row["qcew_avg_weekly_wage"] is not None for row in selected) else None,
                "median_permit_units_per_1000": statistics.median([row["permit_units_per_1000"] for row in selected if row["permit_units_per_1000"] is not None]) if any(row["permit_units_per_1000"] is not None for row in selected) else None,
                "median_permit_buildings_per_1000": statistics.median([row["permit_buildings_per_1000"] for row in selected if row["permit_buildings_per_1000"] is not None]) if any(row["permit_buildings_per_1000"] is not None for row in selected) else None,
                "median_public_transit_commute_pct": statistics.median([row["public_transit_commute_pct"] for row in selected if row["public_transit_commute_pct"] is not None]) if any(row["public_transit_commute_pct"] is not None for row in selected) else None,
                "median_walk_commute_pct": statistics.median([row["walk_commute_pct"] for row in selected if row["walk_commute_pct"] is not None]) if any(row["walk_commute_pct"] is not None for row in selected) else None,
                "median_worked_from_home_pct": statistics.median([row["worked_from_home_pct"] for row in selected if row["worked_from_home_pct"] is not None]) if any(row["worked_from_home_pct"] is not None for row in selected) else None,
            }

    result = {
        "format": "us-cbp-acs-transport-capacity-cells-v1",
        "source_unit": "US county, 2023 CBP stock joined to 2023 population, 2023 ACS 5-year vehicle/commute/mode/rent/crowding/language/income/vacancy context, 2023 QCEW all-industry wage context, and 2023 Census BPS permit flow",
        "matched_counties": len(rows),
        "capacity_cut_median_health_est_per_10k": capacity_cut,
        "vehicle_context_cut_median_zero_vehicle_pct": vehicle_cut,
        "cells": cells,
        "method": "County-level descriptive four-cell comparison; health/social-assistance establishment density and zero-vehicle-household share are split at unweighted county medians; cell summaries retain population weights for HPSA and rurality shares.",
        "uncertainty": "ACS margins of error are not propagated in this first pass; CBP employment/service adequacy, neighboring supply, prices beyond gross rent, hours, quality, use, and causal effects remain unmeasured.",
        "boundary": "A high zero-vehicle share is a mobility constraint context, not a complete measure of mobility options; transit, destination, affordability, and travel reliability require separate data.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
