#!/usr/bin/env python3
"""Build a bounded IBIS outcome review for adult day services."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "ibis-adult-day-outcome-review.json"


def pct_change(old: float, new: float) -> float:
    return round((new - old) / old * 100, 1)


def main() -> int:
    observations = [
        {
            "period": "2022",
            "source_id": "cdc-npals-adsc-2022",
            "source_url": "https://www.cdc.gov/nchs/data/hestat/adultday/adult-day-2022.htm",
            "measure": "adult_day_services_centers",
            "value": 3100,
            "unit": "estimated centers",
            "uncertainty": "National estimate from 389 eligible centers weighted to approximately 3,000 centers; source reports reliability standards.",
        },
        {
            "period": "2022",
            "source_id": "cdc-npals-adsc-2022-participants",
            "source_url": "https://www.cdc.gov/nchs/products/databriefs/db502.htm",
            "measure": "enrolled_participants",
            "value": 182000,
            "unit": "estimated enrolled participants",
            "uncertainty": "Rounded national estimate; participant characteristics use complex survey weights and variable-specific missingness.",
        },
        {
            "period": "2022",
            "source_id": "cdc-npals-adsc-2022-operating-status",
            "source_url": "https://www.cdc.gov/nchs/data/hestat/adultday/adult-day-2022.htm",
            "measure": "onsite_only_share",
            "value": 72.9,
            "unit": "percent of centers",
            "uncertainty": "Weighted estimate; 2022 operating-status categories combine onsite/offsite service modes.",
        },
        {
            "period": "2025",
            "source_id": "cdc-npals-adsc-2025-weighted-estimates",
            "source_url": "https://www.cdc.gov/nchs/data/npals/2025/2025-NPALS-ADSC-weighted-estimates.pdf",
            "measure": "adult_day_services_centers",
            "value": 4448,
            "unit": "weighted centers",
            "uncertainty": "Weighted national estimate; standard-error tables are published in the source PDF; 2025 data are restricted at microdata level.",
        },
        {
            "period": "2025",
            "source_id": "cdc-npals-adsc-2025-weighted-estimates",
            "source_url": "https://www.cdc.gov/nchs/data/npals/2025/2025-NPALS-ADSC-weighted-estimates.pdf",
            "measure": "enrolled_participants",
            "value": 227169,
            "unit": "weighted enrolled participants",
            "uncertainty": "Weighted national estimate; standard error 5,434.11 in the source table.",
            "standard_error": 5434.11,
        },
        {
            "period": "2025",
            "source_id": "cdc-npals-adsc-2025-weighted-estimates",
            "source_url": "https://www.cdc.gov/nchs/data/npals/2025/2025-NPALS-ADSC-weighted-estimates.pdf",
            "measure": "average_daily_attendance",
            "value": 157535,
            "unit": "weighted average daily participants",
            "uncertainty": "Weighted estimate; standard error 4,359.33; missing cases excluded.",
            "standard_error": 4359.33,
        },
        {
            "period": "2025",
            "source_id": "cdc-npals-adsc-2025-weighted-estimates",
            "source_url": "https://www.cdc.gov/nchs/data/npals/2025/2025-NPALS-ADSC-weighted-estimates.pdf",
            "measure": "maximum_allowed_capacity",
            "value": 262917,
            "unit": "weighted maximum participant capacity",
            "uncertainty": "Weighted estimate; standard error 5,227.99; missing cases excluded.",
            "standard_error": 5227.99,
        },
        {
            "period": "2025",
            "source_id": "cdc-npals-adsc-2025-weighted-estimates",
            "source_url": "https://www.cdc.gov/nchs/data/npals/2025/2025-NPALS-ADSC-weighted-estimates.pdf",
            "measure": "medicaid_authorized_or_set_up_share",
            "value": 75.9,
            "unit": "percent of centers",
            "uncertainty": "Weighted estimate; standard error 0.97; includes Medicaid state plan, waiver, managed care, or PACE participation.",
            "standard_error": 0.97,
        },
    ]
    by_measure = {}
    for row in observations:
        by_measure.setdefault(row["measure"], {})[row["period"]] = row["value"]
    changes = {
        "adult_day_services_centers_percent_change_2022_to_2025": pct_change(by_measure["adult_day_services_centers"]["2022"], by_measure["adult_day_services_centers"]["2025"]),
        "enrolled_participants_percent_change_2022_to_2025": pct_change(by_measure["enrolled_participants"]["2022"], by_measure["enrolled_participants"]["2025"]),
        "2025_average_daily_attendance_to_enrollment_percent": round(by_measure["average_daily_attendance"]["2025"] / by_measure["enrolled_participants"]["2025"] * 100, 1),
        "2025_average_daily_attendance_to_capacity_percent": round(by_measure["average_daily_attendance"]["2025"] / by_measure["maximum_allowed_capacity"]["2025"] * 100, 1),
    }
    report = {
        "schema": "external-trend-intelligence.ibis-adult-day-outcome-review.v1",
        "finding_slug": "compliance-as-economic-architecture",
        "industry_slug": "adult-day-care",
        "review_status": "bounded_temporal_outcome_review",
        "ibis_claim_ids": ["adc-model", "adc-population"],
        "ibis_claim_boundary": "IBIS describes adult-day capacity as constrained by payer authorization, attendance, documentation, staffing, and transportation; the industry record does not itself establish an outcome series.",
        "observations": observations,
        "derived_changes": changes,
        "interpretation": "The CDC series documents a larger national adult-day service footprint in 2025 than the 2022 estimate and supplies payer, attendance, and capacity measures that can test the capacity mechanism. The measures are descriptive and do not show that compliance caused the changes.",
        "independence_status": "same_publisher_temporal_series",
        "outcome_status": "dated_outcome_measures_present",
        "backtest_status": "descriptive_temporal_comparison_only",
        "counter_signal": "Growth in centers and participants does not prove improved access, margins, staffing, or service quality; 2022 and 2025 survey frames and definitions must be reconciled before treating changes as a structural trend.",
        "falsifier": "After frame and definition reconciliation, the capacity and payer measures do not move in the hypothesized direction or independent state-level outcomes contradict the national pattern.",
        "next_action": "Add an independent state Medicaid authorization/rate or service-utilization series and reconcile 2022 versus 2025 NPALS frames before using this lane in qualification.",
        "boundary": "This bounded review covers one IBIS industry and one CDC source family. It does not validate the full IBIS finding, establish causal compliance effects, or authorize an internal company bridge.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(observations)} observations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
