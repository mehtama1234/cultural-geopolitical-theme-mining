#!/usr/bin/env python3
"""Materialize the TY2025 extension to the Prince William fiscal series."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-prince-william-data-center-fiscal-revenue-2025-extension",
        "title": "Prince William data-center tax revenue reached a reported $465.9 million in TY2025",
        "theme_ids": ["cost", "voice", "energy"],
        "program_theme_ids": ["infrastructure_technology_dependency", "firm_sector_market_power", "housing_place_mobility", "public_systems_feedback", "geopolitical_state_consequences"],
        "source_unit": "Prince William County data-center industry aggregate",
        "geography": "Prince William County, Virginia, United States",
        "observations": [{
            "period": "Tax Year 2025",
            "denominator": {"value": 1, "unit": "Prince William County data-center industry aggregate", "value_type": "reported_aggregate"},
            "measures": {
                "data_center_tax_revenue": {"value": 465.9, "unit": "USD millions", "value_type": "reported_total"},
                "year_over_year_growth": {"value": 59, "unit": "percent", "value_type": "reported_rate"},
                "real_property_tax_revenue": {"value": 221.8, "unit": "USD millions", "value_type": "reported_total"},
                "computer_equipment_tax_revenue": {"value": 218.1, "unit": "USD millions", "value_type": "reported_total"},
                "furniture_fixtures_tax_revenue": {"value": 23.3, "unit": "USD millions", "value_type": "reported_total"},
                "fees_licensing_revenue": {"value": 2.7, "unit": "USD millions", "value_type": "reported_total"},
                "computer_equipment_tax_rate": {"value": 4.15, "unit": "USD per $100 assessed value", "value_type": "reported_rate"},
                "new_data_center_capacity": {"value": 621, "unit": "MW", "value_type": "reported_addition"},
                "turnkey_total_power_capacity": {"value": 1483, "unit": "MW", "value_type": "reported_total"},
                "turnkey_powered_shell_data_center_count": {"value": 55, "unit": "facilities", "value_type": "reported_total"}
            },
            "method": "Transcribed from Table 8 and the executive-summary/category text in the county-linked TY2025 Data Center Revenue Report. The report is hosted as a Flipsnack publication linked from the county Finance and Revenue page; its signed reader data was retrieved and hashed for reproducibility.",
            "uncertainty": "County-reported aggregate; TY2025 is a tax-year report and is not a household incidence estimate. Revenue growth combines assessed-base expansion, equipment cycles, classification, and the computer-equipment rate increase from $3.70 in TY2024 to $4.15 in TY2025. The report does not establish net public benefit, service-cost recovery, household bills, or environmental burden.",
            "subgroup": "Data-center industry aggregate; revenue categories, capacity, facility count, and tax-rate policy are retained as separate measures.",
            "counterinterpretation": "The 59% increase may reflect both physical expansion and tax policy; it cannot be interpreted as a pure demand, productivity, or local-welfare effect.",
            "source_url": "https://www.flipsnack.com/B8877D99E8C/2025-data-center-revenue-report.html",
            "retrieval_hash": "sha256:8e0d9f0df4f618d973a01a16849504770a84a3a22497b0b284166f2fbf79ec62",
            "status": "reported"
        }],
        "related_sources": [
            {"source_url": "https://www.pwcva.gov/department/finance/finance-and-revenue", "claim": "The county Finance and Revenue page links the TY2025 report.", "status": "official-index"},
            {"source_url": "../../records/us-prince-william-data-center-fiscal-revenue-2012-2024.json", "claim": "Prior county-reported series through TY2024; 2025 is kept as a separate extension because the source report changed.", "status": "context"}
        ],
        "boundary": "This is a reported TY2025 local fiscal and capacity observation. It extends the pipeline/operation-to-public-revenue arrow while leaving utility cost allocation, household incidence, public-service cost, jobs/wages, water, environmental burden, legitimacy, and geopolitical leverage open. The signed reader artifact is not itself a county PDF, and no value is inferred from the 2024 series."
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "observations": 1}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
