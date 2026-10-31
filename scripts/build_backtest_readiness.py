#!/usr/bin/env python3
"""Check whether candidate evidence records are locally available for backtesting."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "backtest-readiness.json"


def exists_in_git(path: str) -> bool:
    """Return whether HEAD contains a record excluded by sparse checkout."""
    return subprocess.run(
        ["git", "cat-file", "-e", f"HEAD:{path}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


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
        missing_worktree = [path for path in paths if not (ROOT / path).exists()]
        missing_git = [path for path in missing_worktree if not exists_in_git(path)]
        snapshot_ids = [record_id for record_id in candidate["evidence_record_ids"] if record_id in snapshot["records"]]
        missing_snapshot = [record_id for record_id in candidate["evidence_record_ids"] if record_id not in snapshot["records"]]
        rows.append({
            "candidate_id": candidate["id"],
            "evidence_record_count": len(records),
            "local_record_path_count": len(paths) - len(missing_worktree),
            "missing_local_record_paths": missing_worktree,
            "pinned_git_record_path_count": len(paths) - len(missing_git),
            "missing_pinned_git_record_paths": missing_git,
            "sparse_checkout_excluded_path_count": len(missing_worktree) - len(missing_git),
            "snapshot_record_count": len(snapshot_ids),
            "missing_snapshot_record_ids": missing_snapshot,
            "source_url_count": sum(len(record.get("source_urls", [])) for record in records),
            "status": "records_available_comparability_review" if not missing_snapshot else "blocked_missing_snapshot_record",
            "boundary": "Working-tree availability can be reduced by sparse checkout. Pinned Git records make review possible but do not harmonize units, establish independence, or prove a backtest result.",
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
