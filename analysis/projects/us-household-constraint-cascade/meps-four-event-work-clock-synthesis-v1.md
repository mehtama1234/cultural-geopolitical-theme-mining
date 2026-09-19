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
