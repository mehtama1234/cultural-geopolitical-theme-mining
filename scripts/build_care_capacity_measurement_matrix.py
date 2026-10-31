#!/usr/bin/env python3
"""Extract comparable measurement metadata for the held care-capacity candidate."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "care-capacity-measurement-matrix.json"


def main() -> int:
    candidate = json.loads((ANALYSIS / "care-capacity-candidate.json").read_text())
    manifest = json.loads((ANALYSIS / "observation-manifest.json").read_text())
    by_id = {record["trend_id"]: record for record in manifest["records"]}
    rows = []
    for record_id in candidate["main_manifest_evidence_ids"]:
        record_meta = by_id[record_id]
        raw = subprocess.check_output(["git", "show", f"HEAD:{record_meta['record_path']}"], text=True)
        record = json.loads(raw)
        observations = []
        for observation in record.get("observations", []):
            measures = {}
            for name, measure in observation.get("measures", {}).items():
                if isinstance(measure, dict):
                    measures[name] = {
                        "value": measure.get("value"),
                        "unit": measure.get("unit"),
                        "value_type": measure.get("value_type"),
                    }
            observations.append(
                {
                    "period": observation.get("period"),
                    "denominator": observation.get("denominator"),
                    "measure_names": sorted(measures),
                    "measures": measures,
                }
            )
        rows.append(
            {
                "record_id": record_id,
                "record_path": record_meta["record_path"],
                "title": record["title"],
                "source_unit": record.get("source_unit"),
                "geography": record.get("geography"),
                "source_urls": record_meta.get("source_urls", []),
                "observation_count": len(observations),
                "observations": observations,
            }
        )
    payload = {
        "schema": "external-trend-intelligence.care-capacity-measurement-matrix.v1",
        "candidate_id": candidate["candidate_id"],
        "status": "measurement_reconciliation_required",
        "comparison_dimensions": ["period", "geography", "population", "denominator", "unit", "measure_definition", "source_lineage"],
        "rows": rows,
        "decision": "hold",
        "decision_reason": "The records offer multiple care/access/work signals, but their periods, populations, denominators, and units are heterogeneous. They cannot be pooled or treated as one trend measure without reconciliation.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
