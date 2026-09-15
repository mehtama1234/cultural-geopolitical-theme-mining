# Treasury FIO × Census ZCTA context layer v1

The 2022 Treasury ZIP-code market rows can be matched to same-text 2022 Census
ACS ZCTA codes for a descriptive place-context screen. Of 25,593 Treasury
rows considered, 25,084 matched usable ACS context: 98.0%.

The first result complicates a simple inequality story. Among matched rows,
unweighted mean premiums were $1,630 in ZCTAs with median household income
below $50,000, $1,674 in the $50,000–$99,999 band, and $2,332 in the $100,000+
band. Mean nonrenewal rates moved in the other direction: 1.261% in the
lowest-income band versus 0.909% in the highest-income band. Places with an
owner share below 50% had both higher mean premiums ($2,127) and higher mean
nonrenewal (1.232%) than places with owner share at least 75% ($1,728 and
0.980%).

These are place-level, unweighted descriptive means. Higher-income or
lower-owner-share places may contain more valuable or exposed properties,
different policy mixes, and different insurer markets. The results do not
measure individual affordability or prove that income or tenure causes either
market outcome. The ZIP/ZCTA match is an approximation.

The useful supported pattern is:

```text
place composition and exposure
  -> different observed premium/nonrenewal profiles
  -> household affordability and coverage pressure (supported by the Fed survey,
     but not identified by this join)
  -> repairs, lending, mobility, and political response (open)
```

The next test is to add hazard geography and a later market year, then seek
property, mortgage, claims, repair, and move/stay outcomes at compatible units.
