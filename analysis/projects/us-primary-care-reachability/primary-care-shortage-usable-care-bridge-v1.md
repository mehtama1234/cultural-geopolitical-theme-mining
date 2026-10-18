# Primary-care shortage to usable-care bridge

Status: forty-ninth active depth artifact; checked 2026-10-18.

## What we found

A county can contain health-sector establishments and still have a formal
primary-care shortage designation. Current HRSA data contain 20,905 designated
primary-care rows; row-level metadata show median FTE of 5.18 among rows with
an FTE value, but the formal ratio field is unavailable in the retained file.
These are designation and staffing metadata, not active appointments or care
use.

The Ohio identifier crosswalk advances the route: 61 coordinate-bearing HPSA
rows share an HRSA organization identifier with an official service-site file,
covering 662 site rows. All 662 are marked active and 641 list positive hours,
with a median of 40 hours per week. Yet only 36 of the 61 organizations have a
site with a known full- or part-time schedule; 510 site rows have unknown
schedule status. No appointment, insurance acceptance, wait, completed visit,
or continuity outcome is observed.

The safe chain is:

`shortage designation -> organization/site identity -> listed hours -> [open]
service and insurance acceptance -> appointment -> completed care -> continuity
and household outcome`

## Evidence ledger

| Evidence | Signal | Boundary |
|---|---|---|
| HRSA primary-care designation file | 20,905 designated rows; median designation population 42,551 and median estimated underserved population 23,715 where reported; median score 16 | Rows overlap and are not unique people, sites, or appointments; missing fields are not zero |
| HPSA type comparison | Geographic rows have median 7.0 FTE where available; population rows 5.18; facility/site rows only 543 of 4,866 have FTE, with median 0.375 among that sparse subset | Category and missingness differences make pooled staffing or adequacy claims invalid |
| HRSA/PLACES county comparison | Among counties with population HPSA type, modeled medians include 9.0% transportation insecurity, 16.6% food insecurity, 13.1% housing insecurity, and 18.4% frequent mental distress | County modeled outcomes do not identify designated residents, provider reach, or shortage causation |
| CBP-HPSA bridge | Of 3,072 counties with usable CBP health-sector rows, 2,785 had a designated HPSA component; median establishments per 10,000 residents were similar in represented and nonrepresented counties (23.12 vs 23.44) | Establishment presence is not provider adequacy; HRSA and CBP vintages and components differ |
| Ohio identifier crosswalk | 61 HPSA rows share an organization identifier with service-site data; 56 nearest same-organization sites are within 100 meters, 59 within 5 km, and median distance is 0 km | Same organization does not prove designated service identity, open appointments, acceptance, or use |
| Ohio operating fields | 662 linked site rows are active; 641 list positive hours, median 40 hours/week; only 36 organizations have known full/part-time schedule and 510 rows have unknown schedule | Listed hours are not patient capacity, appointment availability, or continuity |
| California Medi-Cal expansion | In a qualitative sample of nearly 100 undocumented adults, 70% enrolled and 88% of enrolled participants had accessed care at least once after eligibility expansion | Focus-group sample is not statewide or longitudinal; initial access is not continuity or health improvement |
| Procedural continuity comparator | California reported 704,838 procedural disenrollments in a six-month period and 8,481 completed follow-up survey responses | Survey response is selective and does not identify appointment, care, or health effects for all disenrolled people |

## What this connects to

- **Public systems:** a formal shortage designation can trigger resources while
  leaving the patient-facing route unknown.
- **Place and mobility:** distance, transport, schedule, and rurality condition
  whether a nominal site is usable.
- **Health and household room:** waiting, travel, unpaid care, coverage, and
  repeated contact can shift work, money, and family time.
- **Administrative legibility:** renewal, identity, language, and insurance
  rules can interrupt continuity after initial eligibility.
- **Trust and meaning:** a person may interpret a listed site and failed booking
  differently from a completed, respectful, continuous care route.
- **Unequal exposure:** low-income, migrant, seasonal, disabled, and uninsured
  populations may face different routes even inside one county label.

## Deeper question

**When does a formal primary-care shortage designation become a usable care
route rather than a named site with hours that a patient still cannot book or
complete?**

