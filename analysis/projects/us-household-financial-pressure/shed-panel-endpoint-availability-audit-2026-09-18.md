# SHED panel endpoint-availability audit v1

**Checked:** 2026-09-18  
**Status:** retained-artifact availability boundary; no new estimate

## Purpose

The SHED 2024–2025 recontact work now supports same-respondent financial
condition, household adaptation, health direction, care, and income-path
comparisons. This audit asks whether the retained machine-readable outputs also
contain the later endpoints needed for the program's end-to-end bridge:

```text
material condition or event
  -> adaptation and practical room
  -> attribution, trust, or institutional meaning
  -> distinct action, remedy, recovery, or exit
```

The answer is a bounded **no** for the retained panel surface.

## What is available

The committed panel outputs preserve:

- 4,419 shared-respondent 2024–2025 pairs with a valid 2025 panel weight;
- 4,163 pairs with a compatible self-rated-health path;
- broad financial-condition transitions;
- reported cheaper purchasing, reduced use, savings reduction, borrowing,
  delayed purchases, extra work, and emergency-fund states;
- adaptation persistence, re-entry, reversal, and income/condition-path
  conditioning; and
- compatible health and care transition surfaces.

These outputs are sufficient to describe repeated material adaptations and
partial recovery or reversal for the same respondent. They do not identify a
dated bill, purchase, provider, creditor, policy encounter, or other discrete
trigger.

## Endpoint availability

| End-to-end stage | Retained SHED panel surface | Promotion status |
|---|---|---|
| Material condition | 2024–2025 broad condition path | Available for descriptive linkage |
| Household adaptation | Repeated adaptation and re-entry fields | Available for descriptive linkage |
| Health/care context | Health direction and care-path outputs | Available for compatible paired universes |
| Actor or responsibility | No retained field/output | Open |
| Trust or institutional confidence | No retained field/output | Open |
| Civic or political action | No retained field/output | Open |
| Verified remedy or recovery | No retained field/output | Open |
| Switching, non-use, or practical exit | No retained field/output | Open |

The persistence layer already states that the panel does not connect these same
respondents to later trust, attribution, civic action, or voting. The endpoint
audit makes that boundary machine-readable and adds remedy, recovery, and exit
because those are also required by the current stage-coverage contract.

## Interpretation

The panel advances the program's **material condition → repeated adaptation or
reversal** arrow. It does not advance the **adaptation → meaning/trust/action**
arrow, and it cannot be used to infer practical exit or restored security.
Another SHED cross-tab would refine the observed adaptation surface but would
not supply the missing endpoint. The next aligned route is therefore a
respondent-level event-compatible source with a dated trigger, alternatives,
institutional response, and later trust or action, subject to retention,
missingness, weighting, and timing checks.

## Limits

- The audit covers the committed JSON outputs and their reproduction metadata;
  the raw SHED archives are not retained in the repository or current temporary
  acquisition directory.
- Absence here means absence from the retained analytical surface, not a claim
  that no SHED release anywhere contains any related question.
- The panel estimates remain weighted descriptive transitions without
  design-based variance or causal estimation.

## Machine record

See [the machine-readable endpoint audit](data/shed-panel-endpoint-availability-audit-2026-09-18.json).
Related: [SHED panel persistence](shed-2024-2025-panel-persistence-layer-v1.md),
[adaptation by health direction](shed-panel-adaptation-health-path-layer-v1.md),
and the [program next-pass queue](../../US-BROAD-NEXT-PASS-QUEUE_V1.md).
