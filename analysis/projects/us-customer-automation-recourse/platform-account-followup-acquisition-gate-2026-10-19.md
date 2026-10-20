# Platform/account follow-up acquisition gate

**Checked:** 2026-10-19  
**Status:** bounded acquisition audit; no qualifying account-linked public route found

## Question

Can an existing U.S. consumer or platform record follow one stable account or
case from a control, complaint, or remedy attempt through institutional response,
recurrence, trust, and durable switching or exit?

The required chain is:

```text
dated account problem or control attempt
  -> feasible alternative and effort/time cost
  -> provider response and verified correction, payment, or access change
  -> repeat contact, recurrence, or continued exposure
  -> trust judgment and identified switching, non-use, or exit
```

## Candidate-route audit

| Candidate | What the repository has | Missing for qualification |
|---|---|---|
| CFPB complaint and monetary-relief records | Complaint receipt, routing, response labels, explanation, and monetary-relief categories | Account-level exposure, verified correction/payment, repeat contact, recurrence, trust, switching, exit, and non-complainant denominator |
| Block/Cash App enforcement follow-up | Official findings, operational corrective order, $75–120 million redress requirement, defined affected classes, and a 2026-10-19 CFPB payment-list recheck | No public recipient-level list, account correction, payment receipt, residual-loss measure, repeat exposure, trust, continued use, switching, or exit |
| FTC/administrator refund routes | Settlement, issued and sometimes accepted aggregate dollars, reissue instructions, and prospective controls | Stable recipient key, individual receipt and adequacy, account correction, repeat exposure, trust, continued use, switching, or exit |
| Walmart privacy requests | Company-reported access, deletion, and sale-opt-out counts with completion and denial stages | Consumer-level verification, residual data, re-collection, appeal, trust, switching, and durable non-use |
| Platform-worker remedy cases | Named cases with deactivation, appeal, restoration, payment orders, alternative work, and occasional continued trips | Common account key across proceedings, verified receipt, recurrence prevention, non-retaliation, trust, and voluntary platform exit |
| Consumer fraud follow-up | Linked survey exposure, loss, reporting, self-reported recovery, and later household context | Provider/account identity, verified recovery, replacement route, repeat exposure, continued use, switching, and non-use reason |

## Result

No candidate currently supplies all required fields for a defensible same-account
route. The strongest surfaces are complementary, not joinable: complaint data
show institutional routing; refund records show aggregate administration;
privacy records show reported completion; remedy cases show named procedural
stages; and survey follow-up shows reported household context. None follows the
same stable unit through the full chain.

This is an acquisition boundary, not evidence that consumers lack recourse or
that formal remedies fail. It means the current public records stop before the
later account state, recurrence, trust, and exit can be observed together.

The bounded Block/Cash App follow-up is now closed: on 2026-10-19 the CFPB
payments-by-case page contained no Block or Cash App entry in its ongoing or
closed lists, while the official Block page still supplied only a redress
contact route and order summary. The page's non-listing is not evidence that
no distribution occurred. It is a dated failure to observe the missing
recipient/account join. The next qualifying source must be a newly posted
distribution report or privacy-approved account-level follow-up.

## Hello Digit payment-notification checkpoint — 2026-10-19

The [Hello Digit redress record](../../records/us-cfpb-hello-digit-redress-payment-notification-2026.json)
adds a distinct remedy stage. The CFPB's current case page identifies a
2022 consent order requiring at least $68,145 in consumer redress for one
misrepresentation and a $2.7 million civil penalty, with EPIQ administering
payments. The same page lists an October 15, 2026 email-notification date.

This advances the route from enforcement and formal obligation to a dated
administration checkpoint. It does not establish email delivery, payment
delivery or acceptance, individual allocation, account correction, adequacy,
repeat exposure, trust, continued use, switching, or exit. The next useful
checkpoint is a public payment-status or administrator update after
notification; a notification date must not be promoted to receipt.

The CFPB's [Civil Penalty Fund page](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/civil-penalty-fund/)
also lists **$38,220 allocated to Hello Digit**. This closes an agency-level
funding-allocation stage after the original order, but it still does not expose
recipient count, individual amounts, payment delivery, returned payments,
acceptance, adequacy, account correction, or later household recovery. The
allocation is therefore recorded as a separate stage rather than as money
received.

A bounded read-only check of the CFPB-linked EPIQ administrator domain on
October 19 returned HTTP 403, and an exact-domain search located no separate
public payment-status page. This is an access limitation, not evidence of
nonpayment. The next lawful acquisition must use an accessible administrator
response, later CFPB update, or privacy-approved recipient record; the public
allocation cannot be promoted to receipt.

A fresh retrieval of the official CFPB case page on October 19 still exposes
only the order, EPIQ contact route, and October 15 email-notification date.
It does not add a payment-status, recipient, returned-payment, or account-
correction field. This confirms the acquisition boundary without treating a
repeated aggregate page check as a new remedy outcome.

Source: [CFPB Hello Digit payment-by-case page](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/hello-digit/).

## Smallest qualifying acquisition

Prioritize one lawful source with a stable account or case identifier and at
least two dated observations. The minimum fields are:

1. initiating problem or control request and date;
2. account/product/provider and feasible alternative;
3. effort, time, price, or access trade-off;
4. provider response and independently observable correction, payment, or
   access restoration;
5. repeat contact or recurrence state;
6. trust judgment or attributed confidence; and
7. switching, non-use, continued use, or exit with a reason.

Non-users and unresolved cases must remain in the denominator. A published
complaint, administrative closure, issued refund, or deletion-completion label
cannot substitute for verified account state.

## Stopping rule

Stop the consumer/account pass when one new lawful source either supplies the
minimum fields above or confirms that the identifier, later account state, or
trust/exit measure is unavailable. Do not repeat the same aggregate search as if
it were progress toward account-level closure. Rotate next to the infrastructure
or geopolitical thin-middle lane only after this gate is logged.

## Source controls

- [Practical-exit observability audit](practical-exit-observability-audit-v1.md)
- [Consumer recourse, power, and exit bridge](consumer-recourse-power-exit-cross-source-bridge-v1.md)
- [Privacy request completion, persistence, and exit bridge](../us-retailer-privacy-control/privacy-request-completion-persistence-exit-bridge-v1.md)
- [AI customer-service context and remedy audit](../cross-domain/ai-customer-service-context-remedy-audit-v1.md)
- [Platform remedy case ledger](../ai-work-control/data/platform-remedy-case-ledger-v1.json)

**Evidence status:** repository-wide candidate audit completed; no account-linked
end-to-end route qualifies under the stated fields.
