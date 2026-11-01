#!/usr/bin/env python3
"""Pin rights and reuse boundaries for the monitored food-security sources."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "food-insecurity-rights-review.json"


def main() -> int:
    payload = {
        "schema": "external-trend-intelligence.food-insecurity-rights-review.v1",
        "candidate_id": "candidate-us-food-insecurity-persistence",
        "reviewed_on": date.today().isoformat(),
        "sources": [
            {
                "record_id": "comparative-usda-food-security-2022-2024",
                "publisher": "USDA Economic Research Service",
                "terms_url": "https://www.ers.usda.gov/developer/api-terms-of-service",
                "quality_standards_url": "https://www.ers.usda.gov/about-ers/policies-and-standards/data-product-quality/ers-data-product-quality-standards",
                "source_url": "https://www.ers.usda.gov/publications/113622",
                "rights_status": "conditional_attribution_use_documented",
                "terms_scope": "The cited API terms govern API content; the publication and statistical supplement remain subject to exact-artifact reuse review.",
                "observed_terms": "ERS API terms permit searching, displaying, analyzing, retrieving, viewing, and otherwise getting ERS API data, require a prominent non-endorsement notice, prohibit false representation, and reserve access limits and term changes. ERS quality standards describe public dissemination and documentation but are not a redistribution license.",
                "permitted_scope_for_this_observatory": "Store normalized values, source locator, retrieval hash, and derived internal-review calculations with ERS attribution and the required non-endorsement notice.",
                "not_cleared": "Raw publication reproduction, redistribution of source tables, and commercial downstream reuse outside the documented API route require separate review.",
                "publisher_dependence": "direct_official_publisher",
            },
            {
                "record_id": "us-urban-wbns-food-insecurity-persistence-2019-2025",
                "publisher": "Urban Institute",
                "terms_url": "https://www.urban.org/terms-service",
                "source_url": "https://www.urban.org/sites/default/files/2026-03/Food%20Insecurity%20Remained%20High%20in%202025%2C%20As%20Safety%20Net%20Cuts%20Loom%20.pdf",
                "rights_status": "permission_required_for_republication",
                "observed_terms": "Urban states that site content is copyrighted; reproduction, modification, distribution, display, derivative works, and non-personal storage are prohibited unless expressly authorized, and directs users to obtain written permission.",
                "permitted_scope_for_this_observatory": "Retain citation metadata, hashes, normalized values, and a non-republished internal review note; link to the official source.",
                "not_cleared": "Redistributing Urban tables, charts, PDF content, or derived public-facing charts is not cleared without permission.",
                "publisher_dependence": "direct_official_publisher",
            },
        ],
        "alternate_data_access_path": {
            "catalog_url": "https://datacatalog.urban.org/dataset/well-being-and-basic-needs-survey",
            "catalog_license_label": "odc-by",
            "catalog_granularity": "person",
            "catalog_public_access_level": "public",
            "catalog_context": "The Urban Data Catalog describes WBNS public-use files and links to ICPSR/RWJF access, while noting that restricted variables require a separate data-use agreement and institutional review process.",
            "rights_interpretation": "The catalog license and public-use path are not assumed to clear reuse of the specific 2025 report PDF, tables, charts, or a company-facing derivative. Exact file-level license and attribution requirements must be recorded before release.",
            "next_action": "Acquire the exact public-use file or table locator, retain its file hash and license notice, and obtain rights-owner confirmation for any company-facing derived chart.",
        },
        "release_decision": "retain_as_attributed_metadata_and_internal_review_only; do_not_redistribute_upstream_content_or_connect_company_data_until_rights_owner_approves",
        "boundary": "This is an operational rights review, not legal advice or a license grant. Terms can change and source-specific notices may add restrictions.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
