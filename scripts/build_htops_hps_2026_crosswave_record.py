#!/usr/bin/env python3
"""Build a replicate-weighted March/May/July 2026 HTOPS/HPS comparison."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


SOURCE_URL = "https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html"
USER_NOTE_URL = "https://www.census.gov/programs-surveys/household-pulse-survey/technical-documentation/user-notes.html"

MEASURES = {
    "any_expense_difficulty": ("EXPENSE_DIFFICULT", lambda v: v in (2, 3, 4)),
    "sometimes_or_often_not_enough_food": ("FD_SUFF", lambda v: v in (3, 4)),
    "reduced_or_forgone_basic_needs_to_pay_energy_bill": ("ENERGY", lambda v: v == 1),
    "tends_to_trust_federal_statistics": ("TRUST_FEDSTAT", lambda v: v == 1),
    "great_deal_or_quite_a_lot_confidence_in_congress": ("TRUST_CONGRESS", lambda v: v in (1, 2)),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def numeric(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def valid(row, variable: str) -> bool:
    value = numeric(row.get(variable))
    weight = numeric(row.get("PWEIGHT"))
    return value is not None and weight is not None and value not in (-88, -99) and weight > 0


def domain(row, name: str) -> bool:
    if name == "all":
        return True
    if name == "income_under_50k":
        value = numeric(row.get("RHHINCOME"))
        return value in (1, 2, 3)
    if name == "income_100k_plus":
        value = numeric(row.get("RHHINCOME"))
        return value in (6, 7)
    if name == "female":
        return numeric(row.get("ESEX")) == 2
    if name == "male":
        return numeric(row.get("ESEX")) == 1
    if name == "children_in_household":
        value = numeric(row.get("THHLD_NUMKID"))
        return value is not None and value > 0
    if name == "no_children_in_household":
        return numeric(row.get("THHLD_NUMKID")) == 0
    raise ValueError(f"unknown domain: {name}")


def estimate(rows, replicate_rows, variable: str, predicate, domain_name: str):
    pairs = []
    for row, reps in zip(rows, replicate_rows):
        if not valid(row, variable) or not domain(row, domain_name):
            continue
        value = numeric(row[variable])
        weight = numeric(row["PWEIGHT"])
        replicate_weights = [numeric(reps.get(f"PWEIGHT{i}")) for i in range(1, 81)]
        if any(w is None or w <= 0 for w in replicate_weights):
            continue
        pairs.append((value, weight, replicate_weights))
    if not pairs:
        return {"value": None, "standard_error": None, "unweighted_valid_n": 0}
    total_weight = sum(item[1] for item in pairs)
    point = sum(item[1] for item in pairs if predicate(item[0])) / total_weight
    rep_points = []
    for index in range(80):
        rep_weight = sum(item[2][index] for item in pairs)
        rep_points.append(sum(item[2][index] for item in pairs if predicate(item[0])) / rep_weight)
    variance = 4 / 80 * sum((rep - point) ** 2 for rep in rep_points)
    return {
        "value": round(point * 100, 1),
        "standard_error": round((variance ** 0.5) * 100, 2),
        "unweighted_valid_n": len(pairs),
        "value_type": "replicate_weighted_share",
        "unit": "percent of weighted valid respondents",
    }


def parse_spec(spec: str):
    fields = spec.split("|")
    if len(fields) != 4:
        raise argparse.ArgumentTypeError("wave spec must be LABEL|PUF|REPWGT|ZIP")
    return fields[0], Path(fields[1]), Path(fields[2]), Path(fields[3])


def build_contrasts(observations):
    """Add approximate independent-snapshot 90% intervals for headline cells."""
    headline = [
        "any_expense_difficulty",
        "sometimes_or_often_not_enough_food",
        "reduced_or_forgone_basic_needs_to_pay_energy_bill",
        "tends_to_trust_federal_statistics",
        "great_deal_or_quite_a_lot_confidence_in_congress",
        "income_under_50k_any_expense_difficulty",
        "income_100k_plus_any_expense_difficulty",
    ]
    contrasts = []
    for first, second in zip(observations, observations[1:]):
        for measure in headline:
            a = first["measures"][measure]
            b = second["measures"][measure]
            difference = b["value"] - a["value"]
            difference_se = (a["standard_error"] ** 2 + b["standard_error"] ** 2) ** 0.5
            margin = 1.645 * difference_se
            contrasts.append({
                "from": first["period"],
                "to": second["period"],
                "measure": measure,
                "difference_percentage_points": round(difference, 1),
                "approx_independent_standard_error": round(difference_se, 2),
                "approx_90_percent_interval": [round(difference - margin, 1), round(difference + margin, 1)],
                "interpretation": "Independent-snapshot contrast; interval is approximate and is not a within-person or causal estimate.",
            })
    return contrasts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave", action="append", type=parse_spec, required=True, help="LABEL|PUF|REPWGT|ZIP")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    observations = []
    domains = ["all", "income_under_50k", "income_100k_plus", "female", "male", "children_in_household", "no_children_in_household"]
    for label, puf_path, rep_path, zip_path in args.wave:
        rows = read_csv(puf_path)
        replicate_rows = read_csv(rep_path)
        by_id = {row.get("SCRAMID"): row for row in replicate_rows}
        aligned_replicates = [by_id.get(row.get("SCRAMID"), {}) for row in rows]
        measures = {}
        for measure_name, (variable, predicate) in MEASURES.items():
            for domain_name in domains:
                key = measure_name if domain_name == "all" else f"{domain_name}_{measure_name}"
                measures[key] = estimate(rows, aligned_replicates, variable, predicate, domain_name)
        observations.append({
            "period": label,
            "denominator": {
                "value": len(rows),
                "unit": "PUF respondents; measure-specific valid domains reported in each measure",
                "value_type": "survey_sample",
            },
            "measures": measures,
            "method": "Census HTOPS/HPS corrected public-use PUF and 80 replicate-weight file; point estimates use PWEIGHT and standard errors use successive-difference replication, Var(theta)=4/80 sum((theta_i-theta_hat)^2). Missing -88 and -99 values are excluded item-by-item.",
            "uncertainty": "The three releases are independent cross-sectional snapshots after HTOPS changed from a longitudinal design in 2025 to a cross-sectional HPS-focused design in March 2026. Differences are not within-person changes. Standard errors reflect the supplied replicate-weight design but not systematic nonresponse or wording effects.",
            "subgroup": "All respondents plus income-under-$50,000, income-$100,000-plus, female, male, children-present, and no-children domains where the July dictionary coding is shared; domain universes and missingness remain item-specific.",
            "counterinterpretation": "A change in a weighted share can reflect sampling, composition, item routing, wording, or a real population change. It does not identify a price cause, assistance adequacy, institutional blame, trust mechanism, or political action.",
            "source_url": SOURCE_URL,
            "retrieval_hash": "sha256:" + sha256(zip_path),
            "status": "compared",
        })
    record = {
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-census-htops-hps-material-trust-crosswave-2026",
        "title": "Census pulse snapshots show which household-pressure and trust measures move together across 2026",
        "theme_ids": ["cost", "voice", "energy"],
        "program_theme_ids": ["household_room_consumption", "unequal_exposure_status", "care_health_reproduction", "trust_identity_meaning", "political_judgment_action"],
        "source_unit": "US Census Bureau HTOPS/HPS March, corrected May, and July 2026 public-use person respondents",
        "geography": "United States",
        "observations": observations,
        "cross_wave_contrasts": build_contrasts(observations),
        "related_sources": [
            {"source_url": USER_NOTE_URL, "claim": "Census user notes identify the corrected March and May files and the July release.", "status": "primary"},
            {"source_url": "https://www2.census.gov/programs-surveys/demo/technical-documentation/hhp/HTOPS_2605_Source_and_Accuracy.pdf", "claim": "Census successive-difference replication formula and 80-replicate variance guidance.", "status": "primary"},
        ],
        "boundary": "This is a replicate-weighted comparison of three independent 2026 cross-sectional HTOPS/HPS snapshots. It tests subgroup distributions and period movement, not within-person change, causality, institutional blame, trust formation, recovery, or political action.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(observations)} observations")


if __name__ == "__main__":
    main()
