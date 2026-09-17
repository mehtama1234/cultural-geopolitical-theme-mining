#!/usr/bin/env python3
"""Validate the documentation-only UAS episode acquisition manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=root / "analysis/projects/us-household-constraint-cascade/data/uas-minimum-episode-field-manifest-v1.json",
    )
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    if data.get("status") != "documentation_only; no respondent microdata acquired":
        raise ValueError("UAS manifest must remain documentation-only")
    if data.get("storage_policy", {}).get("raw_microdata_in_repository") is not False:
        raise ValueError("UAS manifest must prohibit raw microdata in the repository")
    candidates = {row.get("role"): row for row in data.get("candidate_files", [])}
    required_roles = {
        "monthly_panel",
        "older_ages_monthly_events_panel",
        "uas537_healthcare_experience",
        "uas698_health_cost",
    }
    missing_roles = required_roles - candidates.keys()
    if missing_roles:
        raise ValueError(f"UAS manifest missing candidate routes: {sorted(missing_roles)}")
    older = candidates["older_ages_monthly_events_panel"]
    fields = older.get("documented_candidates", {})
    required_fields = {
        "uasid",
        "wave",
        "final_weight",
        "le001",
        "le011_1_",
        "le_hrs_oopa1",
        "le_hrs_srh1",
        "le_hrs_s1",
        "le_hrs_p1",
    }
    observed_fields = {field for values in fields.values() for field in values}
    if not required_fields <= observed_fields:
        raise ValueError(f"Older Ages route missing documented fields: {sorted(required_fields - observed_fields)}")
    if not older.get("universe", "").startswith("UAS respondents aged 50 and older"):
        raise ValueError("Older Ages route must preserve its age-restricted universe")
    if not older.get("still_verify_after_access"):
        raise ValueError("Older Ages route must retain post-access verification gates")
    promotion = data.get("promotion_requirements", {})
    for group in ("identity_and_timing", "choice_and_consequence", "design"):
        if not promotion.get(group):
            raise ValueError(f"promotion requirements missing {group}")
    if len(data.get("stop_conditions", [])) < 5:
        raise ValueError("manifest must retain multiple stop conditions")
    print(f"VALID UAS episode manifest: {len(candidates)} candidate routes; storage invariant preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
