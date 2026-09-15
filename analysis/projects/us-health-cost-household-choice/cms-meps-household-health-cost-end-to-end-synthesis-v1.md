# From national health spending to household room: what CMS and MEPS can—and cannot—join

**Checked:** 2026-09-15  
**Sources:** [CMS National Health Expenditure Accounts](https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/historical), [CMS NHE fact sheet](https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/nhe-fact-sheet), [AHRQ MEPS Panel 27 public-use file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-252), the [2024 HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes), and the 2024 [office-visit](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254G&prfricon=yes), [prescribed-medicine](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254A&prfricon=yes), [emergency-room](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254E&prfricon=yes), and [inpatient-stay](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254D&prfricon=yes) event files. See also the atlas’s [CMS system-layer record](../../records/us-cms-national-health-expenditure-2024.json), [MEPS longitudinal record](../../records/us-meps-panel27-health-cost-longitudinal-2022-2023.json), and [MEPS expenditure-conditioned record](../../records/us-meps-panel27-baseline-expenditure-outcomes-2022-2023.json).

## The end-to-end finding

CMS and MEPS answer different questions that become more useful when read together.

CMS shows the scale and architecture of the US health economy: approximately **$5.3 trillion** in national health expenditure in 2024, **$15,474 per person**, and **18.0% of GDP**. It also separates private insurance, Medicare, Medicaid, out-of-pocket spending, and sponsor categories.

MEPS moves closer to the person. In the Panel 27 longitudinal analysis retained in this atlas, weighted mean total health expenditure was approximately **$6,972 per person in 2022** and **$7,329 in 2023**; mean out-of-pocket expenditure was approximately **$961** and **$971**, respectively. The paired descriptive analysis also reports changes in perceived health, employment status, wage income, visits, prescriptions, and out-of-pocket spending.

Together, these sources establish a measurement ladder:

```text
CMS national account
  -> payer and sponsor architecture
  -> MEPS person-level expenditure and coverage
  -> health, work, income, and utilization transitions
  -> household care delay, debt, unpaid time, trust, or political response
```

The first three stages are now documented. The final stage is not closed. Neither CMS nor the current MEPS extracts identifies the full same-event chain from a particular bill or coverage rule to a care decision, household substitution, institutional remedy, and political judgment.

## What each source contributes

| Layer | CMS NHEA | MEPS Panel 27 | Safe interpretation |
|---|---|---|---|
| Scale | $5.3T and 18.0% of GDP in 2024 | Not designed as a national-spending account | CMS describes system weight; it is not a typical household |
| Payment route | Private insurance, Medicare, Medicaid, out of pocket, sponsor shares | Person-level total and out-of-pocket expenditure | Payment channels can be compared conceptually, not assumed identical in denominator or scope |
| Time | Annual national account and projections | 2022 and 2023 annual fields plus five-round longitudinal participation | Both have annual clocks; neither alone dates a bill-to-choice episode |
| Outcomes | Services and spending categories | Perceived health, employment, wage income, visits, prescriptions, coverage | MEPS can show co-movement and conditioning; descriptive estimates are not causal explanations |
| Distribution | Aggregate sponsors and payers | Person-level subgroup and expenditure-conditioned differences | Subgroups reveal unequal exposure, but composition and need remain important alternatives |
| Meaning and power | No direct political or cultural judgment measure | No direct trust, political action, provider negotiation, or firm remedy in the current extract | A further survey/event linkage is required |

## The MEPS signal is material, but not a causal story

The Panel 27 results show why a household layer matters. Mean total expenditure rose between the two annual fields, while the estimated out-of-pocket change in the all-person paired comparison was negative and its 95% interval crossed zero. In the same paired universe, about 22.8% were classified as having worsened perceived health, about 21.0% as improved, and about 56.1% as unchanged. These categories do not mean that spending caused health change, or that out-of-pocket spending protected anyone.

The expenditure-conditioned pass adds another boundary. Baseline expenditure bands differ in later health, work, income, utilization, and payment patterns, but baseline expenditure is partly a measure of health need, age, insurance, prices, and service use. A high-expenditure person is not necessarily financially worse off; a low-expenditure person is not necessarily well. Low spending can reflect good health, coverage, inability to reach care, foregone care, or an unobserved household buffer.

The proper claim is therefore modest: **health spending and payment are observable material conditions that can be placed beside later health and work measures, but they do not identify the private decision or institutional event that connects them.**

## What the 2024 event files add

