#!/usr/bin/env python3
"""Build candidate-specific rights evidence for the financial-room lane."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "financial-room-rights-review.json"


def main() -> int:
    rows = [
        {
            "record_id": "comparative-abs-general-social-survey-2025-cultural-participation-financial-stress-connection",
            "publisher": "Australian Bureau of Statistics",
            "terms_urls": ["https://www.abs.gov.au/website-privacy-copyright-and-disclaimer", "https://www.abs.gov.au/about/legislation-and-policy/purchasing-data/abs-conditions-sale"],
            "rights_status": "attribution_route_identified_exact_product_license_open",
            "observed_boundary": "ABS website material is generally CC BY 4.0 unless an exception or product-specific notice applies; third-party material, microdata, logos, and products without a displayed licence require separate review.",
            "permitted_scope": "Retain citation metadata and normalized values for internal review with ABS attribution; do not assume redistribution or commercial derivative rights without checking the exact product notice.",
            "next_action": "Pin the exact GSS table or workbook licence notice and record the attribution text before publishing a derived chart.",
        },
        {
            "record_id": "aihw-hilda-financial-stress-2001-2023",
            "publisher": "Australian Institute of Health and Welfare / HILDA",
            "terms_urls": ["https://www.aihw.gov.au/copyright"],
            "rights_status": "attribution_route_identified_hilda_underlying_license_open",
            "observed_boundary": "AIHW describes CC BY 4.0 attribution for eligible material, with source-specific notices taking precedence; HILDA underlying data and custom analysis terms remain separate review items.",
            "permitted_scope": "Retain normalized metadata and a bounded internal comparison with AIHW attribution; do not redistribute HILDA microdata or assume the summary grants rights to underlying data.",
            "next_action": "Confirm the HILDA/AIHW product notice and any underlying-data restrictions for the exact reported measures.",
        },
        {
            "record_id": "anupoll-financial-stress-2020-2025",
            "publisher": "Australian National University / ANUPoll / Australian Data Archive",
            "terms_urls": ["https://dataverse.ada.edu.au/dataverse/anupoll", "https://polis.cass.anu.edu.au/research/surveys/anupoll/contact-us"],
            "rights_status": "archive_access_and_license_review_required",
            "observed_boundary": "ANUPoll is distributed through an archive and the public summary identifies the survey lineage; archive access, citation, and reuse terms must be checked for the exact dataset or summary.",
            "permitted_scope": "Retain citation metadata and normalized reported endpoints for internal mechanism review; no raw-data redistribution or commercial downstream use is assumed.",
            "next_action": "Capture the archive record's licence, access class, and citation requirements for the exact ANUPoll wave.",
        },
        {
            "record_id": "comparative-anz-roy-morgan-australian-consumer-confidence-september-29-2026-financial-outlook",
            "publisher": "ANZ / Roy Morgan",
            "terms_urls": ["https://www.roymorgan.com/terms-of-use"],
            "rights_status": "restrictive_republication_review_open",
            "observed_boundary": "Roy Morgan terms warn that unauthorized use of services or products may create copyright exposure and that third-party content can carry additional terms.",
            "permitted_scope": "Retain citation, URL, hash, and normalized metadata for internal review only; do not republish the report or derived chart without permission review.",
            "next_action": "Confirm permission or a licensed derived-use basis before exposing any Roy Morgan-derived chart outside the review workspace.",
        },
        {
            "record_id": "federal-reserve-shed-financial-room-2013-2025",
            "publisher": "Board of Governors of the Federal Reserve System",
            "terms_urls": ["https://www.federalreserve.gov/disclaimer.htm", "https://www.federalreserve.gov/policies.htm"],
            "rights_status": "official_policy_identified_exact_artifact_review_open",
            "observed_boundary": "Board material is generally public domain with attribution unless otherwise indicated; non-Board and exact-artifact restrictions remain open.",
            "permitted_scope": "Attributed normalized values and internal review notes only until exact chart, public-use file, and non-Board material scope is recorded.",
            "next_action": "Complete the existing Federal Reserve artifact-level review before downstream publication.",
        },
        {
            "record_id": "comparative-usda-food-security-2022-2024",
            "publisher": "USDA Economic Research Service",
            "terms_urls": ["https://www.ers.usda.gov/developer/api-terms-of-service", "https://www.ers.usda.gov/about-ers/policies-and-standards/data-product-quality/ers-data-product-quality-standards"],
            "rights_status": "conditional_attribution_use_exact_publication_review_open",
            "observed_boundary": "The ERS API terms support attributed API use, but the exact publication and statistical supplement remain subject to separate reuse review.",
            "permitted_scope": "Attributed normalized estimates and internal review only; no raw publication redistribution or company connection before rights-owner review.",
            "next_action": "Resolve exact publication reuse and preserve the required ERS non-endorsement notice.",
        },
        {
            "record_id": "comparative-jpmorgan-household-liquidity-2023",
            "publisher": "JPMorganChase Institute",
            "terms_urls": ["https://www.jpmorganchase.com/institute/all-topics/financial-health-wealth-creation/how-vulnerable-are-americans-to-unexpected-expenses"],
            "rights_status": "restrictive_republication_notice_review_open",
            "observed_boundary": "The snapshot carries a written republication restriction and the public chart is not a machine-readable numeric series.",
            "permitted_scope": "Citation, hash, and normalized metadata for internal mechanism review only.",
            "next_action": "Confirm permission for any derived chart or downstream company use before release.",
        },
    ]
    payload = {
        "schema": "external-trend-intelligence.financial-room-rights-review.v1",
        "candidate_id": "candidate-time-financial-pressure-practical-room",
        "reviewed_on": date.today().isoformat(),
        "source_count": len(rows),
        "rows": rows,
        "release_decision": "retain_attributed_metadata_and_internal_mechanism_review_only; do_not_redistribute_upstream_content_or_connect_company_data_until_each_source_rights_boundary_is_reviewed",
        "boundary": "This is an operational rights-evidence register, not legal advice, a license grant, or a finding that any source is cleared for commercial reuse.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
