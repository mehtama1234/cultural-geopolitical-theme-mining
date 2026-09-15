# Source record: OECD worker-consultation experiment on algorithmic management

**Checked:** 2026-09-14
**Source family:** OECD/Fraunhofer worker-consultation experiment
**Use:** evidence about the conversion of consultation into technology-design choices

## Acquisition and identity

The primary source is Anna Milanez, *Exploring win-win outcomes of algorithmic
management: Lessons from a laboratory experiment on worker consultation*, OECD
Artificial Intelligence Papers No. 43, July 2025. The experiment involved
worker participants from three German manufacturing firms and a total of 16
participants. The source is a working paper and explicitly says that its
opinions are those of the author, not necessarily the official OECD position.

The [machine-readable acquisition record](data/oecd-worker-consultation-experiment-acquisition-v1.json)
preserves the official PDF URL, response metadata, hash, design, sample, and
outcome boundary.

## What was studied

Participants viewed computer simulations of variants of an algorithmic
management system, made individual assessments of design features, and then
participated in a group discussion involving workers, managers, and works
council representatives. The design used a within-subject structure rather
than a treatment/control comparison. The discussion sought agreement on the
features of a system that could be adopted.

The simulated design included features related to autonomy, competence, and
relatedness:

- system strictness and task-order flexibility;
- free-time management and schedule flexibility;
- wearables;
- rewards and sanctions;
- whether the system learns from workers;
- whether workers learn from the system;
- an empathetic communicator; and
- social visibility of performance.

## Direct results

| Result | What the paper reports | Evidence boundary |
|---|---|---|
| Initial disagreement | 17 of 24 firm-level feature assessments were controversial before discussion | The denominator is 8 features × 3 firms; controversy means at least one participant favored and at least one opposed a feature |
| After discussion | 4 of 24 firm-level assessments remained controversial | This is convergence of views, not proof of better implementation or worker welfare |
| Full agreement | One of the three firms reached agreement on all eight features and therefore agreed to the simulated system's implementation | Two firms did not reach full agreement; the system was simulated, not deployed as a production intervention |
| Partial agreement | One firm agreed on seven features; another on five | The unresolved features were especially important for autonomy and flexibility |
| Autonomy conflict | Workers raised task-prioritization, stopping a task, individual tracking, and management-oversight concerns; managers favored conditional flexibility in some production areas | The conflict is directly observed in discussion, but the preferred design was not tested in actual work |
| Negotiated modification | In 19 of 20 agreed feature decisions, participants specified additional criteria or modifications | The paper shows design negotiation, not a legal or operational enforcement mechanism |
| Expected outcomes | Participants generally expected productivity gains and improvements in learning, working conditions, self-organization, stress, and health protection; some expected more performance pressure or worse social relationships | These are participant expectations after the simulation, not observed productivity, pay, stress, or health outcomes |

## What this adds to the atlas

The paper supplies a rare middle layer between a governance policy and a worker
outcome:

```text
algorithmic-management design
  -> worker / manager / works-council discussion
  -> modified feature, unresolved disagreement, or refusal
  -> expected productivity and job-quality consequences
  -> actual deployment and worker outcome still required
```

The strongest result is not the paper's “win-win” label. It is the observation
that consultation surfaced concrete control questions—task order, stopping
work, individual performance visibility, wearable data, rewards, sanctions,
and who may override flexibility—and converted many of them into altered
design criteria. In two of the three firms, disagreement about autonomy still
prevented agreement on the full system.

That pattern complements the IBM Germany agreement. IBM shows how a written
institutional rule can create risk categories, human-decision requirements,
correction routes, and works-council inspection. The OECD experiment shows a
small-scale process in which consultation changes or refuses specific system
features. Neither source demonstrates that a live system improved worker
outcomes after deployment.

## Limits and counterexamples

- Sixteen participants across three German manufacturing firms cannot estimate
  the prevalence or average effect of worker consultation.
- Participants evaluated simulations; the paper does not observe a production
  rollout with measured productivity, pay, stress, injury, turnover, or
  household consequences.
- Expected improvement is not realized improvement. Participants also raised
  risks of performance pressure and damaged social relationships.
- The German works-council setting is institutionally different from most US
  workplaces; the mechanism is comparative, not a US population estimate.
- One full agreement does not mean consensus is always possible; two groups
  retained unresolved disagreement over autonomy-related features.
- Convergence of opinions can reflect persuasion or compromise without equal
  bargaining power, enforceable rights, or later compliance.

## Next test

Replicate the design with a larger and more diverse sample, then follow at least
one agreed system into production. Preserve the feature-level design record,
who participated, unresolved objections, implementation date, actual worker
exposure, override and appeal events, productivity, pay, pace, schedule
control, stress, safety, and later enforcement. The US comparison should code
the same feature dimensions rather than import the German consultation rate or
legal structure.

## Sources

- [OECD publication page](https://www.oecd.org/en/publications/exploring-win-win-outcomes-of-algorithmic-management_84b59397-en.html)
- [Official OECD PDF](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/07/exploring-win-win-outcomes-of-algorithmic-management_88216705/84b59397-en.pdf)
- [Machine-readable acquisition record](data/oecd-worker-consultation-experiment-acquisition-v1.json)
- [Worker voice and AI control synthesis](findings/ai-work-control-068.md)

**Evidence status:** small comparative laboratory experiment with worker,
manager, and works-council participants; direct evidence of discussion and
design negotiation; no realized production, causal worker-outcome, or US
estimate established.
