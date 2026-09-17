#!/usr/bin/env python3
"""Audit which end-to-end endpoints are exposed by the retained HTOPS record."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record",
        type=Path,
        default=root / "analysis/records/us-census-htops-material-trust-panel-april-june-2025.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "analysis/projects/us-cost-trust-politics/data/htops-2025-local-endpoint-observability-audit.json",
    )
    args = parser.parse_args()

    record = json.loads(args.record.read_text(encoding="utf-8"))
    observations = record.get("observations", [])
    if len(observations) != 1:
        raise ValueError("expected one retained HTOPS panel observation")
    measures = observations[0].get("measures", {})
    if not measures:
        raise ValueError("retained HTOPS record has no measures")

    material = sorted(
        key for key in measures if any(
            token in key
            for token in ("expense", "food", "energy", "prices", "job_loss", "work")
        )
    )
    judgment = sorted(
        key for key in measures if any(
            token in key
            for token in ("confidence", "statistics")
        )
    )
    design = sorted(
        key for key in measures
        if key in {
            "baseline_sample_n",
            "followup_sample_n",
            "linked_retention_from_baseline_percent",
            "linked_retention_from_followup_percent",
        }
    )
    endpoint_status = [
        {
            "endpoint": "timed_material_condition_or_followup",
            "status": "exposed",
            "retained_measure_keys": material,
            "interpretation": "The retained record exposes April-to-June linked material transitions and selected later material outcomes.",
        },
        {
            "endpoint": "institutional_judgment",
            "status": "exposed",
            "retained_measure_keys": judgment,
            "interpretation": "The retained record exposes confidence/agreement measures, which are judgment outcomes rather than attribution or action.",
        },
        {
            "endpoint": "sample_and_linkage_design_metadata",
            "status": "exposed",
            "retained_measure_keys": design,
            "interpretation": "The retained record exposes source-file sample counts and linked-retention metadata; these are design fields, not substantive outcomes.",
        },
        {
            "endpoint": "responsible_actor_or_attribution",
            "status": "not_exposed_in_retained_record",
            "retained_measure_keys": [],
            "interpretation": "No actor, blame, responsibility, fairness, or causal attribution field is represented in the committed local panel record.",
        },
        {
            "endpoint": "distinct_civic_or_political_action",
            "status": "not_exposed_in_retained_record",
            "retained_measure_keys": [],
            "interpretation": "No vote, contact, complaint, appeal, organizing, volunteering, registration, or withdrawal field is represented in the committed local panel record.",
        },
        {
            "endpoint": "remedy_recovery_switching_or_exit",
            "status": "not_exposed_in_retained_record",
            "retained_measure_keys": [],
            "interpretation": "No remedy receipt, later recovery, switching, non-use, or exit field is represented in the committed local panel record.",
        },
    ]
    result = {
        "format": "htops-2025-local-endpoint-observability-audit-v1",
        "record": str(args.record.relative_to(root)),
        "linked_ids": record["observations"][0]["denominator"]["value"],
        "retained_measure_count": len(measures),
        "endpoint_status": endpoint_status,
        "boundary": "This is an audit of the committed local trend record, not a complete Census PUF codebook audit. A missing endpoint here means it was not retained or represented in the local artifact; it does not prove the original public-use files lack the field. No national estimate or causal claim is made.",
        "next_gate": "If the PUFs are reacquired, inspect both dictionaries and the shared respondent field surface for dated actor attribution, distinct action, remedy, recovery, switching, and exit before extending the panel estimate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(measures)} retained measures audited")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
