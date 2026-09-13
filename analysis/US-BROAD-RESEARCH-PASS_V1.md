# US broad research pass v1

## Purpose

This is the execution queue for the broader societal, cultural, consumer, financial, institutional, and political program. It is not a one-household study. The household calendar is one possible longitudinal instrument; the main work compares populations, places, customers, workers, firms, markets, agencies, and political measures across source families.

Use the [US broad evidence matrix](US-BROAD-EVIDENCE-MATRIX_V1.md) to assign each arrow to a source, unit, and next test before adding another topic packet.

The [provisional societal trend register](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) is the current synthesis layer. It names recurring patterns across the source packets while keeping each missing join and next test visible.

The cross-source [trust, meaning, and action layer](projects/us-cost-trust-politics/cross-source-trust-action-layer-v1.md)
is the current broad societal connector. It keeps material condition,
attribution, trust, identity, consumer response, civic response, and
institutional response as separate measurements, then identifies the missing
same-respondent or same-case test between them. This preserves the program’s
actual objective: explaining how conditions across households, consumers,
workers, firms, institutions, places, and infrastructure become cultural and
political patterns.

The [capability, dependency, local distribution, and state power layer](projects/ai-work-control/capability-dependence-local-power-layer-v1.md)
extends the program outward to infrastructure and geopolitical consequences.
It treats AI and cloud capacity as a stack of physical, financial, technical,
and institutional complements, then asks who owns them, who pays, who benefits,
and who can switch or inspect. Project announcements remain inputs to the
test, not evidence of realized local capability or sovereignty.

The [care cost, work, family time, and security layer](projects/us-health-cost-household-choice/care-cost-work-family-security-layer-v1.md)
adds social reproduction as a population-level theme. It keeps the medical
bill, payment trouble, credit record, delayed care, paid care, unpaid family
time, work loss, food or housing tradeoff, health, and job freedom separate.
Its next test follows one dated event through the same person or family rather
than treating an annual hardship measure as a complete causal story.

The [place risk, housing security, mobility, and local life layer](projects/us-housing-insurance-affordability/place-risk-mobility-local-life-layer-v1.md)
adds the place-level connection across insurance, housing, energy, transport,
local business, services, and political meaning. It distinguishes occupancy
from secure staying, vehicle access from successful access, business
applications from durable local capacity, and investment from local control.

The [optionality, unequal exposure, time, and exit layer](projects/us-household-calendar-integration/optionality-inequality-time-exit-layer-v1.md)
is the distributional spine across the other themes. It treats cash, time,
alternatives, social support, rights, institutional voice, and practical exit
as separate resources. The next tests must show not only who is exposed, but
who can absorb, refuse, appeal, switch, move, or organize.

The [consumer culture, trust, status, and everyday power layer](projects/us-consumer-culture/consumer-culture-trust-status-layer-v1.md)
adds the cultural/consumer mechanism. It follows how purchase, search, data
sharing, help-seeking, reviews, fraud reporting, and switching become signals
about trust, dignity, status, fairness, and dependence. Use and trust are not
treated as satisfaction or control; the next test follows a customer through
entry, outcome, remedy, and exit while including non-users and non-reporters.

The [public administration, take-up, security, and political feedback layer](projects/us-safety-net-access/public-administration-takeup-security-trust-action-layer-v1.md)
deepens the public-systems bridge. It treats notice, route, documents, timing,
appeal, interruption, and exit as part of the policy—not administrative noise.
It keeps eligibility, receipt, food security, work, debt, health, trust, and
political action separate and specifies the same-episode event-ledger test.

The [SIPP SNAP transition Fay-BRR uncertainty layer](projects/us-safety-net-access/sipp-snap-transition-fay-brr-layer-v1.md)
adds replicate-weight standard errors and intervals to the monthly transition
distribution. It is a statistical-depth improvement to the public-systems
layer, not evidence that a transition was caused by a rule or improved a
household’s security.

