#!/usr/bin/env python3
"""Build a bounded same-respondent April-to-June 2025 HTOPS panel record."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


SOURCE_URL = "https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.2025.html"

MEASURES = {
    "any_expense_difficulty": ("EXPNS_DIF", lambda v: v in (2, 3, 4)),
    "food_insufficiency": ("CURFOODSUF", lambda v: v in (3, 4)),
    "unable_to_pay_energy_bill": ("HSE16", lambda v: v == 1),
    "prices_increased": ("PRICECHNG", lambda v: v == 1),
    "recent_household_job_loss": ("WRKLOSSRV", lambda v: v == 1),
    "any_work_last_seven_days": ("ANYWORK", lambda v: v == 1),
    "agrees_policy_makers_need_federal_statistics": ("FEDSTAT_TRUST", lambda v: v in (1, 2)),
    "high_confidence_in_congress": ("TRUST2_CONGRESS", lambda v: v in (1, 2)),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def valid(row, variable):
    value = number(row.get(variable))
    weight = number(row.get("PWEIGHT"))
    return value is not None and weight is not None and value not in (-88, -99) and weight > 0


def transition_estimates(matched, baseline_reps, variable, predicate):
    cells = {"no_to_no": [], "no_to_yes": [], "yes_to_no": [], "yes_to_yes": []}
    for before, after in matched:
        if not valid(before, variable) or not valid(after, variable):
            continue
        b = bool(predicate(number(before[variable])))
        a = bool(predicate(number(after[variable])))
        key = ("yes" if b else "no") + "_to_" + ("yes" if a else "no")
        cells[key].append((before, after))
    result = {}
    all_valid = sum(len(items) for items in cells.values())
    for key, items in cells.items():
        target_ids = {before["SCRAMID"] for before, _ in items}
        full_denominator = sum(number(before["PWEIGHT"]) for all_items in cells.values() for before, _ in all_items)
        full_numerator = sum(number(before["PWEIGHT"]) for before, _ in items)
        point = full_numerator / full_denominator if full_denominator else None
        # Reuse the baseline replicate weights for the linked, retained sample.
        replicate_points = []
        for index in range(1, 81):
            den = 0.0
            num = 0.0
            for all_items in cells.values():
                for before, _ in all_items:
                    rep = baseline_reps.get(before["SCRAMID"], {})
                    weight = number(rep.get(f"PWEIGHT{index}"))
                    if weight is None or weight <= 0:
                        continue
                    den += weight
                    if before["SCRAMID"] in target_ids:
                        num += weight
            replicate_points.append(num / den if den else 0.0)
        variance = 4 / 80 * sum((x - point) ** 2 for x in replicate_points) if point is not None else None
        result[key] = {
            "value": round(point * 100, 1) if point is not None else None,
            "standard_error": round((variance ** 0.5) * 100, 2) if variance is not None else None,
            "unit": "percent of baseline-weighted valid linked respondents",
            "value_type": "linked_transition_share",
            "unweighted_cell_n": len(items),
            "unweighted_valid_n": all_valid,
        }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--baseline-rep", type=Path, required=True)
    parser.add_argument("--followup", type=Path, required=True)
    parser.add_argument("--followup-rep", type=Path, required=True)
    parser.add_argument("--baseline-zip", type=Path, required=True)
    parser.add_argument("--followup-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    baseline_rows = read_csv(args.baseline)
    followup_rows = read_csv(args.followup)
    baseline_by_id = {row["SCRAMID"]: row for row in baseline_rows}
    followup_by_id = {row["SCRAMID"]: row for row in followup_rows}
    overlap = sorted(set(baseline_by_id) & set(followup_by_id))
    matched = [(baseline_by_id[scramid], followup_by_id[scramid]) for scramid in overlap]
    baseline_rep = {row["SCRAMID"]: row for row in read_csv(args.baseline_rep)}
    followup_rep = {row["SCRAMID"]: row for row in read_csv(args.followup_rep)}
    if not overlap or set(overlap) - set(baseline_rep) or set(overlap) - set(followup_rep):
        raise SystemExit("linked PUF rows and replicate-weight IDs do not align")

    transition_measures = {}
    for name, (variable, predicate) in MEASURES.items():
        transition_measures[name] = transition_estimates(matched, baseline_rep, variable, predicate)

    record = {
        "format": "us-trend-observation-record-v1",
        "trend_id": "us-census-htops-material-trust-panel-april-june-2025",
        "title": "Linked HTOPS respondents show material and institutional measures changing on different paths",
        "theme_ids": ["cost", "voice", "energy", "work"],
        "program_theme_ids": ["household_room_consumption", "unequal_exposure_status", "care_health_reproduction", "trust_identity_meaning", "work_control_bargaining", "political_judgment_action"],
        "source_unit": "US Census Bureau HTOPS April and June 2025 linked public-use person respondents",
        "geography": "United States",
        "observations": [
            {
                "period": "April 15–29 to June 16–25, 2025; linked respondent transitions",
                "denominator": {"value": len(overlap), "unit": "respondents linked by SCRAMID across April and June PUFs; baseline-weighted valid denominator varies by measure", "value_type": "linked_panel_sample"},
                "measures": {"baseline_sample_n": {"value": len(baseline_rows), "unit": "April PUF respondents", "value_type": "sample_count"}, "followup_sample_n": {"value": len(followup_rows), "unit": "June PUF respondents", "value_type": "sample_count"}, "linked_retention_from_baseline_percent": {"value": round(100 * len(overlap) / len(baseline_rows), 1), "unit": "percent of April PUF IDs linked in June", "value_type": "retention_share"}, "linked_retention_from_followup_percent": {"value": round(100 * len(overlap) / len(followup_rows), 1), "unit": "percent of June PUF IDs linked in April", "value_type": "retention_share"}, **{f"{name}_{cell}": value for name, cells in transition_measures.items() for cell, value in cells.items()}},
                "method": "Inner join of April and June 2025 public-use files on SCRAMID; transition cells use the April PWEIGHT among linked respondents. Approximate standard errors use the April successive-difference replicate weights for the retained linked sample. This is a linked descriptive panel extraction, not a nationally reweighted longitudinal estimator.",
                "uncertainty": "The linked sample is a selected retained subset; April cross-sectional weights are not a documented longitudinal attrition-adjusted weight. Panel nonresponse, refresh/replenishment, item missingness, and question reference periods limit population interpretation. The transition cells do not establish that prices, bills, jobs, or institutions caused a later response.",
                "subgroup": "All linked respondents; the PUF retains sex, age, race/ethnicity, income, household composition, and geography for a later attrition and transition audit.",
                "counterinterpretation": "A yes-to-no transition can reflect recovery, temporary timing, reporting variation, or sample retention; a no-to-yes transition can reflect a new exposure, recall difference, or ordinary fluctuation. Agreement that policymakers need federal statistics is not the same measure as trust in federal statistics used in 2026.",
                "source_url": SOURCE_URL,
                "retrieval_hash": "sha256:" + sha256(args.baseline_zip),
                "status": "compared",
            },
        ],
        "related_sources": [{"source_url": "https://www2.census.gov/programs-surveys/demo/datasets/hhp/2025/topical/HTOPS_HPS_2506_CSV.zip", "claim": "June 2025 PUF, replicate weights, and dictionary package.", "status": "primary"}],
        "boundary": "This record is the first same-respondent April-to-June 2025 HTOPS linkage. It measures descriptive transitions among linked respondents and preserves the absence of a longitudinal attrition-adjusted weight; it does not estimate national causal effects, household recovery, trust formation, or political action.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(overlap)} linked respondents")


if __name__ == "__main__":
    main()
