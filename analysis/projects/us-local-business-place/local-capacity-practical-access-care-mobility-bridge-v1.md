# Local capacity, practical access, care adequacy, and mobility bridge v1

**Checked:** 2026-09-12  
**Scope:** US counties and resident access to everyday production, retail, food, and primary care  
**Status:** compared place layers; not a resident-level access or health-outcome estimate

## The broader societal question

Does having establishments in a place mean residents can actually reach,
afford, use, and rely on the service? The answer matters for consumer life,
work, care, family time, local identity, firm exposure, and political demand.

```text
local productive/service capacity
  + vehicle, transit, travel, and neighboring-place options
  + provider adequacy, price, hours, insurance, and staffing
  -> practical access or forced substitution
  -> time, work, care, food, health, and local attachment consequences
  -> business demand, public-system pressure, trust, and political response
```

The current evidence measures pieces of this stack at different levels. It does
not justify calling an establishment count “access.”

## Evidence layers

| Layer | Unit/time | What it adds | Boundary |
|---|---|---|---|
| [CBP essential-sector capacity](cbp-county-essential-capacity-population-layer-v1.md) | County employer stock; 2023 | Establishments and employment per 10,000 residents in manufacturing, retail, health/social assistance, and food | No distance, hours, price, quality, staffing, public/private status, or use |
| [RUCC metro/nonmetro profile](cbp-capacity-rural-urban-profile-v1.md) | County; 2023 | Sector-specific differences across 1,185 metro and 1,943 nonmetro matched counties | Metro/nonmetro is not a travel-time or service-quality measure |
| [NHTS mobility comparison](../us-household-calendar-integration/nhts-transport-comparison-v1.md) | Person/household/trip; 2022 | Vehicle access, rideshare, and work-trip modes in urban/rural categories | Different sample and geography from CBP/RUCC; no destination or service outcome |
| [HRSA primary-care HPSA bridge](cbp-hrsa-primary-care-shortage-bridge-v1.md) | HPSA component and county identifier; current designation over 2023 CBP | Formal shortage components can overlap counties with visible health establishments | Components may be partial, population-based, facility-based, or current-vintage; not county-wide adequacy |
| [Time and care layers](../us-household-calendar-integration/time-work-care-social-participation-layer-v1.md) | Person diary/respondent; 2024/2025 | Work, care, travel, and social-time consequences are measurable elsewhere | Not linked to a specific county capacity or service episode |

## What the comparison supports

### 1. Capacity is sector-specific

The 2023 population-weighted profile shows nonmetro counties with more retail
and manufacturing establishments per resident, metro counties with more health
and social-assistance establishments, and nearly equal food-service capacity.
That does not mean nonmetro residents have easier access to retail or metro
residents receive adequate care. The sector pattern is a reason to avoid one
composite “rural disadvantage” or “service access” score.

### 2. Presence is not adequacy

Among the 3,072 counties with usable CBP health rows and population estimates,
2,785 contained a county identifier represented in a current primary-care HPSA
component. Their median CBP health-establishment density was similar to the
287 counties without such a represented component. This demonstrates a
measurement boundary: visible establishments and formal shortage designations
answer different questions. It does not estimate the share of residents who
lack a provider.

The accompanying employment-scale check also finds nearly identical median
health-sector employees per establishment in the two HPSA-presence groups, so
visible staffing footprint at this level does not settle adequacy either.

### 3. Mobility mediates the option set

The NHTS comparison reports zero-vehicle households at 9.73% in urban areas
and 2.82% in rural areas, while pickup work-trip shares were 12.09% and 22.92%
respectively. Those patterns cannot be directly assigned to CBP counties, but
they show why local supply must be analyzed with the ability to reach an
alternative. A county can have capacity on paper while a resident lacks a
vehicle, affordable fare, time, or a route that reaches the relevant provider.

### 4. Scarcity can redistribute time and family labor

If care, food, repair, or work alternatives require a longer trip or repeated
attempts, the cost may appear as unpaid caregiving, missed work, delayed care,
or reduced social participation rather than as a local business statistic. The
time and care layers provide the downstream measurement vocabulary; the
place-level linkage remains open.

### 5. Place patterns can become cultural and political patterns

Residents may interpret repeated closures, long travel, absent providers, or
unreliable service as personal inconvenience, market change, government failure,
corporate extraction, rural neglect, urban exclusion, or community decline.
Those meanings are not contained in CBP, NHTS, or HPSA records. They require
direct measures of attribution, local identity, trust, organizing, and voting.

## Arrow ledger

| Arrow | Status | Current evidence | Missing evidence |
|---|---|---|---|
| Local establishments → nominal sector capacity | Observed / Compared | CBP stocks and employment normalized by population | Durable hours, staffing, ownership, quality, and neighboring-place supply |
| Nominal capacity → reachable alternative | Open | NHTS vehicle and mode distributions; RUCC comparison | Common geography, destination-level travel time, fare/fuel, and route reliability |
| Health establishments → primary-care adequacy | Compared | CBP–HRSA overlap diagnostic | Provider counts, panel acceptance, appointment wait, HPSA component population, and quality |
| Reachable supply → use, delay, or substitution | Open | Time/care and food layers provide separate outcomes | Same place/person records with service attempt, price, travel, use, and unmet need |
| Access constraint → work, family, or social time | Open | ATUS and care/work evidence | Dated service event plus diary/panel follow-up |
| Place condition → local trust or political demand | Open | Political and cultural layers at population level | Matched places with exposure, local narrative, attribution, and action |

## Matched-place test

Use one common geography and period, preferably county or tract where the
service and mobility records permit. Construct four comparison cells:

1. low nominal capacity / high mobility options;
2. low nominal capacity / low mobility options;
3. high nominal capacity / low mobility options;
4. high nominal capacity / high mobility options.

Within each cell, measure sector-specific prices, hours, staffing, ownership,
travel time, insurance or eligibility, appointment availability, service use,
unmet need, work/care displacement, and local political response. For care,
use HRSA component boundaries and population types rather than assigning every
resident of a county the same shortage status. Include a counterexample where
low nominal capacity is offset by neighboring access or strong public
provision.

## What this changes in the broad program

The societal trend is not simply that some places have more or fewer
businesses. It is that local life is organized by an option stack: nominal
capacity, mobility, institutional eligibility, price, time, quality, and
replaceability. Different combinations can produce different consumer,
worker, caregiver, cultural, and political experiences even when establishment
counts look similar. The next end-to-end claim requires the common-geography
matched design above.
