# Uber / Waheed merits and remedy record v1

**Status:** primary merits decision establishes unfair deactivation and
reactivation/lost-pay orders in principle; amount, receipt, and durability
remain open

**Checked:** 2026-09-15

## Why this record matters

Waheed upgrades one of the Australian census cases from a timing or access
question to a full merits/remedy record. The Fair Work Commission found that
Uber's deactivation was not consistent with the Digital Labour Platform
Deactivation Code and was unfair. The Commission ordered reactivation and
ordered lost remuneration in principle, but directed further information
before quantifying the amount.

## Event chain

| Date | Event | Evidence status | Boundary |
|---|---|---|---|
| 17 Jun 2025 | Deactivation took effect | Primary FWC decision | The Commission resolved the date dispute in the worker's favour |
| 18 Sep 2025 | Timing decision held the application within time | Primary FWC decision | No merits finding in that earlier decision |
| 21 May 2026 | Merits decision found Code non-compliance and unfair deactivation | Primary FWC decision | The decision is not a payment receipt or proof of later access |
| 21 May 2026 | Reactivation ordered within 7 days on prior terms | Primary FWC decision | Actual compliance and continued work remain open |
| 21 May 2026 | Lost remuneration ordered in principle; quantum deferred | Primary FWC decision | No amount or payment deadline is established in the decision located |

## What the Commission found

The decision identifies several procedural failures rather than treating
“human review” as a sufficient label:

- warnings did not include the mandatory opportunity to seek assistance or
  support;
- warning, preliminary, and final notices used general descriptions that did
  not give sufficient information to understand the allegations;
- Uber did not make further inquiries reasonably warranted by the matters;
- Uber had told the worker that some earlier complaints were resolved, then
  later relied on those complaints in the deactivation decision; and
- the worker relied on Uber income as his primary household income source.

The decision therefore links notice quality, evidentiary inquiry, historical
administrative memory, and household dependence. It does not establish that an
autonomous algorithm made the decision; the case remains coded as
platform-mediated control.

## Remedy coding

```text
application within time           observed_adjudicated
Code compliance                    adjudicated_insufficient
valid reason                       adjudicated_not_established
unfair deactivation                observed_adjudicated
reactivation order                 observed_adjudicated
same prior terms                   observed_adjudicated
lost-pay entitlement/order         observed_adjudicated_in_principle
lost-pay amount                    open
payment receipt                    not_observed
actual continued access            not_observed
profile or reason correction       not_observed
recurrence/non-retaliation        not_observed
```

The remedy chain is consequently:

```text
opaque/repeated complaints
  -> inadequate notices and inquiry
  -> unfair deactivation finding
  -> reactivation order
  -> lost-pay calculation [open]
  -> payment/access/durability [open]
```

## Comparison with the Australian cases

Waheed is distinct from the timing-only and settled cases in the census. It
also extends the order-level findings already observed in Mansoor, Al Hussein,
Warraich, Khan, Hotak, and Rehman:

1. The Commission can test whether earlier platform messages were sufficiently
   particular, not merely whether a message existed.
2. A platform's statement that a complaint was “resolved” can become relevant
   evidence when the same complaint is later revived as a deactivation reason.
3. Reactivation and financial restoration remain separate remedial tasks.
4. Household dependence is a relevant consequence of platform exclusion, but
   the decision does not quantify the household's later recovery.

## Decisive next acquisition

Locate the follow-on order or directions that quantify Waheed's lost pay, then
seek evidence of payment, account access, and later recurrence. Preserve the
appeal status separately from the merits and implementation fields; an appeal
does not itself suspend or reverse the primary order in this ledger.

## Sources

- [Waheed, [2026] FWC 1801 — primary merits and remedy decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2026fwc1801.pdf)
- [Waheed, [2025] FWC 2787 — timing decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc2787.pdf)
- [Fair Work Commission decision and order search](https://www.fwc.gov.au/hearings-decisions/find-decisions-and-orders)

## Boundary

The primary decision establishes unfair deactivation, Code failures,
reactivation, and lost-pay entitlement in principle. It does not establish the
amount, payment receipt, actual post-order access, corrected platform records,
recurrence prevention, or anti-retaliation.