The [SIPP SNAP transition context Fay-BRR layer](projects/us-safety-net-access/sipp-snap-transition-context-fay-brr-layer-v1.md)
extends that uncertainty check to resource and job changes around entry and
exit. It provides a sharper descriptive test of the claim that exit is not
automatically improved circumstances, while preserving missingness and the
absence of a same-episode causal design.

The [migration, local demand, housing, services, and belonging layer](projects/us-immigration-local-demand/migration-demand-housing-services-belonging-layer-v1.md)
adds the population-change and place mechanism. It separates workers,
customers, jobs, firms, rents, public capacity, local ownership, belonging, and
political response. The next test compares matched places with different
housing and service responses instead of treating migration as one effect.

The [credit, liquidity, financial records, and institutional power layer](projects/us-financial-intermediation/credit-liquidity-records-power-layer-v1.md)
adds the financial-institution mechanism. It treats liquidity, payment rails,
bank inertia, fees, credit records, debt, switching, and later access as
separate outcomes. The next test follows one dated financial event through
remedy, future terms, household security, trust, and exit.

The reusable [broad end-to-end event ledger](templates/US-BROAD-EVENT-LEDGER_V1.md)
now provides one schema for the next empirical passes. It can hold a consumer,
care, housing, work, benefit, firm, place, or infrastructure event while
keeping unit changes and arrow-level evidence visible. The safety-net and
household-calendar ledgers remain specialized versions rather than definitions
of the whole program.

The schema and simulated fixture are checked by
`scripts/validate_us_broad_event_ledger_fixture.py`; the fixture is explicitly
marked as test data and must never be cited as a finding.

## Governing question

When a US condition, price, rule, technology, or institutional decision changes people’s available choices, how does that change travel through consumer behavior, household security, culture, firm strategy, institutional response, and political judgment—and where does power or risk move?

## Five priority bridges

These are the first execution bridges, not the whole theme inventory. They
organize the next evidence passes across the broader 14-theme program in the
[recovery brief](../END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md).

| Priority | Bridge to test | Source families already present | First measurable unit | Main missing link |
|---|---|---|---|---|
| 1 | **Price/payment → choice → household room** | SIPP, CE, CPS, SHED, BLS, NBER | household-month, consumer unit, product basket, or payment event | The same person’s exact price, sacrifice, debt, and recovery |
| 2 | **Service/platform rule → recourse → trust and exit** | FTC, CFPB, platform studies, NBER, surveys, complaint records | customer contact, complaint, appeal, switch, or unresolved case | Whether faster service actually solves the problem and changes trust |
| 3 | **Work rule/tool → control → household and local power** | NBER, HBS, CPS, BLS, firm filings, local labor data | worker-task, job, workplace, or local labor market | Who receives the productivity gain and who controls the work process |
| 4 | **Housing/energy/insurance → health, mobility, and place** | RECS, FIO/Treasury, FEMA/NFIP, ACS, FHFA, HMDA, SHED, MEPS | housing unit, ZIP-year, household, or disaster event | Same-place linkage from risk or bill to repair, move, health, credit, or staying |
| 5 | **Public aid/rule → take-up → interpretation → political response** | SIPP, SHED, CPS-FSS, ANES/GSS, Fed, NBER, administrative records | person-month, program spell, survey wave, county, or election | The middle steps: burden, blame, belief, action, and durable response |

## First representative cases

These are starting cases from the existing matched-evidence and path records. They are not yet a claim that the five bridges have been proven end to end.

