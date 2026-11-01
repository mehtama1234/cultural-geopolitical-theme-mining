#!/usr/bin/env python3
"""Verify the pinned SHED emergency-expense series before uncertainty review."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
SOURCE = ANALYSIS / "shed-emergency-expense-2013-2025.json"
UNCERTAINTY = ANALYSIS / "shed-emergency-expense-uncertainty-audit.json"
REPRODUCTION = ANALYSIS / "shed-point-estimate-reproduction-audit.json"
OUTPUT = ANALYSIS / "shed-emergency-normalization-audit.json"


def main() -> int:
    source = json.loads(SOURCE.read_text())
    uncertainty = json.loads(UNCERTAINTY.read_text())
    reproduction = json.loads(REPRODUCTION.read_text())
    observations = source.get("observations", [])
    periods = [str(row.get("period")) for row in observations]
    values = [row.get("value") for row in observations]
    checks = {
        "schema_and_acquisition_id": source.get("schema") == "external-trend-intelligence.external-acquisition.v1" and source.get("acquisition_id") == "federal-reserve-shed-emergency-expense-2013-2025",
        "required_metadata": all(source.get(field) for field in ("publisher", "population", "geography", "measure", "unit", "denominator", "method")),
        "annual_periods_2013_2025": periods == [str(year) for year in range(2013, 2026)],
        "numeric_percent_values": all(isinstance(value, (int, float)) and 0 <= value <= 100 for value in values),
        "retrieval_hash_present": bool(source.get("retrieval", {}).get("artifact_sha256")),
        "latest_report_context_present": bool(source.get("latest_official_report_context", {}).get("final_report_sample_count")),
        "uncertainty_hold_preserved": uncertainty.get("release_decision") == "hold" and uncertainty.get("design_based_status") == "not_estimable_from_current_pinned_artifacts",
        "point_estimate_reproduction_linked": reproduction.get("status") == "point_estimate_reproduced_variance_open",
    }
    payload = {
        "schema": "external-trend-intelligence.shed-emergency-normalization-audit.v1",
        "source_artifact": SOURCE.name,
        "status": "normalized_metadata_verified_pending_design_based_uncertainty" if all(checks.values()) else "normalization_audit_failed",
        "observation_count": len(observations),
        "periods": periods,
        "value_range": [min(values), max(values)] if values else None,
        "checks": checks,
        "interpretation_boundary": "The audit verifies normalized chart rows and lineage custody. It does not supply design-based variance, prove question continuity, establish cross-source significance, or qualify a trend.",
        "next_action": "Acquire reproducible design-based variance or replicate-weight instructions and attach year-specific uncertainty before any cross-source significance or promotion.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({payload['status']}; {len(observations)} observations)")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
