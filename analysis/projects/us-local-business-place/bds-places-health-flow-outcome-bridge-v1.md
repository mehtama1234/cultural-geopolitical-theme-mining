# BDS–PLACES health-sector flow/outcome bridge v1

**Checked:** 2026-09-18  
**Question:** Does positive health/social-assistance job flow correspond to a
different county-level social-need or routine-care profile?

## Result in plain words

Not in this bounded descriptive screen. The 2023 BDS health-sector flow was
joined by county FIPS to the retained CDC PLACES 2025 county release, whose
data year is 2023. Among 2,878 counties with a reported BDS health net-job
rate and at least one selected PLACES measure, the negative-net and
nonnegative-net groups had nearly identical medians for several measures:

| PLACES measure | Negative BDS health net-job rate | Nonnegative BDS health net-job rate |
|---|---:|---:|
| Food insecurity | 14.9% | 14.8% |
| Lack of reliable transportation | 8.1% | 8.1% |
| Routine checkup in past year | 78.4% | 78.4% |
| Lack of health insurance | 9.9% | 10.0% |
| Frequent mental distress | 17.1% | 17.3% |

This is not evidence that health-sector flows have no effect. It is evidence
that county employer flow alone does not identify care use, adequacy, or lived
health change. The units and mechanisms remain separate.

## Sources and reproduction boundary

- [CDC PLACES portal](https://www.cdc.gov/places/)
- [CDC PLACES 2025 county release](https://data.cdc.gov/d/swc5-untb), retained file SHA-256: `0f093ce4a185a46eaaa53a09d556cbd37dee7d6d8059666c1a08d03db754d73f`
- [2023 BDS county–sector CSV](https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_st_cty_sec.csv)
- BDS retrieval: transient 12 MB suffix containing all 60,686 2023 rows; suffix SHA-256: `988039900c4244fba737cbe2bd37c37d2bf42f81d88121207ed9d842cb5a7d7b`.

The PLACES file contains modeled county estimates and different measure
universes: food, transportation, and housing-type measures do not necessarily
cover the same counties as routine checkup or insurance measures. The BDS
health net-job sign is defined from reported `net_job_creation_rate`; rows
marked `D` or `N` were excluded rather than treated as zero.

The compact derived comparison is stored in
`data/bds-places-health-flow-outcome-2026-09-18.json`.

## What this adds to the atlas

```text
health-sector employer opening/closing and job flow
  -> [open] provider capacity and reachable care
  -> modeled county social need / routine-care profile
  -> [open] resident use, delay, work/time cost, recovery, trust, and action
```

The join supplies a measured outcome surface without pretending that the
county employer flow caused it. It also preserves a useful counterexample:
counties with negative health-sector net job flow do not automatically have
higher or lower modeled burden across all selected measures.

## Boundaries and next test

Both sources are county aggregates; PLACES is modeled and BDS is an employer
flow. The comparison is not a panel of residents, a provider-availability
measure, a causal estimate, or an appointment/use record. The next decisive
test is a small dated care episode with provider/site availability, travel or
wait, insurance/price, attempted and completed use, and a household/work/time
consequence. Preserve the near-null county counterexample when interpreting
that episode evidence.
