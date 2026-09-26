# DC Solar for All reach and savings scope audit v1

**Checked:** 2026-09-21  
**Purpose:** preserve the distinction between program-level reach, project-level
capacity, and household-level bill outcomes in the public Solar for All record.

## What the public materials say

| Public statement | Unit or scope | What it supports | What it does not support |
|---|---|---|---|
| DOEE's April 2025 program update reports nearly 10,000 households served to date and about $500 average annual savings | Program-level cumulative reach and reported average | Solar for All has a reported household endpoint and a material savings claim | Individual credit, savings distribution, timing, persistence, or net charges |
| The 2024–2025 annual report describes 19 community-renewable-energy projects and 338 low-to-moderate-income households benefiting from a set of arrays | Project/report-period subset | A bounded installed-project and household-benefit count | The full program denominator or all households served to date |
| The same annual-report materials describe 3.5 MW with potential to cut bills by half for more than 900 households | Capacity-linked potential or project grouping | A physical-capacity-to-household-benefit claim | Actual credits for each household or whether the potential was realized |
| DOEE terms state that eligible subscribers receive free community-solar subscriptions and credits through Pepco billing, with estimated savings of about $500 per year | Customer-facing program terms | The intended billing route, price, and timing boundary | Individual enrollment completion, monthly credit, arrears, or durable energy-burden reduction |
| A 2025 DCPSC filing reports 309/309, 303/303, 297/297, and 260/260 listed subscribers receiving a monthly credit on four project rows | Project-row billing implementation | A stronger project-level receipt stage for the listed rows | Credit dollar amount, individual bill posting, offsetting charges, arrears reduction, full-program coverage, or persistence |

These figures should not be added together or treated as one denominator. They
appear to describe different clocks and subsets: cumulative program reach,
project-level annual-report activity, capacity-linked potential, and customer
contract terms.

## Why this matters for the broad atlas

The route is stronger than a construction announcement because it includes a
reported household reach and savings endpoint. But it also demonstrates a
recurring measurement problem:

```text
program reach
  -> project assignment
  -> enrollment and billing-system activation
  -> monthly credit on the customer's bill
  -> net savings after charges
  -> persistent energy security and ability to remain or switch
```

The public record currently supports the first stage and describes the middle
route. It does not independently verify the later stages for the same
households. A program-level average can coexist with unequal assignment,
delayed activation, vacant or ineligible accounts, variable solar output,
housing moves, or credits that do not resolve arrears.

The DCPSC filing moves one part of the route forward: four selected project
rows report every listed subscriber as receiving a monthly credit. That is
stronger than a design or promise, but it remains a project-row endpoint. The
filing does not expose the credit amount, net bill, charges, household
identity, arrears, or later-month continuation, so it cannot be promoted to
individual household savings or energy security.

## Decision

Retain the DC record as a **reported program endpoint**, not a verified
household panel. Do not pool its nearly-10,000 count, 338-household project
count, and 900-household capacity-linked figure. The next high-value evidence
would be a de-identified utility/program extract with household enrollment,
activation date, monthly credit, subscription cost, continued eligibility, and
arrears or energy-burden follow-up.

## Sources

- [DOEE April 2025 Solar for All program update](https://doee.dc.gov/release/doee-launches-next-phase-solar-all-epa-award)
- [DOEE Solar for All customer terms](https://doee.dc.gov/service/solarterms)
- [DCSEU 2024–2025 annual report](https://doee.dc.gov/sites/default/files/dc/sites/doee/publication/attachments/SIGNED_DCSEUAB%2024%27%20%26%2025%27%20Annual%20Report.pdf)
- [DCPSC project-level monthly-credit filing](https://edocket.dcpsc.org/apis/api/Filing/download?attachId=231182&guidFileName=f8e79b1b-f57a-4c90-b284-62dc6f35f109.pdf)
- [Machine-readable DC Solar for All record](../../records/us-doee-solar-for-all-household-bill-savings-2025-2026.json)
- [Machine-readable project-credit record](../../records/us-dcpsc-solar-for-all-monthly-credit-receipt-2025.json)
