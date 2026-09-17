# Finding 026: Refund programs reveal constrained exit across housing, credit, and small business

**Status:** provisional cross-case consumer-power synthesis · **Checked:** 2026-09-17

## The bounded finding

Three recent Federal Trade Commission refund records show a recurring but
carefully bounded pattern: a firm can make exit costly or risky before a
customer reaches a usable alternative, and a later enforcement process can
make a financial remedy visible without showing that practical choice was
restored.

The cases are different and must not be pooled. Invitation Homes concerns
renter charges and move-out deductions; Credit Karma concerns “pre-approved”
credit marketing, application effort, denial, and possible credit-score
exposure; First American Payment Systems concerns payment-processing fees and
early-termination or “zombie” charges imposed on businesses. Their shared
analytical value is the sequence of distinct remedy clocks:

```text
service or financial dependence
  -> fee, application, data, or contract friction
  -> costly or uncertain alternative / exit
  -> enforcement and refund administration
  -> checks or payments sent
  -> [open] receipt, correction, replacement, trust, and practical exit
```

The evidence supports a cross-case research proposition, not a prevalence
estimate: formal redress can repair part of a monetary loss while leaving the
customer's ability to move, switch, borrow, remain housed, or operate a
business unmeasured.

## Case comparison

| Case | Exposed relationship | Public remedy stage | What remains unobserved |
|---|---|---|---|
| Invitation Homes | Renters faced alleged undisclosed smart-home and utility fees and move-out charges | FTC reports 444,131 checks totaling more than $47.2 million | Check cashing, residual housing loss, repairs, later landlord choice, moving, and secure staying |
| Credit Karma | Applicants received allegedly misleading “pre-approved” offers, spent time applying, and some experienced denial or credit-score exposure | FTC reports more than $2.3 million in first-round refunds and a later Zelle reissue route | Applicant-level time, score correction, payment receipt, alternative credit, later borrowing, and non-use |
| First American Payment Systems | Businesses faced alleged hidden or unauthorized fees, early-termination fees, and “zombie charges” | FTC reports 5,588 checks totaling more than $2.6 million; claims remained under review | Check cashing, residual loss, processor switching, transaction continuity, replacement cost, and business exit |

The denominators, units, and clocks differ. The Invitation Homes figure is a
recipient population and total check amount. The Credit Karma figure is a
reported first-round refund amount plus a later delivery route, not a complete
claimant denominator. The First American figure is a check count while claim
review remains active. None can be converted into an average recovery or a
common remedy rate from the public pages.

## What this adds to the broad atlas

### 1. Exit can be constrained before a formal dispute

The cases make three kinds of practical dependence visible:

- a renter may need cash for a deposit, move, or repair while a landlord
  controls charges at the beginning or end of a lease;
- a borrower may spend time and expose a credit record before learning that a
  marketed offer is not usable; and
- a small business may depend on a payment processor for routine revenue while
  contract terms raise the cost of switching.

In each case, the formal contract or market may offer an alternative in
principle. The public records do not show whether the alternative was
reachable, affordable, timely, or compatible with the customer's needs. This
is why formal exit rights and practical exit must remain separate.

### 2. A refund is not one endpoint

The records support a remedy ladder rather than a single “resolved” status:

```text
allegation or finding
  -> settlement / order
  -> eligible class or claimant route
  -> claim review or payment issuance
  -> delivery and receipt
  -> correction of the underlying account, score, lease, or contract
  -> restored alternative and later choice
```

Invitation Homes supplies a large check-distribution stage. Credit Karma
supplies a payment-channel reissue stage after earlier checks or PayPal
payments. First American supplies both a check distribution and an active
claims-review boundary. These are not interchangeable forms of recovery.

The critical distinction is between **money returned** and **capacity
restored**. A refund may arrive after a renter has already moved, after a
credit application has affected later access, or after a business has absorbed
lost transaction capacity. The public record does not establish that any of
those downstream losses were repaired.

### 3. The same pattern crosses consumer and firm boundaries

The small-business case is not merely a business-finance exception. A payment
processor is an operating infrastructure provider: its fees and switching
terms can affect whether a firm can continue accepting revenue. The renter and
borrower cases show the household counterpart. The common question is not
whether all customers experience the same harm; it is who controls the route,
who bears the time and uncertainty, and whether the affected unit has a usable
substitute.

This connects consumer power to firm and sector power without claiming that
the FTC cases measure market concentration or firm-wide conduct prevalence.

## Evidence boundaries and counterexamples

The cases do not show that every fee was unlawful, that every recipient lost
money, or that every customer lacked an alternative. They also do not show
that a refund failed. The needed counterexamples are explicit:

1. an eligible recipient who cashed a payment promptly and regained usable
   room;
2. a customer who switched providers before or after the dispute without a
   material loss;
3. a customer who received a timely correction but no monetary payment;
4. a renter, borrower, or business that experienced the alleged friction but
   retained a viable substitute; and
5. a claimant who received money but still faced an unresolved lease, credit,
   or transaction-capacity consequence.

The current public records do not identify these counterexamples at the
individual level. Their absence is a measurement boundary, not evidence that
the outcomes did not occur.

## Coding rule for the atlas

```text
alleged fee or marketing practice  != measured individual burden
eligible recipient                  != complete claimant population
checks sent                         != checks cashed
refund received                     != corrected account or contract
corrected account                   != restored alternative
continued use or non-use            != free choice without dependence
```

Code the synthesis as **three non-pooled named remedy cases showing monetary
redress and different implementation clocks, with individual receipt,
underlying correction, alternative access, trust, and practical exit open**.
Do not create a cross-case refund percentage, average recovery, or customer
welfare score.

## Next decisive test

The smallest useful follow-up is a privacy-minimized administrator ledger that
retains, for each case, the following separate states:

```text
eligible -> claim filed -> approved -> payment issued
         -> delivered -> cashed/received -> underlying correction
         -> alternative reached -> later stay, switch, non-use, or exit
```

Join those states, where lawful, to the original charge or application,
effort, amount, timing, account or contract correction, and a later
customer/business outcome. Preserve unknown and unreturned payments rather
than treating them as failed recovery. No bulk customer, renter, credit, or
business transaction file is needed to define this test.

## Sources and storage boundary

- [FTC Invitation Homes Settlement refund page](https://www.ftc.gov/enforcement/refunds/invitation-homes-settlement)
- [FTC Credit Karma Settlement refund page](https://www.ftc.gov/enforcement/refunds/credit-karma-settlement)
- [FTC First American Payment Systems Settlement refund page](https://www.ftc.gov/enforcement/refunds/first-american-payment-systems-settlement)
- [Invitation Homes finding](us-customer-automation-recourse-023.md)
- [Credit Karma finding](us-customer-automation-recourse-024.md)
- [First American finding](us-customer-automation-recourse-025.md)

The synthesis uses already retained official HTML findings and adds no raw
consumer, renter, applicant, or business records.
