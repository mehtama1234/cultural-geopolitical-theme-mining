#!/usr/bin/env python3
"""Validate a strategic capability realization ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


EVENT_TYPES = {
    "objective",
    "authorization",
    "agreement",
    "budget",
    "funding",
    "award",
    "modification",
    "production_support",
    "capacity",
    "test",
    "integration",
    "audit_control",
    "shipment",
    "delivery",
    "acceptance",
    "training",
    "fielding",
    "maintenance",
    "inventory",
    "operational_use",
    "external_response",
    "non_observation",
    "comparator",
}
REQUIRED_EVENT_FIELDS = {
    "event_id",
    "event_type",
    "event_date",
    "date_precision",
    "actor",
    "recipient",
    "object",
    "status",
    "source_locator",
    "boundary",
}
ALLOWED_STATUSES = {
    "observed",
    "planned",
    "estimated",
    "inferred",
    "not_observed",
    "observed_comparator",
}


def validate(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if payload.get("schema") != "strategic-capability-realization-ledger-v1":
        errors.append("schema must be strategic-capability-realization-ledger-v1")
    case_id = payload.get("case_id")
    events = payload.get("events")
    if not isinstance(case_id, str) or not case_id:
        errors.append("case_id must be a non-empty string")
    if not isinstance(events, list) or not events:
        errors.append("events must be a non-empty list")
        return errors

    seen: set[str] = set()
    for index, event in enumerate(events):
        prefix = f"events[{index}]"
        if not isinstance(event, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = sorted(REQUIRED_EVENT_FIELDS - event.keys())
        errors.extend(f"{prefix} missing {field}" for field in missing)
        event_id = event.get("event_id")
        if not isinstance(event_id, str) or not event_id:
            errors.append(f"{prefix}.event_id must be a non-empty string")
        elif event_id in seen:
            errors.append(f"{prefix}.event_id is duplicated: {event_id}")
        else:
            seen.add(event_id)
        event_type = event.get("event_type")
        if event_type not in EVENT_TYPES:
            errors.append(f"{prefix}.event_type is unsupported: {event_type!r}")
        status = event.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{prefix}.status is unsupported: {status!r}")
        if "quantity" in event and event["quantity"] is not None:
            if "quantity_unit" not in event or not event["quantity_unit"]:
                errors.append(f"{prefix}.quantity requires quantity_unit")
        if case_id and event.get("case_id") not in (None, case_id):
            errors.append(f"{prefix}.case_id does not match ledger case_id")
        if event_type == "comparator" and status != "observed_comparator":
            errors.append(f"{prefix}.comparator must use observed_comparator status")
        if event_type == "non_observation" and status != "not_observed":
            errors.append(f"{prefix}.non_observation must use not_observed status")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.ledger.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    errors = validate(payload)
    result = {
        "ledger": str(args.ledger),
        "events": len(payload.get("events", [])),
        "status": "valid" if not errors else "invalid",
        "errors": errors,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if errors:
        print(f"INVALID realization ledger: {len(errors)} error(s)")
    else:
        print(f"VALID realization ledger: {result['events']} events")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
