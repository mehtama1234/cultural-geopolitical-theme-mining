#!/usr/bin/env python3
"""Compare paid-employee CBP and nonemployer repair proxies without pooling them."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "census-repair-proxy-comparison.json"


def main() -> int:
    cbp = json.loads((ANALYSIS / "census-repair-industry-snapshot.json").read_text())
    nes = json.loads((ANALYSIS / "census-nonemployer-repair-snapshot.json").read_text())
    cbp_rows = {(row["year"], row["naics"]): row for row in cbp["national"]}
    nes_rows = {row["year"]: row for row in nes["national"] if row["year"] <= 2023}
    years = sorted(set(y for y, _ in cbp_rows) & set(nes_rows))
    rows = []
    for year in years:
        c = [row for (y, _), row in cbp_rows.items() if y == year]
        rows.append({
            "year": year,
            "cbp_paid_employee_establishments": sum(row["establishments"] or 0 for row in c),
            "cbp_paid_employee_employees": sum(row["employees"] or 0 for row in c),
            "nes_nonemployer_establishments": nes_rows[year]["establishments"],
            "nes_nonemployer_receipts_thousands_usd": nes_rows[year]["receipts_thousands_usd"],
        })
    first, last = rows[0], rows[-1]
    def change(key: str) -> int:
        return last[key] - first[key]
    payload = {
        "schema": "external-trend-intelligence.census-repair-proxy-comparison.v1",
        "comparison_id": "census-cbp-versus-nes-repair-2019-2023",
        "status": "bounded_same_publisher_comparison_not_independent_confirmation",
        "source_artifacts": ["census-repair-industry-snapshot.json", "census-nonemployer-repair-snapshot.json"],
        "coverage": {"years": years, "row_count": len(rows)},
        "rows": rows,
        "descriptive_changes": {
            "cbp_paid_employee_establishments": change("cbp_paid_employee_establishments"),
            "cbp_paid_employee_employees": change("cbp_paid_employee_employees"),
            "nes_nonemployer_establishments": change("nes_nonemployer_establishments"),
            "nes_nonemployer_receipts_thousands_usd": change("nes_nonemployer_receipts_thousands_usd"),
        },
        "measurement_map": {
            "cbp": "Paid-employee establishments and employment in CBP NAICS 811211/811213.",
            "nes": "Nonemployer establishments and gross receipts in NES NAICS 81121.",
            "same_publisher": True,
            "population_difference": "CBP covers employer establishments; NES covers businesses without paid employees, with different classification and reporting frames.",
        },
        "interpretation": "The comparison tests whether broad employer and nonemployer repair signals move in the same descriptive direction. It does not estimate a market total, repair transactions, phone access, policy impact, or consumer outcomes.",
        "counter_signals": [
            "The CBP categories split consumer and communication equipment while NES aggregates them at five digits.",
            "Receipts are nominal gross business receipts and are not comparable to CBP payroll or employment.",
            "Both series share the Census publisher and administrative classification risks, so agreement is not independent confirmation.",
        ],
        "pooling_decision": "do_not_pool_or_count_as_independent_confirmation",
        "falsifier": "A phone-specific repair or replacement series shows a materially different direction or timing from both broad proxies.",
        "next_action": "Use the comparison as a measurement-boundary check; acquire phone-specific transaction or consumer outcome data before qualification or internal exposure testing.",
        "rights_basis": "Derived normalized comparison from official Census public-download artifacts; preserve source artifact names and checksums through their manifests.",
        "boundary": "This same-publisher comparison improves external measurement discipline but leaves the phone-repair candidate held.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} aligned years)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
