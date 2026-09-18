# Finding 094: AI can change work time before the record shows who controls it

**Status:** non-pooled workplace implementation synthesis  
**Checked:** 2026-09-17

## The bounded finding

The current US-centered workplace evidence supports a precise but limited
claim: generative-AI access and algorithmic-management systems can alter
measured task performance, email time, or work timing before the evidence
shows whether workers keep the benefit, whether employers convert it into more
output, or whether representatives can contest the new allocation.

The relevant chain is:

```text
tool access or algorithmic management
  -> adoption, task performance, email time, monitoring, or schedule pressure
  -> employer allocation of saved capacity
  -> worker discretion, pay, pace, voice, and household time
  -> remedy, bargaining, trust, or exit
```

The first two stages are measurable in separate studies. The conversion from
changed work process to worker control remains open in a common workplace
event.

## Evidence surfaces kept separate

| Evidence surface | Observed result | What it does not establish |
|---|---|---|
| NBER randomized field experiment | Six-month access intervention across 66 firms and 7,137 knowledge workers; treated users used the tool and spent about two fewer hours per week on email in the second half; work outside regular hours decreased and task quantity/composition showed no detectable change | Whether total workload fell, whether saved time remained with workers, or whether pay, discretion, health, and household time improved |
| NBER customer-support experiment | A separate 5,179-agent field experiment estimated about a 14% increase in issues resolved per hour with AI assistance | Whether the gain changed staffing, targets, pay, pace, monitoring, worker bargaining, or customer outcomes |
| OECD algorithmic-management survey | Among US firms with 20+ employees, managers reported 90% using at least one algorithmic-management tool, 76% using ten or more, and 55% monitoring conversation content or tone | Worker exposure, consent, consequential use, appeal, enforcement, or whether monitoring changed job quality |
| NBER executive survey | Across nearly 6,000 executives in the US, UK, Germany, and Australia, 69% reported active AI use and 90% reported no past three-year firm employment/productivity impact; expected next-three-year productivity was +1.4%, with employer employment expectations −0.7% and employee expectations +0.5% | Realized employment, pay, implementation, or a US-only expectation estimate |
| BLS union context | US union membership moved from 9.9% in 2024 to 10.0% in 2025; represented workers from 11.1% to 11.2% | AI exposure, practical bargaining power, schedule control, or whether representation changed a technology decision |

These are different units, clocks, and estimands. The table is a mechanism map,
not a pooled AI productivity, employment, or worker-welfare estimate.

## What the randomized evidence closes—and leaves open

The knowledge-worker experiment is valuable because access was assigned rather
than inferred from workers who chose to use a tool. It places time movement
after an intervention and reports a null result for measured task quantity or
composition. That is stronger than a cross-sectional adoption percentage.

But “two fewer email hours” is not yet “two hours returned to the worker.” The
hours may have become meetings, documentation, customer handling, faster
throughput, availability expectations, or additional tasks. The study's
measured time result cannot identify who had authority over the resulting
capacity.

The customer-support experiment provides a complementary counterexample.
Higher issues resolved per hour can be a worker benefit if it reduces queue
pressure or preserves judgment. It can be a worker cost if management raises
targets, reduces staffing, or treats assistance as a reason to intensify pace.
The productivity result alone cannot distinguish those paths.

The safe coding is therefore:

```text
assigned access       = intervention
tool use               = adoption
less email time        = measured time movement
more issues per hour  = measured output movement
saved capacity        = ownership/control question
worker benefit        = unobserved until allocation and outcome are measured
```

## Algorithmic management changes the control problem

The OECD employer survey broadens the issue beyond generative AI. A system
that instructs, monitors, or evaluates workers can distribute control even if
it is not described as an AI assistant. The US manager reports—90% with at
least one tool, 76% with ten or more, and 55% monitoring conversation content
or tone—make organizational visibility and evaluation part of the work
environment.

Those figures do not say that 55% of workers experienced harmful monitoring.
They identify a governance surface that worker-level surveys and the NBER
field experiment do not share. A scheduling system, quality dashboard,
conversation monitor, or generative assistant can have different effects on
privacy, pace, breaks, evaluation, and appeal.

The executive survey adds a time-horizon counterexample. Ninety percent of
executives reported no past three-year firm employment/productivity impact,
while the same survey records forward expectations for productivity and
employment. Low retrospective impact and future organizational change can
coexist. Expectations are not outcomes, but they identify where firms may
allocate future gains before worker consequences are visible.

## Representation is an institution, not proof of control

Formal union membership and representation provide a potential route for
workers to negotiate technology, but the 2024–2025 BLS movement is too small
and too aggregate to establish practical control. A represented worker may
have a route to information, consultation, or bargaining; the public annual
series does not show whether a specific AI deployment was contested, modified,
or remedied.

The decisive distinction is:

1. **Information:** workers know what system exists and what it influences.
2. **Voice:** workers or representatives can question or negotiate it.
3. **Control:** that participation changes pace, data, monitoring, allocation,
   human review, refusal, or appeal.
4. **Remedy:** a worker can reverse an error or obtain relief after harm.

Adoption and productivity reach the first part of the work-process chain.
Formal representation may create a route to the third and fourth stages, but
neither representation rate nor consultation presence proves that conversion.

## Counterexamples and limits

- Less email time can coexist with unchanged total work or higher output
  expectations.
- Higher issues resolved per hour can improve service without improving job
  quality, or can intensify work if targets rise.
- Manager-reported algorithmic-management use is not worker exposure or proof
  of consequential monitoring.
- Executive expectations can precede real change, but cannot forecast realized
  employment or pay effects without implementation follow-up.
- Union coverage is not a direct measure of worker control and excludes
  informal voice, nonrepresented workers, contractors, and platform workers.
- The studies cover different countries, sectors, occupations, tools, and
  periods; no cross-source effect size should be calculated.

## Why this matters to the broad goal

This is the workplace analogue of the consumer-recourse and recall findings.
In each case, an upstream institutional stage is easier to measure than the
protected outcome:

```text
AI access or management tool -> measured work change -> allocation -> control
recall notice                 -> correction report   -> receipt   -> safety
complaint route              -> response label      -> remedy    -> exit
```

The atlas should therefore treat worker time, customer correction, and product
correction as intermediate currencies. The societal question is who controls
the conversion and who bears the residual risk.

## Next decisive test

Select one US workplace deployment and follow the same workplace or worker
from implementation through at least one later outcome. Required fields are
implementation date, worker exposure, training, monitoring, pace, hours, pay,
discretion, data visibility, appeal, representation, household-time effects,
and later enforcement. The decisive observation is a changed rule, preserved
worker time, successful appeal, or durable remedy—not adoption or productivity
alone.

## Sources and reproduction boundary

This finding reads the committed non-pooled comparison record and linked source
notes; it downloads no new respondent or firm archive. The [machine-readable
comparison record](../../../records/us-ai-management-bargaining-voice-crosssource-2024-2026.json)
preserves denominators, methods, uncertainty, and source hashes.

**Evidence status:** selected randomized, employer-reported, executive, and
formal-representation surfaces establish work-process and governance stages;
worker control, household security, remedy, trust, and exit remain open.
