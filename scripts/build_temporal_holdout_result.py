#!/usr/bin/env python3
"""Compute a descriptive directional readout from the registered ABS holdout."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "temporal-holdout-result.json"


def main() -> int:
    design = json.loads((ANALYSIS / "temporal-holdout-design.json").read_text())
    rows = []
    for item in design["measures"]:
        delta = item["holdout_value"] - item["construction_value"]
        rows.append({
            "measure": item["measure"],
            "construction_value": item["construction_value"],
            "holdout_value": item["holdout_value"],
            "change": delta,
            "direction": "increase" if delta > 0 else "decrease" if delta < 0 else "flat",
            "interpretation": (
                "supports greater reported financial pressure" if item["measure"] in {"cash_flow_problem", "dissaving"} and delta > 0
                else "counter-signal: social contact increased alongside financial pressure" if item["measure"] == "outside_household_weekly_contact" and delta > 0
                else "does not support the expected direction"
            ),
        })
    report = {
        "schema": "external-trend-intelligence.temporal-holdout-result.v1",
        "design": "temporal-holdout-design.json",
        "candidate_id": design["candidate_id"],
        "status": "descriptive_holdout_readout_single_family",
        "result": rows,
        "signal_summary": "Two financial-room measures increased from 2020 to 2025, while weekly outside-household contact also increased.",
        "supports": ["directional mechanism check", "counter-signal preservation", "decision narrative on pressure versus social reconnection"],
        "does_not_support": ["causality", "individual change", "independent corroboration", "qualified trend", "company exposure"],
        "falsifier_for_candidate": "If later compatible waves show financial-room measures stable or falling while the same population frame is maintained, the pressure direction should be reversed or retired.",
        "next_action": "Repeat with the next ABS GSS cycle and compare against an independent household-finance source using a pre-specified compatible measure.",
        "boundary": "This is a descriptive repeated-cross-section readout; the social-contact increase is retained as a counter-signal rather than treated as failure or ignored.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} measures)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
