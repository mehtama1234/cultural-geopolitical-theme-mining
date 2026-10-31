# Bounded company-pilot validation protocol

This protocol defines the minimum evidence required before a company pilot can
be called validated. A pilot is a decision test, not proof that an external
trend caused a company outcome.

## Entry gate

The linked external candidate must be marked `qualified_external_trend` in the
qualification matrix, with source identity, comparable unit/population/
geography/period, independence review, persistence, counter-signal, falsifier,
and backtest evidence. A pilot remains `design_only_external_gate` while any
gate is missing.

## Pre-registration

Before access to internal data, record:

- company, business unit, decision owner, and decision to be informed;
- internal dataset, snapshot/query, entity identifier or documented aggregate
  basis, geography, period, unit, and denominator;
- external-to-internal crosswalk and expected unmatched cases;
- primary outcome, secondary outcomes, comparison group, and expected
  direction;
- privacy class, lawful access basis, retention limit, and redistribution rule;
- falsifier, stop rule, and analysis owner.

## Validation stages

1. **Access validation:** data owner and rights/privacy review are approved.
2. **Identity validation:** identifiers or aggregate comparison basis reconcile;
   unmatched, suppressed, and missing records remain visible.
3. **Measurement validation:** external and internal units, periods,
   populations, and geography are stated separately and are not silently
   substituted.
4. **Outcome validation:** the primary outcome is observed with a pre-specified
   comparison and uncertainty; missing outcomes are not coded as zero.
5. **Robustness validation:** results survive the falsifier, reasonable
   alternative definitions, and a held-out or later-period check where one is
   possible.
6. **Decision validation:** the decision owner records what changed, what did
   not change, and whether the result was useful despite uncertainty.

## Final states

- `approved_test`: access and pre-registration complete; analysis may begin.
- `validated_useful`: all validation stages complete and decision usefulness is
  documented.
- `rejected`: the pilot failed a pre-specified gate or rights/privacy review.
- `inconclusive`: analysis completed but the falsifier or measurement boundary
  prevents a decision claim.

No final state upgrades the external trend itself or authorizes reuse outside
the registered decision context.
