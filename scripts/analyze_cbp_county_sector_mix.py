#!/usr/bin/env python3
"""Summarize selected CBP sectors as shares of county establishments."""

from __future__ import annotations

import argparse
import csv
import io
import statistics
from pathlib import Path
from zipfile import ZipFile


SECTORS = {
    "31----": "manufacturing",
    "44----": "retail",
    "62----": "health_social_assistance",
    "72----": "accommodation_food",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cbp", type=Path, required=True)
    parser.add_argument("--minimum-establishments", type=int, default=100)
    args = parser.parse_args()

    counties: dict[tuple[str, str], dict[str, int]] = {}
    with ZipFile(args.cbp) as archive:
        members = [name for name in archive.namelist() if name.endswith(".txt")]
        if len(members) != 1:
            raise ValueError(f"expected one CBP text member, found {members}")
        with archive.open(members[0]) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="latin1"))
            for row in reader:
                if row.get("naics") not in ("------", *SECTORS) or not row.get("est", "").isdigit():
                    continue
                key = (row["fipstate"], row["fipscty"])
                counties.setdefault(key, {})[row["naics"]] = int(row["est"])

    eligible = [
        values for values in counties.values()
        if values.get("------", 0) >= args.minimum_establishments
    ]
    print(f"counties={len(eligible)}")
    for code, label in SECTORS.items():
        shares = [100 * values.get(code, 0) / values["------"] for values in eligible]
        quartiles = statistics.quantiles(shares, n=4, method="inclusive")
        print(
            f"{label}\tmedian={statistics.median(shares):.2f}%"
            f"\tp25={quartiles[0]:.2f}%\tp75={quartiles[2]:.2f}%"
        )


if __name__ == "__main__":
    main()
