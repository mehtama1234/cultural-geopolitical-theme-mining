# US broad program continuity ledger v1

**Checked:** 2026-09-17
**Status:** active long-term program control record  
**Scope:** the complete 14-theme Cultural, Social, and Geopolitical Theme
Mining program

The current concise governing statement is the [broader goal restatement](../BROAD-GOAL-RESTATEMENT_V1.md).

The current focused bridge checkpoint is the [material-to-action status
ledger](US-BROAD-MATERIAL-TO-ACTION-STATUS_V1.md).

The latest reproducibility checkpoint is the [CES medical-affordability/action
audit](projects/us-health-cost-household-choice/cces-medical-affordability-action-reproduction-audit-2026-09-16.md):
the existing local 2018/2020 module files reproduce the committed
hardship/attribution/action screen, while the episode-level remedy, recovery,
trust, and exit arrows remain open.

This ledger keeps the program moving across sessions. It is not a progress
report that can be closed by completing one analysis. A research pass changes
one or more evidence rows; the program remains active until the user changes
or ends it.

## Governing outcome

Maintain a US-centered, cross-source living trend atlas that discovers,
compares, tests, and revisits recurring cultural, societal, political,
consumer, institutional, financial, firm, infrastructure, and geopolitical
themes. Preserve the path from measured condition to behavior, institutional
response, power or risk redistribution, meaning, and wider consequence while
marking every unsupported arrow as open.

The program is successful only when it keeps improving the map across people,
households, consumers, workers, firms, places, institutions, infrastructure,
markets, and states. One dataset, one finding, one bridge, or one session is
never the completion condition.

## Current system state

| Control | Current state | Evidence |
|---|---|---|
| Theme scope | 14 themes represented | [Theme inventory](US-BROAD-THEME-INVENTORY_V1.md) |
| Cross-source map | 56 numbered rotations across the priority bridges, plus later canonical trend additions and broader theme links | [Cross-source synthesis](US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md), [evidence matrix](US-BROAD-EVIDENCE-MATRIX_V1.md), [theme atlas](us-theme-atlas.md) |
| Theme end-to-end audit | 14 theme rows audited from the canonical matrix; all retain a next-required test, and 5 explicitly declare an open status | [Theme end-to-end coverage audit](US-BROAD-THEME-END-TO-END-COVERAGE-AUDIT_V1.md), `audit_broad_theme_end_to_end_coverage.py` |
| Source coverage | 103 project packets; source-family coverage is indexed | [Source coverage](us-source-coverage.md), [source registry](../manifests/source-registry.json) |
| Source-registry coverage | 114 registered source entries; all 114 have analysis-domain references, 106 cite the registered landing URL exactly, and the reverse audit tracks observed domains outside registered families | [Source-registry coverage audit](US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.md), `audit_source_registry_coverage.py` |
| Trend registry | 311 machine-readable records; 1108 observations | [Trend-observation registry](us-trend-observations.md), `validate_trend_observation_records.py` |
| Findings | Domain findings plus a program-level long-form finding are generated as Markdown and HTML and parity-checked where the matched-evidence contract applies | [Matched-evidence index](us-matched-evidence-index.md), [program-level finding](findings/us-broad-program-unequal-optionality-path-001.md), `validate_us_finding_parity.py` |
| Evidence discipline | Units, dates, geography, denominators, methods, limits, counterexamples, and open arrows are required | [Trend protocol](US-BROAD-TREND-EXTRACTION-PROTOCOL_V1.md) |
| Link integrity | Relative Markdown references are checked across the workspace | `validate_local_markdown_links.py` |
| Source-record integrity | Project source-search records must carry date, geography, status, question, and linked source metadata | `validate_source_search_records.py` |
| Trend-record integrity | Recurring trend observations must preserve period, denominator, method, uncertainty, subgroup, counterinterpretation, source URL, and retrieval hash | `validate_trend_observation_records.py` |
| Trend metadata depth | Required fields are complete across all 311 records/1108 observations; optional related-source and reproduction-audit context is reported separately | [Trend metadata coverage audit](US-TREND-METADATA-COVERAGE-AUDIT_V1.md), `audit_trend_metadata_coverage.py` |
| Trend publication | Validated trend records have generated Markdown and HTML registry editions | [Trend-observation registry](../site/us-trend-observations.html), `build_us_trend_observation_registry.py` |
| Cross-source synthesis | The current evidence is periodically read across the full material-to-state chain without merging incompatible units | [Cross-source trend synthesis](US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md) |
| Recurrent-source freshness | Official recurring releases, next checks, revision rules, and access-gated dependencies are tracked separately from findings | [Vintage watchlist](US-RECURRENT-SOURCE-VINTAGE-WATCHLIST_V1.md) |
| Trend-to-atlas linkage | Every machine-readable trend/case record is tagged to validated atlas umbrella themes | `theme_ids` in trend schema and [published registry](../site/us-trend-observations.html) |
| Theme breadth control | Trend records are grouped by umbrella theme and missing-record themes are surfaced | [Trend-theme coverage](../site/us-trend-theme-coverage.html), `build_us_trend_theme_coverage.py` |
| Control synchronization | Registry, theme coverage, source-packet count, HTML edition, and this ledger are checked against current source files | `validate_program_control_sync.py` |
| Active depth lane | Second-cycle same-person and event-compatible depth: timing, persistence, payment, coverage, institutional route, remedy, and household-room boundaries | [Next-pass queue](US-BROAD-NEXT-PASS-QUEUE_V1.md) |
| Hard acquisition dependency | PSID main waves and/or an equivalent same-unit event design | [PSID extract specification](projects/us-household-calendar-integration/psid-material-time-care-extract-spec-v1.md), [wave-file audit protocol](projects/us-household-calendar-integration/psid-wave-file-audit-protocol-v1.md) |

## Broad-goal resumption checkpoint

**Reset:** 2026-09-16

The program is explicitly resumed as the full societal, cultural, political,
consumer, institutional, firm, infrastructure, and geopolitical trend-mining
program. The household constraint and health-cost work remains an evidence
lane, but its unavailable UAS/PSID respondent files do not pause the atlas or
define its success condition.

The first rotating pass used already acquired local evidence and required no
bulk download. It will read the CFPB complaint and response layers, household
fraud and recovery estimates, CPSC safety intervention records, and platform
remedy cases as one bounded comparison of **practical exit**:

```text
problem or restriction
  -> visibility and route to a decision-maker
  -> effort, waiting, review, correction, or compensation
  -> restored access or usable alternative
  -> continued use, switching, non-use, trust, or exit
```

The comparison is not a pooled consumer-outcome estimate. Each source keeps
its own unit, denominator, clock, and evidence type. The deliverable is a
cross-domain mechanism synthesis that identifies which middle stages are
observed and which final outcomes remain open. The next rotation then moves to
AI/platform agency and work control, followed by public-system feedback and
firm/infrastructure dependence, while material/time/care remains an active
later lane rather than a program-wide gate.

The completed first-pass artifact is the [practical-exit cross-domain
synthesis](projects/us-customer-automation-recourse/practical-exit-cross-domain-synthesis-v1.md).

The second rotation now advances AI/platform agency through the [AI optionality
and control-conversion synthesis](projects/us-digital-habits-attention/ai-optionality-control-conversion-synthesis-v1.md).
It preserves the distinction between adoption, immediate time or engagement
effects, captured benefit, dependence, correction, trust, and practical exit.

The third rotation advances public-system feedback through the [SNAP
route-divergence synthesis](projects/us-safety-net-access/snap-route-divergence-food-security-political-feedback-synthesis-v1.md).
It keeps administrative handling, benefit transition, food security, trust,
blame, and political action as separate stages and uses the new reproducible
reason-specific food-security layer without claiming a benefit effect.

The fourth rotation advances firm, infrastructure, and geopolitical capacity
through the [capacity-without-exit cross-domain synthesis](projects/ai-work-control/capacity-without-exit-cross-domain-synthesis-v1.md).
It keeps physical capacity, fiscal revenue, governance rules, local incidence,
replaceability, and external response as separate stages rather than treating
investment or an agreement as public benefit or leverage.
The current realization-stage audit now makes the comparison executable across
the US data-center and Poland JASSM-ER ledgers: the data-center case has 13
dated records including governance and operational-stress events, while the
JASSM-ER case has 7 records centered on authorization, agreement, planned
delivery, and a control comparator. Accepted output, replaceability, public or
partner incidence, and changed external behavior remain open.
The supplier-control follow-up now audits the richer local USAspending response:
74 returned subaward rows resolve to 51 named recipients, with descriptions,
UEIs, and performance-location fields on the returned records; the top five
recipients represent 49.5004% of returned amount. This identifies a traceable
network and a concentration lead, not production output, delivery, market
share, or replaceability.

The fifth rotation returns to material/time/care through the [time-as-hidden-
price cross-domain synthesis](projects/us-household-calendar-integration/time-as-hidden-price-cross-domain-synthesis-v1.md).
It uses existing SIPP, ATUS, MEPS, and SHED evidence without making the
unavailable PSID/UAS acquisition a program-wide gate, and keeps money, time,
care, health, recovery, trust, and political availability as distinct clocks.

The sixth rotation advances unequal exposure and cultural meaning through the
[unequal-optionality/status/meaning synthesis](projects/us-cost-trust-politics/unequal-optionality-status-meaning-synthesis-v1.md).
It compares subgroup-conditioned material and time surfaces with the HTOPS
political counterexample, keeping exposure, practical alternatives,
interpretation, trust, and action as separate stages.

The seventh rotation advances political judgment and collective action through
the [political-action menu synthesis](projects/us-cost-trust-politics/political-action-menu-not-ladder-synthesis-v1.md).
It treats voting, contact, volunteering, complaint, organizing, switching,
and withdrawal as distinct actions rather than one engagement ladder.

