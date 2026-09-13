#!/usr/bin/env python3
"""Extract product-conditioned narrative and submission-route shares."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def buckets(data: dict, name: str) -> dict[str, int]:
    agg = data.get("aggregations", {}).get(name, {}).get(name, {})
    return {
        str(bucket.get("key_as_string", bucket.get("key"))): int(bucket["doc_count"])
        for bucket in agg.get("buckets", [])
    }


def share(count: int, total: int) -> float | None:
    return round(100 * count / total, 3) if total else None


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
        total = int(data["hits"]["total"]["value"])
        narrative = buckets(data, "has_narrative")
        submitted = buckets(data, "submitted_via")
        products[name] = {
            "published_records": total,
            "narrative_present": share(narrative.get("true", 0), total),
            "narrative_absent": share(narrative.get("false", 0), total),
            "submitted_via": {
                key: share(value, total) for key, value in sorted(submitted.items())
            },
        }
    result = {
        "format": "us-cfpb-product-visibility-routes-v1",
        "source_unit": "published CFPB complaint record in a product-filtered API aggregation",
        "products": products,
        "causal_estimation": False,
        "boundary": "Narrative and submission-channel shares describe recorded complaint visibility; they do not measure all consumers, access barriers, harm, remedy, or the quality of a submitted account.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"products": len(products)}, indent=2))


if __name__ == "__main__":
    main()
