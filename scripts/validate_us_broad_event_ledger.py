#!/usr/bin/env python3
"""Validate a broad event ledger against the research-design contract.

The validator checks structure and disclosure controls only. It does not infer
causality, certify a linkage, or turn a simulated fixture into evidence.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "manifests/us-broad-event-ledger-schema-v1.json").read_text())


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(path: Path) -> tuple[int, int, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != SCHEMA["format"]:
        raise ValueError("ledger schema does not match the broad event-ledger contract")
    evidence_class = data.get("evidence_class", "")
    if evidence_class == "simulated_test_data":
        allowed_statuses = {"simulated_test_data"}
    else:
        allowed_statuses = set(SCHEMA["evidence_status"]) - {"simulated_test_data"}

    required = set(SCHEMA["required_event_fields"])
    units = set(SCHEMA["valid_units"])
    statuses = set(SCHEMA["evidence_status"])
    actors = set(SCHEMA["controlled_values"]["actor_initiating_change"])
    conditions = set(SCHEMA["controlled_values"]["condition_or_decision"])
    event_ids: set[str] = set()
    events = data.get("events", [])
    if not isinstance(events, list):
        raise ValueError("events must be a list")
    for event in events:
        if not isinstance(event, dict):
            raise ValueError("each event must be an object")
        missing = sorted(required - set(event))
        if missing:
            raise ValueError(f"event missing fields: {missing}")
        event_id = event["event_id"]
        if not nonempty(event_id) or event_id in event_ids:
            raise ValueError(f"event id missing or duplicated: {event_id!r}")
        event_ids.add(event_id)
        if event["unit"] not in units:
            raise ValueError(f"invalid unit for {event_id}")
        if event["actor_initiating_change"] not in actors:
            raise ValueError(f"invalid initiating actor for {event_id}")
        if event["condition_or_decision"] not in conditions:
            raise ValueError(f"invalid condition for {event_id}")
        if event["evidence_status"] not in statuses or event["evidence_status"] not in allowed_statuses:
            raise ValueError(f"invalid evidence status for {event_id}")
        for field in ("geography", "date_precision", "denominator", "method",
                      "missingness", "counterexample", "source_and_uncertainty"):
            if not nonempty(event[field]):
                raise ValueError(f"empty required metadata {field} for {event_id}")
        try:
            date.fromisoformat(event["event_date"])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid ISO event_date for {event_id}") from exc
        if evidence_class != "simulated_test_data" and "fictional" in event["source_and_uncertainty"].lower():
            raise ValueError(f"real ledger cannot label source as fictional: {event_id}")

    arrow_fields = set(SCHEMA["arrow_fields"])
    arrows = data.get("arrows", [])
    if not isinstance(arrows, list):
        raise ValueError("arrows must be a list")
    arrow_ids: set[str] = set()
    for arrow in arrows:
        if not isinstance(arrow, dict):
            raise ValueError("each arrow must be an object")
        missing = sorted(arrow_fields - set(arrow))
        if missing:
            raise ValueError(f"arrow missing fields: {missing}")
        arrow_id = arrow["arrow_id"]
        if not nonempty(arrow_id) or arrow_id in arrow_ids:
            raise ValueError(f"arrow id missing or duplicated: {arrow_id!r}")
        arrow_ids.add(arrow_id)
        if arrow["status"] not in statuses or arrow["status"] not in allowed_statuses:
            raise ValueError(f"invalid arrow status for {arrow_id}")
        if not isinstance(arrow["unit_held_constant"], bool) or not isinstance(arrow["time_order_valid"], bool):
            raise ValueError(f"arrow controls must be boolean for {arrow_id}")
        for field in ("from", "to", "evidence", "counterexample", "remaining_gap"):
            if not nonempty(arrow[field]):
                raise ValueError(f"empty arrow field {field} for {arrow_id}")

    return len(events), len(arrows), evidence_class or "unspecified"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="JSON ledger to validate")
    args = parser.parse_args()
    events, arrows, evidence_class = validate(args.ledger)
    print(f"VALID broad event ledger: {events} event(s), {arrows} arrow(s), class={evidence_class}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
