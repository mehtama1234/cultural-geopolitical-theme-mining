#!/usr/bin/env python3
"""Compare annual CFPB published-complaint response aggregates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def buckets(snapshot: dict, name: str) -> dict[str, int]:
    group = snapshot.get("aggregations", {}).get(name, {}).get(name, {})
    return {
        str(item.get("key_as_string", item.get("key"))): int(item["doc_count"])
        for item in group.get("buckets", [])
    }


def shares(counts: dict[str, int], total: int) -> dict[str, float]:
    return {key: round(100 * value / total, 4) for key, value in sorted(counts.items())}


def parse_input(value: str) -> tuple[int, Path]:
    year, separator, path = value.partition("=")
    if not separator or not year.isdigit() or not path:
        raise argparse.ArgumentTypeError("snapshot must be YEAR=JSON_PATH")
    return int(year), Path(path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=parse_input, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    years = {}
    for year, path in args.snapshot:
        snapshot = json.loads(path.read_text(encoding="utf-8"))
        total = int(snapshot["total_records"]["value"])
        years[str(year)] = {
            "published_records": total,
            "company_response_counts": buckets(snapshot, "company_response"),
            "company_response_shares": shares(buckets(snapshot, "company_response"), total),
            "timely_counts": buckets(snapshot, "timely"),
            "timely_shares": shares(buckets(snapshot, "timely"), total),
            "narrative_counts": buckets(snapshot, "has_narrative"),
            "narrative_shares": shares(buckets(snapshot, "has_narrative"), total),
            "product_counts": buckets(snapshot, "product"),
            "retrieved_sha256": snapshot["retrieved_sha256"],
            "api_metadata": snapshot.get("api_metadata", {}),
        }
    result = {
        "format": "us-cfpb-annual-response-trend-v1",
        "source_unit": "published CFPB complaint record, grouped by calendar year received",
        "years": dict(sorted(years.items())),
        "boundary": "This is a trend in published complaint-system records. Product taxonomy, routing, publication rules, complaint propensity, firm mix, and the non-representative sample can change over time; response categories are not verified remedies or harm rates.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"years": sorted(years), "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