The eighth rotation advances the place and local-capacity lane through [local
capacity is not practical exit](projects/us-local-business-place/place-capacity-practical-exit-cross-domain-synthesis-v1.md).
It reframes capacity as an option stack: presence must be joined to
reachability, usability, replaceability, recourse, and practical exit before a
place can be treated as protective. This uses existing local-business,
health-capacity, mobility, housing/insurance, public-route, consumer-recourse,
and place-meaning artifacts without pooling their incompatible units. The next
test remains a dated resident route or place-time episode with attempted use,
fallback, protected/sacrificed outcome, and later stay, switching, movement, or
action.

The ninth rotation advances financial capacity and household room through the
[macro-to-household financial-capacity synthesis](projects/us-financial-intermediation/macro-to-household-financial-capacity-synthesis-v1.md).
It keeps national growth, financial-system capacity, provider supply, user
access, household liquidity, debt, public monitoring, and political meaning as
separate stages. The key conclusion is that aggregate or provider capacity is
not automatically usable household room; the next test remains a dated
obligation or account event with alternatives, payment/record consequences,
remedy, later security, trust, or exit.

The tenth rotation advances housing security and the cost of staying put
through the [housing, insurance, hazard, and energy synthesis](projects/us-housing-insurance-risk/cost-of-staying-put-synthesis-v1.md).
It keeps rent arrears, insurance gaps, premiums, nonrenewal, hazard, energy
burden, repair, and public backstops as distinct but potentially compounding
layers. The next test remains a matched property or household episode linking
notice, claim or repair, assistance, payment/borrowing, health or work
trade-offs, and stay, move, or recovery.

The eleventh rotation advances the institutional-mediation lane through
[route-specific institutional friction](projects/us-household-constraint-cascade/institutional-friction-route-specific-outcomes-cross-domain-synthesis-v1.md).
It separates prescription delay, authorization denial, benefit interruption,
complaint routing, and downstream debt remedies rather than treating them as
one friction measure. The next test is a same-case ledger with the route
object, timing, alternatives, effort, verified remedy, protected/sacrificed
outcome, and later trust, action, switching, or exit.

The twelfth rotation advances domestic capability, dependence, and state
leverage through the [domestic capacity and state-leverage bridge](projects/ai-work-control/domestic-capacity-dependence-state-leverage-cross-source-bridge-v1.md).
It keeps domestic affordability, firm and infrastructure capacity, ownership,
supplier choice, procurement, production, delivery, alliance implementation,
and external behavior as separate stages. The promotion rule is explicit:
spending, agreement, or capacity is not leverage until an observed refusal,
switch, negotiation, regulatory response, or changed external behavior shows
that another actor's options or conduct changed.

The thirteenth rotation advances cultural and political conversion through
[material pressure and political meaning](projects/us-cost-trust-politics/material-pressure-to-political-meaning-synthesis-v1.md).
It preserves the same-respondent temporal evidence for later food, energy, and
work outcomes while showing that institutional confidence, attribution,
identity, and civic action do not move automatically with hardship. The next
test remains a timed design that measures the responsible actor, prior
judgment, information environment, direct action, remedy, and later
legitimacy.

The fourteenth rotation advances time, care, work, and political availability
through the [time-and-care political-availability bridge](projects/us-cost-trust-politics/time-care-to-political-availability-bridge-v1.md).
It keeps work schedules, care, travel, illness, registration barriers, formal
representation, civic action, and withdrawal as distinct resources. The next
test remains a same-person work or care event with schedule control,
information, trust, attribution, voting or organizing, and employer/agency
response measured over time.

The fifteenth rotation advances the end-to-end depth lane through the [MEPS
event-to-later-panel follow-up](projects/us-household-constraint-cascade/meps-event-six-month-followup-v1.md).
It places first office, emergency-room, or inpatient events strictly between
R3/1 and R4/2 before same-person R5/3 health and employment outcomes. The
result strengthens the time-order and persistence stages, while preserving the
boundary that later status is not verified recovery: claim identity,
treatment continuity, alternatives, remedy, household trade-offs, trust, and
exit remain open.

The sixteenth rotation deepens the institutional-response arrow through the
[MEPS friction-to-later-panel screen](projects/us-household-constraint-cascade/meps-friction-later-panel-v1.md).
It carries route-specific denial or prior-authorization reports on the strict
event/person frame into later same-person health and employment transitions.
The health persistence signal is clearer than the employment pattern, but
neither is verified recovery or remedy; claim timing, appeal, treatment
continuity, household adaptation, trust, action, and exit remain open.

The seventeenth rotation advances the money-and-obligation stage through the
[MEPS event payment and bill-context screen](projects/us-health-cost-household-choice/meps-2024-event-payment-bill-context-v1.md).
It shows that observed self/family payment, total event payment, annual bill
problems, coverage, resources, and care-access reports are separate and often
non-monotonic surfaces. The next test remains a dated obligation with
deductible or balance, payment timing, borrowing or substitution, foregone
care, verified remedy, and recovery.

The eighteenth rotation sharpens the practical-room counterexample through the
[MEPS event payment-band screen](projects/us-health-cost-household-choice/meps-2024-event-payment-bands-v1.md).
Within event families, zero payment can coexist with lower confidence in
covering an unexpected expense, while higher payment can coexist with more
medical debt. These are selection and payer-protection patterns, not payment
effects; the next test remains a same-household obligation and liquidity
episode with timing, substitution, debt, care continuation, remedy, and
recovery.

The nineteenth rotation adds coverage-conditioned event context through the
[MEPS acute-event coverage screen](projects/us-health-cost-household-choice/meps-2024-event-context-by-coverage-v1.md).
It shows that acute-event health and bill-problem surfaces differ across
private, public-only, and uninsured groups, while preserving coverage as a
condition rather than an explanation. The next test remains plan adequacy,
event bill timing, care alternatives, delayed or foregone care, treatment
continuity, remedy, and household outcome.

The twentieth rotation returns to consumer power through [consumer loss and
complaint visibility](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-018.md).
It keeps household fraud exposure, unrecovered money, recovery time, payment
route, complaint routing, and response labels as distinct denominators. The
next test remains a same-customer financial-service case with attempted and
unsubmitted contacts, verified correction or recovery, repeat effort, trust,
switching, and exit.

The twenty-first rotation makes the open middle executable through the [MEPS
staged-ledger stage-coverage audit](projects/us-household-constraint-cascade/meps-staged-ledger-stage-coverage-audit-v1.md).
The existing 18,457-row local frame now has a machine-readable coverage report:
trigger and payment/context are observed, choice/route/follow-up are only
reported round proxies, and remedy plus meaning/action are unknown. This is a
depth-control artifact, not a new causal estimate. The next broad pass should
use the same stage vocabulary when advancing another household, consumer,
political, place, institutional, or geopolitical lane.

The twenty-second rotation returns to the cultural and political side of place
through the [migration, local demand, housing, services, and belonging
layer](projects/us-immigration-local-demand/migration-demand-housing-services-belonging-layer-v1.md).
It treats new residents as workers, customers, neighbors, entrepreneurs, and
public-system users simultaneously, while keeping local capacity, unequal
incidence, belonging, attribution, trust, action, and mobility as separate
evidence stages. The existing layer is a cross-source design and not a local
causal estimate; the next pass needs matched place exposure and direct resident
meaning/action measures.

The twenty-third rotation advances the work and firm side through the [firm
capacity, AI adoption, and labor mobility finding](projects/ai-work-control/findings/ai-work-control-064.md).
It keeps establishment training and infrastructure, task-level adoption,
formal representation, and aggregate mobility separate. The next test is a
dated workplace implementation record with monitoring, review, schedule/pay,
grievance, remedy, household, bargaining, and exit outcomes; the present
evidence does not claim worker control or an AI effect.

The twenty-fourth rotation advances housing and place security through the
[place risk, housing security, mobility, and local life layer](projects/us-housing-insurance-affordability/place-risk-mobility-local-life-layer-v1.md).
It keeps rent/mortgage, insurance, hazard, energy, transport, business, and
public-backstop evidence separate while asking who can stay safely, who can
move, and who absorbs the next loss. The next test remains a matched
property/household event with protection, repair, assistance, time/care/work
trade-offs, recovery, and resident meaning; no move or political effect is
claimed from the current place-level surfaces.

The AI/platform lane is refreshed through the [AI use, work, contact, and exit
synthesis](projects/us-digital-habits-attention/ai-use-work-contact-exit-synthesis-v1.md).
It puts ordinary AI adoption, randomized work-time change, synthetic-contact
behavior, companion-product exit tactics, and regulatory inquiry in one
reviewable mechanism map while preserving their separate units and clocks. The
open arrow remains conversion into durable control: data portability, error
correction, captured benefit, worker/consumer alternatives, trust, and later
exit are not jointly observed.

The twenty-fifth rotation advances the financial-access and recourse lane
through [the financial route is part of the social outcome](projects/us-financial-intermediation/financial-access-route-recourse-public-capacity-synthesis-v1.md).
It keeps provider capacity, household account status, nonbank routes, credit
visibility, complaint correction, public fiscal room, household security,
trust, switching, and political judgment separate. The next test remains a
dated account/payment episode with alternatives, terms, effort, response,
remedy, recovery, and exit; the current cross-source layers do not establish
a household financial causal or trust effect.

The twenty-sixth rotation advances the consumer-culture, trust, status, and
everyday-power lane through the [consumer culture, trust, status, and everyday
power layer](projects/us-consumer-culture/consumer-culture-trust-status-layer-v1.md).
It treats buying, searching, sharing data, seeking help, reviewing, reporting,
switching, and staying as distinct participation surfaces that can carry
meaning and generate institutional information. The next test remains a
same-customer dated episode linking need or exposure, social-signaling and
information conditions, cost, response authority, verified remedy, recovery,
switching or abandonment, and later trust or political demand. Participation
is not satisfaction, trust is not consent, and staying is not free choice
without a practical alternative.

The twenty-seventh rotation turns that reader route into a cross-source
proposition through the [consumer participation, trust, and practical power
synthesis](projects/us-consumer-culture/consumer-participation-trust-power-cross-source-synthesis-v1.md).
It places confidence, payment redistribution, platform-mediated civic
attention, charitable-food access, and digital recourse beside one another
without pooling their estimates. The resulting theme is unequal optionality
under institutional mediation: participation can carry money, time, privacy,
attention, safety, stigma, and recovery costs. The next test remains one
dated customer or household episode with alternatives, non-use/non-reporting,
attributed cause, institutional authority, verified remedy, recovery, trust,
and switching or exit.

