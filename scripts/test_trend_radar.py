#!/usr/bin/env python3
"""Validate that the trend radar is derived from the current evidence manifest."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"


def main() -> int:
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    radar = json.loads((ANALYSIS / "trend-radar.json").read_text())
    summary = json.loads((ANALYSIS / "trend-finding-summary.json").read_text())
    counts = Counter()
    hosts = {}
    for record in manifest["records"]:
        for theme in record.get("program_theme_ids", []):
            counts[theme] += 1
            hosts.setdefault(theme, set()).update(record.get("source_hosts", []))
    assert radar["schema"] == "external-trend-intelligence.trend-radar.v1"
    assert radar["record_count"] == manifest["record_count"]
    assert radar["theme_count"] == len(counts) == len(radar["themes"])
    assert radar["qualified_findings"] == summary["qualified_monitored_count"]
    assert radar["held_hypotheses"] == summary["held_hypothesis_count"]
    for row in radar["themes"]:
        assert row["record_count"] == counts[row["theme"]]
        assert row["source_host_count"] == len(hosts[row["theme"]])
        assert row["signal_strength"] in {"high", "medium", "emerging"}
    assert "not a trend-qualification score" in radar["boundary"]
    print("trend radar contract: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
