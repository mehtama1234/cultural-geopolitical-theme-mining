#!/usr/bin/env python3
"""Record what can and cannot be estimated for SHED uncertainty from public artifacts."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "shed-emergency-expense-uncertainty-audit.json"


def main() -> int:
    diagnostics = [
        {"period": "2023", "point_estimate_percent": 63.3169, "effective_sample_size": 9367.2646, "lower_percent": 62.3409, "upper_percent": 64.2928},
        {"period": "2024", "point_estimate_percent": 62.7365, "effective_sample_size": 10337.9478, "lower_percent": 61.8044, "upper_percent": 63.6686},
    ]
    payload = {
        "schema": "external-trend-intelligence.uncertainty-audit.v1",
        "measure": "SHED $400 emergency expense covered completely with cash or equivalent",
        "period": "2024",
        "point_estimate_percent": 63,
        "public_sample_size": {"2023": 11400, "2024": 12295},
        "public_weight_documented": "weight (main qualified respondents, scaled to sample size)",
        "source_urls": [
            "https://www.federalreserve.gov/consumerscommunities/files/SHED_2024codebook.pdf",
            "https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2024_%28CSV%29.zip",
            "https://www.federalreserve.gov/publications/files/2024-report-economic-well-being-us-households-202505.pdf",
            "https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-description.htm",
        ],
        "official_uncertainty_search": {
            "report_interval_text_found": False,
            "codebook_replicate_weight_text_found": False,
            "basis": "The official report publishes point estimates and the codebook documents analysis weights, but neither artifact provides a design-based interval or replicate-weight procedure for this measure.",
            "latest_report_context": {
                "report_period": "2025",
                "field_period": "October 17-28, 2025",
                "final_report_sample_count": 12934,
                "reported_overall_design_effect": 1.14,
                "scope_boundary": "The overall survey design effect is retained as context only; it is not substituted for a measure-specific variance estimate.",
            },
        },
        "official_significance_statement": {
            "status": "publisher_interpretation_preserved",
            "source_url": "https://www.federalreserve.gov/publications/files/2024-report-economic-well-being-us-households-202505.pdf",
            "locator": "pages 44-45, Figure 20 and surrounding text",
            "statement": "The Federal Reserve reports that 63 percent of adults would cover a hypothetical $400 expense with cash or its equivalent in 2024, unchanged from 2022 and 2023; the cash-equivalent definition includes cash, savings, or a credit card paid off at the next statement.",
            "boundary": "This is the publisher's descriptive interpretation, not a reproducible design-based interval or a cross-source significance test.",
        },
        "naive_srs_interval": {
            "status": "diagnostic_only_not_release_valid",
            "confidence_level": 0.95,
            "method": "weighted Bernoulli approximation using effective sample size (sum of weights squared divided by sum of squared weights)",
            "diagnostics": diagnostics,
        },
        "design_based_status": "not_estimable_from_current_pinned_artifacts",
        "missing_inputs": [
            "replicate weights or variance estimation instructions sufficient to reproduce design-based standard errors",
            "year-specific interval attached to the published chart series",
        ],
        "release_decision": "hold",
        "next_test": "Acquire and pin the public-use microdata plus official variance/replicate-weight instructions, then reproduce the published point estimate and design-based interval for at least two years.",
        "boundary": "The naive interval is a diagnostic sanity check only. It must not be used for cross-source significance, pooling, trend qualification, or company decisions.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
