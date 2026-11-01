#!/usr/bin/env python3
"""Pin the Urban Institute's December 2025 WBNS food-insecurity release."""

from __future__ import annotations

import hashlib
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "analysis" / "external-trend-intelligence" / "urban-wbns-food-insecurity-2025.json"
SOURCE_URL = "https://www.urban.org/sites/default/files/2026-03/Food%20Insecurity%20Remained%20High%20in%202025%2C%20As%20Safety%20Net%20Cuts%20Loom%20.pdf"
SOURCE_CHECKSUM = "sha256:8c099a3ca11f3130613ad51035eaf5f18cf99652940c48b42459cada84e8f16f"


def availability() -> dict:
    request = urllib.request.Request(SOURCE_URL, method="HEAD", headers={"User-Agent": "external-observatory/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return {"http_status": response.status, "availability": "official_source_available"}
    except urllib.error.HTTPError as exc:
        return {"http_status": exc.code, "availability": "official_source_unavailable"}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"http_status": None, "availability": "source_check_failed", "error_type": type(exc).__name__}


def main() -> int:
    check = availability()
    payload = {
        "schema": "external-trend-intelligence.urban-wbns-food-insecurity-snapshot.v1",
        "status": "official_release_normalized_monitoring_update",
        "source_id": "urban-wbns-food-insecurity-2025",
        "publisher": "Urban Institute",
        "dataset": "Well-Being and Basic Needs Survey (WBNS), December 2025 food-insecurity release",
        "source_url": SOURCE_URL,
        "publication_date": "2026-03-18",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source_checksum": SOURCE_CHECKSUM,
        "availability_check": check,
        "observation_period": "December 2025; household food insecurity in the last 12 months",
        "population_and_unit": "U.S. adults age 18 and older; percent reporting household food insecurity",
        "geography": "United States",
        "rows": [
            {"category": "all_adults_18_plus", "food_insecurity_percent": 24.2},
            {"category": "working_age_adults_18_64", "food_insecurity_percent": 27.7},
            {"category": "adults_65_plus", "food_insecurity_percent": 12.7},
            {"category": "working_age_adults_in_households_with_children", "food_insecurity_percent": 32.0, "very_low_food_security_percent": 16.2},
            {"category": "working_age_adults_below_200_percent_fpl", "food_insecurity_percent": 51.0},
            {"category": "working_age_adults_200_to_400_percent_fpl", "food_insecurity_percent": 34.2},
            {"category": "working_age_adults_400_percent_fpl_or_more", "food_insecurity_percent": 9.3},
        ],
        "method": "Urban Institute normalized figures from the December 2025 WBNS release; the 2025 sample expanded to include adults age 65 and older and the publication reports an updated estimation approach.",
        "comparability_and_uncertainty": [
            "WBNS is an annual survey of adults and is not numerically interchangeable with USDA's CPS household series.",
            "The 2025 methodology update means estimates differ slightly from earlier Urban publications; preserve the publication's definitions and significance annotations.",
            "The survey has a low cumulative response rate and may underrepresent people experiencing homelessness, low literacy, or limited English/Spanish proficiency.",
            "The figures describe reported household food insecurity, not provider utilization, capacity, revenue, or company demand.",
        ],
        "rights_boundary": "Retain normalized values, source locator, checksum, and attribution; do not redistribute the upstream PDF or reproduce its tables in a commercial frontend without exact-artifact terms review.",
        "next_action": "Use as the next Urban monitoring vintage and reconcile the methodology break before comparing 2025 with earlier values or using it in a company pilot.",
        "boundary": "This is a publisher-reported monitoring update. It supports external persistence monitoring but does not establish causality, policy effect, market size, or company exposure.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(payload['rows'])} normalized rows; {check['availability']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
