# Trend qualification review request

This is the human handoff for deciding whether each candidate remains held,
becomes a qualified external trend, becomes monitored, or is retired. It does
not authorize a company bridge or infer a failed gate as a pass.

## Required review fields

For each candidate, record evidence for source identity, comparability,
independence, persistence, counter-signal, falsifier, backtest, and decision
relevance. Record the exact artifact, reviewer, date, disposition, and next
review date. Missing evidence keeps the candidate held.

| Candidate | Current state | First review action | Required evidence | Decision | Reviewer / date |
| --- | --- | --- | --- | --- | --- |
| `candidate-formal-response-before-recovery` | held | Code formal response → implementation → receipt → durable access → exit stages across independent records | `candidate-qualification-matrix.json`, `falsification-review-queue.json`, `candidate-independence-adjudication-queue.json` | hold / qualify / monitor / retire | TBD |
| `candidate-time-financial-pressure-practical-room` | held | Preserve compatible time, cost, participation, and wellbeing units | `candidate-qualification-matrix.json`, `backtest-comparability-review.json`, `falsification-review-queue.json` | hold / qualify / monitor / retire | TBD |
| `candidate-digital-capability-control-trust` | held | Separate capability, delegation, trust, control, recourse, retention, and exit measures | `candidate-qualification-matrix.json`, `candidate-independence-adjudication-queue.json`, `falsification-review-queue.json` | hold / qualify / monitor / retire | TBD |
| `candidate-infrastructure-dependency-power` | held | Link capacity or ownership to operation, local burden, maintenance, and acceptance outcomes | `candidate-qualification-matrix.json`, `backtest-comparability-review.json`, `falsification-review-queue.json` | hold / qualify / monitor / retire | TBD |
| `candidate-us-food-insecurity-persistence` | monitored | Align USDA and Urban definitions while preserving the 2025 method break | `food-security-independence-review-packet.json`, `food-insecurity-temporal-holdout.json`, `candidate-qualification-matrix.json` | monitor / reverse / retire | TBD |

## Promotion rule

Promote only when every required rubric gate has evidence recorded. A later
release, a distinct host, or a plausible narrative is not enough by itself.
Keep counter-signals, uncertainty, unmatched cases, and publisher dependence
visible in the decision note.

The escalation path is `trend_challenger` → `lineage_reviewer` →
`program_sponsor`. Until sign-off is recorded in the machine-readable artifacts,
all held candidates remain excluded from company pilots.
