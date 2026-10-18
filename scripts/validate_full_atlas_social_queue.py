#!/usr/bin/env python3
"""Validate record-level social augmentation accounting."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"
ATLAS = ROOT / "analysis" / "records"
PLATFORMS = ("youtube", "reddit", "linkedin", "x")
TERMINAL = {"augmented", "documented_access_gap", "not_socially_applicable"}


def main() -> int:
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    atlas_ids = {json.loads(path.read_text(encoding="utf-8")).get("trend_id") for path in ATLAS.glob("*.json")}
    row_ids = [row.get("atlas_record_id") for row in rows]
    errors = []
    if len(rows) != 1978 or payload.get("atlas_record_count") != 1978:
        errors.append(f"expected 1978 queue rows, found {len(rows)}")
    if len(row_ids) != len(set(row_ids)):
        errors.append("duplicate atlas_record_id values")
    if set(row_ids) != atlas_ids:
        errors.append(f"queue/atlas ID mismatch: queue={len(set(row_ids))}, atlas={len(atlas_ids)}")
    for row in rows:
        if set(row.get("platforms", {})) != set(PLATFORMS):
            errors.append(f"{row.get('atlas_record_id')}: platform set is incomplete")
        for platform in PLATFORMS:
            item = row["platforms"][platform]
            if not item.get("query"):
                errors.append(f"{row.get('atlas_record_id')}/{platform}: missing query")
        if row.get("status") in TERMINAL and not row.get("terminal_reason"):
            errors.append(f"{row.get('atlas_record_id')}: terminal row lacks terminal_reason")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    print(f"VALID full-atlas social queue: {len(rows)} records; statuses={counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
