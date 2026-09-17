#!/usr/bin/env python3
"""Map public CFPB complaint records into the broad event-ledger contract.

This produces an administrative route ledger, not a consumer-outcome file.
Complaint identifiers are hashed and ZIP/company/narrative text are omitted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def iso_date(value: str) -> str:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()


def route_hours(received: str, sent: str) -> float | None:
    if not received or not sent:
        return None
    start = datetime.fromisoformat(received.replace("Z", "+00:00"))
    end = datetime.fromisoformat(sent.replace("Z", "+00:00"))
    return round((end - start).total_seconds() / 3600, 4)


def sample_period(dates: list[str]) -> str:
    """Describe the observed calendar span without assuming a source year."""
    years = sorted({d[:4] for d in dates if len(d) >= 4})
    if not years:
        return "unknown period"
    return years[0] if len(years) == 1 else f"{years[0]}–{years[-1]}"


def build(
    input_path: Path,
    required_product: str | None = None,
    required_sub_product: str | None = None,
) -> dict:
    raw = input_path.read_bytes()
    data = json.loads(raw)
    all_hits = data.get("hits", {}).get("hits", [])
    if not all_hits:
        raise ValueError("input contains no complaint records")
    hits = all_hits
    if required_product is not None:
        hits = [
            hit for hit in hits
            if hit.get("_source", {}).get("product") == required_product
        ]
    if required_sub_product is not None:
        hits = [
            hit for hit in hits
            if hit.get("_source", {}).get("sub_product") == required_sub_product
        ]
    if not hits:
        raise ValueError("no complaint records remain after local field filters")
    first = hits[0].get("_source", {})
    product = first.get("product") or "unknown product"
    sub_product = first.get("sub_product")
    filter_note = ""
    if required_product is not None or required_sub_product is not None:
        filter_note = (
            f"; locally filtered from {len(all_hits)} returned records"
            f"; required_product={required_product or 'any'}"
            f"; required_sub_product={required_sub_product or 'any'}"
        )
    dates = [h.get("_source", {}).get("date_received") for h in hits]
    dates = [d for d in dates if d]
    period = sample_period(dates)
    events = []
    for hit in hits:
        row = hit.get("_source", {})
        complaint_id = str(row.get("complaint_id") or hit.get("_id") or "")
        if not complaint_id or not row.get("date_received"):
            raise ValueError("every record needs a public complaint id and date_received")
        case_id = "CFPB-" + hashlib.sha256(complaint_id.encode()).hexdigest()[:16]
        timely = row.get("timely") or "unknown"
        response = row.get("company_response") or "unknown"
        sent = row.get("date_sent_to_company")
        event = {
            "event_id": case_id,
            "unit": "case",
            "geography": row.get("state") or "unknown state; omitted if unavailable",
            "actor_initiating_change": "consumer",
            "event_date": iso_date(row["date_received"]),
            "date_precision": "day from public API timestamp; route timestamp retained only as derived lag",
            "denominator": f"{len(hits)}-record capped retrieval-order sample{filter_note}; product={product}; received {period}",
            "method": "Public CFPB complaint API record mapped to administrative route stages; no weighting or population estimation",
            "missingness": "Public record may omit narrative, public response, route timestamp, or later outcome; omitted fields are not zeros",
            "condition_or_decision": "service_failure",
            "exposure": f"Published CFPB complaint in product route {product}; sub-product={sub_product or 'unknown'}",
            "alternatives_before_action": "Not observed in the public complaint record",
            "immediate_burden_or_benefit": f"Administrative route observed; receipt-to-company-send lag hours={route_hours(row.get('date_received'), sent)}",
            "choice_or_response": f"Complaint submitted via {row.get('submitted_via') or 'unknown'}; narrative_present={bool(row.get('has_narrative'))}",
            "person_or_actor_with_control": "company and CFPB route; exact decision authority not identified",
            "remedy_or_institutional_response": f"company_response={response}; timely={timely}; public_response_present={bool(row.get('company_public_response'))}",
            "immediate_outcome": "Published administrative response label only; customer outcome not observed",
            "protected_outcome": "Not observed in the public complaint record",
            "sacrificed_outcome": "Customer time, money, access, or security outcome not observed",
            "cost_risk_transfer": "Customer effort, financial loss, and time cost are not measured in this record",
            "later_outcome": "unknown: verified correction, recovery, repeat effort, switching, trust, and exit are not in the public record",
            "meaning_and_attribution": "unknown: narrative presence is not a coded meaning or attribution measure",
            "public_or_collective_response": "CFPB complaint submission recorded; no later civic or collective response measured",
            "counterexample": "Same sample contains timely and untimely route labels and records with/without narratives; these are administrative contrasts, not outcome counterexamples",
            "evidence_status": "observed",
            "source_and_uncertainty": f"CFPB public complaint API; raw_sha256={sha256_bytes(raw)}; capped retrieval order{filter_note}; no account denominator, weighting, remedy verification, or causal estimate",
        }
        events.append(event)
    arrows = [
        {
            "arrow_id": "A-01",
            "from": "complaint received",
            "to": "company routing and response label",
            "unit_held_constant": True,
            "time_order_valid": True,
            "evidence": "date_received, date_sent_to_company, timely, and company_response fields in the same public case record",
            "status": "observed",
            "counterexample": "same sample includes same-day and delayed route labels",
            "remaining_gap": "route effort, decision authority, and verified correction",
        },
        {
            "arrow_id": "A-02",
            "from": "company response label",
            "to": "consumer remedy and later trust/exit",
            "unit_held_constant": True,
            "time_order_valid": False,
            "evidence": "no verified downstream outcome field in the public record",
            "status": "open",
            "counterexample": "a recorded explanation may coexist with unresolved harm; no case-level outcome comparison available",
            "remaining_gap": "verified remedy, repeat effort, recovery, switching, trust, and exit",
        },
    ]
    return {
        "evidence_class": "public_administrative_route_records",
        "schema": "us-broad-event-ledger-schema-v1",
        "source": "CFPB Consumer Complaint Database public API",
        "input_sha256": sha256_bytes(raw),
        "events": events,
        "arrows": arrows,
        "boundary": "De-identified administrative route ledger. It is not a representative consumer sample, remedy dataset, or causal estimate. Hashed case IDs are linkage-safe within this extract only; direct identifiers, ZIP codes, company names, and narrative text are omitted.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--require-product")
    parser.add_argument("--require-sub-product")
    args = parser.parse_args()
    output = build(
        args.input,
        required_product=args.require_product,
        required_sub_product=args.require_sub_product,
    )
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"events": len(output["events"]), "arrows": len(output["arrows"]), "input_sha256": output["input_sha256"]}, indent=2))


if __name__ == "__main__":
    main()
