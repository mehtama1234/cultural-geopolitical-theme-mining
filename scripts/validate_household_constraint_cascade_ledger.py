#!/usr/bin/env python3
"""Validate the household constraint-cascade ledger contract.

This checks structure, timing metadata, evidence-status separation, and
simulation disclosure. It does not certify privacy, linkage, causality, or
remedy.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "manifests/us-household-constraint-cascade-ledger-v1.json").read_text())


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(path: Path) -> tuple[int, int, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != SCHEMA["format"]:
        raise ValueError("ledger schema does not match the household cascade contract")
    evidence_class = data.get("evidence_class", "")
    allowed_statuses = {"simulated_test_data"} if evidence_class == "simulated_test_data" else set(SCHEMA["evidence_status"]) - {"simulated_test_data"}
    required = set(SCHEMA["required_event_fields"])
    stages = set(SCHEMA["stage_fields"])
    units = set(SCHEMA["controlled_values"]["unit"])
    statuses = set(SCHEMA["controlled_values"]["evidence_status"])
    stage_statuses = set(SCHEMA["controlled_values"]["stage_status"])
    events = data.get("events")
    if not isinstance(events, list) or not events:
        raise ValueError("events must be a non-empty list")
    event_ids: set[str] = set()
    for event in events:
        if not isinstance(event, dict):
            raise ValueError("each event must be an object")
        missing = sorted(required - set(event))
        if missing:
            raise ValueError(f"event missing fields: {missing}")
        episode_id = event["episode_id"]
        if not nonempty(episode_id) or episode_id in event_ids:
            raise ValueError(f"episode id missing or duplicated: {episode_id!r}")
        event_ids.add(episode_id)
        if event["unit"] not in units:
            raise ValueError(f"invalid unit for {episode_id}")
        if event["evidence_status"] not in statuses or event["evidence_status"] not in allowed_statuses:
            raise ValueError(f"invalid evidence status for {episode_id}")
        for field in ("geography", "denominator", "date_precision", "missingness", "counterexample", "source_and_uncertainty"):
            if not nonempty(event[field]):
                raise ValueError(f"empty required metadata {field} for {episode_id}")
        try:
            date.fromisoformat(event["event_date"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"event_date must be an ISO date for {episode_id}") from exc
        if set(event["stages"]) != stages:
            raise ValueError(f"stage keys do not match contract for {episode_id}")
        for stage_name, stage in event["stages"].items():
            if not isinstance(stage, dict) or not nonempty(stage.get("status")) or stage["status"] not in stage_statuses:
                raise ValueError(f"invalid stage status for {episode_id}/{stage_name}")
            if not nonempty(stage.get("observation")) or not nonempty(stage.get("source")):
                raise ValueError(f"stage requires observation and source for {episode_id}/{stage_name}")
    arrows = data.get("arrows")
    if not isinstance(arrows, list) or not arrows:
        raise ValueError("arrows must be a non-empty list")
    arrow_ids: set[str] = set()
    for arrow in arrows:
        missing = set(SCHEMA["required_arrow_fields"]) - set(arrow)
        if missing:
            raise ValueError(f"arrow missing fields: {sorted(missing)}")
        if not nonempty(arrow["arrow_id"]) or arrow["arrow_id"] in arrow_ids:
            raise ValueError(f"arrow id missing or duplicated: {arrow.get('arrow_id')!r}")
        arrow_ids.add(arrow["arrow_id"])
        if not isinstance(arrow["unit_held_constant"], bool) or not isinstance(arrow["time_order_valid"], bool):
            raise ValueError(f"arrow controls must be boolean for {arrow['arrow_id']}")
        if arrow["status"] not in statuses or arrow["status"] not in allowed_statuses:
            raise ValueError(f"invalid arrow status for {arrow['arrow_id']}")
        for field in ("from", "to", "evidence", "remaining_gap"):
            if not nonempty(arrow[field]):
                raise ValueError(f"empty arrow field {field} for {arrow['arrow_id']}")
    return len(events), len(arrows), evidence_class or "unspecified"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    events, arrows, evidence_class = validate(args.ledger)
    print(f"VALID household cascade ledger: {events} event(s), {arrows} arrow(s), class={evidence_class}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