The twenty-eighth rotation turns the exit question into an observability audit
through the [practical exit observability matrix](projects/us-customer-automation-recourse/practical-exit-observability-audit-v1.md).
It places observed SNAP program exits, platform restoration and continued-use
cases, fraud recovery burden, CFPB visibility, insurance-market movement, and
local capacity beside one another without treating any as a common exit rate.
The next test remains a same-unit episode with alternatives, remedy receipt,
switching/non-use, move/stay, and later trust or action.

The first small implementation test is now complete in the [platform-remedy
ledger dry-run](projects/us-customer-automation-recourse/practical-exit-platform-ledger-dry-run-v1.md).
Across 27 existing local records, 8 can be labeled `access_restored` from
explicit source language and 19 remain `unknown`; none can be promoted to
practical exit because alternatives, relevant costs or constraints, follow-up,
and protected or sacrificed outcomes are not documented at the same-unit
level. The machine-readable [coverage audit](projects/us-customer-automation-recourse/practical-exit-platform-ledger-dry-run-v1.json)
preserves this boundary.

The same contract was then tested against the 25-record CFPB student-loan
event ledger in the [CFPB dry-run](projects/us-customer-automation-recourse/cfpb-practical-exit-contract-dry-run-v1.md).
All 25 rows retain observed route/response visibility but `unknown` post-event
status; no same-customer alternative, remedy receipt, recovery, switching,
non-use, trust, or action is established. This sharpens the next collection
requirement without requiring a larger download.

The twenty-ninth rotation adds a second clock to the end-to-end household lane
through the [MEPS event-to-work two-clock audit](projects/us-household-constraint-cascade/meps-event-work-two-clock-audit-v1.md).
R4/2 nonemployment levels after strict-window events are aligned by event family
with R5/3 nonemployment, status change, onset, and resolution. Acute-event level
differences persist, but transition directions are mixed and the smaller R5
universe is not row-merged with the R4 screen. This advances the material →
work → later-status arrow while keeping claim identity, alternatives, remedy,
household recovery, meaning, action, and exit open.

The thirtieth rotation audits the retained HTOPS panel record's endpoint
observability through the [local endpoint audit](projects/us-cost-trust-politics/htops-2025-local-endpoint-observability-audit-v1.md).
The record exposes 36 retained measures (32 substantive material/judgment
measures plus four sample/design fields) but
does not represent attribution, distinct civic/political action, remedy,
recovery, switching, or exit. This turns the next acquisition into a precise
dictionary-and-shared-ID check while preserving the distinction between a
missing local artifact and a missing source variable; no large acquisition or
new estimate was made.

The thirty-first rotation extends the local MEPS event spine with the
[prescription-event cascade](projects/us-household-constraint-cascade/meps-prescription-event-cascade-v1.md).
Among 18,723 round-order-valid person records, 1,773 had a first prescription
event inside the R3/1-to-R4/2 window. The event-window group has higher later
care-delay, medical-debt, collector-contact, and nonemployment context than
the complementary group. The result advances dated health-to-household
coverage while retaining the missing claim-level need, fill/adherence,
treatment continuity, remedy, recovery, trust, action, and exit arrows; no new
data was downloaded.

The thirty-second rotation carries the prescription-event group to a later
R5/3 clock through the [six-month follow-up](projects/us-household-constraint-cascade/meps-prescription-event-six-month-followup-v1.md).
Of 18,691 round-order-valid people, 724 had an in-window prescription event.
Health worsening is lower in the event-window group, while employment status
change and both nonemployment onset and resolution are higher. The mixed
directions are preserved as selected descriptive context; later status is not
called recovery, and adherence, continuity, remedy, household recovery, trust,
action, and exit remain open.

The thirty-third rotation rechecks the CFPB public complaint schema through a
three-record mortgage probe documented in the [consumer-outcome field audit](projects/us-customer-automation-recourse/cfpb-consumer-outcome-field-audit-v1.md).
The current response exposes receipt, routing, response, timeliness, and
place/product fields but no verified correction, repeat effort, account change,
switching, non-use, or post-response assessment; narrative-field visibility
also differs from the earlier probe. This updates the schema boundary without
turning response labels into remedy or exit evidence, and no bulk data was
acquired.


The consumer-power lane was refreshed on 2026-09-13 with a live CFPB
aggregate-only API snapshot and reusable fetcher. This is current
institutional-response evidence, not a verified consumer-outcome result.
The annual 2020–2024 comparison now adds time while retaining taxonomy,
routing, and publication-rule breaks as explicit counterinterpretations.
The [case-route sample](projects/us-customer-automation-recourse/cfpb-case-route-sample-2024-v1.md)
adds a bounded case-level receipt-to-company-routing diagnostic, with
product-conditioned visibility and response labels. It does not estimate
population route rates or verified remedy; same-case effort, outcome, trust,
switching, and exit remain open.

The household fraud lane now includes a codebook-backed SHED subgroup layer
conditioning exposure, unrecovered money, and recovery time on age, income, and
account payment route. It strengthens the household loss-to-burden stage while
leaving verified firm remedy, digital-access and general disability gradients,
later trust, switching, and exit open.

The platform/data/attention lane now includes the [Pew 2026 AI daily-life,
control, and public-concern layer](projects/us-digital-habits-attention/pew-2026-ai-daily-life-control-layer-v1.md).
It adds current U.S. adult measures of chatbot adoption, frequency, purpose,
age differences, perceived usefulness, privacy concern, pace, and confidence in
government regulation. It does not establish dependence, harm, actual privacy
loss, product causation, or practical ability to leave.

The same lane now includes a separate [Pew 2025 adult social-media-use
layer](projects/us-digital-habits-attention/pew-adult-social-media-use-2025-layer-v1.md)
and [bounded finding](projects/us-digital-habits-attention/findings/us-digital-habits-attention-004.md).
It provides adult platform reach, repeated-wave change, frequency, and
age/gender/race-and-ethnicity patterning. The adult sample is kept separate
from the teen platform/chatbot survey and from the frequency sample; reach is
not treated as logged attention, content exposure, persuasion, or exit cost.

The [FTC AI-companion inquiry record](records/us-ftc-ai-companion-inquiry-2025.json)
adds a separate institutional response: seven companies received information
requests about monetization, data use, safety testing, age limits, disclosures,
and possible effects on children and teens. The inquiry is not treated as
evidence of harm or enforcement outcome.

The [World Bank WDR 2026 AI capability and governance record](records/us-world-bank-wdr2026-ai-capability-governance.json)
separates the adopt/adapt/advance framework, value-chain concentration, local
complements, public-service evaluation, and political-power analysis from US
outcome estimates. Its detailed [source-specific layer](projects/ai-work-control/world-bank-wdr2026-ai-capability-governance-layer-v1.md)
and [project finding](projects/ai-work-control/findings/ai-work-control-017.md)
preserve the report's comparative and policy-analysis boundaries.

The [IMF AI adoption and inequality record](records/us-imf-ai-adoption-inequality-2025.json)
separates a modeled wage-inequality channel from a modeled wealth-inequality
channel. Its [source layer](projects/ai-work-control/imf-ai-adoption-inequality-layer-v1.md)
and [detailed finding](projects/ai-work-control/findings/ai-work-control-018.md)
preserve the 2014–2048 scenario horizon and do not treat the modeled Gini
changes as realized U.S. outcomes.

The [BEA AI economic-accounts record](records/us-bea-ai-economic-accounts-utilization-costs-2026.json)
separates early indirect industry-account estimates, state-industry
utilization/output associations, and industry cost contributions. Its [source
layer](projects/ai-work-control/bea-ai-economic-accounts-utilization-costs-layer-v1.md)
and [detailed finding](projects/ai-work-control/findings/ai-work-control-019.md)
preserve the distinct units, timing, denominators, and non-causal boundaries.

The [OFR FY2025 capacity record](records/us-ofr-2025-ai-capacity-workforce-data-infrastructure.json)
adds a public-financial-institution layer: workforce and budget change,
reported operational AI use, analytics-platform transition, and new repo-market
data capacity. Its [source layer](projects/ai-work-control/ofr-2025-public-financial-capacity-layer-v1.md)
and [detailed finding](projects/ai-work-control/findings/ai-work-control-020.md)
preserve the annual-report self-report boundary and do not infer AI causation,
productivity, service quality, or financial-stability outcomes.

The [NBER task-level generative-AI adoption record](records/us-nber-task-level-genai-adoption-2026.json)
adds a worker/task middle layer between occupational exposure and workplace
control. Its [source layer](projects/ai-work-control/nber-w35677-task-level-adoption-layer-v1.md)
and [detailed finding](projects/ai-work-control/findings/ai-work-control-021.md)
preserve the full-paper descriptive status, worker/task unit, measurement
distinction, and open adoption-to-control link.

The cross-source [AI capability synthesis](projects/ai-work-control/findings/ai-work-control-022.md)
now places NBER worker/task adoption beside BEA, BIS, IMF, World Bank, and OFR
evidence. It is explicitly a multi-source mechanism synthesis, not a pooled
causal estimate, and keeps the worker-to-household, public-capacity, and
geopolitical joins open.

The digital-habits lane now has a second detailed [platform agency finding](projects/us-digital-habits-attention/findings/us-digital-habits-attention-002.md)
that separates attention, trust, civic action, complaint visibility, response,
remedy, switching, and exit. It is a cross-source route synthesis, not a
platform-causation or user-harm estimate.

The geopolitical lane now has a detailed [capacity-to-leverage finding](projects/ai-work-control/findings/ai-work-control-023.md)
that keeps resource allocation, commitments, production, integration,
ownership, infrastructure, and regulatory response separate from actual
external behavior change. The finding now incorporates the IMF April 2026 WEO
macro-fiscal layer, so defense financing, debt, and social-spending trade-offs
are recorded as a separate stage before any claim of realized leverage.

