# Political identity conditions the place-context comparison

**Status:** provisional subgroup comparison · **Checked:** 2026-09-14

The capacity/mobility cells do not have one political meaning once broad party
identity is retained. In the 2024 CES county-keyed comparison, federal trust and
civic action differ more sharply across party groups than across the four place
cells alone. This is a required counterweight to reading county capacity as a
direct political cause.

## Federal trust and civic action

| Capacity/mobility cell | Party group | CES respondents | Federal trust | Civic action | Reported voted |
|---|---|---:|---:|---:|---:|
| High capacity / high zero-vehicle | Democratic-leaning | 9,407 | 49.53% | 43.87% | 97.53% |
| High capacity / high zero-vehicle | Independent | 1,932 | 27.48% | 22.72% | 91.85% |
| High capacity / high zero-vehicle | Republican-leaning | 4,736 | 34.19% | 37.90% | 98.28% |
| High capacity / low zero-vehicle | Democratic-leaning | 3,754 | 43.63% | 47.92% | 98.46% |
| High capacity / low zero-vehicle | Independent | 899 | 23.60% | 22.57% | 94.40% |
| High capacity / low zero-vehicle | Republican-leaning | 2,960 | 29.04% | 41.09% | 98.76% |
| Low capacity / high zero-vehicle | Democratic-leaning | 3,471 | 46.62% | 41.52% | 96.53% |
| Low capacity / high zero-vehicle | Independent | 907 | 31.08% | 21.65% | 90.40% |
| Low capacity / high zero-vehicle | Republican-leaning | 2,178 | 34.06% | 31.94% | 98.60% |
| Low capacity / low zero-vehicle | Democratic-leaning | 3,292 | 47.84% | 40.13% | 98.62% |
| Low capacity / low zero-vehicle | Independent | 999 | 25.46% | 24.38% | 90.04% |
| Low capacity / low zero-vehicle | Republican-leaning | 3,573 | 30.95% | 35.90% | 98.21% |

Party identity organizes the institutional-meaning outcomes: Democratic-
leaning respondents report higher federal trust in every displayed cell, while
independents report the lowest trust and civic action. Civic action still varies
within party and place—for example, Democratic-leaning respondents range from
40.13% to 47.92%—so party identity does not erase local context. Reported voting
is high in all displayed groups and should not be treated as the same outcome as
trust or civic action.

## Interpretation boundary

The party grouping uses CES `pid7` codes 1–3 for Democratic-leaning, 4 for
Independent, and 5–7 for Republican-leaning. The small other/unknown cells are
not used for the reader-facing comparison. These are descriptive conditioning
groups, not a causal adjustment: identity may precede the place experience,
co-vary with information and selection, or itself reflect prior local meaning.

The county cells still do not measure which respondent used a business, clinic,
store, transit route, or public system; the data do not record the respondent's
bill, wait, service outcome, blame, belonging, or reason for civic action. No
complex-survey standard errors are estimated here, and county FIPS does not make
each county representative.

The [machine-readable subgroup record](../../../records/us-cces-local-capacity-trust-action-party-2024.json)
preserves all 16 cell-by-party observations, valid universes, thresholds,
weights, hashes, and counterinterpretations. The [reproduction script](../../../../scripts/analyze_ces_local_capacity_trust_action_party.py)
preserves the party recode and endpoint definitions.

**Evidence status:** compared. Party identity is a measured conditioning layer
that materially changes the interpretation of place-context trust/action
patterns; direct local experience, attribution, causality, and institutional
response remain open.
