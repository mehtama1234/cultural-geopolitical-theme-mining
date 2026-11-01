# External data sources in the observatory

This is the plain-language map of the external evidence layer. It answers
“what sources are we using?” without turning a source inventory into a trend
claim. Every source still needs its own publisher, period, unit, denominator,
lineage, independence, and rights review before promotion.

## The eight source families

| Family | What it contributes | Concrete pinned inputs in this release | Current boundary |
| --- | --- | --- | --- |
| Cultural-geopolitical theme mining | Cultural, social, institutional, place, consumer, and geopolitical observations | The local `analysis/records/` corpus and 14-theme observation manifest | Source-backed research records; not automatically representative or causal |
| Social research | Public discussion, creator, and platform signals | Integrated Trend Atlas, collection manifest, publication evidence appendix | Signal layer only; not prevalence, market size, or buying intent |
| Trend hunting | Public-signal synthesis, themes, counter-signals, and remedy/implementation comparisons | Deep-trends evidence graph, signal-to-outcome funnel, remedy and implementation registers | Candidate synthesis; underlying observations must be checked |
| Annual-report research / trends observatory | Public-company filings, strategy, financial claims, operating constraints, and burden transfer | Integrated theme map, public citation list, and citation map | Company-reported claims; independent outcomes remain separate |
| Inc. 5000 analysis | Private-company growth, business models, and bottom-up commercial signals | Rebuild manifest, opportunity intelligence release, independent-source index, strategic source ledger | Ranking and company signals do not prove demand or outcomes |
| IBIS industries | Industry definitions, forces, capacity, dependencies, and bottlenecks | Research manifest, cross-industry findings/patterns, source inventory, claim sample and force map | Analytic synthesis; claim-level source and outcome review is still open |
| Research signals | Capture, provenance, normalization, deduplication, and verification infrastructure | Pinned repository revision and source-custody records | Governance/infrastructure, not evidence of a trend by itself |
| Organization intelligence system | Shared identity, evidence, comparability, review, rights, and release contracts | Pinned repository revision and nested annual-report family snapshot | Governance/integration layer, not an independent evidence family |

## Named external datasets currently used for tests

These are the concrete source records already used in the release artifacts:

- USDA Economic Research Service food-security household series.
- Urban Institute Well-Being and Basic Needs Survey food-insecurity series.
- Urban Institute December 2025 WBNS food-insecurity release, including the
  working-age and income-band monitoring rows.
- Federal Reserve SHED financial-room and emergency-expense series.
- JPMorganChase Institute household-liquidity chart evidence.
- ACS and NHTS mobility-access measures.
- Census County Business Patterns and Nonemployer Statistics repair proxies.
- CDC/NCHS NPALS public tables and Open Repair Alliance mobile-repair records.
- ABS, HILDA/AIHW, ANUPoll, Roy Morgan, and related financial-pressure and
  time/care measures.
- CDC capacity observations and CMS Medicaid-rate evidence in the bounded IBIS
  adult-day-care review.
- U.S. Navy FY2026 maintenance-budget context and USAspending Bath Iron Works
  transaction records used for a held dry-dock/defense execution comparison.
- BLS labor-capacity comparison measures used as a counter-signal.
- GSMA consumer-scam resolution/recovery evidence and British Social Attitudes
  waiting/legitimacy evidence used for a mechanism challenge.
- Public infrastructure and geopolitical records in the PJM, undersea-cable,
  OECD, World Bank, IRENA, and regional development observations.

The named records are not one pooled dataset. They have different populations,
geographies, periods, methods, units, and publishers. The observatory keeps
those differences visible and only compares them when the comparison contract
allows it.

The Navy/USAspending lane is especially constrained: budget requests and
transaction obligations are different constructs, and both may describe the
same Department of Defense program. They are therefore publisher-distinct but
not yet independent confirmation.

## How a source reaches the frontend

```text
source artifact
  -> pinned snapshot and checksum
  -> normalized observation with unit/period/denominator
  -> lineage and rights review
  -> independent comparison and counter-signal
  -> qualification/backtest gate
  -> decision-ready chart or narrative
```

The board reads release-manifest artifacts; it does not scrape upstream pages.
No company identifier or internal dataset is connected by this source guide.
The internal bridge remains blocked until an external trend qualifies and a
separate company decision, rights, privacy, and exposure contract is approved.

## Current status

The source inventory is operational and refreshable. One food-security pattern
is currently qualified for external monitoring. The other candidates remain
held because comparable units, independent outcomes, persistence, falsifiers,
or decision evidence are incomplete. Rights and publisher-dependence reviews
remain open where the exact artifact or reuse terms have not been verified.
