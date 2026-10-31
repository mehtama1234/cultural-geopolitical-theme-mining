#!/usr/bin/env python3
"""Summarize external observatory readiness and unresolved gates."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "release-health.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    status = load("refresh-status.json")
    contract = load("evidence-contract-audit.json")
    qualification = load("candidate-qualification-matrix.json")
    readiness = load("backtest-readiness.json")
    comparability = load("backtest-comparability-review.json")
    monitoring = load("trend-monitoring-register.json")
    pilots = load("pilot-register.json")
    controls = load("source-family-controls.json")
    health = {
        "source_refresh": {
            "families": status["family_count"],
            "ready_for_review": status["ready_for_review_count"],
            "incomplete": status["incomplete_count"],
            "status": "pass" if status["incomplete_count"] == 0 else "hold",
        },
        "evidence_contract": {
            "observations": contract["observation_count"],
            "gaps": contract["contract_gap_count"],
            "status": "pass" if contract["contract_gap_count"] == 0 else "hold",
        },
        "rights_and_publisher_dependence": {
            "families": controls["family_count"],
            "rights_unverified": sum(item["rights_status"] != "verified" for item in controls["families"]),
            "dependence_review_required": sum(item["publisher_dependence"] == "review_required" for item in controls["families"]),
            "status": "hold" if any(item["rights_status"] != "verified" or item["publisher_dependence"] == "review_required" for item in controls["families"]) else "pass",
        },
        "trend_qualification": {
            "candidates": qualification["candidate_count"],
            "qualified": qualification["qualified_external_trend_count"],
            "held": qualification["held_count"],
            "status": "hold" if qualification["held_count"] else "pass",
        },
        "backtest": {
            "records_available_for_review": readiness["ready_for_design_review_count"],
            "comparable_subsets": comparability["comparable_subset_candidate_count"],
            "harmonization_required": comparability["harmonization_required_count"],
            "status": "hold" if comparability["harmonization_required_count"] else "pass",
        },
        "monitoring": {
            "registered": len(monitoring["trends"]),
            "status": "pass" if monitoring["trends"] else "hold",
        },
        "company_pilots": {
            "registered": len(pilots["pilots"]),
            "approved_tests": sum(item["status"] == "approved_test" for item in pilots["pilots"]),
            "status": "hold" if any(item["status"] != "approved_test" for item in pilots["pilots"]) else "pass",
        },
    }
    blockers = []
    if health["trend_qualification"]["held"]:
        blockers.append("external candidates remain held")
    if health["backtest"]["harmonization_required"]:
        blockers.append("backtest units, periods, populations, or geographies require harmonization")
    if health["company_pilots"]["approved_tests"] == 0:
        blockers.append("no company pilot is approved; external qualification gate is not passed")
    if health["rights_and_publisher_dependence"]["status"] == "hold":
        blockers.append("rights and publisher-dependence review remains open for source families")
    report = {
        "schema": "external-trend-intelligence.release-health.v1",
        "release_status": "operational_with_gates" if not any(section["status"] == "hold" for section in health.values()) else "operational_with_open_gates",
        "sections": health,
        "blockers": blockers,
        "boundary": "This is a release-control summary, not evidence that any trend is causal, forecast-valid, rights-cleared, independent, or company-relevant.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({report['release_status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
