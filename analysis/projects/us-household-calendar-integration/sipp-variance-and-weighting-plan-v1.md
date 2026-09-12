# SIPP variance and weighting plan v1

**Checked:** 2026-09-12  
**Source:** [2025 SIPP replicate-weight file](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip) and [replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)

## Official structure

The Census replicate-weight dictionary defines:

- `SSUID`, `PNUM`, `SPANEL`, `SWAVE`, and `MONTHCODE` as the matching fields;
- `REPWGT0` as equivalent to the primary-file `WPFINWGT` final person weight;
- `REPWGT1` through `REPWGT240` as final person replicate weights.

The replicate archive is approximately 536 MB. It is not committed to the repository. The current subgroup point diagnostics use `WPFINWGT` only. A first full-sample Fay-BRR result is recorded in the [SIPP Fay-BRR point estimates](sipp-fay-brr-point-estimates-v1.md); subgroup tables still do not carry design-based standard errors.

## Required implementation

For each person-level proportion or mean:

1. construct the exact field universe and special-code treatment from the Data Dictionary;
2. calculate the full-sample estimate with `REPWGT0`;
3. recalculate the estimate under each of the 240 replicate weights;
4. apply the Census-documented replicate variance formula and degrees-of-freedom rule;
5. publish the estimate, standard error, confidence interval, denominator, universe, and replicate availability;
6. repeat the check for each month, stratum, and transition statistic rather than reusing one national error term.

The 2025 SIPP User Guide specifies Fay's modified BRR: `Var(theta0) = 1/[G(1-k)^2] * sum((theta_i-theta0)^2)`, with `G=240` and `k=0.5`. The implementation uses that formula. The number of replicate columns alone would not authorize guessing a jackknife or successive-difference formula.

## Unit rule

The available replicate weights are person weights. They support person-level estimates, including estimates of people living in households with a reported household condition. They do not create a household weight. Household claims require a documented one-record-per-household selection rule or an official household-weight source.

## Current status

The population, regional, and two-way SIPP layers remain point diagnostics with this limitation stated. The full-sample, tenure, and resource subgroup checks are complete in the [full-sample Fay-BRR result](sipp-fay-brr-point-estimates-v1.md), [tenure Fay-BRR result](sipp-fay-brr-tenure-estimates-v1.md), and [resource Fay-BRR result](sipp-fay-brr-resource-estimates-v1.md). The next statistical-quality pass is to add uncertainty to a small pre-registered tenure × resource set before expanding the number of comparisons.
