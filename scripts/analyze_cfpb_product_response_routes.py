#!/usr/bin/env python3
"""Extract product-conditioned CFPB complaint response-route aggregates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


AGGREGATES = ("company_response", "timely", "has_narrative", "submitted_via")


def buckets(data: dict, name: str) -> dict[str, int]:
    container = data.get("aggregations", {}).get(name, {}).get(name, {})
    return {
        str(bucket.get("key_as_string", bucket.get("key"))): int(bucket["doc_count"])
        for bucket in container.get("buckets", [])
    }


def with_shares(counts: dict[str, int]) -> dict[str, dict[str, float | int]]:
    total = sum(counts.values())
    return {
        key: {"complaints": value, "share_percent": 100 * value / total if total else None}
        for key, value in sorted(counts.items())
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slice", dest="slices", action="append", required=True,
                        help="PRODUCT=JSON_PATH")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    products = {}
    for item in args.slices:
        name, separator, path = item.partition("=")
        if not separator or not name or not path:
            raise ValueError("each --slice must be PRODUCT=JSON_PATH")
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        products[name] = {
            aggregate: with_shares(buckets(data, aggregate))
            for aggregate in AGGREGATES
        }
        products[name]["source_filtered_total"] = int(data["hits"]["total"]["value"])
    result = {
        "format": "us-cfpb-product-response-routes-v1",
        "source_unit": "published CFPB complaint record in a product-filtered API aggregation",
        "products": products,
        "causal_estimation": False,
        "boundary": "Aggregates describe recorded complaint-system routes; they do not measure all consumers, account denominators, harm, remedy adequacy, switching, or trust restoration.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"products": len(products), "aggregates": list(AGGREGATES)}, indent=2))


if __name__ == "__main__":
    main()
