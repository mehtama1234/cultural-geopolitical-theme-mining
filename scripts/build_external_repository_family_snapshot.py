#!/usr/bin/env python3
"""Capture pinned repository lineage for external source families without copying data."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "repository-family-snapshot.json"

FAMILIES = [
    {
        "id": "annual-report-research",
        "repository_path": "/home/mehta/git-repo/organization-intelligence-system",
        "revision": "5d4434b9ff46e8d28176624a7ec44dfddee8be4b",
        "manifest_paths": [
            "annual-report-research/README.md",
            "annual-report-research/START-HERE.md",
            "annual-report-research/analysis/company-first-principles/annual-report-final-integrated-theme-map-pass-1.md",
            "annual-report-research/analysis/company-first-principles/annual-report-public-citation-source-list-pass-1.md",
            "annual-report-research/scripts/verify-trend-archive-json.py",
        ],
        "directory_prefixes": ["annual-report-research/analysis/", "annual-report-research/data/"],
    },
    {
        "id": "inc5000-analysis",
        "repository_path": "/home/mehta/git-repo/inc5000-analysis",
        "revision": "92fad318ff05efcc5707f997bb1b5b18f3bceab2",
        "manifest_paths": [
            "INC5000-INDEPENDENT-SOURCE-INDEX-V1.md",
            "data/processed/inc5000_rebuild_manifest_v1.json",
            "data/processed/opportunity_intelligence_manifest.json",
            "data/processed/strategic_source_ledger.json",
            "data/processed/inc5000_independent_source_index_v1.json",
        ],
        "directory_prefixes": ["data/processed/", "data/public_company_intelligence/"],
    },
    {
        "id": "ibis-industries",
        "repository_path": "/home/mehta/git-repo/ibis-industries",
        "revision": "b895acd021fbe3dc1d610255952b1373748e3bc3",
        "manifest_paths": [
            "research_manifest.json",
            "cross_industry_findings_register.json",
            "cross_industry_trends_2025_2026.json",
            "source_inventory.json",
            "cross_industry_pattern_matrix.json",
            "cross_industry_pattern_inventory.json",
            "cross_industry_pattern_deep_dives.json",
        ],
        "directory_prefixes": ["trend-review-batches/"],
    },
    {
        "id": "social-research",
        "repository_path": "/home/mehta/git-repo/social-research",
        "revision": "c2ff3e3a49129117802425514660ce4b2cf67744",
        "manifest_paths": [
            "analysis/social/integrated-trend-atlas-report.json",
            "analysis/social/multi-platform-collection-manifest.json",
            "analysis/social/publication-release-manifest.json",
            "analysis/social/publication-evidence-appendix.md",
        ],
        "directory_prefixes": ["analysis/social/", "social-trends/"],
    },
    {
        "id": "trend-hunting",
        "repository_path": "/home/mehta/git-repo/trend-hunting",
        "revision": "19d8b2443f26f52da2331736320dcb265a9de34f",
        "manifest_paths": [
            "analysis/DEEP-TRENDS-EVIDENCE-GRAPH-V1.md",
            "analysis/CROSS-REPOSITORY-DEEP-TRENDS-INTEGRATION-V1.md",
            "data/processed/ai_v7_deep_trend_synthesis_v1.json",
            "data/processed/signal_to_outcome_funnel_v1.json",
            "data/processed/ai_v7_ftc_remedy_register_v1.json",
            "data/processed/ai_v7_implementation_search_audit_v1.json",
            "data/processed/ai_v7_recourse_maturity_matrix_v1.json",
            "data/processed/ai_v7_acquisition_ledger_v1.json",
            "data/processed/ai_v7_completed_redress_comparator_v1.json",
            "data/processed/ai_v7_amazon_flex_tip_redress_comparator_v1.json",
            "data/processed/ai_v7_worker_outcome_comparator_v1.json",
            "data/processed/ai_v7_worker_counterexample_comparator_v1.json",
            "data/processed/ai_v7_hotak_outcome_comparator_v1.json",
            "data/processed/ai_v7_ayyub_comparator_v1.json",
            "data/processed/ai_v7_observed_remedy_endpoint_register_v1.json",
            "data/processed/ai_v7_ibm_deployment_outcome_comparator_v1.json",
            "data/processed/ftc_rytr_post_reversal_surface_v1.json",
            "data/processed/ai_v7_cmg_implementation_refresh_20260917.json",
            "data/processed/ai_v7_workado_implementation_refresh_20260917.json",
        ],
        "directory_prefixes": ["analysis/", "data/processed/"],
    },
]


def run(repo: str, *args: str) -> str:
    return subprocess.check_output(["git", "-C", repo, *args], text=True)


def main() -> int:
    families = []
    for family in FAMILIES:
        manifest_entries = []
        for path in family["manifest_paths"]:
            object_ref = f"{family['revision']}:{path}"
            try:
                blob = run(family["repository_path"], "rev-parse", object_ref).strip()
                size = int(run(family["repository_path"], "cat-file", "-s", object_ref).strip())
            except subprocess.CalledProcessError as exc:
                raise ValueError(f"{family['id']} missing pinned path: {path}") from exc
            manifest_entries.append({"path": path, "blob": blob, "size": size})
        family_snapshot = {
            "id": family["id"],
            "repository_path": family["repository_path"],
            "revision": family["revision"],
            "manifest_paths": manifest_entries,
            "directory_prefix_counts": {
                prefix: len(
                    run(family["repository_path"], "rev-list", "--objects", family["revision"], "--", prefix).splitlines()
                )
                for prefix in family["directory_prefixes"]
            },
            "boundary": "Blob lineage proves what was present at the pinned revision; it does not prove that every record is independent, current, representative, or suitable for a trend claim.",
        }
        families.append(family_snapshot)
    snapshot = {
        "schema": "external-trend-intelligence.repository-family-snapshot.v1",
        "purpose": "Pinned lineage for external repository source families used before internal company-data validation.",
        "families": families,
    }
    OUTPUT.write_text(json.dumps(snapshot, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(families)} families)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
