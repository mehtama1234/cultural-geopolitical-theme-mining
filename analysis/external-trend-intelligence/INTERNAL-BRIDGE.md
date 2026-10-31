# External-to-internal bridge

This is the second stage of the new goal. It begins only after an external
candidate has been compared across independent sources and retained with a
counter-signal.

## What a bridge is

A bridge is a bounded test of whether an externally observed trend is relevant
to one company, workflow, customer group, workforce group, product, or place.
It is not a claim that the external source followed the same company or that a
theme match proves causality.

Use [`internal-bridge-schema.json`](internal-bridge-schema.json) and copy
[`internal-bridge-template.json`](internal-bridge-template.json) for each test.

## Required order

1. Name the external candidate and exact observation records.
2. Name the company, internal system, snapshot, owner, and entity key.
3. State external and internal geography, period, unit, and denominator
   separately.
4. Choose the join basis: exact identifier, documented crosswalk, aggregate
   comparison, or no valid join.
5. State the hypothesis and the measurable outcome before looking for a result.
6. Preserve unmatched, incompatible, missing, and suppressed records.
7. Record privacy, access, retention, and redistribution limits.
8. Name a falsifier and a decision owner.

## Valid and invalid connections

| Connection | Valid? | Why |
|---|---|---|
| Exact company or person identifier shared by both sources | Potentially | Still requires period, geography, unit, denominator, and rights checks |
| Versioned crosswalk documented by the source owner | Potentially | Mapping uncertainty and unmatched cases remain visible |
| Same industry label or IBIS category | No, by itself | Category context is not entity identity or company outcome |
| Similar company name or Inc. 5000 appearance | No, by itself | Names and rankings do not prove continuity, mechanism, or exposure |
| Same month or same broad theme | No, by itself | Coincident timing is not a causal or entity-level join |
| External trend compared with an internal aggregate | Sometimes | Must be explicitly labeled aggregate comparison, not individual linkage |

## Release rule

No internal bridge should be shown as an established company finding until the
identity, comparability, rights, missingness, counterexample, and falsifier
checks are reviewed. A failed or impossible join is a useful result and must
be retained rather than silently replaced with a weaker match.
