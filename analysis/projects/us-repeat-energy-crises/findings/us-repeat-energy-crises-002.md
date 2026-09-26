# Finding 002: Energy insecurity separates household sacrifice, public reach, restoration, and durable recovery

**Status:** provisional cross-source energy/public-capacity finding · **Checked:** 2026-09-18

## The bounded finding

The 2024 Residential Energy Consumption Survey reports energy insecurity in
43.56 million primary-residence housing units. The same EIA table reports
32.89 million homes sacrificing food or medicine for energy costs, 17.55
million experiencing unhealthy temperatures, and 16.19 million receiving a
disconnect or delivery-stop notice. These conditions can overlap; a notice is
not a completed shutoff.

The FY2024 LIHEAP annual report separately reports nearly 6 million individuals
and families helped, 5 million heating-assistance households, and 279,000
reported home-energy restoration instances. The live LIHEAP performance API
adds preliminary all-grantee occurrence counts for bill-payment-related service
loss: post-disconnection restoration is 159,320, 166,991, and 171,077 in
FY2023–FY2025, while prevention is 1,868,247, 1,752,072, and 1,853,734.
These are occurrences, not unique households or restoration rates. An existing SIPP transition screen
then follows selected person-month records from utility difficulty to later
food, housing, or resource outcomes. These are complementary but non-pooled
units.

The safe interpretation is:

> Energy insecurity is visible as household sacrifice and service threat, while
> public reach and immediate restoration are visible as separate institutional
> endpoints. Neither source establishes a common take-up or restoration rate,
> durable affordability, repeat-crisis prevention, or household recovery.

## Event chain

```text
energy cost, housing, income, or equipment constraint
  -> food/medicine tradeoff, unhealthy temperature, or service notice
  -> assistance reach and possible restoration
  -> following-month food, housing, or resource condition
  -> [open] next bill, repeat crisis, health, trust, and political action
```

## What the public record supplies

| Stage | Evidence | Still open |
|---|---|---|
| Household consequence | EIA reports 43.56 million energy-insecure homes, including 32.89 million sacrificing food/medicine, 17.55 million with unhealthy temperatures, and 16.19 million with a disconnect/delivery-stop notice | Overlap, duration, cause, completed shutoff, bill amount, and household remedy |
| Public reach | HHS/ACF reports nearly 6 million individuals and families helped and 5 million heating-assistance households in FY2024 | Eligible denominator, application, take-up, benefit amount, timing, and repeat need |
| Program performance | Preliminary LIHEAP API data report 159,320/166,991/171,077 post-disconnection restoration occurrences and 1,868,247/1,752,072/1,853,734 bill-payment prevention occurrences in FY2023/FY2024/FY2025 | Occurrences may repeat; FY2023–FY2025 data are preliminary; no unique-household denominator, effect estimate, or state comparability is implied |
| Immediate restoration | LIHEAP reports 279,000 home-energy restoration instances in FY2024, with a separate bill-payment restoration series available through the API | Which households were restored, duration, next bill, arrears, equipment, and recurrence |
| Following outcome | SIPP preserves a same-person monthly utility-difficulty-to-following-outcome descriptive screen | Dated bill or notice, assistance receipt, provider, causal counterfactual, and verified recovery |

The EIA housing-unit, LIHEAP program, LIHEAP occurrence, and SIPP person-month
denominators are not interchangeable and must not be turned into a single
restoration rate. The selected-state diagnostic adds reporting variation, not
a cross-state effectiveness ranking.

## Selected-state diagnostic: administrative visibility is not effectiveness

The preliminary FY2025 state extract illustrates why the denominator matters:

| State | Households served | Restoration occurrences per served household | Prevention occurrences per served household |
|---|---:|---:|---:|
| California | 146,843 | 0.0703 | 0.6259 |
| New York | 1,159,724 | 0.0007 | 0.0796 |
| Ohio | 261,341 | 0.0171 | 0.3089 |
| Texas | 71,847 | 0.0281 | 0.5559 |
| Virginia | 126,299 | 0.0094 | 0.0990 |

