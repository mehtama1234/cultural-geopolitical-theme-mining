#!/usr/bin/env python3
"""Join bounded April and June 2025 HTOPS files for a descriptive fraud follow-up."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


APRIL_FIELDS = ["SCRAMID", "PWEIGHT", "FRAUD1", "FRAUD2", "FRAUD4", "FRAUD6"]
JUNE_FIELDS = ["SCRAMID", "CURFOODSUF", "HSE16", "WRKLOSSRV", "TRUST1", "TRUST2_CONGRESS", "FEDSTAT_TRUST"]


def number(value: str | None) -> float | None:
    try:
        return float(value) if value not in (None, "") else None
    except ValueError:
        return None


def valid(value: str | None) -> bool:
    parsed = number(value)
    return parsed is not None and parsed not in (-88, -99)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return "sha256:" + digest.hexdigest()


def read_selected(path: Path, fields: list[str]) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in fields if field not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"{path} missing required fields: {missing}")
        rows = {}
        for row in reader:
            key = row["SCRAMID"]
            if key in rows:
                raise ValueError(f"duplicate SCRAMID in {path}: {key}")
            rows[key] = {field: row[field] for field in fields}
    return rows


def weighted_share(rows: list[tuple[dict[str, str], dict[str, str]]], group, outcome) -> dict:
    eligible = [
        (april, june)
        for april, june in rows
        if group(april) and valid(april["PWEIGHT"]) and number(april["PWEIGHT"]) > 0 and outcome(june) is not None
    ]
    denominator = sum(number(april["PWEIGHT"]) for april, _ in eligible)
    numerator = sum(number(april["PWEIGHT"]) for april, june in eligible if outcome(june))
    return {
        "weighted_percent": round(100 * numerator / denominator, 4) if denominator else None,
        "unweighted_valid_n": len(eligible),
        "weighted_denominator": round(denominator, 4),
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--april", type=Path, required=True)
    parser.add_argument("--april-replicates", type=Path, required=True)
    parser.add_argument("--june", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "analysis/projects/us-cost-trust-politics/data/htops-2025-fraud-followup-2025-04-to-06.json",
    )
    args = parser.parse_args()

    april = read_selected(args.april, APRIL_FIELDS)
    june = read_selected(args.june, JUNE_FIELDS)
    with args.april_replicates.open(newline="", encoding="utf-8-sig") as handle:
        replicate_reader = csv.DictReader(handle)
        replicate_fields = replicate_reader.fieldnames or []
        required = ["SCRAMID"] + [f"PWEIGHT{i}" for i in range(81)]
        missing = [field for field in required if field not in replicate_fields]
        if missing:
            raise ValueError(f"April replicate file missing required fields: {missing}")
        april_rep_ids = [row["SCRAMID"] for row in replicate_reader]
    if set(april_rep_ids) != set(april) or len(april_rep_ids) != len(april) or len(set(april_rep_ids)) != len(april_rep_ids):
        raise ValueError("April replicate IDs do not exactly match April PUF IDs")

    ids = sorted(set(april) & set(june))
    pairs = [(april[key], june[key]) for key in ids]
    exposed = lambda row: valid(row["FRAUD1"]) and number(row["FRAUD1"]) == 1
    not_exposed = lambda row: valid(row["FRAUD1"]) and number(row["FRAUD1"]) == 2
    lost = lambda row: exposed(row) and valid(row["FRAUD4"]) and number(row["FRAUD4"]) == 1
    reported = lambda row: exposed(row) and valid(row["FRAUD2"]) and number(row["FRAUD2"]) == 1
    lost_reported = lambda row: lost(row) and reported(row)
    recovered = lambda row: lost_reported(row) and valid(row["FRAUD6"]) and number(row["FRAUD6"]) == 1
    groups = {
        "not_exposed": not_exposed,
        "exposed": exposed,
        "exposed_and_lost": lost,
        "exposed_and_reported": reported,
        "lost_and_reported": lost_reported,
        "lost_reported_and_recovered": recovered,
    }
    outcomes = {
        "june_food_insufficiency": lambda row: (number(row["CURFOODSUF"]) in (3, 4)) if valid(row["CURFOODSUF"]) else None,
        "june_unable_to_pay_energy_bill": lambda row: (number(row["HSE16"]) == 1) if valid(row["HSE16"]) else None,
        "june_recent_household_job_loss": lambda row: (number(row["WRKLOSSRV"]) == 1) if valid(row["WRKLOSSRV"]) else None,
        "june_trust_federal_statistics_code_1": lambda row: (number(row["TRUST1"]) == 1) if valid(row["TRUST1"]) else None,
        "june_confidence_in_congress_code_1": lambda row: (number(row["TRUST2_CONGRESS"]) == 1) if valid(row["TRUST2_CONGRESS"]) else None,
        "june_statistics_policy_trust_code_1": lambda row: (number(row["FEDSTAT_TRUST"]) == 1) if valid(row["FEDSTAT_TRUST"]) else None,
    }
    metrics = {
        group_name: {outcome_name: weighted_share(pairs, group, outcome) for outcome_name, outcome in outcomes.items()}
        for group_name, group in groups.items()
    }
    group_counts = {name: sum(group(row) for row, _ in pairs) for name, group in groups.items()}
    result = {
        "format": "htops-2025-fraud-followup-v1",
        "status": "same_respondent_weighted_descriptive_followup",
        "checked": "2026-09-16",
        "period": "April 15–29 to June 16–25, 2025",
        "linkage_key": "SCRAMID",
        "april_rows": len(april),
        "june_rows": len(june),
        "linked_ids": len(ids),
        "group_unweighted_counts": group_counts,
        "outcomes": list(outcomes),
        "weight": "April PWEIGHT applied to linked respondents; April replicate file schema and exact IDs verified but replicate variance is not used because an attrition-adjusted longitudinal weight is not documented.",
        "metrics": metrics,
        "boundary": "This is an associative same-respondent follow-up, not a causal fraud effect. April fraud questions refer to the prior 12 months; June outcomes are later survey responses but the incident date, actor, alternatives, effort, remedy timing, and trust change are not observed. Linked retention and selective response can bias the descriptive cells. Code-1 trust measures are reported as coding screens, not substantive high-trust labels without the dictionary category interpretation.",
        "source_files": {
            "april_puf": str(args.april),
            "april_replicates": str(args.april_replicates),
            "june_puf": str(args.june),
            "april_puf_sha256": sha256(args.april),
            "april_replicates_sha256": sha256(args.april_replicates),
            "june_puf_sha256": sha256(args.june),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"VALID HTOPS fraud follow-up: {len(ids)} linked IDs; output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
