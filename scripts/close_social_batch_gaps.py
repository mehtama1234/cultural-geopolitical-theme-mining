#!/usr/bin/env python3
"""Close every non-terminal row in a reviewed batch with explicit search gaps.

This is only for rows whose acquisition log already documents the public search
attempt. It never overwrites an augmented platform result.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"
TERMINAL = {"augmented", "documented_access_gap", "not_socially_applicable"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("reason")
    args = parser.parse_args()
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    changed = 0
    for row in payload["rows"]:
        if row.get("batch_id") != args.batch_id or row.get("status") in TERMINAL:
            continue
        for item in row["platforms"].values():
            if item["status"] not in TERMINAL:
                item["status"] = "documented_access_gap"
                item["retrieved"] = str(date.today())
                item["result_or_gap"] = args.reason
        row["status"] = "augmented" if any(item["social_record_ids"] for item in row["platforms"].values()) else "documented_access_gap"
        row["terminal_reason"] = "all four platform attempts recorded; retained evidence or documented search/access outcome"
        row["next_action"] = "quality_audit"
        changed += 1
    fd, temp_name = tempfile.mkstemp(prefix="full-atlas-coverage-", suffix=".json", dir=QUEUE.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        os.replace(temp_name, QUEUE)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    print(f"CLOSED {args.batch_id}: {changed} rows with explicit platform outcomes")


if __name__ == "__main__":
    main()
