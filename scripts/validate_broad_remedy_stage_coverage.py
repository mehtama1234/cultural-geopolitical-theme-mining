#!/usr/bin/env python3
"""Validate remedy-stage coverage against the canonical event-ledger index."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "analysis/data/us-broad-event-ledger-index-v1.json"
AUDIT = ROOT / "analysis/data/us-broad-remedy-stage-coverage-audit-2026-09-18.json"


def main() -> int:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    events: list[dict] = []
    ledgers_with_stage: set[str] = set()
    expected_rows: set[tuple[str, str, str]] = set()

    for entry in index["entries"]:
        path = entry["path"]
        data = json.loads((ROOT / path).read_text(encoding="utf-8"))
        for event in data["events"]:
            events.append(event)
            if "remedy_stage" in event:
                ledgers_with_stage.add(path)
                expected_rows.add((event["event_id"], event["remedy_stage"], path))

    absent = sum("remedy_stage" not in event for event in events)
    stage_counts = Counter(
        event.get("remedy_stage", "unknown_or_not_recorded") for event in events
    )
    expected_portfolio = {
        "ledgers": len(index["entries"]),
        "events": len(events),
        "events_with_explicit_remedy_stage": len(events) - absent,
        "events_without_explicit_remedy_stage": absent,
        "ledgers_with_explicit_remedy_stage": len(ledgers_with_stage),
        "ledgers_without_explicit_remedy_stage": len(index["entries"]) - len(ledgers_with_stage),
    }
    if audit.get("portfolio") != expected_portfolio:
        raise ValueError(f"remedy portfolio stale: {audit.get('portfolio')} != {expected_portfolio}")

    expected_stage_counts = {
        stage: stage_counts.get(stage, 0)
        for stage in audit["stage_counts"]
    }
    if audit.get("stage_counts") != expected_stage_counts:
        raise ValueError(
            f"remedy stage counts stale: {audit.get('stage_counts')} != {expected_stage_counts}"
        )

    actual_rows = {
        (row["event_id"], row["remedy_stage"], row["ledger"])
        for row in audit.get("explicit_stage_rows", [])
    }
    if actual_rows != expected_rows:
        missing = sorted(expected_rows - actual_rows)
        extra = sorted(actual_rows - expected_rows)
        raise ValueError(f"explicit remedy rows stale: missing={missing}, extra={extra}")

    print(
        "VALID remedy-stage coverage: "
        f"{expected_portfolio['events_with_explicit_remedy_stage']} explicit events, "
        f"{stage_counts.get('remedy_reported_received', 0)} reported received, "
        f"{stage_counts.get('remedy_verified_received', 0)} verified received"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
