# UAS health-cost episode and legitimacy acquisition audit v1

**Checked:** 2026-09-15  
**Status:** official documentation route verified; registration-gated microdata not yet acquired; no estimate promoted

## Why this is the next acquisition

The health-cost lane now has strong separate surfaces for cost-related care
foregoing, household adaptation, institutional response, trust, and political
action. It still lacks a source that can preserve one respondent across a
health-cost experience and a later judgment. The Understanding America Study
(UAS) is the strongest currently identified acquisition route because its
respondent identifier can link core, special-topic, and monthly panel files.

The route is not yet a completed finding. UAS data downloads are registration
gated, and the public documentation does not by itself establish the final
usable overlap, response timing, or weight availability. Those are acquisition
checks, not assumptions.

## Documented source architecture

USC describes the UAS Comprehensive File and Comprehensive Panel Dataset as
harmonized multi-wave data. The panel file has one respondent-by-wave record,
supports transitions and panel models, and can be linked to additional UAS
content with the `uasid` identifier. The source page says the latest listed
release was updated in June 2026.

The UAS Monthly Panel Survey covers October 2023 onward. Each record is an
individual-by-wave observation about the previous calendar month and includes
health, financial, employment, and subjective-well-being events, including
health, life satisfaction, pain, stress, and PROMIS meaning-and-purpose
measures. The Older Ages Monthly Events panel covers June 2019–September 2023
for respondents aged 50 and older and documents previous-month medical
expenditures alongside work and health measures.

The source architecture therefore supports a potentially ordered design:

```text
monthly health/financial event or special-module medical-cost experience
  -> care affordability, bill, payment, or foregoing choice
  -> subsequent health, work, financial, pain, or meaning measure
  -> later trust/satisfaction or institutional judgment
```

## Candidate modules and exact fields

| UAS route | Documented fields | What it could close | Boundary to verify after access |
|---|---|---|---|
| UAS 698 health-cost module | Health-care costs in the last two years, out-of-pocket amount, outside help with medical costs/insurance/long-term care, overall satisfaction with quality/cost/convenience, needed-but-not-received care, and reasons including unaffordability, scheduling, transportation, and waiting | Bill/payment burden, alternatives, care foregoing, support route, and satisfaction in the same respondent | Exact field names, dates/recall windows, module-to-core overlap, weights, missingness, and whether trust/action is in the linked wave |
| UAS 537 future-of-health-care module | Recent health-care visits and billing, unaffordable care since March 2020, current ability to afford services, transportation access, household medical bill that was unaffordable or disputed, provider-organization rating, and trust in hospitals and insurers after hospitalization | Direct bill/affordability, access alternative, provider experience, and institution-specific trust | The pandemic-recall window is broad; trust is conditional on hospitalization; verify usable overlap and survey weights |
| UAS Monthly Panel, October 2023–present | Previous-month health, financial, employment, life satisfaction, pain, stress, and meaning/purpose events | A genuinely dated monthly exposure-to-subsequent-outcome backbone | Documentation does not guarantee a medical-bill or trust item in every wave; acquire codebook and enumerate wave coverage |
| UAS Older Ages Monthly Events, June 2019–September 2023 | Previous-month medical expenditures, work hours/earnings, health, life satisfaction, and pain for age 50+ panel members | Monthly medical-spending-to-health/work/meaning timing for an older-age subsample | No documented same-file political-trust endpoint in the public summary; link to core/special modules and retain age restriction |

## Required acquisition and merge test

After registration, acquire the relevant codebooks and data descriptions before
the microdata. Then perform the following checks in order:

1. Confirm `uasid` uniqueness within each file and one-to-many respondent-wave
   structure in the panel files.
2. Inventory exact variable names, value labels, wave dates, field dates,
   recall periods, module eligibility, and item-specific missing codes.
3. Confirm the correct respondent-level or wave-level weights and whether
   replicate/design variables are supplied for the special modules.
4. Match UAS 698 and UAS 537 respondents to adjacent core or panel waves and
   report the overlap and attrition denominator.
5. For monthly files, order the exposure by the previous calendar month and
   require the outcome wave to occur after that exposure; exclude same-period
   ambiguity where the documentation cannot separate event and outcome dates.
6. Preserve non-users and counterexamples: care obtained despite unaffordability
   concern, bills paid without reported sacrifice, unmet care for non-cost
   reasons, trust without a reported bill, and low trust without a health-cost
   exposure.

## Promotion rule

Promote a UAS result into the health-cost end-to-end finding only if one
respondent can be shown to have, in a documented sequence:

```text
dated or bounded health-cost exposure
  -> care/payment choice or bill dispute
  -> later health, work, financial, or meaning outcome
  -> later provider/insurer trust, satisfaction, complaint, switching, or action
```

The result must report the eligible overlap, denominator, panel retention,
weights, missingness, timing, subgroup, uncertainty, and a counterexample.
UAS 698/537 cross-sectional recall items may be promoted as a same-survey
episode-context layer, but not as longitudinal recovery or causal evidence.
The monthly panel can support a stronger temporal association only when its
codebook confirms the relevant medical-cost and later judgment fields.

## Current conclusion

UAS is the smallest credible next acquisition capable of closing more than
one remaining arrow at once. It can potentially add dated or bounded cost,
care choice, alternatives, downstream well-being, and institution-specific
trust while preserving respondent identity. Until registration-gated files and
codebooks are acquired, the correct status is **verified acquisition route**,
not completed evidence.

## Official sources

- [UAS Comprehensive File and Panel Dataset](https://uasdata.usc.edu/index.php?pid=Comprehensive+File&type=3)
- [UAS Monthly Surveys data page](https://uasdata.usc.edu/index.php?pid=Monthly+Surveys&type=3)
- [UAS 537 future-of-health-care questionnaire](https://uasdata.usc.edu/output/paperversion/index.php?r=eNpLtDK2qi62MrFSKkhMT1WyLrYyBLFLk3Iyk_WK8ktLMvPSQaJAweLizBQQ09hKydTYHCZYChE0tFIyVLKuBVwwx5cXVA%2C%2C)
- [UAS 698 health-cost questionnaire](https://uasdata.usc.edu/output/paperversion/index.php?r=eNpLtDK2qi62MrFSKkhMT1WyLrYyBLFLk3Iyk_WK8ktLMvPSQaJAweLizBQQ09hKyczSAiZYChE0tFIyUbKuBVwwyGMXXw%2C%2C)
