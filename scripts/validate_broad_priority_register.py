#!/usr/bin/env python3
"""Validate the broad atlas depth-priority and acquisition route contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "analysis/data/broad-depth-priority-register-v1.json"


def main() -> int:
    payload = json.loads(REGISTER.read_text(encoding="utf-8"))
    rule = payload.get("execution_rule", {})
    required_rule = {
        "broad_atlas_first": "PSID authenticated family/person extract for the material/time/care bridge",
        "health_cost_alternative": "UAS Older Ages or Monthly Panel only for the narrower dated health-cost episode",
        "public_record_stage_first": "Worker remedy receipt and later stability when an identifier-bearing follow-up is available",
        "boundary": "Do not pool PSID, UAS, MEPS, SIPP, or administrative routes as if they were one same-unit episode.",
    }
    for key, expected in required_rule.items():
        if rule.get(key) != expected:
            raise SystemExit(f"priority register execution_rule.{key} is missing or changed")

    priorities = payload.get("priorities", [])
    ranks = [row.get("rank") for row in priorities]
    if ranks != list(range(1, len(priorities) + 1)):
        raise SystemExit(f"priority ranks are not contiguous: {ranks}")
    if not priorities or priorities[0].get("name") != "Household pressure and care":
        raise SystemExit("household pressure and care must remain the first priority")
    if any(not row.get("next_route") or not row.get("open_blocker") for row in priorities):
        raise SystemExit("every priority needs a next route and explicit blocker")

    print(f"VALID broad priority register: {len(priorities)} ranked routes; execution rule preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
