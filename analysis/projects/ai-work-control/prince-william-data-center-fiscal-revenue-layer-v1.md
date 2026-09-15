# Prince William data-center fiscal revenue layer v1

The official Prince William County **2024 Data Center Revenue Report** and its
county-linked **2025 Data Center Revenue Report** add a local public-revenue
series to the existing GIS pipeline and national energy layers. The 2012–2024
report reports data-center industry tax revenue rising from $6.5 million to
$293.7 million, with the 2024 value marked preliminary. The 2025 report adds a
reported $465.9 million in TY2025, up 59% year over year. The series is an
industry aggregate, not a household bill or net-benefit estimate.

| Tax year | Reported data-center revenue ($m) | Year-over-year growth | Computer-equipment rate ($/$100) |
|---:|---:|---:|---:|
| 2012 | 6.5 | — | — |
| 2018 | 36.7 | 31% | 1.25 |
| 2020 | 65.4 | 23% | 1.35 |
| 2022 | 110.8 | 29% | 1.65 |
| 2023 | 166.4 | 50% | 2.15 |
| 2024* | 293.7 | 77% | 3.70 |
| 2025 | 465.9 | 59% | 4.15 |

The reports attribute revenue to real property, computer equipment and
peripherals, furniture and fixtures, and fees/licensing. The TY2025 report
additionally reports $221.8 million real-property revenue, $218.1 million
computer-equipment revenue, 621 MW of new capacity, 1,483 MW of turnkey total
power capacity, and 55 turnkey/powered-shell facilities. The 2024 report
reports 862 MW of turnkey capacity and 240 MW added in 2024. The revenue series should not be
divided by that capacity and called a rate: the tax base, assessment rules,
equipment depreciation, building completion, and tax policy all change over
time. The county states that the computer-equipment rate rose from $2.15 in
2023 to $3.70 in 2024 and estimates roughly $51.9 million of 2024 computer-
equipment revenue was attributable to that rate increase under constant-value
assumptions.

```text
local project/pipeline -> assessed property and equipment -> public revenue
public revenue -> services, tax policy, legitimacy, and local bargaining room (open)
physical load -> utility cost, water, environment, and household incidence (open)
```

This strengthens the local pipeline-to-public-revenue arrow. It does not show
who ultimately benefits, whether public-service costs or externalities offset
revenue, whether residents' bills changed, or whether the fiscal stream
produced public support, opposition, or durable state capacity. The 2022 PFM
fiscal-impact study is a separate modeled cost-benefit exercise and must not be
silently pooled with this county-reported revenue series.

Reproduction: `python3 scripts/build_pwc_data_center_fiscal_record.py --output
analysis/records/us-prince-william-data-center-fiscal-revenue-2012-2024.json`.

Source: [Prince William County Finance and Revenue](https://www.pwcva.gov/department/finance/finance-and-revenue),
[TY2024 Data Center Revenue Report](https://www.pwcva.gov/assets/2025-06/Prince%20William%20County%202024%20Data%20Center%20Revenue%20Report.pdf).

## 2025 extension and acquisition note

The county Finance and Revenue page links the [TY2025 Data Center Industry Tax
Revenue Report](https://www.flipsnack.com/B8877D99E8C/2025-data-center-revenue-report.html),
published on the flipbook page on 2026-07-21 and modified 2026-09-10. Its
signed reader data was retrieved on 2026-09-13 and the decompressed structured
artifact is hashed in the [2025 extension record](../../records/us-prince-william-data-center-fiscal-revenue-2025-extension.json).
The extension is separate from the 2024 record because the source format
changed from a county PDF to a county-linked publication. Reproduction:
`python3 scripts/build_pwc_data_center_fiscal_2025_extension.py --output
analysis/records/us-prince-william-data-center-fiscal-revenue-2025-extension.json`.
