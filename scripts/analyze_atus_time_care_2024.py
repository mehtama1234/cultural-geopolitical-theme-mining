#!/usr/bin/env python3
"""Build weighted 2024 ATUS time/care estimates from official ZIP files."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import pandas as pd


ACTIVITY_PREFIXES = {
    "household_work": {"02"},
    "care_for_people": {"03", "04"},
    "work": {"05"},
    "travel": {"18"},
    "socializing_communicating": {"12"},
}


def archive_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_dat(path: Path) -> pd.DataFrame:
    with zipfile.ZipFile(path) as archive:
        members = [name for name in archive.namelist() if name.endswith(".dat")]
        if len(members) != 1:
            raise ValueError(f"expected one .dat member in {path}, found {members}")
        with archive.open(members[0]) as handle:
            return pd.read_csv(handle, na_values=[-1, -2, -3], low_memory=False)


def weighted_mean(values: pd.Series, weights: pd.Series) -> float | None:
    valid = values.notna() & weights.notna() & (weights > 0)
    if not valid.any():
        return None
    return float((values[valid] * weights[valid]).sum() / weights[valid].sum())


def weighted_share(values: pd.Series, weights: pd.Series) -> float | None:
    valid = values.notna() & weights.notna() & (weights > 0)
    if not valid.any():
        return None
    return float((values[valid] * weights[valid]).sum() / weights[valid].sum() * 100)


def make_person_minutes(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.copy()
    activity["TUCASEID"] = activity["TUCASEID"].astype(str)
    activity["TRCODE"] = pd.to_numeric(activity["TRCODE"], errors="coerce").fillna(-1).astype(int).astype(str).str.zfill(6)
    activity["TUACTDUR24"] = pd.to_numeric(activity["TUACTDUR24"], errors="coerce").fillna(0)
    activity["TRTCCTOT_LN"] = pd.to_numeric(activity["TRTCCTOT_LN"], errors="coerce").fillna(0)
    activity["TRTEC_LN"] = pd.to_numeric(activity["TRTEC_LN"], errors="coerce").fillna(0)
    rows = []
    for case_id, group in activity.groupby("TUCASEID", sort=False):
        prefixes = group["TRCODE"].str[:2]
        row = {"TUCASEID": case_id}
        for name, wanted in ACTIVITY_PREFIXES.items():
            minutes = group.loc[prefixes.isin(wanted), "TUACTDUR24"].sum()
            row[name] = float(minutes)
        row["secondary_childcare"] = float(group["TRTCCTOT_LN"].sum())
        row["eldercare"] = float(group["TRTEC_LN"].sum())
        rows.append(row)
    return pd.DataFrame(rows)


def replicate_se(values: pd.Series, weights: pd.DataFrame, point: float) -> float | None:
    valid = values.notna() & weights.notna().all(axis=1) & (weights > 0).all(axis=1)
    if not valid.any():
        return None
    x = values[valid].to_numpy(dtype=float)
    w = weights.loc[valid].to_numpy(dtype=float)
    estimates = (x[:, None] * w).sum(axis=0) / w.sum(axis=0)
    return float(((4 / len(weights.columns)) * ((estimates - point) ** 2).sum()) ** 0.5)


def group_estimate(frame: pd.DataFrame, label: str, replicate_weights: pd.DataFrame | None = None) -> dict:
    weights = frame["TUFINLWGT"]
    measures = {}
    minute_fields = [*ACTIVITY_PREFIXES, "secondary_childcare", "eldercare"]
    for field in minute_fields:
        values = frame[field]
        point = weighted_mean(values, weights)
        estimate = {
            "value": point,
            "unit": "weighted mean minutes per diary day among people age 15+",
            "value_type": "estimate",
            "valid_unweighted": int((values.notna() & weights.notna() & (weights > 0)).sum()),
        }
        if replicate_weights is not None and point is not None:
            estimate["standard_error"] = replicate_se(values, replicate_weights, point)
            estimate["uncertainty_unit"] = "minutes"
        measures[f"{field}_minutes"] = estimate
        participation_values = (values > 0).astype(float)
        share = weighted_share(participation_values, weights)
        share_estimate = {
            "value": share,
            "unit": "weighted percent participating on diary day",
            "value_type": "share",
            "valid_unweighted": int((values.notna() & weights.notna() & (weights > 0)).sum()),
        }
        if replicate_weights is not None and share is not None:
            share_estimate["standard_error"] = replicate_se(participation_values, replicate_weights, share)
            share_estimate["uncertainty_unit"] = "percentage points"
        measures[f"{field}_participation"] = share_estimate
    return {"group": label, "unweighted_n": int(len(frame)), "measures": measures}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--respondent", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--activity", required=True, type=Path)
    parser.add_argument("--replicate", type=Path)
    parser.add_argument("--eldercare-roster", type=Path)
    parser.add_argument("--year", type=int, default=2024)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    respondent = read_dat(args.respondent)
    summary = read_dat(args.summary)
    activity = read_dat(args.activity)
    required = {"TUCASEID", "TUFINLWGT", "TEAGE", "TESEX", "TELFS"}
    missing = required - set(summary.columns)
    if missing:
        raise ValueError(f"respondent file missing {sorted(missing)}")
    person = make_person_minutes(activity)
    frame = summary[["TUCASEID", "TUFINLWGT", "TEAGE", "TESEX", "TELFS"]].copy()
    frame["TUCASEID"] = frame["TUCASEID"].astype(str)
    frame = frame.merge(person, on="TUCASEID", how="inner", validate="one_to_one")
    frame["TEAGE"] = pd.to_numeric(frame["TEAGE"], errors="coerce")
    frame["TESEX"] = pd.to_numeric(frame["TESEX"], errors="coerce")
    frame["TELFS"] = pd.to_numeric(frame["TELFS"], errors="coerce")
    frame["TUFINLWGT"] = pd.to_numeric(frame["TUFINLWGT"], errors="coerce")
    frame = frame[frame["TUFINLWGT"].notna() & (frame["TUFINLWGT"] > 0)]
    replicate_weights = None
    if args.replicate:
        replicate = read_dat(args.replicate)
        rep_cols = [column for column in replicate.columns if column.startswith("FINLWGT")]
        if len(rep_cols) != 160:
            raise ValueError(f"expected 160 replicate weights, found {len(rep_cols)}")
        replicate["TUCASEID"] = replicate["TUCASEID"].astype(str)
        replicate_weights = replicate[["TUCASEID", *rep_cols]]
        frame = frame.merge(replicate_weights, on="TUCASEID", how="inner", validate="one_to_one")
        replicate_weights = frame[rep_cols].apply(pd.to_numeric, errors="coerce")

    groups = [group_estimate(frame, "all people age 15+", replicate_weights)]
    groups += [group_estimate(frame[frame["TESEX"] == code], label, replicate_weights.loc[frame["TESEX"] == code] if replicate_weights is not None else None) for code, label in [(1, "male"), (2, "female")]]
    age_bins = [(15, 24, "15-24"), (25, 44, "25-44"), (45, 64, "45-64"), (65, 120, "65+")]
    groups += [group_estimate(frame[frame["TEAGE"].between(lo, hi)], label, replicate_weights.loc[frame["TEAGE"].between(lo, hi)] if replicate_weights is not None else None) for lo, hi, label in age_bins]
    lfs = [(1, "employed-at-work"), (2, "employed-absent"), (3, "unemployed-on-layoff"), (4, "unemployed-looking"), (5, "not-in-labor-force")]
    groups += [group_estimate(frame[frame["TELFS"] == code], label, replicate_weights.loc[frame["TELFS"] == code] if replicate_weights is not None else None) for code, label in lfs]

    result = {
        "format": "atus-time-care-estimate-v1",
        "source": "BLS American Time Use Survey 2024 activity summary and activity public-use files, with respondent-file audit input",
        "source_unit": "ATUS respondent age 15+ with one selected diary day",
        "geography": "United States",
        "year": args.year,
        "files": {
            "respondent": {"path": str(args.respondent), "sha256": archive_hash(args.respondent)},
            "summary": {"path": str(args.summary), "sha256": archive_hash(args.summary)},
            "activity": {"path": str(args.activity), "sha256": archive_hash(args.activity)},
        },
        "merged_respondents": int(len(frame)),
        "replicate_weights": {"included": bool(args.replicate), "formula": "sqrt((4/160) * sum((replicate_estimate - point_estimate)^2))" if args.replicate else None, "path": str(args.replicate) if args.replicate else None, "sha256": archive_hash(args.replicate) if args.replicate else None},
        "activity_definitions": {
            "household_work": "primary activities with six-digit TRCODE prefix 02",
            "care_for_people": "primary activities with TRCODE prefixes 03 or 04",
            "work": "primary activities with TRCODE prefix 05",
            "travel": "primary activities with TRCODE prefix 18",
            "socializing_communicating": "primary activities with TRCODE prefix 12",
            "secondary_childcare": "sum of TRTCCTOT_LN across activities",
            "eldercare": "sum of TRTEC_LN across activities",
        },
        "groups": groups,
        "method": "Merge respondent and activity files by TUCASEID; aggregate diary-day minutes per respondent; compute final-weighted means and participation shares.",
        "uncertainty": "Weighted descriptive estimates; when --replicate is supplied, standard errors use the BLS ATUS replicate-weight formula with 160 replicates. No causal event or longitudinal inference.",
        "boundary": "ATUS is a selected one-day diary for one designated respondent. Primary activity totals do not equal a household time budget; secondary childcare and eldercare are retained as separate measures. The estimates do not identify which price, employer, service, or policy produced the time allocation.",
    }
    if args.eldercare_roster:
        roster = read_dat(args.eldercare_roster)
        roster["TUCASEID"] = roster["TUCASEID"].astype(str)
        roster = roster.merge(frame[["TUCASEID", "TUFINLWGT"]], on="TUCASEID", how="inner", validate="many_to_one")
        provider = roster.groupby("TUCASEID", as_index=False).agg(
            recipient_count=("TUCASEID", "size"),
            has_household_recipient=("TRELHH", lambda x: int((x == 1).any())),
            has_nonhousehold_recipient=("TRELHH", lambda x: int((x == 0).any())),
        ).merge(frame[["TUCASEID", "TUFINLWGT"]], on="TUCASEID", how="inner", validate="one_to_one")
        provider_weights = provider["TUFINLWGT"]
        provider_ids = set(provider["TUCASEID"])
        frame["eldercare_provider"] = frame["TUCASEID"].isin(provider_ids)
        provider_mask = frame["eldercare_provider"]
        result["groups"].append(
            group_estimate(
                frame[provider_mask],
                "eldercare-provider",
                replicate_weights.loc[provider_mask] if replicate_weights is not None else None,
            )
        )
        result["groups"].append(
            group_estimate(
                frame[~provider_mask],
                "not-eldercare-provider",
                replicate_weights.loc[~provider_mask] if replicate_weights is not None else None,
            )
        )
        result["eldercare_roster"] = {
            "rows": int(len(roster)),
            "provider_respondents": int(len(provider)),
            "weighted_mean_listed_recipients_per_provider": weighted_mean(provider["recipient_count"], provider_weights),
            "weighted_percent_providers_with_household_recipient": weighted_share(provider["has_household_recipient"], provider_weights),
            "weighted_percent_providers_with_nonhousehold_recipient": weighted_share(provider["has_nonhousehold_recipient"], provider_weights),
            "unit": "ATUS respondent with at least one eldercare-roster record; roster rows are not independently weighted",
            "sha256": archive_hash(args.eldercare_roster),
        }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"wrote {args.output} for {len(frame)} merged respondents")


if __name__ == "__main__":
    main()
