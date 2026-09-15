# IMF WEO geopolitical, fiscal, and macro shock 2026 layer v1

**Checked:** 2026-09-13 · **Status:** official IMF report and database extraction

## Why this layer matters

The atlas already measures defense resources, infrastructure, household pressure, and state capacity in separate lanes. The IMF's April 2026 World Economic Outlook adds a macro bridge: geopolitical conflict and defense mobilization can alter growth, inflation, deficits, debt, external balances, and social spending at the same time. It is a conditional macro layer, not proof of a household or political outcome.

## Direct evidence

Under its limited-duration conflict assumption, IMF projects global growth of 3.1% in 2026 and 3.2% in 2027, with inflation rising modestly in 2026 before declining. The report identifies longer conflict, fragmentation, renewed trade tensions, and disappointment over AI productivity as downside risks.

For a typical defense-spending boom, IMF estimates defense outlays rise about 2.7 percentage points of GDP over roughly two and a half years, with about two-thirds financed through deficits. The average boom is associated with a 2.6-point fiscal-deficit increase and a 7-point public-debt increase within three years; wartime booms show about a 14-point debt increase and falling social spending. These are cross-country episode estimates, not a forecast for every country.

The April 2026 WEO database places US real GDP growth at 2.324% in 2026, period-average CPI inflation at 3.228%, unemployment at 4.376%, and gross general-government debt at 125.781% of GDP in 2026, rising to 142.113% by 2031 in that vintage. These aggregate projections do not identify who bears the adjustment.

## Mechanism under test

```text
geopolitical shock or defense mobilization
  -> commodity, trade, financing, and fiscal conditions
  -> inflation, debt, external balance, and social-spending trade-offs
  -> household/firm/place exposure and institutional legitimacy
  -> political response, alliance behavior, and state leverage
```

The IMF directly informs the macro/fiscal middle of this chain. Household incidence, attribution, legitimacy, unrest, alliance response, and geopolitical leverage require separate compatible records.

## Interpretation and limits

The important finding is joint movement: defense can raise short-run activity while increasing inflation, debt, external pressure, and the risk of crowding out social spending. Growth or fiscal capacity therefore cannot be treated as a one-dimensional proxy for social security or state power. The WEO numbers are conditional on assumptions and can be revised; the US series is an aggregate projection, not a lived-cost estimate.

The next test is to align IMF country/macroeconomic series with US defense procurement, energy and trade exposure, budget composition, household price/adaptation measures, and political judgment/action records. Preserve country, sector, household, firm, and respondent units rather than pooling them.

## Reproducibility

- [IMF World Economic Outlook April 2026](https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026)
- [IMF WEO database](https://data.imf.org/Datasets/WEO)
- [Full report PDF](https://www.imf.org/-/media/files/publications/weo/2026/april/english/text.pdf)
- [Database spreadsheet](https://data.imf.org/-/media/iData/External-Storage/Documents/2F78EE59F79143A7921E5E203D3AAA80/en/WEOApr2026all.xlsx)
- PDF SHA-256: `5c281721761f2ac8f8ae313ea977a0039539aa760039ea3717cf54002d82432a`
- Spreadsheet SHA-256: `b29239cb48f8b895d1e526070c4fde01147bc8f6bd3b86f636363bb6bd87fe7a`
