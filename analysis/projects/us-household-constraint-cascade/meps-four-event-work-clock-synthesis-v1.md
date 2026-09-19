# Four MEPS event families show different later work clocks

**Status:** aligned same-person descriptive synthesis  
**Checked:** 2026-09-18  
**Scope:** month-ordered MEPS 2024 event windows carried to R4/2 and R5/3;
not a causal estimate or verified recovery measure

## Why add the fourth event family

The existing MEPS work-clock audit compared office, emergency-room, and
inpatient events. The retained prescription-event follow-up uses the same
strict R3/1-to-R4/2 month rule and later R5/3 clock, but its output was kept
separate. Putting all four families in one comparison makes a useful
counterexample visible: later employment levels and transitions do not move in
one direction across event types.

```text
first valid event in an inter-round window
  -> R4/2 work-status level
  -> R5/3 work-status level
  -> status change, onset, or resolution screen
```

The event-window group is not a treatment group. The complementary population
can contain people with events outside the window, and event severity,
intended need, coverage, payment obligation, and treatment continuity remain
unobserved.

## Aligned work outcomes

| Event family | Event-window people | Comparison people | R4/2 nonemployment | R5/3 nonemployment | R4→R5 status change | Nonemployment resolved | Nonemployment onset |
|---|---:|---:|---:|---:|---:|---:|---:|
| Prescription | 724 | 17,967 | 24.29% / 33.96% | 26.16% / 35.04% | 13.15% / 9.32% | 11.43% / 5.19% | 12.81% / 7.11% |
| Office | 3,216 | 15,507 | 33.35% / 33.91% | 35.24% / 34.59% | 10.07% / 9.35% | 5.41% / 5.35% | 8.99% / 6.91% |
| Emergency room | 1,101 | 17,622 | 47.62% / 32.98% | 49.01% / 33.84% | 11.49% / 9.35% | 3.58% / 5.52% | 6.67% / 7.32% |
| Inpatient | 545 | 18,178 | 60.13% / 33.03% | 62.18% / 33.90% | 11.83% / 9.40% | 2.61% / 5.51% | 6.34% / 7.31% |

Each cell is **event-window / comparison**. The event and comparison
denominators differ by outcome because only valid records enter each estimate;
the source outputs retain BRR standard errors and field-specific valid counts.

## Payment and burden context on the same event-window design

The companion dated-event screen uses the same inter-round event-window rule
and supplies a separate payment/burden context. Its payment is a weighted
self/family event-payment mean, not the amount owed or a household obligation.

| Event family | Event-window people in payment screen | Mean self/family payment | Cost-related care delay | Medical bill problem | Medical debt | Collector contact |
|---|---:|---:|---:|---:|---:|---:|
| Prescription | 1,773 | $12.76 | 8.09% / 6.45% | 8.82% / 7.48% | 19.45% / 15.17% | 15.03% / 13.08% |
| Office | 3,216 | $66.87 | 6.41% / 6.64% | 8.01% / 7.52% | 16.17% / 15.45% | 13.08% / 13.30% |
| Emergency room | 1,101 | $155.52 | 9.59% / 6.44% | 15.14% / 7.19% | 24.12% / 15.10% | 19.75% / 12.90% |
| Inpatient | 545 | $733.03 | 6.82% / 6.60% | 11.13% / 7.52% | 16.61% / 15.55% | 14.42% / 13.23% |

Each paired percentage is event-window / complementary round-valid. The
payment and burden table has a larger event-window universe than the R5/3 work
table because later-round validity and each outcome's nonmissingness reduce
the usable records. It is aligned context, not a claim that every person in
the payment table appears in the later work estimates.

The useful pattern is not simply “higher payment, worse work.” Inpatient
events have the largest payment mean and the highest later nonemployment, but
prescription events have the lowest payment mean while showing elevated debt,
collector contact, and later work-status movement relative to their comparison
group. Payment amount alone is not a burden, and a lower event payment does
not imply a lower household constraint.

## What the comparison shows

1. **Event severity or route matters.** Acute ER and inpatient groups begin
   with substantially higher nonemployment and remain higher at R5/3. Office
   events sit close to their comparison levels.
2. **Prescription events are a counterexample to a simple deterioration story.**
   Their event-window nonemployment level is lower than the comparison at both
   R4/2 and R5/3, yet status change, nonemployment resolution, and onset are
   all higher. A lower level can coexist with more movement.
3. **Resolution is not the same as recovery.** “Nonemployment resolved” means
   a coded employment-status transition in the available rounds. It does not
   identify job quality, hours, earnings, treatment continuity, debt relief,
   or whether the event caused the earlier status.
4. **Later status is not an event-specific outcome.** The event can follow an
   earlier health need, and the comparison group can include events outside
   the window. Month ordering improves chronology but does not identify the
   causal trigger.

## Arrow ledger

| Arrow | Status | Safe conclusion | Missing link |
|---|---|---|---|
| Dated event → payment/burden context | Same-person descriptive | Event-family payment and care/bill/debt context can be aligned before later work screens | Amount owed, due date, balance, household payer, and event-specific obligation |
| Dated event → R4/2 work-status level | Same-person descriptive | Event families show different contemporaneous nonemployment surfaces | Intended need, baseline job, severity, coverage, and event-specific burden |
| R4/2 → R5/3 work-status level | Same-person ordered | Later levels and direction screens are measurable | Job start/end, hours, earnings, schedule, and reason for change |
| Nonemployment → resolution/onset | Same-person descriptive | Movement differs by event family; prescription and acute events show mixed directions | Whether movement is desirable, adequate, voluntary, or event-related |
| Health/payment event → work and household recovery | Open | No current field identifies treatment continuity, bill remedy, or household adaptation | Claim/bill, amount owed, alternatives, payment, care continuation, remedy, and later security |

## Boundary

This synthesis uses existing local MEPS outputs rather than downloading new
respondent files. It preserves the R3/1-to-R4/2 event rule, the later R5/3
clock, separate valid denominators, and BRR uncertainty. It does not create a
row-level merge between the three-family audit and the prescription output
where the source outputs use different valid subsets.

The result is stronger than an annual event-presence tab because it orders a
dated event before later same-person status fields. It remains weaker than a
complete episode because it does not observe the initiating need, feasible
alternatives, exact bill or claim, care decision, institutional response,
remedy, household recovery, trust, political action, switching, or exit.

## Next decisive join

The next qualifying record remains a claim- or bill-level episode linking the
dated event to amount owed, coverage rule, payment obligation, care
continuation or delay, household money/time substitution, institutional
response, and later work or health recovery. Until then, these four event
families are a timing and counterexample surface, not a causal health-cost or
employment result.

## Sources and reproduction

- [MEPS event-to-work two-clock audit](meps-event-work-two-clock-audit-v1.md)
- [MEPS prescription-event six-month follow-up](meps-prescription-event-six-month-followup-v1.md)
- [Four-event work-clock source output](data-meps-event-work-two-clock-audit-2024.json)
- [Prescription-event source output](data-meps-prescription-event-six-month-followup-2024.json)
- [Dated event-to-household-response screen](meps-dated-cascade-event-screen-v1.md)

**Evidence status:** same-person, month-ordered descriptive comparison with
mixed-direction counterexamples; no causal event, recovery, remedy, trust,
political-action, or exit claim is made.
