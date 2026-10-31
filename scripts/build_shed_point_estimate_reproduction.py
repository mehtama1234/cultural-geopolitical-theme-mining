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
        "source": "Federal Reserve SHED public-use CSV",
        "periods": ["2023", "2024"],
        "published_chart_measure": "adults who would cover a $400 emergency expense using cash or its equivalent",
        "published_chart_value_percent": 63,
        "microdata": [
            {"period": "2023", "url": "https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2023_%28CSV%29.zip", "artifact": "SHED_public_use_data_2023_(CSV).zip", "artifact_sha256": "sha256:8467284631ad649037b7d5e4a535db1b15cfdbc45c3dba14bc21188ed11efb08", "csv_member": "public2023.csv", "row_count": 11400, "weight_field": "weight"},
            {"period": "2024", "url": "https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2024_%28CSV%29.zip", "artifact": "SHED_public_use_data_2024_(CSV).zip", "artifact_sha256": "sha256:b455d02356a0c01a02d7f478c02d772515491564e905ce13db55f272f83567c1", "csv_member": "public2024.csv", "row_count": 12295, "weight_field": "weight"},
        ],
        "reconstructions": [
            {"period": "2023", "rule": "publisher-derived pay_casheqv == Yes", "unweighted_percent": 65.64, "weighted_percent": 63.3169, "published_rounding": "63%"},
            {"period": "2024", "rule": "publisher-derived pay_casheqv == Yes", "unweighted_percent": 65.92, "weighted_percent": 62.7365, "published_rounding": "63%"},
            {"rule": "EF3_c == Yes (cash/checking/savings only)", "unweighted_percent": 43.65, "weighted_percent": 42.5493},
            {"rule": "EF3_a == Yes OR EF3_c == Yes (credit card paid in full or cash)", "unweighted_percent": 73.91, "weighted_percent": 71.2942},
        ],
        "status": "point_estimate_reproduced_variance_open",
        "interpretation": "The published 63% reproduces when the public-use publisher-derived pay_casheqv field is weighted with the main weight and rounded to a whole percent. The obvious EF3 component recodes do not match, so the derived field and its construction are retained as the authoritative lineage path.",
        "missing_inputs": [
            "design-based variance method",
            "replicate weights or equivalent variance instructions",
        ],
        "next_test": "Attach design-based standard errors for both reproduced years before cross-source significance or promotion.",
        "boundary": "Point-estimate reproduction does not establish uncertainty, causality, trend qualification, pooling, or company relevance.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
