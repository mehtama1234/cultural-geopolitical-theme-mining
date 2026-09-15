# California FAIR/private-market ACS context layer v1

The 2022 California FAIR/private-market ZIP comparison can be conditioned on
place-level ACS income and housing structure context. The join matches 1,591
of 1,719 FAIR ZIP rows to usable 2022 ACS ZCTA estimates.

In equal-count quartiles, the lowest-income ZIPs had a 12.34% voluntary
nonrenewal rate among renewed plus nonrenewed decisions, versus 9.80% in the
highest-income ZIPs. ZIPs with the highest share of one-unit detached homes
had an 11.68% rate versus 10.06% in the lowest detached-share quartile. The
low-income group also had a higher mean FAIR share (8.96% versus 4.55% in the
high-income group); the high-detached group had a higher mean FAIR share
(14.08% versus 3.79%).

```text
FAIR share + voluntary nonrenewal
  + income and housing-structure context
  -> the association is partly distributed across place composition
  -> household affordability, coverage loss, repair, and mobility (open)
```

ACS income and structure measures are five-year ZCTA estimates, not the
income or property type of insured households. The FAIR table counts
residential structures, while the voluntary workbook counts broader policy
forms. The quartiles are unweighted by population, structures, or policies;
therefore this is a place-composition screen, not an adjusted estimate.

## Next test

Combine the income, structure, county-risk, and FAIR-share dimensions in a
transparent multivariable descriptive screen, then seek a same-period panel
with premiums, claims, repairs, and household/property outcomes.
