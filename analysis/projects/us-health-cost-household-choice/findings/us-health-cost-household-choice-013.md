# Finding 013: A dated health event is not yet a household recovery episode

**Status:** verified MEPS episode-field availability finding · **Checked:** 2026-09-17

## The bounded finding

The local 2024 MEPS staged event ledger is the strongest retained candidate for
a same-person health-cost-to-household episode, but its available fields stop
before the decisive household-choice and remedy stages. The ledger contains
18,457 privacy-minimized person/event rows. Every row has a hashed episode
identifier and a month-precision first-event date, alongside round-level
payment, coverage, health, employment, bill, debt, collector, denial, and
care-delay context.

The field audit finds no usable episode-level alternative, no event-specific
choice or response, and no verified remedy. Later round fields are context,
not an event-specific recovery outcome. This is a substantive result for the
broad program: a dated record can improve time ordering while still failing to
show how a household paid, substituted, appealed, recovered, trusted, or left.

```text
first observed health event
  -> [missing] initiating need, amount owed, alternative, and household choice
  -> [partial] round-level payment, coverage, work, bill, debt, and health context
  -> [missing] provider/insurer response, appeal, correction, or remedy
  -> [partial] later round context, not verified event recovery
  -> [missing] trust, attribution, action, switching, non-use, or exit
```

## Availability audit

| Required episode stage | Availability in 18,457 staged rows | Safe interpretation |
|---|---|---|
| Event identity and date | Present for every row; hashed episode ID and month precision | A first event-family scaffold is available; day, trigger, and initiating need are not identified |
| Person linkage | Present through privacy-minimized person/event identifiers | Same-person staging is possible within the retained ledger; it does not create a household payer or provider join |
| Payment and coverage | Round-level payment, coverage, health, employment, bill, debt, collector, denial, and care-delay context | Context can be ordered around the event; it is not the event’s amount due, due date, payer, financing, or payment timing |
| Usable alternatives | Missing | No provider, network, coverage, travel, time, payment, family, or service substitute can be observed |
| Event-specific choice | Missing | Care delay or foregoing cannot be assigned to the displayed event or its counterfactual |
| Institutional response | Partial | Denial/prior-authorization context exists, but responsible authority, response date, effort, appeal, and decision are absent |
| Verified remedy | Missing/unknown | No correction, payment plan, coverage restoration, approved appeal, or explicit non-remedy is recorded |
| Follow-up | Partial context | Later round status can show persistence or change, but not whether the event caused it or whether recovery occurred |
| Meaning, action, and exit | Missing | No event-linked attribution, trust, complaint, organizing, vote, switching, non-use, or exit outcome exists |

The audit therefore distinguishes “field absent” from “field not yet analyzed.”
That distinction prevents a round-level bill or health measure from silently
filling the missing middle.

## What the local event spine can still establish

The staged ledger remains useful. It can support a bounded comparison of first
office, emergency-room, inpatient, or prescription event families with
month-ordered payment, coverage, employment, bill, debt, health, and care-delay
context. It can also preserve baseline selection: people with inter-round ER or
inpatient events already differ from people without such events in health and
employment context.

Those are real timing and conditioning contributions. They do not establish
that an event caused a payment burden, that a person delayed treatment, that a
household sacrificed food or work, or that an institution failed to remedy the
problem.

## Why this matters to the end-to-end program

The broad program asks how a condition changes money, time, access, security,
meaning, action, and power. MEPS currently reaches a valuable middle scaffold:

```text
dated event identity
  -> round-level context and later status
```

It does not reach the decision boundary where social consequences become
observable:

```text
amount/need and available alternative
  -> care continuation, delay, substitution, or non-use
  -> household payment, unpaid time, work, food, housing, or debt response
  -> institution's correction or remedy
  -> protected/sacrificed outcome and later recovery
  -> trust, blame, complaint, organizing, voting, switching, or exit
```

This is why the atlas must keep MEPS, SIPP, SHED, CFPB, and platform records as
separate evidence surfaces. A different source may contain one missing field,
but it cannot be assigned to the MEPS person or event without a lawful common
key and compatible clock.

## Counterexamples and limits

- Month-precision event identity is stronger than an annual prevalence screen,
  but it is not a complete bill or treatment episode.
- Round-level payment is not event-specific affordability, amount owed, payer,
  due date, or payment completion.
- A denial or prior-authorization flag is not a dated decision, appeal, remedy,
  treatment interruption, or insurer/provider fault finding.
- A later improvement or worsening in perceived health is not verified recovery
  or failure and may reflect baseline illness, treatment, selection, or unrelated
  events.
- A missing alternative cannot be coded as no alternative, and a missing remedy
  cannot be coded as failed remedy.
- Person-level linkage is not household-level linkage; the person may not be
  the payer, caregiver, or decision-maker.
- The staged ledger does not contain event-linked meaning, trust, complaint,
  political action, switching, non-use, or exit, so those endpoints cannot be
  inferred from health or payment movement.

## Coding rule

```text
dated event             != initiating need
round payment           != event payment
coverage status         != usable alternative
denial flag             != institutional decision
later health            != event recovery
missing remedy          != failed remedy
person linkage          != household payer/decision-maker
continued use           != unconstrained choice
no recorded action      != no action
```

Code this as **verified staged-field evidence that MEPS supplies a large
same-person month-ordered health-event scaffold but lacks episode-level
alternatives, choice, verified remedy, and meaning/action follow-up; no
health-cost-to-household-recovery or political-action claim is promoted**.

## Next decisive test

The smallest qualifying extension must add, for the same person or family and
the same dated event:

```text
initiating need and amount owed
  -> available provider, coverage, payment, time, and family alternatives
  -> chosen, delayed, substituted, or forgone care
  -> payment completion, borrowing, unpaid care, work, food, housing, or debt response
  -> provider/insurer decision, appeal, correction, or verified non-remedy
  -> one-, three-, and six-month health, security, trust, action, switching, or exit outcome
```

The preferred route remains registration-gated UAS Older Ages or Monthly Panel
data because the documented fields may supply event blocks, later health/work,
pain, life satisfaction, meaning, care, bill, and provider-experience measures.
Acquire no respondent file until access is authorized and the hashes, person
keys, overlap, weights, timing, eligibility, and missingness gates pass. If
those fields cannot be obtained, retain this MEPS boundary and rotate rather
than manufacture the episode.

## Sources and storage boundary

- [MEPS event-field availability audit](../meps-event-field-availability-audit-v1.md)
- [MEPS dated health-cost episode spine](../../us-household-constraint-cascade/meps-dated-event-spine-v1.md)
- [Broad next-episode selection](../../../../analysis/broad-next-episode-selection-v1.md)
- [UAS health-cost legitimacy acquisition audit](../uas-health-cost-legitimacy-acquisition-audit-v1.md)
- [MEPS 2024 bounded episode ledger](../meps-2024-bounded-episode-ledger-v1.md)
- [AHRQ MEPS data access](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp)

This finding reads the existing compact availability audit and staged ledger
metadata; no new raw MEPS or UAS respondent file was downloaded.

**Evidence status:** complete field-availability audit of the retained staged
ledger. The acquisition boundary is verified; alternatives, event-specific
choice, remedy, recovery, trust, political action, switching, and exit remain
unobserved.
