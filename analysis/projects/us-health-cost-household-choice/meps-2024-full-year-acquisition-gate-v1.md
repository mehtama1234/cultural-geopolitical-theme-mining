# MEPS 2024 now supplies a bounded design-based health-cost vintage

**Checked:** 2026-09-15  
**Sources:** [AHRQ MEPS HC-256 2024 Full-Year Consolidated PUF](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256&prfricon=yes), [HC-256 documentation](https://meps.ahrq.gov/data_stats/download_data/pufs/h256/h256doc.shtml), [HC-254G office-based visits](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254G&prfricon=yes), [HC-254A prescribed medicines](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254A&prfricon=yes), [HC-254E emergency-room visits](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254E&prfricon=yes), [HC-254D inpatient stays](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-254D&prfricon=yes), and the [AHRQ MEPS release schedule](https://meps.ahrq.gov/about_meps/releaseschedule.jsp)  
**Machine record:** [MEPS 2024 release-gate record](../../records/us-meps-2024-full-year-release-gate.json)

> **The result in one line:** the 2024 MEPS vintage estimates **$8,346.52** in total health expenditure and **$1,117.28** in self/family payment per represented person; the first number describes system resource use, while the second is a narrower direct-payment exposure—not a complete household-burden measure.

## The bounded update

A newer official MEPS vintage is now available for the calendar year 2024. The HC-256 Full-Year Consolidated PUF covers data collected in Rounds 3–5 of Panel 28 and Rounds 1–3 of Panel 29 and is delivered in multiple public-use formats. AHRQ’s 2026 schedule separately identifies the 2023–2024 Panel 28 Longitudinal Data File and the 1996–2024 replicate file for BRR variance estimation.

This closes the acquisition gap and now supports a first bounded analytical finding. The result is deliberately narrower than a household-affordability claim: it is a 2024 person-level spending and self/family-payment estimate with an explicit positive-weight, valid-measure denominator and standard BRR uncertainty. The HC-036BRR variance artifact is available and downloaded; AHRQ describes it as a 483,346-person file with 128 sample indicators for constructing BRR replicate variances, including HC-256.

The reproducible [`audit_meps_hc256_structure.py`](../../../scripts/audit_meps_hc256_structure.py) scan of the downloaded Stata artifact found **19,140 records**, **1,615 variables**, and **18,683 records with a positive `PERWT24F`**. With `--brr-file`, the same script audits the HC-036BRR person-ID join. The file contains the final person weight, variance stratum and PSU, total expenditure, self/family payment, insurance, family income, poverty category, perceived-health, and round-specific employment fields needed for the next audit. This verifies that a usable artifact arrived and that the main structural fields are present; it is not a weighted estimate, a complete valid-case universe, or evidence about spending or care.

The HC-036BRR Stata artifact contains **128 BRR indicators** and **461,092 unique person IDs** in the downloaded file. A direct ID scan found all **19,140 HC-256 person IDs** in HC-036BRR—a 100% linkage rate for the HC-256 records. This closes the identity-coverage gate. The replicate-weight construction has now also been run and checked against AHRQ’s standard-BRR documentation; the remaining work is substantive universe, subgroup, panel-comparability, and event-level auditing.

AHRQ’s variance documentation specifies the standard construction: merge `BRR1`–`BRR128` by `DUPERSID` and `PANEL`, multiply each flag by `2 * PERWT24F`, and calculate BRR variance across the 128 replicate estimates. Fay’s method is a separate option with different multipliers and must not be silently mixed with standard BRR. The reproducible `analyze_meps_hc256_brr.py` implementation follows that standard construction and returned 19,140 linked HC-256 records with no missing replicate flags.

## First bounded 2024 estimate

Using the final person weight and standard BRR replicate weights, the 2024 file gives the following descriptive estimates:

| Measure | Valid records | Weighted mean per person | Standard error | Normal 95% interval |
| --- | ---: | ---: | ---: | ---: |
| Total health expenditure | 18,683 | $8,346.52 | $225.56 | $7,904.43–$8,788.62 |
| Self/family payment | 18,683 | $1,117.28 | $37.73 | $1,043.32–$1,191.24 |

The immediate reader-facing finding is that the average person represented by this 2024 MEPS vintage has substantial total health expenditure, while the self/family payment component is much smaller but still material. That contrast is analytically useful because it separates the health system’s total resource use from the amount assigned directly to people or families. It is not a household budget share, a bill shock measure, or evidence that the remaining amount was painless: insurance premiums, taxes, unpaid care, delayed care, debt, time, and foregone alternatives are outside this two-field estimate.

The estimate is intentionally a starting point for the end-to-end health-cost pathway. The next reader-facing comparison should test which people and households carry the self/family payment, whether payment coincides with unmet need or work/time disruption, and whether event-level records can distinguish ordinary utilization from acute episodes. Until those links are computed, the safe conclusion is a system-to-person payment wedge—not a completed affordability or behavioral story.

## Who carries the direct-payment exposure?

The first subgroup pass uses the HC-256 family-income-to-poverty category (`POVCAT24`). It shows a non-monotonic relationship for total expenditure and a clearer income gradient for self/family payment:

| Poverty category | Valid records | Total expenditure mean | Self/family payment mean |
| --- | ---: | ---: | ---: |
| Poor/negative | 2,940 | $8,323.49 | $442.97 |
| Near poor | 799 | $7,984.26 | $491.94 |
| Low income | 2,293 | $7,290.58 | $843.87 |
| Middle income | 5,004 | $8,007.69 | $952.81 |
| High income | 7,647 | $8,862.43 | $1,497.82 |

The safe insight is not that higher-income people face more hardship. It is that direct self/family payment is not a simple proxy for total health need or system resource use: higher-income people in this vintage have higher direct payment on average, while total expenditure does not move monotonically across the poverty categories. Utilization, age, insurance mix, ability to purchase care, provider mix, and health need may all contribute. The subgroup result therefore sharpens the next question: which groups pay less because they face less need, because coverage pays more, because they use less care, or because they forgo or delay care?

The estimates were produced by [`analyze_meps_hc256_subgroups.py`](../../../scripts/analyze_meps_hc256_subgroups.py), using the same standard-BRR construction as the national estimate. The poverty categories are not yet a household affordability model, and the current pass does not identify premiums, debt, unpaid care, work disruption, or unmet need.

## How coverage changes the direct-payment picture

Among people under 65, the coverage categories show a sharp difference in direct payment while total expenditure is similar for private and public-only coverage:

| Coverage category | Valid records | Total expenditure mean | Self/family payment mean |
| --- | ---: | ---: | ---: |
| Under 65, private | 8,889 | $7,126.98 | $1,179.11 |
| Under 65, public only | 3,653 | $7,086.21 | $268.40 |
| Under 65, uninsured | 1,191 | $1,090.76 | $487.44 |

The bounded insight is that coverage status is closely related to the payment channel: in this descriptive vintage, under-65 public-only respondents show nearly the same total expenditure mean as privately insured respondents but a much smaller self/family payment mean. The uninsured group shows both lower recorded expenditure and an intermediate direct-payment mean. That pattern is compatible with differences in coverage generosity, eligibility, health need, service use, provider mix, and delayed or forgone care; it is not an insurance causal effect.

The 65-plus categories are retained in the machine record but are not mixed into this under-65 comparison. Their age and Medicare composition make them a different estimand, and the smallest coverage cells are too imprecise for a reader-facing ranking. The next test is to link coverage/payment categories to event-level utilization, unmet need, work/time disruption, and household resources rather than interpreting payment alone as welfare.

## The first event-level bridge: office visits

The newly released HC-254G Office-Based Medical Provider Visits File makes the payment result more concrete. AHRQ’s documentation says each record is a household-reported office-based visit and that event-level estimates use `PERWT24F`; it also warns that the event file contains people with office-based visits, not people with no such visit. Using the file’s `VARSTR`/`VARPSU` Taylor design, the 2024 event layer estimates:

| Event measure | Estimate |
| --- | ---: |
| Office-based provider visits | 2.410 billion (SE 78.1 million) |
| Total payments per visit | $308.05 (SE $7.95) |
| Self/family payment per visit | $57.38 (SE $3.04) |
| Visits with positive total payment | 98.73% (SE 0.09 pp) |
| Telehealth share of office-based events | 10.79% (SE 0.69 pp) |

The coverage-conditioned event layer shows a different scale from the annual person estimate:

| Under-65 coverage category | Self/family payment per office visit | Valid events |
| --- | ---: | ---: |
| Private | $75.75 (SE $4.70) | 62,776 |
| Public only | $14.80 (SE $3.29) | 23,022 |
| Uninsured | $117.02 (SE $23.92) | 1,436 |

This is the first direct link from coverage status to a concrete care event and payment channel. It still does not observe whether the visit was necessary, delayed, substituted, paid through debt, or followed by work loss or unpaid care. The event result therefore narrows the next question: which payment paths are attached to repeated or acute episodes, and which are absent because people did not reach care at all?

The event-layer estimates are reproduced by [`analyze_meps_hc254g_event_layer.py`](../../../scripts/analyze_meps_hc254g_event_layer.py). The method intentionally uses HC-254G’s Taylor design rather than silently reusing the person-level BRR calculation for event-level uncertainty.

## A second channel: prescribed medicines

The HC-254A prescribed-medicine file supplies a complementary purchase-level surface. In 2024 it estimates **3.029 billion purchases**, with **$233.25** in total payments and **$16.95** in self/family payment per purchase. These are purchase events, not the share of people who obtained medicine, the share who needed but did not obtain it, or a measure of adherence.

Among under-65 purchase events, the direct-payment pattern is directionally similar to office visits but the scale is different:

| Under-65 coverage category | Self/family payment per medicine purchase | Valid purchases |
| --- | ---: | ---: |
| Private | $21.83 (SE $2.38) | 62,035 |
| Public only | $4.12 (SE $0.60) | 40,300 |
| Uninsured | $55.06 (SE $10.09) | 2,499 |

The cross-channel finding is therefore bounded: public-only coverage is associated with lower observed direct payment per recorded office visit and medicine purchase, while uninsured events show higher direct payment where a purchase or visit is observed. That does not tell us who never reached care, never filled a prescription, delayed treatment, borrowed, or sacrificed time and essentials. The next event pass must combine these event records with person-level non-use, unmet-need, employment, food/housing, and recovery measures.

The purchase estimates are reproduced by [`analyze_meps_hc254a_rx_event_layer.py`](../../../scripts/analyze_meps_hc254a_rx_event_layer.py), using HC-254A’s own Taylor design and keeping purchase events separate from person-level prevalence.

## Acute care is a different payment surface

The HC-254E emergency-room file adds an acute-care comparison. In 2024 it estimates **68.2 million emergency-room visits**, with **$1,405.11** in total payment and **$148.22** in self/family payment per visit. The amounts are far above the office-visit averages, but the populations and clinical circumstances differ; this is an event-level contrast, not a claim that emergency care caused household hardship.

Among under-65 observed emergency-room visits:

| Coverage category | Self/family payment per emergency-room visit | Valid visits |
| --- | ---: | ---: |
| Private | $287.10 (SE $25.53) | 1,267 |
| Public only | $26.92 (SE $6.98) | 1,173 |
| Uninsured | $519.55 (SE $45.51) | 96 |

This strengthens the cross-channel interpretation: coverage is associated with sharply different observed payment channels across office visits, medicines, and emergency care, while emergency care also introduces severity and facility-payment differences. The uninsured emergency estimate is based on only 96 valid visits, so it is a signal for the next test, not a stable population ranking. None of the three event files observes the counterfactual person who delayed or never obtained care.

The emergency-room estimates are reproduced by [`analyze_meps_hc254e_er_event_layer.py`](../../../scripts/analyze_meps_hc254e_er_event_layer.py), using the HC-254E Taylor design and separately summing facility and doctor self/family payments.

## Hospitalization is the high-intensity endpoint

The HC-254D inpatient-stays file completes the first four-channel event sequence. In 2024 it estimates **28.4 million inpatient stays**, averaging **4.9 nights**, **$18,892.70** in total payment, and **$865.20** in self/family payment per stay.

For under-65 observed inpatient stays, the self/family payment means are:

| Coverage category | Self/family payment per inpatient stay | Valid stays |
| --- | ---: | ---: |
| Private | $1,420.00 (SE $274.16) | 435 |
| Public only | $145.83 (SE $42.81) | 413 |

The 20-event uninsured cell is retained in the machine record but not promoted in the reader comparison. The bounded cross-channel story is now clearer: direct payment differs substantially by coverage across routine visits, prescriptions, emergency visits, and hospital stays, but the event intensity and selection also change sharply. The data still do not follow a person from a dated need through care choice, debt or unpaid care, work disruption, recovery, trust, or action.

The inpatient estimates are reproduced by [`analyze_meps_hc254d_inpatient_event_layer.py`](../../../scripts/analyze_meps_hc254d_inpatient_event_layer.py), using the HC-254D Taylor design and separately summing facility and doctor self/family payments.

## Why this matters to the end-to-end program

The current MEPS layer uses Panel 27 longitudinal data for 2022–2023. The 2024 file can extend recency and add event-level material, coverage, health, work, and utilization fields, but it is not automatically a continuation of the same longitudinal estimand. Panel 28 and Panel 29 overlap in the 2024 full-year file, and a person’s participation, weight, and valid fields must be preserved.

```text
2024 file availability
  -> file and codebook acquisition
  -> panel/round, weight, variance, and universe audit
  -> 2024 person/family/event estimates
  -> comparison with Panel 27 and prior annual files
  -> health-cost episode ledger and household adaptation test
```

The strongest next use is not simply updating a mean. It is testing whether 2024 event files and person/family fields can populate the [health-cost event ledger](../../templates/US-HEALTH-COST-EVENT-LEDGER_V1.md): need or service, coverage and payment, care decision, alternatives, time and work, debt, and recovery.

## Acquisition gate

For the 2024 estimate to remain reproducible and interpretable, retain:

1. the exact HC-256 data artifact, codebook, documentation, and retrieval hashes;
2. the Panel 28/29 round map and all relevant person, family, event, and condition identifiers;
3. final weights, strata, PSUs, BRR/replicate files, and the valid-field denominator for every estimate;
4. variable-label and universe checks against the prior Panel 27 analysis;
5. a missingness, nonresponse, panel-overlap, and subgroup-coverage audit;
6. a comparison design that keeps 2024 full-year cross-section, Panel 28 longitudinal, and prior Panel 27 measures separate; and
7. a reader-facing finding that states what the new vintage changes and what remains open.

## What this does not prove

- It does not establish that health spending rose or fell in 2024 relative to a prior vintage; the current estimate is a new bounded level, not yet a harmonized trend comparison.
- It does not establish household affordability, skipped care, medical debt, unpaid care, or work loss.
- It does not make Panel 28 longitudinal data available merely because the schedule lists the file.
- It does not make a 2024 annual file directly comparable to the 2022–2023 Panel 27 longitudinal estimate.
- It does not close the need/bill → care → substitution → recovery → trust/action chain.

## Next action

Preserve the current Panel 27 records as the prior-vintage comparator, then extend this estimate into harmonized subgroups and event-level episodes. The next publication should keep the full-year cross-section, Panel 28 longitudinal file, and prior Panel 27 measures separate while testing the need/bill → care → substitution → recovery → trust/action chain.
