#!/usr/bin/env python3
"""Regression checks for the household-cascade promotion gate."""

from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from validate_household_constraint_cascade_promotion import audit


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "analysis/projects/us-household-constraint-cascade/data/household-constraint-cascade-ledger-fixture-v1.json"


def write_and_audit(payload: dict[str, object]) -> dict[str, object]:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8") as handle:
        json.dump(payload, handle)
        handle.flush()
        return audit(Path(handle.name))


def main() -> int:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    rejected = audit(FIXTURE)
    assert rejected["eligible"] is False
    assert any("remedy_verification" in failure for failure in rejected["failures"])
    assert any("time_order_valid" in failure for failure in rejected["failures"])

    eligible = copy.deepcopy(fixture)
    eligible["evidence_class"] = "reported"
    for event in eligible["events"]:
        event["evidence_status"] = "reported"
        for stage in event["stages"].values():
            stage["status"] = "reported"
    for arrow in eligible["arrows"]:
        arrow["status"] = "reported"
        arrow["time_order_valid"] = True
    accepted = write_and_audit(eligible)
    assert accepted["eligible"] is True, accepted["failures"]
    print("PASS household cascade promotion guard: rejects open fixture and accepts complete synthetic ledger")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