The public-system lane now has a [buffer-and-credit bridge](projects/us-safety-net-access/findings/us-safety-net-access-012.md)
that places SIPP SNAP transitions and following hardship beside Federal Reserve
liquidity, revolving-credit, linked-balance, student-loan, and retirement-action
evidence. It is a non-pooled mechanism map; same-episode route, financial
coping, household outcome, trust, and political-action links remain open.

The follow-on [route-and-buffer synthesis](projects/us-safety-net-access/findings/us-safety-net-access-013.md)
adds the WBNS notice/interruption and charitable-food access layers. It shows
that public receipt, route failure, cash/credit coping, supplemental food, and
unmet need are distinct stages of an incomplete safety-net pathway. The
authenticated WBNS public-use file remains an acquisition gate, and no
same-household remedy, trust, political-action, or recovery claim is promoted.

The SHED fraud lane now has a 2024–2025 annual comparison using the same age
and income definitions. The income ordering remains nonmonotonic, while the
age exposure ordering changes between annual samples; this weakens a simple
age-trend claim and preserves separate annual-sample, reporting, and
composition limits. The 2025 public file lacks the 2024 P2P fields.

The food-security lane now pairs the validated USDA 2024 household-security
record with a validated BLS 2020–2024 food-at-home price-pressure record. The
pair establishes temporal context across price level, inflation rate, food
security, severity, family shielding, and assistance participation, while
keeping household causation and benefit adequacy open.

The same lane now includes the 2024–2025 SHED food-pressure record, adding
income-conditioned food insufficiency and multiple reported adaptations. These
are repeated annual snapshots rather than a linked respondent panel; the
pressure-to-food-to-recovery arrow remains an acquisition target.

The SHED panel lane now includes an authoritative 2024–2025 condition-path
rerun. Official archive checksums and the condition-path output hash are
recorded in the [reproduction audit](projects/us-household-financial-pressure/shed-panel-reproduction-audit-2026-09-13.json),
and the [trend record](records/us-shed-panel-adaptation-condition-path-2024-2025.json)
preserves path and metric-specific denominators. This is durable same-person
descriptive depth; dated causes, attribution, political meaning, and recovery
remain open.

The SHED weight-surface audit confirms that the public-use 2024 and 2025 files
contain main and panel weights but no replicate or variance fields. Design-based
uncertainty remains an explicit acquisition gap rather than an invented
standard error.

The [SHED panel work/health/care synthesis](projects/us-household-financial-pressure/findings/us-household-financial-pressure-011.md)
now places work-more, borrowing, and reduced-use persistence beside health
direction and unpaid-care entry/exit for the same 4,419 paired respondents.
This is descriptive longitudinal depth, not a dated event, schedule-control,
recipient-outcome, trust, or political-action result.

The time/care lane now has a reproducible ATUS 2024 microdata extraction for
7,669 diary respondents. The [ATUS record](records/us-atus-time-care-microdata-2024.json)
keeps primary activity categories separate from secondary childcare and
eldercare, with archive hashes and subgroup denominators. The next depth test
is replicate-weight uncertainty plus the eldercare roster and a dated event;
the one-day diary is not a longitudinal household result.

The new [eldercare network and time-capacity synthesis](projects/us-aging-care-strain/atus-eldercare-network-time-capacity-synthesis-v1.md)
closes that immediate roster-interpretation step: the 2024–2025 extraction
shows that about four in five rostered providers list a non-household
recipient, while preserving separate annual samples, respondent-level weights,
and recipient-record limits. This strengthens the care-network exposure map;
it does not establish distance, intensity, work displacement, recipient
outcomes, or recovery. The next test remains a repeated provider/household
design with schedule control and replacement support.

The same extraction now runs on the official 2025 ATUS files, adding a
2024–2025 annual comparison with replicate-weight uncertainty. This provides
time-order at the population level while explicitly retaining separate annual
samples; individual recovery, event attribution, and same-household linkage
remain acquisition targets.

The material/time/care lane now has an executable [PSID wave-file audit
protocol](projects/us-household-calendar-integration/psid-wave-file-audit-protocol-v1.md)
and `scripts/audit_psid_wave_files.py`. It accepts separate family and
individual files for each 2019/2021/2023 wave, unions their mapped variable
surface, and fails closed on missing waves, fields, or explicit merge keys.
This advances the acquisition gate; no PSID estimate or same-unit end-to-end
claim is implied until universe, missingness, retention, merge, and weight
audits are run on authenticated files.

The PSID access gate was rechecked on 2026-09-17: the official package routes
remain account-controlled and no target microdata files are present locally.
The available SIPP household-selection diagnostic was tightened with a hashed
2025 schema scan showing `WPFINWGT` as the only weight-related variable in the
5,203-variable surface; one-record household results therefore remain
sensitivity diagnostics rather than official household prevalence estimates.

The [SIPP utility/tenure/care/work option-stack synthesis](projects/us-household-calendar-integration/sipp-utility-tenure-care-work-option-stack-synthesis-v1.md)
now consolidates the available 2025 full-file fallback: utility difficulty,
housing tenure, next-month work movement, adjacent resource/job transitions,
and annual child-care work prevention. This advances the same-person
material/time/care conditioning map while preserving mixed clocks, small-cell
uncertainty, and the absence of a dated bill or shutoff event. The next test
remains a dated service event followed through work, care, housing, health,
and recovery.

The linked [SIPP utility-to-work reproduction audit](projects/us-household-calendar-integration/sipp-utility-work-following-reproduction-audit-2026-09-14.json)
was rechecked on 2026-09-16 using the current local `full-v18` slice. It
reproduced the same matched-pair universe and estimates, with no new download;
the dated filename is retained for continuity while its checked field records
the refresh.

The geopolitical/procurement lane now includes a machine-readable
[JASSM/LRASM subaward-structure record](records/usaspending-jassm-lrasm-subaward-structure-2024-2025.json).
It adds one bounded case observation linking a parent award to 74 returned
subaward records, 51 reported recipients, and description-visible component
classes. This advances the supplier/input arrow while leaving ownership,
geography, workforce, production, delivery, readiness, and external response
open.

The [JASSM-ER delivery watchpoint](projects/ai-work-control/jassm-er-delivery-watchpoint-2026-09-13.md)
was rechecked again on 2026-09-14 against current Polish and US official-source
releases and still finds a planned 2026–2030 delivery window, not a separately
reported delivery or acceptance event. Procurement intent and realized
capability remain separate ledger stages.

The [domestic capacity and state-leverage bridge](projects/ai-work-control/domestic-capacity-dependence-state-leverage-cross-source-bridge-v1.md)
now integrates the procurement, SIPRI, and AI-infrastructure realization layers.
It treats resources, commitments, operating milestones, ownership,
replaceability, and external response as separate stages; no leverage claim is
promoted without an observed state or external behavior change.

The [JASSM/LRASM procurement-to-capability realization synthesis](projects/ai-work-control/jassm-lrasm-procurement-to-capability-realization-synthesis-v1.md)
now provides the reader-facing control route for the procurement case. It
separates award, supplier/UEI, facility, capacity, production support,
integration testing, acceptance, delivery, fielding, inventory, maintenance,
replaceability, and external response. The public record currently supports
only the earlier and middle stages; the next acquisition is a dated
identifier-bearing realization event, not a stronger inference from contract
value or factory capacity.

The Prince William data-center lane now adds a county-reported 2012–2024 tax-
revenue series plus a county-linked TY2025 extension alongside the physical GIS
pipeline. The TY2025 report records $465.9 million, up 59% year over year, with
the computer-equipment rate rising to $4.15 per $100. This strengthens local
pipeline-to-public-revenue visibility while leaving actual load, household
incidence, service costs, jobs, environmental burden, legitimacy, and state
leverage open; source format and tax-rate changes remain explicit boundaries.

The meaning/politics lane now has a dedicated [historical GSS finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-024.md)
for the 1972–2024 anchor-year comparison. It preserves the recurring
financial-satisfaction/trust and fairness gradient while documenting changing
gap size, mode, question availability, weights, and the absence of a dated
material-to-action link. The next step is formal harmonization or a timed panel,
not an unbroken causal trend claim.

The financial-intermediation lane now includes the [Global Findex 2025
financial-access finding](projects/us-financial-intermediation/findings/us-financial-intermediation-001.md)
and a hashed World Bank API extract. It adds US account ownership from 2011
through 2024, the near-disappearance of the aggregate gender ownership gap,
and selected-country phone/smartphone/account contrasts. It also preserves the
high-income questionnaire boundary: several 2024 US payment, saving,
borrowing, and emergency-fund indicators are unavailable in the returned
series. The new layer strengthens access and connectivity coverage, but leaves
usable liquidity, terms, safety, remedy, trust, and exit as separate
same-person or same-account tests.

The current rotation also adds the [AI/work-control endpoint audit](projects/ai-work-control/ai-work-control-endpoint-audit-v1.md).
Using only committed local records, it separates AI exposure and adoption from
organizational implementation, worker consultation, rule/design change, and
realized worker control. The local evidence is strongest before the
same-workplace outcome stage; the next test is a named system with notice,
override or appeal, enforcement, workload/pace, pay, schedule, health,
bargaining, and household-security fields plus a differently governed comparison.

The [named workplace system stage ledger](projects/ai-work-control/named-workplace-system-stage-ledger-v1.md)
turns that next test into a controlled comparison of IBM Germany AI governance,
Microsoft Places, and Microsoft 365 Copilot. It records the highest supported
stage for each case and keeps enforcement, actual worker exposure, worker and
household outcomes, and exit as explicit unknowns. This is a local-record
stage comparison, not a worker-power estimate.

The named-system comparison now has a targeted [Microsoft Places technical
control-surface note](projects/ai-work-control/data/microsoft-places-technical-control-surface-source-note-v1.md).
Current official documentation makes consent, manual override/clear,
geography-specific policy, Inform/Ask/Off modes, and no historical Automatic
Update view inspectable. This corroborates available product controls, not the
historical council causal claim, tenant configuration, worker understanding,
enforcement, or worker/household outcomes.

