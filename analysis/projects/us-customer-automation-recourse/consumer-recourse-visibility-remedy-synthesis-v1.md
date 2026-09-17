# When a customer problem becomes visible: complaint routes, clocks, and the missing remedy

**Status:** reader-facing synthesis of US consumer-recourse evidence · **Checked:** 2026-09-15  
**Scope:** household loss, customer contact, CFPB visibility, automation, company response, remedy, trust, and exit

## The question

When a person loses money, cannot access an account, disputes a debt, or needs
a company to correct a decision, what happens between the problem and a real
remedy?

The visible public sequence is often narrated as if it were complete:

```text
customer problem → complaint → company response → resolution
```

The evidence supports a more limited route:

```text
loss or blocked access
  → customer attempts contact
  → complaint enters a publication and screening system
  → agency routes it to a company
  → administrative timing and response labels become visible
  → [open] correction, money returned, access restored, repeat effort, trust, or exit
```

The current atlas can measure the public institutional middle. It cannot yet
measure the customer's full outcome.

## The short answer

1. **Household loss is much larger than the visible complaint stream.** In the
   2024 SHED estimates, 21% of adults experienced some financial fraud; among
   adults experiencing non-credit-card fraud, 63% lost money, 32% had some
   money not recovered, and roughly 30% spent ten or more hours dealing with
   the incident.
2. **The CFPB complaint system is a real institutional handoff, not a remedy
   rate.** It makes receipt, routing, timing, and published response labels
   visible for selected cases.
3. **Recorded response patterns changed between 2024 and 2025, but their
   meaning is not one consumer-welfare trend.** Published complaints nearly
   doubled, explanations became more common, and monetary-relief labels became
   less common, while product mix, screening, publication, and taxonomy also
   changed.
4. **“Timely” is not the same as elapsed routing time.** In 2025’s capped
   student-loan sample, 59.8% were labelled timely while 21.6% took more than
   24 hours from receipt to company send; the 90th-percentile derived interval
   was about 27 days.
5. **The missing endpoint is the important one.** A company explanation or
   non-monetary-relief label does not prove correction, restored access, money
   returned, reduced repeat effort, trust, switching, or exit.

## 1. The household problem is not the complaint denominator

SHED measures adult-reported fraud exposure, financial loss, non-recovery, and
time spent dealing with the incident. CFPB records measure published complaints
that entered a specific agency system and passed its intake, routing, and
publication processes.

These are not two estimates of the same population rate:

| Layer | Unit | What it measures | What it misses |
|---|---|---|---|
| SHED | US adult respondent | fraud exposure, loss, recovery, and time burden | verified provider response and public route |
| CFPB aggregate | published complaint record | visible record volume, product, response, and publication fields | people who never complained or used another route |
| CFPB event ledger | capped case-level record | receipt, routing, channel, timing, narrative visibility, response label | verified remedy, residual loss, repeat effort, and exit |

A person may lose money without filing a complaint. A customer may contact a
firm directly and never reach the CFPB. Someone may abandon the process because
of time, language, disability, digital access, fear, or expected futility.
Those are not zeros in the complaint database. They are outside its observed
route.

## 2. The visible complaint system changed, but not in one direction

The current CFPB aggregate snapshot reports 2,739,722 published complaint
records received in 2024 and 5,452,107 in 2025. Across those published records,
the recorded response mix moved as follows:

| Recorded endpoint | 2024 | 2025 |
|---|---:|---:|
| Company response marked explanation | 49.014% | 58.706% |
| Non-monetary relief | 50.062% | 40.633% |
| Monetary relief | 0.869% | 0.480% |
| Public narrative present | 29.778% | 22.426% |
| Timely = yes | 99.717% | 99.549% |

These values describe published records and recorded fields. They do not show
that consumer harm doubled, that explanations became more effective, that
relief became less valuable, or that customers lost their voice. The stream is
shaped by complaint behavior, product composition, duplicate and fraud
screening, agency capacity, company coding, publication rules, and the API’s
current data vintage.

Product differences reinforce the warning. In 2025, explanation was recorded
for 84.5% of checking/savings complaints, 66.7% of credit-card complaints,
94.9% of mortgage complaints, 81.6% of student-loan complaints, and 91.0% of
vehicle-loan complaints. The threatened resource differs by product: an
explanation about a deposit account, credit report, mortgage, or student loan
does not carry the same practical consequence.

