# Finding 004: Disaster policy redistributes recovery, access, and legitimacy—not just liquidity

**Status:** cross-source end-to-end synthesis · **Checked:** 2026-09-17

## The synthesis

The current disaster lane contains six complementary US evidence surfaces,
not one joined causal dataset:

1. **Firm finance:** government recovery loans can reduce firm exit and
   bankruptcy while increasing employment, revenue, and private credit.
2. **Owner household:** linked business/household accounts show a 40% early
   COVID revenue fall with only a 1.6-cent owner-consumption decline per dollar
   lost, with the average muted pass-through persisting through 2021.
3. **Customer access:** Hurricane Harvey closures increased observed shopping
   distance and generated localized modeled welfare losses even where aggregate
   prices showed little durable movement.
4. **Resident judgment:** nearly a year after Harvey, recovery progress coexisted
   with continued disruption, unmet-help reports, and doubts that relief reached
   those most in need.
5. **Survivor-facing public delivery:** GAO's FEMA review records aggregate
   assistance, helpline reachability, eligibility-letter interpretation,
   direct-housing bottlenecks, and a shift toward state/local delivery centers.
6. **Community economic capacity:** GAO's EDA review records federal
   coordination, supplemental funding and delay, project composition, and the
   inability of current measures to validate broad economic outcomes.
7. **Current survivor-facing administrative stages:** The Los Angeles wildfire
   FEMA snapshot records 261,117 valid registrations, 98,459 IHP referrals,
   35,165 IHP-eligible records, and $182.8 million in reported IHP amounts
   across aggregate city/ZIP rows. The ratios advance visibility of the
   registration-to-eligibility middle, but are not a unique-survivor funnel or
   evidence of payment receipt, adequacy, repair, placement, or durable housing.

The [Harvey cross-source event ledger](../data/harvey-firm-customer-resident-event-ledger-v1.json)
formalizes the shared chronology and open arrows without pooling the underlying
firm, customer, modeled-welfare, and resident-survey denominators.

Together these findings support a more disciplined broad claim: public
intervention can change the survival of firms and the availability of local
options, but its social meaning depends on who receives liquidity, who bears
new debt or travel time, whose household buffers absorb the shock, and whether
residents can see and navigate the remedy. Public capacity also has separate
clocks: an appropriation or award can precede a usable project, and aggregate
assistance can coexist with a difficult application interface. “Recovery” is
therefore a distributional process across money, time, access, security, and
legitimacy.

The current disaster-credit effect audit sharpens the firm-side currency. In
the studied SBA approval-threshold design, disaster credit is associated with a
13.2-percentage-point reduction in firm exit, a 0.170-log-point increase in
full-sample employment, and approximately $17,712 more non-SBA private debt.
These are firm-level realized outcomes, not household recovery: the source does
not show worker pay, hours, benefits, schedule control, owner consumption,
customer affordability, or whether the added borrowing improved or prolonged
security.

## Comparative evidence map

| Layer | Best current evidence | Unit and clock | What it closes | What it cannot close |
|---|---|---|---|---|
| Public recovery credit | SBA loan approval thresholds and linked Census/Experian outcomes | Firms; annual, up to 7 years post-disaster | Exit, employment, revenue, private credit, delinquency, bankruptcy directions/effects; current audit reports -13.2 pp exit, +0.170 log employment, and +$17,712 non-SBA private debt in the studied design | Worker pay/quality, owner cash, customer access, payment burden |
| Owner cash pool | Linked small-business and owner-household accounts | Business-household account links; early COVID through 2021 | Revenue-to-owner-consumption pass-through | Disaster-loan causality, reserves, debt, business survival, workers |
| Customer option set | Payment-card store turnover and modeled demand after Harvey | Stores/cardholders/neighborhoods; storm through Dec. 2018 | Closure, distance, entry, relative/modelled welfare, price-path distinction | Cash users, missed trips, income-specific burden, aid receipt |
| Resident recovery judgment | KFF/EHF weighted 24-county survey | Adults/residents; 10–11 months post-Harvey | Disruption, help adequacy, aid applications, fairness confidence, awareness | Verified payment, causal attribution, later civic action, trust change |
| Survivor-facing public delivery | GAO FEMA review and structured delivery ledger | Agency/interface; Helene, Milton, Los Angeles fires, Texas floods | Aggregate support, reachability, notice friction, housing bottlenecks, delivery redesign | Survivor receipt, placement, adequacy, recovery, trust, action |
| Current Los Angeles wildfire administrative stages | OpenFEMA Registration Intake and Individuals Household Programs snapshot for disaster 4856 | Aggregate city/ZIP rows; 2025–2026 snapshot | Registration, IHP referral, eligibility, and reported assistance amount stages | Unique applicants, payment timing/receipt, adequacy, repair/placement, repeat crisis, trust, action |
| Community economic capacity | GAO EDA review and structured recovery ledger | Agency/project portfolio; FY2013–FY2025 coordination and FY2014–FY2024 grants | Coordination, award scale, funding timing, project composition, measurement limits | Disbursement-to-use, completed assets, jobs/wages, household access, local counterfactual |

