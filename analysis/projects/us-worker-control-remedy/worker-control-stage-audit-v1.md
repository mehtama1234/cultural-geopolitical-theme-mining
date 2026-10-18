# Worker control stage audit

Status: fifty-second active depth artifact; checked 2026-10-18.

## Purpose

The worker-control route asks whether software or AI changes work and whether a
worker can understand, challenge, and recover from that change while retaining
income, schedule control, and a usable alternative. Existing evidence spans
experiments, surveys, international standards, and adjudicated cases. This
audit keeps those units separate and identifies the first missing same-worker
join.

## What we found

The evidence is strongest for exposure and measured performance, weaker for
authority and formal review, and thinnest for received remedy and durable work
control.

| Stage | Evidence | Comparable signal | Boundary |
|---|---|---|---|
| AI/task performance | HBS field experiment with 138 service agents and 256,934 meal-delivery chats | AI suggestions reduced response time 22% and raised automated customer sentiment 0.45 points on a five-point scale; less-experienced agents had a reported 70% time reduction and 1.63-point sentiment increase | No worker pay, schedule control, authority, job security, household effect, or later exit |
| Knowledge-work time | Multi-firm field experiment | 80% of treated workers used the tool in the second half of six months; email time fell by 2 hours per week among treated users | Time saving is not worker control, bargaining power, or shared gain |
| Task exposure/adoption | NBER worker-task survey and 55,634 worker-task observations | Fewer than half adopted in most occupations/tasks; exposure explained 5–53% of occupation variation and 7–44% of task variation depending on measure | Adoption measures do not identify who decided, who benefited, or who could refuse |
| Algorithmic management | OECD employer survey, June–August 2024 | 90% of U.S. firms reported at least one algorithmic-management tool; 55% reported monitoring conversation content or tone | Employer report does not identify worker notice, contestability, accuracy, or remedy |
| Formal rights | ILO platform-work Convention adopted 12 June 2026 | Requires information about automated systems, explanations and human-involved review for significant adverse decisions, data rights, and effective dispute resolution | Ratification, domestic implementation, awareness, use, enforcement, and successful outcomes remain open |
| Same-worker remedy | Australian Fair Work Commission case, 2025-12-15 to 2026-03-20 | Worker deactivation after an alleged failed background check was followed by reactivation and a gross A$7,096.96 lost-remuneration order based on 9.5 weeks | Payment receipt, net loss, household security, continued access, recurrence prevention, trust, and exit are not verified |
| Large platform remedy | Walmart Spark Driver settlement | $79 million direct-driver allocation within a $100 million judgment; ten-year earnings-verification program; some payments made and others still processing | No eligible denominator, sent/received counts, corrected account, schedule control, alternative work, or exit |

These stages show a recurring pattern: measured efficiency can coexist with
unmeasured authority. Formal rights can specify explanation and human review
without showing that a worker knew how to invoke them or received a usable
correction. Reactivation can restore access without proving the lost earnings,
household stability, or future risk were repaired.

## Evidence ledger

| Stage | Current local evidence | Still missing |
|---|---|---|
| System exposure | AI adoption, algorithmic-management use, and platform work are separately measured | Which worker, task, workplace, and decision rule were exposed |
| Notice and understanding | ILO establishes a normative information/explanation right; experiments measure tool use | Actual notice, comprehension, language/access support, and ability to refuse |
| Work effect | Response time, issues resolved per hour, email time, and task adoption are observed | Pay, hours, scheduling, workload quality, performance discipline, and bargaining distribution |
| Voice and review | Human-review and dispute-resolution requirements are specified; formal adjudication exists in one case | Worker effort, representative support, decision authority, review timing, and success rate |
| Remedy | Reactivation and gross lost-remuneration order in one case; platform allocations in named settlements | Verified receipt, net recovery, account correction, residual loss, and recurrence prevention |
| Household security | Broad surveys provide financial stress and work context in separate routes | Same worker's household income, care, debt, time, and security after the decision |
| Durable control and exit | Public discussion supplies concerns about autonomy, layoffs, and AI inequality | Continued work, alternative work, collective action, switching, non-use, or exit for the same worker |

