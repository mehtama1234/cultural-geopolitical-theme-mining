# Project: US household financial pressure and the price of access

The [2024 Consumer Expenditure income-quintile layer](ce-2024-income-quintile-distribution-layer-v1.md)
adds a population spending distribution to the household-pressure branch. It
shows that income and expenditure changes differed across quintiles, with the
lowest-quintile increase concentrated in housing; it does not measure security,
liquid cash, or political meaning.

## Question

When American households face higher prices, fees, interest, or risk, how do firms and financial institutions change the terms of access—and when does private financial pressure become a social or political problem?

This project begins with payment and credit systems, then expands only when the evidence shows a link to housing, health, work, insurance, or public policy.

## Current population layer

The [2025 SHED price-adaptation layer](shed-2025-price-adaptation-layer-v1.md)
adds weighted national respondent-level comparisons of price pressure,
consumer substitution, reduced use, saving cuts, borrowing, delayed purchases,
extra work, emergency capacity, and outside help. It is a descriptive layer
inside the broader 14-theme program, not the program’s definition and not a
one-household case study.

The [SHED 2024–2025 panel persistence layer](shed-2024-2025-panel-persistence-layer-v1.md)
adds 4,419 same-respondent transitions. It shows persistence in financial
condition and repeated price adaptations, while keeping the causes and later
trust or political effects open.

The [SHED panel adaptation by financial-condition path layer](shed-panel-adaptation-condition-path-layer-v1.md)
adds a conditional persistence comparison: prior adaptations are more likely to
persist on a worsening financial-condition path than on an improving path, with
borrowing, reduced use, saving cuts, and delayed purchases kept separate. This
is descriptive population evidence, not a causal estimate.

The [SHED panel adaptation by health direction layer](shed-panel-adaptation-health-path-layer-v1.md)
tests whether those adaptations persist or newly appear across 2024→2025
self-rated-health paths. It shows why improved health cannot be treated as
complete financial recovery.

## Meaty end-to-end goal

Build a source-traceable account of how a financial condition becomes a lived consumer experience and then a shift in company behavior, household choices, institutional trust, and political demand.

For each bounded topic, follow the whole chain:

```text
US price, income, debt, fee, rate, or policy condition
  -> firm or lender pricing and access rule
  -> household choice, constraint, delay, or loss of a buffer
  -> change in consumption, health, housing, work, or family decision
  -> change in trust, status, identity, or sense of fairness
  -> response by regulators, courts, firms, media, parties, or voters
  -> distribution of income, risk, information, and bargaining power
  -> company, sector, financial, and political exposure
  -> finding, counterevidence, limits, and next test
```

The final account must distinguish a fee from a price, access from affordability, reported concern from observed behavior, correlation from cause, and a policy goal from its actual distributional result.

## First working hypothesis

Some consumer systems advertise one visible price while moving the real cost through fees, interest, data, reduced choice, or cross-subsidy. The burden may fall most on people with the fewest ways to avoid the system, while rewards or convenience flow to people with more liquidity and better access. This is a hypothesis to test, not the finding.

The [payment-system incidence finding](findings/us-household-financial-pressure-003.md)
now connects the NBER merchant/model layer to the separate Federal Reserve and
SHED household-pressure layers. It treats payment-system redistribution as a
mechanism and keeps modeled incidence, observed adaptation, and household
welfare as distinct stages.

The [card-offer surface finding](findings/us-household-financial-pressure-004.md)
adds the CFPB 2024–2025 Terms of Credit Card Plans comparison. It shows why a
larger visible product surface and lower product-level median APR do not prove
cheaper realized credit, broader practical access, or better household
financial room.

## Scope

### In scope

- US households and consumers, with subgroup and place differences;
- payment methods, credit access, fees, rewards, overdrafts, and buy-now-pay-later;
- prices, income, debt service, savings, and financial stress;
- firm revenue models, merchant pass-through, lender screening, and risk transfer;
- consumer protection, competition, financial regulation, courts, and enforcement;
- social meaning: fairness, dignity, trust, security, dependence, and political response.

### Out of scope for the first release

- predicting elections or consumer markets;
- claiming that a single fee explains broad political behavior;
- treating company marketing as independent evidence;
- generalizing from one product, income group, or period without a comparison;
- making a moral judgment where the distribution and mechanism have not been measured.

## Required maps

| Map | Questions |
|---|---|
| Material | What happens to prices, balances, income, debt service, savings, and consumption? |
| Social | Who delays, goes without, asks family for help, changes status behavior, or loses trust? |
| Institution | Which firms, lenders, regulators, courts, and lawmakers set or change the terms? |
| Power | Who has choice, information, bargaining power, exit, and the ability to wait? |

## Evidence plan

