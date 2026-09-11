# Macro and infrastructure source packet v1

**Status:** source packet opened; findings not yet settled  
**Checked:** 2026-09-11  
**Project:** AI, work, and control  
**Question:** when AI spreads, do gains stay inside firms, or do they move through wages, firm size, energy systems, finance, and state power?

## Why this packet is next

The first packet followed AI into the workplace. It found that the system's function matters: helping a worker, setting the pace, watching the worker, scoring the worker, and deciding personnel action are different events.

The next question is what makes some functions possible and valuable. The new source set adds five layers that the worker evidence cannot answer alone:

```text
firm adoption and capital
  -> measured productivity and prices
  -> wages, firm size, and inequality
  -> electricity, chips, cloud, and data capacity
  -> financial exposure and public budgets
  -> country advantage, dependence, and bargaining power
```

This is a source map, not proof of that whole chain.

## Source records opened

| Source | What it can measure | Direct result or useful starting point | Method / status | Function or power question |
|---|---|---|---|---|
| [IMF Working Paper 2025/068: AI Adoption and Inequality](https://www.imf.org/en/publications/wp/issues/2025/04/04/ai-adoption-and-inequality-565729) | Household distribution, tasks, wages, wealth, and firm adoption choice | Its household microdata and calibrated task model separates wage inequality from wealth inequality. It reports that voluntary firm adoption can make the wealth effect especially unequal because firms automate high-wage tasks to save costs. | Model plus household microdata; IMF says working papers are research in progress | Who chooses adoption, and who owns the capital that captures the saved cost? |
| [BIS Working Paper 1325: AI adoption, productivity and employment](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms) | Firm productivity, employment, wages, firm size, finance, software, data, and training | Using more than 12,000 matched EU and US non-financial firms, the paper reports a 4% short-run labor-productivity increase, no short-run employment reduction, higher wages in adopting firms, and larger gains for medium and large firms. | Matched EIBIS-ORBIS data and an instrument based on US peers; authors state views are not necessarily BIS policy | Is AI assistance the event, or is capital deepening and complementary investment the real driver? |
| [BEA Digital Economy](https://bea.gov/data/special-topics/digital-economy) | AI measurement, production accounts, prices, data assets, GDP, productivity, and digital trade | BEA is developing AI economic accounts and lists work on AI utilization, expectations and outcomes, industry production accounts, costs and prices, and capitalized data. | Official measurement program; several listed items are new working papers or early estimates | What is counted as output, capital, data, or productivity before distribution is judged? |
| [IEA Energy and AI](https://www.iea.org/reports/energy-and-ai) and [Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai) | Data-centre electricity, grids, fuels, emissions, minerals, affordability, and security | IEA's 2025 report projects global data-centre electricity generation needs to rise from about 460 TWh in 2024 to more than 1,000 TWh in 2030 in its base case. Its 2026 update says AI-focused data-centre electricity use grew faster than total data-centre use in 2025 and highlights grid, supply-chain, and critical-mineral limits. | Global modeling and datasets; scenarios are conditional, not forecasts of certainty | Which places can provide power and connection speed, and who bears grid and land costs? |
| [OFR 2025 Annual Report](https://www.financialresearch.gov/annual-reports/files/OFR-AR-2025.pdf) | Financial-system monitoring, data infrastructure, third-party risk, public analytics capacity, and agency workforce | OFR reports using AI for data processing, security monitoring, support tasks, and ChatOFR; it also reports a 47% decline in its FY2025 workforce and an 11% budget reduction while responsibilities were rebalanced. The report does not establish that AI caused the workforce change. | Official annual report; institutional self-report | When public analytical capacity changes alongside AI and budget cuts, does the state become more or less able to inspect private systems? |
| [World Bank World Development Report 2026: The Promise of AI](https://www.worldbank.org/en/publication/wdr2026) | Development, jobs, public services, infrastructure, skills, institutions, trade, energy costs, and political power | The report says AI's gains depend on local complements and mismatch between development and deployment contexts can weaken results. It frames AI's political impact as reshaping power within and across countries. | Global development report; chapter claims and scenarios need direct table and method review | Does imported AI reduce local capability, or help countries build it? Under what infrastructure and institutional conditions? |

## Early comparison

The sources already disagree in a useful way:

- The BIS firm evidence points to productivity and wages without short-run job loss, but with larger gains for larger firms.
- The IMF model warns that firm choice and capital ownership can still widen wealth inequality even when wage inequality moves differently.
- The World Bank emphasizes local complements and the risk of a widening gap between countries.
- The IEA shows that AI depends on physical systems—electricity, grids, minerals, and connection queues—not only software.
- The OFR record shows that a public institution can use AI while its workforce and analytical infrastructure are also changing, but it cannot tell us the causal role of AI.
- BEA shows that even the measurement of AI output, data capital, cost, and productivity is still being built.

The next finding should therefore not be “AI raises productivity” or “AI causes inequality.” The sharper question is:

> Who can turn AI capability into durable capacity, and who remains dependent on the firms and states that control the complements?

That is a working hypothesis, not an established conclusion.

## Extraction plan

For every item, capture:

1. the exact unit: worker, household, firm, sector, grid, financial institution, or country;
2. whether the result is observed, estimated, modeled, or self-reported;
3. the complement required: capital, data, software, training, power, cloud, skills, or institutions;
4. who pays for it and who owns it;
5. the distributional result: wages, wealth, firm size, prices, jobs, public capacity, or regional access;
6. the path by which a local change could become cross-border dependence;
7. the strongest counterexample and what would change the conclusion.

## Required next reading

1. Read the full IMF model assumptions and sensitivity checks.
2. Read BIS 1325 tables on firm size, finance, software, data, training, and wages.
3. Open the underlying BEA AI papers and production-account tables; record definitions before comparing them with NBER results.
4. Extract IEA regional tables on grid connection, fuel mix, minerals, and affordability.
5. Separate OFR's AI use from its workforce reduction and inspect its third-party and operational-risk sections.
6. Read World Bank chapters 3, 4, 5, and 6 for the same complements-to-power chain across developing economies.
7. Add one source that disputes concentration or dependence, not only one that supports it.

## Related records

- [System-function evidence matrix](system-function-evidence-matrix-v1.md)
- [Finding 010](findings/ai-work-control-010.md)
- [Coverage report](coverage-report-v1.md)
- [Source expansion plan](../../../analysis/source-expansion-plan.md)
