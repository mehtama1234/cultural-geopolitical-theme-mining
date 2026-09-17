# Finding 025: First American payment-processor refunds expose business exit fees without proving replaceability

**Status:** provisional named small-business remedy finding · **Checked:** 2026-09-17

## The bounded finding

The Federal Trade Commission reports that First American Payment Systems sent
5,588 checks totaling more than $2.6 million in February 2025 to businesses
charged hidden or unauthorized fees. The FTC says the alleged practices
included early-termination fees and “zombie charges,” and that First American
paid $4.9 million to settle.

The current January 2026 page says the FTC is still reviewing claims and that
refund amounts depend in part on how many businesses file. This separates a
completed check distribution from an unresolved claims-review population.

The safe interpretation is:

> A payment processor can impose a fee structure that makes exit costly for a
> small business, while enforcement can produce a recipient-counted refund
> program. The public record does not show whether businesses cashed checks,
> changed processors, recovered lost transaction capacity, or became more able
> to resist future fees.

## Event chain

```text
payment processing and enrollment terms
  -> hidden/unauthorized fees and early-termination or zombie charges
  -> FTC enforcement and settlement
  -> 5,588 checks totaling more than $2.6m
  -> [open] cashing, processor switch, business continuity, bargaining, or exit
```

## What the public record supplies

| Stage | Observed evidence | Still open |
|---|---|---|
| Business dependency | First American payment processing is the service relationship | Contract terms, processor alternatives, switching cost, and transaction dependence |
| Fee practice | FTC identifies hidden/unauthorized fees, early-termination fees, and zombie charges | Individual incidence, notice, dispute effort, and operational interruption |
| Formal response | FTC settlement and claims administration; company paid $4.9m | Compliance, recurrence, and contract-practice change |
| Distribution | 5,588 checks totaling more than $2.6m | Amounts by business, cashing, failed delivery, timing, and residual loss |
| Claims boundary | FTC says claims are currently under review and amount depends partly on claim volume | Eligible and filed-claim denominator, approvals, denials, and later payments |
| Business outcome | Refund route makes monetary response visible | Processor switching, payment acceptance, revenue, survival, and exit |
| Meaning/action | Public enforcement creates a formal contest route | Trust, attribution, association, organizing, and political action |

## Why this matters to the broad atlas

Small firms are consumers of infrastructure. A payment processor controls a
basic operating interface for collecting revenue, and an early-termination
fee can convert nominal provider choice into constrained practical exit. This
case therefore connects firm/market power, local business capacity, consumer
recourse, hidden time/cost, and the question of whether a formal remedy changes
real replaceability.

It also makes a useful distinction between payment-program stages. The FTC
reports checks sent to 5,588 businesses, but the same public page says claims
are still being reviewed. Checks sent, claims reviewed, money cashed, and
business capacity restored are separate clocks and denominators.

## Coding consequence

```text
reported fee practice       != measured business-level burden
settlement payment          != processor switching
checks sent                 != checks cashed
refund                     != restored transaction capacity
formal exit right           != practical replaceability
```

Code this as **administrator-reported small-business refund distribution with
an active claims-review boundary; cashing, switching, continuity, and exit
open**. Do not treat the $2.6m total as an average refund without the
business-level amount distribution.

## Next decisive test

The smallest useful follow-up is a de-identified ledger separating eligible,
claim-filed, approved, check-sent, cashed, returned, denied, and unknown-status
businesses, paired where lawful with fee type, processor-switch attempts,
transaction interruption, replacement cost, and subsequent business
continuity. No business transaction archive is needed to specify that test.

## Sources and storage boundary

- [FTC First American Payment Systems Settlement refund page](https://www.ftc.gov/enforcement/refunds/first-american-payment-systems-settlement)
- [FTC active refund-program list](https://www.ftc.gov/enforcement/refunds)

The official HTML page was checked directly and hashed for reproducibility; no
business roster, transaction archive, or bulk claims file was downloaded or
retained.
