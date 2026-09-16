# Anticipatory to remedial worker control synthesis v1

**Status:** bounded thematic synthesis across three control moments; not a
pooled effect estimate or a claim about typical worker experience

**Checked:** 2026-09-15

## The question

When work is converted into data, scores, prompts, classifications, or
platform decisions, at what point can worker voice alter the system or its
consequences? The current evidence can be read as three control moments:

```text
before deployment       during deployment        after harm
negotiated constraints  monitored rollout       adjudicated remedy
IBM Germany             Microsoft Germany       Australia platform cases
```

The same phrase—“human oversight,” “worker voice,” or “review”—means different
things depending on when it is exercised, what information is available, and
whether the actor can change the decision.

## The three moments

| Moment | Record | What is visible | What is not yet visible |
|---|---|---|---|
| Before deployment | IBM Germany works-council framework | Risk classification, inspection, explainability, human final decision, correction, escalation, limits on high-risk personnel systems, retraining/equivalent-job commitments | A named live intervention that changed or stopped a system; worker-level benefit |
| During deployment | Microsoft Germany Copilot and Places rollouts | Council participation in a controlled tolerance phase; concerns about ranking, sensitive inference, and location visibility; feedback to engineering; a reported Places update with country-level targeting and default opt-out | Council minutes, technical diff, enforceable veto, and independent worker outcome |
| After harm | Australian Fair Work proceedings | Notices, responses, human-review findings, external merits review, reactivation, and lost-remuneration orders in selected cases | Payment receipt, continued access, recurrence prevention, non-retaliation, population-level prevalence |

This is not a maturity ladder in which one country is simply ahead of another.
It maps observable institutional functions. A strong ex-ante framework may
never be tested publicly; a strong post-harm order may arrive only after income
and trust have already been damaged.

## Narrow synthesis

### 1. Timing changes the object of control

IBM's framework addresses design and authorization conditions around an AI
system. Microsoft adds a live deployment-stage feedback loop in which councils
could surface concerns while rollout was still controlled. The Australian
cases begin later, when access or income has already been affected. Earlier
intervention can shape the decision surface; later intervention must reconstruct
facts and restore a counterfactual position.

This does not make ex-ante governance automatically effective. IBM establishes
rules; Microsoft reports participation and one concrete Places product change,
but neither establishes an independently verified worker outcome. Post-harm adjudication should not be treated as a
substitute for prevention when the decision is repeated at scale.

### 2. Human involvement is not human authority

The Australian comparison separates Bandameeda from Kumar. In Bandameeda, the
Commission found that meaningful discussion and necessary inquiry were missing.
In Kumar, it accepted that a human Community Operations representative
considered the response and that the process was compliant. IBM requires human
decision-making and correction in defined contexts; Microsoft describes council
feedback and operational monitoring.

The decisive coding question is not whether a human appears in the process
description. It is whether the person or body had access to relevant evidence,
an obligation to investigate and explain, authority to change, pause, or
reverse the consequence, and a traceable record of what changed afterward.

### 3. Proceduralization can expand visibility without guaranteeing recovery

The records show a broad movement toward proceduralized contestability:
classification, notice, explanation, review, escalation, council inspection,
and adjudication. These procedures can make opaque decisions more legible. They
can also increase the amount of worker data visible to employers or platforms.
Microsoft's dashboards, usage signals, and feedback mechanisms are therefore
both governance tools and potential new surfaces of employee visibility; the
public account does not yet show how workers inspect or contest that visibility.

The remedy ledger must keep these endpoints separate:

```text
rule exists -> person can invoke it -> reviewer investigates
            -> decision changes -> access/pay is restored
            -> restoration is received -> future harm is reduced
```

The current evidence reaches different points in this chain. It must not be
collapsed into a single “worker protection” score.

### 4. Formal remedy and practical recovery are different outcomes

Australia currently supplies the deepest public evidence of individual
restoration: selected Fair Work proceedings record reactivation and, in some
cases, ordered lost remuneration. The implementation audit found no public
follow-on evidence for several matters and treats that as a retrieval boundary,
not proof that workers were unpaid. A formal order is an institutional event;
receipt, continued access, and freedom from retaliation are worker outcomes.

This distinction is central to the end-to-end goal. If the project stops at the
order, it measures institutional recognition of harm, not whether the worker's
life or bargaining position recovered.

### 5. The geopolitical theme is usable sovereignty, not abstract autonomy

The cross-border comparison should ask which institutions give workers and
states usable alternatives when a firm controls the data, model, workflow, or
access channel. Germany's works-council institutions add collective inspection
and negotiated constraints. Australia's Commission adds external adjudication
and remedial authority. Malaysia's statutory design names disclosure,
non-automated review, hearing, and Tribunal routes. Cambodia's diagnostic shows
that complaint access can be widespread while reported resolution remains weak.

These are different capacities to inspect, contest, correct, restore, and exit.
The geopolitical question is whether local institutions retain enough
technical, legal, and organizational capacity to make those capacities usable
when the provider is cross-border or the worker is formally independent.

## Evidence boundary

The synthesis combines company-reported deployment accounts, a works-council
agreement and representative account, and primary Australian adjudicative
records. Their units differ: framework, rollout, worker-event, and proceeding.
It therefore supports mechanism hypotheses and acquisition priorities, not
rates, causal effects, or country rankings. It also does not infer that every
decision was made by autonomous AI; the Australian cases remain coded as
platform-mediated control unless the source establishes more.

## Decisive next test

Join one pre-deployment or deployment-stage workplace intervention to one named
system and one post-deployment outcome. The minimum same-unit record should
carry: (1) system and decision surface; (2) representative concern or
intervention; (3) employer/platform response and authority; (4) changed rule,
feature, deployment boundary, or review practice; (5) affected worker or
workforce outcome; and (6) implementation, payment, access, and
non-retaliation follow-up.

The immediate queue is to corroborate the reported Places change with a
works-council or technical artifact, recover the next Australian
payment/access follow-up, and
recover the Malaysian Tribunal case record. Until then, preserve these three
moments as complementary evidence classes rather than forcing them into one
outcome measure.

## Linked writeups

- [IBM Germany works-council AI framework governance record](ibm-germany-works-council-ai-framework-governance-record-v1.md)
- [Microsoft Germany works-council Copilot deployment record](microsoft-germany-works-council-copilot-deployment-record-v1.md)
- [Microsoft Places works-council intervention event](data/microsoft-places-works-council-intervention-event-v1.json)
- [Australian platform-deactivation cross-case synthesis](australian-platform-deactivation-cross-case-synthesis-v1.md)
- [Australian remedy implementation acquisition audit](australian-remedy-implementation-acquisition-audit-2026-09-15.md)
- [Global platform-work remedy comparison](global-platform-remedy-comparison-v1.md)
- [Platform-remedy case ledger](data/platform-remedy-case-ledger-v1.json)
