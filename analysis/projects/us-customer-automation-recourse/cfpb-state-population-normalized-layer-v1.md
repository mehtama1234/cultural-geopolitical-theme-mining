# CFPB complaint geography normalized layer v1

**Checked:** 2026-09-12  
**Complaint source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)  
**Population source:** [Census 2024 state population estimates](https://www2.census.gov/programs-surveys/popest/tables/2020-2024/state/totals/NST-EST2024-POP.xlsx)  
**Complaint window:** received 2024-01-01 through 2024-12-31  
**Population date:** July 1, 2024  
**Population file SHA256:** `4a98cd464d3f9e122e74b47b38f1584e78e9077f4b36be1cabf7a79ab5942852`

## What was calculated

For each of the 50 states and Washington, D.C.,

`published complaints / 2024 resident population × 100,000`.

The matched states contain 2,720,034 published complaints and 340,110,988
residents. The remaining records in the CFPB state aggregation are Puerto Rico,
territories, military addresses, or other non-state codes and are excluded from
the 50-state/D.C. comparison.

## Highest and lowest published-complaint counts per resident

| State or district | Published complaints | Population | Per 100,000 residents |
|---|---:|---:|---:|
| Georgia | 205,628 | 11,180,878 | 1,839.1 |
| Florida | 392,320 | 23,372,215 | 1,678.6 |
| District of Columbia | 9,858 | 702,250 | 1,403.8 |
| Delaware | 13,470 | 1,051,917 | 1,280.5 |
| Louisiana | 56,859 | 4,597,740 | 1,236.7 |
| Nevada | 38,912 | 3,267,467 | 1,190.9 |
| Texas | 360,091 | 31,290,831 | 1,150.8 |
| Maryland | 71,327 | 6,263,220 | 1,138.8 |
| New Jersey | 101,326 | 9,500,851 | 1,066.5 |
| Mississippi | 29,660 | 2,943,045 | 1,007.8 |
| Montana | 1,051 | 1,137,233 | 92.4 |
| Vermont | 647 | 648,493 | 99.8 |
| South Dakota | 945 | 924,669 | 102.2 |
| Maine | 1,746 | 1,405,012 | 124.3 |
| Idaho | 2,628 | 2,001,619 | 131.3 |
| Wyoming | 820 | 587,618 | 139.5 |
| Oregon | 7,180 | 4,272,371 | 168.1 |
| Iowa | 5,715 | 3,241,488 | 176.3 |
| West Virginia | 3,190 | 1,769,979 | 180.2 |
| Alaska | 1,362 | 740,133 | 184.0 |

## Interpretation

Normalizing by population changes the question from “where are there more
complaints?” to “where are more published complaints recorded per resident?”
The spread is large, but it is not a state ranking of consumer harm. It may
reflect product mix, complaint propensity, awareness and access to the CFPB,
company customer base, referrals, publication rules, ZIP/state reporting, and
the composition of residents versus financial-product users.

The place layer therefore supports a distributional and institutional question:
why do complaint-system records vary across places, and do the differences
survive adjustment for product, company exposure, market share, income,
language, age, digital access, and submission channel? It does not establish
that residents in a high-rate state experienced more unresolved harm.

## Next test

Estimate product-specific state rates, use product or account denominators
where available, and compare response categories within product and state.
Add CFPB submission channel and issue, then pair the result with a consumer
survey or local financial-access measure. Keep geography as a place-level
context; do not infer that the complaints are from the same households in SIPP
or respondents in ANES.

Related records: [CFPB complaint-response layer](cfpb-complaint-response-descriptive-layer-v1.md),
[service/platform recourse bridge](../../bridges/us-service-platform-recourse-trust-v1.md),
and the [broad theme coverage matrix](../../US-BROAD-THEME-COVERAGE-MATRIX_V1.md).
