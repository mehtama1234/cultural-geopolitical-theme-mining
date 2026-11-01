#!/usr/bin/env python3
"""Map the required enterprise domains to observed external theme evidence."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "domain-coverage-audit.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


DOMAIN_THEME_MAP = {
    "cultural": ["trust_identity_meaning", "political_judgment_action", "platforms_data_attention"],
    "social": ["care_health_reproduction", "unequal_exposure_status", "consumer_power_recourse"],
    "geopolitical": ["geopolitical_state_consequences", "infrastructure_technology_dependency"],
    "financial": ["household_room_consumption", "firm_sector_market_power", "time_hidden_price"],
    "industry": ["firm_sector_market_power", "infrastructure_technology_dependency"],
    "workforce": ["work_control_bargaining", "time_hidden_price", "unequal_exposure_status"],
    "technology": ["platforms_data_attention", "infrastructure_technology_dependency", "trust_identity_meaning"],
    "infrastructure": ["infrastructure_technology_dependency", "housing_place_mobility", "public_systems_feedback"],
    "market": ["firm_sector_market_power", "consumer_power_recourse", "household_room_consumption"],
}


def main() -> int:
    manifest = load("observation-manifest.json")
    records = manifest["records"]
    domains = {}
    for domain, themes in DOMAIN_THEME_MAP.items():
        matched = [record for record in records if set(record["program_theme_ids"]).intersection(themes)]
        hosts = sorted({host for record in matched for host in record["source_hosts"]})
        urls = sorted({url for record in matched for url in record.get("source_urls", [])})
        domains[domain] = {
            "mapped_themes": themes,
            "record_count": len(matched),
            "observation_count": sum(record["observation_count"] for record in matched),
            "source_host_count": len(hosts),
            "source_hosts_sample": hosts[:25],
            "unique_source_url_count": len(urls),
            "coverage_status": "observed" if matched else "missing",
            "quality_boundary": "Domain coverage means an external record is mapped to at least one theme. It does not prove independent publishers, comparability, rights, persistence, or a qualified trend.",
        }
    missing = [domain for domain, row in domains.items() if row["coverage_status"] == "missing"]
    payload = {
        "schema": "external-trend-intelligence.domain-coverage-audit.v1",
        "status": "required_domain_coverage_visible_quality_unresolved" if missing else "required_domain_coverage_observed_quality_unresolved",
        "required_domain_count": len(DOMAIN_THEME_MAP),
        "observed_domain_count": len(DOMAIN_THEME_MAP) - len(missing),
        "missing_domains": missing,
        "domains": domains,
        "boundary": "This audit makes the requested enterprise scope visible in the external inventory. It is not evidence that every domain has an independent, comparable, rights-cleared, persistent, or decision-ready trend.",
        "next_action": "Review domain-to-theme assignments and route sparse or dependent domains through the lineage, rights, independence, and qualification gates before using them for company decisions.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(domains)} domains; {len(missing)} missing)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
