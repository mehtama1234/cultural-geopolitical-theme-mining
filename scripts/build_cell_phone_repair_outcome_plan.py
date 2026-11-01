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
