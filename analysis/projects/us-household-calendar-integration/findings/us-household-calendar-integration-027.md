# Work, care time, and health cost are separate stages of household room

**Status:** provisional non-pooled cross-source bridge · **Checked:** 2026-09-14

## The bounded finding

The current atlas can now place three evidence stages beside one another:

```text
work-limiting status and monthly resources
  -> earnings/hours and job movement
  -> unpaid care and household-time allocation
  -> health status and medical-cost change
  -> household room, recovery, trust, or political meaning
```

The SIPP, ATUS, and MEPS sources do not follow the same person through this
whole chain. Their value is architectural: each closes a different measurement
gap while showing why the stages must not be collapsed.

## Three evidence surfaces

| Source | Direct evidence | What remains open |
|---|---|---|
| SIPP monthly person transitions | Hours-change shares are higher among people reporting a work-limiting condition at each displayed resource band; earnings-change shares use a separate valid universe | Direction, desired hours, accommodation, job quality, care response, and causality |
| ATUS standardized diary contrast | After age, sex, labor-force status, household-child status, and education standardization, eldercare providers show +70.7 eldercare minutes, +16.8 household-work minutes, −19.7 work minutes, −18.4 socializing minutes, and +9.7 travel minutes per diary day relative to nonproviders | Care onset, intensity beyond the diary, recipient outcome, employer response, and health effect |
| MEPS Panel 27 | From 2022 to 2023, 21.0% improved and 22.8% worsened in health status; total health expenditure rose $630.83 per person while out-of-pocket expenditure fell $50.50 | Whether time allocation or work limitation caused health-cost change, and who carried the household cost |

## The substantive interpretation

Household room is not just money. A person can have a resource-band position,
change hours or earnings, spend time providing care, and face a health-cost
change on different clocks. A lower out-of-pocket amount can coexist with
higher total expenditure. A provider can spend less time in paid work and more
time in care and household work without the data showing whether that was
chosen, required, supported, or harmful.

The SIPP result adds an important moderator: people reporting a work-limiting
condition do not occupy the same transition environment as people without one.
But the field does not tell us whether the difference comes from health,
employer accommodation, job access, age, occupation, household support, or
measurement.

The ATUS result shows the time currency that a monthly income record cannot see.
The MEPS result shows that medical expenditure and health status are distinct
currencies. Together they prevent the program from treating a stable job count,
a lower out-of-pocket amount, or a care-day average as proof of recovered
security.

## Counterexamples

- A work-limiting person may retain stable or improving resources through
  accommodation, savings, benefits, family support, or a flexible job.
- A caregiver may lose paid-work minutes without losing welfare if the care is
  chosen and supported; another may lose work involuntarily and have no
  substitute.
- Total health expenditure can rise while out-of-pocket spending falls through
  coverage, and health can improve while costs increase.
- A high time allocation to care does not identify recipient need, quality,
  exhaustion, or later health.
- Similar cross-source patterns do not establish that the same mechanism
  operated for the same household.

## Next end-to-end test

Use a linked or genuinely repeated household/person design that records a dated
health or care event, work-limiting status, desired and actual hours, earnings,
paid/unpaid care, medical spending, coverage, food/housing/utility trade-offs,
employer or provider response, recovery, and later trust or action. Until such
a design is available, preserve the three currencies—money, time, and health
cost—separately.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [ATUS](https://www.bls.gov/tus/)
- [MEPS](https://meps.ahrq.gov/mepsweb/)
- [Machine-readable cross-source record](../../../records/us-material-work-care-health-crosssource-2022-2025.json)

**Evidence status:** non-pooled cross-source bridge. It identifies complementary
measurement stages and open arrows, not a causal burden index or a same-person
material-to-health-to-political pathway.
