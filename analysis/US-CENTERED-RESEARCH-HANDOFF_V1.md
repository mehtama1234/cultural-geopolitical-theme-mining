# US-centered research handoff v1

## Connected reading guide: current handoff

Start with [the HTML guide](../site/us-theme-atlas.html) and its [Markdown edition](us-theme-atlas.md). Eighty-four topics now sit under five shared themes, with one hundred and seventy-four explained cross-topic connections. Each topic includes subthemes, sources and limits. Connections are labeled as comparisons or questions to test; they are not established causes.

Maintain these relationships in [the shared record](../manifests/us-theme-connections.json). When adding a finding, check related topics by meaning: who is affected, what changed, what choice became harder, and what might happen next. Explain each useful connection in one ordinary sentence and name what evidence is missing. Do not connect topics only because they share a word. Keep the bigger-picture summary honest about which links remain untested.

Eighty-five reading paths now link household costs, care, work, housing, credit, insurance, customer service, public help and political response. Each path explains its shared question and missing evidence. Every adjacent pair must have a recorded connection; the builder checks this. These paths guide reading, not causal conclusions.

Rebuild both editions with `python3 scripts/build_us_theme_atlas.py`. Preserve search, theme filters, direct topic links, expandable sources and connections, readable phone layouts, and visible uncertainty. The [browser check](us-theme-atlas-browser-check.md) records the interactions already tested. Extend those checks when changing navigation or layout.

Keep research passes short. Add a supported finding, a useful connection, or a clear unresolved question, then move to the next topic. The eighty-three opening packets exist; the next work is checking their strongest claims and connections, not recreating project briefs.

The current deepening pass has added fuller household paths to the Markdown records for transportation, rideshare, income timing, childcare, safety-net access, payment fees, utility debt and shutoff, energy and housing, repair and replacement, credit records, rent guarantees, small businesses, reviews, customer automation, inflation, and the big-picture synthesis. These edits are useful only when the HTML page carries the same argument. A valid HTML file is not enough if it still shows an older summary.

The next publishing check is therefore page parity: compare every changed Markdown finding with its HTML page for the title, argument, evidence limits, deeper finding, unknowns, next test, reading rule, and source links. Mark a page `matched`, `HTML-valid-but-stale`, or `missing`. Do not call a finding complete until it is both evidence-checked and matched in the reader-facing page.

The current run of `python3 scripts/validate_us_finding_parity.py` checks 64 finding pairs and passes all 64. The check confirms that “HTML parses” and “HTML matches the current finding” are different gates; keep this parity check in the publication gate whenever a finding changes.

The consolidated `python3 scripts/validate_long_term_publication_gate.py` now runs the program-control, source-coverage, provenance, observation-schema, finding parity, watchlist parity, published-link, local-link, and whitespace checks as one reproducible handoff gate.

## Where we are going

The canonical inventory of the broader societal, cultural, consumer, political, company, sector, and geopolitical objective is [US broad theme inventory v1](US-BROAD-THEME-INVENTORY_V1.md). The shorter [end-to-end program recovery brief](../END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md) is the first file to read after a crash or context loss.

The next major research stream will study the United States from the inside out: what customers and households experience, how firms respond, how money and credit shape the choices available, how public institutions react, and how those changes become social and political pressure.

## Canonical broader objective — do not narrow this to one household

The project is building a broad US map of societal, cultural, consumer, institutional, financial, and political change from many source families. The household-calendar study is only one measurement instrument inside that program; it is not the overall goal and must not replace the population-, market-, firm-, place-, and institution-level analysis.

The actual objective is to extract recurring themes across datasets, surveys, research papers, public records, company evidence, and political or cultural measures:

1. **What families give up to pay the bills:** housing, health care, insurance, food, savings, credit, utilities, repairs, and hidden household tradeoffs.
2. **Who gives up time:** commuting, caregiving, multiple jobs, administrative burden, customer-service loops, unpaid labor, and time as the real price of cheap or free services.
3. **Who can get an answer or change a decision:** appeals, human support, privacy, platform rules, credit records, benefit administration, legal help, switching costs, and exit power.
4. **Who controls the work and gets the gain:** AI, monitoring, schedules, workplace autonomy, employer dependence, career mobility, benefits, productivity, bargaining power, and risk transfer.
5. **How places and infrastructure distribute exposure:** energy, housing condition, insurance, water, transport, climate risk, repairs, service reliability, and the ability to remain or move.

These umbrella themes contain the broader recurring questions the project must continue extracting:

- whether consumer convenience, fees, subscriptions, data rules, ratings, automation, and platform ownership change real choice;
- whether families experience prices, care, debt, insurance, benefits, and housing as sacrifices of money, time, health, security, or freedom;
- whether firms and public programs improve their headline outcome by shifting costs to workers, customers, owners, families, or future bills;
- whether work, employer power, AI, multiple jobs, and benefits change status, autonomy, bargaining power, and local dependence;
- whether private material pressure becomes cultural meaning, trust, blame, identity, public demand, or political action;
- whether personal economic experience and national economic judgment diverge, and what connects a cost to a political interpretation;
- how race, class, age, disability, gender, family structure, migration, geography, and institutional access change who bears the risk;
- how financial, technological, energy, and supply dependencies affect US firms, communities, and state power.

The cross-domain chain to preserve is:

```text
US condition, price, rule, shock, or institutional decision
  -> cash, time, access, control, status, or security changes
  -> customers, households, workers, firms, or voters adapt, delay, borrow, switch, stay, or go without
  -> firm, lender, employer, platform, regulator, court, agency, media, or party responds
  -> costs and power move between people, firms, families, and public systems
  -> culture, trust, identity, public demand, political judgment, and geopolitical or sector exposure may change
  -> finding with evidence, counterevidence, limits, and next test
```

