# Health-cost episode acquisition protocol v1

**Checked:** 2026-09-21
**Status:** implementation specification; not evidence of a completed causal chain

## Objective

Build the smallest defensible same-unit or valid matched design that can follow
an American health-cost episode from exposure to choice, household trade-off,
institutional response, and later legitimacy or action. The protocol exists to
prevent annual survey percentages, event payments, credit records, and trust
measures from being silently treated as one observation.

## Required unit and clock

The preferred unit is a person nested in a household, with a dated episode
window and a pre-exposure observation. The minimum clock is:

```text
pre-period -> need/bill or coverage event -> decision window
           -> 30/90/180-day outcome windows -> later trust/action window
```

If day-level dates are unavailable, month-level ordering is acceptable only when
same-month observations are flagged as ambiguous. Annual fields can provide
context but cannot be presented as post-event outcomes without a dated bridge.

## Episode schema

| Layer | Minimum fields | Why it matters |
|---|---|---|
| Exposure | person/household ID, need or service type, date, severity/urgency, source | Defines what happened and preserves non-users |
| Access and alternatives | coverage type, network status, deductible/coinsurance, quoted price, travel, wait, provider alternatives, liquid cash/credit | Measures practical room rather than nominal insurance |
| Choice | received, delayed, substituted, abandoned, self-treated, borrowed, sought help; reason and counterfactual | Identifies the behavioral mechanism |
| Obligation | amount billed, amount owed, due date, payment, balance, denial, collections, correction | Separates price, obligation, and actual payment |
| Household substitution | work hours/absence, unpaid care, savings, borrowing, food, housing, medication, rest, family help | Records protected and sacrificed outcomes separately |
| Follow-up | treatment continuity, function, health, employment, income, debt, recovery, repeat need | Tests persistence and reversal |
| Institutional route | provider/insurer/employer/regulator/collector contact, effort, response, appeal, remedy, repeat contact | Identifies whether an institution repaired or transferred burden |
| Meaning and action | attribution, dignity/fairness, trust, blame, complaint, switching, organizing, vote/contact/exit; prior identity | Tests legitimacy without assuming distrust equals withdrawal |

Every field needs its own denominator, missingness rule, timing, and uncertainty.
The design must retain people who received care without later hardship, skipped
care without debt, paid successfully, had no institutional complaint, or changed
trust without the measured cost.

## Preferred identification designs

1. **Within-person event study:** compare pre-event and post-event outcomes for
   a dated bill or coverage change, with prior health, season, and concurrent
   shocks recorded.
2. **Coverage or policy discontinuity:** use eligibility, lottery, rule, or
   network changes with care choice and financial outcomes, then separately test
   trust/action rather than treating access as proof of legitimacy.
3. **Matched episode design:** match people with comparable need/severity,
   resources, geography, and baseline trust who face different prices,
   coverage, wait, or institutional responses.
4. **Repeated panel:** require pre-exposure trust/identity and later action;
   use attrition checks and survey weights, and distinguish reported vote,
   contact, complaint, switching, and exit.

Cross-sectional associations are acceptable for discovery and distribution, but
they must not be promoted to causal arrows. A treatment effect on credit access
does not imply a treatment effect on health, and a trust difference does not
imply political withdrawal.

## Analysis outputs

The first implementation should publish four separate tables:

- care continuation/delay/foregoing by coverage, payment room, urgency, and
  alternatives;
- protected versus sacrificed household outcomes by choice;
- institutional response and remedy by obligation and contact effort; and
- trust, attribution, and action by exposure and remedy, with prior trust and
  identity shown separately.

Report weighted totals and subgroup estimates, valid counts, standard errors or
confidence intervals where supported, missingness, attrition, event-order
ambiguity, and a negative-case table. Never collapse these into a single
“health-cost burden” or “legitimacy” index without a separately justified model.

## Acquisition decision rules

Promote the chain only if the new source or matched design supplies at least
one dated exposure, one observed choice, one event-specific obligation or
alternative, one protected and one sacrificed outcome, and a follow-up measure.
Promote the legitimacy arrow only if trust/action is measured after exposure
with prior trust or identity, attribution, and a defined institutional route.
Otherwise publish a bounded bridge and add the missing field to the queue.

The next concrete candidate is a restricted-access or newly released panel that
can preserve person/household identity across health need, financial response,
and trust/action. MEPS remains the strongest event/payment frame; SHED remains
the strongest care-foregoing/adaptation frame; ANES/GSS/CCES remain the
strongest judgment/action frames. Their public identifiers are not currently
compatible, so the next pass must either acquire a compatible panel or label
the cross-source result explicitly as inference.

## Current evidence boundary

The [end-to-end finding](findings/us-health-cost-household-choice-end-to-end-001.md)
and [status matrix](end-to-end-status-matrix-v1.md) show what is already
supported. The [MEPS bounded event ledger](meps-2024-bounded-episode-ledger-v1.md)
provides exact person/event linkage and payment context, but not care choice,
household adaptation, remedy, trust, or action. This protocol defines the
additional acquisition required to close those arrows.

The [CFPB event-ledger health-cost bridge](cfpb-event-ledger-health-cost-bridge-v1.md)
provides an implementation template for the institutional middle: receipt,
route, handoff, and response can be recorded as events, while verified remedy,
recovery, repeat effort, switching, and trust remain separate fields that must
be acquired rather than inferred.

## Current continuation decision — 2026-09-21

The latest cross-domain bridge makes the missing middle more specific. Existing
SHED evidence can connect care foregoing with debt, savings, borrowing, delayed
purchases, and health; CFPB evidence can expose medical-collection and credit
stages; HTOPS can provide an institution-specific confidence surface. These are
useful adjacent currencies, not one episode. No legitimacy arrow should be
promoted until the same person or a valid matched design preserves the exposure
clock, attribution, and prior trust.

The next authorized acquisition should therefore prioritize one of two routes:

1. **MEPS event/payment route:** retain person/event linkage, month ordering,
   payment or bill-problem fields, coverage, care delay, work and household
   context, and every available follow-up field; stop before claiming a remedy,
   trust, or action outcome when those fields are absent.
2. **Compatible health-cost/politics panel:** require a medical-cost exposure
   tied to a dated or bounded period, care/payment adaptation, institutional
   attribution, prior and later trust, and a separately coded action. Do not
   join public SHED, CFPB, HTOPS, ANES, or CCES summaries as if their
   respondents were the same people.

The minimum promotion test is now explicit: a candidate must supply one
episode-level exposure, one choice or non-use decision, one event-specific
obligation or alternative, one protected and one sacrificed outcome, and a
follow-up. For the care-to-legitimacy arrow it must additionally supply
attribution and prior trust or identity. Otherwise the result belongs in the
cross-theme corridor, not the ranked end-to-end chain.

## Workspace execution boundary — 2026-09-21

The local recheck did not find the raw MEPS files required by the event scripts
under `/tmp/cgtm-meps-2024` (HC-256 person file, BRR file, or HC-254 event
files). The committed JSON and Markdown derivatives preserve prior bounded
results, field audits, and hashes, but they are not a substitute for the raw
inputs and do not support a fresh rerun or extension. Until an authorized
source bundle is restored, the MEPS route remains an acquisition-ready design,
not newly executed same-episode evidence.
