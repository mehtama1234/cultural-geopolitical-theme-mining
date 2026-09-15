# Consumer loss and complaint visibility occupy different stages of recourse

**Status:** provisional cross-source consumer-power finding · **Checked:** 2026-09-14

## The bounded finding

The current US evidence separates two parts of the consumer-recourse chain that
are often collapsed:

1. The 2024 Federal Reserve SHED estimates that 21% of adults experienced any
   financial fraud, 63% of adults reporting non-credit-card fraud lost money,
   32% of that conditional group had some money not recovered, and about 30%
   spent ten or more hours dealing with or recovering from the incident.
2. The 2024 CFPB case-route sample shows how selected complaints become
   institutionally visible: web submission ranged from 88.4% to 99.0% across
   four products, while same-day routing ranged from 90.0% to 100.0%. Company
   response labels also differed: mortgage and student-loan samples were
   explanation-heavy, while checking/savings had a larger monetary-relief
   share and credit reporting a larger non-monetary-relief share.

Together these layers establish a measurement asymmetry: household loss and
time burden are not the same denominator as published complaints, and a
complaint route or response label is not verified recovery.

## What the sources measure

| Layer | Unit | Direct contribution | Boundary |
|---|---|---|---|
| Federal Reserve SHED | Weighted adult respondent; conditional fraud paths | Exposure, direct loss, non-recovery, and time burden | Self-report; no verified provider response, complaint, or exit |
| SHED subgroup extraction | 12,295 public-use adult rows; conditional subgroup cells | Income, age, and payment-route differences | No replicate variance fields; selected P2P/account cells |
| CFPB case-route sample | 500 capped published records per selected product | Routing time, channel, narrative visibility, public response, and labels | Retrieval-order sample; no population complaint rate, account denominator, or remedy verification |

The layers should not be pooled. The SHED fraud denominator includes people who
may never contact a firm or regulator; CFPB records include people who entered a
visible complaint system and survived the agency's publication/routing process.
The gap between them is itself an acquisition target, not a missing percentage
that can be inferred.

## Mechanism under test

```text
fraud or account problem
  -> loss, recovery time, and practical burden
  -> access to a complaint or correction route
  -> firm/agency response and verified remedy
  -> repeat effort, switching, continued dependence, trust, or exit
```

The current evidence reaches the first stage and parts of the second and
third. It does not follow the same customer from loss through remedy and later
choice.

## Counterexamples and safeguards

- A household can suffer loss without filing a complaint; complaint counts do
  not estimate fraud incidence or the probability of recovery.
- A fast CFPB routing time is administrative handoff, not company resolution
  time or money returned.
- An explanation, monetary-relief, or non-monetary-relief label is not an
  independently verified outcome.
- P2P cases show higher descriptive non-recovery and time burden than selected
  non-P2P cases, but the comparison does not establish payment-route causation.
- Older adults show higher published fraud exposure/loss measures in some SHED
  comparisons, but that does not by itself establish weaker digital ability,
  higher vulnerability, or lower recovery capacity.
- Continued use after an unresolved problem may indicate necessity or lack of
  alternatives rather than trust or satisfaction.

## Next end-to-end test

Select one essential financial service and build a lawful same-case or linked
panel from first contact through 12 months. Preserve attempted but unsubmitted
contacts, non-complainants where possible, account alternatives, effort,
transfers, response authority, verified correction/payment/restored access,
repeat contact, switching, non-use, trust, attribution, and essential-service
consequences. The comparison must retain a quickly remedied case and a case
with a real substitute as counterexamples.

## Reproduction and sources

- [Federal Reserve household fraud/recovery record](../../../records/us-federal-reserve-household-fraud-recovery-2024.json)
- [SHED subgroup record](../../../records/us-shed-fraud-recovery-subgroups-2024.json)
- [CFPB case-route record](../../../records/us-cfpb-case-route-sample-2024.json)
- [Consumer recourse cross-source bridge](../consumer-recourse-power-exit-cross-source-bridge-v1.md)
- [Federal Reserve 2024 household economic well-being](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm)
- [CFPB consumer complaint data](https://www.consumerfinance.gov/data-research/consumer-complaints/)

**Evidence status:** cross-source descriptive synthesis with distinct survey and
administrative denominators; no same-customer remedy, trust, switching, or
political-action estimate is claimed.