The [broad same-case episode availability audit](broad-same-case-episode-availability-audit-v1.md)
now compares five committed local surfaces: CFPB student-loan events,
platform remedies, the SHED recontact panel, the HTOPS linked panel, and the
MEPS bounded event ledger. No surface closes all nine required episode stages.
The next broad step is therefore to select one lawful stable episode key and
measure stage-specific missingness instead of pooling these complementary
records.

The [ranked next-episode selection](broad-next-episode-selection-v1.md) makes
the next local depth route executable. MEPS is primary because its staged
ledger has 18,457 exact person/event rows with dated first-event families and
payment, coverage, health, employment, and bill context. CFPB/platform remains
the remedy counterexample; SHED and HTOPS remain non-pooled persistence and
meaning context. The MEPS route must stop at an acquisition gap if event-level
alternatives, remedy, or follow-up are absent.

The selected MEPS route has been field-audited across all 18,457 staged rows in
the [MEPS event-field availability audit](projects/us-health-cost-household-choice/meps-event-field-availability-audit-v1.md).
It has complete hashed ID and month-date scaffolding plus round-level context,
but no initiating need, alternatives, event-specific choice/response, verified
remedy, meaning/action, or usable geography. The route remains primary for a
targeted acquisition or linkage; it must not be promoted as a causal recovery
chain.

The remedy counterexample is now field-audited in the [platform-remedy
availability note](projects/us-customer-automation-recourse/platform-remedy-field-availability-audit-v1.md).
All 27 episodes have route and decision records, but none has a documented
alternative, effort, follow-up window, remedy receipt, durability,
protected/sacrificed outcome, or meaning/action; 8 carry `access_restored` and
10 carry observed remedy-related records. This preserves the distinction
between institutional action and lived recovery/exit.

The paired [IMF Financial Access Survey provider-side audit](projects/us-financial-intermediation/imf-fas-provider-side-access-audit-2026-09-15.md)
now separates annual administrative/provider capacity from Findex's adult
reports. A public SDMX query returned and preserved 566 US rows for 2020–2024,
including provider counts, branch density, and household deposit/loan ratios.
The official 2025 release also describes 163 reporting economies and 121
series through 2024. The new US result is a provider-side measurement, not a
household welfare or digital-substitution estimate; the next test is to join it
carefully to user terms, place access, remedy, and household outcomes.

The latest rotation advances the named AI/work-control lane through the
[OpenAI/Statsig recruitment-enforcement event](projects/ai-work-control/findings/ai-work-control-085.md).
The official DOJ/IER agreement records a dated US recruitment practice in
which US workers were required to mail applications while other applicants
could apply electronically, followed by a $1.2 million Treasury payment, a
$2 million potential-back-pay set-aside, applicant identification and notice,
electronic-application and ATS controls, training, reporting, and three years
of oversight. This closes a concrete practice → institutional-remedy-design
segment, while keeping individual applicant exposure, actual payment receipt,
job access, recurrence prevention, worker voice, later trust, and exit open.
The case is a named enforcement event, not a prevalence estimate for AI
recruiting or a causal worker-outcome result.

The next named comparison is the [Apple PERM back-pay implementation
event](projects/ai-work-control/findings/ai-work-control-086.md). DOJ reports
that Apple's $18.25 million back-pay fund was processed and exhausted after
individualized lost-income review of thousands of potential claimants, with
external posting, electronic applications, ATS searchability, training, and
monitoring required by the 2023 settlement. This strengthens the observed
remedy-implementation stage relative to a merely reserved fund, while leaving
individual payment distribution, restored job consideration, durable
compliance, worker voice, household recovery, trust, and exit open. It is a
named implementation event, not a prevalence estimate or causal worker-outcome
result.

The thirty-seventh rotation returns to the bridge between institutional voice
and lived remedy through the [political action menu](projects/us-cost-trust-politics/political-action-menu-not-ladder-synthesis-v1.md)
and [consumer recourse synthesis](projects/us-customer-automation-recourse/consumer-recourse-visibility-remedy-synthesis-v1.md).
It keeps complaints, appeals, legal challenges, votes, contacts, switching,
and withdrawal as distinct action channels, and keeps public routing, formal
orders, payment or distribution, actual restoration, residual loss, trust,
and exit on separate clocks. This adds a durable cross-source comparison, not
a pooled action rate or a same-person remedy result. The next decisive test
remains one lawful episode with a stable identifier through alternatives,
effort, verified remedy receipt, protected or sacrificed outcome, and later
action or exit.

The thirty-eighth rotation carries the worker-side remedy comparison into the
canonical map through the [OpenAI/Statsig recruitment settlement](projects/ai-work-control/findings/ai-work-control-085.md)
and [Apple PERM implementation](projects/ai-work-control/findings/ai-work-control-086.md).
Together they show two different remedy clocks: a potential claimant process
with prospective access controls, and reported aggregate back-pay processing
with an exhausted fund. Neither public record supplies a worker-level
denominator, restored opportunity, durable compliance, later household
security, trust, political action, or exit. The next test remains a lawful
worker-side episode design or a public implementation follow-up with stable
claim/application identifiers.

The thirty-ninth rotation returns to the migration/place and cultural-meaning
lane through the [immigration concern and essential-activity non-use finding](projects/us-immigration-local-demand/findings/us-immigration-local-demand-002.md).
Published WBNS subgroup evidence reports protective or delayed non-use across
work, care, school, transport, police, community, and public-benefit routes
when immigration or information-sharing concerns are present. This makes
non-use a visible participation currency while keeping causal ordering, legal
risk, alternatives, remedy, trust, and political action open.

The fortieth rotation converts that layer into the [migration participation-
currencies synthesis](projects/us-immigration-local-demand/findings/us-immigration-local-demand-003.md).
It compares population presence, local capacity, institution-specific trust,
civic action, voting, and safe institutional use without assigning county
context to respondent experience. The result weakens any single integration or
growth-to-withdrawal narrative; the next test is a place-linked repeated family
or respondent episode with exposure, alternative, attribution, and follow-up.

The forty-first rotation advances work and bargaining through the
[worker-power channels synthesis](projects/us-employee-ownership-meaning/findings/us-employee-ownership-meaning-002.md).
It separates financial stake, intelligible ownership communication,
representative voice, technical control, recourse, monetary remedy, household
security, and exit. The employee-ownership field experiment supplies a
communication-to-retention mechanism, while named workplace and platform
records show why documentation, reactivation, or a formal award is not the
same as wealth or control.

The forty-second rotation returns to material/time/care through the [care-time
hidden-price synthesis](projects/us-household-calendar-integration/findings/us-household-calendar-integration-044.md).
It places stable annual ATUS averages beside selected SIPP childcare-related
work-time loss and following housing/utility hardship. This strengthens the
distributional hidden-price concept while leaving care alternatives, earnings,
schedule control, recovery, trust, and political availability open.

The current four-rotation handoff therefore preserves breadth across meaning,
place, worker power, and household time. The next substantive step is not
another adjacent exposure cross-tab: it is a lawful, storage-light same-unit
episode with an alternative, institutional response, verified remedy or
recovery, and later action/exit field. If that route is unavailable, publish
the exact acquisition gap and rotate to the next theme rather than implying
completion.

The forty-third rotation applies that rule to the [MEPS episode-field
availability finding](projects/us-health-cost-household-choice/findings/us-health-cost-household-choice-013.md).
The retained 18,457-row staged ledger has complete hashed event identity and
month-date scaffolding plus round-level context, but no episode-level
alternative, choice, verified remedy, or meaning/action follow-up. This is a
verified acquisition boundary, not a failed analysis. The UAS respondent files
remain absent and registration-gated; no large respondent archive is retrieved
by default. The next qualifying health-cost result requires an authorized
same-unit source with the missing fields, while the broad program continues
through other lanes.

The forty-fourth rotation applies the storage-light event-compatibility rule
across the ten retained practical-exit routes. The [event qualification register](projects/us-customer-automation-recourse/data/end-to-end-event-qualification-register-2026-09-17.json)
finds zero routes with all of the required stages: dated trigger, alternative
or non-use choice, institutional response, verified protected or sacrificed
outcome, and later meaning/action or exit. The accompanying [finding](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-002.md)
records this as an acquisition/identification boundary. It advances the atlas
by preventing complaint response, access restoration, program exit, or market
movement from being promoted to practical recovery or household exit. No bulk
respondent file was downloaded; the next qualifying artifact remains one
lawful small same-case ledger or valid panel with the missing fields.

The forty-fifth rotation uses the retained SIPP slice for a subgroup reversal
in the material/time/work lane. The [subgroup-conditioned work-direction
record](records/us-sipp-resource-work-direction-subgroups-2024.json) and
[finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-045.md)
condition month-to-month earnings and hours direction on resource band plus
children or SNAP status. Hours remain comparatively stable, but low-resource
earnings composition differs across contexts and the high-resource pattern
converges. The result deepens the money/time/care interpretation without
promoting household composition or program status to a causal effect; remedy,
recovery, trust, political action, and exit remain open.

The forty-sixth rotation rechecks the consumer-remedy implementation lane
through the [Grubhub finding](findings/us-grubhub-platform-remedy-001.md).
The FTC now reports 640,038 checks or PayPal payments totaling more than
$23.8 million and gives recipients defined cash-in or acceptance windows.
This is stronger than a proposed remedy: aggregate distribution is observed,
while individual receipt, restored income/access, adequacy, durability,
continued use, switching, and exit remain open. It is a comparative
counterexample to treating a settlement design and a distributed payment as
the same evidence stage.

The forty-seventh rotation runs the [broad coverage control audit](data/us-broad-theme-end-to-end-coverage-audit-2026-09-17.json)
against the 14-theme matrix without acquiring new data. The audit records 14
Compared, 12 Reported, 5 Open, and 3 Inferred status tokens and identifies five
themes with an explicitly open same-unit end-to-end link. These are matrix
control counts, not population rates or completed causal arrows. The result
confirms that the next executable step is the authenticated PSID wave-file
gate and subsequent retention, missingness, and weight checks; the workspace
must not fetch the PSID archive before account access is available.