## The end-to-end chain, with open arrows

```text
natural disaster or eligibility shock
  -> physical damage, revenue loss, or public-support reallocation
  -> loan, subsidy, insurance, public assistance, private credit, savings, or no remedy
  -> contact, eligibility, placement, coordination, and project implementation constraints
  -> firm survival / exit + owner consumption / debt
  -> worker jobs + customer distance, substitution, and prices
  -> household recovery, local service availability, and perceived fairness
  -> [open] verified remedy receipt, attribution, civic action, switching,
         durable place change, and political/state consequence
```

The arrows must remain separate. A loan that keeps a firm alive may protect
jobs and local entry while also creating private debt. A household can maintain
consumption by using savings or aid without restoring the firm. A new entrant
can have higher modeled consumer value than an exiting store while failing to
arrive in the neighborhood that lost access. A majority can say life is nearly
normal while a large minority still cannot navigate aid or trust its
distribution.

## What this changes about the broad goal

The program should treat disaster recovery as a test of five currencies:

- **Money:** loan amount, repayment, transfers, insurance, savings, and
  private credit;
- **Time:** travel distance, delay, navigation effort, and waiting for repair or
  payment;
- **Access:** firm survival, nearby alternatives, service continuity, and
  practical ability to use aid;
- **Security:** jobs, wages, housing, health, food, and household buffers; and
- **Legitimacy:** whether affected people see the remedy, believe it is fair,
  and can act through a public route.

Public capacity is a separate currency within the map: authorization, reach,
interpretability, placement, coordination, project usability, and validated
outcomes must not be collapsed into a single aid or resilience score.

The evidence currently measures each currency in different source families.
It does not justify an overall “resilience” score or a claim that any one
policy is broadly beneficial. The strongest comparative result is instead a
redistribution proposition: policy can move costs and options between firms,
owners, workers, customers, neighborhoods, and public institutions.

## Counterexamples that prevent a simple story

```text
firm survival       != good jobs
owner consumption    != owner security
new entry            != nearby replacement
stable prices        != stable access
aid application      != aid receipt
aid confidence       != civic action
more eligibility     != more access for the smallest firms
```

The size-rule case adds a further institutional counterexample: widening a
support boundary toward larger firms can reduce small-firm revenue, increase
exits, and lower wages and patenting. The disaster-loan case shows that a
different public credit instrument can improve constrained-firm outcomes. The
instrument, eligibility boundary, and outcome currency all matter.

## Next decisive test

The smallest genuinely end-to-end acquisition is a lawful, privacy-preserving
event ledger that aligns:

1. disaster declaration, damage, or firm/household revenue shock;
2. insurance, loan, grant, or private-credit application and decision;
3. amount, timing, repayment, and verified receipt;
4. firm employment and worker pay/quality;
5. customer service availability, distance, price, or missed purchase; and
6. owner/worker household recovery, perceived fairness, and later civic action.

If no common identifier exists, keep the four layers as a cross-source atlas
and do not manufacture a pooled recovery index. A compact table-level artifact
or consented linked panel is preferable to acquiring raw payment-card,
administrative, or household files.

## Sources and storage boundary

- [Disaster-liquidity finding](us-small-business-disaster-liquidity-001.md)
- [Disaster-loan effect-size audit](../effect-size-audit-v1.md)
- [Owner-household finding](../../us-owner-household-business-tradeoff/findings/us-owner-business-revenue-consumption-covid-001.md)
- [Harvey customer-welfare finding](us-harvey-firm-turnover-consumer-welfare-001.md)
- [Harvey recovery-and-legitimacy finding](us-harvey-recovery-aid-legitimacy-001.md)
- [Harvey cross-source event ledger](../data/harvey-firm-customer-resident-event-ledger-v1.json)
- [FEMA delivery layer](../../us-repeat-energy-crises/gao-2026-fema-disaster-assistance-delivery-capacity-layer-v1.md)
- [FEMA structured delivery ledger](../../us-repeat-energy-crises/data/gao-fema-disaster-assistance-delivery-event-ledger-v1.json)
- [Los Angeles wildfire FEMA stage ledger](../../us-repeat-energy-crises/data/fema-la-wildfire-ihp-stage-event-ledger-v1.json)
- [EDA economic-recovery layer](../../us-repeat-energy-crises/gao-2026-eda-disaster-economic-recovery-outcomes-layer-v1.md)
- [EDA structured recovery ledger](../../us-repeat-energy-crises/data/gao-eda-disaster-economic-recovery-event-ledger-v1.json)
- [Small-business size-rule finding](../../us-small-business-support-size-cutoff/findings/us-small-business-support-size-rule-001.md)
- [Project source packet](../source-search-2026-09-11.md)

This synthesis uses committed summaries and source-traceable records. No new
raw data, PDF archive, or restricted file was downloaded or retained.
