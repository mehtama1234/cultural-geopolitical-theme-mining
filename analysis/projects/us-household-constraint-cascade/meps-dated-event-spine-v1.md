# MEPS dated health-cost episode spine for the household cascade v1

**Checked:** 2026-09-16  
**Status:** dated event spine with bounded follow-up context; not a complete
household episode

## Why this route matters

The SIPP cascade screen supplies adjacent-month utility, work, care, food, and
housing surfaces but no event-level bill or service date. The existing local
MEPS files supply the complementary dated health-cost spine:

```text
first observed office / ER / inpatient event
  -> exact person-panel identity and month
  -> self/family and total event payment
  -> coverage, employment, health, and annual bill context
  -> bounded follow-up health, work, and bill context
```

This is not yet the full chain. It does not reveal whether the person delayed
care, what alternative was available, how the household paid, or whether the
provider/insurer remedied the problem.

## Existing local evidence

The [MEPS first-event ledger](../us-health-cost-household-choice/meps-2024-bounded-episode-ledger-v1.md)
selects one first dated event per person and event family, preventing repeated
encounters from being treated as independent people. Its bounded 2024 screen
reports:

| Event family | First-event people before/same/after R4/2 | Mean self/family payment before/same/after | Follow-up fair/poor health before → after |
|---|---:|---:|---:|
| Office | 12,865 / 506 / 614 | $65.41 / $38.80 / $64.04 | 13.74% → 12.22% / 10.03% → 8.66% / 6.79% → 5.57% |
| Emergency room | 2,128 / 204 / 340 | $148.87 / $104.23 / $90.58 | 27.49% → 26.15% / 21.26% → 19.59% / 19.27% → 14.47% |
| Inpatient | 988 / 101 / 226 | $838.09 / $597.26 / $796.48 | 35.36% → 33.80% / 27.82% → 36.92% / 20.30% → 24.09% |

The payment and health fields are separate weighted context surfaces. “After”
means after the R4/2 reference boundary, not after the event; it must not be
read as recovery.

The [strict inter-round transition layer](../us-health-cost-household-choice/meps-2024-between-round-event-transitions-v1.md)
adds a cleaner baseline/follow-up ordering. People with ER or inpatient events
between R3/1 and R4/2 already had worse baseline health and employment than
people without an event in that window. That baseline selection is itself a
finding and prevents a naive event-effect interpretation.

The [care-delay/adaptation layer](../us-health-cost-household-choice/meps-2024-care-delay-adaptation-v1.md)
supplies the missing household-response vocabulary in a separate same-person
architecture: care delayers report more provider-plan use or inability to pay
for a hypothetical $500 bill, more savings/basic-spending sacrifice, more work
when health needed time off, and more difficulty absorbing time off. Those
fields are not proven to refer to the displayed dated event.

## Arrow status

| Arrow | Status | Safe conclusion | Missing evidence |
|---|---|---|---|
| Health need → observed event | Observed event surface | Event files identify dated office, ER, inpatient, and prescription records | Triggering condition, severity, appointment/search failure, or forgone-care denominator |
| Event → payment | Observed and linked | Event payment is linked to the exact MEPS person and event family | Amount owed, due date, balance, financing, household payer, and payment timing |
| Payment/coverage → care choice | Open | Coverage and event payment condition the feasible-choice problem | Delay, substitution, foregoing, provider alternative, and plan/network terms |
| Care choice → household adaptation | Separate same-person comparison | MEPS care-delay respondents report debt, sacrifice, work/time, and family-care surfaces | Same event ID linking choice to debt, food, housing, work, or unpaid care |
| Event → follow-up outcome | Bounded month/round context | Baseline and follow-up health/work/bill fields can be ordered around an inter-round event | Treatment continuity, recovery, exact episode attribution, and longer follow-up |
| Institutional encounter → remedy | Open | The event can be the anchor for a response ledger | Insurer/provider response, appeal, correction, repeat effort, remedy, and exit |

## What this contributes to the active cascade

MEPS changes the next test from an abstract request for “more longitudinal
data” to a precise linkage specification. The required missing middle is:

```text
dated need or event
  -> amount owed and coverage rule
  -> care continuation, delay, substitution, or foregoing
  -> household money/time/work/care trade-off
  -> institutional response and remedy
  -> one-, three-, and six-month recovery or persistence
```

The SIPP screen can benchmark utility and childcare/work surfaces. MEPS can
anchor dated health-cost episodes. SHED can benchmark coverage transitions,
care foregoing, and adaptation persistence. They should remain separate until
a common person/household key and compatible clocks exist.

## Acquisition and storage decision

No new download is needed for this design pass. The necessary MEPS files are
already available locally under `/tmp/cgtm-meps-2024`; only compact derived
outputs and writeups are committed. A future acquisition is justified only if
it adds a dated bill/claim, household payer or obligation, treatment or care
choice, institutional response, or post-event remedy that cannot be recovered
from the current files.

## Reproduction routes

- [MEPS bounded first-event ledger](../us-health-cost-household-choice/meps-2024-bounded-episode-ledger-v1.md)
- [MEPS inter-round event transitions](../us-health-cost-household-choice/meps-2024-between-round-event-transitions-v1.md)
- [MEPS care-delay/adaptation layer](../us-health-cost-household-choice/meps-2024-care-delay-adaptation-v1.md)
- [MEPS event-payment/bill-context layer](../us-health-cost-household-choice/meps-2024-event-payment-bill-context-v1.md)
- [SIPP unified cascade screen](sipp-constraint-cascade-screen-v1.md)
- [SHED coverage/care panel route](../us-health-cost-household-choice/shed-panel-coverage-care-foregoing-paths-v1.md)

**Evidence status:** existing local MEPS dated-event and bounded follow-up
surfaces integrated as an episode-spine design; no same-episode household
adaptation, remedy, recovery, trust, political-action, or exit claim.
