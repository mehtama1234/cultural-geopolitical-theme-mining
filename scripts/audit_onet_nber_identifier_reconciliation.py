#!/usr/bin/env python3
"""Audit structural and label-level reconciliation between NBER W35677 and O*NET."""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path

def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()

def excel_column(number: int) -> str:
    result = ""
    while number:
        number, remainder = divmod(number - 1, 26)
        result = chr(97 + remainder) + result
    return result

def transformed_identifier(identifier: str, level: str) -> str | None:
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

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nber-dir", type=Path, required=True)
    parser.add_argument("--onet-mapping", type=Path, required=True)
    parser.add_argument("--comparison-mapping", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mapping = list(csv.DictReader(args.onet_mapping.open(encoding="utf-8-sig", newline="")))
    result = {"format": "onet-nber-identifier-reconciliation-audit-v1", "status": "diagnostic-only",
              "identifier_transform": "NBER I## and D## components converted to O*NET letter and integer components; structural probe, not asserted vintage crosswalk", "levels": {}}
    if args.comparison_mapping:
        current_hash = hashlib.sha256(args.onet_mapping.read_bytes()).hexdigest()
        comparison_hash = hashlib.sha256(args.comparison_mapping.read_bytes()).hexdigest()
        result["release_comparison"] = {
            "current_mapping": args.onet_mapping.name,
            "comparison_mapping": args.comparison_mapping.name,
            "current_sha256": current_hash,
            "comparison_sha256": comparison_hash,
            "byte_identical": current_hash == comparison_hash,
            "interpretation": "Byte identity means this comparison does not explain any NBER/O*NET disagreement; it does not prove that NBER used either O*NET release."
        }
    specs = [("DWA", "DWA.csv", "dwaid", "dwatitle", "DWA Element ID", "DWA Element Name"),
             ("IWA", "IWA.csv", "iwaid", "iwatitle", "IWA Element ID", "IWA Element Name")]
    for level, filename, nber_id, nber_title, onet_id, onet_title in specs:
        labels = defaultdict(set); onet_ids = set()
        for row in mapping:
            labels[normalize(row[onet_title])].add(row[onet_id]); onet_ids.add(row[onet_id])
        stats = {"rows": 0, "unique_label_matches": 0, "ambiguous_label_matches": 0, "unmatched_label_matches": 0,
                 "transformable_identifiers": 0, "transformed_identifier_exact_matches": 0,
                 "transformed_id_agrees_with_unique_label": 0, "transformed_id_differs_from_unique_label": 0}
        examples = []
        with (args.nber_dir / filename).open(encoding="utf-8-sig", newline="") as source:
            for row in csv.DictReader(source):
                nber_identifier = row[nber_id]; transformed = transformed_identifier(nber_identifier, level)
                matches = labels.get(normalize(row[nber_title]), set()); stats["rows"] += 1
                if len(matches) == 1:
                    stats["unique_label_matches"] += 1; label_id = next(iter(matches))
                    key = "transformed_id_agrees_with_unique_label" if transformed == label_id else "transformed_id_differs_from_unique_label"
                    stats[key] += 1
                    if transformed != label_id and len(examples) < 10:
                        examples.append({"nber_id": nber_identifier, "transformed_id": transformed, "label_match_onet_id": label_id, "title": row[nber_title]})
                elif matches: stats["ambiguous_label_matches"] += 1
                else: stats["unmatched_label_matches"] += 1
                if transformed is not None: stats["transformable_identifiers"] += 1
                if transformed in onet_ids: stats["transformed_identifier_exact_matches"] += 1
        result["levels"][level] = {"stats": stats, "examples": examples}
    result["source_hashes"] = {name: hashlib.sha256((args.nber_dir / name).read_bytes()).hexdigest() for name in ("DWA.csv", "IWA.csv")}
    result["source_hashes"][args.onet_mapping.name] = hashlib.sha256(args.onet_mapping.read_bytes()).hexdigest()
    if args.comparison_mapping:
        result["source_hashes"][args.comparison_mapping.name] = hashlib.sha256(args.comparison_mapping.read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
