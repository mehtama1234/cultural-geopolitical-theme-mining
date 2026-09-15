# Worker/workplace event ledger v1

**Status:** acquisition and linkage specification · **Checked:** 2026-09-14
**Project:** AI, work, and control

## Purpose

The current program has worker/task adoption, sector mobility, union
representation, pay, household-resource, and infrastructure layers, but those
sources do not follow one worker or workplace through a tool or rule change.
This ledger specifies the missing common key needed to test the end-to-end
work/control claim.

The design must answer a narrower question:

> When a defined tool, AI system, benefit, schedule rule, or monitoring change
> reaches a worker or workplace, does it change paid time, discretion,
> correction burden, bargaining/voice, household room, health, or practical
> exit—and who captures or bears the resulting change?

This is a study design, not evidence that the full chain has already been
observed.

## Current partial population

NBER Working Paper 33795 can populate only a partial event row: randomized
individual access across 66 firms and 7,137 knowledge workers; tool use among
80% of treated workers in the second half of the six-month experiment; about
two fewer email hours per week among those users; and reduced outside-hours
work. It does not populate the downstream control fields.

| Ledger field | Current W33795 status | Still missing |
|---|---|---|
| `event` | Individual access to an AI tool integrated into existing email, meeting, and writing applications; six-month randomized field experiment | Employer rule change, team/workflow redesign, implementation date by workplace |
| `exposure` | Assignment and treated-user use are reported; conditional user result is distinguishable from assignment | Intensity beyond the reported user group, employer permission, training, monitoring, human review |
| `outcome` | Email time and outside-hours work changed; task quantity/composition did not detectably change | Total workload, schedule predictability, pay, health, error/correction time, care, household room |
| `voice` | Not observed in the abstracted result | Notice, consultation, grievance, appeal, correction, bargaining, retaliation concern |
| `exit_followup` | Not observed | Transfer, quit, tool refusal/removal, employer response, later trust or action |

The partial row is useful because it demonstrates the required distinction
between access, use, time, and control. It is not a completed worker-event
ledger or a general claim about AI at work.

## Event chain

```text
defined workplace/tool/rule event
  -> access, training, permission, monitoring, and task assignment
  -> hours, schedule control, pay, productivity, error/correction burden
  -> grievance, bargaining, health, household room, and care response
  -> stay, switch, quit, organizing, employer correction, or public response
  -> later security, meaning, trust, and power
```

The event must have a dated start, a defined exposure boundary, and a named
comparison or counterfactual. “AI-exposed occupation” or “industry adoption”
alone is not an event.

## Required tables and keys

| Table | Minimum fields | Why it is required |
|---|---|---|
| `workplace` | stable workplace ID, firm/parent ID, establishment size, industry, place, ownership, union/works-council status, provider/vendor | Separates employer decision from worker exposure and firm scale |
| `event` | event ID, event type, announcement/start/implementation dates, affected tasks, scope, opt-out/alternative route, rule owner | Establishes timing and what actually changed |
| `worker` | consented worker ID, occupation/tasks, tenure, demographics, pay basis, hours, contract status, household link | Preserves subgroup and selection differences without inferring them from occupation |
| `exposure` | worker-event link, access date, actual use, frequency/intensity, employer permission, training, monitoring, human review, error responsibility | Distinguishes availability, use, and control |
| `outcome` | pay, hours, schedule predictability, task mix, productivity, error/correction time, health, absence, care/time, job search, quit/stay, protected outcome, sacrificed outcome | Separates material, time, health, control, and distributional endpoints |
| `voice` | notice, consultation, grievance, representative contact, appeal, correction, bargaining, retaliation concern, resolution date | Measures institutional route rather than assuming control from adoption |
| `household` | monthly resources, debt/liquidity, care duties, housing/utility/food pressure, partner work, recovery | Tests whether workplace changes alter household room or merely relocate cost |
| `exit_followup` | application, transfer, quit, employer switch, tool removal, provider switch, organizing/action, later trust/fairness | Captures practical exit and response rather than treating non-use as choice |

Each linked measure must retain its original unit, reference period, missingness
rule, denominator, weight, and variance method. Worker-reported, employer-
reported, administrative, and household fields must not be silently merged.
For each outcome window, record what the worker or household protected and
what was sacrificed, delayed, transferred, or placed at risk; unknown is a
valid value when the design does not measure either field.

## Source roles and acquisition gates

| Source family already in the atlas | Role in this design | What it cannot supply alone |
|---|---|---|
| NBER W35677 worker/task adoption | Task-level exposure and within-work adoption variation | Employer permission, monitoring, pay, bargaining, health, or household effects |
| NBER W33795 randomized field experiment | Individual access/use and telemetry-measured email/outside-hours time in 66 firms | Whether saved time remained with workers, changed control, pay, health, voice, household room, or exit |
| BLS JOLTS/CES/CPS and union layers | Sector mobility, pay, representation, hours, and labor-market context | Same-worker event timing, discretion, grievance, or tool exposure |
| SIPP and Federal Reserve SHED | Household resources, debt, liquidity, work, care, and adaptation | Workplace event identity, employer rule, or individual attribution |
| BEA/BIS firm and industry studies | Output, prices, labor/capital composition, and firm productivity context | Worker incidence, distribution of gains, or practical control |
| OECD/ILO workplace governance studies | Monitoring, algorithmic-management, consultation, and worker-risk instruments | US longitudinal worker outcomes or verified remedy |
| OFR, World Bank, IMF, and infrastructure records | Public capacity, complements, modeled distribution, finance, and dependence context | Worker-level exposure, local household incidence, or state leverage |

The first acquisition gate is a worker or workplace panel with a stable key and
a dated event. The second is employer permission/monitoring and task-level
exposure. The third is a household or linked financial follow-up. If a source
fails a gate, it remains context and must not be promoted to a causal arrow.

## Comparison and counterexample structure

Retain at least four groups:

1. exposed workers with actual use;
2. exposed workers with access but no use or opt-out;
3. comparable workers/workplaces without the event; and
4. workers whose event was reversed, delayed, or paired with effective human
   support.

The required counterexample is a case where productivity or tool access rises
without reduced discretion, bargaining room, health, or household security. A
second is a case where adoption is low because task fit or privacy makes
non-use rational, not because capability is absent. A third is a case where a
worker stays because the job improved, not because exit was impossible.

## Estimation and interpretation rules

- Pre-specify event time, treatment intensity, comparison group, and outcomes;
  do not substitute occupation-level exposure for individual treatment.
- Report worker and workplace denominators separately; do not repeat household
  fields as if they were independent worker observations.
- Preserve survey weights, replicate-weight or cluster-variance methods, and
  disclose when a source has no design-based uncertainty.
- Separate short-run productivity from pay, hours, discretion, error burden,
  health, and household security.
- Treat a quit as an observed transition, not evidence of improved opportunity;
  treat staying as neither satisfaction nor constraint without a reason field.
- Stop the arrow before trust, culture, politics, or geopolitical power unless
  attribution and later action are measured after the defined event.

## Durable output contract

A completed pass should produce:

- a de-identified event ledger with row-level provenance;
- a worker/workplace flow table showing inclusion and missingness at every
  stage;
- subgroup and counterexample estimates with uncertainty;
- a source-role matrix distinguishing direct outcome evidence from context;
- a detailed finding stating which arrows are observed, inferred, or open; and
- a reproducible HTML page linked from the program dashboard.

Until that acquisition occurs, the current NBER, BLS, SIPP, Federal Reserve,
BEA, BIS, OECD, ILO, OFR, World Bank, and IMF layers remain valuable but
non-pooled evidence stages.
