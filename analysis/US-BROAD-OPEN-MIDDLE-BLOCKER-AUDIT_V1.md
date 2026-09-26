# Open-middle blocker audit v1

**Checked:** 2026-09-21  
**Scope:** the 97-ledger broad portfolio
**Purpose:** identify which missing stages prevent the atlas from becoming a
same-unit end-to-end account. This is a gap audit, not a recovery estimate.

## Result

The portfolio has 164 explicitly open arrows. The open arrows do not all mean
the same thing. A single arrow can name more than one missing field, so the
categories below overlap and must not be added together.

The communication layer now contains 367 numbered findings, but that larger
reader does not alter this ledger result: the broad event portfolio now has
98 ledgers, 302 events, 454 arrows, and 164 open middle-stage arrows.

| Open stage family | Open-arrow mentions | What is missing in plain language |
|---|---:|---|
| Later outcome or durability | 117 | Did the fix last, or did the problem return? |
| Trust, meaning, or action | 105 | Did the experience change trust, identity, participation, or behavior? |
| Alternative, non-use, switching, or exit | 123 | What could the affected unit actually do instead, and did it do so? |
| Receipt or implementation | 80 | Did the person, household, worker, or customer actually get and use the remedy? |
| Money, time, or adequacy | 74 | What was the amount, time cost, residual loss, or practical sufficiency? |
| Unit, denominator, eligibility, or attribution | 66 | Can the result be tied to the same person/account/firm and responsible actor? |

## Where the bottleneck is concentrated

The largest open-arrow clusters are not one universal societal chain. They are
several recurring conversion problems:

1. **Worker remedies:** public orders and reported payment can be observed, but
   payment receipt, continued or alternative work, household recovery, and
   durable trust are usually not retained in the public record. The DOL
   Workers Owed Wages route adds an earlier handoff: even recovered wages can
   remain in a locate/notice/claim process before the worker can use them.
2. **Consumer and public redress:** distribution, reissue, or a reported repair
   can be observed, but recipient-level receipt, account correction, adequacy,
   and later switching are usually missing. The new SNAP EBT route adds a
   sharper control failure: an issued benefit can be stolen before it becomes
   usable food access. The new Medicare Advantage route adds a second gate:
   an authorization can be formally reversed after an appeal while admission,
   interim care, and functional recovery remain unknown.
3. **Infrastructure and geopolitical capability:** governance, capacity,
   schedules, and route decisions can be observed, but household incidence,
   acceptance, delivered/accepted output, and changed external behavior remain
   open.
4. **Political meaning:** hardship, trust, approval, contact, and action can be
   measured on related surfaces, but a dated burden, attribution, remedy, and
   later response are rarely held on the same unit.

The UAS route now makes the required middle fields concrete rather than
abstract. Its public documentation identifies respondent-wave identity,
weights, dated shocks, and later wellbeing; UAS 537 adds billing contact,
effort/time, respect, and reported billing result; UAS 698 adds outside help,
amount, foregone care, and reasons such as cost, delay, scheduling, work/care
conflict, and transportation. These fields could connect obligation to choice
and institutional response, but the route remains registration-gated and no
respondent file, overlap, receipt, adequacy, or later recovery is currently
observed. Treat this as an acquisition specification, not a completed bridge.

## Formal access/control checkpoint

The [formal-access/control synthesis](US-BROAD-FORMAL-ACCESS-CONTROL-CONVERSION-SYNTHESIS_V1.md)
now consolidates four bounded routes: SNAP EBT theft, Medicare Advantage
prior-authorization reversal, wildfire-insurance partial payment, and consumer
redress. They do not share one cause or effect. They share a measurement rule:
formal availability must be separated from usable control.

The route boundary is often the decisive selection mechanism. A person who
cannot notice a theft, file an appeal, gather documents, wait safely, cash a
payment, or use a replacement disappears from later success counts. This does
not prove that the institution failed in every case; it means a distribution,
reversal, or approval cannot stand in for recipient-level recovery.

This checkpoint changes the next-pass design in one practical way: retain
failed and successful route attempts in the same denominator. For each episode,
capture notice/knowledge, effort, interim substitute, decision, actual receipt
or access, adequacy, and later durability before interpreting trust, switching,
voice, or exit.

## What this changes about the next pass

The next pass should not add another broad sentiment or aggregate distribution
count. It should target one of these compact, lawful follow-ups:

- an authorized UAS Older Ages or PSID file with a stable respondent key and a
  dated event followed by effort, outcome, and later persistence;
- a recipient/account-level redress or repair follow-up with status, receipt,
  correction, and later use; or
- an identifier-bearing defense or infrastructure follow-up that distinguishes
  planned delivery from shipment, acceptance, fielding, operation, and changed
  behavior.

If those inputs are unavailable, the correct output is an explicit acquisition
boundary, not a stronger causal claim. The current portfolio already has broad
coverage; its limiting factor is observability of the middle and the later
outcome.

## Priority decision after the worker-route recheck

The worker-remedy lane is the highest-yield public partial chain currently
retained. The Mudiyanselage case contains a bounded job-loss episode, forced
exit, constrained alternative employment, partial payment, compensation order,
and worker-linked refusal to return because trust was broken. The official
later-outcome search found no public final-payment, compliance, new-job
durability, household, or later-action record. This is an acquisition
boundary—not evidence that the order failed.

The next serious acquisition should therefore seek a privacy-preserving
payroll, compliance, worker-confirmed, or later-employment follow-up for one
named remedy case. Its minimum fields are payment receipt, accepted work or
non-use, pay/hours/commute trade-off, later work status, recurrence, and trust
or exit where directly measured. Until that exists, do not promote the worker
case to durable recovery or practical exit, and do not replace it with another
aggregate remedy count.

## Method boundary

Counts were computed from each ledger's `arrows` array in
`analysis/data/us-broad-event-ledger-index-v1.json`, retaining only arrows with
`status: "open"`. Gap-family counts use phrase matching against each arrow's
`remaining_gap` field and are intentionally overlapping. The machine-readable
version is [the open-middle blocker audit JSON](data/us-broad-open-middle-blocker-audit-v1.json).
The [scope-check script](../scripts/audit_open_middle_blockers.py) independently
recomputes the 98-ledger, 302-event, 454-arrow, and 164-open-arrow scope and
prints an exploratory phrase screen. Its phrase screen is deliberately not
used to overwrite the stored family counts, because the calibrated family
classification and the exploratory token groups are different diagnostics.
These are planning diagnostics, not statistical estimates of societal
prevalence.
