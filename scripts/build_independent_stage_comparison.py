#!/usr/bin/env python3
"""Register an independent-source mechanism comparison without pooling unlike units."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "independent-stage-comparison.json"

RECORD_IDS = [
    "comparative-asean-gsma-consumer-scam-2026-resolution-recovery-digital-trust",
    "bsa43-nhs-waiting-legitimacy-2026",
]
STAGE_KEYS = {
    "formal_response": ["victims_reporting", "policy_feedback", "legitimacy_route"],
    "implementation_gap": ["reported_cases_unresolved", "waiting_as_hidden_price", "quality_access_split"],
    "recovery_or_trust": ["money_losing_victims_recovered_none", "money_losing_victims_recovered_all", "channel_trust_effect", "provider_switching"],
}


def main() -> int:
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())["records"]
    rows = []
    for record_id in RECORD_IDS:
        record = snapshot[record_id]["record"]
        measures = {}
        for observation in record.get("observations", []):
            for name, value in observation.get("measures", {}).items():
                measures[name] = {"value": value.get("value"), "unit": value.get("unit"), "period": observation.get("period")}
        stages = {stage: {key: measures[key] for key in keys if key in measures} for stage, keys in STAGE_KEYS.items()}
        urls = sorted({obs.get("source_url") for obs in record.get("observations", []) if obs.get("source_url", "").startswith("http")})
        rows.append({"record_id": record_id, "geography": record["geography"], "source_unit": record["source_unit"], "source_hosts": sorted({urlparse(url).netloc for url in urls}), "stages": stages})
    report = {
        "schema": "external-trend-intelligence.independent-stage-comparison.v1",
        "status": "mechanism_comparison_only",
        "record_count": len(rows),
        "records": rows,
        "independent_source_families": ["GSMA", "National Centre for Social Research / British Social Attitudes"],
        "supports": ["independent mechanism challenge", "counter-signal design", "candidate outcome vocabulary"],
        "does_not_support": ["pooled prevalence", "common-unit effect estimate", "formal-response causal claim", "company exposure"],
        "blocking_items": ["different populations and geographies", "survey definitions and periods differ", "no common denominator or holdout", "publisher/study lineage still needs review"],
        "next_action": "Use the shared unresolved/recovery/trust vocabulary to acquire a genuinely comparable repeated measure before any backtest or promotion.",
        "boundary": "Independent publishers can challenge a mechanism without making unlike survey and case measures numerically comparable.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