The forty-eighth rotation adds the [2025 SHED banking-substitution finding](projects/us-financial-intermediation/findings/us-financial-intermediation-003.md)
to the financial-access and consumer-recourse lanes. It records unequal
unbanked and overdraft exposure, nonbank transaction substitution, fraud loss
and recovery, provider contact, and reported bank switching from one official
2025 publication. These are distinct conditional surfaces, not a causal
account-to-loss sequence: the next missing fields are the dated account/case,
verified recovery, alternative quality, and reason for staying or leaving.

The forty-ninth rotation adds the [2025 SHED care and living-arrangements finding](projects/us-aging-care-strain/findings/us-aging-care-strain-003.md).
It makes multigenerational living, paid and unpaid childcare, childcare cost,
gendered caretaker roles, adult caregiving, and caregiving-related employment
status visible in one official population module. These are descriptive and
conditional surfaces, not a causal care-to-work or household-displacement
estimate; same-family triggers, alternatives, schedule control, recovery,
meaning, and political-action links remain open.

The fiftieth rotation adds the [2025 SHED employment and AI-control finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-030.md).
It places young-adult job-finding friction, layoffs, voluntary mobility,
workplace schedule organization, and education/control-stratified generative-AI
use on one official population surface. The pattern sharpens the link between
outside options and workplace control, but remains descriptive: causal AI
displacement, productivity, pay, household welfare, trust, and political
response remain open.

The fifty-first rotation extends the practical-exit comparison with the
[Doxo bill-payment record](records/us-ftc-doxo-bill-payment-hidden-fees-2026.json)
and [Grubhub remedy record](records/us-ftc-grubhub-multisided-remedy-2026.json).
These cases add reported search-route confusion, alleged payment friction,
aggregate remedy distribution, and prospective platform controls. They still
do not expose the affected unit's usable alternative, payment or income
outcome, remedy receipt, durability, trust, switching, or exit. The expanded
eight-route finding therefore strengthens the institutional-response surface
without closing the same-case practical-recovery arrow.

The fifty-second rotation adds two official disaster-recovery layers. The [EDA
economic-recovery outcomes layer](projects/us-repeat-energy-crises/gao-2026-eda-disaster-economic-recovery-outcomes-layer-v1.md)
tracks federal coordination, infrastructure awards, readiness, funding delay,
and the inability of current measures to validate broad economic outcomes. The
[disaster-assistance scams and information-trust layer](projects/us-repeat-energy-crises/gao-2026-disaster-assistance-scams-information-trust-layer-v1.md)
tracks verification, underreporting, education, and enforcement friction around
urgent aid. Together they extend the disaster chain from assistance delivery to
community capacity and consumer legitimacy, while preserving the open fields:
same-place counterfactuals, survivor or firm outcomes, warning comprehension,
verified loss or remedy, trust change, and later political action.

The fifty-third rotation adds the [GAO/USGS critical-minerals dependence
layer](projects/ai-work-control/gao-2026-critical-minerals-substitution-recycling-dependence-layer-v1.md).
It places import reliance, processing concentration, substitute performance,
recycling feedstock, and commercial maturity beneath battery, semiconductor,
defense, energy-storage, and consumer-electronics systems. It strengthens the
infrastructure/geopolitical lane while preserving the open stages: a dated
disruption or export-control event, firm redesign or production response,
local burden, supplier switching, and observed external leverage.

The fifty-fourth rotation adds the [CHIPS R&D capacity and governance
layer](projects/ai-work-control/gao-2026-chips-rd-capacity-governance-dependence-layer-v1.md).
It follows public semiconductor incentives from awards and disbursements
through milestones, workforce activity, R&D institutions, and statutory
alignment. It strengthens the work, firm, infrastructure, and geopolitical
lanes while preserving the open links to qualified output, worker retention,
local burden, customer supply, supplier switching, and reduced foreign
dependence.

The fifty-fifth rotation adds the [DOE transmission-needs and large-load
layer](projects/ai-work-control/doe-2026-transmission-needs-data-center-manufacturing-load-layer-v1.md).
It follows data-center, manufacturing, and electrification demand into
transmission congestion, planning, reliability, cost allocation, local burden,
and public participation. It strengthens the household-energy, infrastructure,
and state-capacity lanes while leaving actual customer rates, energized
capacity, land/water incidence, and political response to a region-hour-project
ledger.

The fifty-sixth rotation adds the [Census child-care challenges and work-
adaptation layer](projects/us-aging-care-strain/census-2025-childcare-challenges-work-adaptation-layer-v1.md).
It directly measures paid-care expense, adequacy problems, lost workdays, and
income-stratified adaptations including leave, reduced work, job exit, and
non-search. It strengthens the material/time/care lane while leaving provider
disruption, subsidy and employer access, wages, child wellbeing, and later
recovery open.

The next canonical trend additions extend this rotation without pooling their
source universes. The [institutional-presence and contested-inclusion trend]
(US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) keeps Muslim population, mosque,
representation, public-judgment, discrimination, and violence-association
surfaces as separate clocks; it strengthens the unequal-exposure and cultural-
legitimacy lane while leaving local treatment, access, safety, organizing, and
agenda-setting power open. The [distributed family-care trend]
(US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) keeps kinship care, childcare work
adaptation, unpaid adult care, and assisted-living financing distinct; it
strengthens the material/time/care lane while leaving family-level
alternatives, schedule control, benefit or respite receipt, remaining burden,
and later stability open. Both are canonical trend observations, not new
same-unit causal episodes. The subsequent [banking substitution trend]
(US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) adds income-conditioned account access,
nonbank substitution, fraud recovery, provider contact, and reported switching
as separate financial-power stages. The [care/living-arrangements trend]
(US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) adds multigenerational living, paid and
unpaid childcare, caretaker roles, and adult-care employment associations as a
second official care surface. Both retain their cross-sectional and
conditional boundaries. The [employment/AI-control trend]
(US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) then adds young-adult job-search
friction, labor mobility, schedule organization, education-stratified AI use,
and task-control differences as a distinct work/technology surface. It does
not establish displacement, productivity, bargaining power, or worker action.
The [material-to-political-friction trend](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md)
then separates capacity to act, institutional judgment, contact, and
collective action across the direct CCES panel comparisons and HTOPS surfaces;
the panel shows lower later action/contact after retrospective job-loss or
no-insurance status while favorable Congress approval is close or higher. It
does not establish a hardship-to-distrust or hardship-to-vote pathway. The [social-connection
trend](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) then separates loneliness,
support adequacy, contact frequency, and food insufficiency under material
pressure; it remains a cross-sectional, differently timed HTOPS surface rather
than a same-person help or recovery path.
The [cross-release material-pressure trend](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md)
then places social connection beside institution-specific confidence while
preserving March and July as separate cross-sectional releases. It adds a
cross-scale measurement bridge, not a pooled social-isolation or distrust
estimate.
The [HTOPS fraud-loss follow-up trend](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md)
then adds an exact same-respondent exposure-to-loss-to-later-context route.
It strengthens the distinction between exposure, realized burden, reporting,
reported recovery, and restored security, while leaving verified remedy,
durability, alternatives, trust change, switching, and exit open.
The [Rehman platform-remedy record](records/au-rehman-platform-remedy-2026.json)
then supplies an observed comparative remedy stage: deactivation, worker
application, voluntary reactivation, formal access restoration, and ordered
gross lost remuneration. It closes neither payment receipt nor net recovery,
alternative work, durability, recurrence protection, nor practical exit, so
it is remedy architecture and counterexample evidence rather than a
population estimate.
The [Hotak follow-up record](records/au-hotak-reactivation-continued-work-2025.json)
adds a distinct operational-return stage: more than 150 trips followed
voluntary reactivation before the formal order, while lost-pay quantum,
payment, net recovery, alternatives, durability, and exit remained open. This
separates work activity from financial restoration and unconstrained choice.
The [Amazon Flex refund record](records/us-ftc-amazon-flex-driver-tip-refunds-2026.json)
then adds the next remedy stage: the FTC reports aggregate payment distribution
and a live reissue route for uncashed checks. It advances beyond an obligation
or order without closing driver-level receipt, remaining loss, continued work,
household recovery, bargaining power, or exit.
The [MEPS friction route-direction record](records/us-meps-2024-friction-route-direction-comparison.json)
then rotates the program back to health: repeated-round denial or
prior-authorization reports are followed by more perceived-health worsening,
while employment transitions are comparatively close. It adds a weighted,
BRR-audited longitudinal boundary without closing claim timing, treatment,
appeal, remedy, payment, household recovery, trust, or exit.
The [SNAP administrative-access record](records/us-snap-administrative-access-2026.json)
then returns to public-system route design: study-specific work requirements,
flexible interviews, office access, age exemptions, and recertification
mechanisms alter participation or procedural denial without proving employment
or household-security gains. The evidence remains deliberately non-pooled and
leaves notice, effort, appeal, adequacy, remedy, trust, and action open.
The [Citibank servicing-remedy record](records/us-cfpb-citibank-student-loan-servicing-remedy-2017.json)
then adds a named financial-interface event: account-state and notice errors
could move cost into tax access, fees, capitalized interest, and payment
demands before an ordered restitution and control route. It leaves individual
receipt, adequacy, corrected account/tax position, credit, household recovery,
trust, switching, and exit open.
The [Apple PERM implementation record](records/us-doj-apple-perm-backpay-distribution-2026.json)
then adds a stronger completed-remedy stage: DOJ reports individualized
lost-income review, an exhausted $18.25 million back-pay fund, and qualifying
worker compensation, while recruitment controls and monitoring continue. It
still leaves claimant denominator, individual receipt, restored opportunity,
durable compliance, household recovery, trust, and exit open.

The next rotation adds the [Hims & Hers digital-health consumer-power finding](projects/us-customer-automation-recourse/findings/us-customer-automation-recourse-027.md).
The FTC, Utah, and California complaint alleges a combined privacy, recurring-
billing, refill, and cancellation interface; the FTC FOIA release adds 203
coded complaint records but is selected, heavily concentrated in one BBB
channel, and limited to administrative disposition labels. This expands the
consumer-recourse map into sensitive health-data and treatment-continuity
control while leaving account-level exposure, payment, medical outcome,
verified remedy, trust, switching, and practical exit open.