| Bridge | Starting case | Why it starts here | Immediate next comparison |
|---|---|---|---|
| Price/payment → household room | [Payment choice changes who carries the price](findings/us-payment-fee-matched-evidence-001.md) | It already separates merchant fee, posted price, reward, interest, protection, and household net cost. | Compare payment method, income, credit access, balance carried, and next essential purchase. |
| Service/platform rule → recourse → trust and exit | [A faster answer is not yet a remedy](findings/us-customer-automation-matched-evidence-001.md) | It distinguishes first-response speed from final resolution, customer effort, authority, abandonment, and trust. | Compare routine cases and exceptions by automation path, repeat contact, remedy, and exit. |
| Work rule/tool → control → household and local power | [Health coverage can hold a job in place](findings/us-health-insurance-job-lock-matched-evidence-001.md) | It gives a concrete worker-choice case where a benefit affects job mobility and household security. | Compare coverage dependence, job changes, wages, hours, health, and alternatives; add AI/control cases separately. |
| Housing/energy/insurance → health, mobility, and place | [Insurance can turn a place risk into a staying problem](findings/us-home-insurance-matched-evidence-001.md) | It connects place risk, premium, coverage, credit, home value, repair, sale, and staying without claiming a move. | Compare similar properties by risk, credit, coverage, repairs, claims, financing, and move outcome. |
| Public aid/rule → interpretation → political response | [A public benefit can change economic sentiment](findings/us-transfer-design-household-matched-evidence-001.md) plus [real wages and voting](findings/us-economic-voting-real-wages-matched-evidence-001.md) | Together they separate benefit exposure, household condition, sentiment, real wages, and election results. | Test burden, attribution, party identity, policy knowledge, action, and vote as separate links. |

The first bridge synthesis is now recorded in [price and payment to household room](bridges/us-price-payment-household-room-v1.md). It is deliberately a layered cross-source comparison, not a claim that one household or one price caused a later political result.

The second bridge synthesis is now recorded in [service and platform rules to recourse, trust, and exit](bridges/us-service-platform-recourse-trust-v1.md). It separates first-response speed, final remedy, customer effort, and trust.

The third bridge synthesis is now recorded in [work rules and tools to control, household security, and local power](bridges/us-work-control-household-power-v1.md). It separates output, worker control, usable security, and political voice.

The fourth bridge synthesis is now recorded in [housing, energy, and insurance to health, mobility, and place](bridges/us-housing-energy-insurance-place-v1.md). It separates affordability, protection, home condition, mobility, and recovery.

The fifth bridge synthesis is now recorded in [public aid and rules to interpretation and political response](bridges/us-public-aid-interpretation-political-response-v1.md). It separates exposure, take-up, material result, interpretation, political expression, and political action.

The first reusable population-level measurement attached to a bridge is the [2022 NHTS urban/rural transport comparison](projects/us-household-calendar-integration/nhts-transport-comparison-v1.md). It is a place-and-mobility layer for Bridge 4, not a full housing, energy, insurance, or household-recovery result.

The first 2025 SHED price-adaptation layer is now recorded in [the household financial-pressure project](projects/us-household-financial-pressure/shed-2025-price-adaptation-layer-v1.md). It adds weighted population comparisons of price worsening, substitution, reduced use, saving cuts, borrowing, delayed purchases, extra work, emergency capacity, and outside help. It deepens Bridge 1 and supplies a material exposure layer for Bridge 5, while the political interpretation and action links remain open.

The [ATUS 2024 time-hidden-price layer](projects/us-household-calendar-integration/atus-2024-time-hidden-price-layer-v1.md) now adds official population estimates for household labor, multiple-job weekend work, workplace location, primary childcare, secondary childcare, and socializing. It deepens the time, work-control, care, and cultural-participation themes without turning a one-day diary into a household panel.

The [Pew 2025 news, platform, and civic-engagement layer](projects/us-digital-habits-attention/pew-2025-news-civic-engagement-layer-v1.md) adds population-level information and cultural structure: distinct participation types, partisan news-source ecosystems, and social-media news influencers. It deepens the platforms, trust, identity, and collective-action themes without treating source use as proof of persuasion or causal voting effects.

