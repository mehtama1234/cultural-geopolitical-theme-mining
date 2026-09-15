# ACS state transportation context by state income v1

**Checked:** 2026-09-13  
**Analysis:** [analyze_acs_transport_state_context.py](../../../scripts/analyze_acs_transport_state_context.py)  
**Tables:** [B08201 vehicle availability](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/1YRData/acsdt1y2024-b08201.dat), [B08303 travel time](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/1YRData/acsdt1y2024-b08303.dat), [B19013 median household income](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/1YRData/acsdt1y2024-b19013.dat)

## Result

The state-level context is non-monotonic. The highest-income quartile has the
highest pooled share of workers with 30-plus-minute commutes (42.31%), but the
third quartile has the highest pooled no-vehicle household share (11.52%).
The lowest-income quartile has the lowest long-commute share (33.43%), despite
including the lowest state median incomes.

| State median-income quartile | No vehicle | Commute 30+ min |
|---|---:|---:|
| Q1: $27,213–$72,212 | 6.90% | 33.43% |
| Q2: $72,350–$77,735 | 6.77% | 35.48% |
| Q3: $77,871–$87,534 | 11.52% | 41.22% |
| Q4: $92,090–$109,707 | 8.16% | 42.31% |

This is useful as a counterexample to a single “mobility burden” index. Vehicle
scarcity can be shaped by density and transit structure, while commute length
can be shaped by housing prices, labor-market geography, and household choice.

## Method and boundaries

The 52 state/DC/PR geographic rows are sorted by B19013 median household income
and split into four equal-count groups. B08201 vehicle estimates and B08303
commute estimates are pooled within each group using their table totals. The
groups are geographic contexts, not households assigned to income quartiles.
No margin-of-error propagation is included in this first pass.

The state rows are preserved in the temporary output of the analysis script;
the four bounded observations are in the [trend record](../../records/us-acs-transport-state-income-context-2024.json).
The next test is to condition on explicit household income, race, disability,
urban form, and transit modes, then connect to provider capacity, actual costs,
care trips, and political or cultural meaning.
