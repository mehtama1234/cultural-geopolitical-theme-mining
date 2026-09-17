# GAO 2026 airport transit availability and adoption layer v1

**Checked:** 2026-09-17
**Source:** US Government Accountability Office, GAO-26-107817
**Reference window:** 2019–2023 Census commute data; airport information reviewed in 2025–2026; report published January 28, 2026
**Status:** transportation availability, adoption, and demand-management finding; not a national causal estimate of transit behavior

## Why this update matters

Transportation is often represented as infrastructure supply: does an airport
have a bus or rail connection? GAO's airport review shows why that is
insufficient for a consumer and societal trend atlas. A route can exist while
travel time, accessibility, unfamiliarity, fare, parking, shift timing, or
transfer friction keeps passengers and workers in cars, taxis, or rideshares.

This is a clean example of the atlas's broader conversion thesis. Public
infrastructure becomes a practical option only when it fits a person's time,
cost, safety, mobility, knowledge, and schedule constraints. The same gap also
matters for congestion, emissions, airport labor access, household transport
costs, and local investment decisions.

## Recorded findings

| Surface | Result | Boundary |
|---|---|---|
| Review frame | GAO reviewed all 31 large-hub airports and a random selection of 20 medium- and small-hub airports, 51 total | The 51-airport review is designed coverage, not a complete census of every US commercial airport or every trip |
| Basic availability | All but two small airports reviewed had some bus or rail transit service | “Some level” of service does not establish frequency, span, fare, reliability, directness, or accessibility |
| Large-airport rail | 23 of 31 large airports had rail service; 18 connected on airport grounds or by dedicated air-train, while five used a free bus connection from off-site rail | Presence and connection type do not establish convenient service for every passenger, worker, or shift |
| Medium/small service | The 20 selected medium and small airports generally had bus service between the airport curb and local downtown | Downtown access may not match residential, industrial, overnight, or dispersed employment trips |
| Passenger use | Among 12 airports with passenger mode reports, public-transit use ranged from **4% to 19%** | Only 12 airports had usable passenger mode reports, and the range is not a national average or causal comparison |
| Airport employees | At two large airports visited, 17% and 19% of surveyed employees used public transit; GAO estimated about **4%** of airport and airline employees nationwide used public transit to commute | The two airport surveys and the national Census estimate have different designs and universes |
| Decision factors | Cost, travel time, and familiarity influenced decisions; disability-related elevator and mobility-aid accommodation mattered for some riders | These are reported factors, not a ranked causal decomposition of ridership |
| Worker constraints | Parking, transit benefits, and modes matching work shifts mattered for employees, whose shifts may begin early | A route may be useful for passengers but unusable for workers with overnight or early shifts |
| Demand management | Five visited airports were implementing transportation-demand-management strategies such as signage, advertising, or reduced-cost transit | A strategy is an intervention, not proof of increased ridership or reduced congestion |
| Measurement | Two visited airports set or planned to assess transit-use goals; GAO found many efforts lacked clear outcome evidence | Promotion, stated goals, observed use, congestion, emissions, and worker access remain separate outcomes |

## The central mechanism

```text
airport trip or airport job
  -> available bus/rail connection
  -> time, fare, reliability, accessibility, familiarity, parking, and shift fit
  -> transit choice, car/taxi/rideshare choice, or trip/job constraint
  -> congestion, emissions, household cost, labor access, and airport operations
  -> signage, fare incentive, service redesign, or infrastructure investment
```

The first arrow is a supply measure; the second is the practical-choice
interface. If a rail station is off-site, a free connector can be decisive. If
the connection is infrequent, a worker beginning a shift before dawn may need a
car regardless of the route's nominal presence. If an elevator is unreliable,
the same system has a different value for a passenger using a mobility aid.

This creates several distinct meanings of “transit access”: geographic
availability, temporal availability, physical usability, price affordability,
information discoverability, and dependable trip completion. A single airport
binary cannot represent them. The low national employee share may reflect
service design, parking supply, wages, shift timing, residential geography,
worker preference, or some combination; GAO does not identify the weights.

Demand-management interventions also have distributional consequences. Free
transit or better signs may help riders who already have a workable route,
while workers in late or early shifts still face private-vehicle dependence.
Reduced fares can lower trip cost without improving reliability or travel time.
Airport, transit-agency, employer, passenger, and worker decisions are linked
but not interchangeable.

## What this changes in the broader trend map

This layer adds transportation usability to the atlas's infrastructure,
consumer choice, labor, and place lanes. It shows how large physical systems
can be “available” while practical uptake remains low. It also connects airport
operations to ordinary household and worker constraints: commuting time, shift
coverage, parking cost, disability access, and public subsidy.

The finding is complementary to the household transportation questions in
HTOPS, but it should not be merged with them. HTOPS can measure household-
reported sufficiency and unmet reasons; the GAO airport review measures
airport-specific service and observed or reported mode use. Together they
suggest a useful comparison between perceived household transport sufficiency,
place-level service design, and actual completed trips.

## What remains unproven

GAO does not estimate the causal effect of rail, bus, signage, fare incentives,
parking prices, or transit benefits on passenger or employee mode choice. It
does not show how many trips were missed, how much households paid, or whether
transit access changed airport labor supply, wages, congestion, emissions, or
local political support.

The 4% national employee estimate and the 17–19% figures from two visited
airports are not directly comparable. Passenger use is available for only 12
airports and may use different reporting methods. Availability, use, trip
completion, and rider well-being are separate claims; high use can also reflect
lack of alternatives rather than a high-quality service.

## Next test

Build a route-day-shift ledger for selected airports linking:

- origin geography, passenger or employee status, disability/access need, and
  trip purpose;
- route, transfer, span, headway, fare, parking price, elevator status, and
  real-time reliability;
- shift start/end, transit benefit, travel time, safety, familiarity, and
  accessibility;
- planned, attempted, completed, delayed, and abandoned trips;
- household transport cost, missed work, airport staffing, congestion, and
  emissions; and
- intervention date, ridership change, distributional incidence, and public
  response.

Compare airports with similar passenger and worker profiles but different
service connections and demand-management changes. The strong result is not a
route on a map or a promotional campaign; it is a dependable, affordable,
accessible trip that expands practical mobility for passengers and workers.

## Provenance and storage

No GAO report PDF, Census commute microdata, transit schedule archive, or
airport administrative file was downloaded. This memo retains the official
GAO HTML page, reported figures, methods, and limitations.

**Official review:** <https://www.gao.gov/products/gao-26-107817>
