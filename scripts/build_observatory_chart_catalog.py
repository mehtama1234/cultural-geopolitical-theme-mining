#!/usr/bin/env python3
"""Build the frontend chart catalog with explicit evidence boundaries."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "observatory-chart-catalog.json"


CHARTS = [
    {
        "chart_id": "domain-coverage",
        "theme": "observatory-health",
        "subtheme": "external-domain-coverage",
        "concept": "breadth of observed external evidence",
        "title": "Required enterprise domains observed",
        "chart_type": "coverage_bar",
        "source_artifacts": ["domain-coverage-audit.json"],
        "visual_encoding": {"category": "domain", "value": "record_count", "status": "coverage_status"},
        "required_visible_fields": ["source_host_count", "unique_source_url_count", "coverage_status"],
        "status_field": "status",
        "boundary": "Coverage is an inventory measure, not evidence that a domain trend is valid or decision-ready.",
    },
    {
        "chart_id": "qualified-and-held-trends",
        "theme": "trend-qualification",
        "subtheme": "promotion-and-holdout-gates",
        "concept": "qualified signals versus unresolved hypotheses",
        "title": "Qualified, monitored, and held candidates",
        "chart_type": "status_stack",
        "source_artifacts": ["candidate-qualification-matrix.json", "trend-monitoring-evaluation.json"],
        "visual_encoding": {"category": "gate_status", "value": "candidate_count", "status": "qualification_status"},
        "required_visible_fields": ["blocking_gates", "next_action", "counter_signal"],
        "status_field": "overall_status",
        "boundary": "Held candidates must remain visibly separate from qualified external trends.",
    },
    {
        "chart_id": "food-insecurity-holdout",
        "theme": "social-and-economic-pressure",
        "subtheme": "food-insecurity-persistence",
        "concept": "persistence across construction and holdout periods",
        "title": "Food insecurity: construction versus holdout",
        "chart_type": "paired_endpoint",
        "source_artifacts": ["food-insecurity-temporal-holdout.json", "food-insecurity-independent-comparison.json", "urban-wbns-food-insecurity-2025.json", "usda-temporal-holdout.json"],
        "visual_encoding": {"category": "measure", "value": "value", "series": "construction_or_holdout"},
        "required_visible_fields": ["period", "unit", "geography", "uncertainty", "counter_signal"],
        "status_field": "status",
        "boundary": "Descriptive persistence only; publisher frames and methodology changes are not pooled.",
    },
    {
        "chart_id": "financial-room-context",
        "theme": "financial-and-cultural-pressure",
        "subtheme": "practical-room-and-social-connection",
        "concept": "separate directional mechanisms under financial pressure",
        "title": "Financial pressure and social reconnection",
        "chart_type": "directional_comparison",
        "source_artifacts": ["financial-room-decision-card.json", "us-financial-room-independent-comparison.json"],
        "visual_encoding": {"category": "source_measure", "value": "directional_change", "series": "source_family"},
        "required_visible_fields": ["period", "unit", "geography", "scope_or_denominator", "counter_signal"],
        "status_field": "status",
        "boundary": "Mechanism context only; incompatible denominators and rights prevent pooled estimation or company use.",
    },
    {
        "chart_id": "mobility-income-gradient",
        "theme": "infrastructure-and-access",
        "subtheme": "mobility-constraint",
        "concept": "income-stratified access differences across datasets",
        "title": "Zero-vehicle prevalence by income",
        "chart_type": "multi_source_slope",
        "source_artifacts": ["mobility-access-independent-comparison.json", "mobility-access-temporal-holdout.json"],
        "visual_encoding": {"category": "income_group", "value": "zero_vehicle_percent", "series": "dataset"},
        "required_visible_fields": ["period", "unit", "geography", "scope_or_denominator", "uncertainty"],
        "status_field": "pooling_decision",
        "boundary": "Independent directional challenge, not a common estimate or causal company exposure.",
    },
    {
        "chart_id": "forecast-vintage-spread",
        "theme": "financial-and-market",
        "subtheme": "global-growth-forecast-risk",
        "concept": "publisher disagreement and realized-outcome readiness",
        "title": "Global growth forecast vintages",
        "chart_type": "forecast_range",
        "source_artifacts": ["global-growth-forecast-comparison.json", "forecast-lineage-review.json", "forecast-backtest-register.json"],
        "visual_encoding": {"category": "publisher", "value": "forecast_value", "series": "target_period"},
        "required_visible_fields": ["vintage", "uncertainty", "backtest_status", "evidence_boundary"],
        "status_field": "status",
        "boundary": "Comparison queue, not an endorsed forecast; realized outcomes and rights remain open.",
    },
    {
        "chart_id": "source-freshness",
        "theme": "observatory-health",
        "subtheme": "refresh-reliability",
        "concept": "whether each source family is safe to refresh into the release",
        "title": "Source-family freshness decisions",
        "chart_type": "readiness_matrix",
        "source_artifacts": ["refresh-freshness-decision.json", "refresh-status.json"],
        "visual_encoding": {"category": "source_family", "value": "age_days", "status": "release_decision"},
        "required_visible_fields": ["last_successful_refresh", "age_days", "missing_artifact_count", "action"],
        "status_field": "status",
        "boundary": "Freshness permits intake only; it does not establish rights, independence, or trend validity.",
    },
    {
        "chart_id": "ibis-adult-day-outcome-changes",
        "theme": "industry-and-workforce",
        "subtheme": "adult-day-capacity-and-payer-context",
        "concept": "bounded change across capacity, participation, and state payer context",
        "title": "Adult-day outcome changes: separate measures",
        "chart_type": "normalized_change_bars",
        "source_artifacts": ["ibis-adult-day-outcome-review.json", "npals-public-table-extract.json"],
        "visual_encoding": {"category": "derived_measure", "value": "percent_change", "status": "review_status"},
        "required_visible_fields": ["period", "unit", "geography", "uncertainty", "counter_signal"],
        "status_field": "review_status",
        "boundary": "Separate descriptive changes only; survey-frame differences, state-specific rates, and rights boundaries prevent pooled estimation or causal company claims.",
    },
    {
        "chart_id": "ibis-dock-defense-execution-obligations",
        "theme": "geopolitical-and-infrastructure",
        "subtheme": "naval-maintenance-execution-context",
        "concept": "realized transaction obligations beside, but not pooled with, budget context",
        "title": "Bath Iron Works execution obligations by fiscal year",
        "chart_type": "fiscal_year_bar",
        "source_artifacts": ["ibis-dock-defense-execution-comparison.json", "usaspending-bath-iron-works-execution-snapshot.json"],
        "visual_encoding": {"category": "fiscal_year", "value": "positive_obligation_usd", "status": "comparison_status"},
        "required_visible_fields": ["period", "unit", "geography", "scope_or_denominator", "uncertainty", "counter_signal"],
        "status_field": "status",
        "boundary": "Transaction obligations for one recipient are not completed work, total shipyard demand, or a pooled conversion of Navy budget-request dollars.",
    },
    {
        "chart_id": "rights-readiness",
        "theme": "governance-and-rights",
        "subtheme": "publication-permission",
        "concept": "local evidence and accountable ownership before rights sign-off",
        "title": "Rights review readiness by source family",
        "chart_type": "readiness_matrix",
        "source_artifacts": ["rights-review-readiness.json", "rights-assignment-queue.json", "rights-evidence-register.json"],
        "visual_encoding": {"category": "source_family", "value": "observed_file_count", "status": "review_ready"},
        "required_visible_fields": ["local_evidence_status", "rights_status", "owner_status", "publisher_dependence"],
        "status_field": "status",
        "boundary": "Readiness is not legal clearance or redistribution permission.",
    },
    {
        "chart_id": "open-gate-workload",
        "theme": "operating-model",
        "subtheme": "review-workload-and-continuity",
        "concept": "what prevents promotion or company testing",
        "title": "Open gates and review workload",
        "chart_type": "priority_bubble",
        "source_artifacts": ["open-gate-register.json", "open-gate-history.json"],
        "visual_encoding": {"category": "gate_id", "value": "open_count", "size": "priority", "series": "snapshot_date"},
        "required_visible_fields": ["owner", "status", "acceptance", "priority"],
        "status_field": "status",
        "boundary": "Workload is not evidence that a gate is closed; unresolved critical work stays visible.",
    },
]


def main() -> int:
    required = {"theme", "subtheme", "concept", "title", "chart_type", "source_artifacts", "visual_encoding", "required_visible_fields", "boundary"}
    for chart in CHARTS:
        missing = sorted(required - chart.keys())
        if missing:
            raise ValueError(f"{chart['chart_id']} missing {missing}")
        for artifact in chart["source_artifacts"]:
            if not (ANALYSIS / artifact).exists():
                raise FileNotFoundError(ANALYSIS / artifact)
    payload = {
        "schema": "external-trend-intelligence.observatory-chart-catalog.v1",
        "status": "frontend_chart_contract_registered",
        "chart_count": len(CHARTS),
        "charts": CHARTS,
        "required_chart_metadata": ["theme", "subtheme", "concept", "period", "unit", "geography", "scope_or_denominator", "uncertainty", "counter_signal", "evidence_boundary", "company_gate"],
        "boundary": "The catalog specifies rendering and caveat requirements; it does not create evidence, grant rights, qualify a trend, or authorize an internal company bridge.",
        "next_action": "Implement these chart contracts in the frontend and keep source artifacts synchronized through the release manifest.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(CHARTS)} charts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
