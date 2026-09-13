# US broad program next-pass queue v1

**Checked:** 2026-09-13
**Purpose:** keep breadth across the 14-theme program while choosing depth that can change a claim
**Status:** execution queue; not a claim that any open link has been established

This queue is the handoff from the current evidence map to the next empirical
passes. Every pass must identify the unit, date, geography, denominator,
missingness, uncertainty, and arrow status. A source can deepen one arrow
without completing the societal chain.

## Active continuation checkpoint

The program has completed broad anchor passes across all 14 themes and has
recently added depth in four rotating lanes: household adaptation and care;
time, work, and life-stage distribution; local business and service capacity;
and migration, place, and infrastructure/state dependence. These passes are
cross-source comparisons and bounded same-respondent analyses where the data
permit. They do not yet establish a single population-wide causal chain.

The next active pass is **material/time/care linkage**, documented in the
[acquisition plan](projects/us-household-calendar-integration/material-time-care-linkage-acquisition-plan-v1.md)
and now operationalized by the [PSID extract specification](projects/us-household-calendar-integration/psid-material-time-care-extract-spec-v1.md).
Its purpose is to
identify which missing variables prevent the existing evidence from becoming
an end-to-end societal result:

1. a dated bill, price, care need, rule, or work change;
2. the person or household's alternatives and schedule control;
3. the money and time response, including paid or unpaid substitution;
4. the protected and sacrificed outcomes; and
5. recovery, trust, collective action, or exit at a defined follow-up.

Until a same-unit or valid matched design supplies those fields, the safe
output is a measured distribution, an explicit comparison, or an acquisition
gap—not a claim that one cost caused one cultural or political outcome.

The care-time subpass now has an official published-table baseline in the
[ATUS 2023–2024 care/work layer](projects/us-aging-care-strain/atus-2023-2024-published-care-work-layer-v1.md).
That baseline advances population scale and time intensity, but does not
replace the microdata gate for same-respondent schedule, care, health, and
wellbeing comparisons.

The immediate PSID gate is now concrete: obtain the 2019, 2021, and 2023 main
files, verify the mapped fields and their universes across waves, measure
person/family retention and missingness, preserve weights, and then publish
the first many-family comparison. No result should be promoted before that
gate is passed.

