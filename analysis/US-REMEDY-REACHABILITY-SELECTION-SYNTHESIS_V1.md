# Remedy reachability can select who appears recovered v1

**Checked:** 2026-09-20  
**Status:** bounded cross-domain synthesis; not a recovery rate or causal estimate

## The finding

Across the current consumer, public-benefit, disaster, product-safety, and
worker records, later remedy visibility is often conditioned on an earlier
successful route step:

```text
harm or need
  -> notice, application, complaint, or first payment route
  -> successful reach / acceptance / cashing / contact
  -> later remedy or administrative follow-up
  -> [open] adequate recovery and durable security
```

This creates a selection problem. A second payment, later administrative
follow-up, or visible recipient endpoint may describe people who were already
reachable, not everyone exposed to the original harm. People who missed a
notice, lacked time, could not complete paperwork, could not cash a check, or
did not know how to pursue the route can disappear before the later endpoint.

## Cross-domain evidence

| Surface | What the record makes visible | Selection boundary |
|---|---|---|
| FTC ACRO refunds | 5,685 second-round checks went to people who accepted the first payment | Later payment visibility is conditioned on prior acceptance; second-check receipt, adequacy, and account correction remain open |
| FTC Next-Gen refunds | 104,820 second-round checks went to people who cashed the first check | Cashing is a stronger reachability condition than an offer, but it excludes people who never completed the first route |
| CFPB administered redress | Aggregate funds were cashed, with later reissue and redistribution after unresolved payments | Cashing and reissue totals do not identify who remained unreached, what account was corrected, or whether residual loss ended |
| FTC Amazon Flex refunds | The 2024 report says 2,806 Zelle reissue payments succeeded, participation reached 92.3%, and 130,952 drivers were reported fully compensated | The reported full-compensation endpoint is still aggregate and administrator-defined; driver-level amount, timing, residual loss, and later security remain unknown ([FTC report](https://www.ftc.gov/system/files/ftc_gov/pdf/ftc-refunds-consumers-2024.pdf)) |
| FTC Amazon Prime refunds | Aggregate issued/accepted dollars, expanded automatic eligibility, and possible supplemental payments conditioned on stated acceptance thresholds are visible | Later distribution favors people who clear an earlier route; individual receipt, delay, amount, remaining loss, continued use, switching, trust, and recovery remain unknown |
| CFPB redress-plan design | A Cash App consent order requires a post-plan report identifying consumers/accounts receiving redress and the total amount paid | A reporting requirement makes the intended measurement surface explicit, but the order is not the completed report and does not establish individual receipt, account correction, or recovery |
| SNAP recertification | Respondents report no notice, insufficient time, difficult paperwork, interview barriers, and lost documentation before interruption | A participation or reentry statistic cannot be read as the experience of households who failed at the route boundary |
| FEMA wildfire assistance | Registration, referral, eligibility, and reported assistance stages are visible in an aggregate snapshot | The stages are not a person-level funnel; payment receipt, repair, placement, and survivors who never registered remain unknown |
| Worker remedies | FWO/agency contact and partial payment can make a case visible before a formal order | People without a complaint or institutional contact are not represented in the adjudicated route; final payment and later security remain open |
| Innovative Associates cashback case | A temporary-visa worker reached the Fair Work Ombudsman after being left with no usable wages, and the agency reports full back-pay | The case shows one reachable route, not how many similarly exposed workers could not safely complain or whether the reported payment restored security |
| DOL Workers Owed Wages route | The agency describes locating and notifying workers, holding recovered wages while searching, electronic-payment and claim routes, and eventual Treasury transfer for workers who remain unreachable | The public route does not show whether a particular worker was found, notified, paid, or made more secure; non-claim cannot be assigned to distrust, migration, address change, or any one cause |
| NYC DCWP worker restitution settlements | Named worker groups, restitution amounts, mail/deposit routes, update instructions, scheduled installments, and a proposed unclaimed-restitution fallback are publicly listed for multiple employers | Eligibility and delivery design do not show each worker's receipt, returned or uncashed payment, correct amount, adequacy, later security, trust, or exit; the fallback fund is not yet an implemented disbursement route |
| Product recalls | A repair or repeat remedy can be recorded for a purchaser or product | The public record does not establish safe use, purchaser receipt, or the people who never reached the repair route |

These rows are not pooled. They show a recurring measurement structure, not a
common denominator or a universal institutional failure claim.

## Why this matters for culture and consumer behavior

The latest CFPB records add an important refinement: reachability has at
least two separate layers.

1. **Route reachability:** the person has a usable instruction, contact path,
   application, complaint channel, or payment mechanism.
2. **Outcome reachability:** the person actually receives, cashes, uses, and
   benefits from the remedy.

Cash App currently gives public evidence of route reachability: consumers are
not required to take action at this time, and a contact path is published.
That does not establish outcome reachability. Wells Fargo goes further in a
different direction: the regulator reports formal fulfillment and terminates
the order, but the public record still does not provide borrower-level
receipt, adequacy, or durable recovery. These should not be collapsed into a
single “redressed” variable.

Atkins shows why the distinction matters even when receipt is reported: all
ten drivers were reported paid, but the record still leaves adequacy, later
work, trust, and household security open. Reaching the money stage is
stronger evidence than reaching the information stage, but it is not the
same as reaching recovery.

Reachability changes the meaning of later behavior. A person who receives a
second refund may look like a successfully recovered customer even though the
record says nothing about people who never received the first check. A person
who remains on SNAP may look like continued participation even when the route
was interrupted and household buffers were depleted. A worker who reaches an
agency may appear in the remedy record while a similarly harmed worker who
does not complain is invisible.

The cultural consequence is that “trust,” “satisfaction,” “continued use,” and
“recovery” can be selectively observed among people who remained able to use
the institution. Non-use may mean distrust, exclusion, exhaustion, lack of
information, or a workable alternative; continued use may mean dependence,
not confidence. The atlas must not infer the meaning from the endpoint alone.

The [NYC DCWP restitution reachability ledger](projects/us-customer-automation-recourse/data/nyc-dcwp-restitution-reachability-event-ledger-v1.json)
and [settlement page](https://www.nyc.gov/site/dca/consumers/consumer-complaint-topics.page)
makes the same selection visible before payment:
the city can name eligible worker groups, state restitution amounts, schedule
checks, and provide a mail/deposit update route without exposing which workers
actually received the money or whether it restored lost time and income. A
delivery plan is evidence about institutional reachability, not a worker
recovery rate.

## Required fields for the next episode pass

Every remedy-focused episode should preserve two denominators:

1. everyone exposed or eligible for the route; and
2. everyone who successfully reached each successive step.

The minimum sequence is:

```text
exposed / eligible
  -> notice received
  -> understood and attempted
  -> accepted / filed / cashed / contacted
  -> remedy issued
  -> remedy received
  -> account, work, housing, or safety correction
  -> later security, trust, switching, non-use, or exit
```

Missingness at each step must be reported separately. A later-stage rate must
not use the earlier successful group as though it were the full exposed
population.

## Boundary

The current evidence supports a reachability-selection mechanism and several
concrete route barriers. It does not estimate how large the selection effect
is, prove that any institution intentionally excludes people, or show that
unreached people would have recovered if reached. The next decisive evidence
is a linked claimant, case, or respondent record containing failed attempts,
reissue or correction effort, final receipt, and later outcome.

Related: [remedy implementation and recovery synthesis](US-REMEDY-IMPLEMENTATION-RECOVERY-SYNTHESIS_V1.md),
[strongest end-to-end chains](US-BROAD-STRONGEST-END-TO-END-CHAINS_V1.md),
[remedy-stage coverage audit](data/us-broad-remedy-stage-coverage-audit-2026-09-18.json),
and [consumer repeat-refund recipient gate](projects/us-customer-automation-recourse/ftc-repeat-refund-recipient-gate-synthesis-v1.md).
The new [DOL Workers Owed Wages reachability layer](projects/ai-work-control/dol-workers-owed-wages-reachability-layer-v1.md)
shows that locating, notifying, and maintaining a payment route can remain
part of the remedy after an agency has recovered the wages.
The new [CFPB redress-plan follow-up finding](projects/us-customer-automation-recourse/cfpb-redress-plan-followup-stage-finding-2026-09-19.md)
shows that a formal redress design can explicitly include follow-up for
undeliverable or uncashed payments, while still leaving final receipt and
recovery open.

The same distinction appears in the [CFPB Block/Cash App consent order](https://files.consumerfinance.gov/f/documents/cfpb_block-inc-consent-order_2025-01.pdf):
the order requires a report after the redress plan identifying consumers and
accounts that received redress and the total amount paid. That is a useful
measurement contract, not evidence that the report was completed or that the
underlying fraud/dispute problem was corrected for any named consumer.
