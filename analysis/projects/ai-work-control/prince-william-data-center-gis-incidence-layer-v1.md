# Prince William County data-center GIS incidence layer v1

**Checked:** 2026-09-13  
**Source unit:** public county GIS feature exports for data-center buildings and campus projects  
**Geography:** Prince William County, Virginia  
**Status:** bounded local pipeline/incidence screen; not an electricity, water, bill, or jobs estimate

## Why this layer matters

The national data-center energy estimate establishes scale, but it does not say
where the physical pipeline is concentrated or how much of a planned footprint
has become an actual building. This county GIS layer supplies a local planning
and development view:

```text
campus/project pipeline
  -> building permits and construction status
  -> physical footprint and planning geography
  -> utility, land, traffic, tax, and public-participation questions
  -> actual load, household incidence, local benefit, and state control
```

The first two arrows are visible in the export. The later arrows still require
utility, tax, employment, environmental, and public-record linkage.

## Source and field boundaries

The building-layer metadata describes a county-developed layer intended to track
data-center buildings from inception through occupancy and operational status,
using Tyler LMS/Energov and other county software. The campus-layer metadata
describes non-residentially zoned projects whose final development has not yet
occurred. County planning, development-services, economic-development,
information-technology/geospatial, and real-estate-assessment offices are
listed as the contributing authorities in the layer metadata.

The local exports contain no direct megawatt load, electricity use, water use,
rate allocation, assessed tax amount, employment count, traffic count, or
household survey. `GFA` and `PlannedGFA` are gross-floor-area fields, not
computing capacity. Project status is not proof of approval, construction
completion, operation, or customer load.

The most recent `LastEditDate` values in the campus export correspond to
2026-08-24 UTC; this is a dataset-edit timestamp, not a claim that every
project changed on that date. The analysis is a snapshot, not a time series.

## Building inventory

The building export contains 246 records:

| Building status | Records | Gross floor area | Share of recorded GFA |
|---|---:|---:|---:|
| Completed | 57 | 13,219,176 sq ft | 15.3% |
| Under Construction | 30 | 8,859,558 sq ft | 10.3% |
| Pending | 68 | 33,605,695 sq ft | 38.9% |
| Planned | 91 | 30,613,135 sq ft | 35.5% |
| **Total** | **246** | **86,297,564 sq ft** | **100.0%** |

The completed and under-construction categories together account for about
25.6% of recorded GFA, while pending and planned categories account for about
74.4%. This is a pipeline composition, not a forecast of what will be built:
status definitions, duplicate or phased records, and zero or estimated GFA
fields require a parcel/case audit before interpreting the shares as build-out
probabilities.

## Campus pipeline and geography

The campus export contains 75 records. Its 98,456,207 sq ft of planned GFA is
distributed across four planning districts:

| Planning district | Campus records | Planned GFA | Remaining GFA |
|---|---:|---:|---:|
| Brentsville | 45 | 42,461,554 sq ft | 34,791,552 sq ft |
| Gainesville | 19 | 41,526,421 sq ft | 33,789,983 sq ft |
| Coles | 9 | 12,957,350 sq ft | 8,770,200 sq ft |
| Potomac | 2 | 1,510,882 sq ft | 1,510,882 sq ft |
| **Total** | **75** | **98,456,207 sq ft** | **78,862,617 sq ft** |

Campus status is 9 completed, 15 pending, and 51 planned. The remaining-GFA
field is a project-planning field; it should not be summed with building GFA or
converted into future electricity demand. The geographic result is a targeting
screen: Brentsville and Gainesville contain most of the recorded campus
pipeline, so utility connections, zoning records, traffic, tax, and public
comments should be linked there first.

## What this adds to the broader program

1. **Infrastructure is locally concentrated.** A national demand scenario
   becomes a small number of planning geographies and project pipelines.
2. **Promised capacity and realized capacity are different stages.** The
   building status distribution shows why planned square footage cannot be
   treated as operating load.
3. **The public decision is multi-agency.** The layer itself combines planning,
   permitting, development, assessment, and geospatial records; rate cases and
   utility data are needed to see who carries the next cost.
4. **The local counterexample is possible.** A large planned footprint may have
   low realized load, delayed construction, public cost protections, local
   employment, or a replaceable provider. Those outcomes must be measured rather
   than inferred from the map.

## Arrow ledger

| Arrow | Status | What is safe to say | Missing evidence |
|---|---|---|---|
| Planned campus → building pipeline | Compared within snapshot | Campus and building records contain distinct status stages and footprints | Case-level deduplication and time series |
| Building footprint → electricity/water load | Open | Physical footprint identifies a place for utility linkage | Meter/load, water, substation, and service records |
| Project → household or ratepayer incidence | Open | Concentrated projects identify where incidence should be tested | Tariffs, bills, cost allocation, taxes, traffic, and environmental records |
| Project → local capability/jobs | Open | County records identify development activity | Employment, wages, vendors, training, tax receipts, and local procurement |
| Public record → political meaning/action | Open | The geography defines a public-participation sampling frame | Hearing comments, attribution, trust, organizing, and policy response |

## Next matched-place test

Pair this county snapshot with one comparison county that has a substantial
data-center pipeline but a different rate-design or utility-cost regime. For
each place, collect:

- project and building status by dated case;
- approved and actual load, substation and transmission work;
- tariff, collateral, minimum-billing, and cost-allocation terms;
- assessed value, tax receipts, jobs, wages, vendors, and training;
- water, traffic, land-use, and environmental records;
- hearing comments, public attribution, and later regulatory response; and
- provider/customer exit or replacement evidence.

That comparison would connect physical infrastructure to household incidence,
local benefit, public legitimacy, and state leverage. Until then, this layer is
a local pipeline and targeting result—not proof that data centers caused a
particular bill, political response, or geopolitical advantage.
