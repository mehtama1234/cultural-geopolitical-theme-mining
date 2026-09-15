#!/usr/bin/env python3
"""Compute weighted SHED 2024 fraud and recovery outcomes by available subgroups."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from pathlib import Path

OUT = Path("analysis/projects/us-consumer-fraud-trust/data/shed-fraud-subgroups-2024.json")


def rows(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        name = next(n for n in archive.namelist() if n.endswith(".csv"))
        with archive.open(name) as handle:
            return [{key.lower(): value for key, value in row.items()} for row in csv.DictReader((line.decode("utf-8-sig") for line in handle))]


def clean(v: str | None) -> str:
    return (v or "").strip()


def weighted_share(data: list[dict[str, str]], predicate) -> float | None:
    valid = [(r, float(r["weight"])) for r in data if clean(r.get("weight")) not in {"", "."}]
    denom = sum(w for r, w in valid)
    return round(sum(w for r, w in valid if predicate(r)) / denom * 100, 3) if denom else None


def condition(data: list[dict[str, str]], field: str, labels: dict[str, str], universe=None) -> list[dict]:
    result = []
    for code, label in labels.items():
        group = [r for r in data if clean(r.get(field)) == code and (universe(r) if universe else True)]
        exposure = weighted_share(group, lambda r: clean(r.get("bk47_b")) == "Yes")
        fraud = [r for r in group if clean(r.get("bk47_b")) == "Yes"]
        lost = weighted_share(fraud, lambda r: clean(r.get("bk48")).startswith("I lost money"))
        unrecovered = weighted_share(fraud, lambda r: "some of it" in clean(r.get("bk48")) or "none of it" in clean(r.get("bk48")))
        time_10h = weighted_share(fraud, lambda r: clean(r.get("bk50")) in {"10 to 39 hours", "40 to 79 hours", "80 hours or more"})
        result.append({"group": label, "code": code, "all_adult_rows": len(group), "fraud_rows": len(fraud), "financial_fraud_exposure_percent": exposure, "lost_money_among_other_fraud_percent": lost, "some_or_all_unrecovered_among_other_fraud_percent": unrecovered, "10_or_more_hours_among_other_fraud_percent": time_10h})
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    data = rows(args.input)
    results = {
        "format": "shed-fraud-subgroups-2024-v1",
        "source_unit": "US adult SHED 2024 respondent",
        "weight": "weight",
        "respondent_rows": len(data),
        "definitions": {"financial_fraud_exposure": "BK47_b = 1 (another type of financial fraud or scam)", "lost_money": "BK48 in 1,2,3", "some_or_all_unrecovered": "BK48 in 2,3", "time_10_or_more_hours": "BK50 in 3,4,5"},
        "age": condition(data, "ppagect4", {"18–29": "18–29", "30–44": "30–44", "45–59": "45–59", "60+": "60+"}),
        "income": condition(data, "ppinc7", {"Less than $10,000": "<$10,000", "$10,000 to $24,999": "$10,000–$24,999", "$25,000 to $49,999": "$25,000–$49,999", "$50,000 to $74,999": "$50,000–$74,999", "$75,000 to $99,999": "$75,000–$99,999", "$100,000 to $149,999": "$100,000–$149,999", "$150,000 or more": "$150,000+"}),
        "account_rail_among_other_fraud": condition([r for r in data if clean(r.get("bk51")) == "Yes"], "bk52_b", {"No": "not P2P", "Yes": "P2P service"}, universe=lambda r: clean(r.get("bk52_b")) in {"No", "Yes"}),
        "home_language_subsample": condition(data, "pphi0001", {"Only Spanish": "Only Spanish", "More Spanish than English": "More Spanish than English", "Both Spanish and English equally": "Spanish and English equally", "More English than Spanish": "More English than Spanish", "Only English": "Only English", "Neither Spanish nor English": "Neither Spanish nor English"}),
        "measurement_gaps": ["The public 2024 file does not expose a general all-adult disability indicator suitable for this fraud path; D22_g is conditional on not working or working under 35 hours and is not used here.", "The public 2024 file does not expose a clean general digital-access measure suitable for this fraud path.", "Home-language variables are available only for the Hispanic oversample/module and are not a general language measure; these subgroup results are not population estimates for all adults by language."],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({k: results[k] for k in ("respondent_rows", "age", "income", "account_rail_among_other_fraud", "home_language_subsample", "measurement_gaps")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
