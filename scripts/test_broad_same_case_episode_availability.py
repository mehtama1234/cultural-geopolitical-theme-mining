#!/usr/bin/env python3
"""Regression checks for the broad same-case availability validator."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/validate_broad_same_case_episode_availability.py"
AUDIT = ROOT / "analysis/data/broad-same-case-episode-availability-audit-v1.json"


def run(payload: dict[str, object]) -> subprocess.CompletedProcess[str]:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8") as handle:
        json.dump(payload, handle)
        handle.flush()
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--audit", handle.name],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )


def main() -> int:
    fixture = json.loads(AUDIT.read_text(encoding="utf-8"))
    accepted = run(fixture)
    assert accepted.returncode == 0, accepted.stderr

    missing_boundary = copy.deepcopy(fixture)
    del missing_boundary["storage_boundary"]
    rejected = run(missing_boundary)
    assert rejected.returncode != 0
    assert "top-level fields" in rejected.stderr

    absolute_source = copy.deepcopy(fixture)
    absolute_source["sources"][0]["source"] = str(ROOT / fixture["sources"][0]["source"])
    rejected = run(absolute_source)
    assert rejected.returncode != 0
    assert "repository-relative" in rejected.stderr

    negative_records = copy.deepcopy(fixture)
    negative_records["sources"][0]["records"] = -1
    rejected = run(negative_records)
    assert rejected.returncode != 0
    assert "nonnegative integer" in rejected.stderr

    mismatched_summary = copy.deepcopy(fixture)
    mismatched_summary["stage_summary"]["verified_remedy"]["partial"] = 7
    rejected = run(mismatched_summary)
    assert rejected.returncode != 0
    assert "does not match source rows" in rejected.stderr

    print("PASS broad same-case availability regression checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
