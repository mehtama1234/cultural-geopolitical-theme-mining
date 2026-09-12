# Treasury FIO supporting-metrics audit v1

**Checked:** 2026-09-12  
**Source report:** [Analyses of U.S. Homeowners Insurance Markets, 2018–2022](https://home.treasury.gov/system/files/311/Analyses_of_US_Homeowners_Insurance_Markets_2018-2022_Climate-Related_Risks_and_Other_Factors_0.pdf)  
**Supporting workbook:** [Supporting Underlying Metrics](https://home.treasury.gov/system/files/311/Supporting_Underlying_Metrics_and_Disclaimer_for_Analyses_of_US_Homeowners_Insurance_Markets_2018-2022.xlsx)  
**Evidence type:** insurer data aggregated to ZIP code and year.

## Acquisition and structure

The supporting workbook was downloaded from Treasury and inspected locally. It contains three sheets:

| Sheet | Shape or role |
|---|---|
| Disclaimer & Background | Scope, coverage, privacy, validation, and use limits |
| Metric Definitions | Definitions for the insurance measures |
| Supporting Underlying Metrics | 131,941 data rows, 10 columns, ZIP code by year |

The data sheet contains:

```text
ZIP Code
Year
Policy Decile Grouping
Claim Frequency
Claim Severity
Loss Ratio
Premiums Per Policy
Nonrenewal Rate
Nonpayment Cancellation Rate
Other than Nonpayment Cancellation Rate
```

The file covers 2018–2022. It is not a property-level or household-level file. Treasury’s privacy rule keeps only ZIP codes with information from at least 10 reporting insurers or at least 50 policies for each ZIP code. The supporting workbook therefore cannot be read as a complete list of every ZIP code or every policy.

## Direct Treasury comparison

Treasury’s report groups ZIP codes into the lowest and highest 20 percent by expected annual building losses from nine climate-related perils. Its national 2018–2022 averages are:

| Measure | Lowest-risk ZIP codes | Highest-risk ZIP codes |
|---|---:|---:|
| Claim frequency | 4.1% | 7.0% |
| Claim severity | $19,039 | $23,952 |
| Paid loss ratio | 54.7% | 64.7% |
| Nonrenewal rate | 0.90% | 1.61% |
| Premium per policy | $1,277 | $2,321 |
| Nonpayment cancellation rate | 1.32% | 2.17% |

The report says the highest-risk ZIP codes therefore had premiums about 82% above the lowest-risk group, nonrenewals about 80% higher, and more severe claims. From 2018 to 2022, nonrenewals in the highest-risk group rose from 1.10% to 2.37%.

## What this establishes

The public insurance record supports a strong market-level pattern:

```text
higher modeled peril loss
  -> more frequent and more costly claims
  -> higher premium and cancellation pressure
  -> higher nonrenewal and weaker availability
```

This is stronger than a general claim that “climate risk raises prices.” It shows several insurance measures moving together across risk groups. It still does not prove that risk alone caused every difference. Treasury notes that replacement costs, inflation, state rules, insurer choices, coverage changes, and the mix of insurers can also matter.

## What the workbook cannot answer

- whether a named household received a renewal notice;
- whether its deductible or exclusions changed;
- whether its mortgage escrow payment rose;
- whether it paid, borrowed, delayed a repair, or went without coverage;
- whether a claim was paid enough or quickly enough;
- whether the household stayed, sold, moved, or defaulted.

The workbook is therefore suitable for the place-and-market side of the study. It is not evidence of a household’s full cost of staying.

## Next comparison

Use the workbook’s ZIP-year fields with FEMA risk, ACS household characteristics, FHFA home prices, and HMDA lending records. Start with aggregate risk groups or large regions before attempting ZIP-level comparisons. Preserve the workbook’s coverage and privacy limits in every output.

The household-calendar extension remains necessary for the final link: premium or coverage change, the choice made, the person with control, the cost transferred, and the next-month result.
