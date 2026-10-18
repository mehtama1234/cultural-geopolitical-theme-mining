#!/usr/bin/env python3
"""Open a deterministic batch from the full-atlas social queue."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "analysis" / "social-discussions" / "full-atlas-coverage.json"
BATCH_DIR = ROOT / "analysis" / "social-discussions" / "batches"


def main() -> None:
    batch_id = sys.argv[1] if len(sys.argv) > 1 else "atlas-batch-0001"
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 25
    payload = json.loads(QUEUE.read_text(encoding="utf-8"))
    rows = payload["rows"]
    selected = [row for row in rows if row["status"] in {"queued", "in_review"}][start : start + size]
    if not selected:
        raise SystemExit("no queued rows available for requested batch")
    for row in selected:
        row["status"] = "in_review"
        row["batch_id"] = batch_id
        row["next_action"] = "acquire_and_normalize_platform_results"
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    batch = {
        "schema": "social-augmentation-batch-v1",
        "batch_id": batch_id,
        "opened": str(date.today()),
        "window": "2025-10-17 through 2026-10-17",
        "record_count": len(selected),
        "atlas_record_ids": [row["atlas_record_id"] for row in selected],
        "rows": selected,
        "status": "in_review",
    }
    (BATCH_DIR / f"{batch_id}.json").write_text(json.dumps(batch, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    QUEUE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OPENED {batch_id}: {len(selected)} atlas records")


if __name__ == "__main__":
    main()
