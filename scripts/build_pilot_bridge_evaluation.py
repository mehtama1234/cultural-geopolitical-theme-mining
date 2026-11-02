#!/usr/bin/env python3
"""Evaluate synthetic pilot cells without presenting them as company evidence."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "pilot-bridge-evaluation.json"


def main() -> int:
    simulation = json.loads((ANALYSIS / "pilot-bridge-simulation.json").read_text())
    matched = simulation["matched_cells"]
    high = [row for row in matched if row["external_context_rate"] >= 0.15]
    low = [row for row in matched if row["external_context_rate"] < 0.15]
    high_rate = sum(row["workflow_completion_rate"] for row in high) / len(high) if high else None
    low_rate = sum(row["workflow_completion_rate"] for row in low) / len(low) if low else None
    payload = {
        "schema": "external-trend-intelligence.pilot-bridge-evaluation.v1",
        "status": "synthetic_descriptive_readout_only",
        "pilot_id": simulation["pilot_id"],
        "synthetic_only": True,
        "company_data_accessed": False,
        "grouping_rule": "illustrative split at external_context_rate >= 0.15; not a preregistered company analysis",
        "matched_cell_count": len(matched),
        "unmatched_external_cell_count": len(simulation["unmatched_external_cells"]),
        "missing_outcome_cell_count": len(simulation["missing_outcome_cells"]),
        "high_context_completion_rate": round(high_rate, 4) if high_rate is not None else None,
        "low_context_completion_rate": round(low_rate, 4) if low_rate is not None else None,
        "descriptive_completion_difference": round(high_rate - low_rate, 4) if high_rate is not None and low_rate is not None else None,
        "interpretation": "Synthetic cells exercise the arithmetic and visibility contract only; they do not estimate a company effect or validate the external trend.",
        "required_visibility_checks": simulation["required_visibility_checks"],
        "falsifier": simulation["falsifier"],
        "stop_rule": simulation["stop_rule"],
        "boundary": "No company result, causal estimate, approval, or internal exposure is created by this evaluation.",
        "next_action": "Replace synthetic cells only after external monitoring, rights, privacy, decision-owner, and preregistration gates pass.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} (synthetic cells evaluated; company data accessed: {payload['company_data_accessed']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