## 3. The complaint event ledger makes the middle concrete

The project built a de-identified, reproducible 25-case ledger from student-
loan complaints received in 2024. It preserves complaint receipt, coarse
state, submission channel, narrative presence, receipt-to-company-send lag,
timeliness, and company-response labels.

| Field in the 2024 ledger | Observed result | Boundary |
|---|---:|---|
| Records | 25 of 14,685 matching API records | first returned records, not random or weighted |
| Submission channel | 25 Web submissions | not digital-access or attempted-contact rate |
| Timely label | 24 yes, 1 no | administrative label, not correction time |
| Company response | 23 explanations, 2 non-monetary relief | not verified remedy |
| Routing lag | 0.0956–166.4886 hours | CFPB handoff, not company resolution or customer wait |

This is useful even though the sample is small. It holds several fields on the
same case and shows what a lawful episode ledger can contain. It also prevents
the next analyst from treating a response label as a customer outcome.

## 4. There are multiple clocks, and they disagree

The latest API audit separates two fields that sound similar but are not:

- `timely`, an administrative response label; and
- elapsed time from `date_received` to `date_sent_to_company`, a derived CFPB
  handoff interval.

In capped 500-record product samples for 2025, student-loan complaints had a
59.8% timely share, while 21.6% had a derived routing interval longer than 24
hours. The 90th percentile was 649.6 hours. Other products had different
tails, including very large 90th-percentile intervals in credit reporting and
checking/savings.

The safe interpretation is not that one field is correct and the other false.
They measure different administrative concepts. A timely label is not elapsed
time, elapsed time is not company resolution, and company resolution is not a
verified customer remedy.

The API also illustrates a second clock: the data system itself changes. The
live 2024 and 2025 re-queries no longer returned the earlier `has_narrative`
field. That is missingness in the current schema, not evidence that customers
stopped writing narratives. Any trend analysis must record field presence,
definition, date boundaries, raw hashes, and absent fields separately.

## 5. Why automation changes the power question

The project began with customer-service automation because speed is only one
part of control. A tool may answer a simple question quickly while making a
repeated or exceptional problem harder to explain, appeal, or correct.

The relevant questions are:

```text
automated route or decision
  → what information the customer can see
  → whether a person with authority can be reached
  → effort, waiting, and documentation burden
  → correction, denial, or continued dependence
  → trust, switching, complaint, or exit
```

The CFPB data currently make the complaint and agency-to-company handoff
visible. They do not tell us whether the automated or human system changed the
customer’s substantive outcome, whether a worker could override it, or whether
the customer had a real substitute.

## 6. Product safety adds another route from visibility to remedy

The new [CPSC hazard, recall, and remedy layer](../us-marketplace-product-safety/cpsc-hazard-recall-remedy-layer-v1.md)
shows that the same visibility problem exists outside financial complaints.
CPSC reports 333 voluntary recalls involving roughly 41 million product units
in FY2024, 2,969 regulatory-violation notices, more than 56,000 e-commerce
takedown requests, and more than 58,000 products removed from platforms. Its
NEISS system supplies a probability-sample route for product-related injuries
treated in hospital emergency departments.

Those measures occupy different stages:

```text
hazard or injury signal
  → recall, notice, import examination, or platform takedown
  → consumer awareness and decision
  → repair, replacement, refund, disposal, or no action
  → medical, financial, time, trust, and switching consequence
```

The CPSC numbers make institutional action visible, just as CFPB and DFS make
complaint routing visible. They do not establish that a consumer saw a recall,
still possessed the product, could return it, received an adequate remedy, or
avoided injury. A takedown removes a listing, not necessarily an item from a
home or secondary market. A recall is therefore not a remedy rate, and a
remedy is not automatically a recovered household.

This broadens the consumer-power finding. The core problem is not limited to
automated customer service: in financial services, insurance, and product
safety, public systems can make a problem legible before they can make the
person whole. The next same-case ledger should preserve the product/account
identity, notice route, effort, remedy, delay, cost, and later exit across the
relevant domain rather than treating a public intervention as the endpoint.

## 7. Formal redress and distribution are separate stages

