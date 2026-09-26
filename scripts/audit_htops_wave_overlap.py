#!/usr/bin/env python3
"""Audit SCRAMID overlap among retained HTOPS/HPS wave files."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return "sha256:" + h.hexdigest()


def read_ids(path: Path, member: str | None = None) -> tuple[set[str], int, str]:
    if member:
        with zipfile.ZipFile(path) as archive:
            with archive.open(member) as raw:
                reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig"))
                ids = {row["SCRAMID"] for row in reader if row.get("SCRAMID")}
                rows = reader.line_num - 1
        return ids, rows, digest(path)
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        ids = {row["SCRAMID"] for row in reader if row.get("SCRAMID")}
        rows = reader.line_num - 1
    return ids, rows, digest(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave", action="append", nargs=2, metavar=("LABEL", "PATH"), required=True)
    parser.add_argument("--zip-member", action="append", nargs=2, metavar=("LABEL", "MEMBER"), default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    members = dict(args.zip_member)
    loaded = {}
    for label, raw_path in args.wave:
        path = Path(raw_path)
        ids, rows, sha = read_ids(path, members.get(label))
        loaded[label] = {"path": raw_path, "rows": rows, "ids": ids, "sha256": sha}
    labels = list(loaded)
    pairs = []
    for i, left in enumerate(labels):
        for right in labels[i + 1:]:
            pairs.append({"left": left, "right": right, "shared_scramid": len(loaded[left]["ids"] & loaded[right]["ids"])})
    result = {
        "format": "htops-wave-overlap-audit-v1",
        "checked": "2026-09-19",
        "purpose": "Verify whether retained HTOPS/HPS public-use waves can support same-respondent longitudinal joins before estimating cross-wave outcomes.",
        "waves": [{"wave": label, "file": loaded[label]["path"], "rows": loaded[label]["rows"], "has_scramid": True, "sha256": loaded[label]["sha256"]} for label in labels],
        "pairwise_intersections": pairs,
        "interpretation": "These retained public-use files can support a same-respondent join only where the pairwise SCRAMID intersection is nonzero. Zero overlap is a design/acquisition result, not evidence that respondents changed, recovered, or disappeared.",
        "boundary": "No cross-wave estimate is promoted unless a shared respondent cohort and compatible timing are observed.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}: {len(labels)} waves")
    for pair in pairs:
        print(f"{pair['left']} x {pair['right']}: {pair['shared_scramid']} shared SCRAMID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
