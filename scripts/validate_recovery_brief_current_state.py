#!/usr/bin/env python3
"""Ensure the crash-recovery brief reflects the canonical ledger portfolio."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF = ROOT / "END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md"
SUMMARY = ROOT / "analysis/data/us-broad-event-ledger-portfolio-summary-v1.json"


def main() -> int:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    totals = summary["totals"]
    open_arrows = summary["arrow_status"].get("open", 0)
    text = BRIEF.read_text(encoding="utf-8")
    pattern = re.compile(
        r"event-ledger portfolio contains\s+\*\*(\d+) ledgers, (\d+) events, and (\d+) typed arrows,\s+including (\d+) explicitly open arrows\*\*",
        re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        raise ValueError("recovery brief does not contain the canonical portfolio count line")
    brief_totals = tuple(int(value) for value in match.groups())
    expected = (totals["ledgers"], totals["events"], totals["arrows"], open_arrows)
    if brief_totals != expected:
        raise ValueError(f"recovery brief counts stale: {brief_totals} != {expected}")
    print(
        "VALID recovery brief current state: "
        f"{expected[0]} ledgers, {expected[1]} events, {expected[2]} arrows, "
        f"{expected[3]} open arrows"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
