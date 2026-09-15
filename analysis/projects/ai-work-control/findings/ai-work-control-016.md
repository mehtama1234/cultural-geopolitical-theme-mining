# Finding 016: AI can lower measured prices while shifting adjustment toward labor, capital, and infrastructure

**Status:** provisional cross-source finding; open for US household and worker outcome tests  
**Checked:** 2026-09-13  
**Project:** AI, work, and control  
**Related evidence:** [institutional context record](../macro-infrastructure-institutional-context-layer-v1.md), [IMF extraction note](../imf-ai-adoption-inequality-extraction-v1.md), [macro source packet](../macro-infrastructure-source-packet-v1.md)

## The finding

The current evidence does not support one universal “AI effect.” It supports a
more specific and more consequential possibility:

> AI can raise measured output and lower some industry price pressures while
> shifting the composition of costs, ownership, work, and infrastructure. The
> distributional result depends on who owns the capital, who controls adoption,
> which workers’ tasks are complemented or displaced, and whether local public
> and physical systems can absorb the new demand.

This is a cross-source synthesis, not a pooled estimate. The sources observe
different units and use different designs. Their disagreement is part of the
finding.

## What each source actually establishes

### 1. Firm productivity can rise without immediate job loss

The [BIS firm study](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms)
uses matched EIBIS-ORBIS data on more than 12,000 EU and US non-financial firms.
It estimates a 4% short-run increase in labor productivity associated with AI
adoption, no adverse short-run firm-employment effect, higher wages in adopting
firms, and larger gains among medium and large firms. The study also points to
software, data, and workforce training as complements.

That result is important but bounded. It says that output per worker can rise
in firms that adopt AI. It does not say that all workers receive the gain, that
the gain persists, that small firms can adopt on equal terms, or that workers
gain decision rights. “No short-run employment reduction” is not the same as
stable careers, promotion, safety, or bargaining power.

### 2. Industry accounts show a cost-structure shift

