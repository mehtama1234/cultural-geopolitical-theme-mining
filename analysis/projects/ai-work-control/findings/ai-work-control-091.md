# Finding 091: Platform exclusion can produce separate access and lost-pay remedies

**Status:** comparative adjudicated single-case finding · **Checked:** 2026-09-17

## The bounded finding

In *Tanzeel Ur Rehman v Portier Pacific Pty Ltd* (Australia, UDE2025/384), a
platform worker's account was deactivated on 2025-12-15 over an alleged failed
background check. The worker applied to the Fair Work Commission on 2025-12-30.
Portier voluntarily reactivated access on 2026-02-20, and on 2026-03-20 the
Commission issued concurrent orders restoring access and awarding A$7,096.96
gross lost remuneration.

This closes a meaningful institutional arrow:

```text
platform exclusion -> worker application -> voluntary restoration
                      -> formal access restoration + ordered lost pay
```

It does not show that the worker received the money, recovered net income,
returned to work, had a real alternative, remained protected from recurrence,
or chose continued use, switching, non-use, or exit.

## Remedy-stage evidence

| Stage | Observed | Not observed |
|---|---|---|
| Exclusion | Account deactivation and alleged reason | Platform-wide incidence or error rate |
| Worker route | Unfair-deactivation application | General access to recourse |
| Access remedy | Voluntary reactivation and formal order | Durable restoration or anti-retaliation |
| Financial remedy | A$7,096.96 gross lost-remuneration order | Payment receipt, net pay, expenses, household recovery |
| Choice and action | A formal worker challenge occurred | Alternative work, continued use, switching, organizing, political action, exit |

The Commission's calculation used average weekly earnings over approximately
9.5 weeks. The decision records that no evidence addressed expenses the worker
would have incurred had work continued. The ordered amount therefore cannot be
read as net household recovery or compensation for every consequence of
deactivation.

## Why it matters to the broad atlas

The case supplies a remedy architecture that the survey layers cannot observe:
access restoration and financial restoration can be separate institutional
outputs. It also gives the fraud/consumer-recourse lane a counterexample to a
simple “formal remedy equals recovery” interpretation. A worker can obtain an
order while payment, alternatives, durability, and practical exit remain
unknown.

Because this is one Australian adjudicated matter, it is comparative evidence,
not a US estimate. Its value is to specify the missing fields for a stronger
cross-case or same-worker design: deactivation reason and date, application
route, restoration date, order terms, payment confirmation, expenses, later
work, alternative platforms, recurrence, and worker-reported recovery.

## Coding consequence

```text
formal access order       != realized access durability
ordered gross lost pay    != payment receipt or net recovery
worker application        != population-wide recourse access
restoration               != unconstrained alternative choice
case action               != political action or practical exit
```

Code this as **single-case adjudicated remedy evidence with separate access and
gross-lost-pay outputs; payment, recovery, alternatives, durability, and exit
open**.

## Next decisive test

Locate compliance or payment evidence and a post-order worker-side record of
trips, expenses, alternative work, and continued access. A second case with a
documented non-payment or alternative-work outcome would make the practical
exit comparison sharper.

## Sources and storage boundary

- [Primary Fair Work Commission decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2026fwc953.pdf)
- [Official FWC bulletin](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2026-03-31.htm)
- [Committed local remedy record](../uber-rehman-remedy-record-v1.md)

The work uses the existing compact local record and targeted official URLs. No
bulk archive or new large download was retained.