The new 2024 event files move the analysis from annual person-level payment to four observed care channels. They do not replace the person-level file: each event file represents people who recorded that type of event, while people with no such event are absent from that file.

| Observed channel | Event volume | Direct payment observed at the event | What it adds |
|---|---:|---:|---|
| Office-based provider visits | 2.410 billion visits | $57.38 self/family payment per visit | Routine care, services, provider type, telehealth, and visit-level payment |
| Prescribed medicines | 3.029 billion purchases | $16.95 self/family payment per purchase | Pharmacy purchases, medicine characteristics, and payment channel |
| Emergency-room visits | 68.2 million visits | $148.22 self/family payment per visit | Acute-care intensity and facility/doctor payment components |
| Hospital inpatient stays | 28.4 million stays | $865.20 self/family payment per stay | High-intensity care, nights, and hospitalization payment |

The event scales are not additive household costs. A person can appear in multiple channels, events can be bundled, payment fields are imputed/edited, and the event file does not show people who delayed or never obtained care. Their value is diagnostic: the direct-payment channel changes with the type and intensity of observed care.

The under-65 coverage comparisons reinforce that point. Public-only coverage has lower observed self/family payment than private coverage across office visits, medicine purchases, emergency visits, and inpatient stays. Uninsured observed events have higher direct payment in office, medicine, and emergency settings, but the uninsured inpatient cell is too sparse for a headline estimate. These are coverage-conditioned event patterns, not coverage effects: age, severity, medication mix, provider type, utilization, eligibility, and selection remain entangled.

The event sequence therefore sharpens the program’s missing middle:

```text
annual person exposure
  -> observed care channel and payment
  -> repeated or acute episode
  -> delayed/foregone care, debt, unpaid time, or work disruption
  -> recovery, trust, switching, remedy, or action
```

The first two arrows now have bounded evidence for 2024. The remaining arrows still require same-person or same-household fields for non-use, need, alternatives, time, work, debt, and recovery.

## Payment is not yet the household choice

The new [MEPS event-payment and bill-context layer](meps-2024-event-payment-bill-context-v1.md)
tests the most tempting shortcut in the chain: treating an observed event's
self/family payment as the household's medical burden. It links office, ER,
inpatient, and prescription event payments to the person's annual
`PROBPY42` medical-bill-problem report, then conditions the comparison on
under-65 coverage and annual poverty category.

The result is a useful negative finding. The national event comparison is not
monotonic: bill-problem reporters have lower observed self/family payment for
office visits and prescription purchases, but higher payment for inpatient
stays. Within coverage and resource groups, the signs change again. Private
office and prescription event payments are lower among bill-problem reporters,
while public-only office payments are higher; uninsured acute-event cells are
too small for headline interpretation. The point is not that payment is
irrelevant. It is that payment alone cannot identify affordability, debt,
forgone care, prior balances, or which household member absorbed the cost.

That result changes the required end-to-end design:

```text
observed service and payment
  + coverage, deductible, annual resources, and prior balance
  -> event-specific bill and feasible alternatives
  -> care continued, delayed, substituted, or forgone
  -> money, time, work, unpaid care, food, housing, or debt trade-off
  -> recovery, remedy, switching, trust, or action
```

MEPS currently measures the first line and parts of the context. The [SHED
adaptation-by-health-direction layer](../us-household-financial-pressure/shed-panel-adaptation-health-path-layer-v1.md)
shows in a separate same-respondent panel that improved health does not
automatically reverse borrowing or delayed purchases. Together, these layers
rule out two shortcuts: observed payment is not the same as burden, and
health improvement is not the same as financial recovery. Neither layer yet
observes the same household's bill, choice, time substitution, remedy, and
later judgment.

## Why the aggregate-to-household bridge matters

The CMS total can rise while household experience diverges in several directions:

- an insured household may see higher premiums but fewer point-of-service payments;
- a patient may have low recorded expenditure because care was delayed or never reached;
- a household may pay more while preserving care by reducing savings or borrowing;
- a caregiver may experience the main cost as unpaid time and work disruption;
- public or employer sponsorship may lower direct payment while leaving access, travel, paperwork, or waiting burdens;
- a high national service total may coexist with local shortage, denial, or provider-switching constraints.

This is why the atlas keeps CMS, MEPS, SHED, SIPP, ATUS, medical-debt studies, and administrative recourse records as adjacent layers rather than collapsing them into “health-care burden.” Each observes a different currency: national resources, person-level payment, household adaptation, time, debt, or institutional response.

