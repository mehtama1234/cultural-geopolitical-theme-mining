#!/usr/bin/env python3
"""Pin official Navy budget context for the IBIS dry-dock/defense claim."""

from __future__ import annotations

import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "ibis-dock-defense-outcome-review.json"
URLS = {
    "maintenance_budget": "https://www.secnav.navy.mil/fmc/fmb/Documents/26pres/OMN_Book.pdf",
    "ship_production_schedule": "https://www.secnav.navy.mil/fmc/fmb/Documents/26pres/SCN_Book.pdf",
}


def retrieve(url: str) -> tuple[str, str]:
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            body = response.read()
        return "official_source_available", "sha256:" + hashlib.sha256(body).hexdigest()
    except Exception as error:
        return f"official_source_check_failed:{type(error).__name__}", "not_available"


def main() -> int:
    checked_at = datetime.now(timezone.utc).isoformat()
    availability = {}
    for name, url in URLS.items():
        status, digest = retrieve(url)
        availability[name] = {"url": url, "status": status, "sha256": digest}
    payload = {
        "schema": "external-trend-intelligence.ibis-dock-defense-outcome-review.v1",
        "review_id": "ibis-independence::dry-docks-and-cargo-inspection-services-in-the-us::dock-defense",
        "industry_slug": "dry-docks-and-cargo-inspection-services-in-the-us",
        "claim_id": "dock-defense",
        "review_status": "official_context_acquired_scope_review_pending",
        "publisher": "U.S. Department of the Navy",
        "retrieved_at": checked_at,
        "source_artifacts": availability,
        "observations": [
            {"period": "FY2026", "measure": "ship_maintenance_program_change", "value": 1900000000, "unit": "US dollars increase over PB2025 request", "geography": "United States Navy", "uncertainty": "Budget request context; not realized obligation or completed maintenance output."},
            {"period": "FY2026", "measure": "ship_maintenance_requirement_funded", "value": 97, "unit": "percent of total requirement", "geography": "United States Navy", "uncertainty": "Budget request percentage; not an outcome of delivery, utilization, or contractor revenue."},
            {"period": "FY2026", "measure": "cno_maintenance_availabilities_supported", "value": 57, "unit": "planned availabilities", "geography": "public and private sectors", "uncertainty": "Planned program count; execution and completion are not observed here."},
            {"period": "FY2026", "measure": "private_sector_opn_availabilities", "value": 27, "unit": "planned availabilities", "geography": "US Pacific Fleet and Fleet Forces Command", "uncertainty": "Planned Other Procurement, Navy investment; not a realized dry-dock utilization measure."},
        ],
        "interpretation": "The official FY2026 Navy budget context documents planned maintenance funding and availability workload relevant to the dry-dock/defense claim. It is an external demand and policy context signal, not proof of contract awards, berth utilization, inspection volume, or company performance.",
        "independence_status": "publisher_distinct_official_budget_context_lineage_review_pending",
        "rights_boundary": "Retain normalized observations, source URLs, retrieval time, hashes, and attribution. Do not redistribute the source PDFs or imply that metadata retention clears downstream commercial reuse without exact-artifact review.",
        "counter_signal": "Budgeted workload can be delayed, reprogrammed, or executed by different facilities; planned availabilities do not establish realized demand or capacity utilization.",
        "falsifier": "Subsequent execution records show no corresponding awards, availabilities, or maintenance workload, or the budget context is not comparable to the IBIS claim's unit and period.",
        "release_decision": "retain_normalized_official_context_only",
        "next_action": "Use NAVY-EXECUTION-DATA-REQUEST.md to acquire an official execution or award series with compatible period, geography, and outcome definition before treating this as independent confirmation or promoting the IBIS claim.",
        "boundary": "This artifact is a bounded official context acquisition. It does not validate the IBIS finding, establish causal defense demand, clear rights, or authorize an internal company bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(payload['observations'])} observations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
