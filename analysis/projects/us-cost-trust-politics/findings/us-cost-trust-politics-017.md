# Three 2026 Census pulse snapshots show movement without a single household story

**Status:** provisional replicate-weighted cross-sectional comparison · **Checked:** 2026-09-14

## The bounded finding

Corrected March, corrected May, and July 2026 HTOPS/HPS public-use files show
that household pressure, energy trade-offs, food insufficiency, and
institutional judgment do not move as one block. The broad share reporting any
difficulty with usual expenses was 51.2% in March, 49.8% in corrected May, and
49.8% in July. Food insufficiency moved 6.5% → 8.3% → 7.4%; the share
reporting that the household reduced or forgone basic necessities to pay an
energy bill moved 12.8% → 14.9% → 12.7%. Trust in federal statistics moved
52.1% → 49.7% → 51.5%, while high confidence in Congress moved 18.2% → 18.3%
→ 17.3%.

The meaningful result is the divergence: a broad expense measure was nearly
flat from May to July while narrower food and energy measures changed, and
institutional judgments moved on their own path. These are independent
cross-sectional snapshots, not within-person changes. They do not establish a
price cause, recovery, institutional blame, or a political response.

## Replicate-weighted comparison

Values are weighted percentages; parentheses show the Census successive-
difference replicate-weight standard error in percentage points. The files
were released as public-use PUF, replicate-weight, and dictionary packages; the
March and May files were the corrected versions identified in the Census user
notes.

| Measure | March 2026 | May 2026 corrected | July 2026 | Reading boundary |
|---|---:|---:|---:|---|
| Any difficulty paying usual expenses | 51.2 (1.25) | 49.8 (1.31) | 49.8 (1.14) | Broad household-room measure; not a bill amount |
| Sometimes/often not enough food | 6.5 (0.84) | 8.3 (0.91) | 7.4 (1.12) | Seven-day food-sufficiency item; not annual food security |
| Reduced/forgone basic needs to pay energy bill | 12.8 (0.83) | 14.9 (0.94) | 12.7 (1.18) | Two-month energy trade-off; no arrears duration or remedy |
| Tends to trust federal statistics | 52.1 (1.36) | 49.7 (1.09) | 51.5 (1.12) | One institutional object; not generalized government trust |
| Great deal/quite a lot confidence in Congress | 18.2 (0.91) | 18.3 (0.84) | 17.3 (0.89) | Confidence is not legitimacy, attribution, or political action |

The full machine-readable record also preserves income, sex, children-present,
and no-children domain estimates. The income contrast is persistent but not
constant: any expense difficulty was 63.3%, 60.8%, and 64.2% among respondents
in the under-$50,000 household-income bands, versus 36.9%, 35.1%, and 35.0%
among respondents in the $100,000-plus bands. These are subgroup distributions,
not an estimate of an income effect; composition, question nonresponse, and
other household resources remain relevant.

For a formal but deliberately limited contrast screen, the approximate 90%
independent-snapshot interval for the March-to-May energy trade-off difference
is 0.0 to 4.2 percentage points (difference +2.1); the corresponding May-to-
July interval is -4.7 to 0.3 (difference -2.2). The March-to-May food
insufficiency interval is -0.2 to 3.8 (difference +1.8), and the May-to-July
interval is -3.3 to 1.5 (difference -0.9). These intervals are computed from
the separate replicate-weight standard errors and are not a substitute for a
design-aware pooled test or a same-person comparison. The record preserves the
full contrast table, including the income domains and institutional measures.

## What the comparison changes

### 1. “Household pressure” needs an endpoint

The broad expense question is comparatively stable while food insufficiency and
energy trade-offs show larger period movement. A single pressure index would
hide whether a household is reporting anticipated prices, payment difficulty,
material sacrifice, or an immediate food endpoint. The atlas should keep these
currencies separate until overlap and timing are measured.

### 2. Income gradients persist without becoming a causal story

The under-$50,000 domain is consistently more exposed on the broad expense
measure than the $100,000-plus domain, and the gap remains visible in all three
snapshots. This supports unequal exposure as a recurring descriptive pattern.
It does not identify liquid assets, family support, housing costs, debt, local
prices, or which alternative each household used.

### 3. Trust is neither a simple lag nor a direct hardship response

Federal-statistics trust falls in the corrected May snapshot and rises in July,
while broad expense difficulty is nearly unchanged from May to July. That
co-movement pattern is inconsistent with reading the trust measure as a simple
mechanical lag of the broad expense item. It is still not evidence of a causal
relationship: the survey does not measure the respondent's attributed event,
messenger, news environment, or subsequent action.

### 4. The survey design break matters

The Census documentation says HTOPS used a longitudinal design throughout 2025
and shifted to a cross-sectional HPS-focused design beginning in March 2026.
Therefore the three 2026 files can be compared as repeated population
snapshots, but not as a recontact panel. A 2026 movement cannot be described as
the same households recovering or deteriorating without a valid identifier and
panel design.

## Counterexamples kept visible

- A stable broad expense share can coexist with movement in food or energy
  endpoints because the questions have different universes and reference
  periods.
- A persistent income gradient does not imply that income alone caused the
  pressure; housing, health, debt, family help, and local prices can differ.
- Trust in federal statistics can rise while confidence in Congress falls;
  institutional objects and response scales differ.
- A point change larger than its displayed standard error is not by itself a
  complete difference test; independent-snapshot comparison, wording, design,
  and nonresponse checks still matter.

## Next end-to-end test

Use the subgroup cells to select a dated event design: actual price or energy
exposure, resource alternatives, immediate substitution, food/health/work
outcome, and later trust or action. Pair the Census snapshots with SHED,
WBNS, SIPP, and administrative route records only as complementary populations
unless a valid person-level join exists. The next reproducible statistical
extension is a formal independent-snapshot contrast table with confidence
intervals and harmonized question-universe checks; the next substantive design
is a same-person follow-up, not a larger aggregate index.

## Sources and reproducibility

- [Census HTOPS/HPS public-use files](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)
- [Census user notes](https://www.census.gov/programs-surveys/household-pulse-survey/technical-documentation/user-notes.html)
- [Machine-readable March/May/July comparison](../../../records/us-census-htops-hps-material-trust-crosswave-2026.json)
- [Replicate-weighted comparison builder](../../../../scripts/build_htops_hps_2026_crosswave_record.py)
- [Question-harmonization audit](../htops-2026-question-harmonization-audit-v1.md)
- [July 2026 detailed finding](us-cost-trust-politics-016.md)
- [Federal Reserve 2025 price-adaptation and judgment record](../../../records/us-federal-reserve-price-adaptation-judgment-2025.json)
- [WBNS route-to-security synthesis](../../us-safety-net-access/public-system-route-to-security-triangulation-v1.md)

**Evidence status:** three corrected official cross-sectional public-use files,
with 80-replicate successive-difference standard errors and explicit subgroup
domains; no same-person sequence, causal exposure, attribution, recovery,
trust mechanism, or political-action result is claimed.
