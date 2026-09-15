# Finding 064: Firm capacity, AI adoption, and labor mobility are different gates to worker control

**Status:** provisional non-pooled firm-to-worker comparison · **Checked:** 2026-09-14

## The bounded finding

The latest firm baseline makes the AI/work question more precise. Four public
evidence surfaces now sit beside one another:

1. The World Bank US Enterprise Survey describes establishment size,
   training, employment growth, outages, finance, and manager-selected
   constraints.
2. NBER measures whether workers doing similar tasks report using generative
   AI and shows that exposure scores explain only part of adoption variation.
3. BLS measures formal union membership/representation, which is an
   institutional voice condition but not a direct control outcome.
4. BLS JOLTS measures aggregate establishment openings and quits, which is
   labor-market context but not individual mobility or AI exposure.

The safe synthesis is:

> **Capacity, adoption, representation, and mobility are successive gates—not
> interchangeable measures of worker control. A firm can have training and
> growth without worker discretion; a worker can have access without using a
> tool; a represented workplace can still carry burden; and a cooling quits
> rate can reflect fewer outside options rather than satisfied retention.**

## Evidence surfaces kept separate

| Gate | Direct evidence | Unit and denominator | Boundary |
|---|---|---|---|
| Firm capacity | WBES: training is 29.1%, 59.1%, and 78.9% across small, medium, and large firms; employment growth is 4.2%, 6.4%, and 12.6% | 2,589 US establishments; size-conditioned profile | No AI use, worker receipt, job quality, or causal growth effect |
| Infrastructure exposure | WBES: electrical outages are reported by 21.0%, 23.2%, and 36.2% across the same size strata | Size-conditioned establishment indicators | No outage duration, local load, household burden, or resilience result |
| Task adoption | NBER: fewer than half adopt within most occupations/tasks; exposure explains 5%–53% across occupations and 7%–44% across tasks | 55,634 worker-task observations; related 13,920-worker survey pool | No employer permission, implementation date, monitoring, pay, or discretion |
| Formal voice | BLS: union membership is 9.9% in 2024 and 10.0% in 2025; representation is 11.1% and 11.2% | Employed wage/salary workers; 2025 excludes October | No grievance success, consultation, bargaining outcome, or control |
| Mobility context | BLS: January–July 2026 openings mean 4.3714%, quits mean 1.9571%; July preliminary | Seven monthly total-nonfarm establishment rates | No unique worker transitions, motivations, job quality, or AI attribution |

These figures are not a composite score. They differ in unit, universe,
reference period, method, and uncertainty. The WBES size profile is an
establishment survey; NBER is worker/task evidence; union rates use a CPS
worker denominator; JOLTS is an establishment rate.

## The chain under test

```text
firm size, finance, training, infrastructure, and constraints
  -> tool access, task fit, implementation, and employer rules
  -> worker use, pace, review, schedule, pay, errors, and discretion
  -> voice, correction, bargaining, health, household room, and exit
  -> firm response, public regulation, political meaning, and state capacity
```

The first line is now better conditioned. The middle line is not observed in
one common unit. That distinction prevents three common errors:

- calling a firm’s training offer worker skill gain;
- calling worker-reported AI use employer implementation or productivity; and
- calling a lower quits rate improved worker power.

## What changes in the interpretation

### Scale can supply complements and constraints together

Large establishments report more formal training and higher employment growth,
but also more electrical-outage exposure and a much higher share naming labor
regulations as their biggest obstacle. Scale is therefore not a simple proxy
for capability, resilience, or worker benefit.

### Adoption is not implementation

NBER’s within-task variation shows why occupation-level exposure cannot be
treated as worker treatment. The residual can reflect access, employer rules,
training, task fit, privacy, or reporting. The missing event is when a defined
workplace actually changes a tool, rule, workflow, or monitoring practice.

### Voice and mobility are not the same control surface

Formal representation supplies a possible route for notice, correction, and
bargaining, but the BLS rate does not observe whether that route worked. A
worker may stay because a job is good, because switching is costly, or because
outside options have narrowed. JOLTS cannot distinguish those states.

## Counterexamples retained

- High training and employment growth can coexist with high outage exposure.
- A worker can be exposed to a capable task and still not adopt the tool.
- A large firm can report more labor-regulation concern than a small firm while
  also reporting more training.
- Representation can exist without observed grievance resolution or discretion.
- A lower quits rate can mean normalization or constrained exit, not improved
  workplace quality.

## Next decisive test

The next acquisition is a dated workplace implementation panel with a stable
workplace or worker key. It should record:

1. firm size, sector, ownership, training, finance, infrastructure, and tool;
2. announcement and implementation dates, permission, monitoring, and actual
   exposure;
3. task mix, pace, hours, pay, schedule control, errors, and correction time;
4. notice, consultation, representative contact, appeal, and remedy;
5. household time, care, liquidity, and health response; and
6. switching, exit, organizing, public regulation, or later institutional
   response.

The authenticated World Bank AI follow-up could populate the firm-side portion
of this design, but it cannot replace the worker/workplace event key. Until
both exist, this remains a bounded architecture rather than an end-to-end
worker-control estimate.

## Sources and reproduction

- [Machine-readable record](../../../records/us-firm-capacity-ai-adoption-worker-control-crosssource-2024-2026.json)
- [WBES US firm-capacity baseline](ai-work-control-063.md)
- [NBER task-level adoption record](../../../records/us-nber-task-level-genai-adoption-2026.json)
- [BLS union representation record](../../../records/us-bls-union-representation-2024-2025.json)
- [BLS 2026 JOLTS mobility record](../../../records/us-bls-jolts-national-mobility-2026-ytd.json)
- [WBES AI access recheck](../world-bank-wbes-ai-access-recheck-2026-09-14.md)

**Evidence status:** bounded non-pooled firm-to-worker architecture; no causal
AI, worker-control, household, political, or geopolitical effect is promoted.
