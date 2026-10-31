#!/usr/bin/env python3
"""Verify that unresolved rights/dependence keeps the release on hold."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    controls = load("source-family-controls.json")
    evidence = load("rights-evidence-register.json")
    health = load("release-health.json")
    control_ids = {row["family_id"] for row in controls["families"]}
    evidence_ids = {row["family_id"] for row in evidence["rows"]}
    assert control_ids == evidence_ids
    assert all(row["rights_status"] != "verified" for row in controls["families"])
    assert all(row["publisher_dependence"] == "review_required" for row in controls["families"])
    rights = health["sections"]["rights_and_publisher_dependence"]
    assert rights["status"] == "hold"
    assert "rights and publisher-dependence review remains open for source families" in health["blockers"]
    print("rights release gate: unresolved rights and dependence correctly hold release")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
