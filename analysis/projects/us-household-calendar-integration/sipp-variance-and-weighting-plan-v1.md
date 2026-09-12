# SIPP variance and weighting plan v1

**Checked:** 2026-09-12  
**Source:** [2025 SIPP replicate-weight file](https://www2.census.gov/programs-surveys/sipp/data/datasets/2025/rw2025_csv.zip) and [replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)

## Official structure

The Census replicate-weight dictionary defines:

- `SSUID`, `PNUM`, `SPANEL`, `SWAVE`, and `MONTHCODE` as the matching fields;
- `REPWGT0` as equivalent to the primary-file `WPFINWGT` final person weight;
- `REPWGT1` through `REPWGT240` as final person replicate weights.

The replicate archive is approximately 536 MB. It is not committed to the repository. The current point diagnostics use `WPFINWGT` only and therefore do not carry design-based standard errors.

## Required implementation

For each person-level proportion or mean:

1. construct the exact field universe and special-code treatment from the Data Dictionary;
2. calculate the full-sample estimate with `REPWGT0`;
3. recalculate the estimate under each of the 240 replicate weights;
4. apply the Census-documented replicate variance formula and degrees-of-freedom rule;
5. publish the estimate, standard error, confidence interval, denominator, universe, and replicate availability;
6. repeat the check for each month, stratum, and transition statistic rather than reusing one national error term.

The analyst must first confirm the variance formula from the SIPP technical documentation or Census guidance before coding it. The number of replicate columns alone does not authorize guessing a jackknife or successive-difference formula.

## Unit rule

The available replicate weights are person weights. They support person-level estimates, including estimates of people living in households with a reported household condition. They do not create a household weight. Household claims require a documented one-record-per-household selection rule or an official household-weight source.

## Current status

The population, tenure, resource, regional, and two-way SIPP layers are point diagnostics with this limitation stated. The next statistical-quality pass is to acquire or stream the replicate file, verify the official variance method, and add uncertainty to a small pre-registered set of tables before expanding the number of subgroup comparisons.
