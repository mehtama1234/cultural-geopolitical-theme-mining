# Worker adoption is widespread across tasks but shallow within similar work

## The finding

NBER Working Paper 35677 links generative-AI use to detailed occupations and
tasks in a nationally representative worker survey. The pooled occupation
comparison uses 13,920 employed respondents ages 18–64 across four waves; the
worker-task regressions use 55,634 person-task observations. The paper reports
that AI is used across many occupations and tasks, yet within most of them
fewer than half of workers adopt. Exposure scores explain some, but far from
all, of the variation in adoption.

The defensible finding is narrower: **occupation-level exposure is not a worker-
level adoption measure. Similar work can contain materially different access,
use, and future control pathways.**

## Direct evidence

The paper constructs task-level adoption indexes from worker-reported use and
distinguishes them from platform chat-log activity. The abstract describes
widespread but shallow adoption and substantial variation among workers doing
very similar work. It also reports that chat-log measures tend to classify chats
into generic activities spanning many occupations.

The source-specific [NBER layer](../nber-w35677-task-level-adoption-layer-v1.md)
and [machine-readable record](../../../records/us-nber-task-level-genai-adoption-2026.json)
preserve the sample denominators, task-cell thresholds, method, and working-
paper limits.

## Mechanism

```text
occupation/task exposure
  -> access, permission, training, and perceived usefulness
  -> uneven worker adoption within similar work
  -> different task allocation and evaluation experiences
  -> possible differences in discretion, skill recognition, pay, and voice
```

Only the first two stages are directly measured here. The remaining stages are
not implied by adoption. The paper's individual fixed-effects comparison is
consistent with meaningful worker-level variation, but it does not identify
whether that variation comes from access, learning, workplace rules, task fit,
or worker preferences.

## Cultural and political meaning

An “AI-exposed job” can become a public category even when workers in that job
do not encounter the same tool or rule. That gap can shape whether AI is
experienced as opportunity, surveillance, deskilling, or irrelevant software.
It may also shape whose testimony is visible in workplace and political debate.
Those are hypotheses for linked worker and institutional evidence, not results
of this survey abstract.

## Counterinterpretations

- Shallow adoption may reflect task fit, quality concerns, privacy, or employer
  limits rather than unequal capability.
- Worker reports may miss unreported, informal, or employer-mediated use.
- Chat logs may over-generalize generic activity, while surveys may undercount
  platform use.
- Similar adoption does not establish similar training, monitoring, autonomy,
  or bargaining power.
- The RPS is an online survey calibrated to key CPS demographics, not a simple
  random sample; the paper remains a working paper.

## What would change the finding

It would weaken if exposure almost completely explained adoption once access
and workplace rules were included, or if the within-task variation were mainly
a coding artifact. It would strengthen if within-task adoption differences
persisted after comparable access, training, employer policy, and worker
characteristics were measured.

## Next test

Version the acquired public task-level index files and obtain weighted subgroup estimates
where supported; then match adoption cells to workplace measures of training,
monitoring, autonomy, correction, pay, promotion, health, and worker voice.
Compare the worker survey with field experiments and firm disclosures without
pooling their units.

**Evidence status:** reported full-paper descriptive adoption pattern; workplace,
household, cultural, political, and geopolitical consequences remain open.

## Source

[NBER Working Paper 35677](https://www.nber.org/papers/w35677).
