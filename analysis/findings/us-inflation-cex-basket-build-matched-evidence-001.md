# The data can show groups, but not yet the same family over time

## Short answer

The BLS Consumer Expenditure Survey has the pieces for a better inflation story: spending by income quintile, spending by housing tenure, price categories, and public-use microdata. It also warns us how to read the pieces: the tables are population means and some estimates are suppressed when their relative standard error is high.

This is enough to build a careful group comparison. It is not yet enough to say that a particular renter in a particular income group faced a measured basket, lost a specific option, and then changed a vote. The dimensions exist, but they must be joined without pretending that separate averages are a panel.

## What the matched evidence shows

| Data piece | What it can answer | What it cannot answer alone |
|---|---|---|
| Income-quintile table | How average spending and shares differ across five income groups. | How a renter's basket differs from an owner in the same income group. |
| Housing-tenure table | How average spending and shares differ for renters and owners. | How low-income renters differ from high-income renters without a cross-tab or microdata. |
| Two-year cross-tabs | How some pairs of characteristics can be compared over two years and selected regions. | A full low-income-renter product basket in every place. |
| Public-use microdata | Expenditure, income, and demographic responses for individual consumer units, subject to survey design and disclosure limits. | A true panel that follows the same consumer unit through all years. |
| RSE and suppression rules | Which published estimates are too uncertain for release. | A reason to fill missing cells with guesses. |

Sources: [BLS CE tables](https://www.bls.gov/cex/tables.htm), [BLS CE tables guide](https://www.bls.gov/cex/tables-getting-started-guide.htm), and [BLS CE public-use microdata](https://www.bls.gov/cex/pumd.htm).

## The connection

```text
income group + housing tenure
  -> average spending pattern
  -> price categories and real wage
  -> possible household pressure
  -> choice or trust
```

The first arrow is a group comparison. The later arrows are a test, not a fact. The most important missing bridge is the same consumer unit's income, tenure, purchases, and later response.

## Four views

**Household:** Start with income and tenure, then ask which bills and choices remain hidden.

**Customer:** Add product, size, quality, and substitute to the group average.

**Money and finance:** Report means, shares, standard errors, and suppressed estimates instead of a false precise number.

**Public power:** Do not turn a group average into a claim that every person felt or voted the same way.

## What would change the finding

- A permitted 2024 table export or microdata download with a reproducible checksum.
- A field dictionary mapping income, tenure, rent, food, transport, health, debt, and savings.
- Weighted estimates with standard errors for low-income renters and comparable owners.
- Repeated outcome data that can test choice, trust, and voting after the spending measure.

## Next test

Obtain the permitted BLS files, audit their fields, and produce one table with four groups: low-income renter, higher-income renter, low-income owner, and higher-income owner. Mark every cell as observed, estimated, suppressed, or not available.

## Reading rule

Do not call a demographic table a household panel. State whether the number describes a group, a consumer unit, or the same consumer unit over time.
