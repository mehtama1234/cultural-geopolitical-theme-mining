# SHED 2025 homeowners-insurance pressure layer v1

**Checked:** 2026-09-12  
**Unit:** US adult respondent whose household owns its primary home; 2025 Federal Reserve SHED  
**Method:** weighted descriptive percentages using `weight`; each measure uses its own nonmissing denominator; no design-based standard errors or causal estimate

## The question

When insurance becomes expensive or incomplete, how does that pressure appear
in coverage, shopping, lender dependence, and the ability to protect a home?
This is a housing, financial, consumer, and place-level question. It is not a
single-home move study.

```text
hazard, replacement cost, lender rule, or insurer decision
  -> premium, coverage, deductible, availability, or search changes
  -> household pays more, goes without, accepts a gap, or seeks another policy
  -> repair, mortgage, sale, move/stay, and local-risk decisions change
  -> public insurance, lender, insurer, household, and political response
```

## Owner-level results

Among 8,500 respondents in households that own their homes, 93.5% reported
homeowners or condo insurance, meaning 6.5% did not in this SHED cut. Among
those with an insurance response, 63.2% agreed that cost had risen more than
expected in recent years, 13.5% agreed they struggled to afford premiums, and
19.6% agreed they wanted more coverage but could not afford it. Only 25.7%
reported shopping around in the past 12 months.

| Owner group | Has insurance | Cost up more than expected | Struggles to afford premiums | Wants more coverage but cannot afford it | Shopped around | Satisfied with coverage |
|---|---:|---:|---:|---:|---:|---:|
| All owners | 93.5% | 63.2% | 13.5% | 19.6% | 25.7% | 51.5% |
| Own with mortgage | 97.0% | 62.4% | 15.4% | 21.6% | 26.5% | 49.2% |

The measures are not interchangeable. A household can be insured but face a
premium shock, want more coverage, or be dissatisfied; shopping is an action,
not proof that an affordable alternative existed.

Among respondents reporting no insurance and answering the reason question,
the weighted reasons were: 43.3% could not afford it, 16.1% said it was not
worth the cost, 15.0% self-insured or preferred not to buy, 8.1% said no
company would insure the home, and 17.6% selected another reason. These are
reported reasons among the question's nonmissing universe, not a verified
market denial rate.

## Income distribution among owners

| Reported household income | Owner rows | Has insurance | Struggles to afford premiums | Wants more coverage but cannot afford it | Cost up more than expected | Shopped around |
|---|---:|---:|---:|---:|---:|---:|
| Under $50k | 1,348 | 77.2% | 27.7% | 33.1% | 63.3% | 22.9% |
| $50k–$99k | 2,276 | 92.7% | 18.9% | 24.5% | 64.8% | 24.7% |
| $100k or more | 4,876 | 97.3% | 9.1% | 15.5% | 62.5% | 26.7% |

The sharpest income differences are in coverage, premium affordability, and
desired additional coverage. The cost-increase perception is comparatively
similar across bands, suggesting that exposure to rising costs and the ability
to absorb them are different dimensions.

Mortgage owners report higher coverage, but also more premium difficulty and
unmet coverage preference than the full owner group. A lender requirement may
preserve formal coverage while leaving less room in the budget or less control
over the terms.

## What this adds to the broad societal program

1. **Insurance is a protection-and-control problem, not only a price.** The
   household can pay a premium and still have inadequate coverage or a gap.
2. **Affordability is unequal.** Lower-income owners report much less coverage
   and more difficulty paying or expanding it, while cost increases are widely
   noticed across income groups.
3. **Mortgage dependence changes the option set.** Coverage can be formally
   required while the household still lacks a practical ability to shop, add
   protection, or absorb a deductible.
4. **Shopping is not the same as exit power.** Searching does not reveal how
   many insurers quoted, what exclusions changed, or whether switching was
   possible without losing the mortgage or a needed coverage level.
5. **Housing security remains downstream.** This cross-section does not show
   repair, claims, nonrenewal, sale, move/stay, health, debt, or local political
   response.

## Arrow ledger

| Arrow | Status | Safe current conclusion | Missing test |
|---|---|---|---|
| Risk/cost → premium or coverage pressure | Reported | Many owners report recent cost increases; lower-income owners report more affordability and coverage gaps | Property risk, insurer, premium, deductible, renewal, and coverage records |
| Premium/coverage → search or no insurance | Compared / Reported | Some owners shop; uninsured respondents often cite affordability | Quotes, nonrenewals, insurer availability, policy terms, and failed searches |
| Insurance status → mortgage/repair/sale/move | Open | Coverage and lender requirements can change the option set | Same property/household records through renewal, claim, repair, financing, and move |
| Insurance pressure → household security | Open | Premium and coverage pressure can compete with other needs | Budget, debt, food, health, energy, and deductible payment in the same period |
| Place risk → trust and political response | Open | Insurance encounters can become judgments about insurers, lenders, regulators, or government | Attribution, fairness, local identity, complaint, organizing, and action |

## Next bounded test

Follow comparable owners through one renewal or claim cycle. Record property
risk, premium, deductible, exclusions, insurer, lender requirement, shopping
quotes, nonrenewal, coverage change, repair, claim payment, debt, health,
move/stay, and later trust. Compare low- and high-income owners, mortgage and
free-and-clear owners, renters, and high- versus low-risk places. Include a
counterexample where a high-risk household retained affordable, adequate
coverage or where a premium increase did not change other household choices.

## Reproduction and limits

```text
python3 scripts/analyze_shed_housing_insurance_pressure.py \
  --input /path/to/SHED_2025.csv.zip \
  --output /tmp/shed-housing-insurance-pressure.json
```

The raw SHED file has 12,934 respondent rows; 8,500 belong to owner households
in this module. Insurance questions have different universes, and the reason
question is asked only of respondents without reported insurance. Results are
self-reported weighted averages, not a market denial, premium, claim, or move
rate. The analysis uses the official [Federal Reserve SHED data release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
