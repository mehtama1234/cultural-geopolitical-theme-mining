# Project: US safety-net access, work rules, and the price of help

## Question

When public help is meant to support food or household stability, what makes people lose it: higher income, a rule, an office closing, or the work of proving eligibility?

## Short first pass

Use USDA for food outcomes, NBER for causal tests of work requirements and office access, and Census or state records for place comparisons. Separate leaving a program from finding a job. A program can lose participants without increasing work.

## Possible connection

Food insecurity is not only a household-income story. It may also reflect whether a person can reach, keep, or renew help. This connects the food path to work and political trust without assuming that public assistance always solves the need.

## Decision rule

Move on after a causal participation result, one measured place or administrative barrier, and a counterpoint about work, cost or self-selection.

## Matched evidence pass

The first matched check is [A benefit can be lost without the need going away](../../findings/us-safety-net-access-matched-evidence-001.md), with its [HTML reading page](../../../site/us-safety-net-access-matched-evidence-001.html) and [claims ledger](claims-ledger-v1.md). It confirms access and participation effects while leaving same-household food, work, debt, health, and trust effects open.

The [administrative-burden and access layer](administrative-burden-access-layer-v1.md) records the causal evidence separately: work-rule exits without an employment response, parent disenrollment through administrative burden, and participation changes after office closure. It does not treat program exit as work success or participation as food security.

The [SIPP SNAP transition Fay-BRR uncertainty layer](sipp-snap-transition-fay-brr-layer-v1.md)
adds design-based standard errors and approximate intervals to the adjacent-
month transition shares. It improves uncertainty around the transition
distribution without changing the limits: the same person-month records still
do not identify notice, effort, benefit amount, reason, food/work outcomes, or
political response.

The resulting [bounded finding](findings/us-safety-net-access-007.md) shows that
SNAP entry and especially exit often sit beside a lower monthly income-to-poverty
ratio, person earnings often move around the transition, and job count is usually
unchanged in the smaller valid universe. It keeps household resources, person
earnings, hours, work quality, notice, effort, remedy, trust, and action as
separate stages rather than treating exit as “back to work.”

The [annual child-care context finding](findings/us-safety-net-access-008.md)
adds a careful boundary: stable SNAP-state groups show different annual paid
care, assistance, and work-prevention routes, but adjacent entry/exit cells are
too sparse for promoted care-transition estimates.

The [following-month context finding](findings/us-safety-net-access-009.md)
extends the backbone to three-month sequences: resources often continue to
decline after entry or exit while job count and hours are usually unchanged,
and earnings move in both directions. This remains descriptive until notice,
effort, benefit timing, remedy, and recovery are observed in the same episode.

The [route-to-security synthesis](findings/us-safety-net-access-010.md) now
connects the NBER administrative route studies to the SIPP following sequence
and keeps the unretrieved WBNS public-use file as an explicit acquisition gate.

The [SIPP SNAP transition context Fay-BRR layer](sipp-snap-transition-context-fay-brr-layer-v1.md)
adds the same uncertainty treatment to resource-ratio and job-count changes
around entry and exit. It finds lower resource ratios around 76.37% of valid
exits and 58.57% of valid entries, while keeping the smaller job denominators
and non-causal interpretation visible.

The [SIPP SNAP transition reason Fay-BRR layer](sipp-snap-transition-reason-fay-brr-layer-v1.md)
adds uncertainty to the recorded reason categories. It finds job loss or
reduced wages as the largest classified entry category (30.10%, SE 3.94 pp)
and “other” as the largest classified exit category (49.53%, SE 4.34 pp),
while preserving the central limitation that valid reasons cover only about
half of observed transitions.

The detailed [reason finding](findings/us-safety-net-access-011.md) and
[reproduction audit](sipp-snap-transition-reasons-reproduction-audit-2026-09-14.json)
publish the two classified universes, the 240-replicate Fay–BRR intervals, and
the unclassified transition gap. The reason layer improves mechanism
description; it does not establish a dated administrative episode or causal
program effect.

