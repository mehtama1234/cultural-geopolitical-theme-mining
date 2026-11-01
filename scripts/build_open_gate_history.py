#!/usr/bin/env python3
"""Append an immutable snapshot of open-gate workload after each refresh."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "open-gate-history.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    register = load("open-gate-register.json")
    refresh = load("refresh-history.json")
    run = refresh["latest"]
    snapshot = {
        "run_id": run["run_id"],
        "source_tree_revision": run["source_tree_revision"],
        "total_open_work_items": register["total_open_work_items"],
        "critical_gate_count": register["critical_gate_count"],
        "gates": {gate["gate_id"]: {"priority": gate["priority"], "open_count": gate["open_count"], "status": gate["status"]} for gate in register["gates"]},
    }
    if OUTPUT.exists():
        prior = json.loads(OUTPUT.read_text())
        snapshots = prior.get("snapshots", [])
    else:
        snapshots = []
    if not snapshots or snapshots[-1]["run_id"] != snapshot["run_id"]:
        snapshots.append(snapshot)
    payload = {
        "schema": "external-trend-intelligence.open-gate-history.v1",
        "status": "append_only_gate_workload_history",
        "snapshot_count": len(snapshots),
        "latest_run_id": snapshot["run_id"],
        "latest_total_open_work_items": snapshot["total_open_work_items"],
        "latest_critical_gate_count": snapshot["critical_gate_count"],
        "snapshots": snapshots,
        "append_only": True,
        "boundary": "This history records gate workload snapshots; it does not prove that a gate was closed, that evidence is valid, or that human ownership exists.",
        "next_action": "Compare snapshots after each refresh and investigate any gate increase, reopened gate, or long-lived unresolved critical gate.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(snapshots)} snapshots)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
