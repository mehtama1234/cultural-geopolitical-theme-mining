# Finding 030: Earlier health-insurance noncoverage is followed by lower political contact and action

**Status:** exploratory same-panel descriptive comparison · **Checked:** 2026-09-17

## The bounded finding

In the retained 2010–2012–2014 CCES panel, 912 respondents reported no health
insurance in 2012 and 8,587 reported some insurance. By 2014, the no-insurance
group reported less congressional contact (31.75% versus 40.29%) and less local
political action (21.81% versus 32.48%). Favorable Congress approval was close
(11.51% versus 10.23%), while unfavorable approval was lower in the no-insurance
group (74.77% versus 83.07%).

This is a useful counterexample: material insecurity and institutional judgment
do not have to move with political contact or action in the same way.

## Event chain and limits

```text
2012 health-insurance status
  -> 2014 Congress approval and congressional contact
  -> 2014 local political action
  -> [open] dated coverage event, attribution, remedy, recovery, or exit
```

The no-insurance item is a status measure, not a dated coverage loss, medical
bill, denial, unmet need, or employer event. Differences can reflect age,
employment, health, income, prior political identity, local conditions, and
selection. Same-panel ordering improves temporal structure but does not identify
causality.

| Stage | Observed | Still open |
|---|---|---|
| Material security | 2012 insurance status | Coverage change date, bill, denial, care need, alternatives |
| Institutional judgment | 2014 Congress approval by prior status | Attribution, fairness, generalized trust, trust change |
| Institutional contact | 2014 congressional contact routes | Purpose, response, correction, remedy |
| Political action | 2014 local meeting/sign/campaign/donation composite | Vote mechanism, organizing, withdrawal, switching, exit |
| Recovery | Not represented | Coverage restoration, treatment, household security, political or consumer response |

The 2014 approval denominator is 909 no-insurance and 8,543 insured respondents;
contact and action use 912 and 8,587. Percentages use the supplied panel
weight. No replicate-weight or causal interval is claimed.

## Coding consequence

```text
no insurance status        != dated coverage loss
lower contact/action       != political apathy
Congress approval          != generalized trust
same-panel ordering        != causal effect
material insecurity        != remedy, recovery, or exit
```

Code this as **same-panel weighted descriptive insurance-status follow-up with
lower contact/action and near-similar favorable approval; event attribution,
remedy, recovery, trust change, and exit open**.

## Next decisive test

Use a dated coverage, bill, denial, or care episode with employer/insurer
responsibility, feasible alternatives, payment and care choice, remedy or
non-remedy, and later action or recovery. Preserve the panel result as a
temporal benchmark rather than an episode effect.

## Sources and storage boundary

- [2010–2014 CCES Panel Study](https://doi.org/10.7910/DVN/TOE8I1)
- [Official CES FAQ](https://cces.gov.harvard.edu/frequently-asked-questions)
- [Local audit](../cces-panel-insurance-political-followup-v1.md)
- [Machine-readable record](../../../records/us-cces-panel-insurance-political-followup-2012-2014.json)

The analysis uses the existing local panel extract and records its hash. No
large raw file was downloaded or copied into the repository.
