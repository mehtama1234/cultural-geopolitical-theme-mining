# SIPP population layer v1

**Run date:** 2026-09-12  
**Source:** 2025 SIPP public-use pipe file, 2024 reference year  
**Input slice:** full selected v2 extraction; 379,215 person-record/month rows, 378,291 positive-weight rows  
**Method:** [analyze_sipp_population_layer.py](../../../scripts/analyze_sipp_population_layer.py) using `WPFINWGT`  
**Labels and universes:** [2025 SIPP Data Dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)

## What this layer adds

This is the first labeled population-survey diagnostic attached to the broad research program. It shows how selected material, care, and work conditions appear across SIPP person records and reference months. It is not a single-household case study and does not claim that the conditions form one causal chain.

The table reports the share with verified code `1` among nonblank selected records. The blank share is shown because many fields have a restricted universe. Both are weighted with the final person weight. The result is therefore a person-weighted diagnostic of observed records, not a household-weighted national estimate.

| Field and verified code `1` meaning | Code `1` among nonblank records | Blank weight share | Broad theme or bridge |
|---|---:|---:|---|
| `ETENURE`: owned or being bought | 67.23% | 0.00% | housing, place, inequality |
| `EAWBMORT`: unable to pay rent or mortgage | 4.64% | 0.00% | household room; housing |
| `EAWBGAS`: unable to pay utility bills | 7.06% | 0.00% | household room; housing and energy |
| `EUTILITIES`: paid utilities separately from rent | 68.50% | 97.06% | housing and energy |
| `EENERGY_ASST`: received government energy assistance | 6.40% | 44.77% | public aid; housing and energy |
| `RFOODS`: high or marginal food security | 88.56% | 0.00% | household room; care |
| `EFOOD6`: hungry but did not eat because of money | 25.60% | 83.05% | household room; care |
| `EOWN_SAV`: owned a savings account | 63.72% | 18.26% | financial security |
| `EDEBT_CC`: carried a credit/store-card balance | 27.43% | 18.26% | consumer finance; household room |
| `EPAY`: paid for child care | 30.08% | 92.73% | time, care, and work |
| `EPAYHELP`: received help paying for child care | 6.38% | 92.73% | public aid; care and work |
| `EWORKMORE`: child care prevented working or working more | 3.88% | 90.70% | time, care, and work |
| `RMNUMJOBS`: one job | 54.20% | 16.85% | work, control, and household room |

## What can be said carefully

Within the selected records, the utility-payment-difficulty field has a higher observed nonblank code-`1` share than the rent-or-mortgage difficulty field. That comparison is only descriptive: the questions have different universes, and the scan does not establish whether the same people experienced both conditions or what caused either one.

The child-care fields show why “care cost” is not one measure. Paid care, payment assistance, and being prevented from working are different fields with different universes. The scan can support separate population layers for those conditions; it cannot say that assistance prevented work loss without a comparison design.

Month-to-month code-`1` diagnostic ranges were narrow in the selected records: rent/mortgage payment difficulty 4.61–4.69%, utility-payment difficulty 7.03–7.09%, high/marginal food security 88.45–88.63%, and one job 54.05–54.32%. These ranges are not a national trend estimate and should not be interpreted without design-based variance.

## Limits and next use

- Household fields are repeated on person records. The person weight estimates people represented by those records, not households counted once.
- Nonblank records are not automatically the official universe. The next production table must apply each field's universe and status flags explicitly.
- No replicate-weight variance or confidence intervals were computed.
- The layer does not observe the exact bill, price, service contact, remedy, firm decision, cultural interpretation, trust change, political action, or geopolitical consequence.
- SIPP records are not joined to CE, ATUS, NHTS, SHED, MEPS, or RECS as if they were the same people or households.

Use this layer to choose the next cross-source comparison for the five bridges. The next evidence should connect one of these measured conditions to a separate source on prices, time, firm or agency behavior, interpretation, or political action, while preserving the missing arrows.
