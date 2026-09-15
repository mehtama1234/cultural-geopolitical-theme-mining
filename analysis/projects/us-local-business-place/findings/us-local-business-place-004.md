# Place change and political meaning remain separate stages

**Status:** provisional county-context bridge · **Checked:** 2026-09-14

## The bounded finding

The 2024 Cooperative Election Study can attach respondents to county FIPS and
therefore supplies a political-context layer beside the place-capacity work.
Across 620 counties with at least 100,000 residents, counties in the highest
2020–2023 population-growth quartile show lower pooled federal trust than the
lowest-growth quartile, while civic action and reported voting are broadly
stable. This is a place-context comparison, not evidence that business
capacity, population growth, migration, or housing conditions caused a
respondent's political judgment.

```text
population-change context
  -> county-keyed respondent sample
  -> trust, civic action, reported vote
  -> candidate political-capacity context

business/service capacity, access, belonging, and attribution remain separate
```

## Results

| County population-change group | Counties represented | CES respondents | Median population change | Federal trust | State trust | Any civic action | Reported voted |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 lowest | 155 | 12,277 | -1.023% | 41.927% | 54.174% | 38.112% | 96.714% |
| Q2 | 152 | 9,718 | 0.962% | 38.246% | 55.144% | 37.716% | 96.695% |
| Q3 | 150 | 9,654 | 2.627% | 38.185% | 52.862% | 37.186% | 97.681% |
| Q4 highest | 155 | 7,033 | 6.749% | 35.251% | 57.406% | 37.268% | 97.070% |

Federal trust is 6.676 percentage points lower in the highest-growth group
than in the lowest-growth group in this descriptive screen. State trust is
non-monotonic, civic action differs by less than one percentage point across
the endpoints, and reported voting is high in all groups. The counterexample
matters: a place-change context can coincide with a federal-trust difference
without a parallel decline in reported civic action or voting.

## What this adds to the capacity panel

The current CBP/ACS/QCEW/BPS/HRSA/RUCC screen measures nominal capacity,
material context, mobility context, wages, permits, and institutional shortage
designation in a 3,006-county complete-input frame. The CES screen measures
trust/action/vote among respondents in a different 620-county frame and uses
2020–2023 population change rather than 2023 sector capacity. It therefore
does not support a direct cross-cell regression or a claim that the high-
capacity/high-zero-vehicle cell has a particular political response.

It does establish a useful next design: select matched counties with similar
capacity, mobility, income, housing, and population-change context, then seek
a direct local survey or administrative political measure with the same place
and period. The decisive missing fields are respondent exposure to the local
change, perceived beneficiary or blamed actor, local belonging/fairness,
service use, organizing/contact, and institutional response.

## Boundaries and counterexamples

- Population change includes births, deaths, domestic migration, and
  international migration; it is not a migration or business-turnover measure.
- CES common-post weights produce pooled descriptive percentages here; they do
  not make every county representative, and no complex-survey standard errors
  are estimated in this pass.
- Trust, civic action, and reported voting are separate outcomes. None is a
  direct measure of belonging, fairness, attribution, or political efficacy.
- A high-growth place can have stable civic action; a low-growth place can have
  lower or higher trust for reasons unrelated to business capacity.
- The county-capacity and CES respondent layers are not silently pooled. Their
  denominators, sampling frames, dates, and measures remain visible.

The [machine-readable record](../../../records/us-cces-county-growth-trust-action-2024.json)
preserves the respondent denominators, valid universes, weights, place frame,
hashes, and open arrows. The [reproduction script](../../../../scripts/analyze_ces_local_trust_action_by_growth.py)
preserves the county quartile and endpoint definitions.

## Sources

- [CES 2024 common-content public data](https://doi.org/10.7910/DVN/X11EP6)
- [Census county population estimates](https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv)
- [Existing growth/trust/action context memo](../../us-immigration-local-demand/migration-place-local-trust-action-context-v1.md)

**Evidence status:** compared. The layer strengthens the place-context-to-
political-capacity segment, while direct local meaning, attribution, service
experience, and causal political response remain open.
