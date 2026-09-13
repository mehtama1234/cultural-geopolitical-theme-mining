#!/usr/bin/env python3
"""Summarize CBP employees per establishment by sector and rurality."""

from __future__ import annotations

import argparse
import csv
import io
import statistics
from pathlib import Path
from zipfile import ZipFile

from analyze_cbp_county_all_sector_capacity import SECTORS, quartiles


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--rucc", type=Path, required=True)
    args = parser.parse_args()

    rucc: dict[str, int] = {}
    with args.rucc.open(newline="", encoding="latin1") as source:
        for row in csv.DictReader(source):
            if row.get("Attribute") == "RUCC_2023":
                rucc[row["FIPS"]] = int(row["Value"])

    rows: dict[str, dict[str, tuple[int, int]]] = {}
    with ZipFile(args.cbp) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            for row in csv.DictReader(io.TextIOWrapper(raw, encoding="latin1")):
                code = row.get("naics")
                if code not in SECTORS:
                    continue
                est, emp = row.get("est", ""), row.get("emp", "")
                if not est.isdigit() or not emp.isdigit() or int(est) <= 0:
                    continue
                key = row["fipstate"] + row["fipscty"]
                rows.setdefault(key, {})[code] = (int(est), int(emp))

    print("place_group\tsector\tnumeric_count\tmedian_employees_per_establishment\tp25\tp75")
    for group, predicate in (("all", lambda code: True), ("metro", lambda code: code <= 3), ("nonmetro", lambda code: code >= 4)):
        keys = [key for key in rows if key in rucc and predicate(rucc[key])]
        for code, sector in SECTORS.items():
            values = [rows[key][code][1] / rows[key][code][0] for key in keys if code in rows[key]]
            if not values:
                continue
            median, q25, q75 = quartiles(values)
            print(f"{group}\t{sector}\t{len(values)}\t{median:.2f}\t{q25:.2f}\t{q75:.2f}")


if __name__ == "__main__":
    main()
