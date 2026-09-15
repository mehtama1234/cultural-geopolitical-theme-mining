# Finding 056: Food security depends on route quality, material adequacy, and layered buffers that are not interchangeable

**Status:** provisional non-pooled public-system/food-security bridge · **Checked:** 2026-09-14

## The bounded finding

The public-systems lane now combines four distinct evidence surfaces:

1. USDA/FNA state aggregates measure application and recertification timeliness alongside participation.
2. Urban WBNS measures food insecurity and subgroup exposure in 2025.
3. Urban WBNS measures charitable-food reach, access difficulty, perceived treatment, and unmet need.
4. SIPP follows adjacent SNAP receipt states into following-month rent and utility hardship.

The defensible synthesis is: **formal route performance, receipt, food security, charitable-food access, and household hardship are separate endpoints. A public or private safety-net route can change participation without proving adequate food or housing security, and high receipt can coexist with unmet need.**

## Evidence surfaces kept separate

| Stage | Direct evidence | Unit | What remains open |
|---|---|---|---|
| Formal route | Across 51 states/DC, application timeliness ranges 61.24–97.22% and recertification timeliness 25.23–99.87%; participation correlations are only 0.033 and 0.211. | State aggregates | Household notice, effort, benefit amount, gap days, and remedy |
| Food security | WBNS food insecurity is 27.7% among working-age adults in December 2025, 32.0% with children, 51.0% below 200% FPL, and 52.1% among adults with disabilities. | Respondent-reported household food-security estimates | SNAP receipt, adequacy, causal policy attribution, and same-person route |
| Layered buffer | 39.5% of food-insecure adults reported charitable-food participation, but 28.8% reported unmet charitable-food need; 51.6% of participants reported an access difficulty. | Cross-sectional adult and participant universes | Provider capacity, quantity/adequacy, stigma causality, and later security |
| Following hardship | SIPP following-month rent hardship is 16.40% after no→yes SNAP, 11.53% after yes→no, and 11.98% after yes→yes; utility hardship is 20.80%, 20.83%, and 18.61%. | Fay-BRR weighted person-month transitions | Same-episode notice, amount, food outcome, appeal, trust, and recovery |

These objects are intentionally not pooled. A state route rate, WBNS respondent share, charitable-food access item, and SIPP transition do not share a denominator or a complete household episode.

## The safety-net chain under test

```text
need, eligibility, income, work, care, and health conditions
  -> application, notice, recertification, interview, and benefit route
  -> receipt, interruption, exit, charitable substitution, or unmet need
  -> food, housing, utility, work, health, and time security
  -> fairness, dignity, trust, appeal, organizing, or political action
```

The evidence reaches route quality, food insecurity, mixed-safety-net access, and following hardship. It does not close same-episode adequacy, interpretation, remedy, recovery, or political response.

## What the comparison changes

### Participation is not route quality

The near-zero participation/application-timeliness relationship and small participation/recertification relationship show why a large program can have poor handling in some places and strong handling in others. Participation is a population stock or flow; timeliness is a case-processing measure. Neither is household security.

### Food insecurity is not proof of one program failure

The 2025 WBNS level and subgroup differences identify material exposure, not the responsible program or policy. Prices, wages, household composition, disability, health, housing, debt, work, and multiple supports can produce the same endpoint.

### A buffer can be both used and inadequate

Charitable-food participation among food-insecure adults and unmet need coexist. Access barriers—closed hours, awareness, comfort, variety, transport, safety, and prior treatment—show that “available” is not the same as usable. Perceived unfair treatment is an important meaning/route measure, but it is not an adjudicated discrimination or generalized trust result.

### Receipt and hardship can coexist in the same transition architecture

SIPP prevents the shortcut that exit equals recovery: rent and utility hardship remain after yes→no transitions. It also prevents the shortcut that continued receipt equals security: hardship remains in yes→yes pairs. Entry is a pressure marker and is not a program effect.

## Counterexamples kept visible

- High SNAP participation can coexist with poor timeliness or route burden.
- A household can receive SNAP and charitable food while still reporting food insecurity or unmet need.
- A person can face food insecurity without using either formal or charitable assistance.
- SNAP exit can precede continued housing or utility hardship, while continued receipt can coexist with hardship.
- Access difficulty can reflect hours, transport, awareness, comfort, variety, safety, or treatment rather than one stigma mechanism.
- A route intervention can raise participation without proving higher benefit adequacy or food security.
- A food-insecurity trend can move with prices, wages, supports, or sample composition without identifying one policy cause.

## Next decisive test

Build a linked or matched episode design containing:

1. eligibility, notice, channel, documentation, interview, and route effort;
2. decision, amount, issuance date, gap days, correction, appeal, and reentry;
3. food quantity/security, rent, utility, health, work, care, and time outcomes;
4. formal and charitable alternatives, transport, hours, stigma, treatment, and dignity;
5. attribution, trust, fairness, organizing, complaint, vote, or exit; and
6. a similar exposed household or place with a different route or buffer.

Do not promote this bridge to “SNAP caused food security,” “charitable food replaced public assistance,” or “administrative burden caused distrust” until same-episode outcomes and time order are observed.

## Sources and reproduction

- [Machine-readable cross-source record](../../../records/us-food-security-safety-net-route-buffer-crosssource-2024-2026.json)
- [Public-system route triangulation record](../../../records/us-public-system-route-security-triangulation-2026.json)
- [WBNS food-insecurity record](../../../records/us-urban-wbns-food-insecurity-persistence-2019-2025.json)
- [WBNS charitable-food record](../../../records/us-urban-wbns-charitable-food-access-2019-2025.json)
- [SNAP administrative-access record](../../../records/us-snap-administrative-access-2026.json)
- [SIPP SNAP transition record](../../../records/us-sipp-snap-transition-following-hardship-2024.json)

**Evidence status:** bounded public-system/food-security route comparison; benefit adequacy, same-episode hardship, remedy, recovery, trust, and political action remain unestablished.
