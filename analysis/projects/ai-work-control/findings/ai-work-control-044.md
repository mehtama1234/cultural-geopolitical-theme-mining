# Finding 044: Firm AI expectations are not realized worker outcomes

**Status:** provisional NBER firm-side evidence layer · **Checked:** 2026-09-14

## The bounded finding

NBER Working Paper 34836 surveys nearly 6,000 senior business executives at
firms in the United States, United Kingdom, Germany, and Australia. It puts
three different clocks in the same instrument:

| Clock | Reported result | What it measures |
|---|---|---|
| Current use | 69% of firms actively use AI; more than two thirds of executives regularly use it, averaging 1.5 hours per week | Firm and executive adoption/reach |
| Retrospective realization | Nine in ten executives report no own-firm impact on employment or productivity over the prior three years | Executive-reported realized impact |
| Forward expectation | Over the next three years, executives expect +1.4% productivity, +0.8% output, and -0.7% employment at their firms; employees expect +0.5% employment | Anticipated firm change and an expectation gap |

The defensible synthesis is: **AI is already ordinary at the firm surface, but
the survey reports limited realized own-firm effects alongside sizable forward
expectations—and employer and employee expectations point in different
directions.** This is a bridge between adoption and institutional change, but
it is not evidence that those expected changes occurred.

## Why this layer cannot be pooled with the worker experiment

| Layer | Unit | Direct result | Still missing |
|---|---|---|---|
| NBER W34836 | Senior executives/firms across four countries | Current use, retrospective firm effects, and forward expectations | Worker-level exposure, implementation rules, pay, hours, voice, health, or household effects |
| NBER W33795 | 7,137 knowledge workers across 66 firms | Treated users spent about two fewer hours per week on email and outside-hours work decreased | Whether saved time accrued to workers, changed total workload, pay, health, or bargaining |
| NBER W35677 | Worker-task observations | AI adoption varies within occupations and tasks | Employer permission, monitoring, evaluation, correction, and exit |

The firm survey is broader and forward-looking; the field experiment is narrower
and behaviorally observed; the task survey is adoption-oriented. They do not
share a sufficient firm-worker-task-time key for a single causal estimate.

## Mechanism under test

```text
firm adoption and executive expectation
  -> implementation, permission, training, monitoring, and task redesign
  -> worker time, pace, discretion, evaluation, pay, and correction rights
  -> household room, trust, collective response, and political judgment
```

W34836 populates the first node and a forward-looking expectation node. W33795
populates one observed worker-time transition. The implementation and
appropriation stages remain open: a productivity gain may become shorter hours,
more output, tighter monitoring, staffing reduction, higher margins, or some
combination.

## Counterexamples kept visible

- A 69% firm-use rate does not mean most workers have access, training, or
  permission to use the same tools.
- Nine in ten reporting no past impact may indicate genuine limited effects,
  measurement lag, shallow use, or executives' inability to observe dispersed
  worker-level changes.
- Expected employment reduction is not realized displacement; expected
  employment growth from employees is not realized job creation.
- Expected productivity and output gains do not identify who receives the gain,
  who bears implementation risk, or whether work becomes more meaningful or
  more controlled.
- The four-country executive frame should not be relabeled as a US-only result;
  country institutions, labor markets, and firm composition may differ.

## Next end-to-end test

The next acquisition should link the firm expectation to a named workplace and
worker event, preserving respondent role and timing. At minimum it should
capture:

1. the firm's stated use case and expected outcome;
2. actual tool access, training, permission, monitoring, and human review;
3. task quantity/composition, hours, pace, pay, staffing, and correction rights;
4. worker and employer expectations measured before and after implementation;
5. representation, grievance, switching, retention, and exit; and
6. household time/security and later trust or political response.

The decisive comparison is not simply adopter versus non-adopter. It is
expected productivity gain × realized worker control × appropriation of saved
capacity, with high-expectation/low-realization and low-expectation/high-change
countercells retained.

## Reproduction and sources

- [Firm AI expectations record](../../../records/us-nber-firm-ai-expectations-2026.json)
- [NBER Working Paper 34836: Firm Data on AI](https://www.nber.org/papers/w34836)
- [Worker/workplace event-ledger specification](../worker-workplace-event-ledger-v1.md)
- [AI adoption and worker-control record](../../../records/us-ai-work-adoption-control-2024-2026.json)

**Evidence status:** firm/executive survey layer; no realized employment,
productivity, worker-control, household, cultural, political, or geopolitical
effect is claimed.
