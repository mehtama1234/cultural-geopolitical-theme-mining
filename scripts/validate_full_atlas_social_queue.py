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
PLATFORM_TERMINAL = {"augmented", "documented_access_gap", "not_socially_applicable"}


def main() -> int:
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    atlas_ids = {json.loads(path.read_text(encoding="utf-8")).get("trend_id") for path in ATLAS.glob("*.json")}
    row_ids = [row.get("atlas_record_id") for row in rows]
    errors = []
    expected_count = len(atlas_ids)
    if len(rows) != expected_count or payload.get("atlas_record_count") != expected_count:
        errors.append(f"expected {expected_count} queue rows, found {len(rows)}")
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
            if item.get("status") not in PLATFORM_TERMINAL:
                errors.append(f"{row.get('atlas_record_id')}/{platform}: non-terminal platform status")
            if not item.get("retrieved"):
                errors.append(f"{row.get('atlas_record_id')}/{platform}: missing retrieval date")
            if not item.get("result_or_gap"):
                errors.append(f"{row.get('atlas_record_id')}/{platform}: missing result_or_gap")
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
