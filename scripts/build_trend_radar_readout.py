#!/usr/bin/env python3
"""Render the current evidence-bound trend radar as analyst-readable Markdown."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "TREND-RADAR-READOUT.md"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def main() -> int:
    radar = load("trend-radar.json")
    findings = load("trend-finding-summary.json")
    lines = [
        "# External trend radar readout",
        "",
        f"As of {radar['as_of']}: {radar['record_count']:,} indexed records across {radar['theme_count']} themes.",
        "",
        "This is a prioritization readout, not a claim that evidence volume proves a trend.",
        "",
        "## Current findings",
        "",
    ]
    for finding in findings["findings"]:
        lines.extend([
            f"### {finding['title']}",
            "",
            f"Status: **{finding['status'].replace('_', ' ')}** ({finding['passed_gate_count']}/{finding['gate_count']} gates passed).",
            f"Evidence: {finding['evidence_record_count']} records across {finding['source_host_count']} source hosts.",
            f"Next test: {finding['next_action']}",
            f"Falsifier: {finding['falsifier']}",
            "",
        ])
    lines.extend(["## Highest-density themes", "", "| Theme | Records | Source hosts | Signal label |", "|---|---:|---:|---|"])
    for theme in radar["themes"][:10]:
        lines.append(f"| {theme['theme']} | {theme['record_count']:,} | {theme['source_host_count']:,} | {theme['signal_strength']} |")
    lines.extend(["", "## Boundary", "", radar["boundary"], ""])
    OUTPUT.write_text("\n".join(lines))
    print(f"wrote {OUTPUT} ({len(lines)} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
