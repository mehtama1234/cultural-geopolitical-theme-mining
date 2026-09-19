# Uber / Hotak access-restoration follow-up record v1

**Status:** primary Full Bench record establishes voluntary reactivation,
continued work, and post-reactivation payment; separate lost-pay amount, receipt,
and durability remain open

**Checked:** 2026-09-18

The structured [broad event ledger](data/uber-hotak-end-to-end-event-ledger-v1.json)
records the five observed/open arrows without treating ordinary post-reactivation
payment as lost-pay recovery or durable protection.

## Why this record matters

Hotak supplies the first public follow-up in the Australian packet that goes
beyond a reactivation statement. The agreed facts recorded by the Full Bench
state that Uber restored access on 19 May 2025, the worker recommenced work,
and he completed more than 150 trips afterward. The merits decision also states
that he performed work and received payment from Uber after reactivation. This
is evidence of ordinary post-reactivation work payment, not proof that separate
lost remuneration was paid, that the pre-deactivation position was fully
restored, or that later retaliation was absent.

## Event chain

| Date | Event | Evidence status | Boundary |
|---|---|---|---|
| 8 Apr 2025 | Uber deactivated the worker | Primary agreed facts | Underlying platform decision and review record remain the merits question |
| Between 8 Apr and 19 May 2025 | The Full Bench recorded that the worker felt extremely stressed, anxious, and unsupported and experienced significant income loss and financial hardship during the interruption | Primary Full Bench bulletin/decision summary | This is a case-level adjudicated account of lived burden; it does not quantify net loss, establish causation beyond the case sequence, or measure later recovery |
| 19 May 2025 | Uber voluntarily reactivated access | Primary agreed facts | Voluntary access restoration is not the same as a formal remedial order |
| After 19 May 2025 | Full Bench record states the worker performed work and received payment from Uber | Primary merits decision | Amount/timing of ordinary work payment and any separate lost-remuneration payment are not disclosed |
| By 21 Jul 2025 | Worker had completed more than 150 trips after reactivation | Primary Full Bench record | The record does not establish net earnings, expenses, continued access after that point, or non-retaliation |
| 23 Sep 2025 | Full Bench found the Commission could still determine the unfair-deactivation application and ordered reactivation | Primary merits decision | Lost-pay quantum required further party consultation; payment receipt is open |

## What the record proves

The record supports four separate propositions:

1. Access was restored before the final merits decision.
2. Restoration was operational enough for the worker to perform more than 150
   trips, so the packet can code continued work activity rather than merely an
   asserted account change.
3. Voluntary restoration did not extinguish the Commission's jurisdiction or
   eliminate the need for a formal order.
4. The formal order preserved the possibility of restoring the worker's
   financial and contractual position, not only reopening an app account.
5. The merits record distinguishes payment for work performed after reactivation
   from the separate lost-remuneration remedy that remained to be calculated.

The record does not prove that the worker received the separate lost
remuneration, that the account remained active after the reported 150 trips,
that ratings or profiles were corrected, or that Uber changed its process for
other workers.

The case therefore now has a bounded lived-burden observation between the
deactivation and restoration stages: the legal record describes stress,
anxiety, feeling unsupported, income loss, and financial hardship. Those are
not a population prevalence estimate or a validated household-recovery
measure, but they prevent the chain from being read as only an administrative
access event.

## Coding

```text
voluntary_reactivation              observed_adjudicated_record
continued_access_after_reactivation observed_adjudicated_record
150_plus_trips                      observed_adjudicated_record
formal_reactivation_order           observed_adjudicated_record
post_reactivation_work_payment      observed_adjudicated_record
lost_pay_quantum                    open_after_direction_to_confer
lost_pay_payment_receipt            not_observed
profile_or_reason_correction        not_observed
recurrence_prevention               not_observed
anti_retaliation                    not_observed
```

This is a useful distinction for the remedy ledger:

```text
account reopened -> work performed/payment -> lost-pay recovery -> durable protection
       observed           observed                  open                  open
```

The first two arrows should not be silently promoted into the latter two.

## Targeted public-record recheck (2026-09-18)

The official Fair Work Commission decision index and bulletin route were
rechecked for `UDE2025/53`, `Hotak`, and a later lost-remuneration order. The
merits decision states that payment was received for work performed after
reactivation, while the reactivation order and decision preserve a separate
lost-remuneration calculation. The recheck did not locate a later public filing
that verifies payment of that separate remedy, net recovery, durable access, or
non-retaliation. This is an indexed-public-record boundary, not evidence that
the separate remedy was unpaid or that the worker stopped working.

The strongest currently observed chain remains:

```text
deactivation -> voluntary reactivation -> work/payment -> formal order
      observed            observed          observed       observed
lost-pay amount/order -> lost-pay receipt -> durable protection
       partial/open          open                open
```

## Interpretation

Hotak demonstrates why implementation evidence needs a clock and a unit. A
worker can return to the platform and produce observable work activity while
the legal system is still deciding whether a formal order is necessary and
what lost remuneration would restore the pre-deactivation position. The
institutional remedy therefore has at least two dimensions: renewed capacity
to work and reconstruction of the income position lost during exclusion.

It also sharpens the corporate-identity theme. The Full Bench agreed facts
identify Rasier Pacific as the platform operator and distinguish it from Uber
B.V. within the services arrangement. That named respondent structure made it
possible to litigate both access and the broader restoration question. It does
not resolve whether the worker could enforce every part of the order in
practice.

## Decisive next acquisition

Locate the later lost-remuneration order or party communication, then seek
worker-side evidence of payment and continued access. Preserve separate dates
and evidence classes for voluntary reactivation, formal reactivation order,
trip activity, payment, and later recurrence.

## Sources

- [Hotak, [2025] FWCFB 151 — agreed facts and 150-plus trips](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwcfb151.pdf)
- [Hotak, [2025] FWCFB 214 — merits and formal reactivation order](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwcfb214.pdf)
- [FWC Bulletin Volume 10/25 — Hotak case summary and remedy sequence](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-09-30.htm)
- [Fair Work Commission decision search](https://www.fwc.gov.au/hearings-decisions/find-decisions-and-orders)

## Boundary

The record establishes access restoration and subsequent trip activity in a
primary adjudicative document. It does not establish the worker's net income,
payment receipt, ongoing account status, corrected platform record, or
protection from retaliation.
