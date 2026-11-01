#!/usr/bin/env python3
"""Build an independence and lineage review for the bounded forecast comparison."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "forecast-lineage-review.json"


def main() -> int:
    comparison = json.loads((ANALYSIS / "global-growth-forecast-comparison.json").read_text())
    by_record = {}
    measures = defaultdict(list)
    for forecast in comparison["forecasts"]:
        for value in forecast["values"]:
            host = value["source_hosts"][0] if value["source_hosts"] else None
            by_record[value["record_id"]] = {
                "record_id": value["record_id"],
                "source_family": host,
                "source_host": host,
                "title": value["title"],
                "forecast_period": value["period"],
                "publication_date": None,
                "vintage_status": "not_present_in_comparison_artifact",
                "rights_status": "not_verified",
                "publisher_dependence": "requires_source-level_review",
            }
            measures[forecast["measure"]].append(value["record_id"])
    hosts = [row["source_host"] for row in by_record.values() if row["source_host"]]
    shared_host_count = sum(1 for host in set(hosts) if hosts.count(host) > 1)
    report = {
        "schema": "external-trend-intelligence.forecast-lineage-review.v1",
        "comparison_artifact": "global-growth-forecast-comparison.json",
        "status": "publisher_distinct_pending_vintage_rights_and_outcome_review",
        "record_count": len(by_record),
        "source_host_count": len(set(hosts)),
        "shared_host_count": shared_host_count,
        "rows": list(by_record.values()),
        "measure_record_map": dict(measures),
        "independence_checks": {
            "distinct_publisher_hosts": len(set(hosts)) == 3,
            "same_host_duplicate_count": shared_host_count,
            "common_model_or_input_review": "pending",
            "forecast_vintage_review": "pending",
            "uncertainty_interval_review": "pending",
            "rights_review": "pending",
            "realized_outcome_backtest": "pending",
        },
        "next_action": "Attach publication date, forecast vintage, scenario or interval metadata, source terms, and the realized outcome to each row without collapsing revisions.",
        "boundary": "Distinct publisher hosts are a lineage signal, not proof of independent models or forecast accuracy. This artifact does not endorse a forecast or authorize company exposure.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(by_record)} forecast records; {len(set(hosts))} hosts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
