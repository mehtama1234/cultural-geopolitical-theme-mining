# Migration/place context: joint growth, nativity, trust, and action v1

**Checked:** 2026-09-13  
**Unit:** 2024 Cooperative Election Study common-content post-election respondent  
**Context axes:** county population change and ACS foreign-born share, both 2020–2023/2023 place measures  
**Status:** exploratory weighted contextual comparison; not an immigration-attitude or causal estimate

## Question

Does the local political-context pattern differ when population growth and
foreign-born share are considered together? A one-axis comparison could mistake
composition for growth, or growth for composition. The joint screen uses the
same county-keyed CES trust/action measures as the [growth-only
layer](migration-place-local-trust-action-context-v1.md).

## Main joint result: federal trust

Cells are pooled weighted percentages saying they trust the federal government
a great deal or a fair amount. Rows are population-growth quartiles; columns are
foreign-born-share quartiles. The cells are contextual estimates, not
county-representative opinion estimates.

| Growth \\ foreign-born share | Q1 lowest | Q2 | Q3 | Q4 highest |
|---|---:|---:|---:|---:|
| Q1 lowest growth | 44.092% | 41.767% | 41.844% | 39.542% |
| Q2 | 38.441% | 39.243% | 36.191% | 39.124% |
| Q3 | 36.478% | 37.269% | 37.476% | 41.288% |
| Q4 highest growth | 39.186% | 27.846% | 34.364% | 36.055% |

The pattern is not monotonic on either axis. The lowest federal-trust cell is
high-growth/Q2-nativity (27.846%), while high-growth/high-nativity is 36.055%
and low-growth/high-nativity is 39.542%. This weakens any simple claim that
either growth or foreign-born composition alone determines local distrust.

## Other endpoints

### State trust

| Growth \\ foreign-born share | Q1 lowest | Q2 | Q3 | Q4 highest |
|---|---:|---:|---:|---:|
| Q1 lowest growth | 53.725% | 54.635% | 53.707% | 54.574% |
| Q2 | 54.708% | 57.112% | 53.167% | 55.009% |
| Q3 | 54.653% | 53.304% | 50.849% | 52.908% |
| Q4 highest growth | 59.135% | 50.822% | 58.442% | 58.483% |

State trust is generally higher than federal trust, but it too varies across
the joint cells rather than following one direction.

### Civic action

| Growth \\ foreign-born share | Q1 lowest | Q2 | Q3 | Q4 highest |
|---|---:|---:|---:|---:|
| Q1 lowest growth | 37.881% | 42.015% | 35.058% | 36.047% |
| Q2 | 39.051% | 36.204% | 39.806% | 35.792% |
| Q3 | 34.629% | 38.759% | 36.835% | 37.552% |
| Q4 highest growth | 37.764% | 38.666% | 37.837% | 35.036% |

Civic action is comparatively stable across cells. The highest observed cell
is 42.015% and the lowest is 34.629%, so the screen does not support a simple
withdrawal or mobilization story based on these two place axes.

## Interpretation boundary

This is a contextual bridge, not a test of whether immigration changes trust.
Population growth includes births, deaths, domestic migration, and
international migration. Foreign-born share is a composition indicator, not a
measure of recent arrivals, legal status, or personal contact. CES respondents
are not the same people as ANES respondents, and the CES common file does not
contain the ANES immigration battery. The tables do not measure belonging,
fairness, blame, or what any respondent thought caused local change.

The most defensible reading is a counterexample result: federal trust varies
across combined place conditions, but neither growth nor foreign-born share
alone explains the pattern; civic action remains broadly stable. Housing,
service capacity, party composition, race/class distribution, media, and
neighboring-place access remain plausible explanations.

## Coverage and uncertainty record

The place frame contains 620 counties with at least 100,000 residents and
usable 2020 and 2023 population estimates. Each axis has four quartiles. CES
respondent counts in the 16 cells range from 1,133 to 3,675. Percentages use
`commonpostweight`; this pass does not claim design-based standard errors or
county-representative estimates because the public-use variance design was not
implemented at this joint-cell level.

## Reproduction

```text
python3 scripts/analyze_ces_local_trust_action_joint_axes.py \
  --cces /tmp/cces24-common.csv \
  --population /tmp/co-est2024-alldata.csv \
  --nativity /tmp/acsdt5y2023-b05002.dat \
  --output /tmp/cces-joint-trust-action.tsv
```

Sources: [CES Common Content, 2024](https://doi.org/10.7910/DVN/X11EP6), the
[CES public-data page](https://cces.gov.harvard.edu/explore), Census county
population estimates, and ACS table-based B05002 foreign-born counts.

## Next use

Use the joint screen to choose counterexamples for a real local-meaning study:
high-growth/high-nativity places with stable civic action, low-growth/high-
nativity places with different trust, and high-growth/low-nativity places with
low federal trust. Then seek direct local immigration-attitude or public-
discourse measures before assigning a cultural explanation.
