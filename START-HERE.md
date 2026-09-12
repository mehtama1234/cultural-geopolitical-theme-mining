# Start here

Open the [connected HTML reading guide](site/us-theme-atlas.html) or its [Markdown edition](analysis/us-theme-atlas.md). Each topic has subthemes, sources, limits and explained connections. The editable relationship record is [us-theme-connections.json](manifests/us-theme-connections.json); rebuild both editions with `python3 scripts/build_us_theme_atlas.py`, then validate them with `python3 scripts/validate_us_theme_atlas.py`.

The [US source coverage index](site/us-source-coverage.html) shows the current project packets, recorded sources and open gaps. Rebuild it with `python3 scripts/build_us_source_coverage.py`.

The [US evidence and map audit](site/us-evidence-audit.html) shows which topics have a specific evidence check, how many semantic links and reading paths reach each topic, and where the record is still opening-only.

The [big-picture synthesis](site/us-big-picture-synthesis.html) pulls the five themes together and shows which links are supported, which are comparisons, and which still need a stronger test.

The [matched-evidence index](site/us-matched-evidence.html) collects the deeper checks completed after the opening source packets and shows the open link in each one.

The first complete connected memo is [When household protection becomes a public feeling](site/us-household-cost-path-001.html), with its [Markdown record](analysis/findings/us-household-cost-path-001.md). It joins three source-backed observations while keeping the missing same-household evidence visible.

The second is [When faster service and longer use point in different directions](site/us-work-service-attention-path-001.html), with its [Markdown record](analysis/findings/us-work-service-attention-path-001.md). It joins worker AI access, customer resolution and the ability to leave while keeping the separate-study limit visible.

The third is [When health costs move into family time](site/us-health-care-time-path-001.html), with its [Markdown record](analysis/findings/us-health-care-time-path-001.md). It joins unpaid care, paid work and medical debt while keeping the different-study boundary visible.

The next short project is [US household energy burden](analysis/projects/us-energy-household-burden/README.md), with its [source search record](analysis/projects/us-energy-household-burden/source-search-2026-09-11.md). It joins energy bills, housing conditions and room for other household costs.

The fourth connected memo is [The cost of staying in a home is a stack of bills and risks](site/us-home-cost-stack-001.html), with its [Markdown record](analysis/findings/us-home-cost-stack-001.md). It joins energy burden, reported energy insecurity, homeowners insurance and home value while keeping the same-household gap visible.

## The question

What forces are changing how people in the United States live, spend, work, borrow, vote, and trust institutions—and how do those changes affect firms, finance, and state power?

Do not begin with a grand theory. Begin with a narrow question that can be checked.

The center of gravity is US customer, consumer, societal, financial, and political life. HBS, NBER, and international sources help us find and test the mechanisms; they do not automatically make the project global in scope.

Examples:

- When does a new tool change who has bargaining power at work?
- When does a cost shift from a company to a household?
- When does a local labor shortage change migration, family life, and politics?
- When does a supply-chain change become a security problem?
- When does a change in trust alter markets before it changes elections?
- When does a price, credit, housing, or service shock become a political identity or voting issue?
- When does a firm's growth model depend on households carrying more risk?
- When does financial stress change family decisions before it appears in national statistics?

## The work loop

1. Choose one topic from the queue.
2. Collect the HBS story and the underlying study when available.
3. Search NBER by topic, program, paper metadata, and data source.
4. Add outside evidence only when it tests, extends, or challenges the first sources.
5. Record each source in the evidence ledger before writing a conclusion.
6. Turn each supported claim into a short finding card.
7. Link findings into a cultural, social, institutional, and geopolitical theme map.
8. Write a plain-language memo in Markdown.
9. Publish the same memo as HTML with source links and an evidence table.
10. Recheck the finding after new data, a later paper, or a strong counterexample.

## The standard for a finding

A finding must answer:

