# Housing, coverage, and the household constraint cascade v1

**Checked:** 2026-09-16  
**Status:** compared cross-source bridge; not a same-household causal estimate  
**Scope:** US housing/coverage position, utility pressure, care, work, food,
debt, recovery, and institutional response

## The question

When a household has less protection or less room—because coverage changes,
utility payment becomes difficult, housing protection becomes expensive, or a
care need arrives—which need does it protect, which one does it delay or
transfer, and what remains available afterward?

```text
protection or payment pressure
  -> practical room shrinks
  -> care / work / food / housing / debt trade-off
  -> unpaid family or public-program substitution
  -> persistence, recovery, remedy, or exit
```

The sources below measure adjacent arrows on different samples and clocks.

## Evidence ledger

| Arrow | Current evidence | What it supports | What remains open |
|---|---|---|---|
| Coverage position → care choice | SHED 2024–2025 recontact panel; 4,419 paired respondents | Insured-to-uninsured respondents show 13.01% care-foregoing entry and 19.53% persistence; uninsured-to-uninsured respondents show 37.35% persistence. Stable insured respondents show 6.74% entry and 14.53% persistence. | Plan adequacy, dated need or bill, treatment continuity, and coverage causation |
| Dated health event → bounded person-panel context | [MEPS dated episode spine](meps-dated-event-spine-v1.md) | Existing local MEPS event files link first office, ER, and inpatient event months and payments to exact person identity, coverage, health, employment, and bill context; strict inter-round windows preserve baseline selection. | Amount owed, household payer, care choice, adaptation, remedy, and recovery |
| Coverage position → financial adaptation | Same SHED panel | Medical debt, reduced savings, borrowing, delayed purchases, and fair/poor health differ across coverage paths; uninsured-to-uninsured respondents report 22.57% medical debt and 44.77% reduced savings. | Whether coverage change produced the adaptation, and which expense was protected |
| Utility difficulty → next-month work movement | SIPP 2025 public-use file; 2024 reference year; same-person monthly pairs | Utility-difficulty pairs show 81.68% earnings change and 7.71% hours change at the following month; no-difficulty pairs show 84.03% and 5.28%. | Exact bill, shutoff, desired hours, involuntary change, care substitution, and employer response |
| Utility difficulty × tenure → work movement | SIPP tenure-conditioned layer | Hours-change estimates are 7.61% for difficulty/owner and 7.58% for difficulty/renter, versus 4.93% and 5.96% without difficulty. | Tenure mechanism, housing cost, local labor market, and causal work effect |
| Utility difficulty × tenure → childcare/work prevention | SIPP annual fall childcare measure attached to December utility/tenure condition | Childcare arrangements prevented work or more for 9.35% of difficulty/owner records, 8.13% of difficulty/renter records, 2.84% of no-difficulty/owner records, and 5.01% of no-difficulty/renter records. | Monthly care time, dated utility response, household prevalence, and direction of the relationship |
| Utility × tenure × childcare → joint next-month surface | [Unified SIPP same-person cascade screen](sipp-constraint-cascade-screen-v1.md) | 2,600 November-to-December pairs keep work movement, mortgage hardship, food insecurity, and resource-band movement in the same eight-cell utility/tenure/childcare frame. | Dated trigger, desired work, care hours, causal direction, and recovery |
| Housing protection → room | SHED homeowners-insurance module | Among owners, 13.5% report premium affordability difficulty and 19.6% want more coverage but cannot afford it; under-$50k owners report 27.7% premium difficulty and 33.1% unmet coverage preference. | Same owner’s premium, deductible, renewal, repair, mortgage, debt, and move/stay outcome |
| Pressure → food/basic security | SHED food-pressure and USDA food-security layers | Food, saving, borrowing, reduced use, and outside-help routes are observable as distinct adaptations. | Which household event caused which food or housing trade-off, and later recovery |
| Adaptation → persistence/recovery | SHED 2024–2025 persistence panel | Prior borrowing, saving cuts, delayed purchases, reduced use, and extra work often persist into 2025; improving respondents also sometimes end an adaptation. | Dated trigger, remedy, material recovery, and whether the same need remains unmet |
| Household burden → institution → legitimacy/action | CFPB, public-system, ANES/CES/CPS, and institutional layers | Complaint, agency, trust, attribution, and action are separately measurable endpoints. | Same person/episode linkage from household burden through remedy to trust, action, switching, or exit |

