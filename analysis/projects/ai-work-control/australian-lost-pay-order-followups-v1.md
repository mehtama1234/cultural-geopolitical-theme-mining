# Australian lost-pay order follow-ups v1

**Status:** primary order-level implementation comparison; payment receipt and
durability remain open

**Checked:** 2026-09-15

## Why this record matters

The Australian packet previously established several reactivation and lost-pay
orders, but it did not consistently separate the later order document from the
underlying merits decision. The Fair Work Commission's order records for
Mansoor and Al Hussein make that separation visible. They add enforceable
deadlines and payment instructions, but still do not prove that the worker
received money or retained access without later harm.

## Newly verified order events

| Matter | Primary order | What the order establishes | What remains open |
|---|---|---|---|
| Mansoor, `UDE2025/141` | `PR792727`, 17 Oct 2025 | Reinstatement within 7 days on prior terms; $6,073.23 gross less tax for lost earnings; payment within 14 days | Receipt, actual access, continued work, profile correction, recurrence, non-retaliation |
| Al Hussein, `UDE2025/134` | `PR792947`, 24 Oct 2025 | Reinstatement on prior terms; deemed work during the interruption; compliance deadline of 31 Oct 2025 | Lost-pay quantum, payment, actual access, continued work, recurrence, non-retaliation |

The Mansoor order is a payment order with a specified amount and deadline. It
is not a receipt. The Al Hussein order is a formal access-restoration order,
but the order document located in the current search frame does not establish a
quantified later payment.

## Remedy chain

```text
unfair deactivation
  -> merits finding
  -> reactivation order
  -> lost-pay order or quantum direction
  -> payment deadline
  -> payment receipt / continued access / durable protection
```

| Arrow | Mansoor | Al Hussein |
|---|---|---|
| Adjudicated unfairness | observed | observed |
| Reactivation order | observed | observed |
| Same prior terms | observed | observed |
| Lost-pay amount | `$6,073.23` ordered | not quantified in located order |
| Payment deadline | 14 days from 17 Oct 2025 | not observed in located order |
| Receipt | not observed | not observed |
| Continued access | not observed | not observed |
| Recurrence/non-retaliation | not observed | not observed |

## Interpretation

These orders show why “remedy” is not a single binary variable. The legal
institution can specify a restored contractual position, deem work to have
been performed during the interruption, calculate lost earnings, and impose a
deadline. Each step increases institutional legibility and potential
enforceability. None of those steps alone demonstrates that the worker's
income, account, rating, or bargaining position actually recovered.

Mansoor also makes the financial bridge more concrete. The amount is not a
generic compensation award: it is framed as lost earnings caused by the
deactivation and is subject to tax treatment. A follow-up study must therefore
capture the order date, amount, deadline, receipt, and any deductions as
separate fields.

Al Hussein demonstrates a different open join. The Commission ordered
reactivation while directing the parties to confer on lost-pay quantum. A
worker can therefore obtain formal access restoration while the financial
consequence remains administratively unresolved. This is the same structural
gap identified in Hotak and Warraich, now visible alongside an order that
states a concrete compliance date.

## Coding rule

```text
amount ordered       != payment received
deadline specified   != deadline met
access ordered       != access verified
reactivation         != profile correction
formal restoration   != durable non-retaliation
```

The normalized ledger should promote only the fields established by the order.
It should not infer payment from the passage of a deadline, or access from the
existence of a reinstatement direction.

## Decisive next acquisition

Search the FWC document system for post-order payment directions, variation
orders, compliance correspondence, or later merits documents for these exact
matters. The strongest worker-outcome upgrade would be a consented worker-side
record or platform communication showing payment and continued account access,
paired with a date and evidence type.

## Sources

- [Mansoor, [2025] FWC 3111 — merits decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc3111.pdf)
- [Mansoor, PR792727 — reactivation and $6,073.23 order](https://www.fwc.gov.au/documents/awardsandorders/pdf/pr792727.pdf)
- [Al Hussein, [2025] FWC 3176 — merits decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc3176.pdf)
- [Al Hussein, PR792947 — reactivation order](https://www.fwc.gov.au/documents/awardsandorders/pdf/pr792947.pdf)
- [Fair Work Commission decision and order search](https://www.fwc.gov.au/hearings-decisions/find-decisions-and-orders)

## Boundary

This record establishes primary order contents and deadlines. It does not
establish payment receipt, actual or continuing account access, corrected
platform records, recurrence prevention, or anti-retaliation.
