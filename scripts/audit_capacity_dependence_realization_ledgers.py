#!/usr/bin/env python3
"""Audit local realization ledgers for capacity, control, and leverage stages."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


STAGE_BY_EVENT = {
    "authorization": "commitment",
    "agreement": "commitment",
    "modification": "commitment",
    "delivery": "delivery_or_operation",
    "capacity": "capacity_or_operation",
    "operational_use": "delivery_or_operation",
    "external_response": "governance_or_external_response",
    "audit_control": "control_or_replaceability",
    "comparator": "counterexample",
    "non_observation": "missing_stage",
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "analysis/projects/ai-work-control/data/capacity-dependence-realization-audit-v1.json")
    parser.add_argument("ledgers", nargs="*", type=Path, default=[
        root / "analysis/projects/ai-work-control/data/us-data-center-realization-ledger-v1.json",
        root / "analysis/projects/ai-work-control/data/poland-jassm-er-realization-ledger-v1.json",
    ])
    args = parser.parse_args()
    cases = []
    for path in args.ledgers:
        data = json.loads(path.read_text(encoding="utf-8"))
        events = []
        for event in data["events"]:
            event_type = event["event_type"]
            events.append({
                "event_id": event["event_id"],
                "event_date": event["event_date"],
                "event_type": event_type,
                "stage": STAGE_BY_EVENT.get(event_type, "unclassified"),
                "source_status": event["status"],
                "boundary": event["boundary"],
            })
        cases.append({
            "case_id": data["case_id"],
            "source_ledger": str(path.relative_to(root)),
            "promotion_status": data["promotion_status"],
            "event_count": len(events),
            "stage_counts": dict(sorted(Counter(e["stage"] for e in events).items())),
            "status_counts": dict(sorted(Counter(e["source_status"] for e in events).items())),
            "events": events,
        })
    result = {
        "format": "capacity-dependence-realization-audit-v1",
        "status": "stage_coverage_audit_only",
        "checked": "2026-09-16",
        "cases": cases,
        "cross_case_boundary": "The ledgers show commitment, selected capacity, governance, and operational-stress stages, but do not establish complete accepted/operating capability, replaceability, household/partner incidence, or changed external behavior.",
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"WROTE {args.output.relative_to(root)}")
    for case in cases:
        print(case["case_id"], case["stage_counts"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
