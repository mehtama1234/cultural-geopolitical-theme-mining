#!/usr/bin/env python3
"""Capture the public national Map the Meal Gap page as a bounded source snapshot."""

from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "feeding-america-map-meal-gap-2026-national.json"
SOURCE_URL = "https://map.feedingamerica.org/"


def fetch() -> tuple[dict | None, dict]:
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "external-observatory/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read()
            match = re.search(rb'<script data-page="app" type="application/json">(.*?)</script>', raw, re.S)
            if not match:
                raise ValueError("app JSON payload not found")
            app = json.loads(match.group(1))
            selected = app["props"]["selected"]
            return selected, {
                "http_status": response.status,
                "availability": "official_source_available",
                "retrieval_hash": "sha256:" + hashlib.sha256(raw).hexdigest(),
            }
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        return None, {"http_status": None, "availability": "pinned_snapshot_retained_fetch_failed", "error_type": type(exc).__name__}


def main() -> int:
    selected, check = fetch()
    selected = selected or {
        "year": "2024",
        "type": "national",
        "insecurity": 0.144,
        "population": 47900000,
        "money_needed": 33644026788,
        "cost_per_meal": 3.7,
        "low_band": 0.43,
        "mid_band": 0.19,
        "high_band": 0.38,
    }
    payload = {
        "schema": "external-trend-intelligence.feeding-america-map-meal-gap-snapshot.v1",
        "status": "public_national_estimate_snapshot_method_review_pending",
        "publisher": "Feeding America",
        "dataset": "Map the Meal Gap 2026 public national estimate",
        "source_url": SOURCE_URL,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "availability_check": check,
        "observation_period": "2024 estimate published in 2026",
        "geography": "United States national overall population",
        "unit_and_denominator": "modeled share of individuals living in food-insecure households; estimated population count; annual food budget shortfall in USD; average meal cost in USD",
        "observations": {
            "food_insecurity_rate": selected["insecurity"],
            "food_insecure_population": selected["population"],
            "annual_food_budget_shortfall_usd": selected["money_needed"],
            "average_meal_cost_usd": selected["cost_per_meal"],
            "program_eligibility_bands": {
                "below_snap_threshold": selected.get("low_band"),
                "between_130_and_185_percent_poverty": selected.get("mid_band"),
                "above_snap_threshold": selected.get("high_band"),
            },
        },
        "method_and_dependence": "Feeding America models local estimates using CPS-FSS, ACS, BLS/LAUS, and local food-price inputs; the national page is a modeled estimate, not a direct provider transaction or visit count.",
        "rights_boundary": "The public page is observable and citable; the underlying county dataset is request-gated. Do not redistribute bulk data or create company-facing derived charts until exact dataset terms and permission are recorded.",
        "comparability_limits": [
            "This publisher's modeled individual-level estimate is not directly comparable to USDA's household CPS-FSS receipt measures.",
            "The 2026 release reports 2024 estimates and should not be treated as a contemporaneous 2026 outcome.",
            "Food insecurity and food budget shortfall are demand-context measures, not provider capacity, visits, meals served, or revenue.",
        ],
        "next_action": "Use as an independent publisher challenge and acquire the request-gated underlying data or technical appendix before any pooled estimate or IBIS promotion.",
        "boundary": "This snapshot records a public modeled estimate for lineage comparison. It does not establish causal demand, independent validation, rights clearance, or a company decision outcome.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({check['availability']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
