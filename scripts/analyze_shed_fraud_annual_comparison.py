#!/usr/bin/env python3
"""Compare codebook-backed SHED fraud burden measures across annual files."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from pathlib import Path


AGE = {"18–29": "18–29", "30–44": "30–44", "45–59": "45–59", "60+": "60+"}
INCOME = {
    "Less than $10,000": "<$10,000",
    "$10,000 to $24,999": "$10,000–$24,999",
    "$25,000 to $49,999": "$25,000–$49,999",
    "$50,000 to $74,999": "$50,000–$74,999",
    "$75,000 to $99,999": "$75,000–$99,999",
    "$100,000 to $149,999": "$100,000–$149,999",
    "$150,000 or more": "$150,000+",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        name = next(n for n in archive.namelist() if n.endswith(".csv"))
        with archive.open(name) as handle:
            return [{k.lower(): v for k, v in row.items()} for row in csv.DictReader((line.decode("utf-8-sig") for line in handle))]


def text(value: str | None) -> str:
    return (value or "").strip()


def share(data: list[dict[str, str]], predicate) -> float | None:
    weighted = [(row, float(row["weight"])) for row in data if text(row.get("weight")) not in {"", "."}]
    total = sum(weight for _, weight in weighted)
    return round(sum(weight for row, weight in weighted if predicate(row)) / total * 100, 3) if total else None


def screen(data: list[dict[str, str]], field: str, labels: dict[str, str]) -> list[dict]:
    output = []
    for code, label in labels.items():
        group = [row for row in data if text(row.get(field)) == code]
        fraud = [row for row in group if text(row.get("bk47_b")) == "Yes"]
        output.append({
            "group": label,
            "code": code,
            "all_adult_rows": len(group),
            "fraud_rows": len(fraud),
            "financial_fraud_exposure_percent": share(group, lambda row: text(row.get("bk47_b")) == "Yes"),
            "lost_money_among_other_fraud_percent": share(fraud, lambda row: text(row.get("bk48")).startswith("I lost money")),
            "some_or_all_unrecovered_among_other_fraud_percent": share(fraud, lambda row: "some of it" in text(row.get("bk48")) or "none of it" in text(row.get("bk48"))),
            "10_or_more_hours_among_other_fraud_percent": share(fraud, lambda row: text(row.get("bk50")) in {"10 to 39 hours", "40 to 79 hours", "80 hours or more"}),
        })
    return output


def analyze(year: int, path: Path) -> dict:
    data = read_rows(path)
    return {
        "year": year,
        "source_unit": f"US adult SHED {year} respondent",
        "weight": "weight",
        "respondent_rows": len(data),
        "age": screen(data, "ppagect4", AGE),
        "income": screen(data, "ppinc7", INCOME),
        "available_fields": sorted({field for field in ("bk47_b", "bk48", "bk50", "bk51", "bk52_b", "ppagect4", "ppinc7") if any(field in row for row in data)}),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, help="YEAR=PATH to an official SHED CSV ZIP")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    annual = []
    for value in args.input:
        year_text, path_text = value.split("=", 1)
        annual.append(analyze(int(year_text), Path(path_text)))
    annual.sort(key=lambda item: item["year"])
    output = {
        "format": "shed-fraud-annual-comparison-v1",
        "source_unit": "separate annual SHED respondent samples",
        "annual": annual,
        "definitions": {
            "financial_fraud_exposure": "BK47_b = Yes",
            "lost_money": "BK48 begins with I lost money",
            "some_or_all_unrecovered": "BK48 contains some of it or none of it",
            "time_10_or_more_hours": "BK50 is 10 to 39 hours, 40 to 79 hours, or 80 hours or more",
        },
        "boundary": "Weighted descriptive annual comparison; the 2024 and 2025 files are separate annual samples and are not treated as a panel. Percentages use metric-specific nonmissing denominators within each subgroup. The 2025 public file lacks the 2024 account-rail fields BK51/BK52_b, so no annual P2P comparison is inferred.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "years": [item["year"] for item in annual]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
