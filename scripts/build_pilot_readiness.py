#!/usr/bin/env python3
"""Build an explicit, fail-closed readiness checklist for company pilots."""

from __future__ import annotations

import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "pilot-readiness.json"


def load(name: str) -> dict:
    return json.loads((ANALYSIS / name).read_text())


def present(value: object) -> bool:
    return value is not None and value != "" and value != []


def main() -> int:
    pilots = load("pilot-register.json")["pilots"]
    matrix = load("candidate-qualification-matrix.json")
    matrix_by_id = {item["candidate_id"]: item for item in matrix["rows"]}
    rights_reviews = {
        load("food-insecurity-rights-review.json")["candidate_id"]: load("food-insecurity-rights-review.json")
    }
    rows = []
    for pilot in pilots:
        candidate = matrix_by_id.get(pilot["candidate_id"], {})
        rights_review = rights_reviews.get(pilot["candidate_id"])
        checks = [
            {
                "id": "external_qualification",
                "label": "External candidate has passed all qualification gates",
                "status": "pass" if candidate.get("gate_status") in {"qualified_external_trend", "monitored_external_trend"} else "blocked",
                "evidence": "candidate-qualification-matrix.json",
                "detail": f"candidate matrix: {candidate.get('gate_status', 'candidate not found')}; pilot gate record: {pilot['external_gate'].get('current_status', 'not recorded')}",
            },
            {
                "id": "external_rights_reuse",
                "label": "External source rights permit the proposed downstream company use",
                "status": "pass" if rights_review and "do_not_redistribute" not in rights_review.get("release_decision", "") and "do_not_connect_company_data" not in rights_review.get("release_decision", "") else "blocked",
                "evidence": "food-insecurity-rights-review.json" if rights_review else "rights-review-queue.json",
                "detail": rights_review.get("release_decision", "candidate-specific rights review is not complete") if rights_review else "no candidate-specific rights reuse review is recorded",
            },
            {
                "id": "company_decision_contract",
                "label": "Company, business unit, decision owner, and decision are registered",
                "status": "pass" if all(present(pilot["company_ref"].get(k)) for k in ("company_id", "business_unit", "decision_owner")) else "blocked",
                "evidence": "pilot-register.json",
                "detail": "company identity and decision owner are required before internal access",
            },
            {
                "id": "internal_data_contract",
                "label": "Internal dataset, snapshot, key, period, outcome, unit, and denominator are specified",
                "status": "pass" if all(present(pilot["internal_data_contract"].get(k)) for k in ("dataset", "snapshot_or_query", "entity_key", "period", "outcome", "unit", "denominator")) else "blocked",
                "evidence": "pilot-register.json",
                "detail": "no internal dataset is connected at design stage",
            },
            {
                "id": "access_privacy_rights",
                "label": "Lawful access, privacy class, retention, and redistribution rules are approved",
                "status": "pass" if pilot["privacy_and_rights"].get("privacy_class") not in {None, "Not assessed"} and pilot["privacy_and_rights"].get("access_basis") not in {None, "Pending named data owner and lawful access review"} else "blocked",
                "evidence": "PILOT-VALIDATION-PROTOCOL.md",
                "detail": "data-owner and privacy review remain pending",
            },
            {
                "id": "analysis_preregistration",
                "label": "Crosswalk, comparison, primary outcome, falsifier, stop rule, and analysis owner are registered",
                "status": "blocked",
                "evidence": "PILOT-VALIDATION-PROTOCOL.md",
                "detail": "pre-registration is prohibited until external qualification, rights reuse, and company access gates pass",
            },
        ]
        external_blocked = any(c["id"] in {"external_qualification", "external_rights_reuse"} and c["status"] != "pass" for c in checks)
        rows.append({
            "pilot_id": pilot["pilot_id"],
            "candidate_id": pilot["candidate_id"],
            "current_status": pilot["status"],
            "readiness_status": "ready_for_approved_test" if all(c["status"] == "pass" for c in checks) else ("blocked_external_first" if external_blocked else "blocked_company_gate"),
            "checks": checks,
            "blocking_check_ids": [c["id"] for c in checks if c["status"] != "pass"],
            "boundary": "A readiness pass authorizes only a separately approved test; it never proves causality or permits unregistered reuse of company data.",
        })
    report = {
        "schema": "external-trend-intelligence.pilot-readiness.v1",
        "pilot_count": len(rows),
        "ready_for_approved_test_count": sum(r["readiness_status"] == "ready_for_approved_test" for r in rows),
        "blocked_external_first_count": sum(r["readiness_status"] == "blocked_external_first" for r in rows),
        "blocked_company_gate_count": sum(r["readiness_status"] == "blocked_company_gate" for r in rows),
        "pilots": rows,
        "boundary": "This artifact is a fail-closed checklist. It does not connect internal company data and does not upgrade an external candidate.",
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {OUTPUT} ({report['blocked_external_first_count']} blocked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