The [USDA 2024 food-security layer](projects/us-food-budget-security/usda-2024-food-security-layer-v1.md) adds a basic-security endpoint to the price, care, public-assistance, and inequality themes. It shows the national distribution of low and very low food security, child/adult shielding, subgroup exposure, and assistance participation while keeping the exact price-to-food and food-to-political paths open.

The [local business formation and place layer](projects/us-local-business-place/local-business-formation-place-layer-v1.md) adds a firm, sector, and place layer. It separates entrepreneur movement, business applications, employer-firm formation, and local service or identity effects, keeping the business-count-to-community and domestic-capacity-to-state links open.

The first fresh bounded acquisition is the [SIPP 2025 acquisition](projects/us-household-calendar-integration/sipp-bounded-acquisition-v1.md). It confirms an accessible monthly population-survey backbone for household security, work, benefits, energy, food, and debt. Its 100,000-row engineering slice is not yet a weighted finding.

The full SIPP slice now has a [weighted descriptive scan](projects/us-household-calendar-integration/sipp-weighted-code-scan-v1.md). It is a person-record/month layer using `WPFINWGT`, with official value labels attached; household weighting, variance estimates, and causal interpretation remain separate next steps.

The SIPP fields are mapped to the five bridges in the [SIPP broad-bridge crosswalk](projects/us-household-calendar-integration/sipp-broad-bridge-crosswalk-v1.md). This makes SIPP a population layer for material and work conditions while keeping service, cultural, political, company, and geopolitical links open for their own sources.

The first labeled descriptive result is in the [SIPP population layer](projects/us-household-calendar-integration/sipp-population-layer-v1.md). It reports field-specific nonblank diagnostics and monthly ranges, with person-weight, universe, household-repetition, and variance limits stated beside the results.

The first SIPP cross-group comparison is the [tenure-stratified population layer](projects/us-household-calendar-integration/sipp-tenure-stratified-layer-v1.md). It compares owners, renters, and rent-free occupants across payment difficulty, food hardship, debt, and work, while keeping the comparison descriptive.

The resource comparison is in the [income-to-poverty-ratio stratified layer](projects/us-household-calendar-integration/sipp-resource-stratified-layer-v1.md). It adds a documented inequality axis and shows why debt, work, food, housing, and utility measures cannot be collapsed into one hardship score.

The identifier-complete extract now supports the [SIPP person-transition layer](projects/us-household-calendar-integration/sipp-person-transition-layer-v1.md). It confirms which selected fields can support genuine month-to-month analysis and which are annual/reference-period measures repeated in monthly records.

The transition layer now includes monthly income-to-poverty-ratio bands and job counts, providing a first within-person resource/work mobility diagnostic for the price/payment → household-room and work-control bridges.

The first intersectional SIPP table is the [tenure × resource two-way layer](projects/us-household-calendar-integration/sipp-tenure-resource-two-way-layer-v1.md). It identifies the distribution of material pressure among owners, renters, and rent-free occupants across resource bands without converting association into cause.

The place layer is the [region-stratified SIPP comparison](projects/us-household-calendar-integration/sipp-region-stratified-layer-v1.md). It attaches the official four-region residence field to the material/work measures and keeps local mechanisms open for other sources.

The first design-based uncertainty check is the [SIPP Fay-BRR point-estimate layer](projects/us-household-calendar-integration/sipp-fay-brr-point-estimates-v1.md). It covers five full-sample diagnostics; subgroup tables remain point-only until their replicate estimates are computed.

The first uncertainty-aware subgroup comparison is the [SIPP Fay-BRR tenure layer](projects/us-household-calendar-integration/sipp-fay-brr-tenure-estimates-v1.md). It covers housing, utility, and food-hardship measures for owners, renters, and rent-free occupants.

The first uncertainty-aware resource comparison is the [SIPP Fay-BRR resource layer](projects/us-household-calendar-integration/sipp-fay-brr-resource-estimates-v1.md). It tests the monthly income-to-poverty gradient for the same material measures.