- What changed?
- How do we know?
- What is the step between the evidence and the claim?
- Who is affected first?
- Who adapts next?
- What larger institution or power relation changes?
- What is fact, what is inference, and what is still unknown?
- What evidence would weaken or reverse the finding?

## First project

Begin with **AI adoption, work, and the new middle layer of control**. This connects current HBS material on AI adoption and careers with NBER work on labor markets, productivity, firms, inequality, and technology. Do not assume AI is the cause. Test whether the real change is in task control, measurement, worker bargaining power, training, or ownership of the workflow.

The initial project brief is [analysis/projects/ai-work-control/README.md](analysis/projects/ai-work-control/README.md).

## Next major project direction

Build a US-centered evidence system for the links among customer behavior, household security, firm strategy, financial conditions, public policy, and political response. Start with bounded topics, then follow each one from measured condition to lived effect to institutional and power change. The handoff is [analysis/US-CENTERED-RESEARCH-HANDOFF_V1.md](analysis/US-CENTERED-RESEARCH-HANDOFF_V1.md).

The first new project is [US household financial pressure and the price of access](analysis/projects/us-household-financial-pressure/README.md), with its opening [source search record](analysis/projects/us-household-financial-pressure/source-search-2026-09-11.md).

The next short pass is [US housing, insurance, and the cost of staying put](analysis/projects/us-housing-insurance-risk/README.md), with its [source search record](analysis/projects/us-housing-insurance-risk/source-search-2026-09-11.md).

The following short pass is [US health costs and the choices people give up](analysis/projects/us-health-cost-household-choice/README.md), with its [source search record](analysis/projects/us-health-cost-household-choice/source-search-2026-09-11.md).

The next short pass is [US cost of living, trust, and political response](analysis/projects/us-cost-trust-politics/README.md), with its [source search record](analysis/projects/us-cost-trust-politics/source-search-2026-09-11.md).

The following short pass is [US aging, care, and the hidden second job](analysis/projects/us-aging-care-strain/README.md), with its [source search record](analysis/projects/us-aging-care-strain/source-search-2026-09-11.md).

The next short pass is [US local business and the changing hometown](analysis/projects/us-local-business-place/README.md), with its [source search record](analysis/projects/us-local-business-place/source-search-2026-09-11.md).

The following short pass is [US customer service, automation, and the right to reach a person](analysis/projects/us-customer-automation-recourse/README.md), with its [source search record](analysis/projects/us-customer-automation-recourse/source-search-2026-09-11.md).

The next short pass is [US digital habits, attention, and the need to leave](analysis/projects/us-digital-habits-attention/README.md), with its [source search record](analysis/projects/us-digital-habits-attention/source-search-2026-09-11.md).

The next short pass is [US habit change and the cost of being seen getting help](analysis/projects/us-habit-change-social-judgment/README.md), with its [source search record](analysis/projects/us-habit-change-social-judgment/source-search-2026-09-11.md). It tests whether social judgment makes a useful aid feel costly to use.

The next short pass is [US subscriptions and the cost of not noticing](analysis/projects/us-subscription-inattention/README.md), with its [source search record](analysis/projects/us-subscription-inattention/source-search-2026-09-11.md). It tests when automatic renewal turns lost attention into a recurring household cost.

The next short pass is [US public aid and the shape of a dollar](analysis/projects/us-transfer-design-household-spending/README.md), with its [source search record](analysis/projects/us-transfer-design-household-spending/source-search-2026-09-11.md). It tests whether cash, food, one-time and monthly aid lead to different household choices.

The next short pass is [US inflation and the price people feel](analysis/projects/us-inflation-price-perception/README.md), with its [source search record](analysis/projects/us-inflation-price-perception/source-search-2026-09-11.md). It tests why a slower rise in prices can still feel like a continuing loss.

