# Cultural, social, and geopolitical theme mining v1

## Governing goal

Build a repeatable, US-centered research system that starts with scattered evidence and ends with clear, testable findings about what is changing beneath visible events.

The main object is the American customer, consumer, household, worker, investor, voter, and public institution. International evidence is used when it changes the conditions facing people or firms in the United States, or when it gives us a useful comparison. The project is not a general world-news digest.

The system will mine research stories, working papers, datasets, public records, company evidence, surveys, and security data. It will connect those sources across four questions:

1. What is changing in the material world: work, money, energy, health, technology, land, trade, and production?
2. How does that change enter daily life: family, status, trust, identity, place, migration, and behavior?
3. Which institutions respond: firms, schools, courts, regulators, unions, parties, media, and public agencies?
4. How does power move: who gains choices, who bears risk, who sets rules, who owns the asset or data, and who can make others wait?

The final product is not a news summary. It is a source-traceable explanation:

```text
source
  -> measured claim
  -> method and limit
  -> causal step
  -> affected people and institutions
  -> cultural and social meaning
  -> geopolitical or state effect
  -> company and sector exposure
  -> finding, counterevidence, and next test
```

Every important sentence must be traceable to a source, marked as an inference, or marked as an open question.

## Why this project exists

Many public stories show the final surface of a change: a new policy, a new tool, a price move, a conflict, a company decision, or a shift in public opinion. The deeper cause is often spread across several fields and institutions.

One source may explain the firm. Another may measure the household. A third may show the financial constraint. A fourth may show the state response. The work of this project is to connect those pieces without pretending that they say more than they do.

The system should help answer questions such as:

- When does a technology change who controls work rather than simply making work faster?
- When does a financial rule change family life, firm strategy, or political trust?
- When does energy dependence become a diplomatic or security problem?
- When does a change in migration or age structure alter local business, care, and elections?
- When does a company trend reveal a wider change in status, identity, or social behavior?
- When does an economic dependency give one state leverage over another?
- When does a change in prices, credit, housing, work, or service quality alter how Americans behave and what they believe?
- When does a firm's customer strategy shift risk from a balance sheet onto households or public systems?
- When does a financial or political incentive make a useful reform hard to carry out?

## Source architecture

### Starting sources

