#!/usr/bin/env python3
"""Build a bounded trend record from the Census July 2026 HTOPS/HPS PUF.

The input PUF and its dictionary are distributed by the Census Bureau.  This
script computes weighted descriptive shares only; it does not pool waves or
estimate a causal relationship.  Replicate weights are recorded as available
in the provenance note, but standard errors are intentionally not promoted
until the Census variance guidance is wired into the extractor.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


SOURCE_URL = "https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html"
FILE_URL = "https://www2.census.gov/programs-surveys/demo/datasets/hhp/2026/topical/HTOPS_HPS_2607_CSV.zip"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def weighted_share(rows: list[dict[str, str]], variable: str, predicate, subgroup=None):
    selected = []
    for row in rows:
        if subgroup is not None and not subgroup(row):
            continue
        try:
            value = float(row[variable])
            weight = float(row["PWEIGHT"])
        except (KeyError, TypeError, ValueError):
            continue
        if value in (-88, -99) or weight <= 0:
            continue
        selected.append((value, weight))
    total = sum(weight for _, weight in selected)
    if not selected or total <= 0:
        return None, len(selected)
    numerator = sum(weight for value, weight in selected if predicate(value))
    return round(100 * numerator / total, 1), len(selected)


def measure(rows, variable, name, predicate, unit="percent of weighted respondents"):
    value, n = weighted_share(rows, variable, predicate)
    return name, {"value": value, "unit": unit, "value_type": "share", "unweighted_valid_n": n}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("puf", type=Path)
    parser.add_argument("--zip", type=Path, required=True, help="Downloaded ZIP containing the PUF")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with args.puf.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows or "PWEIGHT" not in rows[0]:
        raise SystemExit("PUF must contain respondents and PWEIGHT")

    measures = dict([
        measure(rows, "EXPENSE_DIFFICULT", "any_expense_difficulty", lambda v: v in (2, 3, 4)),
        measure(rows, "EXPENSE_DIFFICULT", "very_or_somewhat_expense_difficulty", lambda v: v in (3, 4)),
        measure(rows, "PRICECHANGE", "perceive_prices_increased", lambda v: v == 1),
        measure(rows, "PRICECONCERN", "very_or_somewhat_concerned_about_future_price_increase", lambda v: v in (1, 2)),
        measure(rows, "ENERGY", "reduced_or_forgone_basic_needs_to_pay_energy_bill", lambda v: v == 1),
        measure(rows, "ENERGY_BILL", "unable_to_pay_full_energy_bill", lambda v: v == 1),
        measure(rows, "FD_SUFF", "sometimes_or_often_not_enough_food", lambda v: v in (3, 4)),
        measure(rows, "FD_FREE", "received_free_groceries", lambda v: v == 1),
        measure(rows, "FDBEN_SNAP", "currently_receives_snap", lambda v: v == 1),
        measure(rows, "ANXIOUS", "anxiety_more_than_half_or_nearly_every_day", lambda v: v in (3, 4)),
        measure(rows, "SOC_LONELY", "always_or_usually_lonely", lambda v: v in (1, 2)),
        measure(rows, "TRUST_FEDSTAT", "tends_to_trust_federal_statistics", lambda v: v == 1),
        measure(rows, "TRUST_CONGRESS", "great_deal_or_quite_a_lot_confidence_in_congress", lambda v: v in (1, 2)),
    ])
    record = {
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-census-htops-hps-material-trust-july-2026",
        "title": "Current household pressure and institutional trust coexist in the July 2026 Census pulse",
        "theme_ids": ["cost", "voice", "energy"],
        "program_theme_ids": [
            "household_room_consumption",
            "unequal_exposure_status",
            "care_health_reproduction",
            "trust_identity_meaning",
            "political_judgment_action",
        ],
        "source_unit": "US Census Bureau HTOPS/HPS July 2026 public-use person respondent",
        "geography": "United States",
        "observations": [{
            "period": "July 15–August 3, 2026 HTOPS/HPS cross-sectional topical release",
            "denominator": {
                "value": len(rows),
                "unit": "PUF respondents; weighted shares use positive PWEIGHT and variable-specific valid cases",
                "value_type": "survey_sample",
            },
            "measures": measures,
            "method": "Census July 2026 HTOPS/HPS CSV public-use file; weighted descriptive shares calculated with PWEIGHT after excluding -88 not-in-universe and -99 did-not-answer codes. The release includes 80 person replicate-weight columns, retained in the downloaded archive but not used for standard errors in this first point-estimate extraction.",
            "uncertainty": "Cross-sectional survey estimates are not a same-person event sequence and do not establish that prices, energy bills, food conditions, or institutions caused anxiety, loneliness, or trust. Valid denominators vary by item; nonresponse and survey design require replicate-weight variance before precision claims. The July file is a current pulse, not a trend by itself.",
            "subgroup": "All PUF respondents ages and universes defined by the July 2026 dictionary; income and sex subgroup cells remain available for the next stratified pass.",
            "counterinterpretation": "Households can report pressure while retaining food sufficiency, assistance, social support, or trust; trust in federal statistics is not trust in all institutions, and confidence in Congress is not political action or legitimacy.",
            "source_url": SOURCE_URL,
            "retrieval_hash": "sha256:" + sha256(args.zip),
            "status": "reported",
        }],
        "related_sources": [{
            "source_url": FILE_URL,
            "claim": "Official July 2026 HTOPS/HPS PUF ZIP containing the CSV respondent file, data dictionary, and replicate-weight file.",
            "status": "primary",
        }],
        "boundary": "This record provides current weighted distributions for household expense and price pressure, energy trade-offs, food sufficiency and assistance, selected mental/social measures, and institutional trust. It is not a longitudinal comparison, causal exposure design, political-action estimate, or evidence that material pressure changed trust.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(rows)} respondents")


if __name__ == "__main__":
    main()
