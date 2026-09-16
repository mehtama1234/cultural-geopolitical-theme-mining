#!/usr/bin/env python3
"""Fetch an aggregate-only CFPB complaint API snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import ssl
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_URL = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date-min", required=True)
    parser.add_argument("--date-max", required=True)
    parser.add_argument("--product", action="append", default=[])
    parser.add_argument("--sub-product", action="append", default=[])
    parser.add_argument(
        "--expect-total",
        type=int,
        help="fail after writing the snapshot if the API returns a different total",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--insecure-tls", action="store_true",
                        help="use only when the local CA store is unavailable")
    args = parser.parse_args()
    query = [("date_received_min", args.date_min),
             ("date_received_max", args.date_max), ("size", "0")]
    query.extend(("product", product) for product in args.product)
    query.extend(("sub_product", sub_product) for sub_product in args.sub_product)
    url = BASE_URL + "?" + urlencode(query)
    request = Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "cultural-geopolitical-theme-mining/1.0",
    })
    context = ssl._create_unverified_context() if args.insecure_tls else None
    with urlopen(request, timeout=120, context=context) as response:
        raw = response.read()
    payload = json.loads(raw)
    total_records = payload.get("hits", {}).get("total", {})
    returned_total = total_records.get("value") if isinstance(total_records, dict) else total_records
    filter_check = None
    if args.expect_total is not None:
        filter_check = {
            "expected_total": args.expect_total,
            "returned_total": returned_total,
            "status": "matched" if returned_total == args.expect_total else "mismatch",
        }
    output = {
        "format": "us-cfpb-complaint-aggregation-snapshot-v1",
        "request_url": url,
        "date_received_min": args.date_min,
        "date_received_max": args.date_max,
        "product_filters": args.product,
        "sub_product_filters": args.sub_product,
        "retrieved_sha256": hashlib.sha256(raw).hexdigest(),
        "api_metadata": payload.get("_meta", {}),
        "total_records": total_records,
        "aggregations": payload.get("aggregations", {}),
        "boundary": "Aggregate published complaint records are not a representative sample, account-denominated harm rate, verified remedy, switching, or trust measure.",
    }
    if filter_check is not None:
        output["expected_total_check"] = filter_check
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "total_records": output["total_records"], "sha256": output["retrieved_sha256"]}, indent=2))
    if filter_check and filter_check["status"] == "mismatch":
        raise SystemExit(
            f"expected {args.expect_total} records but API returned {returned_total}"
        )


if __name__ == "__main__":
    main()
