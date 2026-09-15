# Prince William data-center fiscal-capacity bridge v1

This bridge places the county-reported fiscal series beside the county GIS
pipeline and the county-linked TY2025 capacity report. It is a matched-place
context, not a causal or household-incidence estimate.

| Observation | Source | Directly reported value | What it permits | What it does not permit |
|---|---|---:|---|---|
| TY2024 data-center tax revenue | County TY2024 report | $293.7M; preliminary | Local public-revenue visibility | Net benefit, service-cost recovery, household bills |
| TY2024 turnkey capacity context | County TY2024 report | 862 MW total; 240 MW added | Fiscal and capacity time-point context | Revenue per MW as a stable productivity or tax rate |
| TY2025 data-center tax revenue | County-linked TY2025 report, Table 8 | $465.9M; 59% reported growth | A later fiscal observation | Pure physical-growth effect, because the equipment rate rose from $3.70 to $4.15 per $100 |
| TY2025 revenue categories | County-linked TY2025 report | $221.8M real property; $218.1M computer equipment; $23.3M furniture/fixtures; $2.7M fees/licensing | Identifies the composition of the public-revenue stream | Who pays, who benefits, or whether costs offset revenue |
| TY2025 capacity context | County-linked TY2025 report | 621 MW added; 1,483 MW turnkey total; 55 turnkey/powered-shell facilities | Places the fiscal jump beside reported physical expansion | Utility load, water use, local employment, or completed-service delivery |
| Local pipeline geography | County GIS snapshot | 246 buildings; 75 campuses; 5.2% of planned campus GFA completed in the snapshot | Targets where infrastructure, service, and political-incidence records should be collected | Actual operating load or resident exposure |

The two fiscal reports and the GIS snapshot establish a bounded arrow:

```text
data-center development and equipment base
  -> assessed property/equipment and county tax revenue
```

The reports also support a cautious 2024-to-2025 descriptive comparison: the
reported revenue increase is approximately 58.5% from the published rounded
values ($465.9M / $293.7M - 1), consistent with the report's rounded 59%.
That comparison is not a rate or productivity measure. The tax-rate change,
asset depreciation, classification, building completion, and different report
formats are all live explanations.

The next arrows remain open:

```text
public revenue -> local service provision, tax distribution, or legitimacy
physical capacity -> electricity/water demand and utility cost allocation
local exposure -> household bills, jobs/wages, health, environment, or political action
county fiscal dependence -> bargaining room or state/geopolitical leverage
```

## Reproduction and source boundary

The 2012–2024 fiscal record is reproduced by
`scripts/build_pwc_data_center_fiscal_record.py`. The TY2025 extension is
reproduced by `scripts/build_pwc_data_center_fiscal_2025_extension.py`. The
GIS context is documented in the [GIS incidence layer](prince-william-data-center-gis-incidence-layer-v1.md).

Sources: [Prince William County Finance and Revenue](https://www.pwcva.gov/department/finance/finance-and-revenue),
[TY2024 Data Center Revenue Report](https://www.pwcva.gov/assets/2025-06/Prince%20William%20County%202024%20Data%20Center%20Revenue%20Report.pdf),
and the county-linked [TY2025 Data Center Revenue Report](https://www.flipsnack.com/B8877D99E8C/2025-data-center-revenue-report.html).