## What this connects to

- **Firm power:** a productivity gain can increase firm capacity without
  changing who controls the task, schedule, evaluation, or surplus.
- **Unequal exposure:** adoption and benefit may differ by education,
  occupation, experience, and platform status; aggregate averages hide that
  distribution.
- **Household room:** time saved or income restored matters only if it reaches
  the worker and is not offset by monitoring, schedule volatility, debt, or
  unpaid care.
- **Institutional legitimacy:** an explanation or appeal right becomes real
  only when it can be used and produces a timely, adequate correction.
- **Cultural meaning:** workers may interpret AI as assistance, surveillance,
  status threat, or opportunity; measured productivity does not choose among
  those meanings.

## Deeper question

**When does AI assistance or algorithmic review transfer real control to a
worker rather than merely increase the speed or observability of work?**

This question is high value because the current evidence contains both positive
productivity effects and strong exposure/control concerns, but no compatible
same-worker chain through notice, challenge, remedy receipt, household effect,
and later work choice.

## Bounded public discussion

The existing LinkedIn, Reddit, X, and YouTube records add a bounded meaning
layer: discussions connect AI to uneven productivity, layoffs, autonomy,
younger-worker opportunity, and job quality. They include counter-signals that
AI can help workers learn or complete tasks faster. These posts are useful for
testing worker interpretations and policy concerns, but they are not measures
of adoption, control, remedy, or exit.

## Challenge checks

- Productivity, time savings, sentiment, and task adoption were not treated as
  worker welfare or control.
- Employer-reported algorithmic-management use was not treated as worker-side
  exposure or harm.
- ILO rights were treated as a normative institutional stage, not compliance or
  worker awareness.
- Reactivation, a gross lost-remuneration order, and settlement allocations were
  not treated as verified receipt or household recovery.
- The Australian case, U.S. platform settlements, experiments, and surveys were
  not pooled into one worker denominator.
- Public discussion was used for meaning and counterexamples only.

## Next test

Construct one protected same-worker or workplace episode ledger:

```text
worker/workplace key | system and decision exposure | notice/understanding |
task/pay/schedule/monitoring effect | refusal or appeal | review authority |
correction/reactivation/payment | receipt and residual loss | household effect |
continued work or alternative | collective action | switch/non-use/exit |
later recurrence and trust
```

Start with an adjudicated case or authorized worker survey that exposes both
the decision and follow-up. Require a dated decision, a worker-side outcome, a
remedy receipt or verified non-receipt, and a later work or household field
before making a control claim.

## Stopping rule

Do not call AI empowering, worker-protective, or remedy-effective from adoption,
time saved, sentiment, employer reports, a legal standard, reactivation, or a
judgment alone. Close this subtest only when one compatible worker or workplace
episode links exposure to notice, challenge, remedy receipt, household or
work outcome, and later control, alternative work, collective action, or exit—
or when the source owner confirms the exact missing fields are unavailable.

## Source links

- [AI adoption and control cross-source record](../../records/us-ai-work-adoption-control-2024-2026.json)
- [AI management and bargaining record](../../records/us-ai-management-bargaining-voice-crosssource-2024-2026.json)
- [ILO platform-work convention](../../records/comparative-ilo-platform-economy-convention-2026-algorithmic-management-rights-remedy.json)
- [Australian platform-worker remedy](../../records/au-rehman-platform-remedy-2026.json)
- [Walmart Spark Driver remedy](../../records/us-ftc-walmart-spark-driver-remedy-2026.json)
- [Worker control and remedy bridge](worker-control-adoption-remedy-recovery-bridge-v1.md)
- [LinkedIn AI-work discussion](../../social-discussions/records/ai-work-control-005.json)
- [Reddit worker AI discussion](../../social-discussions/records/ai-work-control-003.json)
- [X AI-layoff discussion](../../social-discussions/records/ai-work-control-x-001.json)
- [YouTube future-of-work discussion](../../social-discussions/records/ai-work-control-001.json)
