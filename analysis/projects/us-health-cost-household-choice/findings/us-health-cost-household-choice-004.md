# Finding 004: Event payment is not a monotonic measure of the later household burden surface

**Status:** payment-band conditioned MEPS transition screen · **Checked:** 2026-09-15

## Bounded result

Among people whose first emergency-room or inpatient event occurred strictly
between the MEPS R3/1 and R4/2 endpoint months, event-level family payment
does not produce a simple increasing ladder of later health or bill problems.
The payment bands are zero, positive under $100, and $100 or more. These are
event payments, not complete bills or household obligations.

| Event family | Payment band | Event-window people | Baseline fair/poor health | R4/2 fair/poor health | R4/2 bill problem |
|---|---|---:|---:|---:|---:|
| Emergency room | $0 | 765 | 28.51% | 30.34% | 14.28% |
| Emergency room | $0.01–$99.99 | 99 | 24.79% | 24.55% | 11.35% |
| Emergency room | $100+ | 244 | 14.43% | 17.81% | 18.11% |
| Inpatient | $0 | 343 | 33.37% | 36.08% | 11.77% |
| Inpatient | $0.01–$99.99 | 34 | 29.82% | 32.17% | 11.47% |
| Inpatient | $100+ | 175 | 20.60% | 25.34% | 9.58% |

The zero-payment acute-event groups have worse baseline and follow-up health
than the $100+ groups, while ER bill-problem shares are higher in the $100+
band. This is a warning against treating observed payment as either household
burden or a sufficient proxy for affordability.

## What this adds to the chain

~~~text
strictly timed observed care event
  -> event-level family payment
  -> later health/work/bill context
  -> payment and burden remain distinct
~~~

The design preserves person identity, event month, family-paid amount, a
pre-event health screen, and BRR uncertainty. It therefore sharpens the
payment-to-context arrow while also showing why the payment measure cannot
stand in for a household choice.

## Boundaries

Family payment can reflect insurance, public coverage, payer mix, imputation,
event severity, negotiated charges, payment capacity, and the distinction
between facility and professional costs. The event window is selected, the
positive-under-$100 inpatient cell is small, and the public files do not
identify the full bill, due date, borrowing, savings draw, delayed care,
unpaid care, treatment continuity, or remedy.

The result is descriptive, not causal. It does not show that payment caused
the later bill or health context, nor that zero payment meant zero burden.

## Reproduction

- [Reproduction audit](../meps-2024-interround-payment-reproduction-audit-2026-09-16.md)
- [Canonical machine record](../../../records/us-meps-2024-interround-payment-followup.json)
- [MEPS inter-round transition layer](../meps-2024-between-round-event-transitions-v1.md)
- [Analysis script](../../../../scripts/analyze_meps_interround_payment_followup.py)
- [AHRQ MEPS HC-256 download page](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256)

**Evidence status:** strict month-ordered, payment-band conditioned
descriptive comparison with baseline selection and payment/burden boundaries
preserved. Recovery, household adaptation, remedy, trust, political action,
and geopolitical consequence remain open.
