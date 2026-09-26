# Finding 001: Survey nonresponse can make income look higher and poverty look lower

**Status:** bounded measurement and data-quality finding · **Checked:** 2026-09-22

## The bounded finding

The Census Bureau reports that the weighted response rate for the 2026 Current
Population Survey Annual Social and Economic Supplement was 61.3%. Census
linked survey responses to administrative and census records to compare the
official survey-only weights with alternative weights designed to account for
observed nonresponse differences.

The evaluation finds that, since 2020, survey-only income estimates have been
about 2% to 4% higher than the alternative estimates across the income
distribution. In 2026, the survey-only median income estimate was 2.8% higher.
The survey-only poverty rate was 0.6 percentage points lower than the
alternative-weight estimate.

This does not mean the published survey is unusable. Census reports that the
post-2020 bias has been relatively stable, so year-to-year income and poverty
changes were generally not significantly biased except for the 2019–2020
comparison. The important boundary is about levels and subgroup visibility,
not an automatic rejection of every trend.

The route is:

```text
who answers the survey
  -> respondent/nonrespondent composition
  -> published income and poverty estimate
  -> interpretation of material pressure and inequality [open]
  -> policy, cultural, or political judgment [open]
```

## What this adds to the broader atlas

This is a measurement version of the atlas's central concern: what is visible
in an official record is shaped by the route that produces the record. A
headline income increase can be real as a change in the published series while
the level is shifted upward because higher earners are more represented among
respondents.

It also makes source comparison more disciplined. A survey, an administrative
file, a linked panel, and a perception poll do not simply provide more or less
data; they see different people and outcomes. The Census adjustment is a
stronger benchmark because it uses linked records, but it still cannot correct
differences that are absent from those records.

## Limits and counterexamples

- The adjustment is not a definitive truth measure; unobserved differences can
  remain.
- The 2026 method uses 2024 administrative records because 2025 records were
  unavailable.
- A response rate alone does not establish bias; bias depends on differences
  between respondents and nonrespondents.
- The finding does not show which households were missed or how their culture,
  trust, political judgment, or lived hardship differed.
- A level bias does not automatically erase a year-to-year direction.

## Next decisive test

The next useful artifact is a protected respondent/nonrespondent comparison
that joins income, poverty, race, place, household structure, program receipt,
health, trust, and political action across survey and administrative coverage.
Until that exists, treat national survey levels as adjusted estimates with a
known boundary, not as a complete census of material life.

## Sources

- [Census Bureau: Using Administrative Data to Evaluate Nonresponse Bias in the 2026 CPS ASEC](https://www.census.gov/newsroom/blogs/research-matters/2026/09/evaluating-nonresponse-bias.html)
- [Machine-readable trend record](../../../records/us-census-cps-asec-nonresponse-bias-2026.json)

**Evidence status:** official Census analysis documents a persistent post-2020
nonresponse bias in survey-only income and poverty levels while preserving a
limited year-to-year trend interpretation; population experience and
unobserved nonresponse differences remain open.
