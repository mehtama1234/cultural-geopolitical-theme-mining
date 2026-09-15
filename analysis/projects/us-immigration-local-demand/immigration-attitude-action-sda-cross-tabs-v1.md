# Immigration attitude, institutional meaning, and action: ANES cross-tabs v1

**Checked:** 2026-09-13  
**Unit:** ANES 2024 Time Series Study post-election respondent  
**Route:** official UC Berkeley SDA interface, `anes2024full`  
**Weight:** `V240107b`, post-election raked weight for the 2016–2024 panel, face-to-face and web samples combined with PAPI  
**Design:** complex stratified-cluster Taylor-series standard errors  
**Status:** bounded descriptive result; not a causal or county-level estimate

## Why this is a useful societal result

This is the first actual respondent-level immigration meaning/action result in
the migration lane. It does not say that local housing or service conditions
caused these opinions. It shows that immigration policy preference is related
to several distinct interpretations—economic, labor-market, crime, cultural,
institutional, and electoral—and therefore should not be treated as one
latent “pro-” or “anti-immigration” attitude.

## Main results

All cells below are row percentages; the number in parentheses is the complex
sample standard error in percentage points. The row is the first variable in
each table and the columns are the desired immigration-level categories.

### Perceived economic meaning

| Respondent says immigrants are… | Increase a lot | Increase a little | Same | Decrease a little | Decrease a lot |
|---|---:|---:|---:|---:|---:|
| Extremely good for the economy | 17.6 (1.87) | 16.7 (1.74) | 49.1 (2.26) | 10.3 (1.48) | 6.4 (1.16) |
| Neither good nor bad | 4.7 (.97) | 6.5 (1.19) | 41.7 (2.21) | 21.2 (2.07) | 25.8 (2.05) |
| Extremely bad for the economy | 1.4 (3.20) | 4.4 (2.15) | 4.2 (1.46) | 6.9 (2.73) | 73.0 (4.44) |

Respondents who evaluate immigrants as economically very bad are much more
likely to want immigration decreased; respondents who evaluate immigrants as
very good are more likely to want it increased or left unchanged. These are
aligned judgments, not proof that either judgment reflects measured local
economic conditions.

### Perceived job competition

| Recent immigration is… likely to take jobs from people already here | Increase a lot | Increase a little | Same | Decrease a little | Decrease a lot |
|---|---:|---:|---:|---:|---:|
| Extremely likely | 12.0 (1.69) | 4.1 (1.89) | 16.1 (2.21) | 14.3 (1.94) | 53.5 (2.63) |
| Somewhat likely | 3.0 (.58) | 8.6 (1.01) | 44.1 (1.76) | 23.8 (1.56) | 20.5 (1.40) |
| Not at all likely | 11.8 (1.16) | 17.8 (1.57) | 47.2 (1.66) | 15.5 (1.21) | 7.8 (1.00) |

Perceived labor competition has a sharper association with desired direction
than with the size of the preferred change. People can oppose immigration
because they expect distributional harm even when the size of their preferred
reduction is not directly observed as a material calculation.

### Conditional citizenship pathway

| Path to citizenship for unauthorized immigrants | Increase a lot | Increase a little | Same | Decrease a little | Decrease a lot |
|---|---:|---:|---:|---:|---:|
| Favor | 8.8 (.72) | 13.8 (1.04) | 41.9 (1.24) | 19.7 (1.12) | 15.8 (.94) |
| Oppose | 6.4 (1.20) | 6.2 (1.14) | 23.4 (1.80) | 14.8 (1.77) | 49.3 (2.46) |
| Neither | 5.3 (1.05) | 6.0 (1.13) | 38.6 (2.41) | 21.7 (2.07) | 28.4 (2.15) |

Legal inclusion and desired immigration scale are related but not identical.
Even among respondents who favor a conditional pathway, most prefer keeping
levels the same or reducing them. This prevents a simplistic cultural reading
in which every policy dimension collapses into one camp.

### Reported presidential vote

| Reported candidate | Increase a lot | Increase a little | Same | Decrease a little | Decrease a lot |
|---|---:|---:|---:|---:|---:|
| Kamala Harris | 9.2 (.94) | 14.8 (1.26) | 47.4 (1.53) | 20.5 (1.32) | 8.1 (.87) |
| Donald Trump | 6.1 (.84) | 6.6 (.94) | 27.7 (1.63) | 16.3 (1.40) | 43.3 (1.84) |

The vote table is a political-action endpoint, but it is not an immigration
effect estimate. Party identity, race, religion, ideology, media, candidate
evaluation, economic judgment, and other issues are plausible alternatives.
It also excludes respondents with other candidate reports.

### Immigration scale and federal-government trust

| Desired immigration level | Always trust | Most of time | About half | Some of time | Never |
|---|---:|---:|---:|---:|---:|
| Increase a lot | 3.5 (1.67) | 12.0 (2.38) | 27.1 (3.52) | 36.0 (3.50) | 21.4 (3.49) |
| Same | 1.5 (.45) | 15.4 (1.30) | 32.6 (1.78) | 40.4 (1.67) | 10.0 (.90) |
| Decrease a lot | .9 (.45) | 5.6 (.87) | 24.0 (1.69) | 43.9 (1.91) | 25.6 (1.79) |

Trust is not a synonym for immigration preference. This is a descriptive
institutional-meaning gradient: it cannot tell whether trust shaped the
policy view, the policy view shaped trust, or both reflect prior identity and
information.

## Valid-case and uncertainty record

| Cross-tab | Valid unweighted cases | Total cases | Excluded by weight | Invalid/missing row or column |
|---|---:|---:|---:|---:|
| Immigration level × economic meaning | 4,685 | 5,521 | 557 | 279 |
| Immigration level × job competition | 4,697 | 5,521 | 557 | 267 |
| Immigration level × citizenship pathway | 4,692 | 5,521 | 557 | 272 |
| Immigration level × reported presidential vote | 3,654 | 5,521 | 557 | 1,310 |
| Immigration level × federal-government trust | 4,882 | 5,521 | 557 | 82 |

The vote table has substantial missingness because it requires a valid
post-election candidate report. These are weighted descriptive cross-tabs,
not adjusted regressions, and no multiple-comparison correction is claimed.

## What this changes in the broader program

The migration/place evidence now has two explicit layers:

```text
place layer: growth, nativity proxy, rent, vacancy, crowding, language access,
             firms, health capacity, and housing/service option stack

respondent layer: economic meaning, job attribution, crime attribution,
                  legal inclusion, cultural adaptation, trust, and vote
```

The layers may be compared only where geography, timing, and sample design
support the comparison. The safe societal conclusion is narrower: immigration
is interpreted through multiple material and cultural frames, and those frames
are associated with different policy and electoral responses. The tables do
not establish which local condition produced the interpretation.

## Reproduction

The tables were run through the official [ANES 2024 Full Release SDA
interface](https://sda.berkeley.edu/sdaweb/analysis/?dataset=anes2024full),
using `V242227` as the row, the listed variable as the column, `V240107b` as
the weight, row percentages, complex design, and standard errors. The
variable wording and universes are documented in the [official ANES study
release](https://electionstudies.org/data-center/2024-time-series-study/) and
[codebook](https://electionstudies.org/wp-content/uploads/2025/05/anes_timeseries_2024_userguidecodebook_20250430.pdf).

The bounded cross-tabs are preserved in the [machine-readable trend record](../../records/us-anes-immigration-meaning-action-2024.json)
for the shared registry and theme-coverage builds.
