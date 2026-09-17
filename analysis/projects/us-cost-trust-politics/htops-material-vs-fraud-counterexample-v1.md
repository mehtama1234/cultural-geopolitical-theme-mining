# HTOPS material pressure versus fraud/loss counterexample v1

**Status:** within-panel nonpooled counterexample; no new causal estimate
**Checked:** 2026-09-16
**Machine record:** [material-versus-fraud comparison](data/htops-material-vs-fraud-counterexample-2025.json)
**Fraud route:** [April-to-June fraud follow-up](htops-2025-fraud-followup-v1.md)
**Material route:** [HTOPS cross-lagged audit](data/htops-2025-cross-lagged-panel-audit.json)

## Purpose

The broad goal requires counterexamples to simple stories. The new fraud
follow-up could be misread as saying that any reported scam exposure produces
the same downstream household strain as general financial pressure. The
existing HTOPS material-pressure screen provides a within-panel comparator.

Both routes use the April-to-June 2025 linked HTOPS panel and April weights,
but they use different April group definitions and selected valid outcome
universes. They are compared as parallel aggregate screens, not rejoined at
the respondent-row level here.

## Results

| Route contrast | Food insufficiency | Unable to pay energy bill | Recent household job loss |
|---|---:|---:|---:|
| April expense difficulty vs not difficult | 12.3% vs 1.1% | 21.4% vs 2.2% | 11.7% vs 2.9% |
| April fraud exposure vs no exposure | 6.12% vs 9.37% | 10.66% vs 16.84% | 6.86% vs 9.22% |
| April exposure + money loss vs no exposure | 23.82% vs 9.37% | 43.81% vs 16.84% | 8.31% vs 9.22% |
| April money loss + report vs no exposure | 12.22% vs 9.37% | 44.86% vs 16.84% | 11.56% vs 9.22% |

The material-pressure route is positive across all three later material
outcomes. Fraud exposure alone is lower than the no-exposure comparator in
this linked sample, while exposure accompanied by reported money loss is
higher for food and energy. Job loss does not follow the same pattern.

## What the counterexample changes

This comparison weakens three tempting inferences:

1. A retrospective exposure report is not the same thing as realized loss.
2. Realized loss is not the same thing as general expense difficulty.
3. A higher later energy-bill hardship share does not imply a uniform later
   food or employment response.

The result supports a more precise broad-program route:

```text
condition or exposure
  -> realized loss or constraint
  -> distinct household outcome
```

The conversion step must be measured rather than inferred from an exposure
label. This is exactly the kind of distribution and counterexample discipline
needed before moving from consumer events to trust, legitimacy, or political
action.

## Limits

The April fraud questions refer to the prior 12 months, not a dated event. The
material-pressure exposure is also self-reported. Neither route observes the
actor, alternatives, effort, remedy, prior outcome, or reason for the June
response. Linked retention is selective, April weights are not documented as
attrition-adjusted longitudinal weights, and the loss/report group has only 51
respondents. No causal effect, trust change, recovery, switching, or exit is
claimed.

## Reproduction

```text
python3 scripts/synthesize_htops_material_fraud_counterexample.py
```

The synthesis reads the two committed aggregate JSON records and downloads
nothing.
