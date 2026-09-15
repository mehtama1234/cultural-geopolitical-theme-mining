# Finding 063: US firm capacity is a size-stratified bundle, not one adoption score

**Status:** provisional public-firm baseline · **Checked:** 2026-09-14

## The bounded finding

The public World Bank Enterprise Survey profile for the United States is not
the missing AI follow-up, but it does add a useful firm-level middle layer.
Across 2,589 establishments interviewed from May 2024 through April 2025,
small, medium, and large firms report different combinations of employment
growth, formal training, infrastructure disruption, bank-financed investment,
and perceived constraints.

The safe interpretation is:

> **Firm capacity is a bundle of scale, training, infrastructure exposure,
> finance, and institutional constraint. A single “firm readiness” or AI
> adoption number would erase the structure that determines who can actually
> change work.**

This is a public baseline, not an AI finding. The separate 2026 AI-focused
follow-up is confirmed in the World Bank release catalog, but its respondent
microdata and questionnaire remain behind the authenticated portal.

## What the profile directly reports

| Surface | Small | Medium | Large | What it means | What it does not mean |
|---|---:|---:|---:|---|---|
| Average workers per establishment | 7.4 | 33.0 | 193.7 | Scale differs sharply across the size strata | Not a worker-level employment distribution or firm productivity estimate |
| Employment growth | 4.2% | 6.4% | 12.6% | The reported growth measure is higher for large establishments | Not causal growth, job quality, pay, or worker bargaining power |
| Firms offering formal training | 29.1% | 59.1% | 78.9% | Training capacity is strongly size-conditioned | Not training quality, worker access, completion, or skill gains |
| Firms experiencing electrical outages | 21.0% | 23.2% | 36.2% | Large establishments report more outage exposure | Not outage duration, lost output, local grid burden, or household incidence |
| Firms using banks to finance investment | 19.2% | 15.0% | 33.9% | Bank-financed investment is not monotonic across size | Not credit approval, cost of capital, or investment amount |

The profile also shows different reported “biggest obstacle” mixes. An
inadequately educated workforce is selected by 28.1% of small, 28.2% of
medium, and 19.6% of large establishments. Tax rates are selected by 22.3%,
16.3%, and 14.4%, respectively. Labor regulations are selected by 6.6%,
10.3%, and 22.8%. These are manager-selected perceptions, not a rank-order
measure of every constraint a firm experiences.

## Why this matters for the AI/work-control program

The public baseline changes the next AI question. It is no longer adequate to
ask only whether firms adopt a tool or whether a sector reports productivity.
The relevant sequence is:

```text
firm size and sector
  -> training and management capacity
  -> finance and infrastructure reliability
  -> tool access, implementation, and worker exposure
  -> task change, review, schedule, pay, error burden, and voice
  -> household room, retention/exit, and institutional response
```

The first three stages are partially visible in this public profile. The
profile does not identify AI use, implementation timing, employer permission,
monitoring, human review, worker discretion, or later household outcomes. The
2026 AI follow-up is therefore valuable precisely because it could add the
missing implementation layer—not because the 2024 profile can be relabeled as
AI evidence.

## Counterexamples the profile preserves

- Large firms report more formal training and higher reported employment
  growth, but they also report more electrical-outage exposure and a much
  higher share naming labor regulations as their biggest obstacle.
- Bank-financed investment is lowest in the medium stratum in the profile;
  larger scale does not translate into a monotonic bank-finance share.
- Small and medium firms are more likely than large firms to name an
  inadequately educated workforce as their biggest obstacle, while large firms
  more often name labor regulations. The constraint is not one universal
  “skills gap.”
- A training offer is not worker receipt, a reported employment-growth rate is
  not a good-job measure, and an outage report is not a local household bill.

## Evidence and uncertainty boundary

The country profile reports point values by size group. The public PDF does not
provide the complete standard-error, weighting, nonresponse, and common-universe
documentation needed to treat every size contrast as a precision-tested causal
comparison. Each indicator also has its own universe: training, outages, bank
finance, and biggest-obstacle responses are not interchangeable denominators.

The public indicator layer can support future bounded comparisons where the
indicator definition, standard error, observation count, and common survey
universe are exposed. The profile itself is sufficient for a descriptive firm
baseline, not for a pooled “capacity” score.

## Next test

When the US AI follow-up file is obtained, the first join should be by firm
size, sector, and the documented survey universe. Audit whether AI use,
function, integration, training, employment, sales, productivity, and costs
are measured for the same firms and whether standard errors and missingness are
available. Then compare implementation and work-control outcomes by size while
retaining a non-adopter or low-capacity counterexample.

Until that gate passes, this finding contributes firm capacity and constraint
context only.

## Sources and reproduction

- [US 2024 Enterprise Survey country profile](https://www.enterprisesurveys.org/content/dam/enterprisesurveys/documents/country/United-States-2024.pdf)
- [Machine-readable record](../../../records/us-world-bank-enterprise-survey-firm-capacity-size-2024.json)
- [WBES AI follow-up access recheck](../world-bank-wbes-ai-access-recheck-2026-09-14.md)
- [WBES data updates](https://www.enterprisesurveys.org/en/data/data-updates)
- [WBES public indicator/custom-query layer](https://www.enterprisesurveys.org/en/data/custom-query)

**Evidence status:** official public country-profile baseline; descriptive and
non-pooled; no AI-adoption, causal productivity, worker-control, household, or
geopolitical claim is promoted.
