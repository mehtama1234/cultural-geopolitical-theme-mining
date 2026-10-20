#!/usr/bin/env python3
"""Run the long-term atlas publication and evidence controls as one gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    ("macro tension register", ["scripts/validate_macro_tension_register.py"]),
    ("program control sync", ["scripts/validate_program_control_sync.py"]),
    (
        "strategic realization ledger",
        [
            "scripts/validate_realization_ledger.py",
            "analysis/projects/ai-work-control/data/poland-jassm-er-realization-ledger-v1.json",
        ],
    ),
    (
        "data-center realization ledger",
        [
            "scripts/validate_realization_ledger.py",
            "analysis/projects/ai-work-control/data/us-data-center-realization-ledger-v1.json",
        ],
    ),
    ("source registry coverage", ["scripts/audit_source_registry_coverage.py"]),
    ("broad source-promotion audit", ["scripts/audit_source_promotion.py"]),
    ("source-search records", ["scripts/validate_source_search_records.py"]),
    ("trend provenance", ["scripts/validate_trend_provenance.py"]),
    ("trend observation records", ["scripts/validate_trend_observation_records.py"]),
    ("social discussion schema", ["scripts/validate_social_discussions.py"]),
    ("full-atlas social queue", ["scripts/validate_full_atlas_social_queue.py"]),
    ("14-theme social coverage", ["scripts/validate_social_theme_coverage.py"]),
    ("independent trend discovery", ["scripts/validate_independent_trends.py"]),
    ("finding Markdown/HTML parity", ["scripts/validate_us_finding_parity.py"]),
    ("watchlist Markdown/HTML parity", ["scripts/validate_watchlist_parity.py"]),
    ("broad counterexample register", ["scripts/validate_broad_counterexample_register.py"]),
    ("broad priority register", ["scripts/validate_broad_priority_register.py"]),
    ("PSID wave-file audit", ["scripts/test_psid_wave_file_audit.py"]),
    ("broad theme pulse sections", ["scripts/validate_broad_theme_pulse_sections.py"]),
    ("source-first theme map", ["scripts/validate_source_first_theme_map.py"]),
    ("broad-goal integrity", ["scripts/test_broad_goal_integrity.py"]),
    (
        "broad event-ledger contract",
        ["scripts/test_us_broad_event_ledger_contract.py"],
    ),
    (
        "real broad event-ledger index",
        ["scripts/validate_real_broad_event_ledgers.py"],
    ),
    (
        "broad event-ledger portfolio summary",
        ["scripts/validate_broad_event_ledger_portfolio_summary.py"],
    ),
    (
        "broad remedy-stage coverage",
        ["scripts/validate_broad_remedy_stage_coverage.py"],
    ),
    (
        "recovery brief current state",
        ["scripts/validate_recovery_brief_current_state.py"],
    ),
    (
        "broad same-case availability guards",
        ["scripts/test_broad_same_case_episode_availability.py"],
    ),
    ("UAS Older Ages follow-up guards", ["scripts/test_uas_older_ages_event_followup.py"]),
    ("UAS episode manifest", ["scripts/validate_uas_episode_manifest.py"]),
    ("published site links", ["scripts/validate_published_site_links.py"]),
    ("local Markdown links", ["scripts/validate_local_markdown_links.py"]),
    ("acquisition resource policy", ["scripts/test_acquisition_resource_policy.py"]),
    ("program control handoff counts", ["scripts/test_program_control_sync.py"]),
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