| Theme | Current anchor | Next depth pass | Required counterexample | Durable output |
|---|---|---|---|---|
| 1. Household room and consumption | SHED panel, CE income-quintile spending, food security, SIPP, prices | Follow a dated price/payment event through spending, food, debt, health, and recovery in the same unit | Pressure rises but no other need is displaced because a buffer or substitute protects the unit | Event-ledger extract plus distribution table |
| 2. Time as hidden price | ATUS, NHTS, caregiving, multiple-job, participation-friction layers | Measure waiting, travel, care, paperwork, and schedule control beside the money response | A high-time-cost route does not reduce work, care, rest, or civic availability | Time-displacement comparison |
| 3. Consumer power and recourse | CFPB process/product layers, complaint records, platform and repair findings | Trace first contact, effort, response, verified remedy, abandonment, switching, and later trust | A difficult route still produces a timely verified remedy and equal exit | Same-case recourse ledger |
| 4. Platforms, data, and attention | Pew source ecosystems, platform/data/agency layer, privacy and review findings | Compare the same issue across source environments, measuring encounter, interpretation, sharing, and action separately | Exposure differs but belief/action does not, or users retain practical inspection and exit | Respondent/source measurement table |
| 5. Work, control, and bargaining | AI work-control cases, SIPP work transitions, job-lock and employer records | Pair a tool, benefit, or schedule change with pay, hours, discretion, health, worker voice, and exit | Productivity or benefit change occurs without reduced control or bargaining room | Worker-event comparison |
| 6. Care, health, and social reproduction | SHED 2024/2025 care layers, care/work split, ATUS plan, medical-cost research | Follow a recurring care need through paid/unpaid labor, work, food/housing, health, and recipient outcome | Care remains high while work, health, and recipient safety remain stable through real support | Same-family longitudinal design or explicit acquisition gap |
| 7. Housing, place, and mobility | Insurance, housing, energy, NHTS, CBP, HRSA, migration/place profiles | Match place risk and local capacity to travel, price, repair, service use, move/stay, and work | Low nominal capacity is offset by neighboring access, public provision, or affordable mobility | Matched-place panel |
| 8. Unequal exposure and status | SIPP intersectional Fay-BRR layers, SHED panels, USDA, ATUS, migration | Estimate joint distributions of cash, time, support, rights, access, and exit rather than one demographic penalty | A high-exposure group retains options through an observed institution or social network | Distribution and uncertainty register |
| 9. Trust, identity, and cultural meaning | ANES trust/meaning, Pew source trust, CFPB cultural themes, migration meaning design | Measure attribution, dignity, belonging, blame, legitimacy, and norm change after a defined encounter | Hardship occurs without distrust, or trust changes without the predicted material exposure | Meaning/action instrument |
| 10. Public systems and policy feedback | SIPP SNAP transitions/reasons/Fay-BRR, administrative-burden and event-ledger designs | Follow notice, effort, receipt, interruption, remedy, security, interpretation, and later action | Exit follows improved security or a low-burden route yields no material loss | Same-episode public-system ledger |
| 11. Political judgment and collective action | ANES worry/judgment/trust/vote, CPS participation friction, Pew engagement styles | Use repeated respondents or a policy event to separate exposure, attribution, trust, civic action, and vote | Pressure does not change judgment; judgment changes without pressure; trust changes without action | Longitudinal political instrument |
| 12. Firm, sector, and market power | BFS, BDS, CBP, establishment scale, firm/market-power layer, CFPB | Follow one firm or sector decision across customer, worker, owner, place, and public-system outcomes | Similar decision leaves terms unchanged because alternatives or worker/customer power are real | Matched firm-event record |
| 13. Infrastructure, technology, and dependency | AI capacity/ownership cases, state-leverage ledger, domestic-capacity bridge | Verify operational capacity, ownership, local incidence, energy/water burden, interoperability, and switching | Capacity rises with local learning, public inspection, and provider replaceability | Realization/control ledger |
| 14. Geopolitical and state consequences | Tariff/price, energy, finance, migration, and AI state-leverage layers | Trace domestic capacity or dependence to an observed state choice, external response, alliance, or leverage change | Domestic dependence does not alter strategic choice, or capability is replaceable without external concession | State-leverage case comparison |

## Sequencing rule

Run the next passes in four rotating lanes so breadth is preserved:

1. **Material and time:** themes 1, 2, 6, and 8;
2. **Consumer, platform, and work power:** themes 3, 4, 5, and 12;
3. **Place, public systems, and politics:** themes 7, 10, and 11;
4. **Meaning, infrastructure, and state consequences:** themes 9, 13, and 14.

After each lane produces one depth artifact, return to the widest lane with
the fewest measured arrows. Do not add a new narrative packet merely because
an existing open link is difficult; record the acquisition or identification
gap and test a counterexample instead.

## Promotion rule

A provisional societal trend may be strengthened only when the next pass adds
at least one of the following: a same-unit or valid matched design, a second
time period, a subgroup or place conditioning check, design-based uncertainty,
a verified institutional outcome, or a measured reversal/counterexample. A
cross-source alignment without one of these remains context, not a completed
arrow.

## Relationship to the program

This queue operationalizes the [14-theme inventory](US-BROAD-THEME-INVENTORY_V1.md),
the [coverage matrix](US-BROAD-THEME-COVERAGE-MATRIX_V1.md), the [trend register](US-PROVISIONAL-SOCIETAL-TRENDS_V1.md),
and the [broad trend-extraction protocol](US-BROAD-TREND-EXTRACTION-PROTOCOL_V1.md).
The [recovery brief](../END_TO_END_PROGRAM_RECOVERY_BRIEF_V1.md) remains the
canonical end-to-end objective.
