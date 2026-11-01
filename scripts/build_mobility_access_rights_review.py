#!/usr/bin/env python3
"""Record conservative rights and retention boundaries for the mobility comparison."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "mobility-access-rights-review.json"


def main() -> int:
    rows = [
        {
            "source_family": "2024 ACS 1-year PUMS",
            "publisher": "U.S. Census Bureau",
            "source_urls": ["https://www2.census.gov/programs-surveys/acs/data/pums/2024/1-Year/csv_hus.zip", "https://www2.census.gov/programs-surveys/acs/data/pums/2024/1-Year/csv_pus.zip"],
            "terms_urls": ["https://www.census.gov/about/policies/privacy.html"],
            "rights_status": "official_policy_identified_exact_artifact_review_open",
            "permitted_scope": "Retain source locator, hash, normalized values, and attributed internal-review calculations; do not assume the exact PUMS product notice clears downstream republication.",
            "not_cleared": "Public-facing redistribution of source files or derived charts, commercial reuse, and any microdata export remain unapproved.",
            "next_action": "Record the exact PUMS product notice and attribution language before publishing a derived mobility chart.",
        },
        {
            "source_family": "2022 National Household Travel Survey",
            "publisher": "Federal Highway Administration / ORNL",
            "source_urls": ["https://nhts.ornl.gov/media/2022/download/csv.zip"],
            "terms_urls": ["https://nhts.ornl.gov/"],
            "rights_status": "access_route_identified_exact_artifact_review_open",
            "permitted_scope": "Retain citation metadata, retrieval hash, normalized aggregate slices, and internal review notes; do not redistribute the raw archive or assume derived-chart rights.",
            "not_cleared": "Raw archive redistribution, commercial reuse, and public derived charts remain unapproved until the exact archive terms are documented.",
            "next_action": "Capture the archive's exact terms, citation, and retention requirements for the 2022 download.",
        },
    ]
    report = {
        "schema": "external-trend-intelligence.mobility-access-rights-review.v1",
        "candidate_id": "candidate-time-financial-pressure-practical-room",
        "reviewed_on": date.today().isoformat(),
        "source_count": len(rows),
        "rows": rows,
        "release_decision": "retain_attributed_metadata_and_internal_review_only; do_not_redistribute_or_connect_company_data_until_rights_owner_approves",
        "boundary": "This is an operational rights register, not legal advice or a license grant. Exact product and archive terms remain controlling.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} sources; release held)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
