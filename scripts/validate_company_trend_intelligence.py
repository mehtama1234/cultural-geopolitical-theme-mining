#!/usr/bin/env python3
"""Validate the company-facing trend portfolio and linked Markdown records."""

from __future__ import annotations

import json
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "analysis" / "company-trend-intelligence"


def main() -> int:
    schema = json.loads((BASE / "schema.json").read_text(encoding="utf-8"))
    portfolio = json.loads((BASE / "portfolio.json").read_text(encoding="utf-8"))
    with (BASE / "portfolio.csv").open(newline="", encoding="utf-8") as handle:
        csv_rows = list(csv.DictReader(handle))

    assert schema["schema"] == "company-trend-intelligence-record-v1"
    assert portfolio["schema"] == "company-trend-intelligence-portfolio-v1"

    required = set(schema["required"])
    statuses = set(schema["status_values"])
    records = portfolio["records"]
    assert len(csv_rows) == len(records), "CSV and JSON record counts differ"
    ids = [record["trend_id"] for record in records]
    assert len(ids) == len(set(ids)), "duplicate trend_id"
    assert records, "portfolio has no records"

    for record in records:
        assert set(("trend_id", "title", "path", "status", "confidence", "horizon", "domains", "decision_owners", "open_test")) <= set(record), record
        assert record["status"] in statuses, record
        assert record["confidence"] in {"high", "medium", "low"}, record
        assert set(record["horizon"]) <= {"now", "next", "longer_term"}, record
        path = BASE / record["path"]
        assert path.is_file(), path
        text = path.read_text(encoding="utf-8")
        assert record["trend_id"] in text, record["trend_id"]
        assert record["title"] in text, record["title"]
        for heading in ("## Evidence", "## Mechanism", "## Business exposure", "## Leading indicators", "## Counterevidence and limits", "## Next test"):
            assert heading in text, f"{path}: missing {heading}"

    assert {row["trend_id"] for row in csv_rows} == set(ids), "CSV and JSON IDs differ"

    assert required >= {"trend_id", "title", "status", "evidence", "business_exposure", "leading_indicators", "next_test"}
    print(f"valid company trend portfolio: {len(records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
