# CBP 2023 sector and local-service capacity layer

**Checked:** 2026-09-12  
**Source:** [Census County Business Patterns](https://www.census.gov/data/developers/data-sets/cbp-zbp/cbp-api.html)  
**File:** `cbp23us.zip`, national 2023 file; SHA-256 `3f9018f807f1ffd7bcbb00690f9792573bc2bc6bb4cfab9df14ca7ab3eac0862`  
**Status:** durable employer-establishment baseline; not a measure of service quality, ownership, or access.

## Why sector structure matters

“More businesses” is too vague for the broad program. Retail, health care,
food service, and manufacturing play different roles in everyday life,
employment, consumption, resilience, and local identity. CBP supplies a
durable employer-establishment and employment baseline against which early BFS
application signals can be checked.

```text
sector and establishment structure
  -> jobs, payroll, goods, care, food, production, and meeting places
  -> household access, prices, time, health, belonging, and resilience
  -> worker, consumer, resident, firm, and public response
```

## National 2023 baseline

The all-industry row and selected two-digit sectors report:

| Sector | Employer establishments | Employment |
|---|---:|---:|
| All industries | 8,361,342 | 139,831,742 |
| Manufacturing (31–33) | 284,452 | 12,335,234 |
| Retail trade (44–45) | 1,043,373 | 16,046,207 |
| Health care and social assistance (62) | 1,003,398 | 22,063,238 |
| Accommodation and food services (72) | 784,882 | 14,608,170 |

The selected sectors are not interchangeable. Health care and social
assistance is a care and employment system; retail is a consumer-access and
distribution system; accommodation and food services combine consumption,
service work, and social space; manufacturing is a productive-capacity and
supply-chain system.

## What this adds to the firm/place map

- **Consumer life:** retail and food establishments are possible access points,
  but establishment presence does not show prices, hours, quality, distance,
  affordability, or whether a household can use them.
- **Care and health:** health/social-assistance employment makes care capacity
  visible as a sector, but not the amount, quality, cost, or unpaid family work
  avoided or required.
- **Work and bargaining:** employment counts provide scale, not pay, schedule,
  control, worker voice, or job security.
- **Local identity:** a sector's establishments may be meeting places or local
  institutions, but CBP does not measure belonging, trust, or cultural meaning.
- **State and geopolitical capacity:** manufacturing employment is a baseline
  for productive capacity, not proof of domestic resilience, ownership,
  supply-chain independence, or strategic leverage.

## Relation to BFS applications

BFS applications are an early flow and CBP establishments are an employer stock.
The earlier [BFS–CBP county stage comparison](bfs-cbp-county-stage-comparison-v1.md)
matches them by county, but it does not establish which applications become
employers or services. The sector baseline gives the next comparison a sharper
target: do applications in a place correspond to durable retail, care, food,
or production capacity, or do they remain unformed or shift into another
sector?

## Next executable comparison

For matched counties or commuting areas, align BFS applications with CBP
sector establishments and employment, then add population, distance/access,
business survival, payroll, ownership, vacancies, prices, and local political
or belonging measures. Use broad sectors before narrow industries, document
suppression and disclosure rules, and include places where applications rise
without durable service or employment growth.

## Limits

CBP covers employer establishments and employment in the reference period. It
does not cover nonemployer firms as employer establishments, reveal individual
employer operations, measure service quality or consumer use, or identify
local ownership and political effects. The national table is a baseline, not a
county-level causal result.
