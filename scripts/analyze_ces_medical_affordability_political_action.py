#!/usr/bin/env python3
"""Analyze CES medical-expense hardship, attribution, and political action.

The inputs are the Stata release-118 ``*_crisis_vv.tab`` extracts from the
Politics of Personal Crisis replication package.  The script produces weighted
descriptive group contrasts and an explicitly exploratory weighted-logistic
screen.  It does not claim CES Taylor-series survey variance estimates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.api as sm


OUTCOMES = [
    "voted_valid",
    "part_meeting",
    "part_sign",
    "part_work",
    "part_protest",
    "part_contact",
    "part_donate",
]
CONTROLS = [
    "voted2016_valid",
    "female",
    "black",
    "hisp",
    "other",
    "age",
    "educ",
    "income",
    "married",
    "churchattend",
    "child18_01",
]
ATTRIBUTION_LABELS = {
    1: "bad_luck",
    2: "choices",
    3: "economy",
    4: "federal_government",
    5: "state_government",
    6: "local_government",
    7: "none_of_these",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def weighted_mean(frame: pd.DataFrame, outcome: str) -> float | None:
    valid = frame[[outcome, "teamweight"]].dropna()
    valid = valid[valid["teamweight"] > 0]
    if valid.empty:
        return None
    return float(np.average(valid[outcome].astype(float), weights=valid.teamweight))


def read_extract(path: Path, year: str) -> tuple[pd.DataFrame, dict[str, str]]:
    fields = ["crisis_medexp", "total_crises", "teamweight", *OUTCOMES, *CONTROLS]
    if year == "2020":
        fields += ["UTK315", "UTK356"]
    else:
        fields += [
            "resp_medexp_badluck",
            "resp_medexp_choices",
            "resp_medexp_economy",
            "resp_medexp_federal",
            "resp_medexp_state",
            "resp_medexp_local",
            "resp_medexp_none",
        ]
    frame, _ = pyreadstat.read_dta(
        path, usecols=sorted(set(fields)), apply_value_formats=False, encoding="latin1"
    )
    missing = sorted(set(fields) - set(frame.columns))
    if missing:
        raise ValueError(f"{path}: missing fields: {', '.join(missing)}")
    frame["other_crises"] = frame["total_crises"] - frame["crisis_medexp"]
    return frame, {"path": str(path), "sha256": sha256(path), "year": year}


def descriptive(frame: pd.DataFrame) -> dict[str, object]:
    valid = frame.dropna(subset=["crisis_medexp", "teamweight"])
    hardship = valid[valid["crisis_medexp"] == 1]
    groups: dict[str, object] = {}
    for code, group in valid.groupby("crisis_medexp"):
        key = "medical_expense_crisis" if int(code) == 1 else "no_medical_expense_crisis"
        groups[key] = {
            "records": int(len(group)),
            "weight": float(group.teamweight.sum()),
            "outcomes_percent": {
                outcome: weighted_mean(group, outcome) * 100
                for outcome in OUTCOMES
            },
        }
    return {
        "records": int(len(valid)),
        "medical_expense_crisis_unweighted_percent": float(100 * len(hardship) / len(valid)) if len(valid) else None,
        "medical_expense_crisis_weighted_percent": float(100 * hardship.teamweight.sum() / valid.teamweight.sum()) if valid.teamweight.sum() else None,
        "groups": groups,
    }


def adjusted_screen(frame: pd.DataFrame) -> dict[str, object]:
    fields = [
        "crisis_medexp",
        "other_crises",
        *CONTROLS,
        "teamweight",
    ]
    results: dict[str, object] = {}
    for outcome in OUTCOMES:
        data = frame[fields + [outcome]].copy()
        data = data.apply(pd.to_numeric, errors="coerce").replace([np.inf, -np.inf], np.nan).dropna()
        if data.empty or data[outcome].nunique() < 2:
            results[outcome] = {"records": int(len(data)), "estimable": False}
            continue
        x = sm.add_constant(data[["crisis_medexp", "other_crises", *CONTROLS]].astype(float))
        model = sm.GLM(
            data[outcome].astype(float),
            x,
            family=sm.families.Binomial(),
            freq_weights=data.teamweight.astype(float),
        )
        fit = model.fit(cov_type="HC1")
        coefficient = float(fit.params["crisis_medexp"])
        standard_error = float(fit.bse["crisis_medexp"])
        results[outcome] = {
            "records": int(len(data)),
            "estimable": True,
            "odds_ratio": float(np.exp(coefficient)),
            "interval_95_model_robust": [
                float(np.exp(coefficient - 1.96 * standard_error)),
                float(np.exp(coefficient + 1.96 * standard_error)),
            ],
            "p_value": float(fit.pvalues["crisis_medexp"]),
        }
    return results


def attribution(frame: pd.DataFrame) -> dict[str, object]:
    if "UTK356" not in frame:
        result: dict[str, object] = {}
        hardship = frame[frame.crisis_medexp == 1]
        total_weight = float(hardship.teamweight.sum())
        flags = {
            "bad_luck": "resp_medexp_badluck",
            "choices": "resp_medexp_choices",
            "economy": "resp_medexp_economy",
            "federal_government": "resp_medexp_federal",
            "state_government": "resp_medexp_state",
            "local_government": "resp_medexp_local",
            "none_of_these": "resp_medexp_none",
        }
        for label, field in flags.items():
            selected = hardship[hardship[field] == 1]
            result[label] = {
                "records": int(len(selected)),
                "weighted_flag_share_percent": float(100 * selected.teamweight.sum() / total_weight),
                "contact_percent": weighted_mean(selected, "part_contact") * 100,
                "protest_percent": weighted_mean(selected, "part_protest") * 100,
            }
        return {"hardship_records": int(len(hardship)), "multiple_response_flags": True, "groups": result}
    hardship = frame[frame.crisis_medexp == 1].dropna(subset=["UTK356", "teamweight"])
    total_weight = float(hardship.teamweight.sum())
    result: dict[str, object] = {}
    for code, group in hardship.groupby("UTK356"):
        label = ATTRIBUTION_LABELS.get(int(code), str(code))
        result[label] = {
            "records": int(len(group)),
            "weighted_share_percent": float(100 * group.teamweight.sum() / total_weight),
            "contact_percent": weighted_mean(group, "part_contact") * 100,
            "protest_percent": weighted_mean(group, "part_protest") * 100,
        }
    return {"hardship_records": int(len(hardship)), "groups": result}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-2018", type=Path, required=True)
    parser.add_argument("--input-2020", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    outputs: dict[str, object] = {
        "format": "ces-medical-affordability-political-action-analysis-v1",
        "weight": "teamweight",
        "causal_estimation": False,
        "variance_estimate": "HC1 model-robust screening only; no CES design-based variance",
        "boundary": "The published study models total crisis count. Medical-specific estimates here are analyst-produced descriptive and adjusted screens.",
        "years": {},
    }
    for year, path in (("2018", args.input_2018), ("2020", args.input_2020)):
        frame, source = read_extract(path, year)
        outputs["years"][year] = {
            "source": source,
            "descriptive": descriptive(frame),
            "adjusted_screen": adjusted_screen(frame),
            "attribution": attribution(frame),
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(outputs, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(outputs, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