1. Start with HBS and NBER to identify the mechanism and underlying study.
2. Check Federal Reserve household data, BLS prices and spending measures, BEA accounts, and Census household data.
3. Check CFPB complaints, market reports, enforcement records, rulemakings, and consumer education material.
4. Check bank, card-network, retailer, lender, and platform filings for the business model and disclosed risks.
5. Check surveys such as Pew, SHED, GSS, and ANES to test attitudes and reported experience; preserve wording and field dates.
6. Check court records, state enforcement, FTC/DOJ actions, and congressional or GAO material to test how rules work in practice.
7. Use BIS, IMF, OFR, World Bank, and other international sources only when they explain a US financial or geopolitical constraint or supply a useful comparator.
8. Write one plain-language finding in Markdown, then a matching HTML page. No slogans, no inflated language, and no causal claim that the evidence cannot carry.

## First deliverables

- dated source search record;
- source records with method, population, geography, period, and limits;
- claims ledger;
- payment-and-access mechanism map;
- subgroup and place comparison;
- company and sector bridge;
- political and institutional bridge;
- counterevidence record;
- one plain-language Markdown finding and matching HTML page;
- open gaps and a next test.

## Completion rule

The project is not complete when it has many sources. It is complete for one bounded question when the central mechanism is supported by at least two independent source families, a serious challenge has been tested, distribution is visible, and every important sentence is either directly sourced, clearly labeled as inference, or left as an open question.
The [aggregate-credit comparison](findings/us-household-financial-pressure-005.md)
now places the New York Fed 2026 Q2 household-debt snapshot beside the
Federal Reserve 2025 SHED household and linked-credit layers. It keeps
aggregate balances, survey capacity, and hardship-conditioned balance growth
as separate units and leaves the dated borrower-to-payment-to-trust path open.

The [SIPP utility-credit-savings finding](findings/us-household-financial-pressure-006.md)
adds a same-month person-record joint diagnostic: utility-payment difficulty
coexists with more balance carrying and less savings-account ownership, while
the resource-stratified cells show that credit access is not a simple
deprivation scale. Fay-BRR precision and household-level temporal ordering
remain the next gates.

The [BEA July 2026 income-and-outlays finding](findings/us-household-financial-pressure-007.md)
adds a current aggregate macro benchmark for personal income, disposable
income, consumption, services-versus-goods composition, outlays, and saving.
It keeps national accounts separate from household buffers, SIPP person-month
records, and New York Fed credit aggregates; it does not treat rising income
or PCE as evidence of equal household room.

The [August 2026 CPI finding](findings/us-household-financial-pressure-008.md)
adds the adjacent official price checkpoint: all-items CPI rose 0.4% in the
month and 3.4% over the year, with gasoline and energy contributing materially
to the movement. The CPI provides a dated aggregate price surface, not
household incidence, affordability, substitution, hardship, or political
meaning. The next test is a valid household or matched-place exposure design
that connects category-specific prices to alternatives, response, and recovery.

The [August 2026 PPI finding](findings/us-household-financial-pressure-009.md)
adds the upstream seller-side layer: final demand rose 0.4% monthly and 5.4%
over the year, while energy, diesel, and intermediate-goods indexes moved more
sharply. PPI is a possible transmission surface, not evidence of consumer
pass-through, firm margin change, household burden, or political response. The
next test is a named product or sector with a traceable price, contract/margin,
customer, and recovery or exit path.

The [current macro cross-source synthesis](findings/us-household-financial-pressure-010.md)
puts August labor, August CPI, August PPI, and July BEA income/outlays beside
one another. It makes the calendar alignment useful as a conditioning surface
while preserving the missing joins among worker, firm, product, household,
trust, and political-action units.

The [SHED panel reproduction audit](shed-panel-reproduction-audit-2026-09-13.json)
was rechecked on 2026-09-14 against the locally retained official archives.
The adaptation-condition and health/care outputs reproduced their prior hashes
and all 4,419 paired respondents. This confirms the descriptive panel layer;
it does not add replicate-weight uncertainty or causal identification.

The [panel work/health/care synthesis](findings/us-household-financial-pressure-011.md)
now places work-more, borrowing, reduced-use persistence beside health
direction and unpaid adult-care entry/exit. It strengthens the same-respondent
material-to-adaptation-to-care bridge while preserving the missing event,
hours, schedule-control, recipient-outcome, trust, and political-action links.

The reader-facing [financial-pressure, adaptation, and recovery synthesis](financial-pressure-adaptation-recovery-synthesis-v1.md)
connects the same-respondent persistence and re-entry tables to the
non-synchronized health and unpaid-care paths. It keeps the actual numbers,
conditional denominators, counterexamples, and public-use weight boundary
visible while explaining what the next dated event design must add.
