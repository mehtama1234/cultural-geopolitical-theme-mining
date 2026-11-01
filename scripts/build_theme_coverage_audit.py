#!/usr/bin/env python3
"""Audit breadth of observed program themes without treating volume as validity."""

from __future__ import annotations

import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "theme-coverage-audit.json"


def main() -> int:
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    rows = {}
    for theme in sorted(manifest["program_theme_counts"]):
        records = [record for record in manifest["records"] if theme in record["program_theme_ids"]]
        hosts = sorted({host for record in records for host in record["source_hosts"]})
        source_urls = [url for record in records for url in record.get("source_urls", [])]
        unique_source_urls = sorted(set(source_urls))
        reused_source_url_count = len(source_urls) - len(unique_source_urls)
        statuses = collections.Counter(status for record in records for status in record["observation_statuses"])
        rows[theme] = {
            "record_count": len(records),
            "observation_count": sum(record["observation_count"] for record in records),
            "source_host_count": len(hosts),
            "source_hosts": hosts,
            "source_url_count": len(source_urls),
            "unique_source_url_count": len(unique_source_urls),
            "reused_source_url_count": reused_source_url_count,
            "source_url_reuse_ratio": round(reused_source_url_count / len(source_urls), 4) if source_urls else 0,
            "observation_status_counts": dict(sorted(statuses.items())),
            "coverage_status": "observed" if records else "missing",
            "quality_boundary": "Coverage indicates captured records and hosts only; it does not prove independence, comparability, rights, persistence, or trend qualification.",
        }
    sparse = [theme for theme, row in rows.items() if row["record_count"] < 10]
    payload = {
        "schema": "external-trend-intelligence.theme-coverage-audit.v1",
        "status": "theme_coverage_visible_quality_unresolved",
        "theme_count": len(rows),
        "observed_theme_count": sum(row["coverage_status"] == "observed" for row in rows.values()),
        "sparse_theme_count": len(sparse),
        "sparse_themes": sparse,
        "themes": rows,
        "boundary": "This audit checks breadth and repeated-URL pressure in the external observation inventory. A large record count, multiple hosts, or unique URLs is not independent confirmation and does not authorize company use.",
        "next_action": "Review sparse themes, repeated URLs, and source-family mapping during the next coverage review; preserve missing, dependent, and non-comparable evidence explicitly.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} themes; {len(sparse)} sparse)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