The next short pass is [US tariffs and the price that arrives later](analysis/projects/us-tariff-price-pass-through/README.md), with its [source search record](analysis/projects/us-tariff-price-pass-through/source-search-2026-09-11.md). It tests how trade policy becomes a delayed household price.

The next short pass is [US multiple jobs and the cost of flexibility](analysis/projects/us-multiple-job-spending-strain/README.md), with its [source search record](analysis/projects/us-multiple-job-spending-strain/source-search-2026-09-11.md). It tests what equal income fails to show when work comes through several jobs.

The next short pass is [US bank customers and the cost of staying put](analysis/projects/us-bank-depositor-inertia/README.md), with its [source search record](analysis/projects/us-bank-depositor-inertia/source-search-2026-09-11.md). It tests when convenience and switching effort move value from depositors to banks.

The next short pass is [US privacy rules and the decision to share](analysis/projects/us-privacy-trust-data-sharing/README.md), with its [source search record](analysis/projects/us-privacy-trust-data-sharing/source-search-2026-09-11.md). It tests whether privacy protection can increase trust and data sharing at the same time.

The next short pass is [US real wages and the vote](analysis/projects/us-economic-voting-real-wages/README.md), with its [source search record](analysis/projects/us-economic-voting-real-wages/source-search-2026-09-11.md). It tests whether voters respond more to lost buying power than to inflation alone.

The next short pass is [US hometown business and the loss of local ownership](analysis/projects/us-hometown-entrepreneurship-decline/README.md), with its [source search record](analysis/projects/us-hometown-entrepreneurship-decline/source-search-2026-09-11.md). It tests what changes when would-be business owners leave home more often.

The next short pass is [US households and the meaning of an interest-rate change](analysis/projects/us-household-monetary-policy/README.md), with its [source search record](analysis/projects/us-household-monetary-policy/source-search-2026-09-11.md). It tests how rate decisions become household beliefs about prices, borrowing and saving.

The next short pass is [US older consumers are not one market](analysis/projects/us-older-consumer-segments/README.md), with its [source search record](analysis/projects/us-older-consumer-segments/source-search-2026-09-11.md). It tests what age-based marketing misses about health, independence, buying power and care.

The next short pass is [US AI emotional support and the private care gap](analysis/projects/us-ai-emotional-support-apps/README.md), with its [source search record](analysis/projects/us-ai-emotional-support-apps/source-search-2026-09-11.md). It tests when private AI support helps, holds attention or fails to reach human care.

The next short pass is [US vehicle repair as a household shock](analysis/projects/us-vehicle-repair-household-shock/README.md), with its [source search record](analysis/projects/us-vehicle-repair-household-shock/source-search-2026-09-11.md). It tests what a household gives up to keep moving when a repair arrives before the next paycheck.

The next short pass is [US family support as a hidden safety net](analysis/projects/us-family-support-hidden-safety-net/README.md), with its [source search record](analysis/projects/us-family-support-hidden-safety-net/source-search-2026-09-11.md). It tests who catches a household shock with money or unpaid care, and what the helper gives up.

The next short pass is [US owner households and the business tradeoff](analysis/projects/us-owner-household-business-tradeoff/README.md), with its [source search record](analysis/projects/us-owner-household-business-tradeoff/source-search-2026-09-11.md). It tests which side gets protected when a small business and its household share one cash pool.

The next short pass is [US benefit loss and the work choice](analysis/projects/us-benefit-cliff-work-choice/README.md), with its [source search record](analysis/projects/us-benefit-cliff-work-choice/source-search-2026-09-11.md). It tests what remains after a raise and the public help it may replace are counted together.

The next short pass is [US utility shutoff and bill timing](analysis/projects/us-utility-shutoff-bill-timing/README.md), with its [source search record](analysis/projects/us-utility-shutoff-bill-timing/source-search-2026-09-11.md). It tests whether the gap between income and the due date becomes a service, credit or health problem.

