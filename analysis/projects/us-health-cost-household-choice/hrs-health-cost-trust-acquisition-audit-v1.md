# HRS health-cost and institutional-trust acquisition audit v1

**Checked:** 2026-09-15  
**Status:** official-codebook route verified; no local microdata estimate promoted; age-50-plus boundary retained

## Why this is a useful parallel route

The Health and Retirement Study (HRS) is a nationally representative panel of
older Americans with repeated health, health-services, work, income, wealth,
and psychosocial measures. Its official 2020 documentation places
cost-related delayed care and institutional trust close enough in the study
architecture to provide a useful counterpart to the UAS acquisition. It also
offers a deliberately different population: people age 50 and older rather
than the all-adult UAS panel.

This is an acquisition route, not a completed end-to-end result. HRS files and
module samples must be merged using the official identifiers and sample
weights, with module eligibility, missingness, and timing preserved.

## Published 2019 codebook baseline

The official HRS 2019 Health Survey codebook provides a useful unweighted
baseline while microdata access remains pending. Among 5,097 respondents, 425
reported delaying medical care because of cost in the prior 12 months (8.34%),
and 299 reported needing medical care but not getting it because they could
not afford it (5.87%). For satisfaction with the cost of health care, 721 of
5,097 respondents were somewhat or very dissatisfied (14.14%); the codebook
also reports 6 multiple-selection errors and 72 blank/missing records for that
item.

These are codebook frequencies, not weighted population estimates. The
questions have different universes and the 2019 Health Survey is not itself a
dated bill-to-trust panel. They establish that the older-adult source has
measurable cost-related care and cost-satisfaction surfaces and provide a
counterpart against which a later respondent-level acquisition can be
checked.

## Documented field path

The 2020 Section N health-services documentation identifies:

- `N290`: needed medical care but did not get it because it could not be
  afforded, with a two-year/last-interview recall window;
- `N235`: overall satisfaction with health care, considering quality, cost,
  and convenience;
- `N295`: whether wishes for care were taken into account;
- `N333`: out-of-pocket health-care payment fields in the health-services
  questionnaire family (exact analytic suffix/variant must be confirmed in the
  released file).

The 2020 COVID section identifies `W579_` for delayed or forgone medical or
dental care since March 2020 and `RCOVW580M1`–`RCOVW580M3` for reasons,
including “couldn't afford it,” appointment/access problems, closure or
rescheduling, deciding it could wait, and fear of going. These reasons keep
price, access, time, and pandemic-specific routes separate.

The 2020 Section V psychosocial module identifies:

- `RV557`: trust in people in general;
- `RV558`: trust in Social Security;
- `RV559`: trust in Medicare or Medicaid;
- `RV563`: trust in insurance companies;
- `RV555`: perceived potential for deception by insurance companies.

The trust module is not automatically a post-bill measure. Its module
assignment, field date, and relation to the health-services interview must be
verified before calling it a later endpoint.

## Published 2020 trust baseline

The official HRS 2020 Final Release Section V codebook reports descriptive
module frequencies for the institutional endpoint: trust in Medicare or
Medicaid averaged 6.36 on a 0--10 scale among 1,321 valid responses, while
trust in insurance companies averaged 4.85 among 1,318 valid responses. The
same module reports perceived potential for deception by insurance companies
at 43.21 on a 0--100 scale among 1,307 valid responses. These are unweighted
module statistics; the codebook shows 14,379 records blank/inapplicable for
each item and separate small counts for web non-response, don't know, and
refusal. They are a usable older-adult legitimacy baseline, not evidence that
health-cost hardship caused the judgments.

The codebook's routing also matters: Section V's trust block is assigned to
an eligible self-report module sample, not the full HRS respondent file. The
reported trust and deception means therefore cannot be compared directly with
the 2019 Health Survey rates or interpreted as a panel change until released
files, identifiers, weights, and timing are verified.

