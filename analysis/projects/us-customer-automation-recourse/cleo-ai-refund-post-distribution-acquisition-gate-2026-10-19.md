# Cleo AI refund post-distribution acquisition gate

**Checked:** 2026-10-19  
**Status:** scheduled follow-up; payment delivery has not yet reached its announced start date

## Purpose

The Cleo AI route now has an official aggregate remedy announcement, but not a
recipient-level outcome. This gate defines the next lawful public-data pass so
that an announced payment is not counted as a received refund.

The planned sequence is:

```text
eligible consumer and notification
  -> PayPal payment sent
  -> delivery and account access
  -> acceptance, return, or reissue
  -> amount received and timing
  -> original loss, fee, or subscription correction
  -> household liquidity, repeat borrowing, trust, switching, or exit
```

## Authoritative schedule at this checkpoint

The FTC says that email notification may occur between October 8 and October
26, 2026; PayPal payments begin October 27, 2026; and recipients should accept
the payment within 30 days. The public announcement reports 2,124,796 planned
payments totaling more than $15.8 million. These are aggregate program facts,
not a recipient-level delivery or acceptance rate.

## Required next-pass fields

| Stage | Minimum observable field | Do not infer |
|---|---|---|
| Notification | announcement, notice channel, notice date/window | that every eligible person saw the email |
| Delivery | payment initiated, delivered, failed, or returned; date | delivery from eligibility or email list size |
| Acceptance | accepted, declined, expired, or reissued; date | receipt from payment initiation |
| Amount | individual or distribution-level amount and timing | adequacy from the aggregate total |
| Correction | subscription cancellation, fee correction, account status, or residual claim | restored household liquidity from payment alone |
| Later outcome | repeat cash-advance use, alternative borrowing, repayment, trust, switching, or exit | changed behavior from accepting a refund |

## Lawful acquisition boundary

Use only the FTC refund page, official post-distribution announcements,
administrator aggregate reports, and privacy-preserving follow-up that has
explicit authorization. Do not seek recipient names, PayPal account data, or
raw administrator files. If the administrator publishes only aggregate totals,
record the stage as aggregate reported receipt and leave person-level receipt,
adequacy, and later outcome open.

## Timing and stopping rule

1. Recheck the official FTC refund page on or after **2026-10-27** for a
   delivery-start or distribution update.
2. Recheck after the stated 30-day acceptance window closes, using the actual
   administrator deadline if the FTC updates it.
3. Stop the public pass when the available record supplies no new stage field;
   record that observability boundary rather than repeating the same aggregate
   announcement.

## Current boundary

At the 2026-10-19 checkpoint, the route closes official allegations, settlement,
eligibility framing, notification window, planned payment count/value, payment
start date, and acceptance instruction. It leaves delivery, acceptance, return,
reissue, amount by recipient, adequacy, account correction, household recovery,
repeat borrowing, trust, switching, and exit unresolved.

## Live-source checkpoint — 2026-10-19

The current FTC refund page and October 2026 announcement were opened and
rechecked on this date. Both still state that notifications run through October
26, 2026, PayPal payments begin October 27, 2026, and recipients should accept
payments within 30 days. No delivery, acceptance, return, reissue, or
recipient-level outcome field has been added to the public record at this
checkpoint.

## Sources

- [FTC Cleo AI refund page](https://search.ftc.gov/enforcement/refunds/cleo-ai-refunds)
- [FTC refund announcement, October 8, 2026](https://search.ftc.gov/news-events/news/press-releases/2026/10/ftc-returns-more-158-million-consumers-misled-cash-advance-app-company-cleo-ai)
- [Cleo AI event ledger](data/ftc-cleo-ai-refund-planned-payment-event-ledger-v1.json)

**Evidence status:** official aggregate schedule and remedy-administration
boundary; recipient-level delivery, receipt, adequacy, and later outcome are
not yet observable.
