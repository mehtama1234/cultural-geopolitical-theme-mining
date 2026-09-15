#!/usr/bin/env python3
"""Build a reproducible USDA SNAP participation/route/access state crosswalk."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from bs4 import BeautifulSoup
from openpyxl import load_workbook


STATES = {
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
    "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",
}


def read_html_rate_table(path: Path, value_column: str) -> dict[str, float]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for table in soup.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [cell.get_text(" ", strip=True) for cell in tr.find_all(["th", "td"])]
            if len(cells) >= 2:
                rows.append(cells)
        if not rows or rows[0][0].lower() not in {"state", ""}:
            continue
        result = {}
        for row in rows[1:]:
            if row[0] in STATES:
                try:
                    result[row[0]] = float(row[1].replace("%", ""))
                except ValueError:
                    continue
        if len(result) >= 45:
            return result
    raise ValueError(f"Could not find a state table in {path} for {value_column}")


def read_pai(path: Path) -> dict[str, float]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for table in soup.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [cell.get_text(" ", strip=True) for cell in tr.find_all(["th", "td"])]
            if len(cells) >= 2:
                rows.append(cells)
        if rows and "2023 PAI" in " ".join(rows[0]):
            result = {}
            for row in rows[1:]:
                if row[0] in STATES:
                    try:
                        result[row[0]] = float(row[1])
                    except ValueError:
                        continue
            if len(result) >= 45:
                return result
    raise ValueError(f"Could not find the 2023 PAI state table in {path}")


def read_snap_rates(path: Path) -> dict[str, float]:
    sheet = load_workbook(path, data_only=True, read_only=True).active
    result = {}
    for row in sheet.iter_rows(min_row=3, max_col=2):
        if row[0].value and isinstance(row[1].value, (int, float)):
            result[str(row[0].value)] = float(row[1].value)
    return {name: value for name, value in result.items() if name in STATES}


def pearson(rows: list[dict], left: str, right: str) -> float:
    xs = [float(row[left]) for row in rows]
    ys = [float(row[right]) for row in rows]
    mean_x, mean_y = sum(xs) / len(xs), sum(ys) / len(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator = math.sqrt(
        sum((x - mean_x) ** 2 for x in xs) * sum((y - mean_y) ** 2 for y in ys)
    )
    return round(numerator / denominator, 3) if denominator else None


def summary(rows: list[dict], field: str) -> dict:
    values = sorted(row[field] for row in rows)
    middle = values[len(values) // 2]
    return {
        "min": round(values[0], 3),
        "median": round(middle, 3),
        "max": round(values[-1], 3),
        "mean": round(sum(values) / len(values), 3),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snap-xlsx", type=Path, required=True)
    parser.add_argument("--apt-html", type=Path, required=True)
    parser.add_argument("--rpt-html", type=Path, required=True)
    parser.add_argument("--pai-html", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    participation = read_snap_rates(args.snap_xlsx)
    apt = read_html_rate_table(args.apt_html, "FY2025 application processing timeliness")
    rpt = read_html_rate_table(args.rpt_html, "FY2025 recertification processing timeliness")
    pai = read_pai(args.pai_html)
    names = sorted(set(participation) & set(apt) & set(rpt) & set(pai))
    if len(names) != 51:
        raise ValueError(f"Expected 51 common states/DC, found {len(names)}")
    rows = [
        {
            "state": name,
            "snap_participation_rate": participation[name],
            "application_timeliness_rate": apt[name],
            "recertification_timeliness_rate": rpt[name],
            "program_access_index_2023": pai[name],
        }
        for name in names
    ]
    result = {
        "format": "usda-snap-route-state-context-v1",
        "source": "USDA/FNA FY2025 state participation, FY2025 application and recertification processing timeliness, and 2023 Program Access Index",
        "state_count": len(rows),
        "definitions": {
            "snap_participation_rate": "FY2025 average monthly SNAP participants as a percent of state population.",
            "application_timeliness_rate": "FY2025 share of applications subject to the timeliness measure processed timely; timely means opportunity to participate within 30 days for regular or 7 days for expedited service, with the FNA page's routing and exclusion rules.",
            "recertification_timeliness_rate": "FY2025 share of recertifications in the timeliness measure for which the household had access to the benefit allotment by the normal issuance date; FNA separates client-caused from agency-caused delays.",
            "program_access_index_2023": "Calendar-year 2023 average monthly SNAP participation divided by the number of people with income below 125 percent of the federal poverty line; it is an access indicator, not a strict eligible-population take-up rate.",
        },
        "summaries": {
            "snap_participation_rate": summary(rows, "snap_participation_rate"),
            "application_timeliness_rate": summary(rows, "application_timeliness_rate"),
            "recertification_timeliness_rate": summary(rows, "recertification_timeliness_rate"),
            "program_access_index_2023": summary(rows, "program_access_index_2023"),
        },
        "correlations_with_fy2025_snap_participation": {
            "application_timeliness_rate": pearson(rows, "snap_participation_rate", "application_timeliness_rate"),
            "recertification_timeliness_rate": pearson(rows, "snap_participation_rate", "recertification_timeliness_rate"),
            "program_access_index_2023": pearson(rows, "snap_participation_rate", "program_access_index_2023"),
        },
        "states": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
