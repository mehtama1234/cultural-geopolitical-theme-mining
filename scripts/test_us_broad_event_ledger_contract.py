#!/usr/bin/env python3
"""Regression checks for required end-to-end event-ledger stages."""

from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from validate_us_broad_event_ledger import validate


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "analysis/samples/US-BROAD-EVENT-LEDGER-SIMULATED_V1.json"


def main() -> int:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="broad-event-contract-") as directory:
        valid_path = Path(directory) / "valid.json"
        valid_path.write_text(json.dumps(data), encoding="utf-8")
        events, arrows, evidence_class = validate(valid_path)
        assert (events, arrows, evidence_class) == (1, 1, "simulated_test_data")

        invalid = copy.deepcopy(data)
        invalid["events"][0]["alternatives_before_action"] = ""
        invalid_path = Path(directory) / "invalid.json"
        invalid_path.write_text(json.dumps(invalid), encoding="utf-8")
        try:
            validate(invalid_path)
        except ValueError as error:
            assert "alternatives_before_action" in str(error), error
        else:
            raise AssertionError("blank required event stage was accepted")

    print("PASS broad event-ledger contract regression: unknown accepted, blank stage rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
