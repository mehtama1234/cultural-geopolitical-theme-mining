#!/usr/bin/env python3
"""Extract the medical-debt subproduct count from a CFPB aggregate snapshot.

This is an administrative visibility measure. It does not estimate medical
debt prevalence, complaint incidence, remedy, or household recovery.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    data = json.loads(args.snapshot.read_text(encoding="utf-8"))
    product_buckets = data["aggregations"]["product"]["product"]["buckets"]
    debt = next(bucket for bucket in product_buckets if bucket["key"] == "Debt collection")
    medical = next(
        bucket
        for bucket in debt["sub_product.raw"]["buckets"]
        if bucket["key"] == "Medical debt"
    )
    all_published = int(data["total_records"]["value"])
    debt_collection = int(debt["doc_count"])
    medical_debt = int(medical["doc_count"])
    result = {
        "schema": "us-cfpb-medical-debt-visibility-v1",
        "source_unit": "published CFPB complaint record represented in a 2025 product/sub-product aggregate snapshot",
        "window": {
            "date_received_min": data.get("date_received_min"),
            "date_received_max": data.get("date_received_max"),
        },
        "counts": {
            "all_published_records": all_published,
            "debt_collection_records": debt_collection,
            "medical_debt_records": medical_debt,
        },
        "shares_percent": {
            "medical_debt_of_all_published": 100 * medical_debt / all_published,
            "medical_debt_of_debt_collection": 100 * medical_debt / debt_collection,
        },
        "input": {"path": str(args.snapshot), "sha256": sha256(args.snapshot)},
        "method": "Read the nested Debt collection -> Medical debt bucket and divide by the snapshot total and Debt collection parent bucket; no record-level deduplication or outcome inference.",
        "boundary": "This is complaint-system visibility, not medical-debt prevalence, harm incidence, a rate among debtors, verified remedy, money recovered, care restoration, trust, switching, or exit. Product/sub-product selection and publication rules shape the count.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
