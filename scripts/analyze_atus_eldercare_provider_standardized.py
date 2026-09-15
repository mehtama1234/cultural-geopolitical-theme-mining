#!/usr/bin/env python3
"""Standardize ATUS eldercare-provider time contrasts to a pooled composition."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

from analyze_atus_time_care_2024 import make_person_minutes, read_dat


OUTCOMES = [
    "household_work",
    "care_for_people",
    "work",
    "travel",
    "socializing_communicating",
    "secondary_childcare",
    "eldercare",
]


def archive_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def prepare_frame(respondent_path: Path, summary_path: Path, activity_path: Path, roster_path: Path) -> pd.DataFrame:
    summary = read_dat(summary_path)
    activity = read_dat(activity_path)
    required = {"TUCASEID", "TUFINLWGT", "TEAGE", "TESEX", "TELFS", "TRCHILDNUM", "PEEDUCA"}
    missing = required - set(summary.columns)
    if missing:
        raise ValueError(f"summary file missing {sorted(missing)}")
    person = make_person_minutes(activity)
    frame = summary[["TUCASEID", "TUFINLWGT", "TEAGE", "TESEX", "TELFS", "TRCHILDNUM", "PEEDUCA"]].copy()
    frame["TUCASEID"] = frame["TUCASEID"].astype(str)
    frame = frame.merge(person, on="TUCASEID", how="inner", validate="one_to_one")
    roster = read_dat(roster_path)
    roster["TUCASEID"] = roster["TUCASEID"].astype(str)
    provider_ids = set(roster["TUCASEID"].dropna())
    frame["eldercare_provider"] = frame["TUCASEID"].isin(provider_ids).astype(int)
    frame["TEAGE"] = pd.to_numeric(frame["TEAGE"], errors="coerce")
    frame["TESEX"] = pd.to_numeric(frame["TESEX"], errors="coerce")
    frame["TELFS"] = pd.to_numeric(frame["TELFS"], errors="coerce")
    frame["TRCHILDNUM"] = pd.to_numeric(frame["TRCHILDNUM"], errors="coerce")
    frame["PEEDUCA"] = pd.to_numeric(frame["PEEDUCA"], errors="coerce")
    frame["TUFINLWGT"] = pd.to_numeric(frame["TUFINLWGT"], errors="coerce")
    frame = frame[frame["TUFINLWGT"].notna() & (frame["TUFINLWGT"] > 0)].copy()
    frame["age_band"] = pd.cut(
        frame["TEAGE"],
        bins=[14, 24, 44, 64, 120],
        labels=["15-24", "25-44", "45-64", "65+"],
    )
    frame["has_household_child"] = (frame["TRCHILDNUM"] > 0).astype("Int64")
    frame["education_band"] = pd.cut(
        frame["PEEDUCA"],
        bins=[30, 39, 41, 46],
        labels=["high-school-or-less", "some-college-or-associate", "bachelor-or-more"],
    )
    frame["cell"] = (
        frame["age_band"].astype(str)
        + "|sex="
        + frame["TESEX"].astype("Int64").astype(str)
        + "|lfs="
        + frame["TELFS"].astype("Int64").astype(str)
        + "|child="
        + frame["has_household_child"].astype(str)
        + "|edu="
        + frame["education_band"].astype(str)
    )
    return frame


def standardized_difference(frame: pd.DataFrame, replicate_weights: pd.DataFrame, outcome: str) -> dict:
    valid = frame[["cell", "eldercare_provider", "TUFINLWGT", outcome]].notna().all(axis=1)
    valid &= frame["TUFINLWGT"] > 0
    base = frame.loc[valid].copy()
    # Retain only cells represented by both provider statuses.
    support = base.groupby(["cell", "eldercare_provider"], observed=True).size().unstack(fill_value=0)
    common = support.index[(support.get(0, 0) > 0) & (support.get(1, 0) > 0)]
    base = base[base["cell"].isin(common)].copy()
    if base.empty:
        return {"value": None, "standard_error": None, "common_cells": 0, "provider_n": 0, "nonprovider_n": 0}

    def estimate(weights: pd.Series) -> float:
        work = base.assign(_weight=np.asarray(weights.loc[base.index], dtype=float))
        target = work.groupby("cell", observed=True)["_weight"].sum()
        target = target / target.sum()
        means = work.groupby(["eldercare_provider", "cell"], observed=True).apply(
            lambda g: float(np.average(g[outcome], weights=g["_weight"])),
            include_groups=False,
        )
        provider = float(sum(target[cell] * means[(1, cell)] for cell in common))
        nonprovider = float(sum(target[cell] * means[(0, cell)] for cell in common))
        return provider - nonprovider

    point = estimate(frame["TUFINLWGT"])
    reps = [estimate(replicate_weights[column]) for column in replicate_weights.columns]
    se = float(np.sqrt((4 / len(reps)) * sum((x - point) ** 2 for x in reps)))
    return {
        "value": point,
        "standard_error": se,
        "common_cells": int(len(common)),
        "provider_n": int((base["eldercare_provider"] == 1).sum()),
        "nonprovider_n": int((base["eldercare_provider"] == 0).sum()),
        "formula": "pooled age-band x sex x labor-force-status standardization; sqrt((4/160) * sum((replicate difference - point difference)^2))",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--respondent", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--activity", required=True, type=Path)
    parser.add_argument("--replicate", required=True, type=Path)
    parser.add_argument("--eldercare-roster", required=True, type=Path)
    parser.add_argument("--year", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    frame = prepare_frame(args.respondent, args.summary, args.activity, args.eldercare_roster)
    replicate = read_dat(args.replicate)
    rep_cols = [column for column in replicate.columns if column.startswith("FINLWGT")]
    if len(rep_cols) != 160:
        raise ValueError(f"expected 160 replicate weights, found {len(rep_cols)}")
    replicate["TUCASEID"] = replicate["TUCASEID"].astype(str)
    frame = frame.merge(replicate[["TUCASEID", *rep_cols]], on="TUCASEID", how="inner", validate="one_to_one")
    replicate_weights = frame[rep_cols].apply(pd.to_numeric, errors="coerce")

    results = {outcome: standardized_difference(frame, replicate_weights, outcome) for outcome in OUTCOMES}
    result = {
        "format": "atus-eldercare-provider-standardized-v1",
        "year": args.year,
        "source_unit": "ATUS respondent age 15+ with one selected diary day",
        "geography": "United States",
        "merged_respondents": int(len(frame)),
        "provider_respondents": int(frame["eldercare_provider"].sum()),
        "nonprovider_respondents": int((frame["eldercare_provider"] == 0).sum()),
        "covariates": "pooled age bands 15-24, 25-44, 45-64, 65+ crossed with TESEX, TELFS, binary TRCHILDNUM>0 household-child indicator, and broad PEEDUCA education bands",
        "results": results,
        "method": "Aggregate activity rows by TUCASEID, define provider status from any eldercare-roster record, and standardize provider minus nonprovider time means to the pooled distribution of supported age-band x sex x labor-force-status x household-child x education cells.",
        "uncertainty": "ATUS 160 replicate-weight standard errors are propagated through the standardized difference. This is an adjusted descriptive association, not a causal estimate; supported-cell overlap is required.",
        "files": {
            "respondent": {"path": str(args.respondent), "sha256": archive_hash(args.respondent)},
            "summary": {"path": str(args.summary), "sha256": archive_hash(args.summary)},
            "activity": {"path": str(args.activity), "sha256": archive_hash(args.activity)},
            "replicate": {"path": str(args.replicate), "sha256": archive_hash(args.replicate)},
            "eldercare_roster": {"path": str(args.eldercare_roster), "sha256": archive_hash(args.eldercare_roster)},
        },
        "boundary": "Provider status is not randomized or dated. Standardization addresses only the listed age, sex, and labor-force composition; health, family structure, recipient need, diary timing, schedule control, and care intensity remain open.",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"wrote {args.output} for {len(frame)} respondents")


if __name__ == "__main__":
    main()
