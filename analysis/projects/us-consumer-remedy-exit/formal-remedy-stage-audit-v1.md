# Formal remedy stage audit

Status: fifty-first active depth artifact; checked 2026-10-18.

## Purpose

The consumer-remedy route asks whether a formal refund, correction, or account
control becomes usable relief and then changes continued use, switching, or
exit. Public records contain many administrative milestones, but they use
different denominators and clocks. This audit puts those milestones side by
side without creating a pooled remedy rate.

## What we found

The public funnel is strongest at the point where an institution authorizes or
sends relief, and weakest at recipient-level receipt, adequacy, and later choice.

| Route | Formal stage visible | Next visible stage | What is not observed |
|---|---|---|---|
| FTC 2024 first-distribution table | 4,350,411 consumers sent payments totaling $314,837,561.91 across 33 cases | 2,794,012 had cashed a payment; reported cashing rate 64.2% | Adequacy, full compensation, correction, repeat contact, continued use, switching, or exit |
| FTC 2024 closed programs | 25 programs returned $148,337,472.49; 1,162,743 consumers cashed at least one payment; 65.7% cashing rate; $127.58 average returned per person | Program closure and returned money | Whether the payment repaired the original loss or changed later behavior |
| Amazon Prime redress | $845 million issued by September 2026; revised cap $200 per eligible consumer; automatic check, PayPal, or Venmo route | Expanded eligibility and automatic delivery design | Eligible denominator, successful receipt/cashing, adequacy, subscription correction, continued use, or exit |
| CFPB BrightSpeed | 122,507 eligible consumers; $53,885,244 compensable harm; 122,507 initial checks mailed in FY2024 Q4 | Case page still listed distribution as ongoing in September 2026 | Cashed checks, reissues, retained amount, final receipt, residual loss, or later behavior; public amount labels differ by $549,999.93 |
| FTC Grubhub | More than $23.8 million distributed to 640,038 affected consumers; check and PayPal acceptance windows | Prospective account-contestability, driver-pay, and restaurant-consent controls | Group-specific receipt, control use, restored access/income, alternatives, trust, switching, or exit |
| FTC Walmart Spark Driver | $79 million direct-driver allocation inside a $100 million judgment; ten-year earnings-verification program | Some payments reported made; others still in identification/payment processing | Eligible denominator, sent/received/unresolved counts, corrected earnings, continued work, alternative work, or exit |
| Platform-worker case ledger | 9 records show restoration or access resumption; 3 recognize or order lost earnings; 5 leave lost remuneration or later quantum open | No durable recurrence-prevention observation | 0 records observe worker exit or platform switching; 0 observe durable recurrence prevention |

The key counterexample is that administrative progress does not move on one
scale. A payment can be sent but not cashed; a check can be mailed while a case
remains administratively open; access can resume while lost earnings remain
unresolved; and a prospective control can exist without evidence that anyone
used it. “Distributed,” “received,” “usable,” and “exit-enabled” are separate
states.

## Evidence ledger

| Stage | Strongest current evidence | Boundary |
|---|---|---|
| Exposure/loss | Named FTC, CFPB, and platform cases identify affected populations or conduct | Eligibility and harm definitions differ; they are not one consumer population |
| Contact/complaint | Orders, administrators, FAQs, and public complaint routes are documented | Individual effort, language/access need, and human reach are usually absent |
| Decision/formal remedy | Monetary judgments, allocations, refund rules, account controls, and compliance periods are visible | A formal order does not prove execution or adequacy |
| Sent/mailed/distributed | FTC, CFPB, and platform records report payments, checks, or distribution totals | These are administrative actions, not verified individual receipt |
| Cashed/accepted | FTC reports a 64.2% first-distribution and 65.7% closed-program cashing surface; Grubhub specifies acceptance windows | Cashing is not compensation adequacy, corrected account state, or restored security |
| Access restored | Platform ledger records 9 restoration/access-resumption cases | Restoration may be temporary and does not show payment, control, or recurrence prevention |
| Continued use/switch/exit | Public Reddit, YouTube, X, and LinkedIn discussions provide bounded interpretations | Discussion is not a same-account behavioral outcome; the case ledger observes 0 exits/switches |

