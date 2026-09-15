# Material pressure is jointly distributed across work limitation, children, and resources

**Status:** official-universe Fay-BRR intersectional finding · **Checked:** 2026-09-13

## The bounded finding

The 2025 SIPP public-use file, representing the 2024 reference year, shows that
material pressure is not adequately described by one income band, one work
status, or one family label. Across person-month records, utility difficulty,
food hardship, food security, and job status vary across the intersection of a
work-limiting condition, household members under 18, and monthly resources.

Among work-limited people below the poverty threshold, utility-payment
difficulty is 29.77% when the household has one or more members under 18,
versus 18.11% when it has none. The corresponding high/marginal food-security
shares are 54.16% and 60.97%. These are weighted descriptive cells, not child,
disability, or income effects.

The resource gradient is substantial, but the endpoints do not form one
universal story. Among work-limited people with one or more household members
under 18, utility difficulty falls to 6.74% at 4× poverty or more, while the
one-job share rises to 44.51%. The high-resource hunger estimate is 24.18% but
has only 368 valid records and a 10.41-point standard error. That counter-pattern
must remain visible rather than being converted into a claim that children
protect or worsen food security.

## What is measured

| Dimension | Operational measure | Boundary |
|---|---|---|
| Work limitation | `EDISABL`, a condition limiting the kind or amount of work | Not a complete disability, health, or accommodation measure |
| Children | `RHNUMU18`, one or more household members under 18 | Not parenthood, caregiving, care hours, or child well-being |
| Resources | Monthly household income-to-poverty ratio `THINCPOV` | Person records repeat household conditions; not a household-weighted estimate |
| Outcomes | Utility difficulty, hunger, high/marginal food security, and one-job status | Separate official universes and valid denominators |
| Uncertainty | 240 Fay-BRR replicate weights, `G=240`, perturbation factor 0.5 | Design-based uncertainty does not remove selection or measurement limits |

The calculation read 379,215 primary person-month rows; 378,291 positive-weight
rows matched the replicate file. All 16 intersection cells were produced in
the underlying calculation, while the machine record preserves selected
low-resource, high-resource, and counter-pattern cells.

## The social route under test

```text
work limitation + household composition + material room
  -> paid work, care alternatives, and utility/food pressure
  -> substitution, delay, borrowing, unpaid labor, or going without
  -> health, schedule control, recovery, trust, and political meaning
```

This pass establishes only the first distributional stage and parts of the
second. It does not observe a dated bill, care episode, employer decision,
benefit route, accommodation, later health result, trust, voting, or collective
action.

## Why the intersection matters

Income alone hides the capacity difference between people with and without a
work-limiting condition. Work limitation alone hides household composition and
resource differences. Household members under 18 identify a coordination
context, but not who provides care or whether children are shielded. The joint
table therefore helps locate where a later time/care or institutional study
should look without pretending that the table explains the mechanism.

The “one job” measure is especially important as a counterexample to a simple
security score. A person can have one job and still face utility difficulty or
food hardship; job count does not measure hours, pay, benefits, stability,
choice, or bargaining power.

## Arrow status

| Arrow | Status | Safe conclusion |
|---|---|---|
| Resources × work limitation × children → material conditions | Observed distribution | The intersection is associated with different utility and food outcomes with design-based uncertainty. |
| Work limitation → job status | Descriptive association | Job shares differ, but hours, pay, health, accommodation, and choice are unmeasured. |
| Children → care burden or sacrifice | Open | Household child presence is not a care-time measure. |
| Material pressure → a specific bill, employer, or policy event | Open | SIPP does not identify the exact trigger or institutional actor. |
| Material pressure → recovery, trust, political action, or exit | Open | Requires a defined same-unit follow-up and direct meaning/action measures. |

## Method and limits

The source is the 2025 SIPP public-use file for the 2024 reference year. The
final person weight is `WPFINWGT`; uncertainty uses `REPWGT1`–`REPWGT240` under
the Census Fay modified-BRR formula. Official status flags and outcome
universes were retained. Household outcomes repeat across people, so these
are person-weighted estimates, not household counts.

The low-resource child-present work-limited cell has a 5.51-point utility SE
and a 6.64-point hunger SE. The high-resource child-present work-limited hunger
cell has a 10.41-point SE. Sparse cells and nonmonotonic endpoints are part of
the finding. No causal ranking should be inferred.

## Next test

Use the same intersection to condition a valid care-time, work-schedule,
benefit-route, or health outcome, then define a one-record-per-household rule
where household claims are necessary. The end-to-end test still requires a
dated pressure or care event, alternatives and schedule control, money/time
substitution, protected and sacrificed outcomes, and later recovery, trust, or
action.

**Evidence status:** reproducible design-based person-weighted intersectional
comparison with explicit universes, uncertainty, counter-patterns, and open
arrows; no causal or complete same-unit societal chain is claimed.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)
- [Machine-readable observation record](../../../records/us-sipp-work-limitation-children-resources-2024.json)
