# Ohio place option-stack synthesis v1

**Checked:** 2026-09-18  
**Scope:** 2023 Ohio county employer flow, mobility context, modeled health
burden, and current institutional shortage designations

## What the completed Ohio stack can say

The four bounded panels now form a coherent place-level sequence:

```text
sector-specific employer flow
  + vehicle and commute constraint context
  + modeled health/social-need measures
  + formal HPSA component designations
  -> [open] reachable provider/service alternative and completed use
  -> [open] household time, price, work, recovery, trust, or action
```

The evidence supports a conditional, not causal, reading. High-zero-vehicle
Ohio counties show higher modeled transportation, food, mental-distress, and
insurance burdens, while routine-checkup medians are nearly unchanged. Their
health and food employer-flow profiles are weaker in the complete four-sector
panel. But the HRSA surface shows that formal shortage designations are mostly
tract- or population-shaped objects, so neither employer flow nor HPSA row count
can be treated as resident-level care access.

## Core comparison

| Layer | Low zero-vehicle group | High zero-vehicle group | Evidence status |
|---|---:|---:|---|
| Ohio counties in PLACES panel | 44 | 44 | observed denominator |
| Median zero-vehicle household share | 4.515% | 7.435% | observed ACS aggregate |
| Median health-sector net-job rate, complete BDS panel | 3.466% | 1.001% | compared county-sector aggregate; n=25 per group |
| Median accommodation/food net-job rate, complete BDS panel | 5.535% | 4.296% | compared county-sector aggregate; n=25 per group |
| Median modeled routine-checkup prevalence | 77.05% | 76.95% | estimated PLACES county measure |
| Median modeled food insecurity | 13.20% | 15.95% | estimated PLACES county measure |
| Median modeled transportation insecurity | 7.45% | 8.80% | estimated PLACES county measure |
| Counties with designated HPSA component | 39/44 | 42/44 | observed current administrative designation |
| Designated HPSA component rows | 197 | 942 | observed rows; not a shortage rate |

The HPSA row difference is deliberately not interpreted as a fivefold provider
or shortage difference. In the high-zero-vehicle group, 845 of 942 designated
rows are census-tract components; in the low-zero-vehicle group, 144 of 197
are tract components. Granularity, population object, and overlap change the
row count.

## Counterexample retained

County `39089` shows why the stack cannot be reduced to one direction. Its
zero-vehicle share is 5.338% and its long-commute share is 41.540%. Its 2023
sector net-job rates are:

| Retail | Transportation | Health/social assistance | Accommodation/food |
|---:|---:|---:|---:|
| -2.997% | 96.707% | 3.466% | 3.572% |

Its modeled PLACES values include 77.2% routine checkups, 7.0%
transportation insecurity, 12.2% food insecurity, and 18.1% frequent mental
distress. The transport flow may be denominator-sensitive; the comparison is
retained as a guardrail, not as a causal case study.

## Arrow ledger

| Arrow | What is actually observed or estimated | Status | What remains open |
|---|---|---|---|
| Place type / mobility context → sector flow | ACS vehicle/commute aggregates aligned to same-state BDS county-sector rates | Compared | Causes, firm identity, survival, worker quality |
| Mobility context → modeled burden | High-zero-vehicle group has higher modeled social-need medians | Compared / estimated | Resident-level exposure, travel, price, use |
| Employer flow → modeled care/social outcome | Health-flow sign changes less than the mobility split in this Ohio screen | Compared / estimated | Provider reach, treatment, causal timing |
| County → formal shortage object | Current HPSA designations identify tract, single-county, and unknown components | Observed administrative classification | Designated population’s actual care and provider availability |
| Nominal capacity → reachable alternative | Not measured | Open | Site, hours, accepting provider, travel/wait, fare, appointment |
| Reachable alternative → completed use/outcome | Not measured | Open | Attempt, completion, delay, substitution, health/work consequence |
| Outcome → meaning/action/exit | Not measured | Open | Trust, complaint, switching, organizing, political response |

## Sources and boundaries

- [BDS metro/nonmetro turnover profile](bds-rural-urban-turnover-profile-v1.md)
- [BDS–ACS Ohio mobility panel](bds-ohio-mobility-panel-v1.md)
- [BDS–ACS–PLACES Ohio outcome panel](bds-ohio-places-outcome-panel-v1.md)
- [Ohio HPSA component surface](bds-ohio-hrsa-provider-surface-v1.md)

All four layers preserve their source units and dates. BDS is a county-sector
employer aggregate; ACS is a county household/worker aggregate; PLACES is a
modeled county estimate using age-adjusted prevalence; HRSA is a current
administrative component file created 2026-09-14. None follows the same person
to a provider, appointment, bill, recovery, or political action.

## Decision

This lane has reached a useful measurement boundary. The next place-specific
pass should acquire or identify one provider/site and travel/use surface with a
defined population, or a dated closure-and-care-use record. If that route is
not available, rotate to the material/time or consumer/work lane rather than
adding another county median.
