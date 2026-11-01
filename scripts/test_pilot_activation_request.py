#!/usr/bin/env python3
"""Verify the human pilot activation request stays fail-closed and complete."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def main() -> int:
    request = (ANALYSIS / "PILOT-ACTIVATION-REQUEST.md").read_text()
    intake = json.loads((ANALYSIS / "pilot-contract-intake.json").read_text())
    queue = json.loads((ANALYSIS / "pilot-activation-queue.json").read_text())
    matrix = json.loads((ANALYSIS / "candidate-qualification-matrix.json").read_text())

    recommended = "pilot-food-security-service-room-001"
    row = next(item for item in intake["pilots"] if item["pilot_id"] == recommended)
    candidate = next(item for item in matrix["rows"] if item["candidate_id"] == row["candidate_id"])
    assert candidate["gate_status"] == "monitored_external_trend"
    assert any(item["pilot_id"] == recommended and not item["company_data_accessed"] for item in queue["rows"])
    field_labels = {
        "company_id": "Company and business unit",
        "business_unit": "Company and business unit",
        "decision_owner": "Decision owner and decision deadline",
        "internal_dataset": "Internal dataset and snapshot/query",
        "period": "Geography and period",
        "primary_outcome": "Primary outcome and denominator",
        "unit": "Comparison group and unit",
        "denominator": "Primary outcome and denominator",
        "privacy_class": "Privacy class and lawful-access basis",
        "lawful_access_basis": "Privacy class and lawful-access basis",
        "analysis_owner": "Analysis owner",
        "stop_rule": "Falsifier and stop rule",
    }
    for field in intake["required_fields"]:
        assert field_labels[field] in request, field
    request_lower = request.casefold()
    for phrase in [
        "source-specific rights owner",
        "privacy, lawful access",
        "falsifier",
        "stop rule",
        "company_data_accessed=false",
        "approved_test_count=0",
        "design_only_external_gate",
    ]:
        assert phrase.casefold() in request_lower, phrase
    print("pilot activation request: fail-closed contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
