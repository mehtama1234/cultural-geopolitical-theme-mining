# Child-care work prevention is followed by mixed earnings movement and lower hours stability

**Status:** provisional official-universe Fay-BRR finding  
**Checked:** 2026-09-16

## Bounded finding

The SIPP monthly person-record screen uses `EWORKMORE`—whether child-care
arrangements prevented a reference parent from working or working more—to
condition next-month earnings and hours direction. It reads 379,215 rows,
identifies 31,992 people, and matches 10,944 pair rows to the official
240-replicate archive.

| Current resource band | Child-care work prevention | Next-month hours same | Earnings increase / decrease |
|---|---|---:|---:|
| Below 1× poverty | Yes | 74.5% (n=71) | 34.8% / 25.0% (n=70) |
| Below 1× poverty | No | 82.6% (n=1,186) | 36.7% / 28.9% (n=1,156) |
| 4× poverty or more | Yes | 92.2% (n=351) | 42.0% / 40.8% (n=351) |
| 4× poverty or more | No | 95.5% (n=9,336) | 43.2% / 42.5% (n=9,283) |

The descriptive pattern is consistent with a care/work constraint that can
coexist with unchanged hours, hours movement, and earnings movement in both
directions. The low-resource prevention-positive cell is too small for a stable
ranking; its hours estimate has a wide interval (the underlying reproduction
output reports an SE of roughly 10 percentage points). At higher resources,
the prevention-positive cell is larger, but the difference in hours stability
is still an association among selected reference parents, not a care effect.

## Why this matters for the end-to-end goal

This is a stronger care proxy than simply observing a household member under
18, but it still does not identify the event that produced the constraint:

```text
child-care arrangement / work prevention
  -> next-month hours and earnings movement
  -> possible household time or material trade-off
  -> recovery, institutional response, trust, or exit
```

The earnings result is deliberately not labeled as loss. In every displayed
cell, earnings increase and decrease shares coexist; an increase may reflect
more work, job composition, pay, or reporting, while a decrease may reflect
care, health, employment, or another shock. Hours stability is likewise not
proof that care was affordable or that work was protected.

## Timing, universe, and limitations

`EWORKMORE` is an annual fall reference-parent measure attached here to a
monthly adjacent-pair screen. The design supplies ordering, not a dated
child-care episode. Its valid universe is restricted by the official
`AWORKMORE` status and reference-parent routing; it is not an all-adult or
household prevalence estimate. Hours and earnings use separate valid-pair
denominators, and person weights do not become household weights.

| Arrow | Status | Safe conclusion |
|---|---|---|
| Child-care work prevention → following earnings/hours direction | Descriptive same-person transition | Direction is mixed; hours are less often unchanged in the prevention-positive cells |
| Child-care arrangement → care minutes or schedule control | Open | Neither is measured by `EWORKMORE` |
| Constraint → dated price, provider, employer, or policy | Open | No trigger or institutional actor is identified |
| Transition → recovery, trust, political action, or exit | Open | Requires a defined later observation |

The calculation uses `WPFINWGT` and all 240 replicate weights with Fay BRR.
Primary and replicate inputs remain outside Git; the [machine-readable
record](../data/sipp-childcare-work-direction-2024.json) preserves hashes,
counts, selected cells, and boundaries. The [analysis
script](../../../../scripts/analyze_sipp_childcare_work_direction.py) defines
the grouping, matching, and variance logic.

## Next decisive test

Use the care-specific universe with a directly measured care/time-loss amount,
desired and actual hours, schedule control, paid/unpaid care, and a later
health, food, housing, or work-continuity outcome. Keep the annual fall versus
monthly clock explicit until a genuinely dated care event is available.

## Official source

- [Census 2025 SIPP data and documentation](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP child-care work-prevention/following-hardship bridge](../sipp-childcare-work-hardship-bridge-v1.md)
