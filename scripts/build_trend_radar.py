#!/usr/bin/env python3
"""Rank external themes by evidence volume and source-host diversity."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "trend-radar.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    manifest = load("observation-manifest.json")
    findings = load("trend-finding-summary.json")
    records = defaultdict(lambda: {"record_count": 0, "observation_count": 0, "hosts": set(), "statuses": set()})
    for record in manifest["records"]:
        for theme in record.get("program_theme_ids", []):
            row = records[theme]
            row["record_count"] += 1
            row["observation_count"] += record.get("observation_count", 0)
            row["hosts"].update(record.get("source_hosts", []))
            row["statuses"].update(record.get("observation_statuses", []))
    rows = []
    for theme, row in records.items():
        rows.append({
            "theme": theme,
            "record_count": row["record_count"],
            "observation_count": row["observation_count"],
            "source_host_count": len(row["hosts"]),
            "observation_statuses": sorted(row["statuses"]),
            "signal_strength": "high" if row["record_count"] >= 1000 and len(row["hosts"]) >= 20 else "medium" if row["record_count"] >= 400 else "emerging",
        })
    rows.sort(key=lambda row: (-row["record_count"], -row["source_host_count"], row["theme"]))
    payload = {
        "schema": "external-trend-intelligence.trend-radar.v1",
        "as_of": date.today().isoformat(),
        "theme_count": len(rows),
        "record_count": manifest["record_count"],
        "qualified_findings": findings["qualified_monitored_count"],
        "held_hypotheses": findings["held_hypothesis_count"],
        "themes": rows,
        "boundary": "This radar prioritizes external review by evidence volume and host diversity. It is not a trend-qualification score, causal estimate, or authorization for internal data use.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} themes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
