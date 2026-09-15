# Finding 057: AI utilization and modeled output signals do not yet identify worker gain or control

**Status:** provisional non-pooled AI/work-power bridge · **Checked:** 2026-09-14

## The bounded finding

The atlas now places five evidence surfaces in sequence:

1. NBER measures worker-reported adoption and shows that exposure scores explain only part of variation among occupations and tasks.
2. BEA links state-industry utilization to employment and output in descriptive associations, while separately identifying the limits of national-account measurement.
3. BEA industry-account work provides early exploratory input and labor-share estimates, not a direct AI line item or household pass-through measure.
4. NBER executives report current use, limited retrospective effects, and divergent future expectations.
5. BLS JOLTS provides aggregate labor-market mobility context, but not AI exposure or worker control.

The defensible synthesis is: **AI is becoming measurable in tasks, firms, and industry accounts, but utilization, modeled output association, expected restructuring, and aggregate labor mobility remain distinct from realized worker gain, bargaining power, or household security.**

## Evidence surfaces kept separate

| Stage | Direct evidence | Unit | What remains open |
|---|---|---|---|
| Task adoption | NBER reports fewer than half adopting within most occupations/tasks; exposure explains 5–53% of adoption variation across occupations and 7–44% across tasks; compared task measures correlate below 0.4. | Worker survey, task, and platform-index measures | Employer permission, implementation, pay, time ownership, and workplace consequence |
| State-industry association | BEA reports 0.4–0.6% employment and 0.1–0.2% real-output differences per one-point higher frequent-user share in a descriptive state-industry design. | 75,292 Gallup worker observations linked to state-industry outcomes | Causal direction, cell precision, distribution, and who receives output or employment gains |
| Industry-account measurement | BEA notes no direct AI line item in current national accounts and presents early exploratory labor/input contributions across 1,586 industry-year observations. | Industry-year production accounts | Realized firm decisions, price pass-through, worker incidence, and unmeasured AI costs |
| Firm expectations | NBER reports 69% active use and 90% no past three-year employment/productivity impact, alongside expected next-three-year productivity of +1.4% and employer employment of −0.7%. | Senior executives across four countries | Realized implementation, occupation exposure, pay, hours, discretion, and representation |
| Labor mobility context | JOLTS openings fell from a 6.85% 2022 annual mean to 4.275% in 2025; the January–July 2026 mean is 4.3714% and quits 1.9571%, with July preliminary. | Total nonfarm establishment rates | Whether the movement reflects AI, normalization, demand, composition, or worker welfare |

These objects are intentionally not pooled. A task adoption share, state-industry association, industry-account decomposition, executive expectation, and establishment rate do not share a denominator or estimand.

## The chain under test

```text
tool access and task fit
  -> adoption, output, time, skill, monitoring, and managerial discretion
  -> pay, hours, schedule control, health, job continuity, and appeal
  -> representation, bargaining, exit, collective action, and household room
  -> firm strategy, public regulation, institutional legitimacy, and state capacity
```

The current evidence reaches the first node and selected macro/firm indicators. It does not close the workplace-control or household-incidence nodes.

## What the comparison changes

### Output association is not distribution

The BEA state-industry association is useful for identifying where utilization and outcomes co-vary. It cannot establish that AI caused the difference or that workers received the resulting output. The early industry-account estimates add measurement discipline: the national accounts do not yet contain a direct AI line item.

### Expectations are not implementation

The NBER executive survey makes the time distinction visible: firms can report little realized effect over the prior three years while expecting productivity and employment changes over the next three. That is a signal for a realization watch, not evidence of future job loss or worker empowerment.

### Aggregate mobility is a context, not an AI endpoint

JOLTS shows that openings and quits cooled after 2022; the January–July 2026 partial-year refresh remains in that cool range, but July is preliminary. Because its denominator is establishments and it contains no AI exposure, it cannot identify whether workers became less mobile because of technology, weaker demand, changing preferences, or other composition. The partial-year mean must not be treated as a completed annual trend.

## Counterexamples kept visible

- High task adoption can coexist with unchanged pay, intensified targets, or employer capture of the gain.
- A positive state-industry association can reflect managerial quality, demand, complementary capital, or reverse causality.
- A lower labor-share contribution does not identify a worker-level wage loss or a household price effect.
- Low retrospective executive impact can coexist with a future reorganization that never materializes.
- Falling quits can reflect normalization rather than reduced bargaining power or AI displacement.
- A task-level productivity gain can narrow a performance gap without increasing worker discretion or representation.

## Next decisive test

Select one workplace technology or implementation rule and build a same-workplace/event panel containing:

1. implementation date, tool function, worker exposure, training, and monitoring;
2. output, total hours, pace, pay, scheduling, errors, health, and job continuity;
3. discretion, data visibility, correction, appeal, and refusal rights;
4. representation, consultation, bargaining, or alternative voice route;
5. household-time and financial consequences; and
6. switching, exit, collective action, firm response, or regulatory remedy.

Until that common unit is observed, the atlas should not translate AI utilization into “AI job loss,” “worker empowerment,” or “AI sovereignty.”

## Sources and reproduction

- [Machine-readable cross-source record](../../../records/us-ai-utilization-output-mobility-control-crosssource-2025-2026.json)
- [NBER task-level adoption record](../../../records/us-nber-task-level-genai-adoption-2026.json)
- [BEA AI economic-account record](../../../records/us-bea-ai-economic-accounts-utilization-costs-2026.json)
- [NBER firm-expectations record](../../../records/us-nber-firm-ai-expectations-2026.json)
- [BLS JOLTS national mobility record](../../../records/us-bls-jolts-national-mobility-2020-2025.json)
- [BLS JOLTS January–July 2026 refresh](../../../records/us-bls-jolts-national-mobility-2026-ytd.json)

**Evidence status:** bounded measurement-to-labor-market comparison; realized workplace control, worker incidence, household effects, political response, and geopolitical leverage remain unestablished.
