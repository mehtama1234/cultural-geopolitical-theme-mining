# Finding 002: Energy insecurity separates household sacrifice, public reach, restoration, and durable recovery

**Status:** provisional cross-source energy/public-capacity finding · **Checked:** 2026-09-17

## The bounded finding

The 2024 Residential Energy Consumption Survey reports energy insecurity in
43.56 million primary-residence housing units. The same EIA table reports
32.89 million homes sacrificing food or medicine for energy costs, 17.55
million experiencing unhealthy temperatures, and 16.19 million receiving a
disconnect or delivery-stop notice. These conditions can overlap; a notice is
not a completed shutoff.

The FY2024 LIHEAP annual report separately reports nearly 6 million individuals
and families helped, 5 million heating-assistance households, and 279,000
reported home-energy restoration instances. An existing SIPP transition screen
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
| Immediate restoration | LIHEAP reports 279,000 home-energy restoration instances | Which households were restored, duration, next bill, arrears, equipment, and recurrence |
| Following outcome | SIPP preserves a same-person monthly utility-difficulty-to-following-outcome descriptive screen | Dated bill or notice, assistance receipt, provider, causal counterfactual, and verified recovery |

The EIA housing-unit, LIHEAP program, and SIPP person-month denominators are
not interchangeable and must not be turned into a single restoration rate.

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
- [Structured energy consequence/public-restoration record](../../../records/us-energy-household-consequence-public-restoration-2024-2026.json)
- [SIPP utility-to-following-outcome record](../../../records/us-sipp-utility-care-following-outcomes-2024.json)

No household bill, utility-account, LIHEAP case, or personally identifying
microdata were added.