These differences are real differences in the reported administrative surface,
but they are not state effectiveness scores. Occurrences can repeat, states
may define and report events differently, and the served-household denominator
is not the number exposed, eligible, disconnected, or at risk. The comparison
therefore advances a broader mechanism: local program design and reporting
capacity help determine which parts of energy insecurity become visible, while
household durability and the next-bill outcome remain unobserved.

## Benefit size is another separate currency

The official FY2024 state profiles add a material-size layer that the
occurrence API does not contain. Texas reported an average heating-assistance
benefit of $1,102, while Ohio reported an average of $327. These are different
reporting vintages and assistance profiles, not a state ranking. They show why
“household served” is not enough to describe the intervention: benefit size,
energy burden, bill amount, fuel type, timing, and arrears may all change the
amount of usable room created.

The profiles still do not show whether the payment covered the household's
actual bill, prevented a shutoff, restored service, protected food or medicine,
or prevented a later repeat crisis. Benefit amount is therefore a better
material measure than an occurrence count, but it is not recovery.

The Virginia trajectory provides a useful cross-lane caution: reported
households served rose from 118,347 in FY2023 to 144,007 in FY2024 and then
fell to 126,299 in preliminary FY2025, while restoration occurrences fell
from 2,382 to 1,824 to 1,185 and prevention occurrences from 18,157 to 16,309
to 12,509. This is program context alongside the Virginia utility-governance
ledger, not evidence that Rider T1, large-load policy, rates, weather, or any
other infrastructure event caused the LIHEAP trajectory.

## Why it matters to the broader atlas

This layer makes a multiple-currency adjustment visible. A household can
preserve electricity by sacrificing food or medicine, tolerate unhealthy
temperatures, borrow, seek aid, or receive a reconnection without returning to
stable affordability. Public capacity can therefore be visible at the same
time that private burden and repeat exposure remain unresolved.

Keep these states separate:

```text
energy insecurity   != completed shutoff
notice              != loss of service
program reach       != take-up rate
restoration         != durable affordability
following hardship  != utility-caused hardship
continued service   != free choice without sacrifice
```

## Next decisive test

Build a privacy-minimized household or person-month episode ledger linking a
dated bill/notice, temperature or equipment condition, assistance application
and receipt, reconnection, next bill, food/medicine tradeoff, housing and health
outcome, repeat crisis, complaint, trust, and later action. Preserve households
that avoided disconnection, used informal support, or received assistance
without restoration, and retain non-applicants and denied routes.

## Sources and storage boundary

- [EIA 2024 Residential Energy Consumption Survey Table HC11.1](https://www.eia.gov/consumption/residential/data/2024/hc/pdf/HC11.1_2024.pdf)
- [HHS/ACF FY2024 LIHEAP annual report](https://ocsannualreport.acf.hhs.gov/annual-report-fy24/priorities-and-fy24-spotlights)
- [FY2024 Texas LIHEAP state profile](https://stage.liheappm.acf.hhs.gov/sites/default/files/private/congress/profiles/2024/FY2024_Texas_Profile.pdf)
- [FY2024 Ohio LIHEAP state profile](https://stage.liheappm.acf.hhs.gov/sites/default/files/private/congress/profiles/2024/FY2024_Ohio_Profile.pdf)
- [LIHEAP FY2023–FY2025 performance extraction](../data/us-liheap-performance-measures-2023-2025.json)
- [Selected-state FY2025 diagnostic](../data/liheap-state-performance-diagnostic-fy2025.json)
- [Virginia FY2023–FY2025 trajectory](../data/liheap-virginia-performance-2023-2025.json)
- [Structured energy consequence/public-restoration record](../../../records/us-energy-household-consequence-public-restoration-2024-2026.json)
- [SIPP utility-to-following-outcome record](../../../records/us-sipp-utility-care-following-outcomes-2024.json)

No household bill, utility-account, LIHEAP case, or personally identifying
microdata were added.
