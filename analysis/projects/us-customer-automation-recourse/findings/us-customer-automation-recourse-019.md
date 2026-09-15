# A public complaint ledger observes institutional handoff, not consumer remedy

**Status:** reproducible CFPB administrative route finding · **Checked:** 2026-09-14

## The bounded finding

The CFPB public complaint API can support a small, de-identified event ledger
for the institutional middle of a consumer-recourse episode. In a fixed
retrieval-order sample of 25 student-loan complaints received during 2024, the
ledger preserves receipt date, coarse state, routing to the company,
receipt-to-send lag, submission channel, narrative presence, timeliness, and
published company-response labels.

It does not observe whether the company corrected the account, returned money,
restored access, prevented a missed payment, reduced repeat effort, or changed
the customer's trust or provider choice. The finding is therefore about what
the public administrative system makes visible—not about the probability of
consumer harm or successful remedy.

## What the 25-case ledger contains

| Field | Observed result | Unit / denominator | Boundary |
|---|---:|---|---|
| Complaint receipt | 25 records | Capped retrieval-order sample filtered to `product=Student loan`, received in 2024 | Not random, not weighted, and not a complaint-incidence rate |
| Submission channel | 25 Web submissions | 25 published cases | Does not measure digital access or attempted-but-unsubmitted contacts |
| Timeliness label | 24 `Yes`, 1 `No` | 25 published cases | Administrative coding; not elapsed time to correction or payment |
| Company response | 23 `Closed with explanation`, 2 `Closed with non-monetary relief` | 25 published cases | A published label is not verified remedy or customer satisfaction |
| Narrative presence | Varies across cases | 25 published cases | Presence is not narrative meaning, attribution, or severity |
| Routing lag | Derived from receipt and date-sent timestamps | Case-level hours where both timestamps are present | Routing to the company is not company resolution time |

The raw API response contained 14,685 matching student-loan records according to
the endpoint metadata, but only the first 25 returned records were extracted.
That distinction is central: the 25-case ledger is a reproducibility and field
contract test, not a sample from which population shares should be inferred.

## Case-level variation inside the ledger

The derived receipt-to-company-send lag ranges from **0.0956 to 166.4886
hours**. The median is **0.3711 hours** and the 90th-percentile order statistic
is **0.9972 hours**. One case therefore creates a long routing tail even though
most selected records were sent in under an hour. The lag is a routing measure,
not a resolution or remedy measure.

The 14 records with a narrative have a median routing lag of 0.337 hours
(range 0.0956–23.718 hours); the 11 without a narrative have a median of 0.397
hours (range 0.136–166.4886 hours). The two `Closed with non-monetary relief`
records have a median lag of 0.163 hours, compared with 0.397 hours among the
23 `Closed with explanation` records. These tiny, retrieval-order groups are
descriptive contrasts only: they cannot support a claim that narrative
presence, routing speed, or response label caused a different customer outcome.

The one `timely=No` case has a routing lag of 0.491 hours, illustrating why the
timeliness field must not be substituted for the derived routing timestamp.
The two fields describe different administrative endpoints or coding rules;
the extract does not identify which one corresponds to customer delay.

## The measured episode segment

```text
customer problem or loss
  -> complaint becomes visible in the CFPB system
  -> CFPB sends the case to the company
  -> company-response and timeliness labels are published
  -> verified correction, recovery, repeat effort, trust, switching, or exit
```

The first three arrows can be represented with a stable, de-identified case
key inside this extract. The final arrow is absent from the public record. The
ledger therefore improves the program's episode design by making the handoff
stage concrete while preserving the missing outcome stage.

## Why this adds something beyond aggregate complaint trends

Annual CFPB aggregates can show changes in complaint volume, response labels,
product mix, publication, or timing fields. The event ledger adds a common
case-level sequence: receipt and routing are held on the same record, and
derived lag can be compared with narrative and response fields. That makes it
possible to specify a lawful follow-up design rather than asking an aggregate
response label to stand in for remedy.

The ledger also exposes the route's selection boundary. A customer must decide
to submit, find a channel, survive intake and publication rules, and appear in
the returned API extract. Customers who did not complain, complained by a
different route, abandoned the process, or received an unrecorded correction
are not represented as zeros.

## Counterexamples and safeguards

- A case marked `Closed with explanation` may have been fully resolved, partly
  resolved, or unresolved; the label alone cannot distinguish those outcomes.
- A same-day send may indicate efficient routing, but it does not show that the
  company had authority, information, or willingness to correct the problem.
- A non-monetary-relief label is not a dollar recovery and may or may not match
  the customer's requested remedy.
- A missing narrative is not evidence that the case lacked harm or meaning.
- Web-only submission in this capped extract is a property of the retrieved
  records, not evidence that all affected borrowers can use the Web.
- A coarse state field is place context, not a measure of servicing location,
  borrower residence quality, or local institutional performance.

## Next same-case test

Extend one essential financial-service route into a lawful consented follow-up
or verified administrative linkage. Retain:

1. attempted but unsubmitted contacts and prior efforts;
2. account status, notice, payment interruption, and the customer's requested
   outcome;
3. who had authority to change the decision and what alternatives existed;
4. exact correction, refund, restored access, or other verified remedy;
5. repeat contact, elapsed effort, switching, continued dependence, trust,
   attribution, and exit at a defined follow-up; and
6. a quickly remedied case and a case with a genuine substitute as
   counterexamples.

The public ledger is a route-stage baseline for that design. It should not be
expanded by repeatedly downloading larger capped samples unless the new sample
adds a defensible comparison, a stable product/time frame, or an outcome field.

## Reproduction and sources

- [CFPB public event-ledger acquisition audit](../cfpb-public-event-ledger-acquisition-audit-2026-09-14.md)
- [Committed de-identified 25-case ledger](../data/cfpb-student-loan-event-ledger-2024-25.json)
- [Ledger builder](../../../../scripts/build_cfpb_event_ledger_sample.py)
- [Broad event-ledger validator](../../../../scripts/validate_us_broad_event_ledger.py)
- [CFPB case-route record](../../../records/us-cfpb-case-route-sample-2024.json)
- [Consumer loss and complaint visibility finding](us-customer-automation-recourse-018.md)
- [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB public complaint API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/)

**Evidence status:** observed administrative route fields in a reproducible,
capped 25-case extract. No population route rate, verified remedy, household
recovery, trust, switching, exit, or political-action estimate is claimed.