The next short pass is [US health coverage and staying in a job](analysis/projects/us-health-insurance-job-lock/README.md), with its [source search record](analysis/projects/us-health-insurance-job-lock/source-search-2026-09-11.md). It tests whether employer coverage changes the cost of leaving, retraining or starting something new.

The next short pass is [US medical debt relief and what it changes](analysis/projects/us-medical-debt-relief-outcomes/README.md), with its [source search record](analysis/projects/us-medical-debt-relief-outcomes/source-search-2026-09-11.md). It tests whether removing medical debt changes credit, care, health or only the record.

The next short pass is [US cash aid and household structure](analysis/projects/us-cash-aid-household-structure/README.md), with its [source search record](analysis/projects/us-cash-aid-household-structure/source-search-2026-09-11.md). It tests whether regular cash changes housing payments, crowding or who can live independently.

The next short pass is [US cash policy and public mood](analysis/projects/us-policy-sentiment-cash-benefit/README.md), with its [source search record](analysis/projects/us-policy-sentiment-cash-benefit/source-search-2026-09-11.md). It tests whether a lost benefit changes how families judge the economy before it can be tied to trust or voting.

The next short pass is [US income volatility and the room to spend](analysis/projects/us-income-volatility-spending-risk/README.md), with its [source search record](analysis/projects/us-income-volatility-spending-risk/source-search-2026-09-11.md). It tests what unpredictable pay changes that an average wage measure misses.

The next short pass is [US durable purchases and borrowed room](analysis/projects/us-durable-purchase-financing/README.md), with its [source search record](analysis/projects/us-durable-purchase-financing/source-search-2026-09-11.md). It tests whether a one-time payment protects daily access or becomes a longer monthly obligation.

The next short pass is [US guaranteed income and household dynamics](analysis/projects/us-guaranteed-income-household-dynamics/README.md), with its [source search record](analysis/projects/us-guaranteed-income-household-dynamics/source-search-2026-09-11.md). It tests what changes inside a household when only one person receives regular cash.

The next short pass is [US immigration, local demand and place](analysis/projects/us-immigration-local-demand/README.md), with its [source search record](analysis/projects/us-immigration-local-demand/source-search-2026-09-11.md). It tests how new residents change local customers, jobs, housing, services and belonging.

The next short pass is [US hidden fees and the price people can compare](analysis/projects/us-hidden-fees-price-salience/README.md), with its [source search record](analysis/projects/us-hidden-fees-price-salience/source-search-2026-09-11.md). It tests whether a low first price changes what people buy and what they finally pay.

The next short pass is [US payment fees and who pays](analysis/projects/us-payment-fee-redistribution/README.md), with its [source search record](analysis/projects/us-payment-fee-redistribution/source-search-2026-09-11.md). It tests whether card rewards and merchant fees move money between shoppers through common prices.

The next short pass is [US credit records and financial visibility](analysis/projects/us-credit-record-visibility/README.md), with its [source search record](analysis/projects/us-credit-record-visibility/source-search-2026-09-11.md). It tests how a payment record becomes a gate to credit, housing or a bank account.

The next short pass is [US eviction as a household cascade](analysis/projects/us-eviction-cascade/README.md), with its [source search record](analysis/projects/us-eviction-cascade/source-search-2026-09-11.md). It tests what an eviction order changes beyond the loss of a home.

The next short pass is [US housing-court legal help](analysis/projects/us-housing-court-legal-help/README.md), with its [source search record](analysis/projects/us-housing-court-legal-help/source-search-2026-09-11.md). It tests whether a person with legal knowledge can change the housing path before a court order becomes a wider household loss.

The next short pass is [US rental assistance and eviction prevention](analysis/projects/us-rental-assistance-eviction-prevention/README.md), with its [source search record](analysis/projects/us-rental-assistance-eviction-prevention/source-search-2026-09-11.md). It tests whether rent aid prevents displacement or mainly buys time when the rent problem remains.

