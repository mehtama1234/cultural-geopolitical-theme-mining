#!/usr/bin/env python3
"""Search pinned records for repeated measures that may be comparable."""

from __future__ import annotations

import json
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "compatible-measure-search.json"


def load_at_head(relative: str) -> dict | None:
    try:
        raw = subprocess.check_output(["git", "show", f"HEAD:{relative}"], cwd=ROOT, text=True)
        value = json.loads(raw)
        return value if isinstance(value, dict) else None
    except (subprocess.CalledProcessError, json.JSONDecodeError, UnicodeDecodeError):
        return None


def main() -> int:
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    scanned = 0
    for item in manifest["records"]:
        record = load_at_head(item["record_path"])
        if not record:
            continue
        scanned += 1
        hosts = set()
        for observation in record.get("observations", []):
            urls = [observation.get("source_url", ""), *observation.get("source_urls", [])]
            hosts.update(urlparse(url).netloc.lower() for url in urls if isinstance(url, str) and url.startswith("http"))
            for measure, value in (observation.get("measures") or {}).items():
                if not isinstance(value, dict) or not value.get("unit"):
                    continue
                groups[(measure, value["unit"])].append(
                    {
                        "record_id": record.get("trend_id"),
                        "title": record.get("title"),
                        "geography": record.get("geography"),
                        "period": observation.get("period"),
                        "value": value.get("value"),
                        "hosts": sorted(hosts),
                    }
                )

    rows = []
    for (measure, unit), observations in sorted(groups.items()):
        record_ids = sorted({row["record_id"] for row in observations})
        hosts = sorted({host for row in observations for host in row["hosts"]})
        if len(record_ids) < 2 or len(hosts) < 2:
            continue
        rows.append(
            {
                "measure": measure,
                "unit": unit,
                "record_count": len(record_ids),
                "record_ids": record_ids,
                "source_host_count": len(hosts),
                "source_hosts": hosts,
                "observations": observations,
                "status": "candidate_compatibility_review",
                "boundary": "Matching a measure key and unit is only a discovery filter; population, denominator, geography, period, method, uncertainty, publisher dependence, and rights still require review.",
            }
        )
    report = {
        "schema": "external-trend-intelligence.compatible-measure-search.v1",
        "source_manifest": "observation-manifest.json",
        "record_count_in_manifest": manifest["record_count"],
        "record_count_scanned_at_pinned_head": scanned,
        "measure_group_count": len(groups),
        "candidate_compatibility_group_count": len(rows),
        "rows": rows,
        "status": "candidates_found_pending_review" if rows else "no_cross_host_measure_pairs_found",
        "next_action": "For each candidate group, reconcile population, denominator, geography, period, method, uncertainty, rights, and publisher dependence before any comparison or promotion.",
        "boundary": "This search is a discovery aid, not an independence score, pooled estimate, backtest, trend qualification, or company finding.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidate groups; scanned {scanned} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
