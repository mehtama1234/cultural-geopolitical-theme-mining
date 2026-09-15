# HTOPS/HPS 2026 question-harmonization audit v1

**Checked:** 2026-09-14  
**Scope:** March 2026, corrected May 2026, and July 2026 Census HTOPS/HPS
public-use files  
**Status:** headline variables text- and codebook-aligned for descriptive
comparison; not a panel or causal design

## Audit result

The headline variables used in the cross-wave record are present in all three
public-use dictionaries with the same question text and substantive response
coding:

- `EXPENSE_DIFFICULT`: usual household expense difficulty over the last two
  months;
- `FD_SUFF`: food sufficiency over the last seven days;
- `ENERGY`: reduced/forgone basic necessities to pay an energy bill over the
  last two months;
- `TRUST_FEDSTAT`: tendency to trust federal statistics;
- `TRUST_CONGRESS`: confidence in Congress;
- `RHHINCOME`: 2025 household-income bands;
- `ESEX`: edited male/female category; and
- `THHLD_NUMKID`: children under 18 in the household.

The July `FD_SUFF` dictionary does not list a `-88 Not in universe` value,
whereas March and corrected May do. The extraction excludes `-88` wherever it
appears and reports item-specific valid denominators. This difference does not
change the substantive four-category food coding, but it is retained as a
missingness/routing note rather than silently treating the files as identical.

## File and method controls

| Release | Collection period | PUF respondents | ZIP SHA-256 | Dictionary SHA-256 |
|---|---|---:|---|---|
| March 2026 | March 13–30, 2026 | 12,521 | `7bcd56139bf3997901db78dbf75f20f0aebfa919b188c2d5b6ae9350df9c6d1` | `788d683ca91668d61fd9516278b71348c430b6ebf145e6d3a7dbdbdd1c635794` |
| May 2026 corrected | April 29–May 18, 2026 | 12,636 | `7bd1d26ed2aaa88d4f12c9b51bca6d284cc3a19891144e000d873b9d80837667` | `dee1baafaacfb3685d36dc7d244867314a22696133f0a55c67e7d31a31b20eab` |
| July 2026 | July 15–August 3, 2026 | 12,755 | `43980716428de1b6e2a215973f31b0f0a0af4317107a97ef889dbf569d207a31` | `f91b0509a92e00218c8c59aa61237b5b494641860af5e72fc9e30143d9590585` |

The March and May ZIPs are the corrected files linked by the Census release
page. Each package includes a PUF, a replicate-weight file, and a data
dictionary. The comparison uses `PWEIGHT`, excludes item-specific `-88` and
`-99` values, and applies the Census successive-difference formula to the 80
replicate weights:

```text
Var(theta_hat) = 4 / 80 * sum((theta_i - theta_hat)^2)
```

## Interpretation boundary

Exact wording alignment supports a descriptive period comparison. It does not
remove differences in sample composition, nonresponse, seasonal conditions,
survey mode, weighting, or the documented change from longitudinal HTOPS in
2025 to cross-sectional HPS-focused releases in March 2026. The cross-wave
record therefore reports weighted distributions and approximate independent-
snapshot contrasts, not same-person change or causal effects.

## Sources

- [Census HTOPS/HPS public-use files](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)
- [Census user notes](https://www.census.gov/programs-surveys/household-pulse-survey/technical-documentation/user-notes.html)
- [Census technical-documentation directory](https://www2.census.gov/programs-surveys/demo/technical-documentation/hhp/)
- [Cross-wave machine record](../../records/us-census-htops-hps-material-trust-crosswave-2026.json)
- [Cross-wave record builder](../../../scripts/build_htops_hps_2026_crosswave_record.py)
