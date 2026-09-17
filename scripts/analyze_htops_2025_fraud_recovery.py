#!/usr/bin/env python3
"""Run a bounded, weighted April 2025 HTOPS fraud/recovery screen."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


EXPECTED = {
    "FRAUD1": "FRAUD1",
    "FRAUD2": "FRAUD2",
    "FRAUD4": "FRAUD4",
    "FRAUD5_amount": "TFRAUD5",
    "FRAUD6": "FRAUD6",
    "life_satisfaction": "SATISFACTION",
    "social_support": "SOCIAL1_first",
    "loneliness": "SOCIAL2_first",
    "institutional_trust": "TRUST1",
    "statistics_policy_trust": "FEDSTAT_TRUST",
    "person_weight": "PWEIGHT",
    "respondent_id": "SCRAMID",
}


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


def weighted_share(rows: list[dict[str, str]], predicate, denominator=None) -> dict:
    eligible = [row for row in rows if (denominator(row) if denominator else True) and number(row["PWEIGHT"]) and number(row["PWEIGHT"]) > 0]
    total = sum(number(row["PWEIGHT"]) for row in eligible)
    selected = sum(number(row["PWEIGHT"]) for row in eligible if predicate(row))
    return {
        "weighted_percent": round(100 * selected / total, 4) if total else None,
        "unweighted_valid_n": len(eligible),
        "weighted_denominator": round(total, 4),
    }


def dictionary_map(path: Path) -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    import openpyxl

    sheet = openpyxl.load_workbook(path, read_only=True, data_only=True).active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        question_id, _, variable, label, _, _, values, universe, _ = row
        if variable:
            mapping[str(variable)] = {
                "question_id": str(question_id),
                "label": str(label),
                "values": str(values),
                "universe": str(universe),
            }
    return mapping


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--puf", type=Path, required=True)
    parser.add_argument("--dictionary", type=Path, required=True)
    parser.add_argument("--replicate-weights", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "analysis/projects/us-cost-trust-politics/data/htops-2025-fraud-recovery-screen-2025-04.json",
    )
    args = parser.parse_args()

    dictionary = dictionary_map(args.dictionary)
    with args.puf.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        missing = [variable for variable in EXPECTED.values() if variable not in columns]
        if missing:
            raise ValueError(f"PUF missing required columns: {missing}")
        missing_dictionary = [variable for variable in EXPECTED.values() if variable not in dictionary]
        if missing_dictionary:
            raise ValueError(f"dictionary missing required variables: {missing_dictionary}")
        rows = list(reader)

    if len(rows) == 0:
        raise ValueError("PUF contained no rows")
    if len({row["SCRAMID"] for row in rows}) != len(rows):
        raise ValueError("SCRAMID is not unique in the PUF")

    with args.replicate_weights.open(newline="", encoding="utf-8-sig") as handle:
        replicate_reader = csv.DictReader(handle)
        replicate_columns = replicate_reader.fieldnames or []
        required_replicates = ["SCRAMID"] + [f"PWEIGHT{i}" for i in range(81)]
        missing_replicates = [column for column in required_replicates if column not in replicate_columns]
        if missing_replicates:
            raise ValueError(f"replicate-weight file missing required columns: {missing_replicates}")
        replicate_ids = [row["SCRAMID"] for row in replicate_reader]
    puf_ids = {row["SCRAMID"] for row in rows}
    if len(replicate_ids) != len(rows) or len(set(replicate_ids)) != len(replicate_ids) or set(replicate_ids) != puf_ids:
        raise ValueError("replicate-weight IDs do not exactly match PUF IDs")

    valid_rows = [row for row in rows if valid(row["PWEIGHT"]) and number(row["PWEIGHT"]) > 0]
    exposed = lambda row: valid(row["FRAUD1"]) and number(row["FRAUD1"]) == 1
    lost = lambda row: exposed(row) and valid(row["FRAUD4"]) and number(row["FRAUD4"]) == 1
    reported = lambda row: exposed(row) and valid(row["FRAUD2"]) and number(row["FRAUD2"]) == 1
    recovered_universe = lambda row: lost(row) and reported(row) and valid(row["FRAUD6"])
    metrics = {
        "scam_exposure_among_valid_weighted_respondents": weighted_share(valid_rows, exposed, lambda row: valid(row["FRAUD1"])),
        "government_or_law_enforcement_reporting_among_exposed": weighted_share(valid_rows, reported, lambda row: exposed(row) and valid(row["FRAUD2"])),
        "money_loss_among_exposed": weighted_share(valid_rows, lost, lambda row: exposed(row) and valid(row["FRAUD4"])),
        "recovery_among_loss_and_report_universe": weighted_share(valid_rows, lambda row: number(row["FRAUD6"]) == 1, recovered_universe),
        "positive_reported_loss_amount_among_loss_universe": weighted_share(
            valid_rows,
            lambda row: number(row["TFRAUD5"]) is not None and number(row["TFRAUD5"]) > 0,
            lambda row: lost(row) and valid(row["TFRAUD5"]),
        ),
        "mean_life_satisfaction_among_valid_weighted_respondents": {
            "weighted_mean_0_to_10": round(
                sum(number(row["SATISFACTION"]) * number(row["PWEIGHT"]) for row in valid_rows if valid(row["SATISFACTION"]))
                / sum(number(row["PWEIGHT"]) for row in valid_rows if valid(row["SATISFACTION"])),
                4,
            ),
            "unweighted_valid_n": sum(valid(row["SATISFACTION"]) for row in valid_rows),
        },
    }

    code_counts = {}
    for variable in ("FRAUD1", "FRAUD2", "FRAUD4", "FRAUD6", "TRUST1", "FEDSTAT_TRUST"):
        code_counts[variable] = dict(sorted(Counter(row[variable] for row in rows).items()))

    output = {
        "format": "htops-2025-fraud-recovery-screen-v1",
        "status": "weighted_descriptive_screen",
        "checked": "2026-09-16",
        "period": "April 15–29, 2025; fraud questions refer to the prior 12 months",
        "source_unit": "April 2025 HTOPS topical PUF respondent",
        "rows": len(rows),
        "valid_positive_person_weight_rows": len(valid_rows),
        "candidate_variable_map": EXPECTED,
        "dictionary_metadata": {variable: dictionary[variable] for variable in sorted(set(EXPECTED.values()))},
        "metrics": metrics,
        "raw_code_counts": code_counts,
        "boundary": "This is a weighted descriptive screen. Fraud exposure is retrospective and does not identify an incident date, named actor, alternatives, effort, remedy timing, or later trust change. Reporting and agency recovery are distinct outcomes; no causal, longitudinal, practical-exit, or population-harm claim is promoted. TFRAUD5 is a topcoded amount field and is not treated as an exact uncensored loss total.",
        "source_files": {
            "puf": str(args.puf),
            "dictionary": str(args.dictionary),
            "replicate_weights": str(args.replicate_weights),
            "puf_sha256": sha256(args.puf),
            "dictionary_sha256": sha256(args.dictionary),
            "replicate_weights_sha256": sha256(args.replicate_weights),
            "replicate_weight_columns": len(replicate_columns),
            "replicate_weight_file_present_in_archive": True,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"VALID HTOPS fraud/recovery screen: {len(rows)} rows; output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
