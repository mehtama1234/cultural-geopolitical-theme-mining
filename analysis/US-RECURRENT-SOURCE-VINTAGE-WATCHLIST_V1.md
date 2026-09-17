# US recurrent-source vintage watchlist v1

**Checked:** 2026-09-17
**Status:** active refresh control; not a claim that any source closes an
end-to-end arrow

**Official calendar recheck:** the current [BEA release schedule](https://www.bea.gov/news/schedule/full)
lists the annual update and Q2 GDP third estimate/corporate profits for
September 30, 2026, with September Personal Income and Outlays listed for
October 29. The [BLS 2026 release calendar](https://www.bls.gov/schedule/2026/)
lists August JOLTS for September 29, September Employment Situation for
October 2, September CPI for October 14, September PPI for October 15, and
September import/export prices for October 16.
These are scheduled checkpoints, not guarantees that the resulting vintage
will be comparable or that a new causal claim will be warranted.

## Purpose

The atlas contains both slow research layers and recurring official releases.
Without a refresh control, a current-looking finding can silently become a
stale comparison or mix preliminary and revised vintages. This watchlist
records the latest usable vintage, the next expected recheck, and the evidence
that must be preserved when the source moves.

The watchlist is a control surface, not a forecast. A scheduled release may be
delayed, revised, or changed in definition. Every refresh must retain the old
vintage where a later release supersedes it.

**HTOPS/HPS page recheck (2026-09-17):** the [Census public-use datasets
page](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)
continues to list the July 2026 PUF and identifies corrected March and May
2026 files. The page was revised September 4, 2026; no new PUF was acquired
for this recheck. The local atlas already retains the July cross-sectional
comparison and the corrected-file weighting audit. The 2025
longitudinal-to-2026 cross-sectional design break remains a required boundary.

## Current refresh queue

| Source family | Latest usable vintage in atlas | Next expected check | Refresh action | Boundary that must remain visible |
|---|---|---|---|---|
| BEA Personal Income and Outlays | July 2026; [record](records/us-bea-personal-income-outlays-2026-july.json) | September 30 annual update; October 29, 2026 September flows | Archive July page/hash; separate annual-update revisions from the next monthly flow release | Aggregate national accounts are not household buffers or welfare |
| BEA GDP and Corporate Profits | Q2 2026 second estimate; [record](records/us-bea-gdp-corporate-profits-2026q2.json) | September 30, 2026 | Compare third estimate with second; preserve annual-rate units and profit definition | GDP/profits are not worker control, household gain, or firm-level market power |
| BLS JOLTS | January–July 2026; July preliminary | September 29, 2026 expected August release | Re-fetch openings, hires, quits, layoffs, and separations; preserve preliminary/final status | Establishment rates are not individual transition probabilities |
| BLS Employment Situation | August 2026; establishment August preliminary | October 2, 2026 expected September release | Re-fetch CPS and CES separately; retain revisions to prior months | Household and establishment surveys have different universes |
| BLS Consumer Price Index | August 2026; [record](records/us-bls-cpi-2026-august.json) | October 14, 2026 expected September release | Re-fetch CPI-U all-items, core, food, energy, gasoline, and shelter; preserve seasonal-adjustment status and category definitions | CPI-U is an aggregate urban price index, not household-specific hardship, affordability, or lived inflation |
| BLS Producer Price Index | August 2026; [record](records/us-bls-ppi-2026-august.json) | October 15, 2026 expected September release | Re-fetch final/intermediate demand, energy, diesel, and revision notes; preserve seller-side versus consumer-side definitions | PPI is an upstream seller-side index, not automatic consumer pass-through, firm margin, or household burden |
| BLS Import and Export Price Indexes | August 2026; official page rechecked September 17, 2026 | October 16, 2026 expected September release | Preserve import/export, fuel/nonfuel, locality, terms-of-trade, and revision fields; the current release reports import prices +7.0% year over year and export prices +8.6% | Cross-border price movement is an upstream trade and competitiveness signal, not a tariff incidence, consumer pass-through, firm margin, or geopolitical leverage estimate |
| BLS CES selected earnings | January–August 2026; July/August preliminary | October 2, 2026 expected September data | Re-run series-page fetcher; preserve page hashes and partial-year denominator | Sector means are not worker wage trajectories or real purchasing power |
| Federal Reserve SHED | 2025 annual survey and linked credit records | Next annual publication; date not yet fixed in this atlas | Preserve question wording, linked-sample consent, and subgroup denominators | Hypothetical capacity and linked records are distinct from transactions |
| USDA ERS household food security | 2024 annual report; [machine record](records/usda-food-security-2024.json) | Next annual report; date not yet fixed in this atlas | Recheck the ERS report/media page, preserve CPS-FSS vintage, household denominator, severity definition, and statistical-significance notes; the media page was updated July 28, 2026 without a newer annual estimate | Annual household food security is not a dated grocery, benefit, price, health, trust, or political-action episode |
| CMS National Health Expenditure Accounts | 2024 historical accounts; 2025–2034 projections | Next annual NHE release or projection update; date not yet fixed in this atlas | Preserve service, payer, sponsor, GDP-share, projection, and methodology vintages; keep NHEA separate from household surveys | National spending and sponsor shares are not household affordability, care access, debt, time burden, or health outcomes |
| MEPS / Panel 27 and HC-256 | 2024 full-year HC-256 release; 2022–2023 Panel 27 longitudinal analysis | 2023–2024 Panel 28 longitudinal file and next annual MEPS update | Preserve panel/round universe, PERWT24F/LONGWT, VARSTR, VARPSU, valid-field denominators, expenditure definitions, and revisions | A newer file and structural scan are not yet a 2024 estimate or dated bill-to-care episode |
| IMF Financial Access Survey | 2025 release; US SDMX extract through 2024 and cross-country comparison | Next annual FAS release; date not yet fixed in this atlas | Preserve API query, indicator code, transformation, country availability, and raw-response hash; separate downloaded US payload from undownloaded report PDF | Provider counts, branch density, and balance-to-GDP ratios are not household access, affordability, welfare, or remedy |
| SIPRI Military Expenditure Database | 2025 estimates released in 2026; global, national, regional, and NATO aggregates | Next annual military-expenditure release; date not yet fixed in this atlas | Preserve current/constant-dollar basis, exchange-rate treatment, estimates, fiscal-year conventions, alliance aggregation, and report hash | Spending is resource allocation, not readiness, production, delivery, deterrence, domestic incidence, or leverage |
| LBNL data-center energy analysis | 2025 national estimate and 2030 reference/sensitivity scenarios | Next annual or major scenario update; date not fixed | Preserve historical versus modeled status, scenario assumptions, equipment/utilization/cooling boundary, and report hash | Modeled load is not observed demand, approved interconnection, household bills, local incidence, or geopolitical capacity |
| New York Fed household debt and credit | 2026 Q2 aggregate dashboard | Q3 release; date to be confirmed | Snapshot balances, delinquency, dashboard notes, and any methodology change | Aggregate credit cannot identify which households bear stress |
| Census HTOPS/HPS | July 2026; March and May PUFs corrected September 10, 2026; linked April–June 2025 panels | Next public-use release; monitor weekly | Preserve correction note, design-break, replicate-weight, and linked-sample notes; do not interpolate an unlisted August wave | Repeated snapshots are not automatically same-person panels |
| GSS / NORC | 1972–2024 historical comparison and 2024 financial-position/trust layer | Next annual or public-use release; date not fixed | Preserve question availability, mode, weights, wording, and changing sample/design coverage before comparing years | Repeated cross-sections are not same-person exposure-to-action panels |
| CFPB Consumer Complaint Database | 2025 annual; live recheck 2026-09-14 returned 5,452,107 records and index total 17,737,752 | Ongoing API refresh | Capture index timestamp, query universe, fields, raw-response hash, and snapshot hash | Complaint visibility and response labels are not verified remedy rates |
| SIPP | 2024 reference-year analysis from 2025 file | Next public-use annual file; date to be confirmed | Re-run field/universe and Fay-BRR checks when a new file appears | Person records, household fields, and monthly/reference-period measures differ |
| PSID | Pre-acquisition; no local microdata | When account-controlled files are supplied | Run structural wave audit before merge or estimate | Access gate is not a null result; no estimate may be inferred |
| World Bank Enterprise Surveys AI follow-up | Metadata/access record; authenticated microdata not obtained | When portal access is available | Download US/comparison files, document survey design, then audit variables | Public catalog metadata are not firm adoption or employment estimates |
| JASSM-ER delivery watchpoint | Official schedule/context through September 14, 2026 | Recheck on next official acceptance, delivery, fielding, or schedule event | Search US/partner defense records; preserve non-observation as such | A missing public event is not proof that no delivery occurred |
| Large-load state utility governance | Virginia approved/implementation records, Texas proposed rule, Georgia filing/disclosure records through 2026 | Event-driven: next order, rule, hearing, filing, or operational-stress report | Preserve approved versus proposed versus modeled terms, customer class, docket, disclosure status, and event timing | Filed allocation terms and load events are not observed household bills, net public benefit, reliability failure, or public trust |
| CPSC consumer safety and recall systems | FY2024 annual performance report; current recall/data-system pages; 2025 NEISS treatment data available for query | Event-driven and annual: new performance report, recall dataset, remedy update, NEISS release, or major enforcement action | Preserve fiscal/calendar year, recall versus warning versus violation notice, product/unit denominator, import/takedown scope, NEISS sample and coding vintage, and remedy status | Recall, takedown, or injury-surveillance activity is not consumer exposure, awareness, remedy receipt, avoided injury, or household recovery |
| ENERGY STAR program and product criteria | 2023 annual overview; 2024 Most Efficient criteria and current impacts page | Annual criteria and impact refresh; product-category criteria may change on a separate schedule | Preserve criteria version, federal-minimum comparison, modeled versus observed savings, partner/household denominator, product category, and rebate/installation route | Label recognition, partner reach, and modeled savings are not household purchase, installation, use, or realized bill reduction |
| New York DFS insurance recourse and availability | 2025 consumer-protection annual report; 2025 availability survey and homeowners reporting instructions | Annual report and event-driven data-call/complaint/market releases | Preserve complaint category, closure and positive-outcome definition, recovery accounting, insurer reporting universe, cancellation/nonrenewal fields, and state geography | Complaint recovery and reporting requirements are not market-wide availability, adequate claims, repair, mobility, or trust |
| Pew Fiscal 50 state fiscal buffers | Fiscal 2025 rainy-day and total-balance analysis; tax-revenue context through early 2025 | Annual fiscal-year refresh and event-driven state budget revisions | Preserve fiscal year, reserve versus ending balance, days-of-operations denominator, state coverage, revenue vintage, and policy changes | State reserve capacity is not a household buffer, service outcome, disaster recovery, or political legitimacy |

## Required refresh record

For every recurring-source update, append or regenerate a record containing:

- source URL, retrieval date, page or file title, release date, and vintage;
- exact unit, geography, denominator, seasonality, and preliminary/revised
  status;
- retrieval hash for a downloaded artifact or an explicit page-vintage note;
- changes from the prior release, including revised historical values;
- subgroup, coverage, nonresponse, and design changes;
- counterinterpretations and any broken comparability;
- links to the affected machine record, finding, dashboard, and open-arrow
  entry; and
- the next expected check or an explicit “date not fixed” status.

Do not overwrite a previous record merely because the source page now shows a
new value. A revision is part of the finding's history.

## Promotion rule

A refreshed source may update a finding's date or context without changing its
interpretation. Promote a new substantive claim only when the new vintage
adds a changed measure, a new subgroup/place, a reversal, a verified
institutional response, or a stronger same-unit/matched design. If a release
changes definitions, publish a comparability warning before calculating a
trend.

## Current open dependencies

1. **PSID:** account acceptance and file delivery are required before the
   material/time/care extract can move from specification to evidence.
2. **World Bank Enterprise Surveys:** authenticated microdata and survey
   documentation are required before firm-level AI estimates can enter the
   atlas.
3. **Same-unit bridges:** BLS, BEA, Fed, SIPP, CFPB, and New York Fed refreshes
   improve context but do not create a worker/household/firm event key.
4. **Meaning and action:** trust, dignity, identity, political judgment, and
   exit remain open unless a source measures them in relation to a defined
   encounter or event.

## Reproduction links

- [BEA release schedule](https://www.bea.gov/news/schedule)
- [BLS release calendar](https://www.bls.gov/schedule/news_release/)
- [BLS CPI program and data](https://www.bls.gov/cpi/)
- [Federal Reserve SHED](https://www.federalreserve.gov/consumerscommunities/shed.htm)
- [USDA ERS food security media resources](https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/media-resources)
- [New York Fed household debt and credit](https://www.newyorkfed.org/microeconomics/hhdc)
- [CFPB complaint database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- [PSID packaged-data page](https://simba.isr.umich.edu/Zips/ZipMain.aspx)
- [World Bank Enterprise Surveys data updates](https://www.enterprisesurveys.org/en/data/data-updates)
