#!/usr/bin/env python3
"""Build a bounded outcome-acquisition plan for the IBIS cell-repair claim."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "cell-phone-repair-outcome-acquisition-plan.json"
ITU_PATH = "analysis/records/comparative-itu-global-e-waste-monitor-2024-digital-circularity-material-recovery.json"
FTC_PATH = "analysis/findings/us-right-to-repair-household-cost-matched-evidence-001.md"


def git_blob(path: str) -> tuple[str, str]:
    text = subprocess.check_output(["git", "show", f"HEAD:{path}"], cwd=ROOT, text=True)
    blob = subprocess.check_output(["git", "rev-parse", f"HEAD:{path}"], cwd=ROOT, text=True).strip()
    return text, blob


def main() -> int:
    itu_text, itu_blob = git_blob(ITU_PATH)
    itu = json.loads(itu_text)
    ftc_text, ftc_blob = git_blob(FTC_PATH)
    plan = {
        "schema": "external-trend-intelligence.cell-phone-repair-outcome-acquisition-plan.v1",
        "candidate_id": "candidate-compliance-as-economic-architecture-cell-phone-repair",
        "finding_slug": "compliance-as-economic-architecture",
        "industry_slug": "cell-phone-repair",
        "claim_id": "repair-policy",
        "status": "held_outcome_acquisition_ready",
        "claim": "New York and Colorado materials illustrate rising state-level consumer access and right-to-repair policy for electronics.",
        "current_disposition": "held_outcome_missing",
        "observed_proxy_artifact": "census-repair-industry-snapshot.json",
        "observed_proxy_status": "descriptive_industry_proxy_not_phone_outcome",
        "pinned_context": {
            "state_policy_sources": [
                {
                    "publisher": "New York Attorney General",
                    "url": "https://ag.ny.gov/press-release/2024/attorney-general-james-reminds-consumers-its-easier-ever-get-electronics",
                    "role": "state policy/consumer-access context",
                    "period": "2024 source page; effective date requires verification",
                },
                {
                    "publisher": "Colorado General Assembly",
                    "url": "https://www.leg.colorado.gov/bills/hb24-1121",
                    "role": "state legislation context",
                    "period": "HB24-1121; enactment/effective date requires verification",
                },
            ],
            "repair_barrier_context": {
                "publisher": "Federal Trade Commission",
                "role": "US repair-restriction and warranty mechanism context; not a phone outcome series",
                "source_revision": ftc_blob,
                "source_sha256": "sha256:" + hashlib.sha256(ftc_text.encode()).hexdigest(),
                "linked_sources": [
                    "https://www.ftc.gov/system/files/documents/reports/nixing-fix-ftc-report-congress-repair-restrictions/nixing_the_fix_report_final_5521_630pm-508_002.pdf",
                    "https://www.ftc.gov/news-events/news/press-releases/2024/07/ftc-warns-companies-stop-warranty-practices-harm-consumers-right-repair",
                ],
            },
            "global_circularity_counter_signal": {
                "publisher": "International Telecommunication Union / Global E-waste Monitor",
                "source_revision": itu_blob,
                "source_sha256": itu["reproduction_audit"]["source_url_sha256"],
                "period": "2022",
                "measures": {
                    "global_ewaste_generation_kg": 62000000000,
                    "formal_recovery_percent": 22.3,
                },
                "boundary": "Global aggregate e-waste and policy synthesis; not US phone repair volume, household replacement behavior, or causal policy evaluation.",
            },
        },
        "why_not_pooled": [
            "State policy sources describe legal access and implementation, not realized repair behavior.",
            "FTC evidence describes mechanisms and restrictions, not a representative phone-repair outcome panel.",
            "ITU e-waste measures are global and aggregate, with different denominators and geography.",
            "The three evidence lanes do not share a unit, population, period, or outcome definition that permits pooling.",
        ],
        "target_outcome": {
            "name": "US consumer electronics repair-access outcome panel",
            "minimum_period": "two comparable annual or quarterly periods before and after an explicitly dated policy change",
            "population": "US phone/device owners or repair transactions with a documented sampling or administrative frame",
            "required_measures": [
                "repair attempts and completed repairs",
                "repair versus replacement decision",
                "parts/tool/software access outcome",
                "quoted price and paid price",
                "days without device",
                "repeat failure or warranty return",
                "device age and geography",
                "denominator and missingness",
            ],
        },
        "source_targets": [
            {
                "publisher": "FTC or state consumer-protection agencies",
                "artifact": "complaints, enforcement, warranty, or repair-access records with dated denominators",
                "acceptance": "phone/electronics scope and period are explicit; do not substitute general legal text for an outcome",
            },
            {
                "publisher": "EPA or state e-waste programs",
                "artifact": "electronics collection/reuse/recycling series with device category and geography",
                "acceptance": "repair/reuse is separable from recycling and denominator is documented",
            },
            {
                "publisher": "independent repair transaction or consumer survey source",
                "artifact": "dated repair volume, price, time-to-repair, replacement, or device-life panel",
                "acceptance": "publisher, sampling frame, uncertainty, and rights are documented; vendor marketing alone is insufficient",
            },
        ],
        "source_screen_2026_10_31": [
            {
                "publisher": "U.S. Census Bureau",
                "artifact": "Nonemployer Statistics (NES), NAICS 811211/811213",
                "url": "https://www.census.gov/programs-surveys/nonemployer-statistics.html",
                "screen_status": "best_public_candidate",
                "what_it_can_support": "annual subnational establishments and receipts for consumer-electronics and communication-equipment repair categories",
                "limitation": "industry receipts are not phone-repair transactions, policy exposure, prices, or repair outcomes; NAICS mapping must be verified",
            },
            {
                "publisher": "U.S. Census Bureau",
                "artifact": "Annual Integrated Economic Survey, NAICS 811212",
                "url": "https://data.census.gov/table?codeset=naics~811212&g=010XX00US",
                "screen_status": "context_candidate",
                "what_it_can_support": "annual computer and office machine repair revenue/payroll context",
                "limitation": "not phone-specific and does not measure repair attempts, completion, price, or device life",
            },
            {
                "publisher": "U.S. EPA",
                "artifact": "Durable Goods: Product-Specific Data",
                "url": "https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/durable-goods-product-specific-data",
                "screen_status": "counter_signal_only",
                "what_it_can_support": "selected consumer-electronics generation and recycling context through 2018",
                "limitation": "includes phones with other electronics, ends in 2018, and measures end-of-life tonnage rather than repair or replacement behavior",
            },
            {
                "publisher": "U.S. EPA",
                "artifact": "Alternatives for Disposition of Electronics Planning Tool (ADEPT)",
                "url": "https://www.epa.gov/land-research/alternatives-disposition-electronics-planning-tool-adept",
                "screen_status": "modeled_candidate_not_observed_outcome",
                "what_it_can_support": "state-level modeled reuse, recycling, and disposal pathways",
                "limitation": "uses top-down data and bottom-up assumptions; not a direct repair transaction series or policy evaluation",
            },
            {
                "publisher": "U.S. Bureau of Labor Statistics",
                "artifact": "Employment and output by industry, NAICS 811200",
                "url": "https://www.bls.gov/emp/tables/industry-employment-and-output.htm",
                "screen_status": "labor_context_only",
                "what_it_can_support": "broad employment/output context for electronic and precision equipment repair",
                "limitation": "category is broader than phone repair and cannot establish consumer repair access or policy effect",
            },
            {
                "publisher": "Open Repair Alliance",
                "artifact": "Open Repair Alliance full open repair dataset, ORDS v0.3",
                "url": "https://openrepair.org/open-data/downloads/",
                "screen_status": "phone_specific_global_outcome_candidate_gated_download",
                "what_it_can_support": "row-level community repair attempts, device category, repair outcome, product age, barriers, event date, and geography; the current release includes more than 416,000 EEE records through July 2026",
                "rights_basis": "Open Repair Alliance states CC BY-SA 4.0; the download form requests contact/use information before issuing the dataset link",
                "limitation": "global community-repair events are not a representative US transaction panel; selection, event coverage, partner composition, and phone-category completeness must be assessed before any US policy comparison",
                "acquisition_next_step": "Complete the publisher download form, retain the issued URL and checksum, inspect ORDS v0.3 fields, and screen mobile-phone rows by country, event date, outcome, and missingness",
            },
        ],
        "observed_outcome_proxy_artifact": "open-repair-alliance-mobile-snapshot.json",
        "observed_outcome_proxy_status": "acquired_phone_specific_global_community_repair_proxy_not_policy_outcome",
        "required_fields": [
            "source_owner_and_rights_basis",
            "policy_effective_date_or_exposure_definition",
            "device_category_and_population",
            "geography",
            "period",
            "repair_or_replacement_measure",
            "unit_and_denominator",
            "uncertainty_or_missingness",
            "independent_publisher_lineage",
        ],
        "acceptance_criteria": [
            "at least one dated outcome measure is independent of the state-policy source",
            "the outcome has a compatible US device population and explicit denominator",
            "policy exposure and implementation dates are verified from primary records",
            "repair and recycling are not silently treated as the same outcome",
            "counter-signals and non-exposed or comparison geographies are retained",
        ],
        "stop_rule": "Do not promote the IBIS claim, pool the state/FTC/ITU evidence, or run an internal company bridge if no comparable outcome frame, uncertainty, rights basis, and independent lineage can be obtained.",
        "next_action": "Acquire one dated US repair/replacement outcome series and reconcile its device population and denominator to the verified New York and Colorado policy effective dates.",
        "boundary": "This plan advances acquisition and comparison design; it is not evidence that right-to-repair policy increased repair volume or reduced e-waste.",
    }
    OUTPUT.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({plan['status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
