#!/usr/bin/env python3
"""Run the storage-light March 2026 HTOPS social-connection screen.

The script reads the corrected PUF ZIP without extracting its respondent or
replicate files to disk. It validates exact SCRAMID and primary-weight
alignment, then estimates outcome shares by household expense difficulty.
Results are descriptive respondent-weighted conditional shares. The 80
successive-difference replicate weights supply precision diagnostics; no
longitudinal or causal estimator is implied.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import zipfile
from pathlib import Path


GROUPS = ("1", "2", "3", "4")
OUTCOMES = ("lonely", "support", "talk", "food")
AGE_BANDS = ("25_44", "45_64", "65_plus")


def code(value: str) -> str:
    return value.split(".", 1)[0]


def age_band(value: str) -> str | None:
    try:
        age = int(float(value))
    except (TypeError, ValueError):
        return None
    if 25 <= age <= 44:
        return "25_44"
    if 45 <= age <= 64:
        return "45_64"
    if age >= 65:
        return "65_plus"
    return None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def empty_cells() -> dict[str, dict[str, list[float]]]:
    return {group: {outcome: [0.0, 0.0] for outcome in OUTCOMES} for group in GROUPS}


def outcomes(row: dict[str, str]) -> dict[str, tuple[bool, bool]]:
    return {
        "lonely": (row["SOC_LONELY"] in {"1.0", "2.0"}, row["SOC_LONELY"] in {"1.0", "2.0", "3.0", "4.0", "5.0"}),
        "support": (row["SOC_SUPPORT"] in {"4.0", "5.0"}, row["SOC_SUPPORT"] in {"1.0", "2.0", "3.0", "4.0", "5.0"}),
        "talk": (row["SOC_TALK"] == "4.0", row["SOC_TALK"] in {"1.0", "2.0", "3.0", "4.0"}),
        "food": (row["FD_SUFF"] in {"3.0", "4.0"}, row["FD_SUFF"] in {"1.0", "2.0", "3.0", "4.0"}),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path, help="corrected HTOPS_HPS_2603_CSV.zip")
    parser.add_argument("--output", required=True, type=Path, help="derived JSON output path")
    parser.add_argument("--puf-member", default="HTOPS_HPS_2603_PUF.csv")
    parser.add_argument("--rep-member", default="HTOPS_HPS_2603_REPWGT_PUF.csv")
    args = parser.parse_args()

    with zipfile.ZipFile(args.zip) as archive:
        primary: dict[str, tuple[str, dict[str, str], float]] = {}
        all_main_ids: set[str] = set()
        all_primary_weights: dict[str, float] = {}
        main_rows = 0
        duplicate_main = 0
        with archive.open(args.puf_member) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            required = {"SCRAMID", "PWEIGHT", "EXPENSE_DIFFICULT", "TAGE", "SOC_LONELY", "SOC_SUPPORT", "SOC_TALK", "FD_SUFF"}
            missing = required - set(reader.fieldnames or [])
            if missing:
                raise SystemExit(f"PUF missing fields: {sorted(missing)}")
            for row in reader:
                main_rows += 1
                sid = row["SCRAMID"]
                all_main_ids.add(sid)
                if sid in primary:
                    duplicate_main += 1
                    continue
                try:
                    weight = float(row["PWEIGHT"])
                except (TypeError, ValueError):
                    continue
                all_primary_weights[sid] = weight
                group = code(row["EXPENSE_DIFFICULT"])
                if group in GROUPS:
                    primary[sid] = (group, row, weight)

        point = empty_cells()
        replicate = [empty_cells() for _ in range(80)]
        n_by_group = {group: 0 for group in GROUPS}
        age_point = {band: empty_cells() for band in AGE_BANDS}
        age_replicate = {band: [empty_cells() for _ in range(80)] for band in AGE_BANDS}
        age_n_by_group = {band: {group: 0 for group in GROUPS} for band in AGE_BANDS}
        seen: set[str] = set()
        duplicate_rep = 0
        extra_rep = 0
        max_weight_difference = 0.0
        rep_rows = 0
        with archive.open(args.rep_member) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            rep_columns = [f"PWEIGHT{i}" for i in range(81)]
            missing = set(rep_columns + ["SCRAMID"]) - set(reader.fieldnames or [])
            if missing:
                raise SystemExit(f"replicate file missing fields: {sorted(missing)}")
            for row in reader:
                rep_rows += 1
                sid = row["SCRAMID"]
                if sid in seen:
                    duplicate_rep += 1
                seen.add(sid)
                if sid not in all_main_ids:
                    extra_rep += 1
                item = primary.get(sid)
                if item is None:
                    continue
                group, source, base_weight = item
                if sid in all_primary_weights:
                    max_weight_difference = max(max_weight_difference, abs(float(row["PWEIGHT0"]) - all_primary_weights[sid]))
                n_by_group[group] += 1
                band = age_band(source["TAGE"])
                if band is not None:
                    age_n_by_group[band][group] += 1
                for name, (positive, valid) in outcomes(source).items():
                    if not valid:
                        continue
                    point[group][name][0] += base_weight * positive
                    point[group][name][1] += base_weight
                    for index in range(80):
                        weight = float(row[f"PWEIGHT{index + 1}"])
                        replicate[index][group][name][0] += weight * positive
                        replicate[index][group][name][1] += weight
                        if band is not None:
                            age_replicate[band][index][group][name][0] += weight * positive
                            age_replicate[band][index][group][name][1] += weight
                    if band is not None:
                        age_point[band][group][name][0] += base_weight * positive
                        age_point[band][group][name][1] += base_weight

    estimates: dict[str, dict[str, object]] = {}
    for group in GROUPS:
        estimates[group] = {"unweighted_n": n_by_group[group]}
        for name in OUTCOMES:
            numerator, denominator = point[group][name]
            estimate = 100.0 * numerator / denominator if denominator else math.nan
            replicate_estimates = []
            for cells in replicate:
                rep_num, rep_den = cells[group][name]
                replicate_estimates.append(100.0 * rep_num / rep_den if rep_den else math.nan)
            valid_replicates = [value for value in replicate_estimates if math.isfinite(value)]
            standard_error = math.sqrt(sum((value - estimate) ** 2 for value in valid_replicates) / 80.0) if valid_replicates else math.nan
            estimates[group][name] = {
                "estimate_pct": round(estimate, 3) if math.isfinite(estimate) else None,
                "se_pct_points": round(standard_error, 3) if math.isfinite(standard_error) else None,
                "valid_weighted_n": round(denominator) if denominator else 0,
            }

    age_estimates: dict[str, dict[str, dict[str, object]]] = {}
    for band in AGE_BANDS:
        age_estimates[band] = {}
        for group in GROUPS:
            age_estimates[band][group] = {"unweighted_n": age_n_by_group[band][group]}
            for name in OUTCOMES:
                numerator, denominator = age_point[band][group][name]
                estimate = 100.0 * numerator / denominator if denominator else math.nan
                replicate_estimates = []
                for cells in age_replicate[band]:
                    rep_num, rep_den = cells[group][name]
                    replicate_estimates.append(100.0 * rep_num / rep_den if rep_den else math.nan)
                valid_replicates = [value for value in replicate_estimates if math.isfinite(value)]
                standard_error = math.sqrt(sum((value - estimate) ** 2 for value in valid_replicates) / 80.0) if valid_replicates else math.nan
                age_estimates[band][group][name] = {
                    "estimate_pct": round(estimate, 3) if math.isfinite(estimate) else None,
                    "se_pct_points": round(standard_error, 3) if math.isfinite(standard_error) else None,
                    "valid_weighted_n": round(denominator) if denominator else 0,
                }

    result = {
        "format": "htops-2026-social-connection-screen-v1",
        "field_window": "March 13–30, 2026",
        "main_rows": main_rows,
        "replicate_rows": rep_rows,
        "valid_expense_rows": len(primary),
        "alignment": {
            "duplicate_main_ids": duplicate_main,
            "duplicate_replicate_ids": duplicate_rep,
            "missing_replicate_ids": len(all_main_ids - seen),
            "extra_replicate_ids": extra_rep,
            "max_abs_primary_weight_difference": max_weight_difference,
        },
        "weight": "PWEIGHT with PWEIGHT1–PWEIGHT80 successive-difference replicate weights",
        "estimates": estimates,
        "age_band_estimates": age_estimates,
        "input_sha256": f"sha256:{sha256(args.zip)}",
        "boundary": "Descriptive same-round respondent-weighted conditional shares; expense is household-reported, social outcomes are respondent-reported, and March 2026 is cross-sectional. No causal, longitudinal, or household-level loneliness estimator is implied.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "valid_expense_rows": len(primary), "groups": len(estimates)}, indent=2))


if __name__ == "__main__":
    main()
