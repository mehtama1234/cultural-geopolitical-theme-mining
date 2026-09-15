#!/usr/bin/env python3
"""Audit dated CFPB complaint-to-company routing fields in capped product samples."""

from __future__ import annotations

import argparse
import hashlib
import json
import ssl
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_URL = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def shares(counter: Counter[str], total: int) -> dict[str, dict[str, float | int]]:
    return {key: {"records": value, "share_percent": 100 * value / total if total else None} for key, value in sorted(counter.items())}


def fetch(query: dict[str, str]) -> tuple[dict, str]:
    url = BASE_URL + "?" + urlencode(query)
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    with urlopen(request, timeout=120, context=ssl.create_default_context()) as response:
        raw = response.read()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def summarize(payload: dict, raw_hash: str, query: dict[str, str]) -> dict:
    hits = payload.get("hits", {}).get("hits", [])
    response = Counter()
    timely = Counter()
    via = Counter()
    narrative = Counter()
    public_response = Counter()
    lags = []
    for hit in hits:
        row = hit.get("_source", {})
        response[row.get("company_response") or "Missing"] += 1
        timely[row.get("timely") or "Missing"] += 1
        via[row.get("submitted_via") or "Missing"] += 1
        narrative["present" if row.get("has_narrative") else "absent"] += 1
        public_response["present" if row.get("company_public_response") else "absent"] += 1
        received, sent = parse_date(row.get("date_received")), parse_date(row.get("date_sent_to_company"))
        if received and sent:
            lags.append((sent - received).total_seconds() / 3600)
    return {
        "request": {"query": query, "raw_sha256": raw_hash},
        "total_matching_records": payload.get("hits", {}).get("total", {}),
        "sample_records": len(hits),
        "response": shares(response, len(hits)),
        "timely": shares(timely, len(hits)),
        "submitted_via": shares(via, len(hits)),
        "narrative": shares(narrative, len(hits)),
        "company_public_response": shares(public_response, len(hits)),
        "receipt_to_company_send_hours": {
            "valid_records": len(lags),
            "median": sorted(lags)[len(lags) // 2] if lags else None,
            "p90": sorted(lags)[int(0.9 * (len(lags) - 1))] if lags else None,
            "same_calendar_day_percent": 100 * sum(1 for value in lags if value < 24) / len(lags) if lags else None,
            "max": max(lags) if lags else None,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date-min", required=True)
    parser.add_argument("--date-max", required=True)
    parser.add_argument("--product", action="append", required=True)
    parser.add_argument("--sample-size", type=int, default=1000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.sample_size <= 10000:
        raise ValueError("sample size must be between 1 and 10000")
    products = {}
    for product in args.product:
        query = {"date_received_min": args.date_min, "date_received_max": args.date_max, "product": product, "size": str(args.sample_size)}
        payload, raw_hash = fetch(query)
        products[product] = summarize(payload, raw_hash, query)
    output = {
        "format": "us-cfpb-case-route-sample-v1",
        "source_unit": "capped retrieval-order sample of published CFPB complaint records",
        "date_received_min": args.date_min,
        "date_received_max": args.date_max,
        "sample_design": "up to requested size per product using API retrieval order; not random and not weighted",
        "products": products,
        "causal_estimation": False,
        "boundary": "Date sent to company measures CFPB routing delay, not company response or consumer remedy. Company response, timely, narrative, and public-response fields are administrative/publication fields. Capped retrieval-order samples are not population estimates and cannot be joined to SIPP, SHED, or ANES respondents.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"products": len(products), "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
