# Finding 029: Reported job loss is followed by lower political action but not uniformly lower Congress approval

**Status:** exploratory same-panel descriptive comparison · **Checked:** 2026-09-17

## The bounded finding

The retained 9,500-person 2010–2012–2014 CCES panel permits a compact timeline:
a 2012 retrospective question about job loss during the prior two years can be
followed into 2014 Congress approval, congressional contact, and local political
action. Among 829 respondents reporting job loss and 8,671 reporting no job
loss, the job-loss group had lower weighted local political action (23.93% versus
31.57%) and slightly lower congressional contact (37.36% versus 39.14%).

Congress approval did not move in the same direction: favorable approval was
13.86% in the job-loss group versus 10.06% in the no-loss group, while
unfavorable approval was 80.85% versus 81.88%. This is a counterexample to
equating material disruption with uniform institutional distrust or withdrawal.

## Event chain and limits

```text
retrospective job-loss screen
  -> later Congress approval and contact
  -> later local political action
  -> [open] dated attribution, remedy, recovery, trust change, or exit
```

The job-loss question is not a dated separation or a verified income shock. It
does not identify employer, cause, duration, benefit loss, alternative work,
household consequences, or whether the respondent considered Congress
responsible. The 2014 political outcomes are institution-specific and can be
shaped by prior party identity, economic expectations, health, local labor
conditions, and other events.

| Stage | Observed | Still open |
|---|---|---|
| Work disruption | 829 respondents reported losing a job in the prior two years | Date, actor, involuntary status, income/benefit/time loss |
| Institutional judgment | Congress approval differs slightly and non-monotonically | Generalized trust, blame, fairness, and trust change |
| Institutional contact | Any congressional contact is separately measured | Purpose, complaint/request, response, and resolution |
| Political action | Meeting/sign/campaign-work/donation composite is lower after job-loss screen | Voting, organizing, withdrawal, switching, and mechanism |
| Recovery | No recovery variable in this screen | New work, income restoration, remedy, household security, exit |

The valid Congress-approval denominators are 827 job-loss and 8,626 no-loss
respondents; contact and action use 829 and 8,671. Percentages use the supplied
panel weight. No replicate-weight or causal interval is claimed.

## Why this matters to the broad atlas

This is a stronger temporal arrangement than a single cross-sectional proxy: the
same respondent supplies an earlier work-disruption screen and later political
outcomes. Its main value is diagnostic. It shows that work disruption may
coincide with reduced action availability while institution-specific approval
does not simply fall. The result keeps “political judgment,” “institutional
contact,” and “collective action” as separate downstream currencies.

## Coding consequence

```text
retrospective job loss       != dated involuntary separation
lower action                 != political apathy
Congress approval            != generalized trust
same-panel ordering          != causal effect
political action             != remedy, recovery, or exit
```

Code this as **same-panel weighted descriptive work-disruption follow-up with
lower observed action and non-monotonic institution-specific approval;
attribution, remedy, recovery, trust change, and exit open**.

## Next decisive test

Use a panel with a dated separation, employer or benefit event, income/time
effect, alternative work, blame/fairness, and later contact or organizing. If
that is unavailable, pair this screen with a same-case labor or public-record
remedy ledger and preserve the population-panel and case units separately.

## Sources and storage boundary

- [2010–2014 CCES Panel Study](https://doi.org/10.7910/DVN/TOE8I1)
- [Official CES FAQ](https://cces.gov.harvard.edu/frequently-asked-questions)
- [Local reproduction audit](../cces-panel-job-loss-political-followup-v1.md)
- [Machine-readable record](../../../records/us-cces-panel-job-loss-political-followup-2012-2014.json)

The analysis reads the existing local panel extract and records its hash. No
large raw file was downloaded or added to the repository.
