# US broad retained same-unit bridge matrix v1

**Checked:** 2026-09-18  
**Purpose:** identify what the strongest retained same-unit routes actually
close in the broad end-to-end model. This is a bridge audit, not a pooled
estimate or a claim that the rows describe the same people.

## Required chain

```text
dated condition or event
  -> alternative / non-use
  -> money, time, access, or control trade-off
  -> institutional response
  -> protected or sacrificed outcome
  -> verified remedy / recovery
  -> persistence
  -> meaning, trust, action, or exit
```

| Retained route | Same-unit evidence actually observed | Strongest closed bridge | Still missing or weak |
|---|---|---|---|
| [MEPS dated event → later panel](projects/us-household-constraint-cascade/meps-event-six-month-followup-v1.md) | Person-level event window before R4/2 context, then R5/3 health and employment levels and conditional transitions; BRR-weighted descriptive denominators | Dated event → later health/work status or transition | Event may follow the real need; no alternative, payer/claim identity, treatment continuity, institutional response, verified remedy, trust, action, or exit |
| [SHED 2024→2025 persistence](projects/us-household-financial-pressure/shed-2024-2025-panel-persistence-layer-v1.md) | Same respondent’s financial condition and reported substitutions, reduced use, borrowing, savings cuts, delayed purchases, and extra work across two waves | Financial pressure/adaptation → persistence or partial reversal | Trigger is not transaction-dated; alternatives, actor, institutional response, protected outcome, remedy, trust, action, and exit are absent |
| [CCES 2010→2014 job-loss panel](projects/us-cost-trust-politics/cces-panel-job-loss-political-followup-v1.md) | Same panel respondent’s earlier reported job loss/benefit cut, later insurance status, Congress judgment, contact, and local political action | Earlier work disruption → later institutional judgment/action | Separation date, employer, alternatives, trade-off, remedy, recovery, attribution change, and causal interpretation are absent |

## What this proves

The broad program has real longitudinal bridges at three different points in
the chain:

1. **MEPS** supplies event-to-later-outcome timing.
2. **SHED** supplies adaptation persistence and reversal.
3. **CCES** supplies later judgment and action after a prior disruption.

Together they support a structured research model. They do **not** support
joining medical events, financial adaptation, and job loss into one household
or one population pathway. The missing middle is not merely “more data”; it is
specific fields: usable alternatives, event-specific institutional response,
verified remedy or recovery, and direct meaning/action after the episode.

## Acquisition consequence

The next high-value route must preserve a same-unit key and add at least:

- a dated or bounded trigger and responsible actor;
- the alternative, non-use, or refusal decision;
- money, time, access, or control cost;
- institutional response and remedy receipt or defined outcome follow-up;
- later persistence, trust, action, switching, or exit.

An aggregate exposure, complaint, settlement, or sentiment cross-tab does not
fill these fields. The authorized UAS/PSID/HRS routes remain the strongest
documented acquisition candidates; the retained MEPS, SHED, and CCES routes
remain the comparison anchors and counterexamples.

## Interpretation boundary

All three routes are descriptive or compared designs with source-specific
weights, missingness, selection, and timing limits. A bridge status means the
specified adjacent stages are observed for the same unit; it does not mean the
upstream condition caused the downstream result.
