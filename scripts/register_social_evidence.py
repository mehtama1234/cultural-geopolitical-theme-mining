#!/usr/bin/env python3
"""Register a normalized social record against an exact atlas record."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"


def main() -> None:
    if len(sys.argv) < 4:
        raise SystemExit("usage: register_social_evidence.py ATLAS_ID PLATFORM RECORD_ID")
    atlas_id, platform, record_id = sys.argv[1:4]
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    matches = [row for row in payload["rows"] if row["atlas_record_id"] == atlas_id]
    if len(matches) != 1:
        raise SystemExit(f"expected one atlas row for {atlas_id}, found {len(matches)}")
    row = matches[0]
    if platform not in row["platforms"]:
        raise SystemExit(f"unsupported platform: {platform}")
    item = row["platforms"][platform]
    if record_id not in item["social_record_ids"]:
        item["social_record_ids"].append(record_id)
    item["status"] = "augmented"
    item["retrieved"] = str(date.today())
    item["result_or_gap"] = "normalized social evidence retained"
    row["next_action"] = "complete_remaining_platform_attempts"
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"REGISTERED {record_id} -> {atlas_id}/{platform}")


if __name__ == "__main__":
    main()
