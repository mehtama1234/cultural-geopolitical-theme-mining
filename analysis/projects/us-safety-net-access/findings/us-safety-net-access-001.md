# State SNAP participation is not a simple poverty or mobility ranking

**Status:** descriptive state-context finding; ecological and non-causal  
**Checked:** 2026-09-14  
**Sources:** USDA FY2025 SNAP state chart data and 2024 ACS state transportation context

## The finding

SNAP participation varies widely across states, but the variation cannot be
read as a simple poverty ranking or an administrative-performance ranking. In
a 51-state/DC crosswalk, the mean participation rate is highest in the lowest
ACS median-income quartile, falls in the second quartile, rises in the third,
and falls again in the highest quartile. Meanwhile, long-commute exposure rises
across the income groups and zero-vehicle exposure peaks in the third group.

That pattern is a warning about the number of different systems hidden inside a
state rate: need, eligibility, household composition, labor-market geography,
transportation, administration, office/channel access, and take-up.

## Matched state-context comparison

| ACS median-income group among matched states/DC | States | Income range | Mean SNAP participation | Zero-vehicle households | Commute 30+ minutes |
|---|---:|---:|---:|---:|---:|
| Q1 | 13 | $59,127–$72,350 | 13.10% | 6.56% | 33.29% |
| Q2 | 13 | $72,389–$77,871 | 9.80% | 6.84% | 35.11% |
| Q3 | 13 | $79,721–$92,090 | 12.22% | 11.13% | 41.40% |
| Q4 | 12 | $95,665–$109,707 | 10.91% | 8.36% | 42.47% |

SNAP participation is an unweighted mean of the state rates. The ACS vehicle
and commute measures are pooled using their table totals. The income groups
are geographic contexts, not households assigned to income bands.

## Why the non-monotonic pattern matters

If participation were treated as a direct proxy for poverty, the Q2 dip and Q3
rise would be unexplained noise. A more careful interpretation is that state
income is only one context variable. States with similar median income can
have different household composition, employment, housing, transportation,
disability, migration, eligibility rules, and administrative routes.

The mobility measures make the same point from another direction. Q4 has the
highest long-commute share despite the highest state median-income range, while
Q3 has the highest pooled zero-vehicle share. A long commute may reflect labor
market geography, housing costs, or choice; zero vehicles may reflect transit,
density, disability, household composition, or constrained access. Neither is
automatically a hardship measure.

Simple unweighted state-level screens produce correlations of −0.110 between
SNAP participation and state median income, 0.425 between SNAP participation
and zero-vehicle share, and 0.485 between SNAP participation and long-commute
share. These figures are descriptive screens, not causal coefficients and not
household-level associations.

## Counterexamples

- New Mexico has the highest participation rate, 21.9%, but a 5.10%
  zero-vehicle household share and a 29.93% long-commute share.
- DC has high participation, 20.3%, and the highest zero-vehicle and commute
  shares in the crosswalk, alongside the highest state median income.
- Wyoming has the lowest participation rate, 4.7%, without being the highest-
  income state; its zero-vehicle share is 4.28% and long-commute share 19.16%.

These cases prevent a single explanation. They do not prove that any one state
has better or worse administration, nor do they show that transport caused
SNAP participation.

## What remains unmeasured

The crosswalk does not observe eligible nonparticipants, application effort,
notice comprehension, office distance, processing time, procedural denials,
renewal churn, benefit amount, food security, household debt, or political
interpretation. The USDA state denominator is the state/DC population; the ACS
vehicle and commute fields have separate table universes. The years also differ
(FY2025 versus 2024 ACS).

The next state test should add comparable eligibility and need measures, state
administrative route measures, and a consistent time window. Only then can the
program distinguish a high-need state from a high-take-up state, a low-need
state from an underaccess state, and a mobility context from a mobility burden.

Read the [reproducible crosswalk layer](../usda-snap-acs-state-crosswalk-v1.md),
[machine-readable crosswalk record](../../../records/usda-snap-acs-state-crosswalk-2026.json),
[machine-readable FY2025 SNAP state-participation record](../../../records/usda-snap-fy2025-state-participation-2026.json),
[machine-readable FY2025 SNAP context record](../../../records/usda-snap-fy2025-current-context-2026.json),
and [SNAP administrative-access finding](../../../findings/us-safety-net-access-matched-evidence-001.md).

Sources: [USDA FY2025 state chart data](https://www.ers.usda.gov/media/29462/55416-chart-data-file.xlsx?v=68216), [USDA SNAP context](https://www.ers.usda.gov/topics/food-nutrition-assistance/supplemental-nutrition-assistance-program-snap/key-statistics-and-research), and [2024 ACS state context](../../../records/us-acs-transport-state-income-context-2024.json).