Do not turn this into one grand causal theory. Each link must remain labeled as observed, reported, inferred, compared, or open. The goal is a connected societal research map whose strongest paths can later be tested with joined records—not a single-household story.

The active execution queue is [US broad research pass v1](US-BROAD-RESEARCH-PASS_V1.md). It prioritizes five bridges: price/payment to household room; service or platform rules to recourse and trust; work tools to control and power; housing, energy, and insurance to health and mobility; and public aid or rules to interpretation and political response.

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

The repository already has the research method, source registry, AI/work-control project, claims ledger, findings, theme map, company bridges, source packets, and HTML publishing pattern. The current US atlas maintains **255 validated trend records, 979 observations, 103 source-search packets, 14 broad program themes, 174 explained connections, 85 reading paths, and 529 link-validated HTML pages**. It currently carries one hundred and seventy-four connections, and eighty-five reading paths. The next implementation step is to deepen the strongest open links with matched US evidence, then turn the strongest path into a complete finding from source to lived effect to institutional response.

The current implementation has completed a substantial first deepening pass and has kept the atlas validator green. Reader-facing HTML is now published for the deepened routes, including the CMS-to-MEPS health-cost bridge and the recurrent-source watchlist. The remaining end-to-end work is not more prose alone: use the integrated household calendar and same-episode ledgers to test the strongest cross-topic chains with actual joined records, while preserving source-vintage controls and the missing event-level links.

The first concrete design for that next study is [the household-calendar integration brief](US-HOUSEHOLD-CALENDAR-INTEGRATION_V1.md), with a [reader-facing HTML edition](../site/us-household-calendar-integration.html). It defines the twelve-month unit, event ledger, five linked tests, comparison design, privacy rules, and conditions that would change the working picture. It is a plan for evidence collection, not evidence of a national effect.

The first source boundary pass is recorded in the [household-calendar source search record](projects/us-household-calendar-integration/source-search-record-v1.md). It assigns roles to SIPP, CE, ATUS, BEA, SHED, MEPS, and RECS, and states where a new consent-based calendar panel is still needed.

The next working artifact is the [source-to-question matrix](projects/us-household-calendar-integration/source-to-question-matrix-v1.md). It maps each claim to direct evidence, useful proxies, missing fields, and a small first extraction pass.

The first time-and-money bridge is in the [time and spending layer](projects/us-household-calendar-integration/time-spending-layer-v1.md). It defines how ATUS and CE can set scale and categories without being falsely merged into one household panel.

The first published-table reference pass is in the [ATUS and CE reference pass](projects/us-household-calendar-integration/atus-ce-reference-pass-v1.md). It records the transport spending and work/care travel baselines, with their units and limits.

The first transport paper scan is in the [transport paper scan](projects/us-household-calendar-integration/transport-paper-scan-v1.md), with a [reader-facing HTML page](../site/us-transport-paper-scan.html). It separates household choice, city-wide effects, and worker or firm effects, then turns the reading into questions for the calendar.

The next connected reading pass is [housing and insurance risk](projects/us-housing-insurance-affordability/paper-scan-v1.md), with a [reader-facing HTML page](../site/us-housing-insurance-paper-scan.html). It follows how a place risk or credit record can become a premium, coverage gap, financing problem, repair delay, sale loss, or public cost. The existing [home-insurance finding](../site/us-home-insurance-matched-evidence-001.html) carries the current evidence-backed argument.

The first household-level check for that topic is the [Federal Reserve insurance pass](projects/us-housing-insurance-affordability/fed-shed-housing-insurance-pass-v1.md). It separates no coverage, too little coverage, and coverage that is hard to carry.

The public-record map is in [housing and insurance public records](projects/us-housing-insurance-affordability/public-record-map-v1.md). It defines what SHED, Treasury FIO, FEMA, NFIP, FHFA, HMDA, and ACS can each contribute and where the same-property gap remains.

The first direct market-data acquisition is recorded in the [Treasury FIO supporting-metrics audit](projects/us-housing-insurance-affordability/fio-supporting-metrics-audit-v1.md). It checks the ZIP-year workbook structure and preserves Treasury’s coverage and privacy limits.

The next connected paper pass is [health costs and the choices people give up](projects/us-health-cost-household-choice/paper-scan-v1.md), with a [reader-facing HTML page](../site/us-health-cost-paper-scan.html). It separates the bill, the payment problem, the credit record, the health effect, and the work or care choice that may follow. The health-cost lane now also has a [CES medical-affordability action finding](findings/us-medical-affordability-political-action-matched-evidence-001.md): same-respondent hardship, attribution, and political action are observed, while the dated bill-to-remedy-to-legitimacy join remains open.

The consumer-power lane now has a bounded [CFPB response route layer](projects/us-consumer-fraud-trust/cfpb-response-route-layer-v1.md). It adds product-conditioned patterns for monetary relief, non-monetary relief, explanation, pending review, and response timing. It does not treat administrative closure as verified recovery, restored trust, switching, or political action; those remain the next linked-record gap.

The next political bridge is [cost, trust, and political response](projects/us-cost-trust-politics/paper-scan-v1.md), with the existing [reader-facing finding](../site/us-cost-trust-politics-path-001.html). It uses household price actions, real wages, sentiment, party identity, and trust as separate measures rather than one “economic mood” number.

The program is deliberately open-ended. “Exhaustive” means a recorded search across the defined source universe, clear inclusion and exclusion rules, repeated searches over time, and visible gaps—not a claim that every relevant source or hidden cause has been found.
