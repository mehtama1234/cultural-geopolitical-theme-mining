"""Validate the simulated broad event-ledger fixture without treating it as evidence."""

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "manifests/us-broad-event-ledger-schema-v1.json").read_text())
FIXTURE = ROOT / "analysis/samples/US-BROAD-EVENT-LEDGER-SIMULATED_V1.json"


def main() -> int:
    data = json.loads(FIXTURE.read_text())
    if data.get("evidence_class") != "simulated_test_data":
        raise ValueError("fixture must be marked simulated_test_data")
    if data.get("schema") != SCHEMA["format"]:
        raise ValueError("fixture schema does not match")

    required = set(SCHEMA["required_event_fields"])
    units = set(SCHEMA["valid_units"])
    statuses = set(SCHEMA["evidence_status"])
    actors = set(SCHEMA["controlled_values"]["actor_initiating_change"])
    conditions = set(SCHEMA["controlled_values"]["condition_or_decision"])
    for event in data.get("events", []):
        missing = sorted(required - set(event))
        if missing:
            raise ValueError(f"missing event fields: {missing}")
        if event["unit"] not in units:
            raise ValueError("invalid unit")
        if event["actor_initiating_change"] not in actors:
            raise ValueError("invalid initiating actor")
        if event["condition_or_decision"] not in conditions:
            raise ValueError("invalid condition")
        if event["evidence_status"] != "simulated_test_data" or event["evidence_status"] not in statuses:
            raise ValueError("invalid evidence status")
        date.fromisoformat(event["event_date"])

    arrow_fields = set(SCHEMA["arrow_fields"])
    for arrow in data.get("arrows", []):
        missing = sorted(arrow_fields - set(arrow))
        if missing:
            raise ValueError(f"missing arrow fields: {missing}")
        if arrow["status"] != "simulated_test_data":
            raise ValueError("invalid arrow status")

    print(f"VALID simulated broad ledger: {len(data.get('events', []))} event(s), {len(data.get('arrows', []))} arrow(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
