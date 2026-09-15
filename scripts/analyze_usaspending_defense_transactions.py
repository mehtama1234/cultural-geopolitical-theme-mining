#!/usr/bin/env python3
"""Summarize recipients, places, and industrial codes in a USAspending extract."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8"))
    rows = source["response"]["results"]
    amounts = [float(row.get("Transaction Amount") or 0) for row in rows]
    recipient_amounts: defaultdict[str, float] = defaultdict(float)
    state_amounts: defaultdict[str, float] = defaultdict(float)
    naics_amounts: defaultdict[str, float] = defaultdict(float)
    psc_amounts: defaultdict[str, float] = defaultdict(float)
    for row, amount in zip(rows, amounts):
        recipient_amounts[str(row.get("Recipient Name") or "Unknown")] += amount
        state_amounts[str(row.get("pop_state_code") or "Unknown")] += amount
        naics_amounts[str(row.get("naics_code") or "Unknown")] += amount
        psc_amounts[str(row.get("product_or_service_code") or "Unknown")] += amount
    total = sum(amounts)
    def ranked(values: dict[str, float], limit: int = 10) -> list[dict[str, object]]:
        return [{"key": key, "amount": round(value, 2), "share_of_page_amount": round(100 * value / total, 4) if total else 0.0}
                for key, value in sorted(values.items(), key=lambda item: (-item[1], item[0]))[:limit]]
    output = {
        "format": "usaspending-defense-transaction-profile-v1",
        "input": str(args.input),
        "input_response_sha256": source.get("response_sha256"),
        "records": len(rows),
        "page_transaction_amount_total": round(total, 2),
        "recipient_count": len(recipient_amounts),
        "place_of_performance_state_count": len(state_amounts),
        "naics_count": len(naics_amounts),
        "product_or_service_code_count": len(psc_amounts),
        "top_recipients": ranked(recipient_amounts),
        "top_performance_states": ranked(state_amounts),
        "top_naics": ranked(naics_amounts),
        "top_product_or_service_codes": ranked(psc_amounts),
        "boundary": "Descriptive concentration profile of a bounded USAspending transaction retrieval page sorted by transaction amount; not total DoD procurement, supplier-market share, delivered capability, production, readiness, or geopolitical leverage.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "records": len(rows), "page_transaction_amount_total": round(total, 2)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