- [Harvard Business School Working Knowledge](https://www.library.hbs.edu/working-knowledge): readable research stories and topic discovery.
- [NBER Working Papers](https://www.nber.org/papers): early research, methods, results, and related programs.

### Research and interpretation

- [Brookings](https://www.brookings.edu/topics/)
- [Chatham House](https://www.chathamhouse.org/topics)
- [Carnegie Endowment](https://carnegieendowment.org/research/)
- [World Bank Research](https://www.worldbank.org/en/research)

### People and social life

- [Pew Research Center](https://www.pewresearch.org/)
- [UNDP Human Development Data](https://hdr.undp.org/data-center)

### Material and economic conditions

- [World Bank Open Data](https://data.worldbank.org/)
- [OECD Data Explorer](https://data-explorer.oecd.org/)
- [IMF Data](https://data.imf.org/en)
- [IMF publications by Manmohan Singh](https://www.imf.org/en/publications/publications-by-author?author=Manmohan%20Singh&name=Manmohan%20Singh)
- [ILOSTAT](https://ilostat.ilo.org/)
- [FRED](https://fred.stlouisfed.org/)
- [BEA Learning Center](https://www.bea.gov/resources/learning-center)

### Money, energy, and security

- [BIS Papers](https://www.bis.org/publications/bis-paper)
- [Office of Financial Research](https://www.financialresearch.gov/)
- [IEA Reports](https://www.iea.org/analysis?type=report)
- [SIPRI databases](https://www.sipri.org/databases)

The registry in `manifests/source-registry.json` records the role, source type, access note, and use limit for each source.

## Scope lock

The first release will support:

- topic discovery and topic queues;
- source metadata and page capture;
- paper, report, dataset, survey, filing, and public-record notes;
- claim and evidence ledgers;
- method, sample, date, geography, and limitation records;
- material, social, institutional, and power maps;
- theme and subtheme links;
- company and sector exposure notes;
- Markdown finding cards and HTML research pages;
- source coverage and contradiction reports;
- versioned manifests and reproducible builds.

The first release will not claim to predict elections, forecast markets, prove hidden coordination, infer private motives, or establish causality from repeated headlines. It will not copy full articles or papers. It will not treat a model-generated connection as evidence.

## End-to-end workflow

### Phase 0 — Freeze the question

Every project starts with one bounded question, a time window, a geography, affected groups, and a reason the question matters.

The project must state:

- the visible event or trend;
- the deeper change being tested;
- the people, firms, or institutions in scope;
- the smallest useful unit of analysis;
- what is outside the project;
- what evidence could change the question itself.
- which US population, place, market, or institution is the primary unit;
- whether the question is about customers, consumers, workers, firms, investors, voters, or public agencies;
- what foreign evidence is being used as comparison rather than as the main subject.

Exit evidence: a project brief with a question, scope, source plan, and falsification plan.

### Phase 1 — Build the source universe

Search the registered sources by topic, author, research program, paper metadata, geography, date, and related terms. Save a source record before writing about it.

Each source record must include:

- stable URL and access date;
- title, author, institution, date, revision, and source type;
- abstract or short description in our own words;
- data and method;
- geography, population, and time range;
- license and permitted-use note;
- related sources and later versions;
- reason the source matters to the project.

Exit evidence: a dated source manifest with search terms, results screened, included sources, excluded sources, and known access gaps.

### Phase 2 — Extract claims, not prose

For each source, record only claims that can be checked. Separate:

- what the source directly observes;
- what the authors estimate or compare;
- what the source suggests but does not establish;
- what we infer by connecting it to another source.

Do not let an attractive phrase become the finding. The finding must survive contact with the table, figure, method, and limits.

Exit evidence: a claim ledger where every claim has a source, evidence location, confidence label, and limit.

### Phase 3 — Test the mechanism

Write the proposed chain in short form:

```text
condition -> constraint or choice -> behavior -> measured result -> wider effect
```

For every arrow, ask:

- Is this step measured?
- Is it only inferred?
- Could another mechanism explain the result?
- Who acts, and what choice do they have?
- What time delay exists between the steps?
- Does the mechanism work in another place, group, or period?

Exit evidence: a mechanism map with direct evidence, inference labels, competing explanations, and open links.

### Phase 4 — Build the four maps

#### Material map

Track US work, wages, prices, debt, credit, housing, consumption, energy, land, technology, health, trade, production, and physical infrastructure.

#### Social map

Track American family life, care, status, trust, identity, class, race, gender, age, migration, place, and daily behavior.

#### Institution map

Track firms, schools, courts, regulators, unions, parties, media, public agencies, and international bodies.

#### Power map

Track ownership, bargaining power, exit options, rule-setting, risk transfer, information control, waiting power, and dependence.

For US political and financial work, also track who can set the terms of credit, prices, benefits, access, enforcement, and public attention.

Exit evidence: each proposed theme connects at least two maps and names what is still missing from the other maps.

### Phase 5 — Make the theme and subthemes

A theme is a repeated mechanism across several findings. A subtheme is a narrower path inside it.

For example:

```text
theme: control moves from workers to systems
  -> AI changes task measurement
  -> measurement changes promotion and bargaining
  -> bargaining changes household security
  -> household security changes local politics and trust
  -> technology dependence changes national leverage
```

The theme cannot be supported by one article or one institution. It needs multiple source families, a clear link between findings, and at least one serious counterargument.

Exit evidence: a theme map with linked finding IDs, source diversity, agreement, disagreement, and confidence.

### Phase 6 — Link the theme to firms and sectors

Only after the social and institutional mechanism is clear, examine company and sector exposure.

Record:

- which input, cost, customer, worker, asset, or rule is affected;
- which firms gain options and which lose them;
- whether the change is a tailwind, headwind, or transfer of risk;
- what the annual report, filing, earnings call, or operating data directly shows;
- what is only a hypothesis about future effects.

This keeps company research connected to the wider world without turning every social change into an investment claim.

Exit evidence: a company and sector bridge that links each exposure to a measured condition and a stated uncertainty.

### Phase 7 — Write the finding

Each finding card must contain:

1. one-sentence finding;
2. what we directly know;
3. the causal chain;
4. who gains, loses, adapts, or cannot exit;
5. material, social, institutional, and geopolitical meaning;
6. company or sector exposure, if relevant;
7. limits and missing evidence;
8. what would change our mind;
9. a source table.

The Markdown version is the working record. The HTML version is the readable public page. They must contain the same claims and source links.

### Phase 8 — Recheck and publish

Before publication:

- rerun the source and claim checks;
- check every link and source date;
- check that working papers are labeled as provisional;
- check that forecasts and scenarios are not written as observed facts;
- check that quotes remain within permitted use;
- check that the HTML matches the Markdown;
- preserve the manifest, hashes, and build date;
- record unresolved questions for the next review.

Exit evidence: a versioned Markdown memo, HTML page, source manifest, claim ledger, contradiction report, and publication check.

## Evidence rules

### Source hierarchy

Use original studies, official statistics, datasets, filings, and public records for core claims. Use institutional reports and expert analysis to provide context or competing explanations. Use news and commentary mainly for discovery unless the item itself is the primary record of an event.

### Provisional work

Working papers, forecasts, scenarios, early estimates, and expert views receive explicit labels. A provisional source may support a question or a conditional finding. It cannot silently support a settled claim.

### No false connection

Two trends moving together do not prove that one caused the other. A theme may be plausible before it is proven. The memo must say which it is.

### No hidden certainty

Confidence is based on evidence quality, not on how many sources repeat the same words. Ten summaries of one study are still one study.

### No source laundering

If a secondary article cites a paper, read the paper when possible. If the paper cites a dataset, read the data definition. If a policy report makes a claim, identify whether it is measured, modeled, or recommended.

### No invented balance

A weak counterargument should not be added merely to look balanced. Include the strongest reasonable challenge and explain whether it changes the finding.

## Coverage and quality gates

A project is ready for publication only when:

1. the question and scope are frozen;
2. the source search is recorded;
3. every major claim has a source and location;
4. the method, sample, date, geography, and limit are recorded;
5. direct evidence and inference are separated;
6. at least two source families support the central mechanism;
7. at least one source challenges the mechanism;
8. affected groups and distribution are named;
9. the material, social, institutional, and power maps are complete enough to show gaps;
10. working papers, forecasts, and scenarios are labeled;
11. company links do not outrun the evidence;
12. Markdown and HTML say the same thing;
13. source links, hashes, and build records pass validation;
14. the limits and next tests are visible to the reader.

## Core deliverables

The repository will contain:

- source registry and source manifests;
- topic queue and project briefs;
- raw source records and access notes;
- claim and evidence ledgers;
- method and coverage reports;
- finding cards;
- theme and subtheme maps;
- company and sector bridges;
- Markdown research memos;
- matching HTML pages;
- source, link, claim, and build validators;
- versioned publication manifests.

## First major project

Start with **AI, work, and control**.

Question: when firms adopt AI, does the main change come from better tools, tighter measurement, new supervision, or a shift in who owns the work process?

The project must compare:

- output and productivity;
- task and skill change;
- monitoring and bargaining power;
- wages, promotion, and career movement;
- small firms versus large firms;
- household security and social status;
- local political trust;
- technology and labor dependence between states.

The next major US-centered stream should extend this method from workplace AI into customer, consumer, societal, financial, and political life. It should ask how firms, credit conditions, public policy, technology, and social meaning interact in the daily experience of people in the United States.

Its first recurring chain is:

```text
US condition or shock
  -> firm, household, market, or government response
  -> change in price, access, work, debt, security, or service quality
  -> change in behavior, trust, identity, or political demand
  -> institutional response and distribution of power
  -> company, sector, financial, and geopolitical exposure
  -> finding, counterevidence, and next test
```

The starter brief is in `analysis/projects/ai-work-control/README.md`.

## Release rule

The first release proves a sound research and publishing process. It does not claim that the system has discovered secret causes, predicted political events, or established universal laws.

The standard is useful restraint: show the evidence, show the bridge between facts, name the people and institutions involved, and leave the reader able to check the work.
