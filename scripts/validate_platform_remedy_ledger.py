#!/usr/bin/env python3
"""Validate the platform-remedy ledger's required structural invariants."""

import json
import sys
from pathlib import Path


STAGE_FIELDS = (
    "explanation",
    "human_review",
    "correction_restoration",
    "payment_compensation",
    "anti_retaliation",
)
REQUIRED_RECORD_FIELDS = (
    "id",
    "place",
    "population",
    "source_type",
    "decision_surface",
    "worker_route",
    "stages",
    "evidence_strength",
    "boundary",
)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL platform remedy ledger: {message}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "analysis/projects/ai-work-control/data/platform-remedy-case-ledger-v1.json"
    )
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot load {path}: {exc}")

    if payload.get("schema_version") != "platform-remedy-case-ledger-v1":
        fail("unexpected schema_version")
    if payload.get("stage_fields") != list(STAGE_FIELDS):
        fail("stage_fields do not match the protocol")
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        fail("records must be a non-empty list")

    ids = []
    for index, record in enumerate(records):
        missing = [field for field in REQUIRED_RECORD_FIELDS if field not in record]
        if missing:
            fail(f"record {index} missing {', '.join(missing)}")
        record_id = record["id"]
        if record_id in ids:
            fail(f"duplicate record id {record_id}")
        ids.append(record_id)
        if not isinstance(record["decision_surface"], list) or not record["decision_surface"]:
            fail(f"record {record_id} decision_surface must be non-empty")
        stages = record["stages"]
        if set(stages) != set(STAGE_FIELDS):
            fail(f"record {record_id} has incorrect stage keys")
        for field in REQUIRED_RECORD_FIELDS:
            if field not in ("decision_surface", "stages") and (
                not isinstance(record[field], str) or not record[field].strip()
            ):
                fail(f"record {record_id} field {field} must be a non-empty string")
        if "implementation_stage" in record and (
            not isinstance(record["implementation_stage"], str)
            or not record["implementation_stage"].strip()
        ):
            fail(f"record {record_id} implementation_stage must be a non-empty string when present")
        for field in STAGE_FIELDS:
            if not isinstance(stages[field], str) or not stages[field].strip():
                fail(f"record {record_id} stage {field} must be a non-empty string")

    print(f"PASS platform remedy ledger: {len(records)} records; required fields and stage keys valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
