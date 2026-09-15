#!/usr/bin/env python3
"""Estimate SHED adaptation persistence and entry by same-respondent health direction."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from pathlib import Path

HEALTH = ["Poor", "Fair", "Good", "Very good", "Excellent"]
METRICS = {
    "cheaper_products": "INF3_a",
    "used_less_or_stopped": "INF3_b",
    "reduced_savings": "INF3_c",
    "increased_borrowing": "INF3_d",
    "delayed_major_purchase": "INF3_e",
    "worked_more_or_got_job": "INF3_f",
}


def read_zip(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"expected one CSV in {path}, found {names}")
        with archive.open(names[0]) as handle:
            return list(csv.DictReader((line.decode("utf-8-sig") for line in handle)))


def clean(value: str | None) -> str:
    return (value or "").strip()


def direction(before: str, after: str) -> str:
    before_i, after_i = HEALTH.index(before), HEALTH.index(after)
    if after_i < before_i:
        return "worsened"
    if after_i > before_i:
        return "improved"
    return "unchanged"


def weighted_share(rows: list[tuple[dict[str, str], dict[str, str], float]], field: str,
                   before_state: str) -> dict[str, float | int | None]:
    valid = [row for row in rows if clean(row[0].get(field)) == before_state and clean(row[1].get(field)) in {"Yes", "No"}]
    denominator = sum(row[2] for row in valid)
    yes = sum(row[2] for row in valid if clean(row[1].get(field)) == "Yes")
    return {
        "valid_pairs": len(valid),
        "weighted_denominator": round(denominator, 3),
        "share_yes_2025_percent": round(100 * yes / denominator, 3) if denominator else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    old = {clean(row.get("shedid")): row for row in read_zip(args.old)}
    pairs = []
    for row in read_zip(args.new):
        identifier, weight = clean(row.get("shedid")), clean(row.get("panel_weight"))
        if identifier not in old or not weight:
            continue
        before, after = clean(old[identifier].get("pph10001")), clean(row.get("pph10001"))
        if before in HEALTH and after in HEALTH:
            pairs.append((old[identifier], row, float(weight), direction(before, after)))

    result: dict[str, object] = {
        "format": "us-shed-panel-adaptation-health-path-v1",
        "source_unit": "SHED respondent recontact panel, 2024 to 2025",
        "weight": "2025 panel_weight",
        "paired_rows_with_health_path": len(pairs),
        "variance_estimation": False,
        "causal_estimation": False,
        "health_paths": {},
    }
    for path_name in ["worsened", "unchanged", "improved"]:
        path_pairs = [pair[:3] for pair in pairs if pair[3] == path_name]
        result["health_paths"][path_name] = {
            "paired_rows": len(path_pairs),
            "adaptations": {
                metric: {
                    "persistence_among_2024_yes": weighted_share(path_pairs, field, "Yes"),
                    "entry_among_2024_no": weighted_share(path_pairs, field, "No"),
                }
                for metric, field in METRICS.items()
            },
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