The next short pass is [US emergency assistance and the work path](analysis/projects/us-emergency-assistance-work-path/README.md), with its [source search record](analysis/projects/us-emergency-assistance-work-path/source-search-2026-09-11.md). It tests whether preventing a housing break protects work and later earnings.

The next short pass is [US rent-guarantee insurance](analysis/projects/us-rent-guarantee-insurance/README.md), with its [source search record](analysis/projects/us-rent-guarantee-insurance/source-search-2026-09-11.md). It tests whether rent protection can share a short shock before it becomes arrears, court or lost housing.

The next short pass is [US home insurance affordability](analysis/projects/us-home-insurance-affordability/README.md), with its [source search record](analysis/projects/us-home-insurance-affordability/source-search-2026-09-11.md). It tests when disaster risk and credit standing make the cost of keeping a home harder to carry.

The next short pass is [US remote work and shopping cost](analysis/projects/us-remote-work-shopping-cost/README.md), with its [source search record](analysis/projects/us-remote-work-shopping-cost/source-search-2026-09-11.md). It tests how moving work home changes shopping mode, prices, time and unpaid household work.

The next short pass is [US payment-system outage resilience](analysis/projects/us-payment-system-outage-resilience/README.md), with its [source search record](analysis/projects/us-payment-system-outage-resilience/source-search-2026-09-11.md). It tests what households can still buy when electricity or a payment network fails.

The next short pass is [US emergency credit after a disaster](analysis/projects/us-emergency-credit-disaster/README.md), with its [source search record](analysis/projects/us-emergency-credit-disaster/source-search-2026-09-11.md). It tests when timely borrowing protects a household from bankruptcy and when it creates a later payment burden.

The next short pass is [US small-business disaster liquidity](analysis/projects/us-small-business-disaster-liquidity/README.md), with its [source search record](analysis/projects/us-small-business-disaster-liquidity/source-search-2026-09-11.md). It tests whether recovery credit protects the owner's household, workers, customers and local services together.

The next short pass is [US small-business support and size rules](analysis/projects/us-small-business-support-size-cutoff/README.md), with its [source search record](analysis/projects/us-small-business-support-size-cutoff/source-search-2026-09-11.md). It tests whether broader eligibility shifts public support toward larger firms and away from the smallest ones.

The next short pass is [US student-loan policy uncertainty](analysis/projects/us-student-loan-policy-uncertainty/README.md), with its [source search record](analysis/projects/us-student-loan-policy-uncertainty/source-search-2026-09-11.md). It tests how a debt promise changes household payments and spending before the policy is settled.

The next short pass is [US trust in the Federal Reserve](analysis/projects/us-fed-partisan-trust/README.md), with its [source search record](analysis/projects/us-fed-partisan-trust/source-search-2026-09-11.md). It tests whether political identity changes how households hear an economic message.

The next short pass is [US inflation cause beliefs](analysis/projects/us-inflation-cause-beliefs/README.md), with its [source search record](analysis/projects/us-inflation-cause-beliefs/source-search-2026-09-11.md). It tests how a household price becomes a story about responsibility and political action.

The next short pass is [US news selection and inflation belief](analysis/projects/us-news-selection-inflation/README.md), with its [source search record](analysis/projects/us-news-selection-inflation/source-search-2026-09-11.md). It tests whether higher-price news shifts economic expectations more than lower-price news.

The next short pass is [US fiscal news and household choice](analysis/projects/us-fiscal-news-household/README.md), with its [source search record](analysis/projects/us-fiscal-news-household/source-search-2026-09-11.md). It tests whether future public debt changes today's household spending or political judgment.

The next short pass is [US safe drinking water](analysis/projects/us-safe-drinking-water/README.md), with its [source search record](analysis/projects/us-safe-drinking-water/source-search-2026-09-11.md). It tests whether public water quality sits underneath household health, private cost, home value and trust in a place.

