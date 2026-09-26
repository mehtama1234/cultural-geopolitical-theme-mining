# Ohio place option-stack synthesis v1

**Checked:** 2026-09-19
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

The new [Ohio HPSA coordinate-availability audit](hrsa-ohio-coordinate-availability-audit-v1.md)
sharpens the next step. Of 1,342 retained Ohio primary-care HPSA rows, only 94
(7.0%) have both latitude and longitude; all population and geographic rows in
the filtered file lack coordinates. A county FIPS code therefore cannot be
converted into resident travel time. The coordinate-bearing facility rows can
support a small identity/hours/travel check, but accepting patients, insurance,
wait, completed use, and household consequences remain open.

The follow-up [HPSA-to-health-center crosswalk probe](hrsa-ohio-hpsa-site-crosswalk-probe-v1.md)
shows that the candidate route is technically feasible: 56 of 94 coordinate-
bearing HPSA rows have a nearest HRSA site within 100 meters and 87 within 10
kilometers. These are proximity matches, not confirmed organization or service
matches. The result advances site identification while leaving hours, insurance,
wait, actual use, and household consequences open.

The stronger [identifier crosswalk](hrsa-ohio-hpsa-site-identifier-crosswalk-v1.md)
finds a shared BHCMIS organization identifier for 61 of the 94 coordinate-
bearing HPSA rows. Among those same-organization candidates, 56 are within 100
meters and 60 within 10 kilometers. This is an administrative organization
link, not proof of designated service identity, appointment availability,
completed use, or resident recovery.

The [operating-fields audit](hrsa-ohio-hpsa-site-operating-fields-audit-v1.md)
adds a practical but limited stage: 641 of 662 site records under the shared
organizations list positive weekly hours, but only 152 have a known full- or
part-time schedule and 525 have an unknown operating calendar. Nominal hours
are therefore visible before patient acceptance, wait, appointment, and actual
use.

## Counterexample retained

The new [HPWO named-site access checkpoint](hrsa-hpwo-allen-county-named-site-access-v1.md)
follows one shared-organization-ID case into a named active site: North Lima
Community Health Center is listed under Health Partners of Western Ohio with 72
hours per week. HPWO's official patient-facing page also reports a new-patient
route, limited same-day appointments, insurance coverage, and sliding-fee or
payment-plan options. These are organization-level route signals, not proof of
a site-specific appointment, wait, completed care, or recovery.

The site's own patient-facing page confirms a phone and service categories but
shows multiple overlapping hour lines without clearly labeling the service or
appointment type. This is itself an access-quality boundary: a public schedule
can exist without yielding one unambiguous medical appointment schedule.
HPWO's general contact page also says its email form does not schedule
appointments and directs patients to call or use the portal; the HRSA and
current HPWO pages list different phone numbers. The route therefore ends at a
phone/portal handoff with unresolved information friction.
The linked patient portal is login-gated and exposes no public slots or wait
times, so portal existence should not be counted as public appointment access.

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
- [Ohio HPSA coordinate-availability audit](hrsa-ohio-coordinate-availability-audit-v1.md)
- [Ohio HPSA-to-health-center crosswalk probe](hrsa-ohio-hpsa-site-crosswalk-probe-v1.md)
- [Ohio HPSA-to-site identifier crosswalk](hrsa-ohio-hpsa-site-identifier-crosswalk-v1.md)
- [Ohio HPSA-linked site operating-fields audit](hrsa-ohio-hpsa-site-operating-fields-audit-v1.md)

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
