#!/usr/bin/env python3
"""Record a searched platform outcome for one atlas row.

Use documented_access_gap only after a dated public search attempt is described
in the batch acquisition log; this is an accounting state, not a claim that the
platform contains no relevant discussion.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"
TERMINAL = {"augmented", "documented_access_gap", "not_socially_applicable"}


def main() -> None:
    if len(sys.argv) < 5:
        raise SystemExit("usage: record_social_platform_outcome.py ATLAS_ID PLATFORM STATUS REASON")
    atlas_id, platform, status = sys.argv[1:4]
    reason = " ".join(sys.argv[4:])
    if status not in {"documented_access_gap", "not_socially_applicable"}:
        raise SystemExit("status must be documented_access_gap or not_socially_applicable")
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    rows = [row for row in payload["rows"] if row["atlas_record_id"] == atlas_id]
    if len(rows) != 1:
        raise SystemExit(f"expected one atlas row for {atlas_id}, found {len(rows)}")
    row = rows[0]
    item = row["platforms"].get(platform)
    if item is None:
        raise SystemExit(f"unsupported platform: {platform}")
    item["status"] = status
    item["retrieved"] = str(date.today())
    item["result_or_gap"] = reason
    if all(part["status"] in TERMINAL for part in row["platforms"].values()):
        row["status"] = "augmented" if any(part["social_record_ids"] for part in row["platforms"].values()) else "documented_access_gap"
        row["terminal_reason"] = "all four platform attempts recorded; retained evidence or documented search/access outcome"
        row["next_action"] = "quality_audit"
    else:
        row["next_action"] = "complete_remaining_platform_attempts"
    fd, temp_name = tempfile.mkstemp(prefix="full-atlas-coverage-", suffix=".json", dir=QUEUE.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        os.replace(temp_name, QUEUE)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    print(f"RECORDED {atlas_id}/{platform}: {status}")


if __name__ == "__main__":
    main()
