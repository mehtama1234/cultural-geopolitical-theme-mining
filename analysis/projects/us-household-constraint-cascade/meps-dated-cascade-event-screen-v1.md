# MEPS dated event to household-response screen v1

**Checked:** 2026-09-16  
**Status:** same-person month-ordered descriptive screen; not a causal event
estimate

## The new local test

This pass takes the dated MEPS event spine one step further. For each event
family, it selects the person’s first valid event strictly between the R3/1 and
R4/2 endpoint months, then compares that event-window group with the
complementary round-valid population. It carries event payment and exact
person-panel context alongside R4/2 care delay, medical-bill problems, medical
debt, collector contact, and employment status.

The screen now also accepts the optional HC-254A prescription event file; the
new [prescription-event layer](meps-prescription-event-cascade-v1.md) records
its results separately while leaving the prior three event families unchanged.

```text
first dated event in an inter-round window
  -> event self/family payment
  -> same-person care-delay, bill, debt, collection, and work-status context
```

The event date is month-level. The outcome fields are round-level and do not
identify the event’s bill, claim, or remedy.

## Results

| Event family | Event-window people | Complementary round-valid people | Event-window self/family payment | Cost-related care delay | Medical bill problem | Medical debt | Collector contact | Not employed at R4/2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Prescription | 1,773 | 16,950 | $12.76 | 8.09% vs 6.45% | 8.82% vs 7.48% | 19.45% vs 15.17% | 15.03% vs 13.08% | 37.53% vs 33.42% |
| Office | 3,216 | 15,507 | $66.87 | 6.41% vs 6.64% | 8.01% vs 7.52% | 16.17% vs 15.45% | 13.08% vs 13.30% | 33.35% vs 33.91% |
| Emergency room | 1,101 | 17,622 | $155.52 | 9.59% vs 6.44% | 15.14% vs 7.19% | 24.12% vs 15.10% | 19.75% vs 12.90% | 47.62% vs 32.98% |
| Inpatient | 545 | 18,178 | $733.03 | 6.82% vs 6.60% | 11.13% vs 7.52% | 16.61% vs 15.55% | 14.42% vs 13.23% | 60.13% vs 33.03% |

Each paired percentage is event-window versus complementary round-valid. The
event-window payment is the weighted mean for the first dated event; the
response shares use `PERWT24F` and 128 HC-036BRR flags with field-specific valid
denominators. The employment column is the share with valid `EMPST42=4`, where
the MEPS employed codes are 1–3 and nonemployment is code 4. The complementary
group is not a no-need control: it can contain people with events outside the
inter-round window.

## What this adds

1. **A dated event can be placed before a same-person round context.** The
   screen is more temporally disciplined than an annual event-presence table.
2. **Acute event channels differ.** ER events have higher point estimates for
   bill problems, medical debt, collector contact, and care delay than the
   complementary group; office and inpatient results are less separated on
   this particular outcome surface.
3. **The work-status endpoint separates acute event channels.** Nonemployment
   at R4/2 is 47.62% after an ER event and 60.13% after an inpatient event,
   versus 32.98% and 33.03% in their respective complementary groups. The
   office comparison is 33.35% versus 33.91%. These are level differences,
   not job-loss or event-caused employment estimates.
4. **Payment is still not burden.** The event-window payment mean does not
   identify the amount owed, deductible, balance, household payer, or whether
   the person delayed or forgone care.
5. **The household-response arrow remains only partly observed.** Care delay,
   debt, and bill status are same-person context, not proof that the displayed
   event caused them; employment status is not hours, earnings, schedule
   control, or job quality.

## Weight and timing correction

The first draft of this screen included ESAQ work/time adaptations under
`PERWT24F`. That was methodologically invalid because ESAQ adaptation questions
use `ESAQWT24F` and do not share the HC-036BRR event variance surface. Those
fields are deliberately excluded here. The existing
[MEPS care-delay/adaptation layer](../us-health-cost-household-choice/meps-2024-care-delay-adaptation-v1.md)
remains the correct separate ESAQ-weighted context route.

## Boundaries and counterexamples

- The event may be a consequence of a prior need, not the beginning of the
  household episode.
- Month ordering excludes endpoint ambiguity but not event-day ordering,
  severity, coverage, access, or baseline selection.
- `DLAYCA42`, `PROBPY42`, `MEDDEBT42`, `FWDEBT42`, and `EMPST42` do not identify a claim,
  invoice, payment due date, appeal, provider response, or remedy.
- The nonemployment endpoint is an R4/2 level indicator; it does not measure
  transition from employment, job loss, hours loss, or work causation.
- Similar or lower payment can coexist with greater burden because payment
  does not capture unpaid amounts, deductibles, prior balances, or forgone care.
- The complementary population is not a causal counterfactual and is not
  necessarily event-free.
- No recovery, switching, trust, political-action, or exit outcome is measured.

## Decisive next join

The required next artifact is a claim- or bill-level ledger that links the
dated need/event to amount owed, coverage rule, payment obligation, care
continuation or delay, household money/time substitution, institutional
response, and one-, three-, and six-month recovery. The ESAQ adaptation fields
can then be joined only if a compatible respondent/episode key and weight
design are documented.

## Reproduction

- [Machine-readable event screen](data-meps-dated-cascade-event-screen-2024.json)
- [Analysis script](../../../scripts/analyze_meps_dated_cascade_event_screen.py)
- [MEPS dated event spine](meps-dated-event-spine-v1.md)
- [MEPS inter-round event transition source](../us-health-cost-household-choice/meps-2024-between-round-event-transitions-v1.md)
- [MEPS care-delay/adaptation source](../us-health-cost-household-choice/meps-2024-care-delay-adaptation-v1.md)

Primary HC-256 hash: `b4bde859b39f626345561c05570292bb7264dd92eb76ce0c1a14d6b89076aed5`  
BRR hash: `44f1e5a864c1d318327a0fbd3a0ff48a583c74c3a104aae357032cfbfaa5a32e`  
Office event-file hash: `19e81a7f816ea8bf518dd0a47ac6087bb747f5f0feffb3dd64d36c250864cda4`
Emergency-room event-file hash: `23071ad1ffa7a2abf46721f4388be6b462f2fc6413dbef8323282db276081723`
Inpatient event-file hash: `5a71c7680f11ebb7dfc5e579ea8b63e6fb090b2ff2eb9a943c7abccdc13cb464`
Script hash: `6999deaeedbc1a0c8bb42c6afb8a68fd0eecebb5a5229772f5921a806ca206c5`
Output hash: `72808206961171c77774cc191bc9954e67a2d82eb76f8b7543e77309f174fd38`

**Evidence status:** reproduced dated event-to-context screen; not a complete
same-episode household adaptation, remedy, recovery, trust, political-action,
or exit result.
