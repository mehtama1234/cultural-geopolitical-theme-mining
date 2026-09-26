#!/usr/bin/env python3
"""Validate every committed real broad event ledger in the explicit index."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from validate_us_broad_event_ledger import validate
from audit_open_middle_blockers import validate_scope as validate_open_middle_scope


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "analysis/data/us-broad-event-ledger-index-v1.json"
SCHEMA = "us-broad-event-ledger-schema-v1"


def main() -> int:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    entries = index.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("ledger index must contain a non-empty entries list")
    paths: set[str] = set()
    total_events = 0
    total_arrows = 0
    for entry in entries:
        path_text = entry.get("path") if isinstance(entry, dict) else None
        if not isinstance(path_text, str) or not path_text:
            raise ValueError("each ledger index entry needs a path")
        if path_text in paths:
            raise ValueError(f"duplicate ledger index path: {path_text}")
        paths.add(path_text)
        path = ROOT / path_text
        if not path.is_file():
            raise ValueError(f"indexed ledger is missing: {path_text}")
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("schema") != SCHEMA:
            raise ValueError(f"indexed file is not a broad event ledger: {path_text}")
        events, arrows, evidence_class = validate(path)
        total_events += events
        total_arrows += arrows
        print(f"VALID {path_text}: {events} event(s), {arrows} arrow(s), class={evidence_class}")
    open_scope = validate_open_middle_scope()
    print(
        f"VALID real broad event-ledger index: {len(entries)} ledgers, "
        f"{total_events} events, {total_arrows} arrows; "
        f"open-middle scope {open_scope['open_arrow_count']} open arrows"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