The following rotation adds the [Amazon advertising-auction finding](projects/us-local-business-place/findings/us-local-business-place-013.md).
The FTC and 22 states allege hidden Sponsored Products surcharges and a route
from marketplace visibility to seller cost and possible consumer pass-through.
The case is not adjudicated and provides no auction logs, seller margins,
product prices, purchases, returns, firm survival, or household denominator.
This adds a new firm-to-household distribution mechanism while preserving the
separate seller, product, and consumer clocks.

The next infrastructure rotation adds the [Virginia large-load governance finding](projects/ai-work-control/findings/ai-work-control-096.md).
The SCC record places reported Dominion load-drop events beside GS-5 demand and
contract rules and a modeled reduction in the typical residential Rider T1
increase. It strengthens the observable state-response stage while leaving
actual bills, facility exposure, reliability, public-cost recovery, local
burden, and legitimacy open.

The next household/public-capacity rotation adds the [energy/public-restoration finding](projects/us-repeat-energy-crises/findings/us-repeat-energy-crises-002.md).
EIA household consequences, LIHEAP reach/restoration aggregates, and a SIPP
following-month screen now sit together as a deliberately non-pooled route.
This makes sacrifice, public reach, immediate restoration, and durable recovery
distinct clocks; dated bills, receipt, reconnection, next-bill affordability,
repeat crisis, and later trust/action remain open.

The next state/geopolitical rotation adds the [capacity-realization finding](projects/ai-work-control/findings/ai-work-control-097.md).
Critical minerals, CHIPS awards, data-center/grid capacity, and defense
procurement now share a formal realization-stage comparison without being
pooled. Authorization, funding, milestones, operation, replaceability,
affected-actor response, and leverage remain separate clocks; the next test is
an identifier-bearing production-to-use and response ledger.

The capacity rotation now adds the [Taiwan semiconductor partial-realization record](records/us-commerce-taiwan-semiconductor-investment-2026.json).
TSMC Arizona supplies a first-fab production and workforce stage beside
investment, CHIPS, later-fab, packaging, childcare, and supplier commitments.
It strengthens the commitment-to-operation bridge without establishing output
yield, domestic ownership, replaceability, local burden, or geopolitical
leverage.

The next migration/cultural-meaning rotation adds the [mobility-meaning finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-036.md).
Pew's Latino survey places perceived family progress beside American-Dream
attainability, nativity, future children, and open-ended definitions of a good
life. This adds meaning and reference-group structure without treating survey
judgment as observed mobility, belonging, trust, or political action.

The next work/identity rotation adds the [working-class identity finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-037.md).
Pew's 2026 identity measure crosses income, education, party, financial stress,
and work type, showing why “working class” cannot serve as a hidden composite
class variable. The next test is a same-worker route from job quality and
respect through identity, attribution, voice, organizing, and political action.

The next legitimacy rotation adds the [institutional-legitimacy finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-038.md).
Gallup's near-historic-low average confidence coexists with a sharp small-
business/large-technology contrast and partisan institution judgments. This
keeps capability, dependence, confidence, performance, use, contestation, and
action on separate clocks; the next test is a named encounter-to-response
ledger.

The next civic-portfolio rotation adds the [public-life engagement finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-039.md).
Pew's four engagement groups separate activity portfolios from generalized
trust: high political interest varies widely, while federal trust stays low and
perceived news unfairness stays high. The next test is a same-respondent route
through time/resources, source exposure, activity, trust, institutional
response, and later action or withdrawal.

The next household-security rotation adds the [Census income/poverty/insurance finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-040.md).
The 2025 CPS ASEC release puts median income, official poverty, SPM poverty,
and full-year uninsured status on separate clocks. This strengthens the national
baseline while leaving same-household disposable room, care access, adaptation,
trust, action, and recovery open.

The next market-activity rotation adds the [Census retail-demand boundary finding](projects/us-cost-trust-politics/findings/us-cost-trust-politics-041.md).
The August 2026 establishment-sales release records nominal retail and
food-services growth and a contemporaneous revision, but no price-adjusted
quantity, household incidence, payment/debt route, firm margin, local access,
or survival outcome. It extends the household-security baseline without
turning sales into a welfare or confidence measure.

The next consumer-recourse rotation promotes the [VRURC implementation finding](projects/us-marketplace-product-safety/findings/us-product-recall-response-003.md).
One recall key joins a dated hazard notice and replacement offer to a later
firm-reported correction snapshot, while the product denominators differ and
consumer receipt, safe restoration, residual cost, trust, and switching remain
unobserved. This closes an implementation-stage bridge without converting
correction progress into household recovery.

The next health-cost rotation adds the [MEPS dated medical-event record](records/us-meps-dated-medical-event-household-work-2024.json).
The local event spine now preserves month ordering across prescription, office,
emergency-room, and inpatient events and carries selected payment, care-delay,
bill, debt, collection, employment, and later-round context. It advances the
event-to-household/work arrow while leaving initiating need, alternatives,
claim-level obligation, treatment continuity, remedy, verified recovery, and
later meaning/action open.
The [availability-to-use conversion trend](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md)
then adds a cross-domain interface rule: nominal capacity is not a usable
option until price, time, information, accessibility, schedule, reliability,
and alternatives permit completed use and a protected outcome. It remains a
non-pooled mechanism synthesis, not a universal conversion rate.

The current worker-control follow-up adds two storage-light official-source
audits without counting them as a new population estimate. The [Elegant AI
recruiting settlement audit](projects/ai-work-control/elegant-settlement-compliance-follow-up-audit-2026-09-17.md)
rechecks a named federal settlement and finds enforceable penalty, notice,
training, policy, inquiry, and cure provisions but no public confirmation of
implementation, applicant restoration, or later worker behavior. The [NYC AEDT
follow-up audit](projects/ai-work-control/nyc-aedt-enforcement-follow-up-acquisition-audit-2026-09-17.md)
finds a bias-audit, notice, complaint, and referral route but no public named
worker outcome. Together they strengthen the institutional contestability
stage of the AI/work lane while leaving tool exposure, notice receipt,
appeal/override, correction, compensation, durable compliance, trust,
bargaining, and exit open.
The [Elegant AI-recruiting trend](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md) now
promotes that bounded U.S. event into the canonical register: AI-assisted
recruiting can enter a named exclusion and produce enforceable prospective
controls, but settlement terms are not proof of payment, completed monitoring,
restored opportunity, durable compliance, or later worker action.

