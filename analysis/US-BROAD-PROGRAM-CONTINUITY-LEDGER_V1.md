# US broad program continuity ledger v1

**Checked:** 2026-09-15  
**Status:** active long-term program control record  
**Scope:** the complete 14-theme Cultural, Social, and Geopolitical Theme
Mining program

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
| Cross-source map | Five priority bridges plus broader theme links | [Evidence matrix](US-BROAD-EVIDENCE-MATRIX_V1.md), [theme atlas](us-theme-atlas.md) |
| Source coverage | 103 project packets; source-family coverage is indexed | [Source coverage](us-source-coverage.md), [source registry](../manifests/source-registry.json) |
| Source-registry coverage | 114 registered source entries; all 114 have analysis-domain references, 106 cite the registered landing URL exactly, and the reverse audit tracks observed domains outside registered families | [Source-registry coverage audit](US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.md), `audit_source_registry_coverage.py` |
| Trend registry | 234 machine-readable records; 902 observations | [Trend-observation registry](us-trend-observations.md), `validate_trend_observation_records.py` |
| Findings | Domain findings plus a program-level long-form finding are generated as Markdown and HTML and parity-checked where the matched-evidence contract applies | [Matched-evidence index](us-matched-evidence-index.md), [program-level finding](findings/us-broad-program-unequal-optionality-path-001.md), `validate_us_finding_parity.py` |
| Evidence discipline | Units, dates, geography, denominators, methods, limits, counterexamples, and open arrows are required | [Trend protocol](US-BROAD-TREND-EXTRACTION-PROTOCOL_V1.md) |
| Link integrity | Relative Markdown references are checked across the workspace | `validate_local_markdown_links.py` |
| Source-record integrity | Project source-search records must carry date, geography, status, question, and linked source metadata | `validate_source_search_records.py` |
| Trend-record integrity | Recurring trend observations must preserve period, denominator, method, uncertainty, subgroup, counterinterpretation, source URL, and retrieval hash | `validate_trend_observation_records.py` |
| Trend metadata depth | Required fields are complete across all 234 records/902 observations; optional related-source and reproduction-audit context is reported separately | [Trend metadata coverage audit](US-TREND-METADATA-COVERAGE-AUDIT_V1.md), `audit_trend_metadata_coverage.py` |
| Trend publication | Validated trend records have generated Markdown and HTML registry editions | [Trend-observation registry](../site/us-trend-observations.html), `build_us_trend_observation_registry.py` |
| Cross-source synthesis | The current evidence is periodically read across the full material-to-state chain without merging incompatible units | [Cross-source trend synthesis](US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md) |
| Recurrent-source freshness | Official recurring releases, next checks, revision rules, and access-gated dependencies are tracked separately from findings | [Vintage watchlist](US-RECURRENT-SOURCE-VINTAGE-WATCHLIST_V1.md) |
| Trend-to-atlas linkage | Every machine-readable trend/case record is tagged to validated atlas umbrella themes | `theme_ids` in trend schema and [published registry](../site/us-trend-observations.html) |
| Theme breadth control | Trend records are grouped by umbrella theme and missing-record themes are surfaced | [Trend-theme coverage](../site/us-trend-theme-coverage.html), `build_us_trend_theme_coverage.py` |
| Control synchronization | Registry, theme coverage, source-packet count, HTML edition, and this ledger are checked against current source files | `validate_program_control_sync.py` |
| Active depth lane | Material/time/care linkage across many families or a valid matched design | [Next-pass queue](US-BROAD-NEXT-PASS-QUEUE_V1.md) |
| Hard acquisition dependency | PSID main waves and/or an equivalent same-unit event design | [PSID extract specification](projects/us-household-calendar-integration/psid-material-time-care-extract-spec-v1.md), [wave-file audit protocol](projects/us-household-calendar-integration/psid-wave-file-audit-protocol-v1.md) |

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

The PSID access gate was rechecked on 2026-09-14: the official package routes
remain account-controlled and no target microdata files are present locally.
The available SIPP household-selection diagnostic was tightened with a hashed
2025 schema scan showing `WPFINWGT` as the only weight-related variable in the
5,203-variable surface; one-record household results therefore remain
sensitivity diagnostics rather than official household prevalence estimates.

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

The paired [IMF Financial Access Survey provider-side audit](projects/us-financial-intermediation/imf-fas-provider-side-access-audit-2026-09-15.md)
now separates annual administrative/provider capacity from Findex's adult
reports. A public SDMX query returned and preserved 566 US rows for 2020–2024,
including provider counts, branch density, and household deposit/loan ratios.
The official 2025 release also describes 163 reporting economies and 121
series through 2024. The new US result is a provider-side measurement, not a
household welfare or digital-substitution estimate; the next test is to join it
carefully to user terms, place access, remedy, and household outcomes.

## Active research lanes

These lanes rotate. The next available source does not redefine the program.

1. **Material, time, care, and recovery:** acquire and audit PSID 2019/2021/2023 or an equivalent same-unit design; test resources, work, unpaid care, schedule/time pressure, health, wellbeing, retention, and missingness.
2. **Consumer and public-system episodes:** obtain a same-case or valid panel path from contact or notice through effort, decision, remedy, later security, trust, and exit.
3. **Place, firm, and infrastructure incidence:** match capacity or firm decisions to local access, ownership, costs, quality, worker/customer outcomes, and practical replaceability.
4. **Meaning and political action:** use repeated respondents or a defined event to separate exposure, attribution, identity, trust, civic action, turnout, and vote.
5. **Geopolitical/state leverage:** verify realized capacity, ownership, alternatives, switching, and an observed state or external response before claiming leverage.

## Next executable checkpoint

The next substantive checkpoint is the PSID acquisition gate:

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
