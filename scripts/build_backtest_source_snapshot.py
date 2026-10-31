#!/usr/bin/env python3
"""Pin candidate source records from repository history for bounded backtest review."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "backtest-source-snapshot.json"
SOURCE_COMMIT = "0ef63b3b5ebadb69e89ed5d453eb38038a9b2382"


def main() -> int:
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    by_id = {record["trend_id"]: record for record in manifest["records"]}
    candidates = json.loads((ANALYSIS / "candidate-comparisons.json").read_text())["candidates"]
    records = {}
    for candidate in candidates:
        for record_id in candidate["evidence_record_ids"]:
            record = by_id.get(record_id)
            if not record or record_id in records:
                continue
            path = record["record_path"]
            try:
                raw = subprocess.check_output(["git", "show", f"{SOURCE_COMMIT}:{path}"], cwd=ROOT)
            except subprocess.CalledProcessError:
                continue
            records[record_id] = {
                "record_path": path,
                "source_commit": SOURCE_COMMIT,
                "blob_sha256": hashlib.sha256(raw).hexdigest(),
                "record": json.loads(raw),
            }
    report = {
        "schema": "external-trend-intelligence.backtest-source-snapshot.v1",
        "source_commit": SOURCE_COMMIT,
        "candidate_count": len(candidates),
        "record_count": len(records),
        "records": records,
        "boundary": "This is a pinned historical snapshot for review. It does not harmonize units, establish independence, or prove a backtest result.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(records)} records from {SOURCE_COMMIT[:12]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
