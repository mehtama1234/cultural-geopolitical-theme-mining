#!/usr/bin/env python3
"""Pin a bounded CDC NPALS public-table extract and definition reconciliation."""

from __future__ import annotations

import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "npals-public-table-extract.json"
API = "https://data.cdc.gov/resource/wibz-pb5q.json"


def fetch_rows() -> tuple[str, list[dict]]:
    where = (
        "(survey_year='2020' OR survey_year='2022' OR survey_year='2025') AND "
        "(select_setting='Adult Day Services Center' OR select_setting='Adult day services center') AND "
        "select_measure in('Number of providers','Number of people served','Capacity') AND value_type='Number'"
    )
    params = {"$where": where, "$limit": "5000"}
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = response.read()
    return url, json.loads(payload)


def numeric_rows(rows: list[dict]) -> list[dict]:
    selected_levels = {
        "Number of providers": {"Number of providers"},
        "Capacity": {"Total licensed maximum capacity or total number of beds"},
        "Number of people served": {"Daily average"},
    }
    output = []
    for row in rows:
        if row.get("levels_of_measure") not in selected_levels.get(row.get("select_measure"), set()):
            continue
        if "value" not in row:
            continue
        item = {
            "survey_year": int(row["survey_year"]),
            "geography": row["geography"],
            "measure": row["select_measure"],
            "level": row["levels_of_measure"],
            "value": float(row["value"]),
            "standard_error": float(row["se"]) if row.get("se") is not None else None,
            "low_95_ci": float(row["low_95_ci"]) if row.get("low_95_ci") is not None else None,
            "high_95_ci": float(row["high_95_ci"]) if row.get("high_95_ci") is not None else None,
        }
        output.append(item)
    return sorted(output, key=lambda item: (item["survey_year"], item["geography"], item["measure"]))


def main() -> int:
    checked_at = datetime.now(timezone.utc).isoformat()
    try:
        url, raw_rows = fetch_rows()
    except Exception as error:
        if not OUTPUT.exists():
            raise
        previous = json.loads(OUTPUT.read_text())
        previous["retrieval_status"] = "stale_previous_extract_source_unavailable"
        previous["source_available"] = False
        previous["checked_at"] = checked_at
        previous["retrieval_error"] = f"{type(error).__name__}: {error}"
        OUTPUT.write_text(json.dumps(previous, indent=2) + "\n")
        print(f"source unavailable; preserved previous NPALS extract ({previous.get('numeric_row_count', 0)} rows)")
        return 0
    rows = numeric_rows(raw_rows)
    national = [row for row in rows if row["geography"] == "National"]
    state_2020 = [row for row in rows if row["survey_year"] == 2020 and row["geography"] != "National"]
    report = {
        "schema": "external-trend-intelligence.npals-public-table-extract.v1",
        "source_id": "cdc-npals-public-biennial-overview-wibz-pb5q",
        "source_url": "https://data.cdc.gov/National-Center-for-Health-Statistics/Biennial-Overview-of-Post-acute-and-Long-term-Care/wibz-pb5q",
        "api_url": url,
        "retrieval_status": "fresh_api_extract",
        "source_available": True,
        "retrieved_at": checked_at,
        "checked_at": checked_at,
        "raw_row_count": len(raw_rows),
        "numeric_row_count": len(rows),
        "state_2020_row_count": len(state_2020),
        "state_2020_geography_count": len({row["geography"] for row in state_2020}),
        "state_2020_frame_geography_count": len({row["geography"] for row in raw_rows if row.get("survey_year") == "2020"}),
        "national_row_count": len(national),
        "rows": rows,
        "reconciliation": {
            "status": "definition_reconciliation_required",
            "comparisons": [
                {
                    "period": 2022,
                    "measure": "adult_day_services_centers",
                    "public_table_value": 3100,
                    "existing_pdf_normalized_value": 3100,
                    "comparison_status": "directionally_aligned_but_definition_and_rounding_review_required",
                },
                {
                    "period": 2025,
                    "measure": "adult_day_services_centers",
                    "public_table_value": 3300,
                    "existing_pdf_normalized_value": 4448,
                    "comparison_status": "not_comparable_without_definition_review",
                    "note": "The public table provider-count field and the weighted PDF center estimate do not match; retain both values and do not calculate a growth rate across them.",
                },
            ],
            "boundary": "The public table and weighted PDF may use different universes, definitions, or table constructions. This extract is a reconciliation control, not a validated utilization trend.",
        },
        "rights_boundary": "Retain normalized API observations, query URL, retrieval time, and source metadata; do not redistribute upstream table contents beyond the permitted public-data use.",
        "next_action": "Map the API table definition and 2025 survey universe to the weighted PDF before using provider, capacity, or attendance changes in qualification.",
    }
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    report["normalized_rows_sha256"] = hashlib.sha256(canonical).hexdigest()
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} numeric rows; {len(state_2020)} 2020 state rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