The next short pass is [US bank fees and household room](analysis/projects/us-bank-fees-household-wellbeing/README.md), with its [source search record](analysis/projects/us-bank-fees-household-wellbeing/source-search-2026-09-11.md). It tests whether a bank rule creates real room for low-cash households or moves the shortage into another fee or credit product.

The next short pass is [US self-fulfilling credit scores](analysis/projects/us-self-fulfilling-credit-scores/README.md), with its [source search record](analysis/projects/us-self-fulfilling-credit-scores/source-search-2026-09-11.md). It tests whether a score can become a barrier that helps produce the default it forecasts.

The next short pass is [US Auto-IRA and household balance sheets](analysis/projects/us-auto-ira-household-balance-sheets/README.md), with its [source search record](analysis/projects/us-auto-ira-household-balance-sheets/source-search-2026-09-11.md). It tests whether automatic workplace saving creates a real buffer or shifts short-term pressure into credit-card debt.

The next short pass is [US low-liquidity consumption constraints](analysis/projects/us-low-liquidity-consumption-constraints/README.md), with its [source search record](analysis/projects/us-low-liquidity-consumption-constraints/source-search-2026-09-11.md). It tests whether visible spending reflects preference, cash limits, credit limits or the cost of changing a plan.

The next short pass is [US rising income risk at the top](analysis/projects/us-rising-income-risk-top/README.md), with its [source search record](analysis/projects/us-rising-income-risk-top/source-search-2026-09-11.md). It tests whether higher saving among high earners changes wealth gaps and the wider price of money.

The next short pass is [US employer political influence](analysis/projects/us-employer-political-influence/README.md), with its [source search record](analysis/projects/us-employer-political-influence/source-search-2026-09-11.md). It tests whether a dominant local employer can carry job dependence into political belief and voting.

The next short pass is [US local prices and consumption geography](analysis/projects/us-local-prices-consumption-geography/README.md), with its [source search record](analysis/projects/us-local-prices-consumption-geography/source-search-2026-09-11.md). It tests whether the same income buys a different life by place, especially for lower-income households.

The next short pass is [US Child Tax Credit and economic sentiment](analysis/projects/us-child-tax-credit-sentiment/README.md), with its [source search record](analysis/projects/us-child-tax-credit-sentiment/source-search-2026-09-11.md). It tests whether public help changes how families judge their own economy and government beyond the direct income change.

The next short pass is [US environmental policy cost beliefs](analysis/projects/us-environmental-policy-cost-beliefs/README.md), with its [source search record](analysis/projects/us-environmental-policy-cost-beliefs/source-search-2026-09-11.md). It tests whether beliefs about the household energy bill steer which environmental policy wins.

The next short pass is [US rideshare price search](analysis/projects/us-rideshare-price-search-friction/README.md), with its [source search record](analysis/projects/us-rideshare-price-search-friction/source-search-2026-09-11.md). It tests whether app convenience leaves customers with less price power even when two platforms compete.

The next short pass is [US rideshare licensing and customer safety](analysis/projects/us-rideshare-licensing-customer-safety/README.md), with its [source search record](analysis/projects/us-rideshare-licensing-customer-safety/source-search-2026-09-11.md). It tests whether licensing improves the ride customers receive or mainly changes who can enter the work.

The next short pass is [US platform data neutrality](analysis/projects/us-platform-data-neutrality/README.md), with its [source search record](analysis/projects/us-platform-data-neutrality/source-search-2026-09-11.md). It tests whether equal data access opens customer competition or weakens the platform's reason to improve the data.

The next short pass is [US time-intensive platform consumption](analysis/projects/us-time-intensive-platform-consumption/README.md), with its [source search record](analysis/projects/us-time-intensive-platform-consumption/source-search-2026-09-11.md). It tests what a free service costs in time and attention, and how that changes customer benefit and competition.

