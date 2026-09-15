# Treasury FIO homeowners-insurance market layer v1

The [Treasury Federal Insurance Office release](https://home.treasury.gov/news/press-releases/jy2791)
and its [supporting ZIP-code workbook](https://home.treasury.gov/system/files/311/Supporting_Underlying_Metrics_and_Disclaimer_for_Analyses_of_US_Homeowners_Insurance_Markets_2018-2022.xlsx)
add the market-side condition to the Federal Reserve household layer.

For 2018–2022, Treasury reports that homeowners in the 20% of ZIP codes with
the highest expected annual building losses from climate-related perils paid
$2,321 per policy on average, 82% more than homeowners in the lowest-risk 20%
of ZIP codes. Average policy nonrenewal rates were approximately 80% higher in
the highest-risk group. Average paid claim severity was about $24,000 in the
highest-risk group versus $19,000 in the lowest-risk group.

The workbook provides annual ZIP-code metrics for premiums, claims, loss
ratios, nonrenewals, and cancellations, subject to minimum reporting thresholds.
It covers the 2018–2022 window, excludes 2023–2024 activity, and does not
represent every insurer, policy form, residual market, excess-and-surplus
market, or flood insurance. Treasury also warns that retrospective reporting
and ZIP-level anomalies limit fine-grained inference.

The reproducible workbook audit finds 127,965 valid ZIP-code/year rows: exactly
25,593 rows for each year from 2018 through 2022. It treats the 4,000 or so
rows without a usable ZIP/year key as excluded from the audit counts and keeps
the workbook's policy-count decile separate from Treasury's climate-risk
quintile. The audit output is
[treasury-fio-workbook-audit.json](data/treasury-fio-workbook-audit.json).

The supported bridge is therefore:

```text
climate-risk geography -> higher observed premium and nonrenewal exposure
                         -> possible household coverage/affordability pressure
```

The second arrow is a cross-source hypothesis, not a result of this market
dataset. The next test is to join these market measures to household income,
rent/ownership, claims, repairs, mortgage status, and move/stay outcomes in a
matched place-time design.
