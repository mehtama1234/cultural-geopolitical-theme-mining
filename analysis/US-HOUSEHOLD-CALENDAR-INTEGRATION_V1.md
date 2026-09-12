# The household calendar: a twelve-month test of connected pressure

## Why this is the next study

The findings keep returning to the same problem: a household can look stable in one record while losing room in another. Annual income can hide a bad week. A paid utility bill can hide skipped medicine. A working car can hide credit debt. A benefit exit can hide an administrative failure. A vote can show a judgment without showing the bill or choice behind it.

The next study should follow the same household through time. It should not try to prove every connection at once. It should record the dates when money, time, access, and control changed, then test which links actually occurred.

The study is a research design, not evidence that these chains happen to every household.

## Bounded question

When a US household faces a dated cost, work, health, care, housing, transport, service, or policy shock, which need does it protect, which need does it delay, who controls the remedy, and what remains available the following month?

## Scope

- **Place:** United States, with urban, suburban, rural, and manufactured-home households.
- **Period:** twelve months, with a two-year follow-up for a smaller panel.
- **Unit:** the household’s shared budget, time, care, and access—not an income record alone.
- **People:** renters, owners, single-adult households, families with children, caregivers, disabled people, and households with irregular work.
- **Shocks:** a bill or price change, income change, repair, care disruption, benefit decision, service failure, insurance change, or major purchase.
- **Outside scope:** predicting a vote, proving private motive, or claiming a national causal effect from a small panel.

## The chain to test

```text
dated condition or shock
  -> cash, time, access, or control changes
  -> household protects one need and gives up, delays, or borrows for another
  -> firm, lender, landlord, utility, employer, agency, or family responds
  -> next-month room, trust, work, health, housing, or political judgment changes
```

Every arrow receives one of three labels:

- **Observed:** recorded directly or linked to a permitted administrative record.
- **Reported:** stated by the household or another participant but not independently checked.
- **Inferred:** a proposed connection that needs another test.

## The event ledger

For every disruption, record:

| Field | Record |
|---|---|
| Date and warning | When the household knew, and how much notice it had |
| First condition | Bill, pay change, repair, denial, care need, price, rule, or service failure |
| Amount and time | Dollars due, hours needed, deadline, and expected duration |
| Need at risk | Food, medicine, housing, energy, transport, care, work, rest, or communication |
| Choice made | Paid, delayed, borrowed, switched, appealed, used family help, or went without |
| Immediate result | Service kept, work kept, purchase made, care received, or problem continued |
| Person with control | Household, employer, landlord, firm, lender, utility, agency, court, or family helper |
| Remedy path | Repair, refund, aid, appeal, payment plan, replacement, legal help, or no remedy |
| Next-month effect | Debt, fee, missed work, health change, repeat bill, weaker option, or recovery |
| Evidence status | Observed, reported, inferred, unknown, or disputed |

## The monthly household record

Each month should contain the same basic fields so the events can be joined:

- income by date, source, and expected reliability;
- rent or mortgage, utilities, insurance, transport, care, food, medicine, debt, and fees;
- liquid savings, available credit, family help, unpaid care, and unpaid work;
- work hours, commute, schedule changes, missed shifts, and job changes;
- home condition, safe temperature, equipment failure, service status, and repair authority;
- purchases, substitutions, quantity, quality, return, replacement, and disposal;
- applications, notices, denials, appeals, customer contacts, and time spent;
- housing move, renewal, coverage, account, and credit outcomes;
- monthly views of financial security, trust in the relevant institution, blame, and policy preference;
- turnout or vote only if lawfully collected with informed consent, and never treated as the automatic result of a household event.

## Five linked tests

### 1. Timing

Does the date of income, aid, bill, or repair predict what gets delayed? Compare households with similar annual income and different payment calendars.

### 2. Real alternatives

Could the household switch provider, route, job, product, or housing without a larger cost? Record the alternative offered, its price, time, quality, and deadline.

### 3. Control

Who could change the condition? Separate the person paying from the landlord, employer, platform, insurer, utility, or agency that controls the fix.

### 4. Transfer

Did the cost move to a credit account, family helper, worker, customer, public agency, future bill, or waste system? Record the receiver and the new burden.

### 5. Recovery

Did the household regain the lost room within one month, six months, or a year? A service restored or bill paid is not enough if debt, health, missed work, or the next barrier remains.

## Comparison design

The first panel should be large enough to compare household types, not large enough to claim a national effect. Stratify by tenure, income stability, geography, housing type, care need, vehicle dependence, and access to family help. Oversample households likely to be missed by online surveys, including phone-only and limited-internet households.

Use within-household changes first. Then compare similar households with different payment calendars, provider choices, local services, or policy exposure. Keep a serious counterexample in every test: a household with the same shock that recovered without the predicted tradeoff, or a household with the predicted tradeoff but no later institutional or political response.

## What the study can and cannot say

It can show whether a dated shock was followed by a recorded choice, who carried the immediate cost, whether a remedy was available, and whether the next month became harder or safer.

It cannot, by itself, prove that a household’s political view was caused by one bill, that a firm intended a result, or that the panel represents every US household. Political and social links remain conditional unless the study measures the interpretation and action between the material event and the final response.

## Privacy and data rules

Collect only what is needed for the question. Separate contact details from research records. Use consent for bank, health, credit, location, and political data. Do not collect vote choice merely because it is interesting. Let participants correct a record, skip a question, or leave the panel. Report small groups carefully so a detailed timeline cannot identify a household.

## First deliverables

1. A dated household questionnaire and event diary.
2. A codebook with definitions for money, time, access, control, transfer, recovery, and evidence status.
3. A de-identified monthly data table and event table.
4. A claims ledger that points to the household record, source record, or permitted administrative record.
5. A contradiction and missingness report.
6. One Markdown finding and matching HTML page for each tested chain.
7. A public methods note that states what the panel cannot establish.

The initial field definition is in [the versioned JSON schema](../manifests/us-household-calendar-schema-v1.json), and the blank collection form is in [the event-ledger template](templates/US-HOUSEHOLD-CALENDAR-EVENT-LEDGER_V1.md).

The starting claims and their current limits are recorded in [the integration claims ledger](projects/us-household-calendar-integration/claims-ledger-v1.md).

The draft participant instrument is [the household-calendar questionnaire](templates/US-HOUSEHOLD-CALENDAR-QUESTIONNAIRE_V1.md). It uses plain questions for timing, need, choice, control, transfer, recovery, and optional public judgment.

## What would change the working picture

- Most households with a dated shock recover without protecting one need by sacrificing another.
- Payment timing does not predict the first cut after controlling for liquid savings and alternatives.
- Households with the same control and alternatives have different outcomes for reasons not captured by the proposed chains.
- Service restoration reliably restores household room rather than moving cost into debt, family labor, health, or the next bill.
- Material pressure does not alter trust, blame, action, turnout, or policy preference even when those steps are measured.

## Reading rule

Follow the date, the choice, the person with control, the cost transferred, and the next month. Do not turn a connected map into a causal claim until the same household record carries the link.
