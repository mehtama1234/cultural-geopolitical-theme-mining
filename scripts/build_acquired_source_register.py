#!/usr/bin/env python3
"""Create a source-specific register for datasets actually acquired by the observatory."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "acquired-source-register.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    ora = load("open-repair-alliance-mobile-snapshot.json")
    cbp = load("census-repair-industry-snapshot.json")
    nes = load("census-nonemployer-repair-snapshot.json")
    npals = load("npals-public-table-extract.json")
    shed = load("federal-reserve-shed-financial-room-2013-2025.json")
    community = load("usda-community-food-assistance-2024.json")
    rows = [
        {
            "source_id": ora["acquisition_id"],
            "publisher": ora["source"]["publisher"],
            "dataset": ora["source"]["dataset"],
            "artifact": "open-repair-alliance-mobile-snapshot.json",
            "source_url": ora["source"]["download_url"],
            "retrieved_at": ora["retrieved_at"],
            "revision_or_release": ora["source"]["reported_release_scope"],
            "checksum": ora["source"]["artifact_sha256"],
            "license_or_terms": ora["source"]["license"],
            "access_status": "acquired",
            "population_and_unit": ora["units"]["record"],
            "geography_and_period": "country-level global and USA rows; events through July 2026",
            "publisher_dependence": "single_publisher_community_event_series",
            "interpretation_status": ora["status"],
            "rights_boundary": ora["rights_basis"],
            "next_review": ora["next_action"],
        },
        {
            "source_id": cbp["acquisition_id"],
            "publisher": cbp["source"]["publisher"],
            "dataset": cbp["source"]["dataset"],
            "artifact": "census-repair-industry-snapshot.json",
            "source_url": cbp["source"]["documentation_url"],
            "retrieved_at": cbp["retrieved_at"],
            "revision_or_release": "County Business Patterns 2019-2023",
            "checksum": "multiple_download_checksums_preserved_in_artifact",
            "license_or_terms": cbp["rights_basis"],
            "access_status": "acquired",
            "population_and_unit": cbp["units"]["establishments"],
            "geography_and_period": "US national and state; 2019-2023",
            "publisher_dependence": "single_publisher_census_series",
            "interpretation_status": cbp["status"],
            "rights_boundary": cbp["rights_basis"],
            "next_review": cbp["next_action"],
        },
        {
            "source_id": nes["acquisition_id"],
            "publisher": nes["source"]["publisher"],
            "dataset": nes["source"]["dataset"],
            "artifact": "census-nonemployer-repair-snapshot.json",
            "source_url": nes["source"]["dataset_url"],
            "retrieved_at": nes["retrieved_at"],
            "revision_or_release": "Nonemployer Statistics 2019-2024",
            "checksum": "multiple_download_checksums_preserved_in_artifact",
            "license_or_terms": nes["rights_basis"],
            "access_status": "acquired",
            "population_and_unit": nes["units"]["establishments"],
            "geography_and_period": "US national and state; 2019-2024",
            "publisher_dependence": "single_publisher_census_series",
            "interpretation_status": nes["status"],
            "rights_boundary": nes["rights_basis"],
            "next_review": nes["next_action"],
        },
        {
            "source_id": npals["source_id"],
            "publisher": "CDC/NCHS",
            "dataset": "NPALS public biennial overview API extract",
            "artifact": "npals-public-table-extract.json",
            "source_url": npals["source_url"],
            "retrieved_at": npals["retrieved_at"],
            "revision_or_release": "2020 state frame and 2022/2025 national rows",
            "checksum": npals["normalized_rows_sha256"],
            "license_or_terms": npals["rights_boundary"],
            "access_status": npals["retrieval_status"],
            "population_and_unit": "provider, capacity, and people-served rows with CDC table definitions",
            "geography_and_period": "52 2020 geographies in frame; 44 numeric geographies; national 2022/2025",
            "publisher_dependence": "single_publisher_government_survey_series",
            "interpretation_status": "definition_reconciliation_counter_signal",
            "rights_boundary": npals["rights_boundary"],
            "next_review": npals["next_action"],
        },
        {
            "source_id": shed["acquisition_id"],
            "publisher": shed["publisher"],
            "dataset": "Survey of Household Economics and Decisionmaking financial-room series",
            "artifact": "federal-reserve-shed-financial-room-2013-2025.json",
            "source_url": shed["source_urls"][0],
            "retrieved_at": shed["retrieval"]["retrieved_at"],
            "revision_or_release": "SHED 2013-2025 annual repeated cross-sections",
            "checksum": shed["retrieval"]["artifact_sha256"],
            "license_or_terms": shed["rights_boundary"],
            "access_status": shed["status"],
            "population_and_unit": f"{shed['population']}; {shed['unit']}",
            "geography_and_period": shed["geography"],
            "publisher_dependence": "single_publisher_government_survey_series",
            "interpretation_status": shed["status"],
            "rights_boundary": shed["rights_boundary"],
            "next_review": "Complete uncertainty and exact-artifact rights review before derived-chart redistribution.",
        },
        {
            "source_id": "usda-community-food-assistance-2024-ap126",
            "publisher": community["publisher"],
            "dataset": community["dataset"],
            "artifact": "usda-community-food-assistance-2024.json",
            "source_url": community["source_url"],
            "retrieved_at": community["retrieved_at"],
            "revision_or_release": "AP-126; December 2024 CPS Food Security Supplement",
            "checksum": community["source_checksum"],
            "license_or_terms": community["rights_boundary"],
            "access_status": community["availability_check"]["availability"],
            "population_and_unit": community["population_and_unit"],
            "geography_and_period": "United States; 12 months ending December 2024",
            "publisher_dependence": "single_publisher_government_survey_series",
            "interpretation_status": "household_community_food_use_context_not_provider_capacity",
            "rights_boundary": community["rights_boundary"],
            "next_review": community["next_action"],
        },
    ]
    payload = {
        "schema": "external-trend-intelligence.acquired-source-register.v1",
        "status": "acquired_sources_registered_with_lineage_and_boundaries",
        "source_count": len(rows),
        "required_fields": ["source_id", "publisher", "dataset", "artifact", "source_url", "retrieved_at", "revision_or_release", "checksum", "license_or_terms", "access_status", "population_and_unit", "geography_and_period", "publisher_dependence", "interpretation_status", "rights_boundary", "next_review"],
        "sources": rows,
        "boundary": "This register covers acquired artifacts only. It supplements, but does not replace, the 118-source discovery registry; it is not legal clearance, independence proof, or permission to pool unlike populations.",
        "next_action": "Add each newly acquired external artifact here during refresh and route unresolved rights, lineage, and comparability issues to the relevant review queue.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} acquired sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
