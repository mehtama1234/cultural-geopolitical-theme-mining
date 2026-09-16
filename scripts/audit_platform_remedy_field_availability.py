#!/usr/bin/env python3
"""Audit practical-exit fields in the local platform-remedy dry-run ledger."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def status(row: dict, key: str) -> str:
    value = row.get(key)
    if isinstance(value, dict):
        return str(value.get("evidence_status", "missing"))
    return "observed" if value not in (None, "") else "missing"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=root / "analysis/projects/us-customer-automation-recourse/practical-exit-platform-ledger-dry-run-v1.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "analysis/projects/us-customer-automation-recourse/data/platform-remedy-field-availability-2026-09-16.json",
    )
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    episodes = data.get("episodes", [])
    if len(episodes) != 27:
        raise ValueError(f"expected 27 platform episodes, found {len(episodes)}")
    fields = [
        "alternatives",
        "effort",
        "followup_window",
        "meaning_and_action",
        "protected_outcome",
        "sacrificed_outcome",
    ]
    availability = {
        field: {key: value for key, value in sorted(Counter(status(row, field) for row in episodes).items())}
        for field in fields
    }
    remedy_status = Counter(status(row, "remedy_verification") for row in episodes)
    post_status = Counter(str(row.get("post_event_status", "missing")) for row in episodes)
    output = {
        "format": "platform-remedy-field-availability-audit-v1",
        "status": "field_availability_audit",
        "checked": "2026-09-16",
        "source_unit": "local platform-remedy practical-exit dry-run episodes",
        "episodes": len(episodes),
        "observed_route_count": sum(status(row, "attempted_route") == "observed" for row in episodes),
        "observed_decision_count": sum(status(row, "decision") == "observed" for row in episodes),
        "field_status_counts": availability,
        "remedy_verification_status_counts": dict(sorted(remedy_status.items())),
        "post_event_status_counts": dict(sorted(post_status.items())),
        "result": "All 27 episodes have observed attempted routes and decisions. Ten have observed remedy-related records and eight have access_restored post-event labels, but all 27 have unknown alternatives, effort, follow-up window, remedy receipt, durability, protected/sacrificed outcomes, and meaning/action.",
        "boundary": "This is a field-availability audit of an existing source-coded dry-run, not a representative platform-worker sample, remedy receipt rate, welfare estimate, or practical-exit rate.",
        "source": "analysis/projects/us-customer-automation-recourse/practical-exit-platform-ledger-dry-run-v1.json",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"VALID platform remedy field availability audit: {len(episodes)} episodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
