#!/usr/bin/env python3
"""Audit reproduction of the published SHED emergency-expense point estimate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "shed-point-estimate-reproduction-audit.json"


def main() -> int:
    payload = {
        "schema": "external-trend-intelligence.reproduction-audit.v1",
        "source": "Federal Reserve SHED 2024 public-use CSV",
        "period": "2024",
        "published_chart_measure": "adults who would cover a $400 emergency expense using cash or its equivalent",
        "published_chart_value_percent": 63,
        "microdata": {
            "url": "https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2024_%28CSV%29.zip",
            "artifact": "SHED_public_use_data_2024_(CSV).zip",
            "artifact_sha256": "sha256:b455d02356a0c01a02d7f478c02d772515491564e905ce13db55f272f83567c1",
            "csv_member": "public2024.csv",
            "row_count": 12295,
            "weight_field": "weight",
        },
        "reconstructions": [
            {"rule": "EF3_c == Yes (cash/checking/savings only)", "unweighted_percent": 43.65, "weighted_percent": 42.5493},
            {"rule": "EF3_a == Yes OR EF3_c == Yes (credit card paid in full or cash)", "unweighted_percent": 73.91, "weighted_percent": 71.2942},
        ],
        "status": "reproduction_mismatch_hold",
        "interpretation": "The published 63% cannot be reproduced from the obvious EF3 response combinations with the public 2024 weight using the current codebook interpretation. The chart construction, denominator, recode, or response universe requires source-owner clarification before treating the microdata as a validated estimate.",
        "missing_inputs": [
            "publisher chart construction or analysis code",
            "exact response recode and denominator universe",
            "design-based variance method",
        ],
        "next_test": "Reconcile the chart CSV, codebook, and microdata using the publisher's exact recode; retain the mismatch as a falsifier until the point estimate reproduces.",
        "boundary": "This audit does not replace the publisher estimate and does not authorize a recalculated trend, interval, pooling, or company decision.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
