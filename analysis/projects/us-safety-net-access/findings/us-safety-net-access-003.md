# Recertification failure is a lived interruption, not just a processing metric

## The short finding

The official state timeliness series tells us how cases in a quality-control universe were processed. The Urban Institute’s December 2024 Well-Being and Basic Needs Survey shows what the route looked like from the recipient side: among working-age adults in families receiving SNAP, 24% reported an involuntary stop or interruption during the prior year, including 13% who said the family could not recertify on time.

The most common reported barriers among the 182 respondents in that interruption subgroup were not having enough time after receiving a notice (40%) and not receiving a notice (32%). Other respondents reported paperwork difficulty (22%), inability to participate in a required interview (16%), and lost paperwork or documentation at a SNAP office (15%). Multiple reasons could be selected, so these are overlapping route failures, not a causal decomposition.

## The route has several failure points

| Stage | Respondent-reported evidence |
|---|---|
| Notice reaches the household | 32% of the reason-specific subgroup said they did not receive notice about the need to recertify |
| Notice leaves enough usable time | 40% said they did not have enough time after receiving a notice |
| Paperwork is usable | 22% said paperwork was too difficult to understand or complete |
| Interview channel is reachable | 16% could not participate in a required interview |
| Documents survive the handoff | 15% said the SNAP office lost paperwork or documentation |
| Recipient can find the route | 10% did not know how to recertify |

This is why “recertification burden” should not be reduced to a single time variable. A notice can be sent but arrive too late; a deadline can be legally sufficient but practically unusable; a document can be submitted but not remain in the case pathway.

## Exposure is not evenly distributed

Urban reports higher involuntary interruption among adults ages 18–34 than among adults ages 55–64 (28% versus 16%), among adults living with children than those not living with children (29% versus 19%), and among workers than nonworkers (32% versus 18%). The inability-to-recertify figures show the same directional pattern: 16% versus 9% across the age groups, 15% versus 11% by children, and 16% versus 11% by employment status.

These are descriptive subgroup differences, not effects of employment or parenthood. Work schedules, certification periods, earnings volatility, documentation, household composition, notice reach, and case complexity can move together. They nevertheless identify the cells where the next linked or matched design should look for route friction.

## Institutional help is part of the route

Twenty-seven percent of adults in the published SNAP-family universe reported help from someone at a SNAP office with an application or recertification. Smaller shares reported help from a food provider (5%), community organization (5%), health provider (4%), or someone else (7%). Help is not the same as remedy: these figures do not show whether contact prevented interruption, corrected a decision, changed the benefit amount, or reduced later hardship.

## What this adds to the end-to-end program

The combined evidence now distinguishes three layers:

1. **Administrative performance:** official APT/RPT rates across state quality-control universes.
2. **Lived route exposure:** respondent-reported notice, time, paperwork, interview, and document barriers.
3. **Material consequence:** SIPP transition and following-hardship measures, which are population-level and not the same respondents or episodes.

The supported chain is therefore:

`recertification rule → notice/time/paperwork/interview route → reported interruption or loss → possible material hardship`

The source supports the route and interruption portions, but not a same-person estimate of the downstream hardship arrow. Trust, political judgment, appeal, correction, and action remain open rather than inferred from interruption.

## Limits

- The Urban analysis uses a nationally representative survey of more than 7,500 working-age adults in the December 2024 WBNS; the exact analytic denominator for the headline percentages is not disclosed in the brief.
- The barrier estimates use 182 respondents and allow multiple responses; they do not sum to 100% and are limited in precision.
- The reference period is retrospective. The source does not provide exact notice dates, benefit amounts, gap days, case decisions, agency corrections, appeals, or administrative verification.
- “Unable to recertify on time” is a reported reason, not proof of agency fault or household ineligibility. “Did not receive a notice” and “office lost paperwork” are reported experiences, not independently audited case findings.
- The source does not measure trust, voting, organizing, or political action. Those outcomes require separate evidence and cannot be inferred from benefit interruption.

## Sources and reproducibility

- [Detailed WBNS route layer](../urban-wbns-snap-recertification-interruption-layer-v1.md)
- [Machine-readable observation record](../../../records/us-urban-wbns-snap-recertification-interruption-2024.json)
- [USDA/FNA state route-performance finding](us-safety-net-access-002.md)
- [Urban Institute brief](https://www.urban.org/research/publication/paperwork-burdens-cost-one-eight-working-age-snap-recipients-their-benefits)
- [Urban Institute brief PDF](https://www.urban.org/sites/default/files/2025-09/SNAP-Experiences-Summary.pdf)
- [WBNS survey program](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)