## What the comparison says now

### 1. Protection is a condition of choice, not a binary status

“Insured,” “owner,” and “utility paid” each hide different amounts of usable
room. The SHED panel shows that stable coverage can coexist with care foregoing,
debt, and reduced savings. The insurance layer shows that an owner can have a
policy while still reporting affordability or adequacy pressure. The SIPP layer
shows that utility difficulty can sit beside work and childcare movement even
when tenure is held in the comparison.

### 2. The cascade is multidimensional

The same pressure can appear as a care delay, a savings cut, a borrowed dollar,
an extra shift, a prevented work opportunity, food substitution, or unpaid help.
These are not interchangeable measures of “stress.” They identify different
needs being protected and different people or institutions absorbing the cost.

### 3. Housing position changes the menu, but does not explain it by itself

Tenure changes the comparison surface, but the owner/renter split does not
identify rent or mortgage burden, family support, local prices, job type, or
care alternatives. Likewise, insurance coverage does not establish the ability
to remain, repair, sell, or move. Housing is a moderator and institutional
constraint candidate, not a complete mechanism in the current evidence.

### 4. Recovery must be tracked on several clocks

The SHED panel’s broad financial-condition improvement does not guarantee that
borrowing, reduced savings, or delayed purchases end. Conversely, some
improving respondents stop an adaptation. A valid episode therefore needs
health, cash, debt, work, care, housing, and institutional clocks rather than a
single “recovered” flag.

## Counterexamples that prevent overclaiming

- Earnings change is common both with and without utility difficulty; the SIPP
  screen is not a work-loss estimate.
- Coverage gain does not automatically remove care foregoing or adaptation;
  uninsured-to-insured respondents still show substantial 2025 borrowing and
  delayed-purchase shares.
- Stable insurance does not equal adequate insurance, and shopping does not
  equal practical exit power.
- The smallest SIPP childcare cells have wide intervals and an annual fall
  measure cannot be treated as a December consequence.
- Improving financial condition can coexist with persistent adaptation, while
  adaptation can also end without proving that the underlying need was repaired.

## Decisive next test

The next test should be a small, dated episode ledger—not another broad
cross-sectional index. For each person or household, record:

1. the bill, renewal, coverage loss/gain, shutoff threat, care need, or repair
   event and its date;
2. cash obligation, deductible or balance, benefit rule, and feasible
   alternatives;
3. care continuation/delay, utility action, food substitution, borrowing,
   work-hour change, childcare substitution, and unpaid help;
4. insurer, utility, employer, lender, provider, agency, or family response;
5. next-month and later health, work, debt, housing, care, trust, switching,
   and exit outcomes; and
6. a matched counterexample with similar exposure but a different amount of
   liquid room, schedule control, coverage, transport, or family support.

The existing SIPP and SHED files can continue to supply bounded benchmark
surfaces. No new bulk acquisition is required for this design pass. A new
source should be acquired only if it supplies a missing dated episode and its
size, access, retention, and cleanup plan are explicit.

## Source and reproduction routes

- [SHED coverage/care record](../../records/us-shed-panel-coverage-care-foregoing-paths-2024-2025.json)
- [SIPP utility/work record](../../records/us-sipp-utility-work-following-2024.json)
- [SIPP utility/tenure/work record](../../records/us-sipp-utility-work-tenure-following-2024.json)
- [SIPP utility/tenure/childcare record](../../records/us-sipp-utility-tenure-childcare-2024.json)
- [SHED coverage/care audit](../us-health-cost-household-choice/shed-panel-coverage-care-foregoing-reproduction-audit-2026-09-16.md)
- [SIPP utility/work audit](../us-household-calendar-integration/sipp-utility-work-following-reproduction-audit-2026-09-14.json)
- [SIPP tenure/work audit](../us-household-calendar-integration/sipp-utility-work-tenure-reproduction-audit-2026-09-16.json)
- [SIPP tenure/childcare audit](../us-household-calendar-integration/sipp-utility-tenure-childcare-reproduction-audit-2026-09-16.json)

**Evidence status:** compared cross-source bridge with local reproduction
routes; not a same-household episode, causal estimate, or political-outcome
claim.
