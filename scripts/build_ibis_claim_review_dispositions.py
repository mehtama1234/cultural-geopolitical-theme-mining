#!/usr/bin/env python3
"""Record conservative, evidence-backed triage dispositions for IBIS claims."""

from __future__ import annotations

import json
from pathlib import Path


ANALYSIS = Path(__file__).resolve().parents[1] / "analysis" / "external-trend-intelligence"
INPUT = ANALYSIS / "ibis-first-review-batch.json"
OUTPUT = ANALYSIS / "ibis-claim-review-dispositions.json"


def main() -> int:
    batch = json.loads(INPUT.read_text())
    def summarize(target: dict, *, disposition: str, independence_finding: str, outcome_finding: str, counter_signal: str, next_test: str) -> dict:
        publisher_counts = {}
        source_type_counts = {}
        for source in target["sources"]:
            publisher_counts[source.get("publisher", "unknown")] = publisher_counts.get(source.get("publisher", "unknown"), 0) + 1
            source_type_counts[source.get("source_type", "unknown")] = source_type_counts.get(source.get("source_type", "unknown"), 0) + 1
        return {
        "review_id": target["review_id"],
        "industry_slug": target["industry_slug"],
        "claim_id": target["claim_id"],
        "claim_text": target["claim_text"],
        "review_scope": "repository_metadata_triage",
        "review_status": "triage_complete_full_review_required",
        "disposition": disposition,
        "evidence_checked": {
            "source_count": len(target["sources"]),
            "publisher_counts": publisher_counts,
            "source_type_counts": source_type_counts,
            "missing_published_at_count": sum(source.get("published_at") is None for source in target["sources"]),
            "source_urls": [source.get("url") for source in target["sources"]],
        },
        "independence_finding": independence_finding,
        "outcome_finding": outcome_finding,
        "rights_finding": "Not verified for the exact artifacts; retain links as evidence locators only.",
        "counter_signal": counter_signal,
        "next_test": next_test,
        "company_bridge_status": "blocked_external_first_gate",
        "stop_rule": "Do not count this claim as independent confirmation, use it to qualify the IBIS finding, or connect it to internal company data until the missing lineage, rights, and outcome fields are completed.",
        }
    target = next(row for row in batch["claims"] if row["review_id"].endswith("drug-and-alcohol-test-kit-manufacturing::test-demand"))
    repair = next(row for row in batch["claims"] if row["review_id"].endswith("cell-phone-repair::repair-policy"))
    atm = next(row for row in batch["claims"] if row["review_id"].endswith("atm-manufacturing::atm-cash"))
    eating = next(row for row in batch["claims"] if row["review_id"].endswith("eating-disorder-clinics::ed-need"))
    flying = next(row for row in batch["claims"] if row["review_id"].endswith("flying-schools::flight-demand"))
    shelter = next(row for row in batch["claims"] if row["review_id"].endswith("community-housing-and-homeless-shelters-in-the-us::shelter-affordability"))
    dna = next(row for row in batch["claims"] if row["review_id"].endswith("dna-and-dna-forensic-laboratories::dna-public"))
    family = next(row for row in batch["claims"] if row["review_id"].endswith("family-law-and-divorce-lawyers-and-attorneys::family-demographics"))
    oven = next(row for row in batch["claims"] if row["review_id"].endswith("commercial-oven-manufacturing::com-scale"))
    financial = next(row for row in batch["claims"] if row["review_id"].endswith("financial-data-service-providers::fdsp-alternative"))
    dispositions = [
        summarize(
            target,
            disposition="held_insufficient_evidence",
            independence_finding="Not established: three of four source rows are Quest Diagnostics material, and the local records do not establish whether those publications share an underlying study, sample, or methodology.",
            outcome_finding="Not observed: the artifact lists candidate measures such as test volume, positivity, turnaround, and lab capacity but contains no dated independent outcome series.",
            counter_signal="The government source describes population substance-use context, while the company sources describe a vendor's testing observations; the populations and denominators are not interchangeable.",
            next_test="Recover the exact Quest methodology and sample frame, then acquire an independent dated testing-volume or positivity series with a compatible population and denominator.",
        ),
        summarize(
            repair,
            disposition="held_outcome_missing",
            independence_finding="Provisional source diversity only: New York Attorney General and Colorado General Assembly are distinct government publishers and URLs, with no shared host in the pinned metadata. This is not yet a verified independent comparison because publication dates and underlying policy-document lineage remain unresolved.",
            outcome_finding="Not observed: state policy materials establish legal or program context but do not provide a comparable repair-volume, repair-versus-replace, e-waste, or device-life outcome series.",
            counter_signal="Two state policy examples may not represent national policy adoption or consumer behavior; states differ in implementation, coverage, and effective dates.",
            next_test="Verify the enacted-law versions and effective dates, then acquire a dated independent outcome series with a defined device population and denominator (repair volume, repair rate, device age, or e-waste).",
        ),
        summarize(
            atm,
            disposition="held_outcome_missing",
            independence_finding="Publisher diversity is provisional: ATM Advantage and Federal Reserve Financial Services are distinct hosts, but the metadata does not establish whether the trade article restates the same Fed evidence or uses a compatible population.",
            outcome_finding="Not observed: the claim has no dated outcome candidates in the pinned artifact for cash use, withdrawal volume, transaction share, or ATM economics.",
            counter_signal="Cash-importance context and ATM-location economics are different measures; neither establishes a persistent consumer or operator trend by itself.",
            next_test="Recover the underlying Federal Reserve survey/table and acquire a dated transaction or cash-use series with a stated denominator before any trend claim.",
        ),
        summarize(
            eating,
            disposition="held_insufficient_evidence",
            independence_finding="Not established: NIMH and NIH are both U.S. federal health publishers, and the local metadata does not establish separate study, sample, or methodological lineage.",
            outcome_finding="Not observed: candidate measures are listed, but no dated independent clinic demand, wait-time, treatment, or utilization outcome is attached.",
            counter_signal="A federal evidence page and a federal research page can describe need without measuring clinic capacity or realized service use.",
            next_test="Map the exact NIMH/NIH source artifacts and acquire a dated independent utilization or capacity series with a defined population and denominator.",
        ),
        summarize(
            flying,
            disposition="held_insufficient_evidence",
            independence_finding="Not established: all six source rows are flight-school company pages; distinct URLs do not establish independent market evidence and may reflect promotional positioning.",
            outcome_finding="Not observed: the artifact lists candidate demand measures but contains no dated enrollment, completion, utilization, or licensing outcome series.",
            counter_signal="School-reported offerings and testimonials can coexist with flat or declining realized student demand; the source frame cannot resolve that direction.",
            next_test="Acquire an independent FAA, enrollment, certification, or utilization series and separate company marketing claims from observed outcomes.",
        ),
        summarize(
            shelter,
            disposition="held_outcome_missing",
            independence_finding="Provisional source diversity only: Urban Institute Housing Matters and DESC are distinct publishers, but the metadata does not establish a common rent-burden definition, underlying survey lineage, or independent outcome linkage.",
            outcome_finding="Not observed: the claim reports affordability context but no dated shelter inflow, exit, bed, unit, or operating outcome with a compatible denominator.",
            counter_signal="Rent burden can rise without shelter demand moving in the same direction; affordability is a mechanism hypothesis, not an operator outcome.",
            next_test="Map the exact rent-burden estimate and acquire a dated independent shelter-demand or housing-exit measure with geography and denominator.",
        ),
        summarize(
            dna,
            disposition="held_insufficient_evidence",
            independence_finding="Not established: Bureau of Justice Assistance and Grants.gov are both government publication routes, and the metadata does not establish separate study lineage or independent measurement.",
            outcome_finding="Not observed: candidate measures are listed, but no dated forensic-lab workload, turnaround, case volume, or utilization outcome is attached.",
            counter_signal="A grant or program announcement can document policy attention without measuring realized laboratory demand or capacity.",
            next_test="Recover the underlying program and award artifacts, then acquire a dated independent forensic workload or capacity series with an explicit denominator.",
        ),
        summarize(
            family,
            disposition="held_insufficient_evidence",
            independence_finding="Provisional diversity only: Divorce.com is a company source and Bowling Green State University is academic, but the metadata does not establish whether the reported demographic measures use compatible populations or independent source data.",
            outcome_finding="Not observed: demographic context is not a dated legal-service demand, filings, case volume, or conversion outcome.",
            counter_signal="Population or marriage trends do not automatically translate into demand for a specific legal-service channel.",
            next_test="Document the population and period for each source and acquire an independent dated family-law filing or service-utilization outcome.",
        ),
        summarize(
            oven,
            disposition="held_insufficient_evidence",
            independence_finding="Not established: the four source rows are company or company-filing materials, including an Ali Group/Welbilt relationship; distinct URLs cannot count as independent market confirmation.",
            outcome_finding="Not observed: the artifact lists candidate commercial-oven measures but no independent dated orders, shipments, installed base, or utilization series.",
            counter_signal="Corporate product and filing statements can describe strategy or positioning without revealing market-wide realized demand.",
            next_test="Acquire an independent shipment, trade, procurement, or installed-base series and resolve the Ali/Welbilt source lineage before review.",
        ),
        summarize(
            financial,
            disposition="held_insufficient_evidence",
            independence_finding="Not established: the four rows mix trade/research firms and a company source; the metadata does not establish separate samples, methods, or underlying data ownership.",
            outcome_finding="Not observed: candidate measures are listed, but no dated independent revenue, client, adoption, or workflow outcome is linked to the claim.",
            counter_signal="Vendor and analyst descriptions of alternative data can reflect market narratives rather than measured buyer adoption or realized outcomes.",
            next_test="Map each publisher's underlying dataset and acquire an independent dated buyer, adoption, or revenue measure with a defined denominator.",
        ),
    ]
    disposition_ids = {row["review_id"] for row in dispositions}
    pending = [row["review_id"] for row in batch["claims"] if row["review_id"] not in disposition_ids]
    payload = {
        "schema": "external-trend-intelligence.ibis-claim-review-dispositions.v1",
        "finding_slug": batch["finding_slug"],
        "source_revision": batch["source_revision"],
        "status": "ten_conservative_triage_dispositions_recorded",
        "review_method": "metadata-only triage from pinned repository artifacts; not legal rights clearance or independent outcome validation",
        "completed_disposition_count": len(dispositions),
        "pending_first_batch_count": len(pending),
        "pending_review_ids": pending,
        "dispositions": dispositions,
        "next_action": "Complete the remaining first-batch reviews, then acquire dated independent outcomes for claims that survive metadata triage.",
        "boundary": "This artifact records ten held triage dispositions. It does not qualify any claim, establish source independence, clear rights, validate an outcome, or authorize a company bridge.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(dispositions)} dispositions; {len(pending)} first-batch claims pending)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
