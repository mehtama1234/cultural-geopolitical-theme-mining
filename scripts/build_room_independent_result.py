#!/usr/bin/env python3
"""Summarize directional agreement across ABS GSS and HILDA household measures."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "room-independent-result.json"


def main() -> int:
    comparison = json.loads((ANALYSIS / "room-independent-comparison.json").read_text())
    abs_measures = comparison["records"][0]["measures"]
    hilda = comparison["records"][1]["measures"]
    rows = [
        {"source": "ABS GSS", "measure": "cash_flow_problem", "from_period": "2020", "to_period": "2025", "from_value": abs_measures["cash_flow_problem_2020"]["value"], "to_value": abs_measures["cash_flow_problem_2025"]["value"]},
        {"source": "ABS GSS", "measure": "dissaving", "from_period": "2020", "to_period": "2025", "from_value": abs_measures["dissaving_2020"]["value"], "to_value": abs_measures["dissaving_2025"]["value"]},
        {"source": "HILDA via AIHW", "measure": "cash_flow_problem", "from_period": "2020", "to_period": "2023", "from_value": hilda["cash_flow_problem_2020"]["value"], "to_value": hilda["cash_flow_problem_2023"]["value"]},
        {"source": "HILDA via AIHW", "measure": "unable_to_raise_2000", "from_period": "2020", "to_period": "2023", "from_value": hilda["unable_to_raise_2000_2020"]["value"], "to_value": hilda["unable_to_raise_2000_2023"]["value"]},
    ]
    for row in rows:
        row["change"] = row["to_value"] - row["from_value"]
        row["direction"] = "increase" if row["change"] > 0 else "decrease" if row["change"] < 0 else "flat"
    report = {
        "schema": "external-trend-intelligence.room-independent-result.v1",
        "candidate_id": comparison["candidate_id"],
        "status": "directional_cross_source_agreement_only",
        "rows": rows,
        "directional_summary": "ABS GSS and HILDA both show increases in household financial-pressure measures across their available periods.",
        "counter_signal": "ABS GSS also shows increased weekly outside-household contact; financial pressure and social reconnection should remain separate signals.",
        "does_not_support": ["common-period effect estimate", "pooled prevalence", "causality", "qualified trend", "company exposure"],
        "blocking_items": ["HILDA ends in 2023 while ABS reaches 2025", "measure definitions and source methods differ", "no common independent 2025 endpoint"],
        "next_action": "Acquire or refresh an independent household-finance measure through 2025 and reconcile definitions before a formal backtest.",
        "boundary": "Directional agreement across independent sources is a stronger mechanism check, not proof of a single population trend.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
