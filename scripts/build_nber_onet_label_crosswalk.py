#!/usr/bin/env python3
"""Build a reproducible provisional NBER W35677/O*NET label crosswalk."""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path

def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()

def excel_column(number: int) -> str:
    result = ""
    while number:
        number, remainder = divmod(number - 1, 26)
        result = chr(97 + remainder) + result
    return result

def structural_id(identifier: str, level: str) -> str | None:
    parts = identifier.split(".")
    if level == "DWA":
        if len(parts) < 2:
            return None
        activity = re.fullmatch(r"I(\d+)", parts[-2])
        detail = re.fullmatch(r"D(\d+)", parts[-1])
        if not activity or not detail:
            return None
        return ".".join(parts[:-2] + [excel_column(int(activity.group(1))), str(int(detail.group(1)))])
    activity = re.fullmatch(r"I(\d+)", parts[-1]) if parts else None
    return ".".join(parts[:-1] + [excel_column(int(activity.group(1)))]) if activity else None

def read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nber-dir", type=Path, required=True)
    ap.add_argument("--onet-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    mapping = read(args.onet_dir / "gwas_to_iwas_to_dwas.csv")
    specs = [("DWA", "dwaid", "dwatitle", "DWA Element ID", "DWA Element Name"),
             ("IWA", "iwaid", "iwatitle", "IWA Element ID", "IWA Element Name")]
    out = {"format": "nber-onet-provisional-label-crosswalk-v1", "status": "provisional-label-match-only", "levels": {}}
    for level, n_id, n_title, o_id, o_title in specs:
        index: dict[str, set[str]] = defaultdict(set)
        for row in mapping:
            index[norm(row[o_title])].add(row[o_id])
        rows = []
        for row in read(args.nber_dir / f"{level}.csv"):
            matches = sorted(index.get(norm(row[n_title]), set()))
            probe = structural_id(row[n_id], level)
            rows.append({"nber_id": row[n_id], "nber_title": row[n_title], "onet_ids": matches,
                         "match_status": "unique_label" if len(matches) == 1 else ("unmatched" if not matches else "ambiguous_label"),
                         "structural_id_probe": probe,
                         "structural_id_in_onet": probe in {item for values in index.values() for item in values},
                         "structural_id_agrees_with_label": len(matches) == 1 and probe == matches[0]})
        out["levels"][level] = {"rows": rows, "row_count": len(rows),
            "unique_label_matches": sum(r["match_status"] == "unique_label" for r in rows),
            "unmatched": sum(r["match_status"] == "unmatched" for r in rows),
            "ambiguous": sum(r["match_status"] == "ambiguous_label" for r in rows)}
    # BWA is an aggregation layer: map its prefix to the O*NET GWA elements
    # below that prefix, while retaining the fact that the labels differ.
    gwa_by_prefix: dict[str, set[str]] = defaultdict(set)
    for row in mapping:
        gwa_by_prefix[row["GWA Element ID"][:7]].add(row["GWA Element ID"])
    bwa_rows = []
    for row in read(args.nber_dir / "BWA.csv"):
        ids = sorted(gwa_by_prefix.get(row["bwaid"], set()))
        bwa_rows.append({"nber_id": row["bwaid"], "nber_title": row["bwatitle"],
                         "onet_gwa_ids": ids,
                         "match_status": "prefix_aggregation" if ids else "unmatched"})
    out["levels"]["BWA"] = {"rows": bwa_rows, "row_count": len(bwa_rows),
        "prefix_aggregation_matches": sum(r["match_status"] == "prefix_aggregation" for r in bwa_rows),
        "unmatched": sum(r["match_status"] == "unmatched" for r in bwa_rows),
        "note": "BWA labels are retained as NBER aggregation labels; O*NET GWA IDs are supplied only as prefix members."}
    out["source_hashes"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.nber_dir.glob("*.csv"))}
    out["source_hashes"]["gwas_to_iwas_to_dwas.csv"] = hashlib.sha256((args.onet_dir / "gwas_to_iwas_to_dwas.csv").read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Built provisional crosswalk: {sum(x['row_count'] for x in out['levels'].values())} rows")

if __name__ == "__main__":
    main()
