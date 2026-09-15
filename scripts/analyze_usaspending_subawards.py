#!/usr/bin/env python3
"""Profile recipients, amounts, timing, and descriptions in a subaward extract."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8"))
    rows = source["response"].get("results", [])
    amounts = [float(row.get("amount") or 0) for row in rows]
    recipient_amounts: defaultdict[str, float] = defaultdict(float)
    recipient_counts: defaultdict[str, int] = defaultdict(int)
    for row, amount in zip(rows, amounts):
        recipient = str(row.get("recipient_name") or "Unknown")
        recipient_amounts[recipient] += amount
        recipient_counts[recipient] += 1
    total = sum(amounts)

    def ranked(values: dict[str, float], limit: int = 20) -> list[dict[str, object]]:
        return [
            {
                "recipient": key,
                "amount": round(value, 2),
                "share_of_extract_amount": round(100 * value / total, 4) if total else 0.0,
                "subaward_count": recipient_counts[key],
            }
            for key, value in sorted(values.items(), key=lambda item: (-item[1], item[0]))[:limit]
        ]

    output = {
        "format": "usaspending-award-subaward-profile-v1",
        "input": str(args.input),
        "input_response_sha256": source.get("response_sha256"),
        "records": len(rows),
        "extract_amount_total": round(total, 2),
        "recipient_count": len(recipient_amounts),
        "date_min": min((row.get("action_date") for row in rows if row.get("action_date")), default=None),
        "date_max": max((row.get("action_date") for row in rows if row.get("action_date")), default=None),
        "top_recipients": ranked(recipient_amounts),
        "boundary": "Descriptive concentration profile of the returned USAspending subaward records for one parent award; extract shares are not supplier-market shares and do not establish ownership, tier completeness, production, delivery, readiness, or leverage.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "records": len(rows), "extract_amount_total": round(total, 2), "recipient_count": len(recipient_amounts)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
