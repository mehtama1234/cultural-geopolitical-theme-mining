#!/usr/bin/env python3
"""Measure host overlap in the external record inventory.

Host overlap is a lineage warning, not proof of publisher identity or
dependence. It is intentionally kept separate from trend qualification.
"""

from __future__ import annotations

import collections
import itertools
import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "record-host-dependence-audit.json"


def main() -> int:
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    host_records: dict[str, set[str]] = collections.defaultdict(set)
    host_themes: dict[str, set[str]] = collections.defaultdict(set)
    pair_counts: collections.Counter[tuple[str, str]] = collections.Counter()
    for record in manifest["records"]:
        hosts = sorted(set(record.get("source_hosts", [])))
        for host in hosts:
            host_records[host].add(record["record_path"])
            host_themes[host].update(record.get("program_theme_ids", []))
        pair_counts.update(itertools.combinations(hosts, 2))
    hosts = [
        {
            "host": host,
            "record_count": len(host_records[host]),
            "theme_count": len(host_themes[host]),
            "themes": sorted(host_themes[host]),
        }
        for host in sorted(host_records, key=lambda item: (-len(host_records[item]), item))
    ]
    shared_hosts = [row for row in hosts if row["record_count"] > 1]
    shared_pairs = [
        {"host_a": a, "host_b": b, "record_count": count}
        for (a, b), count in pair_counts.most_common(100)
    ]
    payload = {
        "schema": "external-trend-intelligence.record-host-dependence-audit.v1",
        "status": "host_overlap_visible_independence_unverified",
        "record_count": manifest["record_count"],
        "unique_host_count": len(hosts),
        "shared_host_count": len(shared_hosts),
        "shared_host_record_count": sum(row["record_count"] for row in shared_hosts),
        "host_rows": hosts[:100],
        "host_row_limit": 100,
        "shared_host_pairs": shared_pairs,
        "shared_host_pair_limit": 100,
        "boundary": "A shared host can represent one publisher, multiple publishers, a distributor, or a common upstream dataset. Host diversity and overlap are lineage diagnostics only; they do not prove independent confirmation or clear rights.",
        "next_action": "Review high-volume shared hosts and source ownership at artifact level before treating cross-record or cross-theme repetition as independent evidence.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(hosts)} hosts; {len(shared_hosts)} shared)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
