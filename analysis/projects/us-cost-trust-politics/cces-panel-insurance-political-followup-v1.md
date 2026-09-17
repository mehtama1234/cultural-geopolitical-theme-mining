# CCES panel insurance-status to political follow-up audit v1

**Checked:** 2026-09-17  
**Status:** compact same-panel descriptive screen; no causal estimate

## Purpose

Use the already-retained 2010–2012–2014 CCES panel to test whether an earlier
health-insurance status is followed by different institutional contact and
political action, keeping approval, contact, and action separate.

## Reproduction result

The local 9,500-row panel file has 9,499 valid 2012 health-insurance statuses:
912 respondents report no insurance and 8,587 report some insurance. Applying
the supplied panel weight, the no-insurance share is 15.49%.

| 2014 outcome | 2012 no insurance | 2012 insured | Valid n |
|---|---:|---:|---:|
| Favorable Congress approval | 11.51% | 10.23% | 909 / 8,543 |
| Unfavorable Congress approval | 74.77% | 83.07% | 909 / 8,543 |
| Any congressional contact | 31.75% | 40.29% | 912 / 8,587 |
| Any local political action | 21.81% | 32.48% | 912 / 8,587 |

The result adds a second material-security route to the work-loss panel: later
contact and local action are lower among respondents who reported no insurance
in 2012, while favorable Congress approval is close across groups. The result
is a descriptive action/approval divergence, not evidence that coverage status
caused political behavior.

## Field and denominator boundary

`healthins_6_12=1` means no health insurance and `=2` means some form of health
insurance. Congress approval uses `CC14_308b`, with codes 1–2 favorable and 3–4
unfavorable. Congressional contact uses any affirmative `CC14_360x_2` through
`CC14_360x_8`. Local political action uses any affirmative
`CC14_417a_1` through `_4`. The supplied `weight` is applied to each valid
outcome universe.

Health-insurance status is not a dated bill, coverage-loss event, care need,
denial, or employer decision. It may reflect age, work, health, income, and
other resources. The selected panel and attrition are not converted into a
causal transition weight, and no replicate-weight variance is claimed.

## Broad-program consequence

```text
earlier material-security status
  -> later institutional judgment and contact
  -> later political action
  -> [open] attribution, remedy, recovery, trust change, or exit
```

This route confirms that approval and action are different downstream
currencies. It also narrows the next test: a dated coverage or medical-bill
episode must be linked to care choice, alternatives, payment, attribution,
institutional response, and later action or recovery.

## Source and storage boundary

- [2010–2014 CCES Panel Study](https://doi.org/10.7910/DVN/TOE8I1)
- [Official CES FAQ](https://cces.gov.harvard.edu/frequently-asked-questions)
- [Canonical insurance follow-up record](../../records/us-cces-panel-insurance-political-followup-2012-2014.json)

The panel extract was already present outside the repository. No new download
was performed and no raw respondent file was added to Git.
