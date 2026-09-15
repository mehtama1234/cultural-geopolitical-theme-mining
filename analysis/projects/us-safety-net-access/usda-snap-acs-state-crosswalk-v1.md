# SNAP participation, state resources, and mobility context crosswalk v1

**Checked:** 2026-09-14  
**Sources:** USDA FY2025 SNAP state chart data and 2024 ACS state transportation context  
**Unit:** matched state/DC aggregate; 51 observations  
**Method:** descriptive ecological crosswalk; no causal estimate

## Question

Does the large FY2025 state spread in SNAP participation line up simply with
state median household income, or does it coexist with different transportation
option sets? The join matches the USDA participation rate to the existing ACS
state context for median household income, zero-vehicle households, and workers
with commutes of 30 minutes or more.

The ACS state-income quartiles are recomputed over the **51 matched states/DC**
after excluding Puerto Rico, which appears in the existing 52-row ACS context
but not in the USDA state chart. SNAP participation is summarized as the
unweighted mean of state rates; ACS vehicle and commute measures are pooled by
their table totals.

## Results by matched ACS income quartile

| Matched ACS state-income quartile | States | Median-income range | Mean SNAP participation | Zero-vehicle households | Commute 30+ minutes |
|---|---:|---:|---:|---:|---:|
| Q1 | 13 | $59,127–$72,350 | 13.10% | 6.56% | 33.29% |
| Q2 | 13 | $72,389–$77,871 | 9.80% | 6.84% | 35.11% |
| Q3 | 13 | $79,721–$92,090 | 12.22% | 11.13% | 41.40% |
| Q4 | 12 | $95,665–$109,707 | 10.91% | 8.36% | 42.47% |

The SNAP pattern is non-monotonic: the lowest income quartile has a higher
mean participation rate than Q2, Q3 rises again, and Q4 is below Q1 and Q3.
The mobility measures do not move as one currency either. Long-commute exposure
rises across the four groups, while zero-vehicle exposure peaks in Q3.

Across the 51 matched states/DC observations, simple unweighted Pearson
correlations are **−0.110** between SNAP participation and median household
income, **0.425** between SNAP participation and zero-vehicle share, and
**0.485** between SNAP participation and long-commute share. These are screens,
not estimates of causal relationships; no population weighting, standard-error
propagation, or multiple-comparison adjustment is applied.

## Counterexamples that prevent a simple story

- **New Mexico** has the highest SNAP participation rate (21.9%) but a median
  household income of $67,816, a 5.10% zero-vehicle household share, and a
  29.93% long-commute share.
- **District of Columbia** has a high participation rate (20.3%) and the
  highest zero-vehicle and long-commute shares in this crosswalk, alongside the
  highest ACS median household income ($109,707). Density and transit context
  are clearly entangled with the aggregate measures.
- **Wyoming** has the lowest participation rate (4.7%) but is not the
  highest-income state; its zero-vehicle share is 4.28% and long-commute share
  19.16%.

The results therefore do not support reading state SNAP participation as a
simple poverty ranking, a service-quality ranking, or a mobility-burden index.
The same participation rate can arise from different combinations of need,
eligibility, household composition, labor markets, place, transportation, and
administrative access.

## Method and limits

The reusable [crosswalk script](../../../scripts/analyze_usda_snap_acs_state_crosswalk.py)
reads the USDA chart workbook and the existing ACS state-context JSON. The
USDA rate denominator is each state/DC population; ACS vehicle and commute
denominators are their official table universes. The join does not observe
individual households, eligible nonparticipants, state eligibility rules,
office/channel access, processing time, procedural denials, food security,
benefit adequacy, or political meaning.

The state-level associations can be useful for selecting matched places, but
they cannot establish that SNAP caused mobility conditions, that mobility
caused participation, or that a state’s aggregate rate describes any one
household. The next test is a state-level need/eligibility/administrative-route
panel with compatible years and explicit processing or take-up measures.

The structured companion record is [SNAP participation and ACS state context](../../records/usda-snap-acs-state-crosswalk-2026.json).

Sources: [USDA SNAP FY2025 chart data](https://www.ers.usda.gov/media/29462/55416-chart-data-file.xlsx?v=68216), [USDA SNAP context page](https://www.ers.usda.gov/topics/food-nutrition-assistance/supplemental-nutrition-assistance-program-snap/key-statistics-and-research), and [2024 ACS state transportation context](../../records/us-acs-transport-state-income-context-2024.json).