The first uncertainty-aware tenure × resource comparison is the [SIPP Fay-BRR intersectional layer](projects/us-household-calendar-integration/sipp-fay-brr-tenure-resource-estimates-v1.md). It is a population distribution layer feeding the broad housing/place and unequal-exposure themes, not a replacement for the wider program.

The [AI, work, and control project](projects/ai-work-control/README.md) is the current deeper cross-border packet for the work, firm/sector, infrastructure/dependency, and geopolitical themes. Its new [AI capability/dependence layer](projects/ai-work-control/ai-capability-dependence-layer-v1.md) separates capability from ownership, physical complements, local value, replaceability, and state leverage. Its provisional findings, company bridges, macro/infrastructure records, and country cases should be treated as a connected source stream within this broad program, with its stated open gaps preserved.

The [AI infrastructure realization and control layer](projects/ai-work-control/ai-infrastructure-realization-control-layer-v1.md) deepens that cross-border stream with dated milestones and an ownership transition. It separates Romania's public migration target and interim 7-application status from Malaysia's first 25MW handover and later Yondr-to-Vantage campus sale, leaving service quality, local incidence, portability, and state bargaining as explicit tests.

The [safety-net administrative-burden layer](projects/us-safety-net-access/administrative-burden-access-layer-v1.md) deepens the public-systems bridge. It separates eligibility, route-to-help, program exit, employment, food security, and trust, using causal evidence on work rules, parent burden, and office closures while keeping the same-household downstream path open.

The [unequal exposure and status layer](US-UNEQUAL-EXPOSURE-STATUS-LAYER_V1.md) consolidates the distributional evidence across resources, tenure, place, race, family, gender, disability, age, and access route. It makes the next requirement explicit: one valid intersectional comparison with a defined universe, uncertainty, counterexample, mechanism, and downstream outcome.

The first such diagnostic is now the [SIPP Fay-BRR race × resource layer](projects/us-household-calendar-integration/sipp-fay-brr-race-resource-layer-v1.md). It uses the full 2025 SIPP person-month slice and 240 replicate weights to compare rent/mortgage pressure, utility pressure, hunger, food security, and one-job status across four race recodes and four resource bands. It supplies distributional uncertainty and applies the selected variables’ documented status flags and domain conditions; causal mechanisms and downstream outcomes remain open.

The next depth pass is the [SIPP Fay-BRR race × tenure × resource layer](projects/us-household-calendar-integration/sipp-fay-brr-race-tenure-resource-layer-v1.md). It applies the same universe-aware, replicate-weighted design across 48 three-way cells. It is a controlled intersectional distribution check, not a causal decomposition; sparse cells, household counting, mechanisms, and downstream outcomes remain open.

The following status pass is the [SIPP Fay-BRR race × disability × resource layer](projects/us-household-calendar-integration/sipp-fay-brr-race-disability-resource-layer-v1.md). It adds a documented work-limiting-condition measure across 32 cells and shows a large descriptive separation in one-job status alongside material-pressure differences. It does not identify health, care, discrimination, employer, or policy mechanisms.

The next composition pass is the [SIPP Fay-BRR race × children × resource layer](projects/us-household-calendar-integration/sipp-fay-brr-race-children-resource-layer-v1.md). It adds whether a household has members under 18 across 32 cells and shows why child presence, caregiving, employment, and food security must not be collapsed into one family-hardship measure.

The next public-systems layer is the [SIPP SNAP × food-security layer](projects/us-safety-net-access/sipp-snap-food-security-layer-v1.md). It adds current-month SNAP receipt to the same race, child-presence, and resource cells. It shows assistance receipt and food security as distinct population outcomes; application, denial, interruption, benefit amount, route effort, and causal impact remain open.