The new [buffer-and-credit bridge](findings/us-safety-net-access-012.md) places
those public-system transitions inside the wider household financial
constraint documented by the 2025 Federal Reserve SHED and linked credit
records. It keeps the SIPP person-month, SHED adult, linked-credit, and NBER
administrative units separate. The bridge closes no same-person route-to-credit,
food, trust, or political-action arrow; it specifies the next event-ledger
fields required to test them.

The follow-on [route-and-buffer synthesis](findings/us-safety-net-access-013.md)
adds the WBNS lived-route and charitable-food layers to that bridge. It shows
how public receipt, interruption, cash/credit coping, and supplemental food can
occupy one broader safety-net pathway while preserving every source's unit,
denominator, and cross-sectional or retrospective boundary. It does not claim
that any one household followed the full sequence.

The [SNAP reason × following-food-security finding](findings/us-safety-net-access-015.md)
adds `RFOODS` to the adjacent-month reason layer. Job-loss and income-loss
entry, disability and family routes, and several exit routes show distinct but
uncertain following food-security profiles. Receipt entry or exit still does
not establish a benefit effect, food recovery, remedy, or later trust/action.

The next measurement instrument is the [safety-net event ledger](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md), which records the same program episode from notice and effort through benefit interruption, household outcomes, interpretation, and public response.

The [same-episode event-ledger design](same-episode-event-ledger-design-v1.md)
turns that instrument into a population study: many people, places, channels,
and program episodes are stratified and compared, so the public-system bridge
does not collapse into one household story.

The [USDA FY2025 current-context layer](usda-snap-fy2025-current-context-layer-v1.md)
adds the official program-scale, state-range, household-composition, benefit-
distribution, and food-security research context. It is kept separate from
the causal administrative-route studies and the SIPP person-month estimates.
The companion [state participation distribution layer](usda-snap-fy2025-state-participation-layer-v1.md)
preserves all 50 states and DC from the USDA chart-data workbook and publishes
descriptive distribution summaries. A need/eligibility/administration-matched
state comparison remains open.

The [state participation and ACS crosswalk finding](findings/us-safety-net-access-001.md)
matches those rates to 2024 ACS median-income, vehicle, and commute context. It
finds a non-monotonic state-income pattern and keeps ecological, denominator,
and year differences explicit.

The [state route-performance finding](findings/us-safety-net-access-002.md)
adds FY2025 application and recertification timeliness plus the 2023 Program
Access Index, preserving the distinction between population participation and
case-route handling.

The [WBNS lived-route finding](findings/us-safety-net-access-003.md) adds
recipient-reported notice, time, paperwork, interview, interruption, and help
channels. The [route-to-security triangulation](findings/us-safety-net-access-004.md)
reads those results with NBER route interventions and SIPP following hardship
without pooling incompatible units.

The [WBNS public-use route acquisition audit](wbns-public-use-route-acquisition-audit-v1.md)
identifies ICPSR 39691 and maps the 2024 questionnaire's route variables. The
public-use microdata extraction remains a live next gate; no uncomputed WBNS
cross-tabs are treated as findings.
The same audit now records the 2023 ICPSR 39462 fallback check: it supplies a
potential second cross-sectional round, but its file/SDA route also requires
authenticated access and has not been treated as retrieved evidence.

The [WBNS food-insecurity persistence layer](wbns-food-insecurity-persistence-layer-v1.md)
adds a published 2019–2025 material-security series and 2025 subgroup context.
It gives the route program a visible material endpoint while preserving the
cross-sectional, retrospective, methodology-vintage, and non-causal boundaries.
The [food-hardship finding](findings/us-safety-net-access-005.md) is the current
published synthesis; the public-use file remains the next route/outcome test.

The [WBNS charitable-food access layer](wbns-charitable-food-access-layer-v1.md)
adds the mixed-safety-net route: persistent participation, simultaneous unmet
need, time and transport constraints, awareness, comfort, safety, food variety,
and perceived unfair treatment. The [charitable-food finding](findings/us-safety-net-access-006.md)
keeps these access and meaning measures separate from provider capacity and
political response.
