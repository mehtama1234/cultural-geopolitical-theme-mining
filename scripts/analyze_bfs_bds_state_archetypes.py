#!/usr/bin/env python3
"""Create robust state archetypes from BFS applications and BDS dynamics."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path

from analyze_bfs_bds_state_stage_comparison import FIPS_TO_STATE


def quartile(values: list[float], value: float) -> int:
    ordered = sorted(values)
    if value <= ordered[len(ordered) // 4]:
        return 1
    if value <= ordered[len(ordered) // 2]:
        return 2
    if value <= ordered[(3 * len(ordered)) // 4]:
        return 3
    return 4


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bfs", type=Path, required=True)
    parser.add_argument("--bds", type=Path, required=True)
    parser.add_argument("--year", type=int, default=2023)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    applications: dict[str, int] = {}
    with args.bfs.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if int(row["Year"]) == args.year:
                state = row["State"]
                applications[state] = applications.get(state, 0) + int(row["BA_NSA"])

    dynamics: dict[str, dict[str, str]] = {}
    with args.bds.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if int(row["year"]) == args.year and row["st"] in FIPS_TO_STATE:
                dynamics[FIPS_TO_STATE[row["st"]]] = row

    states = sorted(set(applications) & set(dynamics))
    rows = []
    for state in states:
        bds = dynamics[state]
        establishments = float(bds["estabs"])
        normalized = 100 * applications[state] / establishments if establishments else None
        rows.append({
            "state": state,
            "applications": applications[state],
            "establishments": round(establishments),
            "applications_per_100_establishments": round(normalized, 3) if normalized is not None else None,
            "entry_rate": float(bds["estabs_entry_rate"]),
            "exit_rate": float(bds["estabs_exit_rate"]),
            "net_job_creation_rate": float(bds["net_job_creation_rate"]),
        })

    app_values = [row["applications_per_100_establishments"] for row in rows]
    entry_values = [row["entry_rate"] for row in rows]
    exit_values = [row["exit_rate"] for row in rows]
    net_values = [row["net_job_creation_rate"] for row in rows]
    for row in rows:
        row["application_quartile"] = quartile(app_values, row["applications_per_100_establishments"])
        row["entry_quartile"] = quartile(entry_values, row["entry_rate"])
        row["exit_quartile"] = quartile(exit_values, row["exit_rate"])
        row["net_job_quartile"] = quartile(net_values, row["net_job_creation_rate"])

    groups = {}
    for app_q in range(1, 5):
        group = [row for row in rows if row["application_quartile"] == app_q]
        groups[str(app_q)] = {
            "states": len(group),
            "median_entry_rate": round(statistics.median(r["entry_rate"] for r in group), 3),
            "median_exit_rate": round(statistics.median(r["exit_rate"] for r in group), 3),
            "median_net_job_creation_rate": round(statistics.median(r["net_job_creation_rate"] for r in group), 3),
            "median_applications_per_100_establishments": round(statistics.median(r["applications_per_100_establishments"] for r in group), 3),
        }

    result = {
        "format": "us-bfs-bds-state-archetypes-v1",
        "source_unit": "matched state/DC, annual BFS application flow and BDS state dynamics",
        "year": args.year,
        "matched_states": len(rows),
        "groups_by_application_quartile": groups,
        "states": rows,
        "quality_note": "Wyoming is retained for transparency but its unusually high normalized application value is quality-sensitive in the existing BFS audit.",
        "causal_estimation": False,
        "boundary": "State archetypes compare separate BFS and BDS constructions; they do not match firms, establish conversion, or measure local service, worker, or political outcomes.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"matched_states": len(rows), "application_quartiles": len(groups)}, indent=2))


if __name__ == "__main__":
    main()
