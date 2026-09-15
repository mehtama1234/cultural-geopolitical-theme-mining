# California DOI wildfire-risk county context layer v1

The California Department of Insurance's 2022 voluntary-market ZIP workbook
can be aggregated by county and joined to CDI's published county exposure
appendix. Among 56 matched counties, the top equal-count quartile by modeled
high/very-high wildfire share had a weighted voluntary nonrenewal rate of
11.31% among renewed plus nonrenewed decisions, compared with 9.98% in the
bottom quartile. Using CDI's statewide 12.1% exposure share as a threshold,
the corresponding rates were 11.01% at or above the threshold and 10.42%
below it.

```text
modeled wildfire exposure context
  + voluntary-market nonrenewal decisions
  -> a modest county-level availability gradient in this screen
  -> FAIR/private-market interaction, affordability, claims, repair, and
     household mobility (still open)
```

This is a conditioning pass, not a replacement for the ZIP-level FAIR-share
crosswalk. The CDI exposure appendix uses Department of Finance dwelling-unit
estimates dated January 1, 2015, while the voluntary counts are from 2022;
the exposure share is a weighted model estimate, not observed loss. County
aggregation also hides within-county variation, and the voluntary workbook's
policy universe does not equal the FAIR residential-structure universe.

The companion CDI insurer workbook reports statewide earned premium, exposure,
average coverage, and claim/loss counts by wildfire-risk score for 2018–2023.
It extends the market-risk trend but has no household or county key, so it is
not silently merged into the county panel.

## Next test

Find a compatible year/state panel with county or ZIP premiums, FAIR enrollment,
voluntary coverage, claims, repairs, and household/property outcomes. Preserve
the temporal mismatch until a same-period exposure measure is available.