## Smallest defensible HRS design

The first HRS pass should merge the 2020 core health-services file, COVID
module, and psychosocial module for eligible respondents, then link to the
nearest prior and subsequent core waves. The unit should remain the HRS
respondent; spouse and household measures must not be silently substituted.

The repository includes a run-ready structural audit at
`scripts/audit_hrs_health_cost_trust_files.py`:

```text
python3 scripts/audit_hrs_health_cost_trust_files.py \
  --file health=/path/to/hrs-health-file.dta \
  --file covid=/path/to/hrs-covid-file.dta \
  --file trust=/path/to/hrs-psychosocial-file.dta \
  --output /tmp/hrs-health-cost-trust-audit.json
```

It records hashes, candidate HRS fields and labels, direct or composite
`HHIDPN`/`HHID`+`PN` keys, unique-respondent counts, and pairwise overlap. It
does not treat key overlap as evidence of common timing, valid module weights,
or a causal health-cost-to-trust sequence.

```text
prior trust / health / financial context
  -> delayed or forgone care, reason, cost satisfaction, or out-of-pocket field
  -> same-wave and next-wave health/work/financial outcome
  -> trust in Medicare/Medicaid or insurance companies
```

The first release should produce only:

1. valid module overlap and respondent retention;
2. item-specific recall windows and field dates;
3. weighted rates for unaffordability and non-cost delay reasons;
4. trust distributions conditioned on the health-cost measures;
5. baseline and next-wave health, work, and financial outcomes where timing
   supports them; and
6. missingness, module assignment, age restriction, weights, uncertainty, and
   counterexamples.

## Promotion and failure rules

Promote an HRS result only if the released data demonstrate a common respondent
key, a documented temporal order or explicitly bounded same-wave comparison,
and the correct module weight/design treatment. Preserve these counterexamples:

- care delayed for access, scheduling, closure, or fear rather than cost;
- care obtained despite low cost satisfaction or affordability concern;
- trust in an institution despite reported delayed care;
- low institutional trust without a reported health-cost barrier; and
- improved later health without assuming that a bill was remedied.

Do not describe `N290` or `W579_` as a dated bill. Do not describe `RV559` or
`RV563` as trust changed by a medical episode unless the panel timing and
preceding trust measure support that interpretation. Do not pool HRS estimates
with UAS, ANES, CES, SHED, or MEPS denominators; use HRS as an age-specific
replication or counterexample surface.

## Current conclusion

HRS is a viable fallback if UAS registration or module overlap fails, and a
valuable re-test even if UAS succeeds. It can add a mature older-adult panel,
explicit non-cost reasons for delayed care, institutional trust targets, and
health/work/financial context. The 2020 codebook adds a bounded descriptive
baseline in which public-program trust is higher than insurer trust and
perceived insurer deception is substantial, but that contrast is not an
episode-level effect. HRS cannot by documentation alone close the
bill-to-remedy-to-trust arrow: exact payment obligation, remedy effort,
complaint, switching, and episode attribution remain acquisition checks.

## Official sources

- [HRS questionnaires and documentation](https://hrs.isr.umich.edu/documentation/questionnaires)
- [HRS 2019 Health Survey codebook](https://hrs.isr.umich.edu/sites/default/files/meta/2019/health-survey/codebook/hm19a_r.htm)
- [HRS 2020 Section N: Health Services and Insurance](https://hrs.isr.umich.edu/sites/default/files/meta/2020/core/qnaire/online/15hr20N.pdf)
- [HRS 2020 Final Release Section V codebook](https://hrs.isr.umich.edu/sites/default/files/meta/2020/core/codebook/h20v_rf.htm)
- [HRS 2020 COVID section codebook](https://hrs.isr.umich.edu/sites/default/files/meta/2020/core/codebook/h20cov_r.htm)
- [HRS codebooks](https://hrs.isr.umich.edu/documentation/codebooks)
