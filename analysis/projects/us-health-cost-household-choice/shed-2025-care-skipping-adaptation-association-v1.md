# SHED 2025 care foregoing is associated with household financial adaptation

**Checked:** 2026-09-15  
**Status:** weighted same-respondent cross-sectional association; no causal claim  
**Machine record:** [care-skipping/adaptation association](data/us-shed-2025-care-skipping-adaptation-association.json)

## Result

The 2025 SHED microdata allow a same-respondent cross-tab between cost-related
care foregoing and financial outcomes. Respondents who answered all five
care-foregoing fields (`E1_a`–`E1_e`) were classified as reporting any care
skipped when at least one field was “Yes.” Outcomes were then compared using
the single-year SHED analysis weight.

| Outcome reported in the same respondent record | Any care skipped because of cost | No care skipped because of cost |
|---|---:|---:|
| Current medical debt | 42.18% | 10.03% |
| Unexpected major medical expense | 36.03% | 16.17% |
| Three-month emergency funds | 31.45% | 62.84% |
| Used less or stopped products | 82.76% | 51.73% |
| Reduced savings | 64.05% | 33.07% |
| Increased borrowing | 34.03% | 9.64% |
| Delayed a major purchase | 74.31% | 35.64% |
| Worked more or got another job | 32.99% | 11.52% |

The complete care-foregoing universe contains 12,934 respondents. The weighted
share reporting any cost-related care foregoing is 25.72%; the no-foregoing
group is 74.29%. Outcome denominators vary because the adaptation questions
have their own valid-response universes; the machine record preserves each
denominator and row count.

## What this adds to the end-to-end chain

```text
financial constraint or need
  -> care delayed or forgone because of cost
  -> concurrent debt, borrowing, reduced savings, delayed purchases,
     reduced consumption, or additional work
```

This is the first same-respondent bridge in the lane from reported care choice
to household financial adaptation. It is stronger than placing SHED care
foregoing beside a separate adaptation survey because the two stages are
observed in the same respondent record. It still does not identify the
episode that connects them.

The association is also multidirectional. Medical debt or a major expense may
contribute to care foregoing; prior financial scarcity may produce both; poor
health may increase both medical need and financial pressure; and the same
unmeasured access or coverage constraint may affect all outcomes. The result
therefore establishes co-occurrence and distribution, not that skipping care
caused borrowing or that debt caused skipping care.

## Boundaries

The care questions ask about the prior 12 months, while medical debt is
current and the adaptation questions refer to price-related actions over the
prior 12 months. No bill date, clinical condition, exact price, insurance
plan, alternative, treatment consequence, or household event sequence is
available in this cross-tab. “Worked more” does not identify hours or whether
the work offset medical cost; “reduced savings” does not identify the
protected need; and “medical debt” may concern the respondent or a family
member.

The comparison is weighted but does not include replicate-weight standard
errors in this pass. It is not a panel estimate, even though SHED separately
contains a 2024–2025 recontact panel. A necessary counterexample is a person
who skipped care but had stable savings and no debt, or a person with medical
debt who obtained all needed care through insurance, family help, public
coverage, or payment arrangements.

## Expense amount is observed, but not as a bill-to-choice sequence

The 2025 file also records an amount band for unexpected major medical
expenses (`E12_a`). Among respondents reporting any cost-related care
foregoing, the weighted distribution among the 1,657 nonmissing amount
responses was: $1–$499 **13.76%**, $500–$999 **17.82%**, $1,000–$1,999
**21.03%**, $2,000–$4,999 **24.25%**, and $5,000 or more **15.81%**; **7.33%**
selected “Don’t know.” Among respondents reporting no care foregoing, the
corresponding 1,203-response distribution was $1–$499 **18.99%**, $500–$999
**22.66%**, $1,000–$1,999 **17.19%**, $2,000–$4,999 **20.27%**, and $5,000 or
more **13.35%**, with **7.54%** selecting “Don’t know.”

These amount bands sharpen the payment mechanism but do not identify the
amount owed for the care that was skipped. They apply only to respondents who
reported an unexpected major medical expense and share the same prior-year
recall frame; they cannot be interpreted as the causal price of foregoing.

## Next decisive join

The next step is to separate timing and mechanism: identify whether the
respondent had an unexpected medical expense and its amount band, which care
type was forgone, whether insurance or outside help was available, and which
financial response was contemporaneous. The strongest eventual design would retain a dated need,
coverage and alternatives, amount owed, care decision, household trade-off,
and follow-up health/work/debt outcome in one unit. Until then, this result
should be promoted as a same-respondent association, not an end-to-end causal
episode.

## Reproduction

```text
python3 scripts/analyze_shed_care_skipping_adaptation.py \
  --input /tmp/cgtm-shed/shed2025.zip \
  --output analysis/projects/us-health-cost-household-choice/data/us-shed-2025-care-skipping-adaptation-association.json
```

## Source

The variables and response universes are documented in the Federal Reserve
[2025 SHED codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2025codebook.pdf). The public data archive and release notes are maintained on the Federal Reserve [SHED data page](https://www.federalreserve.gov/consumerscommunities/shed_data.htm). The published care-foregoing estimates are summarized in the Board’s [2025 economic-well-being report](https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-economic-hardships.htm).
