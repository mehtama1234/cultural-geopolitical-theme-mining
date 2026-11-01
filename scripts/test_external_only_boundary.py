#!/usr/bin/env python3
"""Fail closed if an external release contains a connected company pilot."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    pilots = load("pilot-register.json")
    readiness = load("pilot-readiness.json")
    manifest = load("release-manifest.json")
    assert readiness["ready_for_approved_test_count"] == 0
    assert all(item["status"] != "approved_test" for item in pilots["pilots"])
    for item in pilots["pilots"]:
        assert item["company_ref"].get("company_id") is None
        assert item["company_ref"].get("business_unit") is None
        assert item["company_ref"].get("decision_owner") is None
        contract = item["internal_data_contract"]
        assert contract.get("dataset") is None
        assert contract.get("snapshot_or_query") is None
        assert contract.get("entity_key") is None
    forbidden = ("raw/internal", "company-data/", "customer-level/")
    assert not any(any(token in artifact["path"] for token in forbidden) for artifact in manifest["artifacts"])
    print("external-only boundary: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
