# Annual child-care routes differ across stable SNAP states while transition cells are too sparse

**Status:** Fay–BRR SIPP care-context finding · **Checked:** 2026-09-14

## The bounded finding

The November-to-December SIPP bridge can attach annual fall child-care fields
to the same identified-person SNAP state, but it cannot support a clean monthly
care-transition estimate. The adjacent November-to-December SNAP entry and exit
cells contain only 2–4 valid annual-care records per outcome. Those cells are
therefore preserved as an acquisition warning, not interpreted as population
rates.

The stable-state context is more measurable. Among valid reference-parent pairs,
stable nonreceipt (`no -> no`) showed 31.02% paid child care, 5.19% child-care
assistance, and 3.42% reported care arrangements preventing work or more work.
Stable receipt (`yes -> yes`) showed 23.94% paid care, 14.64% assistance, and
7.43% work prevention. These are annual/reference-year care characteristics
attached to a stable monthly SNAP state—not evidence that SNAP caused any care
route or that lower paid care means lower care need.

## Direct evidence

| November → December SNAP state | Annual paid care | Annual assistance | Annual care prevented work | Valid pairs |
|---|---:|---:|---:|---:|
| No → No | 31.02% (SE 1.25) | 5.19% (SE 0.66) | 3.42% (SE 0.45) | 1,783 / 1,783 / 2,295 by field |
| Yes → Yes | 23.94% (SE 3.11) | 14.64% (SE 2.59) | 7.43% (SE 1.88) | 259 / 259 / 351 by field |

The intervals are Fay–BRR sampling intervals. The valid denominators differ by
field because the official care universes differ. The stable-SNAP group is
small, and the comparison is selected rather than a matched treatment/control
design.

## Interpretation and counterexamples

The pattern is consistent with a public-system and household-room question:
stable receipt coexists with more reported child-care assistance and work
prevention, while paid-care use is lower. But several explanations remain open:
household composition, child-care need, work schedules, provider access, income,
eligibility, unpaid family care, and reporting can all shape the route.

Lower paid care is not proof of lower care burden. Higher assistance is not proof
that SNAP caused assistance, and work prevention is not a monthly time-loss
measure. The tiny entry/exit cells are a counterexample to the temptation to
read every same-year care field as an observed transition outcome.

```text
annual care route and household room
  -> stable SNAP state is observed
  -> paid care, assistance, and work prevention differ by selected state
  -> monthly care change, notice, effort, adequacy, trust, and recovery remain open
```

## Next test

Acquire a same-episode or panel design that records the dated care need, provider
route, payment and assistance decision, hours lost, employer flexibility,
SNAP notice/effort/amount, household resources, and following work or care
recovery. A broader monthly transition universe should condition on the annual
care characteristic without treating it as a monthly outcome.

## Sources and reproduction

- [SIPP SNAP context layer](../sipp-snap-transition-context-fay-brr-layer-v1.md)
- [Machine-readable annual-care context record](../../../records/us-sipp-snap-annual-childcare-context-2024.json)
- [Machine-readable stable-state childcare record](../../../records/us-sipp-snap-stable-state-childcare-2024.json)
- [Childcare reproduction audit](../sipp-snap-transition-childcare-reproduction-audit-2026-09-14.json)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

**Evidence status:** reproducible annual-care context comparison with explicit
monthly/annual boundary; no SNAP effect, monthly care-change, or security claim.
