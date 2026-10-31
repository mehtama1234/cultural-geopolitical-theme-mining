#!/usr/bin/env python3
"""Validate the company-facing trend portfolio and linked Markdown records."""

from __future__ import annotations

import json
import csv
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "analysis" / "company-trend-intelligence"


def main() -> int:
    schema = json.loads((BASE / "schema.json").read_text(encoding="utf-8"))
    portfolio = json.loads((BASE / "portfolio.json").read_text(encoding="utf-8"))
    with (BASE / "portfolio.csv").open(newline="", encoding="utf-8") as handle:
        csv_rows = list(csv.DictReader(handle))
    with (BASE / "THEME-COVERAGE-MATRIX.csv").open(newline="", encoding="utf-8") as handle:
        theme_rows = list(csv.DictReader(handle))

    assert schema["schema"] == "company-trend-intelligence-record-v1"
    assert portfolio["schema"] == "company-trend-intelligence-portfolio-v1"

    required = set(schema["required"])
    statuses = set(schema["status_values"])
    records = portfolio["records"]
    ids = [record["trend_id"] for record in records]
    theme_coverage = portfolio["theme_coverage"]
    assert len(theme_coverage) == 14, "theme coverage must contain all 14 programme themes"
    assert len(theme_rows) == 14, "theme coverage CSV must contain all 14 programme themes"
    assert {int(row["theme_number"]) for row in theme_rows} == set(range(1, 15)), "theme CSV numbers must be 1..14"
    assert {item["number"] for item in theme_coverage} == set(range(1, 15)), "theme numbers must be 1..14"
    assert {item["coverage"] for item in theme_coverage} <= {"deep", "lens", "open"}, "invalid theme coverage"
    assert {int(row["theme_number"]) for row in theme_rows} == {item["number"] for item in theme_coverage}, "theme JSON and CSV numbers differ"
    assert {row["coverage"] for row in theme_rows} <= {"deep", "lens", "open"}, "invalid theme CSV coverage"
    record_ids = set(ids)
    for item in theme_coverage:
        assert set(item["record_ids"]) <= record_ids, f"unknown trend in theme coverage: {item}"
    assert len(csv_rows) == len(records), "CSV and JSON record counts differ"
    assert len(ids) == len(set(ids)), "duplicate trend_id"
    assert records, "portfolio has no records"

    for record in records:
        assert set(("trend_id", "title", "summary", "path", "source_packets", "status", "confidence", "horizon", "domains", "decision_owners", "open_test")) <= set(record), record
        assert len(record["source_packets"]) >= 1, record["trend_id"]
        assert record["status"] in statuses, record
        assert record["confidence"] in {"high", "medium", "low"}, record
        assert set(record["horizon"]) <= {"now", "next", "longer_term"}, record
        path = BASE / record["path"]
        assert path.is_file(), path
        text = path.read_text(encoding="utf-8")
        assert record["trend_id"] in text, record["trend_id"]
        assert record["title"] in text, record["title"]
        assert record["summary"], record["trend_id"]
        for source in record["source_packets"]:
            repo_path = (BASE / source).resolve().relative_to(ROOT)
            check = subprocess.run(
                ["git", "cat-file", "-e", f"HEAD:{repo_path}"],
                cwd=ROOT,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            assert check.returncode == 0, f"untracked or missing source packet: {repo_path}"
            assert repo_path.name in text, f"source packet not linked in record: {repo_path}"
        for heading in ("## Source packet", "## Evidence", "## Mechanism", "## Business exposure", "## Time horizon", "## Leading indicators", "## Counterevidence and limits", "## Next test"):
            assert heading in text, f"{path}: missing {heading}"
        for label in ("**Now (0–12 months):**", "**Next (1–3 years):**", "**Longer term (3+ years):**"):
            assert label in text, f"{path}: missing horizon {label}"

    assert {row["trend_id"] for row in csv_rows} == set(ids), "CSV and JSON IDs differ"
    assert all(row["source_packets"] for row in csv_rows), "CSV source packets missing"

    assert required >= {"trend_id", "title", "status", "evidence", "business_exposure", "leading_indicators", "next_test"}
    print(f"valid company trend portfolio: {len(records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
