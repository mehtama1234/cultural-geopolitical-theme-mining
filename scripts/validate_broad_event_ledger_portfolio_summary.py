#!/usr/bin/env python3
"""Recompute and validate the committed broad event-ledger portfolio summary."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "analysis/data/us-broad-event-ledger-index-v1.json"
SUMMARY = ROOT / "analysis/data/us-broad-event-ledger-portfolio-summary-v1.json"


def main() -> int:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    events: list[dict] = []
    arrows: list[dict] = []
    domains: Counter[str] = Counter()
    for entry in index["entries"]:
        data = json.loads((ROOT / entry["path"]).read_text(encoding="utf-8"))
        events.extend(data["events"])
        arrows.extend(data["arrows"])
        domains[entry["domain"]] += len(data["events"])

    actual_totals = {
        "ledgers": len(index["entries"]),
        "events": len(events),
        "arrows": len(arrows),
    }
    if summary.get("totals") != actual_totals:
        raise ValueError(f"portfolio totals stale: {summary.get('totals')} != {actual_totals}")

    expected = {
        "events_by_domain": dict(sorted(domains.items())),
        "event_evidence_status": dict(sorted(Counter(e["evidence_status"] for e in events).items())),
        "arrow_status": dict(sorted(Counter(a["status"] for a in arrows).items())),
        "event_units": dict(sorted(Counter(e["unit"] for e in events).items())),
    }
    for field, value in expected.items():
        if summary.get(field) != value:
            raise ValueError(f"portfolio {field} stale: {summary.get(field)} != {value}")

    print(
        "VALID broad event-ledger portfolio summary: "
        f"{actual_totals['ledgers']} ledgers, {actual_totals['events']} events, "
        f"{actual_totals['arrows']} arrows"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
