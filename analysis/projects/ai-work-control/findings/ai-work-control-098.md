# Finding 098: Individual employment remedies can be reported without closing recovery

**Status:** provisional named US enforcement remedy finding · **Checked:** 2026-09-18

## The bounded finding

FY2026 summaries from the Justice Department's Immigrant and Employee Rights
Section report several charging-party resolutions in which an individual
payment was made after an employment or employment-verification dispute. The
reported paid amounts include $5,600, $16,730, $30,000, and $8,000. A separate
September resolution reports an offer of $485,000 in full back pay and
benefits, but not payment.

The safe interpretation is:

> The public enforcement record can establish an agency-reported individual
> monetary remedy and employer control response. It still does not establish
> that the worker regained the original job or opportunity, had a usable
> alternative, recovered household security, trusted the institution, or
> stayed, switched, organized, or exited.

## Event chain

```text
employment or verification barrier
  -> reported lost opportunity, termination, or hiring dispute
  -> IER investigation or resolution
  -> paid back pay/front pay in four summarized cases
     or a back-pay offer in one case
  -> employer training or policy correction
  -> [open] restored work, durable compliance, household recovery,
          trust, action, switching, or exit
```

These are five distinct anonymous resolution summaries, not one pooled
worker-level panel. The amounts are retained as case-level agency reports and
are not converted into a prevalence rate or average remedy.

## Stage table

| Stage | Observed | Still open |
|---|---|---|
| Dated episode | IER dates five FY2026 resolution summaries | Full underlying chronology, affected-worker denominator, and application/shift records |
| Responsible actor | Employer type and location are summarized, but company names are not supplied on the page | Named employer, decision-maker, and complete institutional chain |
| Burden or loss | Alleged non-hire, termination, documentary, or verification harm is described | Individual effort, alternative job, foregone wages, and counterfactual opportunity |
| Monetary remedy | Four cases report payment; one reports a $485,000 offer | Payment instruments, dates, net amount, taxes/fees, and worker confirmation |
| Institutional response | Training, policy correction, and in one case an offer of reinstatement are reported | Durable compliance, actual reinstatement, comparable work, recurrence, and monitoring |
| Recovery and meaning | Not reported | Continued work, household security, trust, attribution, political action, switching, and exit |

## Why it matters to the broad atlas

This adds a stronger middle stage to the work-control and public-systems lanes:
an enforcement route can reach a reported individual payment rather than only
a reserve fund, aggregate distribution, or prospective control. But payment is
not the same currency as opportunity restoration. The same record can therefore
show remedy administration while leaving lived recovery and power unchanged or
unknown.

It also sharpens the same-case promotion gate. The IER summaries observe an
individual remedy, but they do not contain an episode-level alternative or
non-use field, later outcome, trust/action measure, or exit. They cannot be
joined to the existing alternative surface merely because the cases concern a
similar institutional mechanism.

## Coding consequence

```text
agency-reported payment       != worker-confirmed receipt audit
back pay                       != restored job or opportunity
reinstatement offer            != accepted return to work
training/policy correction    != durable compliance
individual remedy              != household recovery, trust, or exit
```

Code this as **agency-reported individual remedy with employer response and
later recovery open**. Keep the $485,000 case as an offer, not a payment.

## Next decisive test

The smallest useful follow-up would retain an episode identifier and pair the
payment or offer with the worker's alternative options, accepted or refused
reinstatement, later employment, net pay, household security, recurrence,
institutional trust, and switching or exit. If those records are unavailable,
the cases remain remedy-stage comparators rather than end-to-end episodes.

## Sources and reproduction

- [DOJ IER FY2026 letters of resolution](https://www.justice.gov/crt/ier-letters-resolutions-fy-2026)
- [Machine-readable trend record](../../../records/us-doj-ier-individual-remedy-followups-2026.json)
- [Broad same-case availability audit](../../../broad-same-case-episode-availability-audit-v1.md)

**Storage boundary:** one official DOJ summary page was retrieved and hashed;
no claimant files, respondent-level data, or bulk archive were downloaded.