The latest broad-program pass adds a detailed [material-pressure to
meaning/action route](../REVIEW-PACKET_CURRENT-THEMES_V1.md#route-13-material-pressure-becomes-meaning-and-political-action)
to the main review packet. It places the retained HTOPS, CCES, CES
medical-affordability, and ANES designs side by side, preserving their
different respondent universes, clocks, and action definitions. The CES
comparison shows that turnout, official contact, protest, and attribution can
move differently across module years; the ANES panel supplies temporal order
but remains confounded by identity and prior judgment. This strengthens the
meaning/action bridge without claiming a universal hardship-to-backlash path.

The current-themes packet is now also published as a [reader-facing HTML
route](../site/review-packet-current-themes.html), linked from the review guide
and current-status page. This makes the detailed writeups reviewable without
requiring repository navigation. The publication gate passes, but the central
same-unit gap remains: no retained record follows a dated material event
through attribution, action, remedy, recovery, and later exit or trust.

The [same-case episode availability audit](broad-same-case-episode-availability-audit-v1.md)
now makes that gap quantitative across 17 retained episode or remedy surfaces.
Fourteen surfaces observe a dated event or exposure, ten observe a responsible
actor, and fourteen observe an institutional response; only one observes an
alternative or non-use outcome, while none observes a verified remedy, meaning
or trust/action endpoint, and none closes recovery, persistence, or exit. Eleven
surfaces have partial remedy information and eleven have partial effort or
trade-off information, but these partial stages do not form a common
denominator. The [ranked next-episode selection](broad-next-episode-selection-v1.md)
therefore retains a strict promotion gate: a future pass must add both an
episode-level alternative/non-use field and a receipt or outcome follow-up,
with denominators, missingness, and the distinction between institutional
response and lived outcome preserved. This is a measurement result and an
acquisition boundary, not a claim that the broad program lacks meaningful
context; no raw data were downloaded for this checkpoint.

## Active research lanes

These lanes rotate. The next available source does not redefine the program.

1. **Material, time, care, and recovery:** acquire and audit PSID 2019/2021/2023 or an equivalent same-unit design; test resources, work, unpaid care, schedule/time pressure, health, wellbeing, retention, and missingness.
2. **Consumer and public-system episodes:** obtain a same-case or valid panel path from contact or notice through effort, decision, remedy, later security, trust, and exit.
3. **Place, firm, and infrastructure incidence:** match capacity or firm decisions to local access, ownership, costs, quality, worker/customer outcomes, and practical replaceability.
4. **Meaning and political action:** use repeated respondents or a defined event to separate exposure, attribution, identity, trust, civic action, turnout, and vote.
5. **Geopolitical/state leverage:** verify realized capacity, ownership, alternatives, switching, and an observed state or external response before claiming leverage.

## Next executable checkpoint

The next substantive checkpoint is the storage-light event-compatibility gate,
followed by the PSID acquisition gate when account access is available. The
retained ten-route qualification register currently finds zero routes that
contain all required stages: dated trigger, alternative or non-use choice,
institutional response, verified protected or sacrificed outcome, and later
meaning/action or exit. The next event pass must identify one lawful small
same-unit route with those fields or publish the precise missing field and
rotate to a retained subgroup/place reversal; it must not promote a complaint
response, access restoration, program exit, or market movement to practical
recovery.

After that event gate, the PSID acquisition gate is:

- obtain the 2019, 2021, and 2023 main family and individual files when account
  access is available;
- verify the mapped F1, BC, health, wellbeing, family-composition, and weight
  fields against each released codebook;
- construct person/family retention and missingness tables before pooling;
- preserve survey mode, universes, status codes, weights, and the valid
  variance method;
- publish a bounded many-family comparison only after these checks pass; and
- if the all-adult repeated-time requirement fails, pair PSID with a defined
  ATUS/time supplement or retain the arrow as an acquisition gap.

Until then, the existing SHED, ATUS published tables, SIPP, and other layers
remain valid distributional or contextual evidence. They must not be silently
joined into a same-family causal result.

## Promotion rule for every new result

Before adding a result to the atlas, record:

1. the source and stable link;
2. the unit, date, geography, denominator, universe, weight, and method;
3. the directly measured claim and its evidence location;
4. the comparison group, subgroup distribution, missingness, and uncertainty;
5. the mechanism arrow and whether it is observed, reported, estimated,
   compared, inferred, or open;
6. at least one counterexample or boundary condition;
7. the actor with control over the next decision and where cost, risk, data,
   time, or power may move; and
8. the next test that could weaken or connect the result.

No result is promoted merely because multiple adjacent sources point in the
same direction.

## Session handoff rule

At the end of each research cycle, update the authoritative record that was
changed, then leave three things explicit:

- what new evidence was added;
- which arrow remains open or was weakened; and
- the next acquisition or comparison that advances the full program.

If an external source is inaccessible, record the exact access condition and
continue with a safe adjacent lane. Do not restart the program around a more
convenient dataset, and do not mark the long-term objective complete because
an intermediate checkpoint is green.

Related controls: [current-status audit](US-BROAD-CURRENT-STATUS-AUDIT_V1.md),
[broad research pass](US-BROAD-RESEARCH-PASS_V1.md), [next-pass queue](US-BROAD-NEXT-PASS-QUEUE_V1.md),
and [recovery brief](../END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md).

The [GAO disability health-care accessibility and oversight layer](projects/us-aging-care-strain/gao-2026-disability-healthcare-accessibility-layer-v1.md)
adds the institutional-usability stage: disability-related needs can encounter
equipment, sensory, communication, digital, bias, and oversight barriers after
coverage or capacity exists. It preserves the open arrows from accommodation
to completed care, health/work consequence, correction, trust, and exit.

The [GAO working adults and safety-net layer](projects/us-safety-net-access/gao-2026-working-adults-medicaid-snap-employer-reliance-layer-v1.md)
adds a labor–public-benefit bridge: millions of adults worked while connected
to Medicaid or SNAP, with private-sector and occupational concentration plus
selected-state repeated employers. It keeps open the arrows from hours, wages,
benefits, and eligibility continuity to household security, worker mobility,
and employer responsibility.

The [GAO disability workforce-program access layer](projects/us-safety-net-access/gao-2026-disability-workforce-program-access-layer-v1.md)
adds public employment infrastructure between disability-related need and labor
market opportunity. It preserves the open links from voluntary disclosure and
accommodation to completed service, placement, retention, household security,
and local oversight correction.

The [GAO airport transit availability and adoption layer](projects/us-transport-mobility/gao-2026-airport-transit-availability-adoption-layer-v1.md)
adds place-level transportation usability between infrastructure provision and
passenger or worker mobility. It preserves open links from route availability
to time, cost, accessibility, shift fit, completed trips, congestion, and
demand-management outcomes.

The [GAO telework, travel, real-estate, and planning layer](projects/us-transport-mobility/gao-2026-telework-travel-real-estate-planning-layer-v1.md)
adds changed work geography between worker arrangements and collective place
outcomes. It preserves open links from telework to trip timing, transit finance,
vehicle use, real-estate demand, investment, distributional burden, and public
response.

The [GAO assisted-living spending and Medicaid-coverage layer](projects/us-aging-care-strain/gao-2026-assisted-living-spending-medicaid-coverage-layer-v1.md)
adds a mixed housing, health, and daily-care stage between need and household
security. It preserves open links from federal/state coverage and spending to
slots, room/board, provider capacity, family labor, resident safety, and later
setting choice.

The [GAO kinship families and intergenerational care-support layer](projects/us-aging-care-strain/gao-2026-kinship-families-intergenerational-care-support-layer-v1.md)
adds family recomposition between parental absence and child/household
security. It preserves open links from caregiver capacity and legal status to
housing, work, benefits, childcare, health, school continuity, respite, and
later placement stability.

The [Pew 2026 electorate racial and ethnic composition layer](projects/us-cost-trust-politics/pew-2026-electorate-racial-ethnic-composition-layer-v1.md)
adds demographic structure between population change and political voice. It
preserves open links from age, citizenship, nativity, and geography to
registration, participation, identity meaning, coalition, representation, and
policy response.

The [Pew 2026 U.S. global-role and international-reception layer](projects/ai-work-control/pew-2026-us-global-role-domestic-partisan-international-comparison-layer-v1.md)
adds external audiences and domestic partisan meaning between material state
capacity and geopolitical consequence. It preserves open links from policy
events to foreign trust, alliance cooperation, cultural/market reception,
domestic consent, and later strategic response.

The [Pew 2025 religious affiliation and cultural identity layer](projects/us-cost-trust-politics/pew-2025-religious-affiliation-switching-cultural-identity-layer-v1.md)
adds identity and community institutions between family transmission and public
meaning. It preserves open links from affiliation or switching to practice,
belonging, service, political interpretation, civic action, and later
institutional continuity.

The [Pew 2026 racial diversity and workplace meaning layer](projects/us-cost-trust-politics/pew-2026-racial-diversity-cultural-workplace-meaning-layer-v1.md)
adds the interpretive stage between population diversity and organizational
legitimacy. It preserves open links from attitudes to actual workplace
practice, fairness, voice, trust, civic action, and distributional outcome.

The [Pew 2026 smartphone time, self-control, and well-being layer](projects/us-digital-habits-attention/pew-2026-smartphone-time-control-wellbeing-layer-v1.md)
adds a consumer-attention stage between device availability and perceived
well-being. It preserves open links from habitual use to utility, displacement,
self-regulation, privacy, switching, measured outcomes, and later social or
political action.

The [cross-source cultural-meaning synthesis](projects/us-cost-trust-politics/cultural-meaning-contested-legitimacy-cross-source-synthesis-v1.md)
records a cross-theme synthesis rather than a new survey: common objects and
conditions can carry divergent utility, cost, identity, fairness, and authority
meanings. It preserves the need for a same-unit episode matrix before claiming
behavioral or political conversion.

The [Gallup 2026 moral values and government-role layer](projects/us-cost-trust-politics/gallup-2026-moral-values-government-role-cultural-polarization-layer-v1.md)
adds a cultural-mood stage between perceived national conditions and public
authority. It preserves open links from moral judgment to attribution, religious
meaning, issue behavior, policy support, trust, and political action.

The [cultural-meaning episode matrix](projects/us-cost-trust-politics/cultural-meaning-episode-matrix-v1.md)
turns the broad cultural synthesis into a row-level control. It preserves the
distinction between partial same-unit bridges and a completed end-to-end route,
and records the next acquisition schema needed to close adjacent stages.

The [Pew 2025 neighbor trust and mutual-aid layer](projects/us-cost-trust-politics/pew-2025-neighbor-trust-help-community-capacity-layer-v1.md)
adds an informal social-institution stage between place and household
protection. It preserves open links from local trust to requested and delivered
help, reciprocal burden, formal services, recovery, mobility, and later action.

The [formal/informal support-capacity synthesis](projects/us-cost-trust-politics/formal-informal-support-capacity-cross-source-synthesis-v1.md)
adds a protection-portfolio stage across family, neighbor, community, market,
and public routes. It preserves the distinction between potential availability,
requested help, delivered aid, provider burden, adequacy, continuity, and later
trust or exit.

The [Census HTOPS 2026 social-connectedness acquisition gate](projects/us-cost-trust-politics/census-2026-htops-social-connectedness-community-engagement-acquisition-gate-v1.md)
adds a possible same-release household/social bridge. It preserves the need to
verify corrected weights, compatible units, table denominators, uncertainty,
and lawful linkage before connecting material pressure to social or cultural
participation.

The next household-energy rotation adds the [SIPP utility-to-work finding](projects/us-household-calendar-integration/findings/us-household-calendar-integration-028.md).
Same-person month-to-next-month pairs place utility-payment difficulty and
energy-assistance status beside earnings and hours movement with Fay–BRR
uncertainty. This adds timing discipline to the energy/work arrow while leaving
the exact bill or shutoff, assistance receipt, desired hours, provider/employer
response, recovery, and later action unobserved.

The next food-security rotation adds the [SIPP utility/food layer](projects/us-household-calendar-integration/sipp-energy-assistance-food-following-layer-v1.md).
Adjacent-month person records place utility difficulty and energy assistance
beside following food insecurity and severity, including a targeted joint
cell. The layer strengthens the material-to-protection route while leaving
benefit timing, adequacy, recovery, repeat crisis, trust, and action open.

The next recourse rotation adds the [FTC remedy-distribution boundary](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md).
First American small-business checks and Credit Karma refunds make aggregate
distribution and reissue visible across payment processing and credit
marketing, while individual receipt, restored opportunity, alternatives,
survival, trust, and exit remain open. The comparison extends the remedy
implementation lane without pooling unlike claimant populations.

The next infrastructure/geopolitical rotation adds the [bulk-power security trend](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md).
Executive Order 14421 and DOE's implementation RFI make federal authority,
security risk surfaces, and stakeholder-input categories visible, but not
covered-equipment determinations, replacement, cost, reliability, household
service, or geopolitical leverage. The route preserves policy intent,
implementation, essential-service incidence, and external consequence as
separate stages.

The next disaster-recovery rotation adds the [firm/customer/resident recovery synthesis](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md).
The causal emergency-loan design, Harvey firm/customer case, and Gulf Coast
resident survey expose different recovery currencies—firm survival and jobs,
customer distance and modeled welfare, and disruption, aid, and legitimacy.
They are not pooled into a universal disaster effect; worker household
security, owner recovery, affordable services, verified aid causality, and
political response remain open.
