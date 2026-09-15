# Care costs are redistributed across money, time, work, and family security

**Status:** provisional cross-source societal finding · **Checked:** 2026-09-14

## The bounded finding

Across three different US evidence layers, care and health costs do not appear
as one household burden with one outcome. They are redistributed across at
least four currencies:

1. **system and household money** — total health expenditure and out-of-pocket
   payment;
2. **coverage and treatment room** — whether payment protection and care access
   move together;
3. **time and work capacity** — whether child-care arrangements prevent work or
   working more; and
4. **family financial adaptation** — reduced use, borrowing, saving cuts, and
   attempts to work more while providing unpaid care.

The strongest safe conclusion is not that one source explains the whole chain.
It is that a care or health-cost analysis that measures only the bill can miss
the way the cost is transferred into unpaid time, work constraint, family
adaptation, or a later loss of household room.

## What the three layers show

| Layer | Unit and period | Measured signal | What it does not measure |
|---|---|---|---|
| MEPS Panel 27 | Same longitudinal persons, 2022→2023 | Mean total health expenditure rose by $630.83 per person in the paired sample while mean out-of-pocket expenditure fell by $50.50; 21.01% reported improved health, 22.85% worsened, and 56.14% unchanged | The specific treatment, price, coverage decision, unpaid-care hours, work response, or political meaning |
| SIPP 2025 release | Person records, 2024 reference months; child-care fields with a same-person SNAP-status bridge | Among stable SNAP cases, 7.43% reported child-care arrangements prevented work or more work versus 3.42% among stable non-SNAP cases; the valid time-loss cells were small and the fall-reference fields are not December outcomes | A dated child-care event, causality from SNAP, provider price, later recovery, or household prevalence |
| Federal Reserve SHED 2024 | US adult respondents | Within each employment position, regular unpaid caregivers reported more reduced use, borrowing, and saving cuts; among full-time workers, caregiver cells were 70.7% reduced use, 24.4% increased borrowing, and 57.4% reduced savings | Care hours, recipient condition, pay/hours, schedule control, leave, household longitudinal change, or the cause of the financial response |

The MEPS result is longitudinal but person-level and health-cost focused. The
SIPP result supplies an explicit work-constraint field but its care variables
refer to a fall reference period rather than the adjacent SNAP month. The SHED
result makes unpaid adult care visible alongside work status and adaptation,
but is cross-sectional. Their different designs are a reason to layer the
evidence, not to pool the percentages or call them one estimate.

## The cross-source mechanism

```text
care or health need
  -> coverage, price, approval, travel, and waiting
  -> paid treatment, delayed care, or unpaid family substitution
  -> work constraint, schedule conflict, reduced use, borrowing, or saving cuts
  -> health, income, family security, dignity, and practical exit room
  -> employer, insurer, provider, public-program, and political response
```

The current evidence supports the middle of this diagram in pieces:

- MEPS shows that total expenditure, out-of-pocket payment, and perceived
  health direction can move differently within repeated persons.
- SIPP shows that child-care arrangements are associated with a reported
  inability to work or work more, with a higher descriptive share in the stable
  SNAP group in this bounded comparison.
- SHED shows that regular unpaid care aligns with more reported financial
  adaptation within each employment group.

The evidence does **not** show that the MEPS expenditure change caused the
SIPP work constraint, that SNAP caused the SIPP care result, or that caregiving
caused the SHED adaptations. These are complementary observations of a social
reproduction problem, not a causal chain joined at the individual level.

## Why the money result cannot be read as relief

MEPS illustrates the central accounting problem. A decrease in paired
out-of-pocket spending can coexist with higher total health expenditure and
with both improved and worsened health. That decrease might reflect coverage,
service mix, timing, lower use, or valid-field selection. It is not by itself
evidence that a household became safer or that care became easier to obtain.

The same caution applies to the other layers. A reported work constraint is
not a wage loss; reduced use is not necessarily reduced need; borrowing is not
proof of a specific medical bill; and employment is not proof of schedule
control or adequate care. The currency being observed must be named before it
is interpreted as welfare, security, or political grievance.

## Distribution and counterexamples

The layers also resist a single class or cultural story. In the SIPP tenure and
poverty comparison, renters showed higher reported child-care work constraint
than owners/buyers within each displayed income band, while paid-care
incidence rose at the highest income band. In SHED, full-time caregivers
reported more borrowing and saving cuts than non-caregivers, but some
non-caregivers also reported severe pressure. In MEPS, baseline poverty cells
did not produce a simple health-direction gradient.

Important counterexamples remain live:

- coverage can lower out-of-pocket payment while treatment or health worsens;
- a caregiver can remain financially stable through paid care, leave, family
  support, or public services;
- a non-caregiver can cut use or borrow because of housing, debt, or another
  health problem;
- a child-care work constraint can reflect schedule design or provider
  availability rather than a lack of willingness to work;
- higher health expenditure can represent valuable treatment rather than
  household harm.

These counterexamples are not footnotes. They determine whether the eventual
interpretation is medical need, institutional protection, time poverty,
employer dependence, family obligation, or political blame.

## Evidence ledger

| Arrow | Current status | Safe wording |
|---|---|---|
| Health need → total spending and payment | Longitudinal descriptive in MEPS | Spending and out-of-pocket payment can diverge within repeated persons |
| Care arrangement → work capacity | Bounded SIPP descriptive comparison | Some reference parents report that care prevented work or more work; the timing and cause remain limited |
| Unpaid care + work position → financial adaptation | SHED descriptive cross-tab | Caregivers report more adaptation within employment groups; no causal estimate |
| Cost/time burden → later health, job mobility, trust, or politics | Open | No current layer follows the same dated event through all these outcomes |

## Next end-to-end test

The next strong design is a dated care or health event followed for twelve
months in the same person or household. It should retain separate fields for:

1. diagnosis, care role, and event date;
2. quoted and final price, coverage, deductible, approval, travel, and waiting;
3. care received, delayed, changed, or refused;
4. paid and unpaid care hours and the family member supplying them;
5. work hours, leave, schedule control, job change, benefits, and lost pay;
6. food, housing, transport, saving, borrowing, collections, and debt; and
7. health, recovery, family time, dignity, trust, institutional contact, and
   political or consumer action.

The comparison should include portable/public versus employer-linked coverage,
high versus low schedule control, and strong versus weak family support. It
must include a stable-care counterexample and a non-caregiver hardship
counterexample. Until such a design is available, this finding remains a
cross-source societal pattern rather than a causal household pathway.

## Sources and reproducibility

- [MEPS Panel 27 health-cost finding](../projects/us-health-cost-household-choice/findings/us-health-cost-household-choice-001.md)
- [MEPS machine-readable record](../records/us-meps-panel27-health-cost-longitudinal-2022-2023.json)
- [SIPP child-care payment, help, and work constraint layer](../projects/us-household-calendar-integration/sipp-care-work-tenure-poverty-layer-v1.md)
- [SIPP SNAP transition and child-care time-loss layer](../projects/us-household-calendar-integration/sipp-snap-childcare-time-loss-layer-v1.md)
- [SHED care and work distribution layer](../projects/us-health-cost-household-choice/shed-care-work-distribution-layer-v1.md)
- [SIPP 2025 public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [Federal Reserve SHED data](https://www.federalreserve.gov/consumerscommunities/shed_data.htm)
- [MEPS HC-252 public-use file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-252)

**Evidence status:** cross-source triangulation with one longitudinal layer and
two descriptive population layers; no pooled estimate, individual-level join,
causal effect, or political endpoint is claimed.
