# US data-center energy load and state-capacity baseline v1

**Checked:** 2026-09-13  
**Geography:** United States  
**Unit:** national data-center electricity use; projected scenario, not a local household estimate  
**Status:** infrastructure-burden baseline; local incidence and state leverage remain open

## Why this pass matters

The AI and infrastructure question is not only whether computing capacity is
built. It is who must supply the power, grid connection, land, water, skills,
public subsidy, and political permission that make the capacity usable—and who
can inspect, price, replace, or refuse it.

```text
AI/data-center investment
  -> electricity, grid connection, cooling, land, labor, and finance demand
  -> utility, public-budget, rate, reliability, and local-development decisions
  -> operating capacity and possible national capability
  -> ownership, cost allocation, public control, and provider replaceability
  -> state bargaining power, household burden, and political conflict
```

This pass measures the national physical demand estimate and the policy
response frame. It does not allocate the burden to particular customers,
counties, utilities, firms, or households.

## Official national estimate

The Lawrence Berkeley National Laboratory **United States Data Center Energy
Usage Report: 2025 Update**, published in June 2026, uses a bottom-up model
based on planned IT-equipment shipments, device electricity use, cooling
performance, facility types, and facility locations.

| Measure | Reported value | Evidence type |
|---|---:|---|
| Reference-case data-center electricity use in 2030 | 649 TWh | Model estimate |
| Reference-case share of total US electricity in 2030 | 11.8% | Model estimate |
| Scenario range for 2030 share | 9.5%–15.3% | Sensitivity scenarios |
| Compounded-uncertainty range for 2030 use | 521–843 TWh | Combined uncertainty scenarios |
| Earlier observed 2023 use | 176 TWh, 4.4% of US electricity | Historical estimate in the 2024 report |

The scenarios are not a promise that the high case will occur. They reflect
different assumptions about equipment shipments, AI-chip lifetimes, idle power,
and server utilization. The model also does not directly forecast how much
grid or on-site generation will be built to meet the load.

## What the baseline adds to the societal map

### 1. Digital capability has a physical price

The national estimate makes electricity a necessary complement to software and
chips. AI capability therefore enters utility planning, transmission, siting,
generation, cooling, and rate design. A technology trend can become a public
infrastructure and household-affordability question before its productivity
benefits are distributed.

### 2. A national load estimate is not a burden estimate

The report does not show who pays for transmission upgrades, how rate classes
change, whether data centers build dedicated supply, or which communities bear
water, land, noise, pollution, or reliability effects. National TWh cannot be
converted into a county household surcharge without utility, regulatory,
geographic, and billing records.

### 3. Policy language reveals the contested allocation

The Department of Energy's 2026 data-center resource hub frames the policy
problem as expanding computing and energy while protecting families and
businesses from undue costs. It describes a proposed/implemented policy frame
in which technology companies should bring or buy new power, pay for required
delivery upgrades, negotiate separate rate structures, invest in local jobs,
and coordinate with grid operators. Those are policy commitments and
administrative claims; this pass does not verify compliance or distributional
results.

### 4. State capacity and private capacity can rise together

The same infrastructure can support national AI capability while increasing
dependence on private equipment, cloud, power, finance, and interconnection
providers. The relevant state-power test is not whether a data center exists;
it is whether public actors can set terms, inspect operations, protect
ratepayers, require local benefit, and replace or discipline a provider.

### 5. Local benefits must be measured against local costs

DOE reports examples of data-center investment producing jobs, labor income,
tax revenue, or local projects. Those are agency-reported benefits, not a
general causal estimate. The next comparison must put jobs, wages, tax receipts,
grid upgrades, energy prices, water, land, and public services in the same
place-year frame.

## Arrow status

| Arrow | Status | Safe conclusion |
|---|---|---|
| AI/data-center growth → electricity demand | Observed/modelled | Historical use and future scenario ranges are documented nationally. |
| Electricity demand → local household or firm burden | Open | National energy estimates do not identify rate, tax, reliability, or service incidence. |
| Infrastructure investment → local capability | Partly reported | Jobs, taxes, and capacity are claimed in official policy materials; durable skills, ownership, and service quality remain unverified. |
| Domestic capacity → state leverage | Open | Leverage requires an observed negotiation, rule, refusal, replacement, or external response. |
| Operating scale → public trust or political action | Open | Requires local exposure, attribution, meaning, and action measures. |

## Counterexample required

The burden-transfer interpretation would weaken where a data-center project
finances incremental power and grid upgrades, uses a separate rate structure,
reduces peak demand, produces durable local skills and tax capacity, and leaves
multiple providers or communities able to refuse or replace the project. A
project that looks large in TWh but has transparent cost allocation and credible
exit is a necessary comparator.

## Next bounded retrieval

For selected US data-center places and utilities, collect:

1. interconnection request, approved load, and actual operating load;
2. utility rate class, upgrade cost, cost-recovery rule, and customer bill;
3. generation mix, water use, cooling system, land, and environmental permits;
4. jobs, wages, local supplier spending, taxes, incentives, and public services;
5. ownership, financing, cloud/customer concentration, contract duration,
   portability, and termination rights; and
6. local hearings, regulator decisions, community action, and any observed
   state or firm change in terms.

Compare a place with dedicated cost allocation and local gains against a place
where new load is socialized across existing customers or where promised
capacity is delayed. Keep projected use, approved capacity, actual use, and
benefit claims as separate variables.

## Official sources

- [LBNL, United States Data Center Energy Usage Report: 2025 Update](https://eta-publications.lbl.gov/publications/united-states-data-center-energy-2025)
- [DOE, Powering America’s AI Future—Data Center Resource Hub](https://www.energy.gov/powering-americas-ai-future-data-center-resource-hub)
- [LBNL, 2024 United States Data Center Energy Usage Report](https://energyanalysis.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report)
