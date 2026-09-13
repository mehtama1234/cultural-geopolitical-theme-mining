# SHED panel financial-condition, health, and care paths v1

**Checked:** 2026-09-13  
**Unit:** recontacted US adult respondent, 2024 to 2025  
**Panel:** 4,419 paired respondents with a 2025 `panel_weight` and a valid
financial-condition path  
**Method:** weighted descriptive transitions; no design-based variance or
causal estimate

## Why this pass matters

The existing SHED panel layer showed that financial adaptations persist or
reverse across the same respondents. This extension asks whether a financial
condition path is accompanied by movement in self-rated health or by entry and
exit from unpaid adult care.

```text
financial condition changes
  -> health may worsen, hold, or improve
  -> unpaid care responsibility may enter or leave
  -> work, time, consumption, family, trust, and political meaning may change
```

The last arrow is not measured here. This is a many-person longitudinal bridge,
not a one-household explanation.

## Results

### Health direction by financial-condition path

| 2024 → 2025 financial condition | Health worsened | Health unchanged | Health improved |
|---|---:|---:|---:|
| Financial condition worsened (804 pairs) | 18.8% | 69.0% | 12.2% |
| Same broad condition (2,866 pairs) | 15.9% | 72.9% | 11.2% |
| Financial condition improved (749 pairs) | 16.5% | 68.8% | 14.6% |

Most respondents stayed in the same broad health category in every financial
path. Financial improvement did not automatically produce health improvement,
and financial worsening did not imply health worsening for most respondents.
This is a useful counterexample to a single-direction hardship story: health,
money, care, and time can move on different schedules.

### Unpaid adult-care transitions

| 2024 → 2025 financial condition | Adult-care entry | Adult-care exit |
|---|---:|---:|
| Financial condition worsened | 10.6% (655 pairs) | 43.3% (149 pairs) |
| Same broad condition | 6.5% (2,447 pairs) | 36.2% (419 pairs) |
| Financial condition improved | 7.5% (627 pairs) | 45.9% (122 pairs) |

Entry is more common in the financially worsened path than in the stable or
improved paths, but the comparison is descriptive and the entry cells include
many kinds of adult-care situations. Exit rates are similar enough to show why
care cannot be treated as a simple permanent burden: care responsibility can
begin or end while financial condition moves in any direction.

The care transition denominator is conditional: entry uses respondents who
reported no unpaid adult care in 2024, while exit uses respondents who reported
adult care in 2024. Health direction likewise uses only respondents with valid
health categories in both waves.

## What this adds to the societal trend map

1. **Material security and health are related but not synchronized.** The
   panel supports a distribution of paths, not a universal household sequence.
2. **Care is a changing social role.** Entry and exit provide a better societal
   measure than treating everyone with a care-related response as permanently
   caregiving.
3. **A financial recovery can coexist with unchanged or worse health.** This
   prevents “recovery” from being defined as one money category alone.
4. **The next open bridge is time and meaning.** The panel does not measure
   care hours, schedule control, the care recipient's outcome, the trigger,
   attribution, trust, collective action, voting, or institutional remedy.

## Boundaries and counterexamples

- SHED condition, health, and care fields are self-reported annual measures;
  they do not identify a dated bill, diagnosis, caregiving event, or policy.
- The financial-condition path is ordinal and broad. It is not a continuous
  income or wealth change and does not establish direction of causation.
- The adult-care field identifies reported unpaid adult care, not hours,
  intensity, relationship, or whether the respondent became a primary carer.
- The panel weight supports descriptive weighting, but this pass does not
  estimate standard errors or fully model recontact selection.
- A necessary counterexample is visible in the health table: many respondents
  in the worsened financial path had unchanged or improved self-rated health,
  while some in the improved path had worsened health.

## Reproduction

```text
python3 scripts/analyze_shed_panel_health_care_paths.py \
  --old /path/to/SHED_public_use_data_2024_(CSV).zip \
  --new /path/to/SHED_2025.csv.zip \
  --output /tmp/shed-panel-health-care-paths.json
```

The calculation uses the official [Federal Reserve SHED data
release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
Raw files and generated JSON are not committed.

Related: [SHED panel persistence](shed-2024-2025-panel-persistence-layer-v1.md),
[care, health, and price adaptation](../us-health-cost-household-choice/shed-2024-care-health-adaptation-layer-v1.md),
and the [broad next-pass queue](../../US-BROAD-NEXT-PASS-QUEUE_V1.md).
