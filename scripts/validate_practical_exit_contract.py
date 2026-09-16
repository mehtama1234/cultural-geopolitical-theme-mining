#!/usr/bin/env python3
"""Validate the practical-exit contract and an optional simulated fixture."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=root / "manifests/practical-exit-observation-contract-v1.json")
    parser.add_argument("--fixture", type=Path, default=root / "analysis/samples/PRACTICAL-EXIT-LEDGER-SIMULATED_V1.json")
    args = parser.parse_args()

    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    statuses = set(contract["evidence_status"])
    post_statuses = set(contract["post_event_status_values"])
    required = set(contract["required_episode_fields"])
    if contract.get("status") != "research-design":
        raise ValueError("contract must remain research-design")
    if not required or not post_statuses:
        raise ValueError("contract must declare required fields and post-event statuses")

    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    if fixture.get("evidence_class") != "simulated_test_data":
        raise ValueError("fixture must be marked simulated_test_data")
    if fixture.get("contract") != contract["format"]:
        raise ValueError("fixture must name the practical-exit contract")

    episodes = fixture.get("episodes", [])
    if not episodes:
        raise ValueError("fixture must contain at least one episode")
    for episode in episodes:
        missing = sorted(required - set(episode))
        if missing:
            raise ValueError(f"episode {episode.get('episode_id')} missing: {', '.join(missing)}")
        if episode["evidence_status"] not in statuses:
            raise ValueError(f"invalid evidence status in {episode['episode_id']}")
        if episode["post_event_status"] not in post_statuses:
            raise ValueError(f"invalid post-event status in {episode['episode_id']}")
        alternatives = episode["alternatives"]
        if not isinstance(alternatives, list) or not alternatives:
            raise ValueError(f"episode {episode['episode_id']} needs an alternatives list")
        for alternative in alternatives:
            for field in contract["minimum_alternative_fields"]:
                if field not in alternative:
                    raise ValueError(f"alternative in {episode['episode_id']} missing {field}")
        if episode["post_event_status"] == "practical_exit":
            if episode["protected_outcome"] in {"", "unknown"} or episode["sacrificed_outcome"] in {"", "unknown"}:
                raise ValueError(f"practical_exit episode {episode['episode_id']} needs protected and sacrificed outcomes")

    print(f"VALID practical-exit contract and simulated fixture: {len(episodes)} episode(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
