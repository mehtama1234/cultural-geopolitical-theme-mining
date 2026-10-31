#!/usr/bin/env python3
"""Review pinned candidate records for comparable periods, units, geography, and outcomes."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "backtest-comparability-review.json"

OUTCOME_TERMS = ("payment", "receipt", "recovery", "access", "trust", "participation", "completion", "reliability", "acceptance", "control", "exit", "retention")


def main() -> int:
    snapshot = json.loads((ANALYSIS / "backtest-source-snapshot.json").read_text())["records"]
    candidates = json.loads((ANALYSIS / "candidate-comparisons.json").read_text())["candidates"]
    rows = []
    for candidate in candidates:
        records = [snapshot[record_id]["record"] for record_id in candidate["evidence_record_ids"] if record_id in snapshot]
        periods = sorted({obs.get("period", "") for record in records for obs in record.get("observations", []) if obs.get("period")})
        geographies = sorted({record.get("geography", "") for record in records if record.get("geography")})
        denominator_units = sorted({obs.get("denominator", {}).get("unit", "") for record in records for obs in record.get("observations", []) if obs.get("denominator", {}).get("unit")})
        measure_units = sorted({measure.get("unit", "") for record in records for obs in record.get("observations", []) for measure in obs.get("measures", {}).values() if measure.get("unit")})
        measure_names = sorted({name for record in records for obs in record.get("observations", []) for name in obs.get("measures", {})})
        outcome_measures = [name for name in measure_names if any(term in name.lower() for term in OUTCOME_TERMS)]
        flags = {
            "periods_present": bool(periods),
            "geographies_present": bool(geographies),
            "single_geography": len(geographies) == 1,
            "single_denominator_unit": len(denominator_units) == 1,
            "single_measure_unit": len(measure_units) == 1,
            "outcome_measure_present": bool(outcome_measures),
        }
        blocking = [name for name, passed in flags.items() if not passed]
        if len(geographies) > 1:
            blocking.append("geography_harmonization")
        if len(denominator_units) > 1:
            blocking.append("denominator_harmonization")
        if len(measure_units) > 1:
            blocking.append("measure_unit_harmonization")
        rows.append({
            "candidate_id": candidate["id"],
            "record_count": len(records),
            "periods": periods,
            "geographies": geographies,
            "denominator_units": denominator_units,
            "measure_units": measure_units,
            "outcome_measures": outcome_measures,
            "flags": flags,
            "status": "comparable_subset_candidate" if not blocking else "harmonization_required",
            "blocking_items": sorted(set(blocking)),
            "next_action": "Define a common unit, population, geography, and period before selecting a holdout window." if blocking else "Select a holdout period and run the pre-specified backtest.",
        })
    report = {
        "schema": "external-trend-intelligence.backtest-comparability-review.v1",
        "candidate_count": len(rows),
        "comparable_subset_candidate_count": sum(row["status"] == "comparable_subset_candidate" for row in rows),
        "harmonization_required_count": sum(row["status"] == "harmonization_required" for row in rows),
        "rows": rows,
        "boundary": "This is a structural comparability review, not a statistical backtest or causal estimate. Presence of an outcome-named field does not establish valid measurement.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
