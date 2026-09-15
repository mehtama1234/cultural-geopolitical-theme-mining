#!/usr/bin/env python3
"""Materialize the Prince William County data-center fiscal time series.

Values are a transcription of Table 9 and the historical computer-equipment
tax-rate table in the county's 2024 Data Center Revenue Report. The script
keeps the source table as the authority instead of implying that a PDF parser
recovered every chart or footnote.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TOTAL_REVENUE = {
    2012: 6.5, 2013: 7.8, 2014: 11.7, 2015: 17.4, 2016: 22.9,
    2017: 27.9, 2018: 36.7, 2019: 53.2, 2020: 65.4, 2021: 85.9,
    2022: 110.8, 2023: 166.4, 2024: 293.7,
}
YOY = {2013: 21, 2014: 50, 2015: 48, 2016: 32, 2017: 22, 2018: 31,
       2019: 45, 2020: 23, 2021: 31, 2022: 29, 2023: 50, 2024: 77}
COMPUTER_RATE = {2013: 1.25, 2014: 1.25, 2015: 1.25, 2016: 1.25,
                 2017: 1.25, 2018: 1.25, 2019: 1.25, 2020: 1.35,
                 2021: 1.50, 2022: 1.65, 2023: 2.15, 2024: 3.70}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    observations = []
    for year in sorted(TOTAL_REVENUE):
        measures = {
            "data_center_tax_revenue": {"value": TOTAL_REVENUE[year], "unit": "USD millions", "value_type": "reported_total"},
        }
        if year in YOY:
            measures["year_over_year_growth"] = {"value": YOY[year], "unit": "percent", "value_type": "reported_rate"}
        if year in COMPUTER_RATE:
            measures["computer_equipment_tax_rate"] = {"value": COMPUTER_RATE[year], "unit": "USD per $100 assessed value", "value_type": "reported_rate"}
        observations.append({
            "period": f"Tax Year {year}",
            "denominator": {"value": 1, "unit": "Prince William County data-center industry aggregate", "value_type": "reported_aggregate"},
            "measures": measures,
            "method": "Transcribed from Table 9 (tax revenue contributions) and the historical computer-equipment tax-rate table in the official county TY2024 report.",
            "uncertainty": "County-reported aggregate; TY2024 is marked preliminary and recognized in FY2025. It is not a household incidence estimate. Historical values are not independently reconstructed from parcel or tax ledgers here.",
            "subgroup": "Data-center industry aggregate; revenue categories and tax-rate policy are retained as separate measures.",
            "counterinterpretation": "Revenue growth reflects development, assessed values, equipment cycles, tax-rate changes, and classification; it does not by itself establish net public benefit, household affordability, jobs, or environmental cost.",
            "source_url": "https://www.pwcva.gov/assets/2025-06/Prince%20William%20County%202024%20Data%20Center%20Revenue%20Report.pdf",
            "retrieval_hash": "sha256:ac77d43d5df548b834a67810123e90645bcf93dba5deb0dd6fd6bc8a570cd70c",
            "status": "reported",
        })
    output = {
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-prince-william-data-center-fiscal-revenue-2012-2024",
        "title": "Prince William data-center tax revenue rose sharply alongside a changing tax rate",
        "theme_ids": ["cost", "voice", "energy"],
        "program_theme_ids": ["infrastructure_technology_dependency", "firm_sector_market_power", "housing_place_mobility", "public_systems_feedback", "geopolitical_state_consequences"],
        "source_unit": "Prince William County data-center industry aggregate",
        "geography": "Prince William County, Virginia, United States",
        "observations": observations,
        "related_sources": [{"source_url": "../../projects/ai-work-control/prince-william-data-center-gis-incidence-layer-v1.md", "claim": "Local GIS pipeline and planning concentration supply physical context for the fiscal series.", "status": "context", "access_boundary": "GIS status and GFA are not tax revenue, load, or household incidence."}],
        "boundary": "This is a reported local fiscal-revenue time series. It strengthens the physical pipeline-to-public-revenue arrow, while leaving utility cost allocation, household bills, public-service cost, jobs/wages, water, environmental burden, legitimacy, and geopolitical leverage open. The 2024 value is preliminary and the 2020–2024 computer-equipment rate changes are an explicit confounder.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "observations": len(observations)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