This question has high decision value for health-resource allocation, high
missing-link value because appointment and completed-care stages are absent,
high connection value across place, household, work, care, and public-system
themes, and high disconfirmation value because a site-level booking panel could
show that nominal capacity is already translating into care. Effort is bounded
to one HPSA component/site and a defined patient population; scope risk is
controlled by separating county models, site metadata, and patient experience.

## What we know so far

The evidence supports a capacity–reachability distinction. HPSA data identify
shortage objects and some staffing fields. The Ohio join identifies plausible
service sites and hours. Neither layer shows whether a patient can obtain the
relevant service, pay for it, wait an acceptable time, complete it, or return
for follow-up.

The California expansion is a useful counterexample: removing a formal
eligibility barrier was followed by reported initial care access for many focus-
group participants. It also shows why access is not continuity: later renewal,
premium, provider, language, and administrative conditions can change the route.

## Bounded public discussion

| Discussion | Signal | Limit |
|---|---|---|
| Reddit waiting-list discussion | People report both faster first appointments and long diagnostic or treatment waits, separating first contact from continuity | UK anecdotal forum; no verified timelines or U.S. population estimate |
| Reddit fragmented-records discussion | Patients describe repeating measurements when providers cannot share information, highlighting patient time and safety work | Self-selected forum; operational and clinical claims are not independently verified |
| LinkedIn No Surprises discussion | Patient protection at the point of care is separated from downstream provider, plan, arbitration, and premium effects | Professional interpretation; not a causal evaluation of access or affordability |

These discussions add lived language about waiting, repeated information work,
and the difference between formal protection and usable care. They do not
measure U.S. appointment success.

## What could change the answer

- A site-level panel could show that active hours and shared identifiers predict
  rapid booking and completed follow-up.
- A site may have open hours but no new-patient capacity, accepted coverage, or
  appropriate service; nominal operation can coexist with practical exclusion.
- A patient may complete one visit and still lose continuity through renewal,
  provider turnover, cost, transport, or incompatible records.
- Initial access can improve after eligibility expansion while later continuity
  worsens after a renewal or premium condition.
- County shortage indicators may be useful for allocation without being useful
  as individual access measures.

## Challenge checks

- HPSA status and listed hours were not treated as appointment or completed-care
  outcomes.
- County correlations and PLACES medians were not treated as causal resident
  effects.
- HPSA rows, sites, organizations, counties, and patients were kept as
  different units.
- Missing schedule fields were not treated as zero capacity.
- The California focus-group result was not generalized to all eligible adults.
- The waiting and records discussions were not treated as representative U.S.
  evidence.
- Patients, caregivers, providers, insurers, administrators, and communities
  were kept as different affected groups.

## Current answer

Partly answered. The atlas can link shortage objects to plausible active sites
and listed hours, but it cannot yet show that a defined patient received timely,
affordable, completed, continuous primary care or what household and trust
effects followed.

## Stopping rule

Do not call a shortage designation effective, ineffective, accessible, or
trust-building from provider counts, FTE fields, site hours, county health
medians, eligibility, or a first visit alone. Stop this pass after one site and
patient population link appointment attempt, wait, acceptance, completed care,
follow-up, and a later health/work/household outcome—or after the source owner
confirms which fields are unavailable.

## Source links

- [HRSA HPSA component and place comparison](../../records/us-hrsa-hpsa-component-places-2025.json)
- [HRSA operational fields](../../records/us-hrsa-hpsa-operational-fields-2026.json)
- [CBP and HRSA primary-care bridge](../us-local-business-place/cbp-hrsa-primary-care-shortage-bridge-v1.md)
- [Ohio HPSA-to-site identifier crosswalk](../us-local-business-place/hrsa-ohio-hpsa-site-identifier-crosswalk-v1.md)
- [Ohio site operating-fields audit](../us-local-business-place/hrsa-ohio-hpsa-site-operating-fields-audit-v1.md)
- [California care access and continuity](../../records/us-california-medical-expansion-access-continuity-2025.json)
- [Reddit waiting and continuity discussion](../../social-discussions/records/atlas-bsa43-nhs-waiting-reddit-002.json)
- [Reddit fragmented-records discussion](../../social-discussions/records/atlas-bsa43-nhs-waiting-reddit-003.json)
- [LinkedIn No Surprises discussion](../../social-discussions/records/atlas-batch-0057-no-surprises-linkedin-001.json)
