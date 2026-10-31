#!/usr/bin/env python3
"""Summarize stage coverage without pooling unlike cross-publisher cases."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "cross-publisher-stage-comparison.json"


def main() -> int:
    panel = json.loads((ANALYSIS / "cross-publisher-stage-panel.json").read_text())
    by_publisher = defaultdict(list)
    for case in panel["cases"]:
        by_publisher[case["publisher_family"]].append(case)
    stage_summary = {}
    for publisher, cases in by_publisher.items():
        stage_summary[publisher] = {
            stage: {
                "observed_case_count": sum(item["stages"][stage]["status"] == "observed" for item in cases),
                "not_observed_case_count": sum(item["stages"][stage]["status"] != "observed" for item in cases),
                "case_count": len(cases),
            }
            for stage in panel["stage_definitions"]
        }
    report = {
        "schema": "external-trend-intelligence.cross-publisher-stage-comparison.v1",
        "panel": panel["subset_id"],
        "status": "descriptive_stage_coverage_only",
        "case_count": panel["case_count"],
        "publisher_case_counts": {publisher: len(cases) for publisher, cases in by_publisher.items()},
        "stage_coverage_by_publisher": stage_summary,
        "supports": ["stage-definition review", "missing-outcome visibility", "holdout design"],
        "does_not_support": ["pooled rates", "publisher-independent confirmation", "causal effect", "population prevalence", "company exposure"],
        "blocking_items": ["case types and denominators differ", "periods and legal processes differ", "no pre-specified independent holdout", "public non-observation is not a negative outcome"],
        "next_action": "Pre-specify a non-case-based holdout with compatible population, period, and outcome definitions before any trend promotion.",
        "boundary": "This is a descriptive coverage comparison. It counts observed stage evidence by publisher but never treats missing public evidence as failure or pools unlike cases.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
