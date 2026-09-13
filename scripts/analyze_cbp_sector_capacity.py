#!/usr/bin/env python3
"""Extract selected durable employer-sector baselines from a CBP ZIP file."""

from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path
from zipfile import ZipFile


SECTORS = {
    "31----": "Manufacturing (31–33)",
    "44----": "Retail trade (44–45)",
    "62----": "Health care and social assistance (62)",
    "72----": "Accommodation and food services (72)",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cbp", type=Path, required=True)
    args = parser.parse_args()

    with ZipFile(args.cbp) as archive:
        members = [name for name in archive.namelist() if name.endswith(".txt")]
        if len(members) != 1:
            raise ValueError(f"expected one CBP text member, found {members}")
        with archive.open(members[0]) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="latin1"))
            rows = [
                row
                for row in reader
                if row.get("lfo") == "-" and row.get("naics") in ("------", *SECTORS)
            ]

    for row in rows:
        label = "All industries" if row["naics"] == "------" else SECTORS[row["naics"]]
        print(f"{label}\testablishments={row['est']}\temployment={row['emp']}")


if __name__ == "__main__":
    main()
