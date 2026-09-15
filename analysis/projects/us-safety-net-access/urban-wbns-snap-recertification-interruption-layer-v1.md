# SNAP recertification interruption: a respondent-level route layer

**Status:** national retrospective survey evidence; not linked administrative case data  
**Updated:** 2026-09-14  
**Unit:** adults ages 18–64 in families receiving SNAP in the prior 12 months, with subgroup and reason-specific respondent universes as stated below  
**Source:** Urban Institute, December 2024 Well-Being and Basic Needs Survey (WBNS) analysis  
**Machine extraction:** `analysis/records/us-urban-wbns-snap-recertification-interruption-2024.json`

## Why this layer matters

The state route-performance layer measures whether cases in an official quality-control universe were processed on time. It cannot show whether a person received or understood a notice, had enough time to respond, could complete paperwork, reached an interview, or experienced a benefit interruption. This Urban analysis adds those respondent-reported route fields.

It is closer to a lived episode than a state participation rate, but it is still not a linked case record. Respondents report what happened during the prior year; the study does not link a person to the agency case file, exact notice date, exact benefit amount, gap length, correction, appeal, or later trust/action.

## Main reported estimates

Among working-age adults in families receiving SNAP in 2024, the December 2024 WBNS analysis reports:

| Reported experience | Share |
|---|---:|
| Benefits stopped or were interrupted involuntarily during the prior year | 24% |
| Benefits stopped/interrupted because the family could not recertify on time | 13% |
| Benefits stopped/interrupted because the family was told it was no longer eligible | 8% |
| Other reason | 3% |

The reason categories are not mutually exclusive. The analysis draws on a nationally representative sample of more than 7,500 adults ages 18–64; the exact analytic denominator is not disclosed in the brief, so this layer does not fabricate one.

## Who reported more interruption

| Subgroup | Any involuntary stop/interruption | Unable to recertify on time | No longer eligible |
|---|---:|---:|---:|
| Ages 18–34 | 28% | 16% | 11% |
| Ages 35–54 | 23% | 12% | 8% |
| Ages 55–64 | 16% | 9% | 4% |
| Living with children under 18 | 29% | 15% | 11% |
| Not living with children under 18 | 19% | 11% | 6% |
| Workers | 32% | 16% | 14% |
| Nonworkers | 18% | 11% | 5% |

Urban reports statistical significance markers for several subgroup contrasts. The differences are not treated here as causal effects of work, children, or age; they may reflect certification length, income volatility, eligibility composition, documentation, notice reach, available time, and other correlated conditions.

## What the route felt like

Among the smaller respondent group reporting loss or interruption because they could not recertify on time (`n = 182`), respondents could select multiple reasons:

| Reported barrier | Share |
|---|---:|
| Not enough time to recertify after receiving a notice | 40% |
| Did not receive a notice about the need to recertify | 32% |
| Paperwork was too difficult to understand or complete | 22% |
| Unable to participate in a required interview | 16% |
| SNAP office lost paperwork or documentation | 15% |
| Did not know how to recertify | 10% |
| Other reason | 8% |

These responses put several distinct mechanisms inside the single phrase “administrative burden”: a notice-reach failure, a time-window failure, a comprehension/completion burden, an interview-channel barrier, a document-handling problem, and an information gap. The categories are not mutually exclusive and should not be summed.

Among adults who recertified at some point in the prior year, 21% reported that recertification was difficult or very difficult. The reported share was 27% for workers and 17% for nonworkers. This is a perception of route difficulty, not an independently verified processing delay.

## Help and institutional contact

Among adults in families receiving SNAP in the prior 12 months, 27% reported help from someone at a SNAP office with an application or recertification. The published figure also reports 5% receiving help from a food pantry/food bank or another free-food provider, 5% from another community organization, 4% from a doctor’s office/clinic/hospital, and 7% from someone else. These are assistance sources, not proof that the assistance solved the case or prevented an interruption.

## Mechanism contribution

This layer strengthens the route portion of the atlas:

```text
recertification requirement
  -> notice reach and time window
  -> paperwork, interview, and document handling
  -> reported interruption or loss
  -> possible material hardship
```

The source supports the first three stages as respondent-reported associations in a retrospective survey. It does not identify the exact interruption duration, expected versus received amount, agency correction, appeal, food-security change in the same respondent, trust, political action, or whether the household later returned. The existing SIPP layers provide separate population-level transition and following-hardship evidence, but they must not be merged with this WBNS route record as if they were the same people or episodes.

## Method and limits

- The source is the Urban Institute’s December 2024 WBNS analysis, published September 2025. The survey is nationally representative for its target population according to the brief; estimates are weighted survey estimates.
- The main universe is adults ages 18–64 in families receiving SNAP in 2024 or the prior 12 months, depending on the item wording. The exact denominator for each published percentage is preserved in the source wording rather than inferred.
- The reason-specific barrier figure uses `n = 182` respondents and permits multiple responses. It is not a distribution of mutually exclusive causes.
- The study is retrospective and self-reported. It does not provide exact notice dates, administrative case disposition, benefit amounts, interruption days, or verified agency responsibility.
- “Unable to recertify on time” is a reported reason, not proof that every case was eligible or that an agency error occurred. Conversely, not receiving a notice or lost paperwork is a reported route experience, not an independently audited administrative finding.
- The finding does not claim that work, children, or age cause interruption. Those subgroups are useful for stratifying the next matched or linked design.

## Sources

- [Urban Institute brief page](https://www.urban.org/research/publication/paperwork-burdens-cost-one-eight-working-age-snap-recipients-their-benefits)
- [Urban Institute brief PDF](https://www.urban.org/sites/default/files/2025-09/SNAP-Experiences-Summary.pdf)
- [Urban Well-Being and Basic Needs Survey](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)
- [USDA/FNA FY2025 recertification timeliness](https://www.fna.usda.gov/snap/qc/timeliness/rpt-fy25)
- [Same-episode ledger implementation specification](same-episode-event-ledger-implementation-v1.md)

