# Backtest design review request

This is the human handoff for the five candidate backtest designs. It does not
score a forecast, qualify a trend, establish causality, or authorize a company
bridge. A candidate remains held until the reviewer records a compatible design
or explicitly retires the comparison.

## Required review fields

For each candidate, record:

- construction period and holdout period;
- one common population, geography, unit, and denominator;
- exact outcome definition and source vintage;
- uncertainty or variance treatment;
- independent publisher/upstream disposition;
- falsifier and counter-signal;
- missingness and unmatched-case policy;
- pre-registration date and reviewer sign-off; and
- decision: `ready`, `redesign`, or `retire`.

Do not compute a score when measures are unlike, the realized outcome is
missing, or uncertainty cannot be carried. A descriptive holdout is not a
predictive backtest.

## Candidate review table

| Candidate | Current blocker | Reviewer | Construction / holdout | Common unit / denominator | Outcome / uncertainty | Falsifier / counter-signal | Decision | Sign-off |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `candidate-formal-response-before-recovery` | geography, denominator, and measure harmonization | TBD | TBD | TBD | TBD | TBD | redesign | TBD |
| `candidate-time-financial-pressure-practical-room` | geography, denominator, and measure harmonization | TBD | TBD | TBD | TBD | TBD | redesign | TBD |
| `candidate-digital-capability-control-trust` | geography, denominator, and measure harmonization | TBD | TBD | TBD | TBD | redesign | TBD |
| `candidate-infrastructure-dependency-power` | geography, denominator, and measure harmonization | TBD | TBD | TBD | TBD | redesign | TBD |
| `candidate-us-food-insecurity-persistence` | geography, denominator, measure, and outcome harmonization | TBD | TBD | TBD | TBD | redesign | TBD |

## Acceptance evidence

- Completed review row linked to the exact source artifacts
- Independent lineage disposition recorded
- Holdout and falsifier registered before outcome inspection
- Uncertainty and missingness treatment documented
- Second reviewer sign-off recorded
- Backtest register updated without partial-year scoring

The escalation path is `trend_challenger` → `lineage_reviewer` →
`program_sponsor`. Until accepted, the candidate remains held and no internal
company data may be connected.
