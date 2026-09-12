"""Validate the simulated household-calendar fixture without treating it as evidence."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "manifests/us-household-calendar-schema-v1.json").read_text())
FIXTURE = ROOT / "analysis/samples/US-HOUSEHOLD-CALENDAR-SIMULATED_V1.json"


def main() -> int:
    data = json.loads(FIXTURE.read_text())
    if data.get("evidence_class") != "simulated_test_data":
        raise ValueError("fixture must be marked simulated_test_data")
    dimensions = {item["name"]: item for item in SCHEMA["dimensions"]}
    for record in data.get("months", []):
        for name, spec in dimensions.items():
            if spec.get("required") and name not in record:
                raise ValueError(f"missing required monthly field: {name}")
        if record.get("tenure") not in dimensions["tenure"]["values"]:
            raise ValueError("invalid tenure")
        if record.get("income_stability") not in dimensions["income_stability"]["values"]:
            raise ValueError("invalid income_stability")
    event_specs = {item["name"]: item for item in SCHEMA["event_fields"]}
    for event in data.get("events", []):
        for name, spec in event_specs.items():
            if spec.get("required") and name not in event:
                raise ValueError(f"missing required event field: {name}")
        if event.get("evidence_status") != "simulated_test_data":
            raise ValueError("invalid evidence_status")
    print(f"VALID simulated fixture: {len(data.get('months', []))} month(s), {len(data.get('events', []))} event(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