The monthly extension is the [SIPP SNAP transition layer](projects/us-safety-net-access/sipp-snap-transition-layer-v1.md). It establishes adjacent-month entry, exit, and persistence rates for SNAP receipt. The next unresolved step is to classify why a transition occurred using the documented start/end reason fields.

The reason pass is now the [SIPP SNAP start and end reason layer](projects/us-safety-net-access/sipp-snap-reason-layer-v1.md). It separates health/work-capacity change, income loss, job loss, family change, recertification, improved-income exit, unmet requirements, non-collection, and “not worth the trouble.” It remains weighted descriptive evidence without notice, effort, or downstream household outcomes.

The transition-aligned extension is the [SIPP SNAP transition × recorded reason layer](projects/us-safety-net-access/sipp-snap-transition-reason-layer-v1.md). It classifies about half of observed no-to-yes and yes-to-no transitions, showing why the unclassified half must not be assigned a single meaning.

The [Fay-BRR reason extension](projects/us-safety-net-access/sipp-snap-transition-reason-fay-brr-layer-v1.md) adds design-based uncertainty to those classified shares: job loss or reduced wages is 30.10% of classified entries (SE 3.94 percentage points), while “other” is 49.53% of classified exits (SE 4.34 percentage points). This is a deeper public-systems measurement layer inside the broad program, not a claim that SNAP explains society-wide change.

The material-context extension is the [SIPP SNAP transition × material-context layer](projects/us-safety-net-access/sipp-snap-transition-context-layer-v1.md). It compares adjacent-month income-resource and job changes around entry and exit; it finds that exit is not automatically synonymous with improving resources, while retaining the non-causal and no-variance limits.

The next empirical priority is now the [safety-net event ledger](templates/US-SAFETY-NET-EVENT-LEDGER_V1.md): connect notice, effort, access route, decision, benefit interruption, food/work/debt outcomes, and later trust for the same program episode. This is the most direct currently identified test of whether public administration changes household security or only changes participation.

## Cross-cutting themes to extract in every pass

- What families give up to pay the bills.
- Who gives up time, and what that time displaces.
- Who can get an answer, appeal, switch, refuse, or leave.
- Who controls the work, data, asset, rule, and gain.
- How place and infrastructure distribute exposure.
- Whether firms or public programs improve a headline outcome by transferring cost elsewhere.
- How class, race, age, disability, gender, family structure, migration, and geography change exposure and exit options.
- How material conditions become cultural meaning, trust, blame, identity, public demand, or political action.
- How financial, technological, energy, and supply dependencies affect US firms, communities, and state power.

## First execution order

1. Use the existing 83-topic atlas to select one representative finding for each bridge.
2. Build a source-to-measure table for each selected bridge. Keep population, unit, date, geography, weight, and method beside every number.
3. Separate direct evidence, reported experience, comparison, inference, and missing data.
4. Add one counterexample for every proposed mechanism.
5. Produce one cross-source comparison before attempting a causal claim.
6. Follow the strongest bridge into a matched finding that connects material condition, behavior, institution, power, and wider social or political meaning.
7. Keep Markdown, HTML, atlas links, and evidence audits synchronized.

## Stop rules

- Do not join surveys by geography and call them the same household or person.
- Do not turn a repeated association into a societal trend without population and time coverage.
- Do not infer culture or politics from hardship alone; measure interpretation and action separately.
- Do not treat company performance, service restoration, benefit delivery, or credit access as household success by itself.
- Do not call a connection causal until the relevant arrow is observed or supported by an appropriate design.

## Definition of an end-to-end result

An end-to-end result must show, at the appropriate population or institutional level:

```text
condition or decision
  -> changed choice or behavior
  -> changed household, consumer, worker, market, or community outcome
  -> actor response and control point
  -> distribution of gain, cost, or risk
  -> cultural, social, political, company, sector, or geopolitical meaning
  -> counterevidence, uncertainty, and next test
```

The result may conclude that a link is not established. That is a valid outcome if the missing step is clearly identified.