## What this connects to

- **Consumer power:** a nominal remedy becomes practical only if the person can
  receive it, understand it, use it, and still choose an alternative.
- **Platform dependence:** restored access may be valuable even when the user
  distrusts the platform, so continued use is not proof of satisfaction.
- **Institutional legitimacy:** unresolved reconciliation gaps and unobserved
  receipt weaken claims about successful redress without proving failure.
- **Worker control:** wage correction and account restoration address different
  harms; neither alone establishes durable bargaining power.
- **Household room:** the value and timing of a payment may matter more than the
  formal judgment total, but household incidence is not in these records.

## Deeper question

**Which administrative transition is the real remedy boundary: money issued,
money cashed, account corrected, loss made whole, or a later ability to choose
another provider or platform?**

The answer matters because each transition can produce a different success
ranking. A program with lower cashing but better account correction may restore
more practical control than a larger nominal distribution. The current public
records cannot test that ranking at the same recipient or account level.

## Bounded public discussion

The existing bounded discussion adds a useful interpretation layer. Public
posts describe refund delay, difficulty reaching a human, escalation through
social channels, locked appeals, and occasional successful account reversals.
They also contain the counter-signal that some users do reach an agent or keep
using the service. These posts support a hypothesis that people judge remedy by
time, human reach, reversibility, and dependence—not a prevalence estimate or
verified outcome.

## Challenge checks

- Sent, mailed, distributed, cashed, accepted, and restored-access states were
  kept separate.
- FTC case and closed-program denominators were not pooled.
- BrightSpeed's $53,885,244 financial-report amount and $53,335,244.07 map
  amount were preserved as a $549,999.93 reconciliation gap, not silently
  harmonized.
- Court judgments and allocations were not treated as recipient receipt.
- Access restoration was not treated as durable work control or exit.
- The zero observed exits in the platform ledger was not converted into a
  zero-exit population rate.
- Public discussion was used for meaning and counterexamples only.

## Next test

Build one recipient/account-level ledger from a program that publishes a
distribution or reissue status. Require a stable case key and retain these
fields:

```text
case/account/recipient key | original loss or control action | contact effort |
decision date | remedy rule and amount | channel | sent/mailed date |
received/cashed/accepted | account correction | residual loss/adequacy |
repeat contact | alternative availability | continued use | switch/non-use/exit |
later trust, earnings, household room, or market response
```

First test whether any public administrator exposes both a delivery status and
a later account or use outcome. If not, record the precise missingness and do
not infer receipt from a program total.

## Stopping rule

Do not call a remedy effective, adequate, trust-repairing, or exit-enabling
from a judgment, allocation, check mailing, distribution total, cashing rate,
case status, or public complaint alone. Close this subtest only when one
identifier-bearing episode links formal remedy to verified receipt, residual
loss or adequacy, and later use, switching, non-use, or exit—or when the source
owner confirms those fields are unavailable.

## Source links

- [FTC refund cashing and reissue funnel](../../records/us-ftc-refund-cashing-reissue-funnel-2024.json)
- [FTC Amazon Prime redress route](../../records/us-ftc-amazon-prime-redress-route-2025-2027.json)
- [FTC Amazon Prime redress expansion](../../records/us-ftc-amazon-prime-redress-expansion-2026.json)
- [CFPB BrightSpeed distribution](../../records/us-cfpb-brightspeed-redress-distribution-2026.json)
- [FTC Grubhub remedy](../../records/us-ftc-grubhub-multisided-remedy-2026.json)
- [FTC Walmart Spark Driver remedy](../../records/us-ftc-walmart-spark-driver-remedy-2026.json)
- [Platform remedy restoration ledger](../../records/us-platform-remedy-restoration-dependence-2024-2026.json)
- [Redress-to-practical-exit bridge](redress-receipt-practical-exit-bridge-v1.md)
