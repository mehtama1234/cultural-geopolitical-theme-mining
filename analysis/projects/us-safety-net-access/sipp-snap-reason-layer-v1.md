# SIPP SNAP start and end reason layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file, 2024 reference year  
**Unit:** SNAP-owning person-month record  
**Weight:** `WPFINWGT`  
**Method:** weighted descriptive reason distributions; no replicate-weight variance estimate

This layer follows the monthly SNAP receipt work into the documented reasons
for starting and ending a SNAP spell. It adds mechanism categories to the
broad public-systems map, but it is not a causal analysis of eligibility,
administrative burden, or food security.

## Overall start reasons

The file contains 22,388 valid owner records with a documented start reason.

| Reason SNAP began | Weighted share |
|---|---:|
| Became disabled or otherwise unable to work | 28.05% |
| Other | 18.21% |
| Loss or reduction of other income | 14.49% |
| Job loss/layoff or wages reduced | 11.63% |
| New child/dependent or pregnancy | 10.40% |
| No change—decided it was time | 5.90% |
| Needed to recertify | 4.55% |
| Separation, divorce, or widowhood | 4.11% |
| No change—heard about the program | 2.66% |

## Overall end reasons

The file contains 1,463 valid owner records with a documented end reason.

| Reason SNAP ended | Weighted share |
|---|---:|
| Other | 42.55% |
| Became ineligible because income increased | 32.09% |
| Still eligible but could not/chose not to collect | 8.10% |
| Requirements not met | 5.42% |
| Time limit reached | 5.80% |
| Benefits not worth the trouble | 3.62% |
| Ineligible because of family changes | 2.42% |

## Resource context

The distribution varies across monthly income-resource bands. Among start
records, the “became disabled or otherwise unable to work” category accounts
for 34.4% below poverty, 28.5% at 1–1.99 times poverty, 20.1% at 2–3.99
times poverty, and 19.8% at 4 times poverty or more. Among end records,
“income increased” accounts for 20.8%, 43.2%, 36.6%, and 20.3% across those
same bands respectively. The band-specific end counts are small, so these are
descriptive signals rather than a monotonic policy effect.

## What this adds

The start reasons show that SNAP entry is connected to several kinds of
household change: health/work capacity, income loss, job loss, family change,
and information or recertification. The end reasons show that “exit” contains
different states: improved income, family change, unmet requirements, time
limits, continued eligibility with non-collection, and benefits judged not
worth the trouble. A caseload decline or receipt transition cannot be given one
meaning without this classification.

This is the bridge from public-program participation to the event ledger. It
still does not tell us whether the recorded reason was selected under
administrative pressure, whether a notice was understood, what effort the
household spent, or what happened to food, work, debt, health, or trust after
the transition.

## Verification and limits

- 379,215 primary person-month rows were read from the full SIPP slice.
- Start and end reasons were restricted to `ESNAP_OWN = PNUM`, as required by
  the dictionary’s owner universe.
- The `ASNAP_BRSN` and `ASNAP_ERSN` status flags were applied; blank and
  not-in-universe records were excluded.
- The start and end records are not necessarily the same people or the same
  spell, and the reason distributions use different denominators.
- Estimates use the person weight and do not include replicate-weight standard
  errors. They should not be treated as precise national rates.
- “Other” remains a large category, and the public-use file does not provide
  the full notice, application, channel, document, appeal, or household-result
  sequence needed for an administrative-burden claim.

## Reproduction

```text
extract_sipp_household_calendar_slice.py
  -> analyze_sipp_snap_reasons.py
```

The raw files, derived CSV, and JSON output are not committed. The calculation
output was `/tmp/us-broad-sipp-2025/full-v13/sipp-snap-reasons.json`.

## Next test

Link each start/end reason to the adjacent-month receipt transition, resource
change, work status, child presence, food security, and re-entry. Then compare
notice and renewal route where administrative records are available. Keep
reported reason, administrative classification, material outcome, and public
interpretation as separate fields.

Related records: [SIPP SNAP transition layer](sipp-snap-transition-layer-v1.md),
[SIPP SNAP × food-security layer](sipp-snap-food-security-layer-v1.md),
[safety-net event ledger](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md),
and [safety-net access layer](administrative-burden-access-layer-v1.md).
