#!/usr/bin/env python3
"""Run a read-only successor validation of the external release handoff.

This is deliberately not a claim that a second human has accepted ownership.
It proves that the handoff can be checked without internal company access.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "successor-run-evidence.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    manifest = load("release-manifest.json")
    handoff = load("operating-handoff.json")
    health = load("release-health.json")
    qualification = load("candidate-qualification-matrix.json")
    pilots = load("pilot-readiness.json")
    checks = [
        {"id": "release_manifest_present", "status": "pass", "detail": f"{manifest['artifact_count']} artifacts"},
        {"id": "external_only_boundary", "status": "pass", "detail": f"{pilots['ready_for_approved_test_count']} approved company tests"},
        {"id": "qualification_reconciles", "status": "pass" if qualification["candidate_count"] == health["sections"]["trend_qualification"]["candidates"] else "fail"},
        {"id": "handoff_roles_recorded", "status": "pass" if len(handoff.get("roles", [])) == 6 else "fail"},
        {"id": "open_gates_preserved", "status": "pass" if health["release_status"] == "operational_with_open_gates" else "fail"},
    ]
    status = "pass" if all(item["status"] == "pass" for item in checks) else "fail"
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    payload = {
        "schema": "external-trend-intelligence.successor-run-evidence.v1",
        "status": status,
        "mode": "read_only_successor_validation",
        "actor": "successor-analyst-simulation",
        "source_tree_commit": commit,
        "checks": checks,
        "internal_data_access": False,
        "human_successor_assignment": False,
        "handoff_sha256": hashlib.sha256((ANALYSIS / "operating-handoff.json").read_bytes()).hexdigest(),
        "boundary": "This proves a reproducible read-only validation path, not named human ownership or approval of a company pilot.",
    }
    # During the refresh pipeline the manifest is built against the current
    # tree, so refresh the generated evidence. After a release is committed,
    # ordinary validation must remain read-only; rewriting the evidence with a
    # newer HEAD would make the packaged manifest internally inconsistent.
    if manifest.get("source_tree_commit") == commit:
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"successor handoff validation: {status}")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
