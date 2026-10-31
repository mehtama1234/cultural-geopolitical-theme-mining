#!/usr/bin/env python3
"""Check whether candidate evidence records are locally available for backtesting."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "backtest-readiness.json"


def main() -> int:
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())
    by_id = {record["trend_id"]: record for record in manifest["records"]}
    candidates = json.loads((ANALYSIS / "candidate-comparisons.json").read_text())["candidates"]
    rows = []
    for candidate in candidates:
        records = [by_id.get(record_id) for record_id in candidate["evidence_record_ids"]]
        records = [record for record in records if record]
        paths = [record["record_path"] for record in records]
        missing = [path for path in paths if not (ROOT / path).exists()]
        snapshot_ids = [record_id for record_id in candidate["evidence_record_ids"] if record_id in snapshot["records"]]
        missing_snapshot = [record_id for record_id in candidate["evidence_record_ids"] if record_id not in snapshot["records"]]
        rows.append({
            "candidate_id": candidate["id"],
            "evidence_record_count": len(records),
            "local_record_path_count": len(paths) - len(missing),
            "missing_local_record_paths": missing,
            "snapshot_record_count": len(snapshot_ids),
            "missing_snapshot_record_ids": missing_snapshot,
            "source_url_count": sum(len(record.get("source_urls", [])) for record in records),
            "status": "records_available_comparability_review" if not missing_snapshot else "blocked_missing_snapshot_record",
            "boundary": "Pinned historical records make review possible but do not harmonize units, establish independence, or prove a backtest result.",
        })
    report = {
        "schema": "external-trend-intelligence.backtest-readiness.v1",
        "candidate_count": len(rows),
        "ready_for_design_review_count": sum(row["status"] == "records_available_comparability_review" for row in rows),
        "blocked_missing_local_record_count": sum(row["status"] == "blocked_missing_snapshot_record" for row in rows),
        "rows": rows,
        "next_action": "Review pinned records for compatible units, periods, populations, outcomes, and independent lineage before attempting a temporal backtest.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
