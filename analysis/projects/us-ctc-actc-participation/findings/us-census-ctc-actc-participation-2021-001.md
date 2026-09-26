# Finding 001: High participation does not mean every eligible dollar reached households

**Status:** bounded tax-credit access and household-room finding · **Checked:** 2026-09-22

## The bounded finding

The Census Bureau's Center for Economic Studies working paper links the 2022
CPS ASEC to IRS administrative data to estimate Child Tax Credit and Additional
Child Tax Credit participation for tax year 2021. It reports that 91% of
eligible taxpayers participated, while dollar participation was 85%. The year
was unusual because the American Rescue Plan temporarily expanded the credit.

The route is:

```text
eligible taxpayer or family
  -> filing, claim, and administrative match
  -> taxpayer participation
  -> dollars received and timing
  -> food, housing, care, debt, and household security [open]
```

The important distinction is between people counted as participating and the
amount of eligible dollars that reached them. Those are related but not
identical endpoints. Neither one shows whether the payment was timely,
adequate, or enough to change a family's material position.

## What this adds to the broader atlas

This adds a tax-benefit version of the program's formal-availability-versus-
usable-protection pattern. Linking survey eligibility to IRS receipt improves
measurement, but the measured endpoint is still participation and dollar
receipt—not household relief. It also creates a useful counterexample to
reading one high take-up percentage as a complete policy success.

## Limits and counterexamples

- The source is a working paper, not a final reviewed Census publication.
- Taxpayer participation and dollar participation are different measures and
  should not be subtracted as if they had the same denominator.
- The paper concerns tax year 2021 and a temporarily expanded credit.
- The public abstract does not show all eligibility, matching, subgroup, or
  payment-timing details.
- Receipt does not establish adequacy, spending, child wellbeing, poverty
  reduction, or durable household security.

## Next decisive test

The next useful artifact is a protected eligible-taxpayer-to-household ledger
joining eligibility, filing, claim, payment timing and amount, child expenses,
debt, food and housing room, later income, and wellbeing. That would show
whether high participation translated into usable and durable protection.

## Source

- [Census CES Working Paper: CTC and ACTC Participation Results](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-49.html)
- [Census research catalog context](https://lehd.ces.census.gov/applications/creat/viewbytag?tags=223)
- [Machine-readable trend record](../../../records/us-census-ctc-actc-participation-2021.json)

**Evidence status:** the official Census working paper reports 91% taxpayer
participation and 85% dollar participation for tax year 2021; adequacy,
timing, and household outcomes remain open.
