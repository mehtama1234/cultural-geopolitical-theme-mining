# SIPP housing-transition field audit v1

**Checked:** 2026-09-25  
**Status:** public-field availability and real-file timing audit confirmed; no housing-transition estimate  
**Source:** 2025 SIPP public-use file and Census 2025 SIPP API variable catalog

## Result

The public 2025 SIPP schema contains enough housing and work fields to justify
a bounded same-respondent availability rerun. The current local SIPP
extraction selected 35 fields for household security, work, care, utilities,
food, and debt, but it did not include the housing-assistance and residence
spell fields below. Therefore the current local outputs cannot answer the
housing-transition question yet, but the missing fields are identifiable in the
public schema rather than requiring an immediate restricted HUD–LEHD extract.

The Census microdata API exposes a raw-record query route for 2025 SIPP, but a
live data query returned the official missing-key response. No Census API key
is present in the workspace. The official public-use archive was nevertheless
available and was streamed locally for a bounded field/timing audit; the raw
uncompressed respondent file remains outside Git.

## Fields to add to the rerun

| Stage | 2025 SIPP field(s) | Schema meaning | Safe interpretation |
|---|---|---|---|
| Assistance | `EHOUSE_ANY`, `EEHC_RENTSUB`, `EEHC_VOUCHER`, `ERENTSUB`, `EVOUCHER`, `EOTHAS_MNYN` | Housing assistance, rent subsidy, voucher, and other assistance indicators | Receipt/availability indicator; not assistance amount, adequacy, or successful use |
| Residence spell | `EEHC_MVMO`, `EEHC_WHY`, `EEHC_TEN`, `EEHC_PVTEN`, `TEHC_MVYR`, `ERH_BMONTH`, `ERH_EMONTH` | Move timing, move reason, tenure, prior tenure, and residence-spell boundaries | Potential transition timing and reason context; not an administrative exit reason or forced/discretionary classification by itself |
| Housing cost | `TRENTMORT`, `EAWBMORT`, `EUTILITIES` | December rent/mortgage amount, inability to pay rent/mortgage, and separate utility payment | Household cost and reported difficulty; `TRENTMORT` is not a monthly bill series |
| Work/resources | Existing `THTOTINC`, `TPEARN`, `THINCPOV`, `RMNUMJOBS`, `RWKSPERM`, plus relevant status flags | Income, earnings, poverty ratio, jobs, and work weeks | Monthly work/resource context, subject to each field's universe and timing |
| Security/adaptation | Existing food, savings, debt, care, and time-loss fields | Food pressure, savings, debt, care constraints, and work-time loss | Adjacent household-security and trade-off outcomes; not verified recovery or trust |

The 2025 API catalog defines `EHOUSE_ANY` as assistance to help pay for
housing, `EEHC_RENTSUB` as rent-subsidy receipt for the residence,
`EEHC_VOUCHER` as housing-voucher receipt for the residence, `EEHC_WHY` as
reason for moving to the residence, and `TRENTMORT` as the household amount
paid for rent or mortgage in December of the reference period. The catalog
also defines `EAWBMORT` as inability to pay rent or mortgage.

## What this route could establish

With the person-month key already used by the local extraction—`SSUID` +
`SHHADID` + `PNUM` + `MONTHCODE`—a rerun could test:

```text
housing assistance or residence transition
  -> rent/mortgage difficulty and utility burden
  -> income, earnings, jobs, and work weeks
  -> care/time loss, food pressure, savings, or debt
  -> adjacent-period persistence or reversal
```

This would be a public same-respondent descriptive bridge. It could strengthen
the housing-to-household-room and housing-to-work lanes, and it could provide
a counterexample to the linked administrative HUD–LEHD and HEARS studies.

## What it cannot establish

SIPP does not by itself provide:

- HUD program identity, administrative eligibility, benefit amount, or agency
  decision history;
- a complete monthly rent series or exact due/payment date;
- landlord response, application effort, search inventory, or reachable units;
- whether a move was forced, desired, or caused by assistance loss;
- housing quality, neighborhood opportunity, or verified homelessness for every
  respondent;
- a remedy, appeal, receipt adequacy, durable recovery, trust, or political
  action endpoint; or
- a valid person-level join to HUD–LEHD or HEARS.

`EEHC_WHY` is a survey move-reason field, not a substitute for a classified
administrative exit reason. `TRENTMORT` is specifically a December-of-reference-
period household amount, so it must not be presented as a twelve-month monthly
rent trajectory. Household-level fields copied to each person's record must
not be counted as independent person observations.

## Rerun gate

Before producing an estimate, the extraction must:

1. verify every selected field and corresponding status flag in the 2025 schema;
2. document each field's reference period and universe;
3. preserve the full 12-month person-month key and household-level-copy flags;
4. use the appropriate person or household weight and replicate-weight method;
5. report valid-pair denominators and missingness for every transition;
6. define assistance entry, exit, continuation, and move windows before looking
   at outcomes; and
7. stop if the fields only support receipt/tenure context rather than a dated
   transition and a later outcome for the same unit.

The additive `housing-transition` extraction profile and its synthetic fixture
smoke test are now in `scripts/extract_sipp_household_calendar_slice.py` and
`scripts/test_sipp_housing_transition_extractor.py`. The real public-file
missingness/timing pass is recorded in the [SIPP housing-transition timing
report](sipp-housing-transition-timing-report-v1.md); its compact result is in
[`data/sipp-housing-transition-timing-audit-2025.json`](data/sipp-housing-transition-timing-audit-2025.json).
No substantive housing estimate is promoted by this audit. The raw SIPP file
remains outside Git.

The verified field list and access state are preserved in the [machine-readable
field manifest](data/sipp-housing-transition-fields-2025.json).

## Sources and local context

- [Census 2025 SIPP data page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [Census 2025 SIPP API variable catalog](https://api.census.gov/data/2025/sipp/variables.html)
- [Local SIPP field audit](../us-household-calendar-integration/sipp-field-audit-v1.md)
- [Local SIPP person-transition layer](../us-household-calendar-integration/sipp-person-transition-layer-v1.md)
- [Housing-transition next-test protocol](housing-transition-next-test-v1.md)
