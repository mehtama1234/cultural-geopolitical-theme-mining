# Finding 005: Expense pressure expands search across income groups, but not the same way

**Status:** bounded same-respondent income-stratified cross-lag finding · **Checked:** 2026-09-19

## The finding

The April-to-June 2025 HTOPS link retains **6,564** respondents with the same
`SCRAMID`. April self-reported expense difficulty is carried to June search,
AI-use, and Congress-confidence outcomes. Within every household-income band,
people reporting expense difficulty searched more than people reporting no
difficulty, but the route differed by resource position:

| April household income band | Job search, difficulty vs not | Benefit search, difficulty vs not | Credit search, difficulty vs not | Any AI use, difficulty vs not |
|---|---:|---:|---:|---:|
| Under $50,000 | 39.8% vs 16.3% | 20.3% vs 10.1% | 16.2% vs 10.1% | 41.6% vs 38.3% |
| $50,000–$99,999 | 46.2% vs 21.4% | 22.5% vs 9.0% | 25.1% vs 11.5% | 60.5% vs 52.9% |
| $100,000 or more | 37.0% vs 25.1% | 15.4% vs 13.0% | 23.6% vs 12.1% | 71.5% vs 71.7% |

The result is not a simple “poor people search, rich people use AI” story.
Search rises across the distribution, but lower-income respondents show a
particularly large job-search gap and a clear benefit-search gap. Higher-income
respondents have much higher AI use overall, yet expense difficulty barely
changes AI use in that group.

The six search fields also show a multi-front navigation burden. Among people
reporting expense difficulty, the weighted mean number of search domains was
1.34 below $50,000, 1.59 at $50,000–$99,999, and 1.39 at $100,000 or more.
The share searching in at least two domains was 40.3%, 45.7%, and 39.4%; among
people without expense difficulty it was 21.8%, 27.1%, and 26.5%. This makes
the burden more concrete: expense pressure is associated with simultaneous
option-building across multiple systems, not merely one isolated search.

The overlap screen also argues against treating AI as a substitute for this
navigation. Among expense-difficulty respondents, June AI users searched at
least two domains at 56.0% below $50,000, 50.6% at $50,000–$99,999, and 40.7%
at $100,000 or more. The corresponding shares among non-AI users were 29.1%,
38.3%, and 36.1%. AI use is therefore associated with more simultaneous search
in this descriptive screen, not with the disappearance of search. This may
reflect greater need, greater digital access, or greater general engagement;
the design cannot distinguish those explanations or establish substitution.

## What the chain establishes

```text
April household resource position and expense difficulty
  -> June search across jobs, food, benefits, credit, housing, and medical help
  -> different navigation routes by income band
  -> completion, usable alternative, remedy, recovery, trust, and exit [open]
```

This strengthens the constrained-agency interpretation. Material pressure is
associated with more option-building effort, but the type of option pursued
depends partly on household resources. Search remains an effort measure, not
evidence that a usable alternative was found or that the household recovered.

## Limits

- Income is the April `RFAM_INCOME` household-income band, not liquid cash,
  wealth, debt capacity, or available time.
- The estimates use April `PWEIGHT` and April successive-difference replicate
  weights; the weights are not documented here as attrition-adjusted
  longitudinal weights.
- Expense difficulty is self-reported and broad; it is not a dated bill or
  named institutional episode.
  - The groups are descriptive. No causal effect, mediation, completion,
  receipt, remedy, recovery, trust change, or exit is identified.

## Reproducibility

- [Income-stratified derived record](../data/htops-2025-material-search-income-strata-v1.json)
- [Base cross-lag derived record](../data/htops-2025-material-search-cross-lag-v1.json)
- [Reproduction script](../../../../scripts/build_htops_2025_material_search_income_strata.py)
- Local April data dictionary input: `/tmp/htops-2504/HTOPS_2504_PUF_DATA_DICTIONARY_CSV.xlsx`
