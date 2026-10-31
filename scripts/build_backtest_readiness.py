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
    by_id = {record["trend_id"]: record for record in manifest["records"]}
    candidates = json.loads((ANALYSIS / "candidate-comparisons.json").read_text())["candidates"]
    rows = []
    for candidate in candidates:
        records = [by_id.get(record_id) for record_id in candidate["evidence_record_ids"]]
        records = [record for record in records if record]
        paths = [record["record_path"] for record in records]
        missing = [path for path in paths if not (ROOT / path).exists()]
        rows.append({
            "candidate_id": candidate["id"],
            "evidence_record_count": len(records),
            "local_record_path_count": len(paths) - len(missing),
            "missing_local_record_paths": missing,
            "source_url_count": sum(len(record.get("source_urls", [])) for record in records),
            "status": "ready_for_design_review" if not missing else "blocked_missing_local_record",
            "boundary": "Source URLs in the manifest do not substitute for the missing local record; no backtest result is inferred.",
        })
    report = {
        "schema": "external-trend-intelligence.backtest-readiness.v1",
        "candidate_count": len(rows),
        "ready_for_design_review_count": sum(row["status"] == "ready_for_design_review" for row in rows),
        "blocked_missing_local_record_count": sum(row["status"] == "blocked_missing_local_record" for row in rows),
        "rows": rows,
        "next_action": "Acquire or repin the missing source-backed record artifacts before attempting a temporal backtest; preserve source identity and rights during acquisition.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
