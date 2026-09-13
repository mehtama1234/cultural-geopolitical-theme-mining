# Project: US local business and the changing hometown

## Question

When local businesses open, close, or move away, what changes for jobs, services, identity, and local political voice?

## Short end-to-end goal

Follow a business change from money, work, or market conditions to the services and relationships people lose or gain, then test the effect on place and local politics.

```text
credit, rent, labor, customer, or market change
  -> business opens, closes, grows, or moves
  -> jobs, services, prices, and meeting places change
  -> local identity, trust, and household choices change
  -> local government, lenders, and residents respond
```

This is a short discovery pass. Go deeper only if business records can be joined to a real change in local life.

## First working idea

The loss of a local business may be more than the loss of a job. It can remove a place where people meet, a source of local knowledge, and a way for residents to feel that they have a stake in the town. New businesses may replace some of that, but not always in the same place or for the same people. This is a working idea, not a conclusion.

## Scope

- US counties, towns, neighborhoods, small businesses, workers, customers, and owners;
- business openings, closures, moves, ownership, jobs, credit, rents, and customer access;
- differences by income, race, immigrant status, industry, rural or urban place, and region;
- local services, identity, trust, and political participation only where measured.

## Writing rule

Use plain words. Say which store, job, service, or meeting place changed, who noticed, and what they did. Do not call a place a “food desert” or “entrepreneurial ecosystem” without showing the exact measure.

## Matched evidence pass

The first matched check is [A business application is not yet a local job or a local place](../../findings/us-local-business-place-matched-evidence-001.md), with its [HTML reading page](../../../site/us-local-business-place-matched-evidence-001.html) and [claims ledger](claims-ledger-v1.md). It confirms a two-step entry gap while leaving local services, belonging, and political effects open.

The [local business formation and place layer](local-business-formation-place-layer-v1.md) adds the broader firm/place evidence: declining local entrepreneurship bias, staged entry from application to employer firm, and Census county data that separate applications from lasting firms. It does not infer services, belonging, jobs, or politics from application counts.

The [firm and market power distribution layer](firm-market-power-distribution-layer-v1.md)
extends this project across customers, workers, owners, places, public systems,
and future state capacity. It asks where a firm decision moves price, time,
data, risk, and control, and keeps cultural and political interpretation as a
separate later arrow.

The [BFS annual county data-quality boundary](bfs-annual-county-data-quality-boundary-v1.md)
records the 2026 release's differential-privacy noise and an exploratory
small-county outlier that must be validated before applications are interpreted
as durable firms, jobs, services, or local identity.

The [BFS–CBP county stage comparison](bfs-cbp-county-stage-comparison-v1.md)
matches applications to employer-establishment stocks in 3,142 counties. Its
median scale diagnostic is recorded for 2023–2025, but it is explicitly not a
formation, survival, or service rate because the two measures have different
units and reference periods.

The [CBP 2023 sector and local-service capacity layer](cbp-2023-sector-service-capacity-layer-v1.md)
adds a durable national baseline for manufacturing, retail, health/social
assistance, and accommodation/food employment and establishments. It keeps
sector presence separate from access, quality, ownership, belonging, and
political effects.

The [BDS realized entry, exit, and sector dynamics layer](bds-realized-entry-exit-sector-layer-v1.md)
adds the missing flow: actual establishment openings and closings, firm deaths,
job creation and destruction, and net job change. It turns the application and
stock comparison into a three-stage test while keeping services, culture, and
politics as separate outcomes.

The [BFS–BDS state stage comparison](bfs-bds-state-stage-comparison-v1.md)
tests that sequence geographically across 51 states and DC. Its normalized
application measure has a descriptive association with BDS entry, exit, and
job-flow rates, but it is not a conversion rate or causal result.

The [BFS–BDS sector bridge](bfs-bds-sector-bridge-v1.md) adds the national
industry dimension. It shows why application volume, realized openings,
turnover, and job growth must be read differently across retail, care, food,
transport, construction, and manufacturing.

The [BDS state-sector turnover profile](bds-state-sector-turnover-profile-v1.md)
adds geographic depth: selected sectors have different entry, exit, and net-job
patterns across states, so a national growth signal cannot be treated as one
uniform social experience.

The [CBP county essential-sector capacity layer](cbp-county-essential-capacity-population-layer-v1.md)
normalizes manufacturing, retail, care, and food establishments by county
population. It is a rough local-capacity baseline, not a measure of access,
quality, affordability, or service use.

The [rural/urban capacity profile](cbp-capacity-rural-urban-profile-v1.md)
stratifies that baseline with USDA's 2023 Rural-Urban Continuum Codes. It shows
that the rural/urban pattern differs by sector, so “place access” cannot be
represented by one metro/nonmetro score.

The [capacity and mobility cross-source bridge](capacity-mobility-cross-source-bridge-v1.md)
connects the county capacity layers to the existing NHTS vehicle and travel
evidence. It defines the next practical-access test without falsely joining
different samples or treating establishment presence as usable access.
