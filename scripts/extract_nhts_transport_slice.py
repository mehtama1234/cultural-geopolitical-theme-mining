#!/usr/bin/env python3
"""Extract a bounded transportation slice from the 2022 NHTS CSV archive."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from zipfile import ZipFile


FILES = {
    "household": {
        "member": "hhv2pub.csv",
        "fields": ["HOUSEID", "WTHHFIN", "HHSIZE", "HHFAMINC", "HHVEHCNT", "DRVRCNT", "WRKCOUNT", "HOMEOWN", "HOMETYPE", "URBRUR", "TDAYDATE", "TRAVDAY"],
        "counts": ["HHVEHCNT", "WRKCOUNT", "URBRUR"],
    },
    "person": {
        "member": "perv2pub.csv",
        "fields": ["HOUSEID", "PERSONID", "WTPERFIN", "R_AGE", "R_SEX", "WORKER", "DRIVER", "GCDWORK", "USEPUBTR", "LAST30_TAXI", "LAST30_RDSHR", "RIDESHARE22", "WRKTRANS", "CONDTRAV", "CONDRIDE"],
        "counts": ["WORKER", "DRIVER", "LAST30_RDSHR", "RIDESHARE22", "CONDTRAV", "CONDRIDE"],
    },
    "trip": {
        "member": "tripv2pub.csv",
        "fields": ["HOUSEID", "PERSONID", "TRIPID", "TRIPPURP", "WHYTRP90", "TRVLCMIN", "STRTTIME", "ENDTIME", "TRPTRANS", "TRIPMODE", "TRPMILES", "WTTRDFIN", "TDAYDATE"],
        "counts": ["TRIPPURP", "WHYTRP90", "TRPTRANS"],
    },
    "vehicle": {
        "member": "vehv2pub.csv",
        "fields": ["HOUSEID", "VEHID", "VEHYEAR", "VEHTYPE", "VEHFUEL", "VEHOWNED", "ANNMILES", "VEHAGE"],
        "counts": ["VEHFUEL", "VEHOWNED"],
    },
}


def extract(archive: Path, output: Path, report_path: Path, max_rows: int | None) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    report_files = {}
    with ZipFile(archive) as source_zip:
        names = set(source_zip.namelist())
        for kind, spec in FILES.items():
            member = spec["member"]
            if member not in names:
                raise ValueError(f"NHTS archive is missing {member}")
            target_path = output / f"{kind}-slice.csv"
            row_count = 0
            households: set[str] = set()
            counts = {field: Counter() for field in spec["counts"]}
            with source_zip.open(member) as raw:
                with _text_reader(raw) as text:
                    reader = csv.DictReader(text)
                    if reader.fieldnames is None:
                        raise ValueError(f"{member} has no header")
                    missing = [field for field in spec["fields"] if field not in reader.fieldnames]
                    if missing:
                        raise ValueError(f"{member} is missing fields: {', '.join(missing)}")
                    with target_path.open("w", encoding="utf-8", newline="") as target:
                        writer = csv.DictWriter(target, fieldnames=spec["fields"])
                        writer.writeheader()
                        for row in reader:
                            selected = {field: row.get(field, "") for field in spec["fields"]}
                            writer.writerow(selected)
                            row_count += 1
                            households.add(selected["HOUSEID"])
                            for field in spec["counts"]:
                                counts[field][selected[field]] += 1
                            if max_rows is not None and row_count >= max_rows:
                                break
            report_files[kind] = {
                "member": member,
                "rows_written": row_count,
                "distinct_households": len(households),
                "value_counts": {field: dict(sorted(values.items())) for field, values in counts.items()},
                "fields": spec["fields"],
            }

    report = {
        "format": "us-household-calendar-nhts-transport-slice-v1",
        "source": "2022 NHTS CSV V2.1 public-use archive",
        "output": str(output),
        "files": report_files,
        "max_rows_per_file": max_rows,
        "raw_data_committed": False,
        "evidence_status": "observed_source_rows",
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


class _text_reader:
    def __init__(self, raw):
        import io
        self.stream = io.TextIOWrapper(raw, encoding="utf-8", newline="")

    def __enter__(self):
        return self.stream

    def __exit__(self, *_):
        self.stream.detach()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True, help="2022 NHTS CSV zip archive")
    parser.add_argument("--output", type=Path, required=True, help="temporary derived CSV directory")
    parser.add_argument("--report", type=Path, required=True, help="JSON coverage report")
    parser.add_argument("--max-rows", type=int, default=None, help="optional per-file smoke-test row limit")
    args = parser.parse_args()
    print(json.dumps(extract(args.archive, args.output, args.report, args.max_rows), indent=2))


if __name__ == "__main__":
    main()
