#!/usr/bin/env python3
"""Add reproducible coverage metrics to external trend candidates."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="analysis/external-trend-intelligence/observation-manifest.json")
    parser.add_argument("--candidates", default="analysis/external-trend-intelligence/candidate-comparisons.json")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text())
    payload = json.loads(Path(args.candidates).read_text())
    by_id = {record["trend_id"]: record for record in manifest["records"]}
    for candidate in payload["candidates"]:
        records = [by_id[record_id] for record_id in candidate["evidence_record_ids"]]
        hosts = Counter(host for record in records for host in record.get("source_hosts", []))
        themes = Counter(theme for record in records for theme in record.get("program_theme_ids", []))
        candidate["coverage"] = {
            "evidence_record_count": len(records),
            "source_host_count": len(hosts),
            "source_host_counts": dict(hosts.most_common()),
            "program_theme_counts": dict(themes.most_common()),
            "independence_status": "unverified",
            "interpretation": "Distinct hosts are discovery coverage, not proof of independent confirmation; publisher lineage and shared source material still require review."
        }
    output = Path(args.output or args.candidates)
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"enriched {len(payload['candidates'])} candidates; wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
