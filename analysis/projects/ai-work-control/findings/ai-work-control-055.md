# Finding 055: Housing security has payment, coverage, hazard, and backstop layers that do not yet form a move outcome

**Status:** provisional non-pooled housing/insurance/place bridge · **Checked:** 2026-09-14

## The bounded finding

The housing/place lane now places four evidence surfaces in one architecture:

1. Federal Reserve SHED measures household rent arrears, uninsured homeowners, and insurance affordability.
2. Treasury FIO measures premiums, nonrenewals, and claim severity across climate-risk ZIP groups.
3. FEMA NRI and Census relationships add modeled hazard and socioeconomic/tenure place context.
4. California FAIR Plan stocks show the scale of a public residual-market backstop.

The defensible synthesis is: **housing security has separate payment, coverage, hazard, market, and public-backstop dimensions. They can move together in places or households, but the current evidence does not show a complete path from cost or hazard to inadequate coverage, repair, move/stay, or political response.**

## Evidence surfaces kept separate

| Stage | Direct evidence | Unit | What remains open |
|---|---|---|---|
| Household payment and coverage | In 2025, 23% of renters reported being behind on rent; 6% of homeowners reported no insurance; 43% of uninsured owners said they could not afford coverage; 30% of insured owners below $50,000 reported premium struggle. | SHED adult respondents and conditional homeowner/renter frames | Arrears duration, eviction, policy terms, claims, repairs, and move/stay |
| Market/hazard exposure | Treasury reports highest climate-risk ZIP quintile premiums around $2,321 per policy, 82% above the lowest-risk quintile, and about 80% higher nonrenewal; FIO/FEMA context shows 0.959% versus 1.271% mean nonrenewal from relatively low to very high rating, while mean premiums are non-monotonic. | ZIP/policy rows and modeled county hazard groups | Causal hazard pricing, household coverage, property composition, insurer choice, and later outcomes |
| Place socioeconomic context | In the 2022 matched ZIP/ZCTA screen, lower-income-place rows have lower mean premiums than high-income-place rows but higher mean nonrenewal; place owner-share groups also diverge. | Unweighted matched place rows | Individual income/tenure, landlord pass-through, coverage adequacy, and displacement |
| Public backstop | California FAIR Plan policies rise from 242,440 in 2021 to 642,010 in 2025 and 696,562 in June 2026; insured exposure rises from $160.6B to $694.0B in the fiscal series and approximately $768B in the later headline. | Residual-market policy/exposure stocks | Voluntary-market causation, affordability, claims, repairs, household moves, and public fiscal incidence |

These objects are intentionally not pooled. A household survey, ZIP-level insurer market, modeled hazard assignment, and residual-market stock do not share a denominator or household trajectory.

## The housing-security chain under test

```text
income, rent, mortgage, hazard, and insurance market conditions
  -> payment pressure, coverage gaps, premium struggle, and public-backstop use
  -> repairs, claims, debt, service access, mobility, and neighborhood change
  -> attribution, trust, local organizing, and policy demand
  -> insurer/regulator/state response and place resilience
```

The evidence reaches payment pressure, coverage status, market exposure, modeled hazard, and public-backstop scale. It does not close repair, move/stay, household welfare, legitimacy, or political response.

## What the comparison changes

### Arrears and insurance are related but not interchangeable

Rent arrears measure a payment episode; no insurance measures coverage status; premium struggle measures affordability perception. None establishes eviction, claim adequacy, or whether housing is lost. The same household may be current on rent and uninsured, insured but under-covered, or in arrears with strong family or public support.

### Market hazard is not household hazard

Treasury and FEMA place data show broad associations between risk groups and market outcomes, but the non-monotonic FEMA premium screen is an important counterexample. Rebuilding costs, property values, regulation, insurer mix, and policy composition all matter. Modeled expected loss is not a realized household loss.

### A public backstop is capacity, not guaranteed security

FAIR Plan growth makes public/private risk transfer visible. It does not show that voluntary coverage withdrew, that households can afford limits and deductibles, or that claims will fund repairs. Backstop scale should be paired with assessments, premiums, claims, repairs, and household outcomes.

### Place gradients do not identify individual incidence

ZIP/ZCTA income and tenure context helps locate unequal exposure but cannot be read as the income or tenure of each insured policy. The lower-income-place/higher-nonrenewal pattern is a target for a property/household panel, not a causal social gradient.

## Counterexamples kept visible

- Rent arrears do not equal eviction or homelessness.
- No insurance can reflect self-insurance or preference as well as unaffordability or market withdrawal.
- A high-risk place can have lower mean premium than a moderately high-risk place because asset, insurer, or market composition differs.
- A public residual pool can grow because of policy design or enrollment visibility without proving voluntary-market collapse.
- Higher premiums do not show that a household can or cannot pay, and lower premiums do not show adequate coverage.
- Coverage can persist while deductibles, exclusions, delays, or underinsurance leave repair capacity weak.
- A place-level nonrenewal gradient does not establish that residents moved, lost wealth, or politically mobilized.

## Next decisive test

Build a compatible property/household-year panel containing:

1. premium, deductible, coverage, nonrenewal, claim, assessment, and insurer;
2. hazard, property type/value, mortgage, rent, income, and tenure;
3. assistance, repair, contractor, debt, service access, and health outcomes;
4. move/stay, vacancy, displacement, and neighborhood change;
5. attribution, trust, local organizing, and regulatory response; and
6. a similar exposed place with different market access or public backstop.

Do not promote this bridge to “climate displacement,” “insurance failure,” or “housing insecurity caused by hazard” until household/property outcomes and time order are observed.

## Sources and reproduction

- [Machine-readable cross-source record](../../../records/us-housing-insurance-payment-coverage-mobility-crosssource-2021-2026.json)
- [Federal Reserve housing/insurance record](../../../records/us-federal-reserve-housing-insurance-risk-2025.json)
- [Treasury FIO insurance-market record](../../../records/us-treasury-fio-homeowners-insurance-market-2018-2022.json)
- [Treasury/FEMA hazard-context record](../../../records/us-treasury-fio-fema-nri-hazard-context-2022.json)
- [California FAIR Plan record](../../../records/us-california-fair-plan-residual-market-growth-2021-2026.json)

**Evidence status:** bounded housing-payment/coverage/hazard/backstop comparison; household/property incidence, repair, mobility, legitimacy, and political response remain unestablished.
