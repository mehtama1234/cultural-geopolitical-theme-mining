# CCES panel job-loss to political follow-up audit v1

**Checked:** 2026-09-17  
**Status:** reproduced compact same-panel descriptive screen; no causal estimate

## Purpose

Test whether the retained 2010–2012–2014 CCES panel can add a material/work
screen before later institutional judgment and political action, without
downloading or retaining another large file.

## Local source and variables

The existing `/tmp/v8_cces_panel_full3waves.dta` contains 9,500 rows and 1,629
columns. Its SHA-256 is
`82c281acaa6a896a1e3071f457f64c68272a746fb43d34e8be50646f7fdc330b`.
The official panel description identifies this as the 2010–2014 CCES Panel
Study. The derived screen uses:

| Stage | Variable | Coding |
|---|---|---|
| Earlier material/work exposure | `CC12_387_4` | 1 = lost job during the prior two years; 2 = no |
| Later institutional judgment | `CC14_308b` | 1–2 = favorable Congress approval; 3–4 = unfavorable; 5 = not sure |
| Later institutional contact | `CC14_360x_2`–`_8` | any affirmative contact route |
| Later political action | `CC14_417a_1`–`_4` | any local political meeting, sign, campaign work, or donation |
| Weight | `weight` | supplied panel weight; no new design-based variance claim |

## Reproduction result

All 9,500 retained rows have a valid job-loss classification. The job-loss
group contains 829 respondents (9.71% weighted); the no-loss group contains
8,671. Weighted 2014 outcome shares are:

| Outcome | Reported job loss | No reported job loss | Valid n by group |
|---|---:|---:|---:|
| Favorable Congress approval | 13.86% | 10.06% | 827 / 8,626 |
| Unfavorable Congress approval | 80.85% | 81.88% | 827 / 8,626 |
| Any congressional contact | 37.36% | 39.14% | 829 / 8,671 |
| Any local political action | 23.93% | 31.57% | 829 / 8,671 |

The screen therefore supplies a counterexample to a single translation rule:
reported job loss coincides with lower measured action but not uniformly lower
Congress approval. The approval item is institution-specific and may encode
party identity or attribution rather than generalized trust.

## Interpretation boundary

The 2012 item asks whether the respondent lost a job during the prior two years;
it does not identify the separation date, employer, involuntary status, income
loss, benefit loss, unemployment duration, alternatives, or remedy. The panel
is selected and retained, and the supplied weight has not been independently
validated as an attrition-adjusted transition weight. Prior political identity,
health, income, local labor conditions, economic expectations, and other shocks
remain competing explanations. These are weighted descriptive contrasts, not
causal job-loss effects or design-based confidence intervals.

## Broad-program consequence

This compact screen strengthens the material/work → judgment/action map by
putting a prior work disruption and later political outcomes on the same
respondent timeline. It also clarifies the next missing fields:

```text
dated separation and actor
  -> income/benefit/time loss and available alternatives
  -> attribution, fairness, and perceived control
  -> contact, vote, organizing, switching, or withdrawal
  -> institutional response and recovery
```

Only the broad prior job-loss screen and later approval/contact/action surfaces
are observed here. Attribution, trust change, remedy, recovery, and exit remain
open.

## Sources

- [2010–2014 CCES Panel Study](https://doi.org/10.7910/DVN/TOE8I1)
- [Official CES FAQ](https://cces.gov.harvard.edu/frequently-asked-questions)
- [Canonical trend record](../../records/us-cces-panel-job-loss-political-followup-2012-2014.json)

The panel file was already present outside the repository. No new download was
performed and no raw respondent file was copied into Git.
