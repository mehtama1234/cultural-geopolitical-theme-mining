# Remedy durability is a separate stage from remedy issuance

**Checked:** 2026-09-18  
**Status:** bounded cross-domain synthesis; no pooled recovery rate claimed  
**Scope:** US consumer, worker, and product-safety records with a visible
institutional response and at least one implementation or follow-up signal

## The finding

Across the retained records, institutions are often able to document a remedy
before they can document durable restoration for the affected person. A refund
can be issued without public evidence of receipt or restored household room. A
repair can be reported without proof that the owner was reached, the product
became safe, or the repair held. A worker payment or access order can exist
without payment receipt, restored opportunity, or protection against recurrence.

The useful chain is therefore:

```text
harm or restriction
  -> remedy offered or ordered
  -> implementation/payment/repair recorded
  -> recipient or user actually receives it
  -> protected condition is restored
  -> restoration persists without repeat harm
  -> trust, continued use, switching, or exit changes
```

The first three stages are visible in several public records. The last four
are usually missing or belong to a different denominator. This is not evidence
that remedies failed; it is evidence that public administrative visibility
ends earlier than lived recovery.

## Cross-domain comparison

| Route | What is observed | What remains open |
|---|---|---|
| Amazon Prime subscription redress | Court and FTC records separate the $1.5B refund pool, aggregate dollars issued and accepted, claims stages, eligibility expansion, and future payment timing | Account-level eligibility, notice, receipt, amount adequacy, delay, continued use, switching, trust, and household recovery |
| Sauna360 product recall | A 2025 repair route is followed by a 2026 CPSC expansion stating that the earlier repair was ineffective and requiring another professional repair | Owner notice, completed second repair, safe restoration, downtime/residual cost, trust, continued use, and non-use |
| VRURC and Honda Talon recalls | Recall-key notices, offered replacement or dealer-repair routes, and reported correction snapshots are visible | Purchaser exposure, notice reach, repair/replacement receipt, safe use, denominator-compatible recovery, and exit |
| Amazon Flex worker refunds | FTC/administrator records show distribution rounds, reissue routes, and aggregate reach, including reported fully compensated drivers | Driver-level receipt, remaining loss, continued or alternative work, bargaining position, durability, and exit |
| Apple PERM recruitment remedy | DOJ reports required electronic/external recruitment controls, individualized lost-income review, and an exhausted $18.25M back-pay fund | Applicant-level receipt, restored consideration or hiring, monitoring findings, recurrence, household recovery, trust, and exit |
| Meadley employment enforcement case | Official FWC follow-up reports compensation payment and further court-ordered money after failed reinstatement | Worker-confirmed receipt, restored job, later employment, household recovery, recurrence, trust, and exit |
| CFPB named redress and reissue routes | BrightSpeed, Navient, and ADSS expose aggregate distribution or check stages; an Ombudsman record exposes recipient-side reissue facilitation | Recipient receipt, account/loan correction, residual loss, durable financial recovery, trust, switching, and exit |
| IER employment remedies | Agency summaries report individual paid remedies or offers plus employer training/policy changes | Independent receipt, accepted reinstatement, later employment, recurrence, household recovery, trust, and action |
| Platform access cases | Some cases show review, reactivation, substitute earnings, or ordered lost remuneration | Payment, actual account status, recurrence protection, freely chosen alternatives, worker recovery, and exit |

These are deliberately not pooled. A dollar issued, a check accepted, a
repair count, a payment offer, an access order, and a reported correction are
different units and clocks.

## What this adds to the atlas

1. **Remedy is not one endpoint.** The program should distinguish offered,
   ordered, implemented, received, adequate, durable, and socially meaningful
   remedies.
2. **Repeat correction is evidence about durability, not automatically failure
   prevalence.** Sauna360 is a clear counterexample to treating a completed
   first repair as permanent safety; it does not reveal how many owners were
   affected or whether the second repair succeeded.
3. **Aggregate distribution is not individual recovery.** Amazon Prime and
   Amazon Flex show stronger implementation visibility than a bare settlement,
   but aggregate issued/accepted or reach figures cannot establish each
   recipient's receipt, remaining loss, or later behavior.
4. **Institutional legitimacy requires a longer clock.** Trust, switching,
   non-use, and continued use are not implied by payment or correction. They
   must be observed separately for the same unit and after the response.

## Evidence boundary

The synthesis supports a recurring mechanism: public systems and firms can
make response capacity visible while leaving the recipient's durable option
set unobserved. It does not estimate remedy success, consumer harm, worker
welfare, safety restoration, or trust change. The source units include named
cases, recall keys, program cohorts, and agency summaries rather than a common
population denominator.

The [portfolio remedy-stage audit](remedy-stage-coverage-audit-v1.md) shows that
the reported-receipt stage is explicit for 9 of 206 event rows, while 32 rows
have at least one standardized remedy-stage value. The remaining 174 rows are
unknown at the standardized stage field, not coded as no remedy. These are
measurement-coverage results, not remedy-failure rates.

The next decisive artifact is a bounded, identifier-compatible follow-up that
preserves:

- original exposure and responsible actor;
- available alternative or non-use choice;
- effort, money, time, and residual loss;
- remedy offer/order, implementation, receipt, amount, and date;
- protected and sacrificed outcomes;
- repeat harm or repeat correction;
- continued use, switching, non-use, trust, or exit.

Until that artifact exists, the atlas should describe remedy visibility and
durability gaps—not convert institutional completion into lived recovery.

## Source records

- [Amazon Prime refund record](../../records/us-ftc-amazon-prime-enrollment-refunds-2026.json)
- [Sauna360 repeat-remedy ledger](../us-marketplace-product-safety/data/sauna360-repeat-remedy-event-ledger-v1.json)
- [VRURC recall record](../../records/us-cpsc-vrurc-recall-implementation-2023-2026.json)
- [Honda Talon recall record](../../records/us-cpsc-honda-talon-recall-implementation-2023-2026.json)
- [Amazon Flex refund record](../../records/us-ftc-amazon-flex-driver-tip-refunds-2026.json)
- [Apple PERM implementation ledger](../ai-work-control/data/apple-perm-backpay-implementation-event-ledger-v1.json)
- [Meadley payment/enforcement ledger](../ai-work-control/data/fwc-meadley-enforced-payment-no-reinstatement-event-ledger-v1.json)
- [CFPB named redress ledger](data/cfpb-named-redress-route-event-ledger-v1.json)
- [CFPB Ombudsman reissue ledger](data/cfpb-ombudsman-redress-reissue-event-ledger-v1.json)
- [IER individual-remedy record](../../records/us-doj-ier-individual-remedy-followups-2026.json)
- [Platform remedy record](../../records/us-platform-remedy-restoration-dependence-2024-2026.json)
