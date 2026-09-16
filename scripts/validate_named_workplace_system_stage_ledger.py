#!/usr/bin/env python3
"""Validate the local named workplace AI stage ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {
    "event_id",
    "system_and_owner",
    "dated_implementation_or_rule",
    "worker_exposure",
    "worker_voice",
    "specific_control_or_rule_change",
    "enforcement_or_appeal",
    "worker_outcome",
    "household_outcome",
    "exit_or_collective_action",
    "source",
    "boundary",
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ledger",
        type=Path,
        default=root / "analysis/projects/ai-work-control/data/named-workplace-system-stage-ledger-v1.json",
    )
    args = parser.parse_args()
    data = json.loads(args.ledger.read_text(encoding="utf-8"))
    if data.get("status") != "bounded_stage_comparison":
        raise ValueError("ledger must remain a bounded stage comparison")
    records = data.get("records", [])
    if len(records) < 2:
        raise ValueError("ledger requires at least two named systems")
    for record in records:
        missing = REQUIRED - set(record)
        if missing:
            raise ValueError(f"{record.get('event_id')} missing {sorted(missing)}")
        source = root / record["source"]
        if not source.exists():
            raise FileNotFoundError(source)
    print(f"VALID named workplace system stage ledger: {len(records)} local records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
