# US-centered research handoff v1

## Connected reading guide: current handoff

Start with [the HTML guide](../site/us-theme-atlas.html) and its [Markdown edition](us-theme-atlas.md). Sixty-three topics now sit under five shared themes, with ninety-one explained cross-topic connections. Each topic includes subthemes, sources and limits. Connections are labeled as comparisons or questions to test; they are not established causes.

Maintain these relationships in [the shared record](../manifests/us-theme-connections.json). When adding a finding, check related topics by meaning: who is affected, what changed, what choice became harder, and what might happen next. Explain each useful connection in one ordinary sentence and name what evidence is missing. Do not connect topics only because they share a word. Keep the bigger-picture summary honest about which links remain untested.

Fifty-eight reading paths now link household costs, care, work, housing, credit, insurance, customer service, public help and political response. Each path explains its shared question and missing evidence. Every adjacent pair must have a recorded connection; the builder checks this. These paths guide reading, not causal conclusions.

Rebuild both editions with `python3 scripts/build_us_theme_atlas.py`. Preserve search, theme filters, direct topic links, expandable sources and connections, readable phone layouts, and visible uncertainty. The [browser check](us-theme-atlas-browser-check.md) records the interactions already tested. Extend those checks when changing navigation or layout.

Keep research passes short. Add a supported finding, a useful connection, or a clear unresolved question, then move to the next topic. The sixty-three opening packets exist; the next work is checking their strongest claims and connections, not recreating project briefs.

## Where we are going

The next major research stream will study the United States from the inside out: what customers and households experience, how firms respond, how money and credit shape the choices available, how public institutions react, and how those changes become social and political pressure.

The aim is to find the deeper mechanism beneath a visible trend. A headline is only the entry point. The work should show the path from a measurable condition to a change in daily life, then to a change in institutional power.

```text
US condition or shock
  -> who changes behavior and why
  -> price, access, work, debt, housing, health, or service effect
  -> household and community meaning
  -> firm, lender, regulator, court, media, or party response
  -> who gains room to act and who carries the risk
  -> financial, company, sector, and geopolitical consequence
  -> finding with limits, counterevidence, and next test
```

## What to study

Start with topics that touch several of these at once:

- customer and consumer behavior;
- household income, debt, housing, care, health, and security;
- prices, fees, insurance, credit, banking, and financial stress;
- work, wages, automation, status, and career paths;
- firm strategy, market power, consolidation, and risk transfer;
- trust in companies, government, media, science, and experts;
- race, class, age, place, migration, and unequal exposure;
- elections, parties, regulation, courts, public spending, and policy feedback;
- energy, infrastructure, supply chains, and dependence that affect US firms or households.

## How to mine a topic

1. Begin with HBS Working Knowledge and NBER to find the question, study, data, and vocabulary.
2. Search the relevant US primary records: BLS, BEA, Census, Federal Reserve, CFPB, SEC, FDIC, GAO, CBO, FTC, DOJ, courts, state agencies, and company filings.
3. Add surveys and social evidence from sources such as Pew, the General Social Survey, ANES, and reputable university projects.
4. Use IMF, BIS, IEA, World Bank, OECD, and similar sources only when they explain a US constraint, provide a clean comparison, or reveal an outside pressure.
5. Record the source before writing the claim. Keep observed facts, estimates, author interpretations, our inferences, and open questions separate.
6. Follow the same people, dollars, decisions, and risks through time. Look for who pays, who waits, who can leave, who sets the rule, and who owns the data or asset.
7. Look for a serious counterexample: a group, place, company, period, or policy where the proposed mechanism does not hold.
8. Write one plain-language finding in Markdown, then a matching HTML page. No slogans, no inflated language, and no causal claim that the evidence cannot carry.

## Pace and writing rule

Use a short first pass for each topic. In that pass, collect a few strong sources, identify the possible deeper pattern, write down the main limit, and decide whether the topic deserves more time. Do not spend days proving a small point when the evidence is thin. Move on when the next test is clear.

Write as if explaining the idea to an intelligent neighbor: short sentences, common words, concrete people and actions. Avoid business fashion words, academic fog, dramatic claims, and filler. Say “who pays,” “who decides,” “who waits,” and “what changed” instead of using a large abstract label.

## Required output for each topic

- a dated search record and source universe;
- source records with method, population, geography, time, and limits;
- a claims ledger with direct evidence and inference labels;
- a mechanism map and four maps: material, social, institution, and power;
- a US distribution table by group, place, income, race, age, gender, or other relevant exposure;
- a customer/consumer, company/sector, financial, and political bridge;
- at least one counterevidence record;
- a Markdown finding and matching HTML page;
- an explicit “what would change our mind” section;
- open gaps and the next research test.

## First queue

The first queue should favor questions where household experience and institutional power may diverge:

- AI and customer service: does convenience reduce human recourse?
- Fees and subscription pricing: when does a small charge become a household tax?
- Housing and insurance: how do risk models change where people can live and what they can afford?
- Consumer credit: when does access protect a household, and when does it move risk onto the borrower?
- Health and care: how do staffing, payment, and automation change trust and access?
- Work and purchasing power: when do productivity gains fail to become household security?
- Political trust: which material experiences move from private frustration to public demand?
- Infrastructure and dependence: which US firms and communities bear the cost of digital and energy expansion?

## Handoff state

The repository already has the research method, source registry, AI/work-control project, claims ledger, findings, theme map, company bridges, source packets, and HTML publishing pattern. The current US atlas has sixty-three topic records, five themes, ninety-one connections and sixty-five reading paths. The next implementation step is to deepen the strongest open links with matched US evidence, then turn the strongest path into a complete finding from source to lived effect to institutional response.

The program is deliberately open-ended. “Exhaustive” means a recorded search across the defined source universe, clear inclusion and exclusion rules, repeated searches over time, and visible gaps—not a claim that every relevant source or hidden cause has been found.
