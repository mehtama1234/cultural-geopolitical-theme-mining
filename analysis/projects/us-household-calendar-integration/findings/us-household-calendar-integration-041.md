# Household children alter the sparse low-resource work transition screen, but not the high-resource earnings split

**Status:** provisional official-universe Fay-BRR finding  
**Checked:** 2026-09-15

## Bounded finding

The SIPP monthly person-record screen now conditions next-month earnings and
hours direction on three simultaneous surfaces: the current resource endpoint,
a reported work-limiting condition, and whether the household includes a
member under 18. It reads 379,215 primary rows, identifies 31,992 people, and
matches 26,427 pair rows to the official 240-replicate archive.

The most defensible result is a counterexample to a single “work limitation
means hours loss” story. At the lower resource endpoint, hours are unchanged
in 63.1% of valid pairs for people with a work-limiting condition and a
household member under 18, compared with 83.0% for the corresponding
work-limited/no-child cell. But the child-present low-resource cell is sparse
(`n=55`) and imprecise (SE 10.8 percentage points). At four times poverty or
more, earnings move in both directions among work-limited people with children:
42.3% increase and 44.6% decrease (`n=619`).

| Current resource / condition | Household under 18 | Next-month hours same | Next-month earnings increase / decrease |
|---|---|---:|---:|
| Below 1× poverty; work-limited | Yes | 63.1% (SE 10.8; n=55) | 51.9% / 33.1% (n=55) |
| Below 1× poverty; work-limited | No | 83.0% (SE 7.6; n=93) | 31.9% / 21.4% (n=93) |
| 4× poverty or more; work-limited | Yes | 89.9% (SE 2.3; n=630) | 42.3% / 44.6% (n=619) |
| 4× poverty or more; work-limited | No | 96.2% (SE 1.2; n=304) | 40.4% / 37.9% (n=299) |

The hours and earnings columns use separate valid-pair universes. “Same” hours
does not mean stable income, and an earnings increase does not mean improved
security. A household member under 18 is not a care-hours measure, a parent
indicator, or evidence that children caused the transition.

## Interpretation

The result supports a more precise material/time/care question:

```text
resource room + work limitation + household composition
  -> different feasible work/time patterns
  -> earnings can rise, fall, or remain unrelated to hours
  -> care responsibility, accommodation, health, and household support remain open
```

The low-resource hours contrast is directionally notable but should not be
ranked as a stable subgroup effect because both work-limited cells are small.
The high-resource work-limited cells provide a stronger counterexample: hours
are usually unchanged, while earnings still split between increases and
decreases. This is consistent with changes in pay, job mix, or reporting rather
than a simple hours mechanism, but those mechanisms are not observed here.

## Arrow status and limits

| Arrow | Status | Safe conclusion |
|---|---|---|
| Resources × work limitation × household composition → following hours/earnings | Observed descriptive transition | Same-person monthly direction differs across some sparse cells; uncertainty remains visible |
| Household member under 18 → care time or work sacrifice | Open | `RHNUMU18` does not identify care responsibility or minutes |
| Work limitation → earnings or hours direction | Descriptive association | Direction is mixed; no causal or welfare interpretation |
| Material condition → dated bill, employer, accommodation, or policy | Open | No specific trigger or actor is recorded |
| Transition → recovery, trust, political action, or exit | Open | Requires a defined follow-up with those outcomes |

The calculation uses `WPFINWGT` and all 240 replicate weights with Fay BRR
(perturbation factor 0.5). Primary and replicate inputs remain outside Git;
the [machine-readable record](../data/sipp-resource-worklimitation-children-direction-2024.json)
preserves hashes, counts, selected cells, and the boundary. The [analysis
script](../../../../scripts/analyze_sipp_resource_worklimitation_children_direction.py)
defines the grouping and matching logic.

## Next decisive test

Replace household composition with an actual care or child-care constraint,
retain the same monthly person key, and add desired hours, schedule control,
paid/unpaid care, benefit route, and a later health or material outcome. Until
then, this is evidence of heterogeneous work transitions under different
resource and household contexts—not evidence of a care-induced earnings loss
or recovery.

## Official source

- [Census 2025 SIPP data and documentation](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP material/time/care acquisition plan](../material-time-care-linkage-acquisition-plan-v1.md)
