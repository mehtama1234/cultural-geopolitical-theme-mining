# NBER W35677 task-level generative-AI adoption layer v1

**Checked:** 2026-09-13  
**Source:** [What Work Does Generative AI Do?](https://www.nber.org/papers/w35677), NBER Working Paper 35677  
**Unit:** worker, detailed occupation, and task relationship  
**Status:** full-paper and public-index descriptive audit completed; subgroup and workplace-outcome follow-up remains open

The [public index acquisition note](nber-w35677-index-acquisition-v1.md)
records the DWA, IWA, and BWA sheets, retrieval hashes, rate construction, and
the O*NET/citation metadata gate. The [O*NET release gate](onet-release-metadata-gate-v1.md)
now records the official 31.0 release boundary and completed input acquisition;
a provisional DWA/IWA
label-match and BWA prefix-aggregation artifact is available, while semantic
equivalence remains unverified. The index release is now also
represented in the shared trend registry.

## Why this source matters

The program needs to distinguish three things that are often collapsed into
one headline: what a task can technically be exposed to, whether a worker
actually adopts a tool, and whether the employer changes the work relationship.
W35677 supplies the middle layer. It links worker-reported generative-AI use to
detailed occupations and tasks and warns that similar work does not imply
similar adoption.

## Direct evidence

The pooled occupation comparison contains 13,920 employed RPS respondents ages
18–64 across four waves. The worker-task regressions use 55,634 person-task
observations among people who perform at least two tasks.

The paper reports widespread but shallow adoption: genAI reaches over 80% of
occupations and over 40% of tasks, but within most of these fewer than half of
workers adopt. Only about 15% of occupations exceed 70% adoption, while no task
does; the occupation/task panels exclude cells with fewer than 20 pooled
observations. Exposure scores explain 5%–53% of adoption variation across
occupations and 7%–44% across tasks, depending on the score. This makes
occupation-level exposure an incomplete proxy for worker access or use.

The public index release contains 682 DWA rows, 256 IWA rows, and 9 BWA rows
with displayed rates. At the broad level, reasoning and decision making is
30.0% across 7,075 unweighted activity observations, while physical and manual
work is 9.6% across 8,351. These rates are task-index observations, not worker
productivity, pay, or control estimates.

The paper separately compares worker-reported task adoption with three
platform chat-log measures. All pairwise task-share correlations are below
0.4. Chat logs tend to classify activity into generic tasks spanning many
occupations; for example, more than 15% of OpenAI chats are classified as
editing written materials even though 2.4% of workers are in occupations that
include that ONET task. The measurement distinction is itself part of the
finding: the observed map depends on who reports use, what counts as a task,
and which activity record is available.

## Evidence chain

```text
technical or occupational exposure
  -> employer access, worker access, training, and permission
  -> worker adopts AI for some tasks but not others
  -> task allocation, discretion, pace, evaluation, and skill recognition
  -> pay, security, wellbeing, household room, and worker voice
```

W35677 directly informs the first two arrows. It does not observe the employer
rules, decision rights, or downstream outcomes in the connected chain.

## Interpretation

The bounded interpretation is that adoption is not simply a property of an
occupation. It is a situated relationship between a worker, a task, a workplace,
and a system. Widespread use can therefore coexist with shallow adoption within
similar work. That pattern can reflect unequal access or support, but it can
also reflect task fit, privacy or quality concerns, employer restrictions, or
limited perceived value.

This matters culturally and politically because “AI exposure” can become a
public category before people experience the same tool, risk, or opportunity.
The paper supports investigating who gets capability and who gets evaluated by
it; it does not support claiming that workers in a high-exposure occupation have
lost control.

## Counterexamples and limits

- A worker may use AI outside the measured task, or use it without reporting it.
- A low-adoption task may be protected by professional norms or may simply have
  poor tool fit.
- Chat logs may over-generalize activity, while surveys may miss employer-
  mediated use.
- Similar adoption rates do not imply similar training, monitoring, autonomy,
  or bargaining power.
- The RPS is an online survey designed to match key CPS demographics, not a
  simple random sample; the paper is a working paper rather than peer-reviewed
  publication.
- The public index release does not contain worker-level records or a full
  subgroup table by worker demographics, employer, or local place.

## What would change the finding

It would weaken if the full data showed that detailed task/occupation exposure
nearly determines adoption after accounting for access and workplace rules, or
if the within-task variation resulted mainly from coding artifacts. It would
strengthen if adoption differences persisted within comparable work after
measuring access, training, employer policy, and worker characteristics.

## Next test

Version the public index files and their O*NET/crosswalk metadata, then produce
adoption estimates by age, education, gender, disability, race, contract type,
industry, and employer size where supported by compatible worker microdata. Pair
the adoption cells with workplace evidence on training,
monitoring, autonomy, correction, pay, promotion, health, and worker voice.
Compare worker-reported adoption with firm disclosures and field experiments,
keeping all units separate until a valid linkage exists.

**Evidence status:** reported full-paper descriptive adoption and measurement result;
workplace control and downstream cultural, household, political, and
geopolitical effects remain open.
