# Uganda platform-work algorithmic remedy record v1

**Status:** official ILO/Makerere worker survey; self-reported exposure and remedy outcomes

**Checked:** 2026-09-15

## Why this record matters

The Uganda study adds a worker-level, non-European observation to the
algorithmic-management pathway. It does not merely describe platform rules:
workers report how ratings, refusal of tasks, deactivation, monitoring, and
complaint routes affected their work. It therefore supplies an important
counterweight to the Dutch court records and the Uber/Ola information order.

The strongest result is not that every platform corrected errors. It is that a
substantial group reported using appeal or complaint channels and reported
positive outcomes. The study cannot independently verify those outcomes or
identify which platform action was reversed in each case.

## Official source and design

- [ILO PROSPECTS: Platform work in Uganda](https://www.ilo.org/sites/default/files/2024-11/24014-ILO-Digital-Labour-Uganda-report-v4-2-E.pdf)
- Source: ILO–Makerere University surveys conducted in 2023
- Cleaned analytical sample: 647 workers across taxi, delivery, domestic and
  personal services, healthcare, online freelancing, and e-commerce/social-media
  selling (report p. 122)
- Main platform taxi/delivery sample: 241 taxi-platform workers and 133
  delivery-platform workers (report p. 51)
- Geography: Uganda, with platform and traditional comparison segments in
  selected sectors

## Evidence matrix

| Stage | Direct survey observation | Boundary |
|---|---|---|
| Economic dependence | More than 70% of workers across sectors reported platform work as their primary income source | Cross-sectional self-report; not a panel of income dependence |
| Ratings | 55–80% across sectors reported that ratings affected work volume; high ratings were associated with better-paying tasks and low ratings could lead to deactivation | Associations reported by workers, not an audited platform rule or causal estimate |
| Allocation and refusal | Algorithms allocated taxi rides and delivery orders using factors such as ratings, hours worked, and acceptance times; 90% of taxi and 73% of delivery workers could refuse work, while 80% and 69% respectively reported negative consequences for refusal | Reported platform practices; platform-specific mechanisms vary |
| Deactivation | About 45% of taxi and delivery workers reported experiencing deactivation; reasons included cancellations, low ratings, complaints, inactivity, late fees, and rejected orders | Duration and permanence varied; not every deactivation was algorithmic |
| Appeal use | About 75% of workers who experienced deactivation reported appealing | Denominator and appeal channel are survey-defined; no case files were linked |
| Appeal outcome | More than 90% of those who appealed in both taxi and delivery sectors reported that the case was resolved in their favour | Self-reported favorable resolution; no independent verification of account restoration, payment, or correction |
| Complaint route | 41% of taxi-platform and 47% of delivery-platform workers reported filing a complaint or requesting platform assistance, mostly over payment issues | Complaint and appeal populations should not be conflated |
| Complaint outcome | 81% of taxi-platform and 92% of delivery-platform workers who sought assistance reported a positive outcome | Positive outcome is not itemized as correction, repayment, reinstatement, or explanation |
| Monitoring | GPS monitoring was reported by 83% of taxi platforms and 97% of delivery platforms; nearly one-third reported monitoring through calls | Exposure is worker-reported and does not establish the exact decision use of each signal |
| Collective voice | Collective action through unions or cooperatives was largely absent; social-media groups were used by 20% of taxi and 49% of delivery workers for information and support | Informal mutual aid is not equivalent to collective bargaining or formal representation |

## Remedy coding

| Remedy field | Code | Reason |
|---|---|---|
| Concrete adverse platform decision | `observed` | Deactivation, reduced work, warnings, ratings, and payment disputes are reported |
| Worker initiated appeal | `observed_self_report` | Approximately three-quarters of affected taxi/delivery workers reported appealing |
| Positive resolution | `observed_self_report` | More than 90% of appellants reported favorable resolution |
| Explanation of automated factors | `not_observed` | The survey does not establish that a worker received a model explanation |
| Human review | `not_observed` | A positive resolution is not enough to identify the review process |
| Data or rating correction | `not_observed` | No linked correction record is reported |
| Account restoration | `not_observed` | Favorable resolution is not defined as reactivation |
| Compensation or repayment | `not_observed` | Payment complaints were common, but the amount and remedy are not specified |
| Anti-retaliation | `not_observed` | No post-appeal retaliation measure is provided |

## Interpretation

Uganda changes the shape of the evidence gap. The current atlas now has an
observed, self-reported appeal pathway outside Europe and the United States,
but not a verified administrative remedy pathway.

```text
ratings / allocation / monitoring
  -> reduced work, warning, or deactivation [worker-reported]
  -> appeal or complaint [worker-reported]
  -> favorable resolution [worker-reported]
  -> identified correction, restoration, repayment, or explanation [open]
```

This record also complicates a simple “no remedy” interpretation. The Dutch
and Uber/Ola records show formal judicial information or status remedies; the
Uganda survey shows workers using platform-level routes with reported positive
outcomes. But the units and evidentiary strength differ. The correct synthesis
is that remedy visibility exists across several settings while remedy content,
verification, and institutional accountability remain uneven.

## Decisive follow-up

Acquire platform-specific Ugandan complaint or appeal forms, worker
organization records, or administrative/court files that identify what a
“positive outcome” meant: reactivation, rating correction, repayment,
explanation, or another action. Preserve the survey as the worker-reported
baseline even if no linked administrative record can be acquired.

## Boundary

This is not a causal estimate, representative national prevalence estimate, or
legal finding. The study is a cross-sectional survey with sector-specific
samples and self-reported outcomes. It supports worker experience and reported
remedy pathways, not verified platform compliance or universal platform
practice.
