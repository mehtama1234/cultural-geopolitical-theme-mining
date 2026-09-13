# Migration/place context: local trust and civic action by growth quartile v1

**Checked:** 2026-09-13  
**Unit:** 2024 Cooperative Election Study common-content post-election respondent  
**Place key:** respondent county FIPS supplied in the public file  
**Context:** Census county population change, 2020–2023  
**Status:** weighted descriptive local-context layer; not an immigration-attitude or causal estimate

## Why this layer is here

The ANES immigration tables measure direct immigration meaning and reported
political action but do not provide a documented public county join. The CES
common file does provide county FIPS, state and federal trust questions,
reported voting, and civic-action items. It does **not** provide the
immigration-specific battery in the common file. This layer therefore measures
whether local political trust/action context differs across places with
different population-growth conditions; it does not substitute local trust for
local immigration opinion.

```text
county growth context
  -> local respondent sample
  -> trust in federal/state government and civic action
  -> contextual political capacity

immigration-specific meaning remains a separate ANES respondent layer
```

## Measures

- **Federal trust:** `CC24_423`, a great deal or a fair amount versus less;
- **State trust:** `CC24_424`, a great deal or a fair amount versus less;
- **Civic action:** any of `CC24_430a_1` through `CC24_430a_6`: local meeting,
  political sign, campaign work, protest, public-official contact, or political
  donation; blood donation is excluded;
- **Reported voting:** `CC24_401 == 5`, definitely voted in the November 2024
  general election;
- **Weight:** `commonpostweight`;
- **Place context:** 620 counties with at least 100,000 residents and usable
  2020 and 2023 population estimates, divided into four county-count quartiles.

The estimates below are pooled weighted percentages within each growth group.
They are not design-based standard-error estimates: the public CES file was
used here for a bounded contextual comparison, and this pass does not have a
replicate-weight or fully specified county-level variance procedure.

## Results

| County population-change group | Counties in place frame | CES counties represented | CES respondents | Median change | Federal trust | State trust | Any civic action | Reported voted |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Q1 lowest | 155 | 155 | 12,277 | -1.023% | 41.927% | 54.174% | 38.112% | 96.714% |
| Q2 | 155 | 152 | 9,718 | 0.962% | 38.246% | 55.144% | 37.716% | 96.695% |
| Q3 | 155 | 150 | 9,654 | 2.627% | 38.185% | 52.862% | 37.186% | 97.681% |
| Q4 highest | 155 | 155 | 7,033 | 6.749% | 35.251% | 57.406% | 37.268% | 97.070% |

## What the screen suggests

Federal trust is lower in the highest-growth quartile than in the lowest-growth
quartile in this descriptive screen: 35.251% versus 41.927%. State trust is
not monotonic, civic action changes little, and reported voting is high in all
four groups. The result therefore does not support a simple “growth produces
withdrawal” story. It suggests a narrower testable possibility: local growth
context may coincide with different federal-versus-state trust patterns while
ordinary civic action remains comparatively stable.

This is not an immigration result. Population change includes births, deaths,
domestic migration, and international migration. The CES respondents are not
the same people as the ANES respondents, and the table does not measure what
respondents think immigration means, whom they blame, or whether local growth
caused their trust judgment.

## Important limitations

1. County survey cells are unequal and some counties have few respondents;
   this pass reports quartile-pooled context rather than county opinion.
2. The CES common file’s county FIPS is a usable place key, but the survey
   sample and weights were not designed here for a county-representative
   estimate.
3. Growth is a proxy for local change, not a migration measure.
4. Trust, voting, and civic action are separate outcomes; none is a direct
   belonging or fairness measure.
5. The CES common-content questionnaire includes local political action and
   trust, but the immigration-specific opinion battery used in the ANES layer
   is not part of this common-file extraction.

## Reproduction

```text
python3 scripts/analyze_ces_local_trust_action_by_growth.py \
  --cces /tmp/cces24-common.csv \
  --population /tmp/co-est2024-alldata.csv \
  --output /tmp/cces-growth-trust-action.tsv
```

Source files are the [CES Common Content, 2024 public
dataset](https://doi.org/10.7910/DVN/X11EP6) and the Census county population
estimates already used in the [migration/place capacity
screen](migration-capacity-all-counties-profile-v1.md). The CES project states
that responses are publicly available through its [Dataverse
repository](https://cces.gov.harvard.edu/explore).

## Next join that is actually justified

Use this as contextual political capacity beside the county housing/service
panel. Keep the ANES immigration battery at the national respondent level
unless a valid geography-bearing immigration survey is acquired. A future
local survey comparison should include direct local immigration meaning,
fairness, attribution, and action—not infer those from trust or election
outcomes.
