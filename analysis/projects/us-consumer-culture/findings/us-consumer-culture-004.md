# Finding 004: Material pressure predicts later option-search more clearly than AI use or political confidence

**Status:** bounded same-respondent HTOPS cross-lag finding  
**Checked:** 2026-09-19  
**Scope:** April 2025 expense difficulty carried to June 2025 search, AI-use,
and Congress-confidence fields; descriptive, not causal

## The finding

Among 6,564 respondents linked by `SCRAMID`, people reporting expense
difficulty in April were more likely than respondents reporting no difficulty to
report targeted online searches in June. The same time-ordered contrast was
much weaker for broad AI use and high confidence in Congress.

| June outcome | April expense difficulty | April expenses not difficult | Difference |
|---|---:|---:|---:|
| Job search | 40.6% (1.1) | 21.8% (0.7) | +18.8 pp |
| Food search | 25.2% (0.8) | 16.6% (0.4) | +8.7 pp |
| Public-benefit search | 19.6% (0.8) | 11.1% (0.3) | +8.5 pp |
| Credit search | 20.3% (0.7) | 11.4% (0.5) | +8.9 pp |
| Housing search | 18.1% (0.6) | 13.3% (0.6) | +4.8 pp |
| Medical search | 17.0% (0.7) | 10.7% (0.3) | +6.3 pp |
| Any AI use | 53.9% (1.0) | 58.5% (0.8) | −4.6 pp |
| High confidence in Congress | 17.2% (0.7) | 16.8% (0.5) | +0.3 pp |

Parentheses are successive-difference replicate standard errors in percentage
points. The estimates use April `PWEIGHT` and its 80 replicate weights, with
valid linked respondent counts of 2,589 in the difficulty group and 3,965 in
the no-difficulty group.

## What this adds

The stronger interpretation is not that financially pressured households “use
more technology.” It is that pressure appears to redirect attention toward
concrete option searches—work, food, benefits, credit, housing, and medical
help—across a two-month window. Broad AI use is not the same behavior as
material navigation, and political confidence barely separates the two
baseline groups in this screen.

This is an early option-building signal. It does not show that the search found
a provider, job, benefit, affordable home, credit line, or remedy. It also does
not show whether the respondent made the search, whether the result was usable,
or whether the later household condition improved.

## Interpretation boundary

- April expense difficulty is self-reported and does not identify a dated bill,
  price change, responsible actor, or amount owed.
- April weights and replicate weights are not documented here as
  attrition-adjusted longitudinal weights.
- The June fields are reported search and use outcomes, not clickstream,
  result-quality, application, approval, payment, or completion records.
- The contrasts are descriptive associations, not a causal effect of expense
  difficulty.
- Search is effort and navigation, not a completed alternative, remedy,
  recovery, switching, or exit.
- High Congress confidence is an institution-specific judgment, not generalized
  trust or political action.

## End-to-end implication

The observed route is:

```text
April material pressure
  -> June targeted option-search
  -> [open] result quality, chosen route, cost, completion, remedy, and later security
```

The next decisive source would link a search or help-seeking episode to the
result encountered, time and money spent, application or transaction outcome,
institutional response, and later recovery or exit. Until then, the result
should be read as constrained navigation—not successful adaptation.

## Reproduction and source boundary

The compact machine result is [the cross-lag JSON](../data/htops-2025-material-search-cross-lag-v1.json).
The reproduction script is
[`build_htops_2025_material_search_cross_lag.py`](../../../../scripts/build_htops_2025_material_search_cross_lag.py).
The source files were already retained locally under `/tmp/htops-2504/` and
`/tmp/htops-2506/`; no new download was performed and no raw respondent file
was copied into Git.

**Evidence status:** same-respondent, two-wave descriptive follow-up with
replicate-weight uncertainty; no causal, remedy, recovery, trust, or exit
claim.
