# California FAIR/private-market crosswalk layer v1

The California Department of Insurance publishes separate but geographically
joinable views of the insurance market. The voluntary-market ZIP workbook
contains annual new, renewed, and non-renewed policy counts for 2020–2023.
Statewide, the calculated nonrenewal share among renewed plus non-renewed
decisions was 10.60% in 2020 and 9.43% in 2023. CDI notes that some categories
changed beginning in 2020, so this is not a perfectly stable taxonomy.

The 2022 FAIR-versus-voluntary PDF reports residential dwelling structures by
ZIP. It matches 1,717 of 1,719 FAIR rows to the voluntary workbook. In a
descriptive equal-count quartile screen, the lowest FAIR-share quartile had a
mean FAIR share of 7.69% and a voluntary nonrenewal rate of 9.89%; the highest
quartile had a mean FAIR share of 26.77% and a voluntary nonrenewal rate of
12.40%.

This is the strongest state-level availability association added so far, but
the denominators are intentionally not merged:

```text
high FAIR share in a ZIP
  ↔ higher voluntary nonrenewal among observed renewal decisions
  → possible private/public market interaction
  → household coverage, affordability, claims, repair, and mobility (open)
```

The FAIR percentage is based on residential structures, while the voluntary
file includes a broader set of policy forms and counts. The result can reflect
wildfire risk, property composition, insurer mix, state rules, and reporting
thresholds. It is not a causal estimate or a same-household transition. The
next test is to condition the ZIP comparison on wildfire risk, income, property
type, and county, then add premiums, claims, and FAIR/voluntary policy outcomes
for later years.
