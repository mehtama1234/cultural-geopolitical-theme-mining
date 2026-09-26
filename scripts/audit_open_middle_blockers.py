"""Check the broad atlas's open-middle scope and screen blocker language.

The category counts intentionally overlap and are an independent phrase
screen, not a replacement for the calibrated family classification in the
stored audit. This script is a diagnostic, not a prevalence estimator.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "analysis/data/us-broad-event-ledger-index-v1.json"
AUDIT = ROOT / "analysis/data/us-broad-open-middle-blocker-audit-v1.json"

CATEGORIES = {
    "later_outcome_or_durability": (
        "later", "durab", "persistence", "recurrence", "continued", "follow-up",
        "recovery", "resilience", "outcome", "security", "stability",
    ),
    "trust_meaning_or_action": (
        "trust", "meaning", "action", "political", "legitimacy", "belonging",
        "confidence", "voice", "acceptance", "public response", "participation",
    ),
    "alternative_nonuse_switching_or_exit": (
        "alternative", "non-use", "nonuse", "switch", "exit", "choice",
        "substitute", "replacement", "refusal", "return", "use",
    ),
    "receipt_or_implementation": (
        "receipt", "payment", "delivery", "implement", "complete", "cash",
        "issuance", "correction", "compliance", "acceptance", "disbursement",
    ),
    "money_time_or_adequacy": (
        "amount", "money", "payment", "wage", "dollar", "cost", "time",
        "adequacy", "residual", "burden", "loss", "sufficient", "hour",
        "debt", "price", "fee", "benefit",
    ),
    "unit_denominator_eligibility_or_attribution": (
        "same-", "same ", "identifier", "denominator", "eligibility", "attribution",
        "responsible", "account", "claimant", "unit", "linkage", "causal",
        "recipient", "applicant", "policy",
    ),
}


def load_open_arrows() -> tuple[list[dict], dict]:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    arrows: list[dict] = []
    for entry in index["entries"]:
        path = ROOT / entry["path"]
        ledger = json.loads(path.read_text(encoding="utf-8"))
        for arrow in ledger.get("arrows", []):
            if arrow.get("status") == "open":
                arrows.append({"ledger": entry["path"], **arrow})
    return arrows, index


def validate_scope() -> dict[str, int]:
    """Return the indexed portfolio scope and fail if the stored audit drifts."""
    arrows, index = load_open_arrows()
    actual = {
        "ledger_count": len(index["entries"]),
        "event_count": sum(
            len(json.loads((ROOT / entry["path"]).read_text(encoding="utf-8")).get("events", []))
            for entry in index["entries"]
        ),
        "arrow_count": sum(
            len(json.loads((ROOT / entry["path"]).read_text(encoding="utf-8")).get("arrows", []))
            for entry in index["entries"]
        ),
        "open_arrow_count": len(arrows),
    }
    expected = json.loads(AUDIT.read_text(encoding="utf-8"))["scope"]
    if actual != expected:
        raise ValueError(f"open-middle scope drift: expected {expected}, actual {actual}")
    return actual


def main() -> int:
    arrows, index = load_open_arrows()
    actual = validate_scope()

    counts = {name: 0 for name in CATEGORIES}
    for arrow in arrows:
        text = str(arrow.get("remaining_gap", "")).lower()
        for name, terms in CATEGORIES.items():
            if any(re.search(re.escape(term), text) for term in terms):
                counts[name] += 1

    print(json.dumps({"scope": actual, "category_mentions": counts}, indent=2))
    print("PASS open-middle ledger scope and open-arrow inventory check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
