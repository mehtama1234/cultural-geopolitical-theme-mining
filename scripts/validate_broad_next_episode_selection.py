#!/usr/bin/env python3
"""Validate the broad program's ranked local episode-route decision."""

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
        default=root / "analysis/data/broad-next-episode-selection-v1.json",
    )
    args = parser.parse_args()
    data = json.loads(args.record.read_text(encoding="utf-8"))
    if data.get("status") != "ranked_local_route_decision":
        raise ValueError("record must remain a ranked local route decision")
    gate = data.get("promotion_gate")
    if not isinstance(gate, dict):
        raise ValueError("record must declare the promotion gate")
    required_additions = gate.get("required_additions")
    if required_additions != [
        "episode_level_alternative_or_nonuse",
        "remedy_receipt_or_outcome_followup",
    ]:
        raise ValueError("promotion gate must require alternative/non-use and receipt/outcome")
    if gate.get("qualifying_local_route") is not False:
        raise ValueError("current local route decision must preserve the open gate")
    if not gate.get("decision") or not gate.get("reason"):
        raise ValueError("promotion gate needs a decision and evidence-based reason")
    routes = data.get("ranked_routes", [])
    if [route.get("rank") for route in routes] != [1, 2, 3]:
        raise ValueError("routes must be ranked 1, 2, 3")
    for route in routes:
        source = root / route["source"]
        if not source.exists():
            raise FileNotFoundError(source)
        if not route.get("next_fields"):
            raise ValueError(f"{route['route']} has no next fields")
        for supporting in route.get("supporting_sources", []):
            supporting_path = Path(supporting)
            if supporting_path.is_absolute() or ".." in supporting_path.parts:
                raise ValueError(
                    f"{route['route']} has unsafe supporting source: {supporting}"
                )
            if not (root / supporting_path).is_file():
                raise FileNotFoundError(root / supporting_path)
    if "MEPS" not in routes[0]["route"]:
        raise ValueError("MEPS must remain the primary local route")
    print(f"VALID broad next-episode selection: {len(routes)} ranked local routes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