## The household-room bridge: what may happen after the payment

The event files make the payment channel more concrete, but they do not observe
what the household did with the remaining room. The atlas therefore places the
MEPS event layer beside the existing SIPP and Federal Reserve evidence without
pretending that the records are joinable.

| Possible pressure point | Adjacent evidence | What a reader may infer safely | What is still unobserved |
|---|---|---|---|
| A routine or acute health payment arrives | MEPS office, medicine, ER, and inpatient event files | Direct payment differs by care channel and observed coverage group | Whether this exact event was delayed, borrowed for, appealed, or paid by another household member |
| The household has limited alternatives | SIPP resource/tenure comparisons and SHED emergency-liquidity responses | Resources, tenure, cash capacity, and credit exposure shape the menu of possible responses | Which alternative was actually available, chosen, or affordable for the same event |
| Care competes with work or unpaid time | SIPP monthly work/resource transitions and ATUS care/time measures | A household can preserve one outcome while moving pressure into hours, earnings, caregiving, travel, or rest | A dated bill-to-time-loss path for the same person or household |
| The episode persists or resolves | MEPS annual health/work measures and SIPP monthly transitions | Health, resources, and work can move on different clocks | Recovery, repeated borrowing, provider switching, insurer remedy, trust, or political action after the episode |

The resulting interpretation is deliberately conditional:

```text
observed care event and payment
  + household resources, tenure, liquidity, and schedule constraints
  -> a feasible response set
  -> payment, borrowing, assistance, extra work, unpaid care, delay, or going without
  -> a protected outcome and a displaced cost
  -> recovery, persistence, remedy, switching, trust, or action
```

Only the first line is measured in the same 2024 MEPS event architecture. The
next lines are supported by adjacent source families with different samples,
periods, units, and recall windows. This is still useful: it tells the reader
what the event payment could be placed beside, while preventing a common error
in which a hypothetical emergency-fund response, a monthly work transition,
or a time-diary activity is reported as the consequence of a particular medical
bill.

The household-room synthesis also supplies the key counterexample. A lower
direct payment can coexist with worse access or more unpaid time; borrowing can
protect medicine or housing today while reducing future room; stable job count
can coexist with changing monthly resources; and reduced work can be either
harm, accommodation, or caregiving. “Adaptation” therefore needs a specified
protected outcome and time horizon before it can be called resilience.

For the reader, the practical rule is: **treat MEPS as evidence about observed
care and payment, SIPP/SHED/ATUS as evidence about possible household room and
substitution, and a same-household episode as the still-open test that would
connect them.** See the atlas’s [multi-clock household synthesis](../us-household-calendar-integration/findings/us-household-calendar-integration-033.md)
and [layered household-room finding](../us-household-calendar-integration/findings/us-household-calendar-integration-032.md)
for the source-specific denominators and limitations.

## What the current evidence does not prove

- CMS’s 18.0% GDP share does not estimate household affordability or clinical value.
- CMS’s household sponsor share does not identify which household paid, delayed, borrowed, or went without care.
- MEPS mean expenditure does not describe the median person, a particular family, or a single medical bill.
- MEPS expenditure-conditioned differences do not show that spending caused later health, employment, income, or utilization outcomes.
- A decline in observed out-of-pocket spending does not establish improved access; it can coexist with coverage changes, service mix, or foregone care.
- Neither source by itself shows trust, political action, provider accountability, insurer remedy, or geopolitical consequence.

## The next end-to-end acquisition

The next strong test is an event-oriented linkage within the available public survey architecture. The reusable [health-cost event ledger](../../templates/US-HEALTH-COST-EVENT-LEDGER_V1.md) defines the fields and promotion rules before any new join is attempted:

1. identify a dated health need, service use, coverage change, bill, or payment problem;
2. retain the person and household expenditure, insurance, income, work, and health fields for the same observation window;
3. identify care delayed, changed, or foregone and the reason reported;
4. add time, unpaid-care, debt, credit, or work-loss measures where the source supports them;
5. separately inspect provider, insurer, regulator, complaint, or policy response;
6. compare whether the route ended in care, substitution, debt, recovery, switching, trust loss, or political action.

The decisive improvement is not another national total. It is a same-household episode with a preserved date, denominator, reason, and outcome. Until that exists, the atlas should describe the evidence as a set of connected scales—not as one completed causal chain.

## Reading rule

When health spending rises, ask four separate questions: did the system spend more, did this person pay more, did this household give something up, and did anyone make the route easier afterward?
