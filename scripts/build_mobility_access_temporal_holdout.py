#!/usr/bin/env python3
"""Build a bounded ACS national temporal holdout for mobility exposure."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "mobility-access-temporal-holdout.json"


def main() -> int:
    measures = [
        {"measure": "zero_vehicle_households", "unit": "percent of households", "construction": {"period": 2023, "value": 8.44}, "holdout": {"period": 2024, "value": 8.52}, "change_percentage_points": 0.08},
        {"measure": "commute_30_minutes_or_more", "unit": "percent of workers not working from home", "construction": {"period": 2023, "value": 37.97}, "holdout": {"period": 2024, "value": 38.69}, "change_percentage_points": 0.72},
    ]
    report = {
        "schema": "external-trend-intelligence.mobility-access-temporal-holdout.v1",
        "candidate_id": "candidate-time-financial-pressure-practical-room",
        "status": "descriptive_single_family_holdout",
        "source_family": "U.S. Census Bureau ACS 1-year national table-based summary files",
        "source_urls": ["https://www2.census.gov/programs-surveys/acs/summary_file/2023/table-based-SF/data/1YRData/acsdt1y2023-b08201.dat", "https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/1YRData/acsdt1y2024-b08201.dat"],
        "measures": measures,
        "uncertainty": "ACS sampling and nonsampling error apply; the pinned source record does not calculate margin-of-error propagation for this first national layer.",
        "counter_signal": "The small national movement can conceal larger state, income, race, disability, and urban/rural differences; vehicle availability and commute duration are not affordability or unmet access.",
        "falsifier": "A later compatible ACS release that reverses the direction under a stable table definition would weaken this descriptive readout.",
        "does_not_support": ["causality", "NHTS replication", "pooled independent estimate", "transport affordability", "company exposure"],
        "next_action": "Acquire ACS margins of error and a repeated income/geography slice, then compare the holdout with a compatible NHTS or other independent travel measure without pooling unlike frames.",
        "boundary": "This is a descriptive repeated-table holdout from one ACS family. It is not an independent validation or company finding.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(measures)} measures; uncertainty propagation pending)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