The next short pass is [US tariff price paths and delayed domestic markups](analysis/projects/us-tariff-domestic-markup-delay/README.md), with its [source search record](analysis/projects/us-tariff-domestic-markup-delay/source-search-2026-09-11.md). It tests why the consumer price effect of a tariff can keep growing after the first import-price change.

The next short pass is [US consumer discrimination and competition](analysis/projects/us-consumer-discrimination-competition/README.md), with its [source search record](analysis/projects/us-consumer-discrimination-competition/source-search-2026-09-11.md). It tests whether competition protects all customers equally when groups have different power to switch.

The next short pass is [US platform-owned products and customer choice](analysis/projects/us-platform-owned-products-choice/README.md), with its [source search record](analysis/projects/us-platform-owned-products-choice/source-search-2026-09-11.md). It tests whether a platform's own products help customers while its control over search raises a longer-run competition question.

The next short pass is [US online reviews and customer trust](analysis/projects/us-online-reviews-trust/README.md), with its [source search record](analysis/projects/us-online-reviews-trust/source-search-2026-09-11.md). It tests whether reviews help customers compare quality or become another paid and controlled gate.

The next short pass is [US consumer credit and the shrinking cash buffer](analysis/projects/us-consumer-credit-liquidity/README.md), with its [source search record](analysis/projects/us-consumer-credit-liquidity/source-search-2026-09-11.md). It tests whether credit is a bridge after a household bill or a later loss of room.

The fifth connected memo is [When credit makes a shock smaller now and larger later](site/us-credit-buffer-path-001.html), with its [Markdown record](analysis/findings/us-credit-buffer-path-001.md). It joins household cash buffers, BNPL payment timing, product fees and wider debt conditions while keeping the different measurement units visible.

The next short project is [US food, the household budget, and basic security](analysis/projects/us-food-budget-security/README.md), with its [source search record](analysis/projects/us-food-budget-security/source-search-2026-09-11.md). It tests whether financial pressure reaches food before it appears as a missed debt payment or skipped care.

The sixth connected memo is [When the budget reaches the dinner table](site/us-food-budget-path-001.html), with its [Markdown record](analysis/findings/us-food-budget-path-001.md). It joins USDA food security, Fed income differences, family exposure and skipped medical care while keeping the different time windows visible.

The next short project is [US safety-net access, work rules, and the price of help](analysis/projects/us-safety-net-access/README.md), with its [source search record](analysis/projects/us-safety-net-access/source-search-2026-09-11.md). It tests whether rules and access barriers remove food support without increasing work.

The seventh connected memo is [When help disappears before the need does](site/us-safety-net-access-path-001.html), with its [Markdown record](analysis/findings/us-safety-net-access-path-001.md). It joins SNAP participation, work requirements and office access while keeping program exit separate from employment.

The next short project is [US childcare, work, and the price of family time](analysis/projects/us-childcare-work-cost/README.md), with its [source search record](analysis/projects/us-childcare-work-cost/source-search-2026-09-11.md). It tests whether households pay for care with cash, unpaid family hours or paid work time.

The eighth connected memo is [When family care becomes paid-work time](site/us-childcare-work-path-001.html), with its [Markdown record](analysis/findings/us-childcare-work-path-001.md). It joins childcare cost, unpaid relative care and reported work loss while keeping support separate from burden.

The next short project is [US transportation, household cost, and access](analysis/projects/us-transportation-household-access/README.md), with its [source search record](analysis/projects/us-transportation-household-access/source-search-2026-09-11.md). It tests whether getting to work, food, care and services is a hidden part of household energy and housing cost.

The ninth connected memo is [When the trip is part of the price](site/us-transportation-access-path-001.html), with its [Markdown record](analysis/findings/us-transportation-access-path-001.md). It joins transportation spending, vehicle insurance, commute time and the value of place while keeping the benefit of access visible.

