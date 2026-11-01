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
        {
            "period": "2021",
            "source_id": "cms-nj-spa-21-0012",
            "source_url": "https://www.medicaid.gov/medicaid/spa/downloads/NJ-21-0012.pdf",
            "measure": "new_jersey_adult_medical_day_care_per_diem",
            "value": 86.10,
            "unit": "US dollars per adult service day",
            "uncertainty": "State-specific approved per-diem rate; applies to adult medical day care/ADHS and is not a national adult-day-services rate.",
        },
        {
            "period": "2025",
            "source_id": "cms-nj-spa-25-0009",
            "source_url": "https://www.medicaid.gov/medicaid/spa/downloads/NJ-25-0009.pdf",
            "measure": "new_jersey_adult_medical_day_care_per_diem",
            "value": 94.66,
            "unit": "US dollars per adult service day",
            "uncertainty": "State-specific approved per-diem rate effective July 16, 2025; applies to adult medical day care/ADHS and is not a national adult-day-services rate.",
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
        "new_jersey_adult_medical_day_care_per_diem_percent_change_2021_to_2025": pct_change(by_measure["new_jersey_adult_medical_day_care_per_diem"]["2021"], by_measure["new_jersey_adult_medical_day_care_per_diem"]["2025"]),
    }
    outcome_acquisition_plan = {
        "status": "targeted_public_source_identified_pending_extraction",
        "target_outcome": "state-level adult-day service supply, attendance, authorization, or utilization measure with a comparable 2022-to-2025 frame",
        "source_targets": [
            {
                "publisher": "CDC/NCHS NPALS",
                "artifact": "2025 NPALS web tables and weighted national/state estimates",
                "url": "https://www.cdc.gov/nchs/npals/study-cycles/2025.html",
                "access_boundary": "public tables and normalized metadata; do not redistribute restricted microdata",
            },
            {
                "publisher": "CDC/NCHS NPALS",
                "artifact": "2022 Adult Day Services Center public-use files and methodology",
                "url": "https://www.cdc.gov/nchs/npals/index.html",
                "access_boundary": "public-use aggregate or de-identified file only; preserve survey weights and methodology",
            },
            {
                "publisher": "CMS / Medicaid",
                "artifact": "state Medicaid managed-care and HCBS access/utilization context",
                "url": "https://data.medicaid.gov/",
                "access_boundary": "contextual state policy or access measures; do not label as adult-day utilization without an explicit service definition",
            },
        ],
        "required_fields": [
            "state_or_geography",
            "provider_or_participant_universe",
            "measure_definition",
            "period",
            "denominator",
            "estimate",
            "standard_error_or_confidence_interval",
            "survey_frame_or_claims_frame",
            "source_revision",
            "rights_basis",
        ],
        "acceptance_criteria": [
            "same adult-day service definition is available for at least two periods",
            "state or national denominator and provider/user universe are explicit",
            "2022 and 2025 survey-frame changes are recorded rather than pooled silently",
            "uncertainty and reliability flags are retained",
            "an independent outcome or utilization measure is linked without treating policy rate as utilization",
        ],
        "stop_rule": "Do not promote the IBIS finding or run an internal bridge if the public tables do not provide a comparable denominator, period, uncertainty treatment, and service definition; restricted-data access requires a separate approved rights and privacy review.",
        "next_action": "Extract the 2025 web-table state/national fields and reconcile them with the 2022 public-use frame before adding any derived utilization claim.",
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
        "interpretation": "The CDC series documents a larger national adult-day service footprint in 2025 than the 2022 estimate, while CMS records a New Jersey adult medical day-care per-diem increase from $86.10 in 2021 to $94.66 effective July 16, 2025. These measures support a bounded capacity-and-payer mechanism comparison but do not show that compliance caused the changes.",
        "independence_status": "partial_cross_publisher_temporal_mechanism_comparison",
        "outcome_status": "dated_outcomes_and_independent_policy_measure_present",
        "backtest_status": "bounded_cross_publisher_mechanism_comparison",
        "rights_review": {
            "cdc_2022": {
                "status": "government_public_domain_with_citation",
                "boundary": "CDC states the 2022 report material is public domain; retain citation and source link, and keep normalized values tied to the official report.",
            },
            "cdc_2025": {
                "status": "government_source_metadata_only",
                "boundary": "Retain normalized values, standard errors, citation, and official PDF link; do not redistribute the full source tables through this board.",
            },
            "cms_new_jersey_spas": {
                "status": "official_policy_document_metadata_only",
                "boundary": "Retain the approved rate, effective date, citation, and official PDF link; do not redistribute the full approval documents through this board.",
            },
            "release_decision": "normalized_values_and_citations_only",
        },
        "counter_signal": "Growth in centers and participants does not prove improved access, margins, staffing, or service quality; 2022 and 2025 survey frames and definitions must be reconciled before treating changes as a structural trend.",
        "falsifier": "After frame and definition reconciliation, the capacity and payer measures do not move in the hypothesized direction or independent state-level outcomes contradict the national pattern.",
        "next_action": "Add state-level attendance, authorization, or claims utilization and reconcile 2022 versus 2025 NPALS frames before using this lane in qualification.",
        "outcome_acquisition_plan": outcome_acquisition_plan,
        "boundary": "This bounded review covers one IBIS industry and one CDC source family. It does not validate the full IBIS finding, establish causal compliance effects, or authorize an internal company bridge.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(observations)} observations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