Two named CFPB cases sharpen the remedy boundary. In the Cash App case, the
Bureau documented fraud and dispute-process failures, required operational
changes, and ordered at least $75 million—and up to $120 million—in consumer
redress. A current payment-by-case check did not list Block/Cash App as an
active distribution case. That absence does not prove nonpayment; it means the
public distribution status and individual receipt are not established here.

BrightSpeed supplies the contrasting visible distribution stage. The CFPB
identifies 122,507 eligible consumers, $53,885,244 in compensable harm, Epiq
Systems as payment administrator, and distribution ongoing from July 23,
2024. This is stronger evidence of an administrative payment route than a
formal order alone, but it still does not reveal how many checks were issued,
successfully delivered, or sufficient to repair each person's loss.

| Case | Formal response | Public distribution surface | Still unknown |
|---|---|---|---|
| Cash App/Block | Operational correction plus up to $120M redress | Case contact route; no current payment-by-case listing located | Eligibility, payment, receipt, remaining loss, repeat effort, trust, switching, exit |
| BrightSpeed | Enforcement action against payment processing for fraudsters | 122,507 eligible consumers, $53.9M compensable harm, administrator, ongoing distribution | Issuance, delivery, amount received, residual loss, recovery, trust, exit |

The closed American Debt Settlement Solutions case supplies a fourth
distribution state. The CFPB says eligible consumers received compensation,
records two distributions from May 2014 through June 2016, and states that the
matter is closed and check reissue requests are no longer honored. This is
evidence that a distribution can reach a documented closed state, but the page
does not provide a person-level receipt file, payment amount distribution,
remaining loss, or later financial behavior. See the [ADSS payment record](https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/payments-by-case/american-debt-solutions/).

The comparison prevents a common error: reading an enforcement order,
administrator listing, or aggregate harm amount as proof that a particular
consumer recovered. The next public check should capture payment status and
administrator updates over time; the strongest eventual design remains a
privacy-approved individual payment/account follow-up.

## What the current evidence supports

The durable finding is institutional rather than psychological:

> Consumer problems become visible through a selective public route whose
> timing, taxonomy, and response labels can be measured, while the customer's
> actual repair, effort, dependence, trust, and exit remain largely outside the
> public record.

This is not a claim that the CFPB route is ineffective. It is a claim that the
currently visible fields cannot prove effectiveness.

## The next decisive test

Select one essential service—student-loan servicing, credit reporting, deposits,
housing finance, or benefit-card access—and build a lawful same-case or
consented account-level follow-up containing:

1. the original problem, notice, account exposure, and requested outcome;
2. attempted but unsubmitted contacts and channel accessibility;
3. who had authority to change the decision and what alternatives existed;
4. receipt, routing, transfers, elapsed effort, and customer waiting;
5. exact correction, refund, restored access, or denial;
6. repeat effort, residual loss, continued dependence, switching, trust, and
   exit; and
7. a follow-up at one, six, and twelve months.

Keep two counterexamples: a quickly remedied case and a case with a genuine
substitute. Also preserve non-complainants or abandoned cases where lawful;
otherwise the route will overrepresent people who could reach the system.

## Evidence boundaries

The aggregate records are published complaint counts, not consumer-harm rates.
The event ledger is a capped retrieval-order sample, not a population sample.
The response labels are not verified remedies. The API’s timing and field
definitions vary by product and vintage. No same-customer link to SHED, SIPP,
ANES, or political action is claimed.

## Source trail

- [CFPB complaint database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [CFPB complaint API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/)
- [Consumer loss and complaint visibility finding](findings/us-customer-automation-recourse-018.md)
- [Public complaint-ledger finding](findings/us-customer-automation-recourse-019.md)
- [Response-label trend finding](findings/us-customer-automation-recourse-020.md)
- [Timing and schema audit](findings/us-customer-automation-recourse-021.md)
- [CPSC hazard, recall, and remedy record](../../records/us-cpsc-consumer-safety-recalls-import-surveillance-fy2024.json)
- [CPSC consumer-safety finding](../us-marketplace-product-safety/cpsc-hazard-recall-remedy-layer-v1.md)
- [Federal Reserve fraud/recovery source](../../records/us-federal-reserve-household-fraud-recovery-2024.json)
- [Consumer-recourse project](README.md)

**Evidence status:** cross-source household and administrative synthesis. It
supports a measured institutional handoff and a schema/timing warning; verified
remedy, same-customer recovery, trust, switching, exit, and political effects
remain open.
