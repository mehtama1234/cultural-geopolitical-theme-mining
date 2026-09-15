#!/usr/bin/env python3
"""Sensitivity checks for the California FAIR/private-market joint screen."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/projects/us-housing-insurance-risk/data"
OUT = DATA / "california-fair-joint-sensitivity-2022.json"


def rate(rows: list[dict], label: str) -> dict:
    renewed = sum(r["renewed"] for r in rows)
    nonrenewed = sum(r["nonrenewed"] for r in rows)
    return {"group": label, "zip_rows": len(rows), "decision_count": renewed + nonrenewed, "nonrenewal_rate": round(nonrenewed / (renewed + nonrenewed), 6) if renewed + nonrenewed else None, "mean_fair_share": round(sum(r["fair_share"] for r in rows) / len(rows), 3) if rows else None}


def split(rows: list[dict], income_cut: float, risk_cut: float, label: str) -> dict:
    cells = {}
    for income_name, income_test in (("low_income", lambda r: r["income"] <= income_cut), ("high_income", lambda r: r["income"] > income_cut)):
        for risk_name, risk_test in (("high_risk", lambda r: r["risk_share"] >= risk_cut), ("low_risk", lambda r: r["risk_share"] < risk_cut)):
            cells[f"{income_name}__{risk_name}"] = rate([r for r in rows if income_test(r) and risk_test(r)], f"{label}:{income_name}__{risk_name}")
    return {"income_cut": income_cut, "risk_cut": risk_cut, "cells": cells}


def main() -> int:
    rows = json.loads((DATA / "california-fair-joint-context-2022-screen.json").read_text())["joined_rows"]
    incomes = sorted(r["income"] for r in rows)
    risks = sorted(r["risk_share"] for r in rows)
    median_income = incomes[len(incomes) // 2]
    median_risk = risks[len(risks) // 2]
    q_income = incomes[len(incomes) // 4]
    q_risk = risks[(3 * len(risks)) // 4]
    checks = [
        split(rows, 50000, 12.1, "$50k_income__12.1pct_risk"),
        split(rows, median_income, median_risk, "median_income__median_risk"),
        split(rows, q_income, q_risk, "lower_income_quartile__upper_risk_quartile"),
    ]
    result = {"format": "california-fair-joint-sensitivity-2022-v1", "joined_zip_rows": len(rows), "cut_points": {"median_income": median_income, "median_risk": median_risk, "lower_income_quartile": q_income, "upper_risk_quartile": q_risk}, "checks": checks, "classification": "Sensitivity analysis of descriptive weighted decision rates; no causal model.", "limits": ["Sensitivity definitions change group composition and do not solve omitted-variable, time, geography, or denominator problems.", "Decision-weighted rates are not population-weighted or household-level probabilities.", "The CDI risk measure is county-level and based on an older dwelling-unit base than the 2022 market counts."]}
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
