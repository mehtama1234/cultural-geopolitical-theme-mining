#!/usr/bin/env python3
"""Summarize Prince William County data-center building/campus GIS exports."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def records(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [feature["attributes"] for feature in payload.get("features", [])]


def number(row: dict, field: str) -> float:
    value = row.get(field)
    return float(value) if isinstance(value, (int, float)) else 0.0


def status_summary(rows: list[dict], field: str, area_field: str) -> dict:
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        groups[str(row.get(field) or "Unknown")].append(row)
    total_area = sum(number(row, area_field) for row in rows)
    return {
        key: {
            "records": len(group),
            "area_sq_ft": sum(number(row, area_field) for row in group),
            "area_share_percent": (100 * sum(number(row, area_field) for row in group) / total_area
                                   if total_area else None),
        }
        for key, group in sorted(groups.items())
    }


def concentration(rows: list[dict], group_field: str, area_field: str) -> dict:
    areas = defaultdict(float)
    for row in rows:
        areas[str(row.get(group_field) or "Unknown")] += number(row, area_field)
    total = sum(areas.values())
    shares = {key: value / total for key, value in areas.items()} if total else {}
    return {
        "group_field": group_field,
        "area_shares": {key: 100 * value for key, value in sorted(shares.items())},
        "hhi_share_fraction": sum(value * value for value in shares.values()),
        "largest_group": max(shares, key=shares.get) if shares else None,
        "largest_group_share_percent": 100 * max(shares.values()) if shares else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--buildings", type=Path, required=True)
    parser.add_argument("--campuses", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    buildings = records(args.buildings)
    campuses = records(args.campuses)
    district: dict[str, dict[str, float | int]] = defaultdict(
        lambda: {"records": 0, "planned_gfa_sq_ft": 0.0, "remaining_gfa_sq_ft": 0.0}
    )
    for row in campuses:
        key = str(row.get("MagistDist") or "Unknown")
        district[key]["records"] += 1
        district[key]["planned_gfa_sq_ft"] += number(row, "PlannedGFA")
        district[key]["remaining_gfa_sq_ft"] += number(row, "RemainingGFA")

    output = {
        "format": "us-prince-william-data-center-gis-incidence-v1",
        "building_records": len(buildings),
        "campus_records": len(campuses),
        "building_gfa_sq_ft": sum(number(row, "GFA") for row in buildings),
        "campus_planned_gfa_sq_ft": sum(number(row, "PlannedGFA") for row in campuses),
        "campus_remaining_gfa_sq_ft": sum(number(row, "RemainingGFA") for row in campuses),
        "building_status": status_summary(buildings, "BuildingStatus", "GFA"),
        "campus_status": status_summary(campuses, "ProjectStatus", "PlannedGFA"),
        "campus_planning_district": dict(sorted(district.items())),
        "campus_planning_district_concentration": concentration(campuses, "MagistDist", "PlannedGFA"),
        "building_status_counts": dict(Counter(row.get("BuildingStatus") for row in buildings)),
        "campus_status_counts": dict(Counter(row.get("ProjectStatus") for row in campuses)),
        "boundary": "GFA is not electricity load; snapshot is not a time series or causal incidence estimate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
