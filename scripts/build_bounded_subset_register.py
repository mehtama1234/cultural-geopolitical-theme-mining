#!/usr/bin/env python3
"""Register bounded subsets that are useful for review without overstating comparability."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "bounded-subset-register.json"


def main() -> int:
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())["records"]
    panel_ids = [
        "au-al-hussein-reactivation-deemed-work-2025",
        "au-fwc-khan-platform-repeat-deactivation-2026",
        "au-mansoor-platform-alternative-earnings-remedy-2025",
    ]
    panel = []
    for record_id in panel_ids:
        record = snapshot[record_id]["record"]
        panel.append({
            "record_id": record_id,
            "source_path": snapshot[record_id]["record_path"],
            "geography": record["geography"],
            "source_unit": record["source_unit"],
            "periods": [obs.get("period") for obs in record.get("observations", [])],
            "source_urls": sorted({obs.get("source_url") for obs in record.get("observations", []) if obs.get("source_url")}),
        })
    report = {
        "schema": "external-trend-intelligence.bounded-subset-register.v1",
        "subsets": [
            {
                "subset_id": "australia-platform-remedy-case-panel-001",
                "candidate_id": "candidate-formal-response-before-recovery",
                "status": "bounded_panel_not_backtest",
                "record_ids": panel_ids,
                "common_frame": "Australia; adjudicated platform-worker remedy cases; case-level stages",
                "panel": panel,
                "supports": ["stage coding", "formal-response-to-recovery pathway review", "falsifier design"],
                "does_not_support": ["population prevalence", "independent-source confirmation", "causal effect", "company exposure"],
                "blocking_gates": ["shared Fair Work Commission publisher lineage", "incomplete payment/receipt and durable-access outcomes", "no independent holdout source family"],
                "next_action": "Code common response, implementation, receipt, recovery, and exit stages; then add an independent non-FWC source family before any trend promotion.",
            }
        ],
        "boundary": "A bounded subset narrows the comparison frame; it does not make shared-publisher cases independent or turn missing outcomes into zeros.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(panel)} panel records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
