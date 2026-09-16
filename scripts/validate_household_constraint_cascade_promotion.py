#!/usr/bin/env python3
"""Audit whether a household-cascade ledger is eligible for end-to-end promotion.

The structural ledger validator accepts explicit unknown stages for research
tracking. This stricter audit is a promotion gate: every required stage and
arrow control must be supported before a result can be described as a closed
same-case chain. It does not establish causality.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads(
    (ROOT / "manifests/us-household-constraint-cascade-ledger-v1.json").read_text()
)
OPEN_STATUSES = {"unknown", "open", "simulated_test_data"}
REQUIRED_STAGES = tuple(SCHEMA["stage_fields"])
EVIDENCE_STATUSES = set(SCHEMA["evidence_status"])
STAGE_STATUSES = set(SCHEMA["controlled_values"]["stage_status"])
UNITS = set(SCHEMA["controlled_values"]["unit"])


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def audit(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    events = data.get("events")
    arrows = data.get("arrows")
    failures: list[str] = []

    if data.get("schema") != SCHEMA["format"]:
        failures.append("schema does not match the household cascade contract")
    evidence_class = data.get("evidence_class")
    if evidence_class not in EVIDENCE_STATUSES:
        failures.append(f"invalid or missing evidence class: {evidence_class!r}")
    elif evidence_class == "simulated_test_data":
        failures.append("ledger is explicitly simulated test data")
    if not isinstance(events, list) or not events:
        failures.append("events must be a non-empty list")
        events = []
    if not isinstance(arrows, list) or not arrows:
        failures.append("arrows must be a non-empty list")
        arrows = []

    event_ids: set[str] = set()
    for index, event in enumerate(events):
        label = event.get("episode_id", f"event[{index}]") if isinstance(event, dict) else f"event[{index}]"
        if not isinstance(event, dict):
            failures.append(f"{label}: event is not an object")
            continue
        episode_id = event.get("episode_id")
        if not nonempty(episode_id) or episode_id in event_ids:
            failures.append(f"{label}: episode_id missing or duplicated")
        else:
            event_ids.add(episode_id)
        if event.get("unit") not in UNITS:
            failures.append(f"{label}: invalid unit")
        if event.get("evidence_status") not in EVIDENCE_STATUSES or event.get("evidence_status") == "simulated_test_data":
            failures.append(f"{label}: invalid or simulated evidence status")
        try:
            date.fromisoformat(event["event_date"])
        except (KeyError, TypeError, ValueError):
            failures.append(f"{label}: event_date is not an ISO date")
        for field in ("denominator", "missingness", "counterexample", "source_and_uncertainty"):
            if not nonempty(event.get(field)):
                failures.append(f"{label}: {field} is empty")
        stages = event.get("stages")
        if not isinstance(stages, dict) or set(stages) != set(REQUIRED_STAGES):
            failures.append(f"{label}: stage keys do not match the contract")
            continue
        for stage_name in REQUIRED_STAGES:
            stage = stages[stage_name]
            if not isinstance(stage, dict):
                failures.append(f"{label}/{stage_name}: stage is not an object")
                continue
            status = stage.get("status")
            if status not in STAGE_STATUSES:
                failures.append(f"{label}/{stage_name}: invalid stage status {status!r}")
            elif status in OPEN_STATUSES:
                failures.append(f"{label}/{stage_name}: stage remains {status or 'missing'}")
            if not nonempty(stage.get("observation")) or not nonempty(stage.get("source")):
                failures.append(f"{label}/{stage_name}: observation and source are required")

    for index, arrow in enumerate(arrows):
        label = arrow.get("arrow_id", f"arrow[{index}]") if isinstance(arrow, dict) else f"arrow[{index}]"
        if not isinstance(arrow, dict):
            failures.append(f"{label}: arrow is not an object")
            continue
        if arrow.get("unit_held_constant") is not True:
            failures.append(f"{label}: unit_held_constant must be true")
        if arrow.get("time_order_valid") is not True:
            failures.append(f"{label}: time_order_valid must be true")
        for field in ("from", "to", "evidence", "remaining_gap"):
            if not nonempty(arrow.get(field)):
                failures.append(f"{label}: {field} is empty")
        if arrow.get("status") not in EVIDENCE_STATUSES:
            failures.append(f"{label}: invalid arrow status {arrow.get('status')!r}")
        elif arrow.get("status") in OPEN_STATUSES:
            failures.append(f"{label}: arrow remains {arrow['status']}")

    return {
        "eligible": not failures,
        "event_count": len(events),
        "arrow_count": len(arrows),
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    result = audit(args.ledger)
    if args.as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
    elif result["eligible"]:
        print(f"ELIGIBLE household cascade promotion: {result['event_count']} event(s), {result['arrow_count']} arrow(s)")
    else:
        print(f"NOT ELIGIBLE household cascade promotion: {len(result['failures'])} gate failure(s)")
        for failure in result["failures"]:
            print(f"- {failure}")
    return 0 if result["eligible"] else 1


if __name__ == "__main__":
    sys.exit(main())
