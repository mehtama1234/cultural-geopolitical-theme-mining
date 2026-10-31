#!/usr/bin/env python3
"""Append one auditable run record to the external observatory refresh ledger."""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "refresh-history.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    existing = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {
        "schema": "external-trend-intelligence.refresh-history.v1",
        "runs": [],
        "append_only": True,
    }
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    manifest = load("observation-manifest.json")
    status = load("refresh-status.json")
    health = load("release-health.json")
    run = {
        "run_id": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_tree_revision": revision,
        "record_count": manifest["record_count"],
        "parse_error_count": manifest["parse_error_count"],
        "source_family_count": status["family_count"],
        "ready_for_review_count": status["ready_for_review_count"],
        "incomplete_count": status["incomplete_count"],
        "release_status": health["release_status"],
        "blocker_count": len(health["blockers"]),
    }
    if not existing["runs"] or existing["runs"][-1].get("source_tree_revision") != revision:
        existing["runs"].append(run)
    existing["latest"] = existing["runs"][-1]
    existing["run_count"] = len(existing["runs"])
    existing["boundary"] = "This ledger proves refresh execution and observed control-plane state across runs. It does not prove source freshness, rights clearance, trend validity, or causal outcomes."
    OUTPUT.write_text(json.dumps(existing, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({existing['run_count']} runs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
