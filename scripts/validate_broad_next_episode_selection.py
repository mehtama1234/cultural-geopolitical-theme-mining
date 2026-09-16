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
    routes = data.get("ranked_routes", [])
    if [route.get("rank") for route in routes] != [1, 2, 3]:
        raise ValueError("routes must be ranked 1, 2, 3")
    for route in routes:
        source = root / route["source"]
        if not source.exists():
            raise FileNotFoundError(source)
        if not route.get("next_fields"):
            raise ValueError(f"{route['route']} has no next fields")
    if "MEPS" not in routes[0]["route"]:
        raise ValueError("MEPS must remain the primary local route")
    print(f"VALID broad next-episode selection: {len(routes)} ranked local routes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
