#!/usr/bin/env python3
"""Validate design-only pilot contracts without accessing company data."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "pilot-design-dry-run.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    register = load("pilot-register.json")
    evaluation = load("pilot-bridge-evaluation.json")
    assert evaluation["schema"] == "external-trend-intelligence.pilot-bridge-evaluation.v1"
    assert evaluation["synthetic_only"] is True
    assert evaluation["company_data_accessed"] is False
    assert evaluation["boundary"] and evaluation["stop_rule"]
    checks = []
    for pilot in register["pilots"]:
        contract = pilot["internal_data_contract"]
        passed = all(
            [
                bool(pilot.get("decision_question")),
                bool(pilot.get("hypothesis")),
                bool(pilot.get("falsifier")),
                bool(pilot.get("external_gate", {}).get("current_blockers")),
                pilot.get("status") == "design_only_external_gate",
                contract.get("dataset") is None,
                pilot.get("privacy_and_rights", {}).get("privacy_class") == "Not assessed",
            ]
        )
        checks.append({"pilot_id": pilot["pilot_id"], "status": "pass" if passed else "fail", "company_data_accessed": False})
    status = "pass" if all(item["status"] == "pass" for item in checks) else "fail"
    payload = {
        "schema": "external-trend-intelligence.pilot-design-dry-run.v1",
        "status": status,
        "pilot_count": len(checks),
        "checks": checks,
        "company_data_accessed": False,
        "approved_test_count": 0,
        "boundary": "This dry run validates pilot design contracts only. It does not approve a pilot, connect internal data, establish causality, or clear rights/privacy review.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"pilot design dry run: {status}")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
