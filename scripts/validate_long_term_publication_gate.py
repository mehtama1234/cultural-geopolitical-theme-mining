#!/usr/bin/env python3
"""Run the long-term atlas publication and evidence controls as one gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    ("program control sync", ["scripts/validate_program_control_sync.py"]),
    (
        "strategic realization ledger",
        [
            "scripts/validate_realization_ledger.py",
            "analysis/projects/ai-work-control/data/poland-jassm-er-realization-ledger-v1.json",
        ],
    ),
    ("source registry coverage", ["scripts/audit_source_registry_coverage.py"]),
    ("source-search records", ["scripts/validate_source_search_records.py"]),
    ("trend provenance", ["scripts/validate_trend_provenance.py"]),
    ("trend observation records", ["scripts/validate_trend_observation_records.py"]),
    ("finding Markdown/HTML parity", ["scripts/validate_us_finding_parity.py"]),
    ("watchlist Markdown/HTML parity", ["scripts/validate_watchlist_parity.py"]),
    ("published site links", ["scripts/validate_published_site_links.py"]),
    ("local Markdown links", ["scripts/validate_local_markdown_links.py"]),
    ("diff whitespace", ["git", "diff", "--check"]),
]


def main() -> int:
    failures: list[str] = []
    for label, command in CHECKS:
        result = subprocess.run(
            [sys.executable, *command]
            if command[0].endswith(".py")
            else command,
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        output = (result.stdout + result.stderr).strip()
        if result.returncode:
            failures.append(label)
            print(f"FAIL {label}")
            if output:
                print(output)
            continue
        summary = output.splitlines()[-1] if output else "passed"
        print(f"PASS {label}: {summary}")
    if failures:
        print("PUBLICATION GATE FAILED: " + ", ".join(failures))
        return 1
    print(f"PUBLICATION GATE PASSED: {len(CHECKS)} checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