The [BEA price-and-cost study](https://www.bea.gov/system/files/papers/BEA-WP2026-8.pdf)
examines 1,586 industry-year observations across 61 private-sector industries
from 1997–2023. Its 2022–2023 baseline interaction for gross-output price
growth is -0.0228 for relatively AI-intensive industries. The corresponding
labor-price contribution is -0.0113, the non-college labor-price contribution
is -0.0071, and the materials-price contribution is -0.0019.

The cost-share results point in the same direction: the labor-share interaction
is -0.011, while the capital-share interaction is +0.0084. In plain language,
AI-intensive industries show lower output-price growth and a shift away from
labor’s share toward capital and materials in the study’s post-period.

The paper does not prove that AI caused this shift. Its AI measure is a relative
industry-intensity quartile based on Census survey data; industries are equally
weighted; input-price contributions combine cost shares and input-price
changes; and the analysis cannot fully separate cheaper material bundles,
input substitution, demand, or unmeasured AI costs. It also does not observe
whether lower industry prices reached households.

### 3. A US state-industry layer shows a positive but non-causal output pattern

The newer [BEA state-industry study](https://www.bea.gov/research/papers/2026/ai-utilization-and-economic-performance)
constructs frequent-AI-use exposure from 75,292 Gallup Workforce Panel
observations collected in Q2 2025–Q1 2026. It links the exposure to 2016–2024
state-industry employment, earnings, and real-output outcomes.

State-industry cells with higher worker-reported frequent AI use show stronger
post-2020 real-output paths. The paper reports approximate semi-elasticities of
0.1–0.2% higher real output and 0.4–0.6% higher employment for each
one-percentage-point higher share of frequent AI users. The employment result
is imprecise. An employer-reported, industry-only BTOS specification does not
recover the same output pattern.

This measurement difference is analytically useful. Workers may report using AI
for a broad range of tasks while firms report narrower use in formal business
functions. The worker-based measure may therefore capture more realized task
use, but it also faces small-cell and worker-selection limits. The study is
descriptive rather than causal: prosperous or well-managed state-industry cells
may both adopt more AI and grow faster.

### 4. Wage inequality and wealth inequality can move in opposite directions

The [IMF Working Paper 2025/068](https://www.elibrary.imf.org/view/journals/001/2025/068/article-A001-en.xml)
combines household microdata with a calibrated task model. In its baseline
2014–2048 AI scenario, the modeled wage Gini falls by 1.73 percentage points,
while the modeled wealth Gini rises by 7.18 percentage points.

The mechanism is not contradictory. AI can displace some high-income tasks and
raise productivity for lower-income workers, reducing wage dispersion. At the
same time, higher-income workers may hold tasks complementary with AI and are
better positioned to receive capital income. When firms choose how much AI to
adopt, modeled cost savings from automating high-wage tasks increase adoption
and make the wealth effect especially pronounced.

These are scenario outputs, not observed US inequality. The result depends on
task displacement, complementarity, capital returns, household distributions,
and the assumed adoption rule. The model does not observe taxes, bargaining,
ownership transfers, worker voice, or political response.

### 5. Public institutions can become more efficient and less capacious at once

The [OFR 2025 Annual Report](https://www.financialresearch.gov/annual-reports/files/OFR-AR-2025.pdf)
reports AI use in data processing, security-compliance monitoring, technology
support, procurement analysis, and ChatOFR. It also reports a workforce path
from 188 employees at the start of FY2025 to 205 in January and 109 at year-end,
with 30% of staff participating in deferred-resignation programs. Its budget
fell from $124.6 million to $110.7 million.

During the same period, OFR decommissioned the shared Joint Analysis Data
Environment, retained OFRAE as its core analytics environment, and added cloud
and GPU capabilities. The report’s own account therefore contains both
capacity expansion and capacity withdrawal.

This cannot be reduced to “AI replaced workers.” The report does not establish
that causal story. A smaller institution may maintain selected services through
automation, while losing training, data procurement, partnerships, or
cross-agency collaboration. Whether oversight becomes stronger or weaker is an
open outcome requiring measures of analytical throughput, error detection,
regulatory response, and financial-system resilience.

### 6. AI capability is materially dependent on energy and local complements

The [IEA Energy and AI analysis](https://www.iea.org/reports/energy-and-ai)
places data-center expansion inside electricity generation, grid connection,
equipment, fuels, and critical-mineral systems. The [World Bank WDR 2026](https://www.worldbank.org/en/publication/wdr2026)
adds infrastructure, skills, data, and institutions as local complements and
frames concentration in advanced models, chips, and data centers as a source
of dependency risk.

The implication is not that every data center harms local households or that
every imported model creates dependence. It is that software capability has a
physical and institutional base. Places with power, connection capacity,
skills, capital, interoperability, and public safeguards can capture more of
the upside. Places without them may consume tools while remaining dependent on
external firms, cloud providers, capital, and standards.

## The end-to-end interpretation

The evidence currently supports this conditional map:

```text
AI adoption and firm capital
  -> output and task productivity
  -> labor/capital/material cost restructuring
  -> prices, wages, and ownership returns
  -> worker and household distribution
  -> public analytical capacity and recourse
  -> electricity, cloud, data, and infrastructure demand
  -> local capability or external dependence
  -> political legitimacy and state bargaining power
```

The first five stages have partial evidence. The final stages are context and
mechanism evidence, not established causal outcomes.

## Contradictions to preserve

1. BIS finds higher productivity and no short-run employment reduction, while
   BEA finds a lower labor-share interaction.
2. BEA finds lower modeled industry price growth, but that does not show lower
   household prices or fair distribution of savings.
3. The IMF model permits lower wage inequality and higher wealth inequality at
   the same time.
4. Worker-reported AI use predicts a stronger output path descriptively, while
   employer-only measurement does not reproduce it.
5. OFR reports operational AI improvements alongside workforce, budget, and
   collaborative-platform reductions.
6. World Bank and IEA evidence makes infrastructure a condition of capability,
   but the local incidence of that infrastructure remains unmeasured.

## What would change the finding

The finding would weaken if compatible US evidence showed that AI-intensive
firms consistently reduce capital concentration, raise labor share, and
deliver gains to workers and households across firm sizes. It would strengthen
if linked data showed that AI-intensive firms concentrate ownership returns,
reduce labor share or bargaining power, pass savings unevenly to purchasers,
and place measurable energy or public-capacity burdens on particular places.

## Next empirical tests

1. Link state-industry AI utilization to firm size, ownership, wages, training,
   and job flows using compatible LEHD, QCEW, Census, and business-survey
   universes.
2. Test whether output-price associations appear in consumer-facing prices and
   household expenditure baskets rather than stopping at industry accounts.
3. Compare AI-intensive and other firms by labor share, wage distribution,
   worker mobility, and training access.
4. Measure OFR-like public-capacity outcomes: data coverage, processing time,
   error detection, supervisory action, and interagency analytical access.
5. Match data-center electricity and rate-governance records to household bills,
   local revenue, water/environmental burden, jobs, and legitimacy measures.
6. Obtain cross-country firm or enterprise-survey microdata to test whether
   adopt/adapt capacity predicts local productivity, worker outcomes, and
   dependence on external providers.
