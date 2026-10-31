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
    n = 12295
    p = 0.63
    se = math.sqrt(p * (1 - p) / n)
    naive_margin = 1.96 * se
    payload = {
        "schema": "external-trend-intelligence.uncertainty-audit.v1",
        "measure": "SHED $400 emergency expense covered completely with cash or equivalent",
        "period": "2024",
        "point_estimate_percent": 63,
        "public_sample_size": n,
        "public_weight_documented": "weight (main qualified respondents, scaled to sample size)",
        "source_urls": [
            "https://www.federalreserve.gov/consumerscommunities/files/SHED_2024codebook.pdf",
            "https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2024_%28CSV%29.zip",
        ],
        "naive_srs_interval": {
            "status": "diagnostic_only_not_release_valid",
            "confidence_level": 0.95,
            "lower_percent": round((p - naive_margin) * 100, 3),
            "upper_percent": round((p + naive_margin) * 100, 3),
            "method": "unweighted binomial approximation using published sample size",
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
