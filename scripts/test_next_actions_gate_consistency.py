#!/usr/bin/env python3
"""Keep the human handoff aligned with the live open-gate register."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def main() -> int:
    register = json.loads((ANALYSIS / "open-gate-register.json").read_text())
    document = (ANALYSIS / "NEXT-ACTIONS.md").read_text()
    gate_count = register["gate_count"]
    assert gate_count == len(register["gates"]) > 0
    assert f"live release has {gate_count} open gates" in document
    assert "One substantive open gate" not in document
    assert "No internal company data may be joined" in document
    for filename in (
        "rights-assignment-queue.json",
        "ownership-assignment-queue.json",
        "candidate-independence-adjudication-queue.json",
        "pilot-activation-queue.json",
        "continuity-review-packet.json",
    ):
        assert (ANALYSIS / filename).exists(), filename
        assert filename in document, filename
    print("next-actions gate consistency: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
