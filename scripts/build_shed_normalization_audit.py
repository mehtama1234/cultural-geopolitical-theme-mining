#!/usr/bin/env python3
"""Verify the pinned SHED series is normalized without upgrading its interpretation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
SOURCE = ANALYSIS / "federal-reserve-shed-financial-room-2013-2025.json"
OUTPUT = ANALYSIS / "shed-normalization-audit.json"


def main() -> int:
    source = json.loads(SOURCE.read_text())
    observations = source.get("observations", [])
    periods = [str(row.get("period")) for row in observations]
    values = [row.get("value") for row in observations]
    checks = {
        "schema_and_acquisition_id": source.get("schema") == "external-trend-intelligence.external-acquisition.v1" and bool(source.get("acquisition_id")),
        "required_metadata": all(source.get(field) for field in ("publisher", "population", "geography", "measure", "unit", "denominator", "method")),
        "annual_periods_2013_2025": periods == [str(year) for year in range(2013, 2026)],
        "numeric_percent_values": all(isinstance(value, (int, float)) and 0 <= value <= 100 for value in values),
        "retrieval_hash_present": bool(source.get("retrieval", {}).get("artifact_sha256")),
        "comparability_boundary_present": bool(source.get("comparability_review", {}).get("not_comparable_without_review")),
        "rights_boundary_present": bool(source.get("rights_boundary")),
    }
    payload = {
        "schema": "external-trend-intelligence.shed-normalization-audit.v1",
        "source_artifact": SOURCE.name,
        "status": "normalized_metadata_verified_pending_rights_and_comparability_review" if all(checks.values()) else "normalization_audit_failed",
        "observation_count": len(observations),
        "periods": periods,
        "value_range": [min(values), max(values)] if values else None,
        "checks": checks,
        "interpretation_boundary": "The audit verifies normalized chart-data rows, metadata, and custody fields. It does not prove question continuity, uncertainty comparability, redistribution permission, causal effect, or a cross-source financial-room trend.",
        "next_action": "Review the 2025 codebook, exact chart/data terms, and a closer emergency-expense or bill-payment measure before pooling or promotion.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({payload['status']}; {len(observations)} observations)")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
