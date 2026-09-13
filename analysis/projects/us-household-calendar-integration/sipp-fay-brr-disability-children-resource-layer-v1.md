# SIPP work limitation × children × resources layer v1

**Checked:** 2026-09-13  
**Source:** 2025 SIPP public-use file, 2024 reference year, with official 240-replicate-weight file  
**Unit:** person record by reference month  
**Weight:** `WPFINWGT`; replicate weights `REPWGT1`–`REPWGT240`  
**Method:** Fay BRR, `G=240`, perturbation factor `0.5`

## Why this comparison matters

The broad program needs to see how material pressure is distributed across
intersecting social responsibilities and capacities. A work-limiting condition
can affect available work and earnings; children can increase care and household
coordination; resources can buffer or intensify both. This is a many-person
distributional test, not a story about one household.

```text
work-limiting condition + children in household + resources
  -> work options, care demands, and material room differ
  -> utility pressure, food hardship, and job status appear in different combinations
  -> households and institutions carry, absorb, or redistribute the burden
  -> later care, health, work, trust, or political effects remain separate tests
```

`EDISABL` is the SIPP indicator for a condition that limits the kind or amount
of work a person can do. `RHNUMU18` identifies whether the household has one or
more members under age 18; it does not measure actual caregiving hours or
whether the person is a parent. `THINCPOV` is a monthly household income-to-
poverty-ratio band.

## Verified calculation

- 379,215 primary person-month rows were read.
- 378,291 positive-weight rows matched the replicate file; no unmatched
  positive-weight rows remained.
- All 16 work-limitation × children × resource cells were produced.
- Official status flags and age/universe rules were applied for each outcome.
- Estimates below are percentages; parentheses are Fay-BRR standard errors in
  percentage points. `n` is the valid person-month record count.

## Selected endpoints

| Work-limiting condition | Children under 18 | Resource band | Utility-payment difficulty | Hungry but did not eat | High/marginal food security | One job |
|---|---|---|---:|---:|---:|---:|
| Yes | None | Below 1.00× poverty | 18.11 (1.72), n=9,404 | 41.26 (3.03), n=4,328 | 60.97 (2.23), n=9,404 | 7.88 (1.12), n=9,404 |
| Yes | 1+ | Below 1.00× poverty | 29.77 (5.51), n=1,608 | 35.97 (6.64), n=917 | 54.16 (5.61), n=1,608 | 16.09 (3.16), n=1,608 |
| No | None | Below 1.00× poverty | 10.33 (1.41), n=12,209 | 35.15 (4.07), n=3,085 | 79.62 (1.80), n=12,209 | 28.90 (1.55), n=12,209 |
| No | 1+ | Below 1.00× poverty | 16.43 (2.16), n=7,909 | 24.35 (4.22), n=2,847 | 72.16 (2.46), n=7,909 | 36.18 (1.89), n=7,909 |
| Yes | None | 4.00× or more | 4.44 (0.64), n=15,079 | 35.39 (5.48), n=1,439 | 92.88 (1.05), n=15,079 | 31.99 (1.56), n=15,079 |
| Yes | 1+ | 4.00× or more | 6.74 (2.13), n=2,498 | 24.18 (10.41), n=368 | 89.37 (3.23), n=2,498 | 44.51 (3.68), n=2,498 |
| No | None | 4.00× or more | 2.32 (0.23), n=96,796 | 22.16 (3.03), n=5,233 | 96.39 (0.36), n=96,796 | 68.58 (0.59), n=96,796 |
| No | 1+ | 4.00× or more | 2.67 (0.51), n=38,197 | 13.62 (3.91), n=2,856 | 95.86 (0.65), n=38,197 | 70.74 (0.87), n=38,197 |

## What the pattern shows

### 1. Resources remain a strong condition, but not the whole explanation

Within each work-limitation and children category, utility difficulty generally
falls and high/marginal food security generally rises as the resource band
increases. This is a distributional gradient, not proof that income alone caused
the outcome.

### 2. Children change the level and composition of pressure

Among people with a work-limiting condition below the poverty threshold, utility
difficulty is 29.77% when there is at least one household member under 18,
compared with 18.11% when there is none. High/marginal food security is also
lower in the children-present cell. The corresponding child-present versus
child-absent differences among people without a work-limiting condition are
smaller for utility difficulty and food security, though still visible.

This does not establish that children caused the difference. Household size,
age, relationship to the child, housing, earnings, care availability, and many
other conditions are bundled into the comparison.

### 3. Work-limiting conditions are not reducible to joblessness

The “one job” measure is not a welfare score and does not measure hours, pay,
benefits, stability, or choice. Still, the distribution differs sharply by
work-limitation status and resource band. A person can have one job while also
facing utility difficulty or food hardship; job count alone cannot stand in for
security or bargaining power.

### 4. The counter-pattern matters

The hunger measure does not move monotonically across every intersection. Among
people with a work-limiting condition at 4× poverty or more, the child-present
cell has a lower point estimate for hunger than the child-absent cell, but its
standard error is large (10.41 points) and its valid count is only 368. Among
people without a work-limiting condition, the child-present high-resource cell
also has a lower point estimate than the child-absent cell. These are reasons to
avoid a simple “children always intensify every hardship” story and to measure
food, utilities, work, and care separately.

## Arrow status

| Arrow | Status | Safe conclusion |
|---|---|---|
| Resources × work limitation × children → material conditions | Observed distribution | The intersection is associated with different reported utility and food conditions, with design-based uncertainty. |
| Work limitation → job status | Descriptive association | One-job shares differ, but hours, pay, health, accommodation, and choice are not identified here. |
| Children → care time or household sacrifice | Not measured in this table | Household presence under 18 is not a care-hours measure. |
| Material condition → specific bill, employer, policy, or health event | Open | SIPP fields do not identify the exact trigger or institutional actor. |
| Material condition → recovery, trust, action, or exit | Open | Requires a defined follow-up and meaning/action measures. |

## Limits

- Person weights are used; household-level outcomes repeat across people and
  should not be interpreted as a household-weighted estimate.
- The table uses selected official universes and excludes invalid or nonblank-
  ineligible records; each outcome has its own valid denominator.
- `EDISABL` is a work-limitation measure, not a complete disability taxonomy.
- `RHNUMU18` is household composition, not parenthood, care responsibility, or
  child well-being.
- The reference year is 2024 in the 2025 SIPP release; this is not a causal
  time-series result.
- Sparse cells and large standard errors, especially for hunger, must remain
  visible.
- No inference is made about race, tenure, health, benefits, repairs, trust,
  political action, firm response, or state power from this table alone.

## Next test

Use the same design to condition the intersection on tenure and race/ethnicity,
then add genuinely monthly work, income, and program transitions. The strongest
follow-up would connect a retained person and household to care hours, work
schedule, benefit route, health, and later recovery. Until then, this layer is
evidence that material room, work capacity, and family composition form a joint
social distribution—not evidence of one universal mechanism.

## Reproduction

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_fay_brr.py \
       --group-by EDISABL_RHNUMU18_THINCPOV --official-universes
```

The raw source, derived slice, and JSON output remain outside the repository.

## Official source

- [Census SIPP program](https://www.census.gov/programs-surveys/sipp.html)
- [2025 SIPP data and documentation](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