The next short project is [US consumer fraud, recovery, and trust](analysis/projects/us-consumer-fraud-trust/README.md), with its [source search record](analysis/projects/us-consumer-fraud-trust/source-search-2026-09-11.md). It tests who carries a loss and whether a usable recovery path shapes trust.

The tenth connected memo is [When a trusted service becomes a dispute](site/us-consumer-fraud-trust-path-001.html), with its [Markdown record](analysis/findings/us-consumer-fraud-trust-path-001.md). It separates scam attempts, reported losses, unrecovered losses and the still-unproven trust response.

The next short project is [US student debt and adult life choices](analysis/projects/us-student-debt-life-choices/README.md), with its [source search record](analysis/projects/us-student-debt-life-choices/source-search-2026-09-11.md). It tests whether education debt becomes a payment, housing, work or family-choice constraint, and keeps balance measures separate from lived outcomes.

The eleventh connected memo is [When education debt follows the first job](site/us-student-debt-life-choices-path-001.html), with its [Markdown record](analysis/findings/us-student-debt-life-choices-path-001.md). It joins borrower payment trouble, credit-record delinquency and a possible life-choice mechanism without treating the links as proven for every borrower.

The twelfth connected memo is [When household choices become a judgment about the country](site/us-cost-trust-politics-path-001.html), with its [Markdown record](analysis/findings/us-cost-trust-politics-path-001.md). It joins price actions, personal and national economic views, and public trust while keeping party identity and voting effects open.

The thirteenth connected memo is [When family care becomes a work decision](site/us-aging-care-work-path-001.html), with its [Markdown record](analysis/findings/us-aging-care-work-path-001.md). It joins unpaid eldercare, paid work and household scheduling while keeping the direction of the work effect open.

The fourteenth connected memo is [When a business idea leaves home](site/us-local-business-place-path-001.html), with its [Markdown record](analysis/findings/us-local-business-place-path-001.md). It joins founder movement, housing and local business counts while keeping lasting jobs, services and belonging as open tests.

The fifteenth connected memo is [When the energy bill begins with the home](site/us-energy-household-burden-path-001.html), with its [Markdown record](analysis/findings/us-energy-household-burden-path-001.md). It joins energy burden, renter control, housing risk and the possible use of credit while keeping the later household tradeoff open.

The sixteenth connected memo is [When a faster answer still leaves the case open](site/us-customer-service-recourse-path-001.html), with its [Markdown record](analysis/findings/us-customer-service-recourse-path-001.md). It joins worker AI support, repeat complaints and the customer's ability to obtain a remedy.

The next short project is [US workplace communication and the price of fitting in](analysis/projects/us-workplace-communication-fit/README.md), with its [source search record](analysis/projects/us-workplace-communication-fit/source-search-2026-09-11.md). It tests whether familiar speech is read as skill and changes access to people-facing work.

The next short project is [US career progression and the mid-level plateau](analysis/projects/us-career-progression-plateau/README.md), with its [source search record](analysis/projects/us-career-progression-plateau/source-search-2026-09-11.md). It tests whether years on the job translate into real movement and what a slow path may leave harder around debt and housing.

The next short project is [US employee ownership and the meaning of the work](analysis/projects/us-employee-ownership-meaning/README.md), with its [source search record](analysis/projects/us-employee-ownership-meaning/source-search-2026-09-11.md). It tests whether a financial claim changes worker retention and household wealth, or mainly changes the message around the job.

The next short project is [US remote work and the value of coming together](analysis/projects/us-remote-work-contact/README.md), with its [source search record](analysis/projects/us-remote-work-contact/source-search-2026-09-11.md). It tests whether a small shared office day changes later communication and retention, and who carries the travel cost.

The seventeenth connected memo is [When ownership means more than a promise](site/us-employee-ownership-meaning-path-001.html), with its [Markdown record](analysis/findings/us-employee-ownership-meaning-path-001.md). It tests whether a worker's financial claim becomes household wealth or only a reason to stay.
