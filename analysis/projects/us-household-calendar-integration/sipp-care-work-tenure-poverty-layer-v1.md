# SIPP child-care payment, help, and work constraint by tenure and poverty v1

**Checked:** 2026-09-13  
**Source:** 2025 SIPP public-use file, 2024 reference months  
**Unit:** person record by reference month; person-weighted diagnostic  
**Method:** `WPFINWGT`; tenure crossed with monthly household income-to-poverty
ratio; code `1` among each field's nonblank records  
**Status:** descriptive distribution; official field universes, replicate-weight
variance, and causal timing are not estimated

## Why this pass matters

Care is a societal labor-and-access institution, not only a private household
expense. This screen asks whether the observed child-care payment, payment help,
and work-constraint fields have different distributions across housing tenure
and income position.

```text
income position + housing tenure
  -> care payment and assistance conditions
  -> reported ability to work or work more
  -> household time, earnings, security, and institutional demand
```

The SIPP file measures the first three layers imperfectly. It does not identify
the provider, price, hours, schedule, notice, or later political meaning.

## Selected results

| Tenure | Income-to-poverty band | Paid child care | Help paying for care | Care prevented work or more work | Valid records for payment / work |
|---|---|---:|---:|---:|---:|
| Owned/bought | Below 1.00x | 19.0% | 7.6% | 3.9% | 1,002 / 1,405 |
| Owned/bought | 1.00–1.99x | 23.4% | 11.7% | 3.4% | 1,994 / 2,727 |
| Owned/bought | 2.00–3.99x | 26.1% | 3.9% | 2.9% | 4,876 / 6,358 |
| Owned/bought | 4.00x+ | 38.4% | 3.9% | 3.1% | 8,945 / 10,878 |
| Rented | Below 1.00x | 23.8% | 13.5% | 6.8% | 1,568 / 2,218 |
| Rented | 1.00–1.99x | 19.2% | 10.9% | 5.1% | 1,958 / 2,753 |
| Rented | 2.00–3.99x | 23.8% | 8.7% | 5.8% | 2,372 / 3,092 |
| Rented | 4.00x+ | 43.5% | 5.4% | 4.5% | 1,342 / 1,733 |

The central distributional pattern is not simply “poor families pay for more
care.” Among renters, the reported work constraint is higher in every displayed
poverty band than among owners/buyers, while paid-care incidence rises sharply
at the highest income band in both tenure groups. Reported help is concentrated
more strongly in lower-income renter and owner groups. These are descriptive
co-occurrences, not evidence that renting or income caused the work constraint.

The pattern also prevents a single cultural explanation. Payment, assistance,
and work limitation do not move as one scale: higher paid-care incidence at the
top income band does not imply higher reported help or work prevention, and
lower-income renters show both more help and more work constraint than
higher-income renters.

## What this adds to the broad program

1. **Care access is stratified by both material position and place in the
   housing market.** Tenure is not treated as a demographic essence; it is a
   condition that may shape cash room, stability, provider choice, and schedule.
2. **Assistance and work protection are different outcomes.** Receiving help
   with payment does not show that care was affordable, reliable, or sufficient
   to preserve work.
3. **The work cost is not reducible to the care bill.** The `EWORKMORE` field
   records a reported work constraint, while `EPAY` and `EPAYHELP` describe
   different care-payment routes.
4. **This widens the societal chain.** Care markets, housing tenure, income,
   labor availability, public assistance, and family time can interact before
   any later trust or political response is observed.

## Boundaries

- The extractor counts person records with a final person weight. Repeated
  household fields are not household counts.
- Blank fields are mostly outside the relevant question universe; they are not
  treated as “no.” The displayed percentages use each field's nonblank records.
- The selected fields are child-care/reference-parent measures, not all adult
  caregiving or all workers with children.
- The screen has no replicate-weight standard errors and does not construct the
  official universe flags for each conditional item. Small cells—especially
  rent-free tenure—should not be generalized.
- The 2024 reference-month file does not link a dated provider failure, price,
  schedule, work loss, remedy, or later civic action.

## Reproduction

```text
python3 scripts/analyze_sipp_two_way_layer.py \
  --input /path/to/sipp-household-slice.csv \
  --output /tmp/sipp-care-work-two-way.json \
  --fields EPAY EPAYHELP EWORKMORE
```

The reusable analysis is [analyze_sipp_two_way_layer.py](../../../scripts/analyze_sipp_two_way_layer.py).
Raw SIPP files and generated JSON remain outside the repository.

Related: [SIPP field audit](sipp-field-audit-v1.md), [care, health, and social
reproduction coverage](../../US-BROAD-THEME-COVERAGE-MATRIX_V1.md), and the
[material/time/care acquisition plan](material-time-care-linkage-acquisition-plan-v1.md).
