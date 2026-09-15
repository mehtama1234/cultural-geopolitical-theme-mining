#!/usr/bin/env python3
"""Compare NBER broad rates with a transparent O*NET-prefix DWA aggregation."""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f: return list(csv.DictReader(f))
def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nber-dir", type=Path, required=True)
    ap.add_argument("--onet-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    mapping = rows(a.onet_dir / "gwas_to_iwas_to_dwas.csv")
    label_map: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for r in mapping: label_map[norm(r["DWA Element Name"])].add((r["DWA Element ID"], r["GWA Element ID"]))
    agg: dict[str, list[float | int]] = defaultdict(lambda: [0.0, 0, 0])
    for r in rows(a.nber_dir / "DWA.csv"):
        if not r["adoption_rate"].strip() or not r["number_observations"].isdigit(): continue
        match = label_map.get(norm(r["dwatitle"]), set())
        if len(match) != 1: continue
        _, gwa = next(iter(match)); prefix = gwa[:7]; obs = int(r["number_observations"]); rate = float(r["adoption_rate"].strip("%"))
        agg[prefix][0] += rate * obs; agg[prefix][1] += obs; agg[prefix][2] += 1
    result = {"format": "nber-bwa-dwa-consistency-audit-v1", "checked": "2026-09-13", "method": "DWA rates weighted by the NBER displayed unweighted observation counts, grouped by O*NET GWA prefix after unique normalized-title matching; compared descriptively to NBER BWA rates.", "levels": []}
    for r in rows(a.nber_dir / "BWA.csv"):
        total, obs, count = agg[r["bwaid"]]; detailed = total / obs if obs else None; bwa = float(r["adoption_rate"].strip("%"))
        result["levels"].append({"bwa_id": r["bwaid"], "bwa_title": r["bwatitle"], "nber_bwa_rate_percent": bwa, "dwa_weighted_rate_percent": round(detailed, 3) if detailed is not None else None, "difference_percentage_points": round(detailed - bwa, 3) if detailed is not None else None, "dwa_rows": int(count), "dwa_unweighted_observations": int(obs)})
    result["source_hashes"] = {p.name: sha(p) for p in sorted(a.nber_dir.glob("*.csv"))}
    result["source_hashes"]["gwas_to_iwas_to_dwas.csv"] = sha(a.onet_dir / "gwas_to_iwas_to_dwas.csv")
    result["boundary"] = "This is a consistency diagnostic, not a re-estimation of the NBER BWA index. The DWA displayed rates and BWA rates may use different valid universes, weights, missingness, and aggregation procedures; differences do not indicate an error or a causal effect."
    a.output.parent.mkdir(parents=True, exist_ok=True); a.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Built BWA/DWA consistency audit: {len(result['levels'])} broad categories")
if __name__ == "__main__": main()
