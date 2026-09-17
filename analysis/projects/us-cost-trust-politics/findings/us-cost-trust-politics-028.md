# Finding 028: Fraud loss is followed by mixed material and institutional responses in a linked HTOPS panel

**Status:** exploratory same-respondent descriptive follow-up · **Checked:** 2026-09-17

## The bounded finding

The April-to-June 2025 HTOPS files can be linked for 6,564 respondents through
the exact `SCRAMID` key. Within that retained intersection, respondents who
reported fraud exposure alone did not show the same later material pattern as
those who reported exposure plus money loss. The April loss groups had much
higher June energy-bill difficulty, while the institutional response measures
were mixed and institution-specific.

For example, the April-weighted June share unable to pay an energy bill was
10.66% among exposure respondents, 43.81% among exposure-plus-loss
respondents, and 44.86% among loss-plus-report respondents. The corresponding
code-1 share for June federal-statistics trust was 72.43%, 58.07%, and 70.20%.
The June Congress-confidence code-1 shares were 3.93%, 4.84%, and 0.80%.
These are coding screens, not claims that code 1 means “high trust.”

The safe interpretation is:

> A same-respondent panel can distinguish reported exposure from reported loss
> and can place later material and institutional responses on the timeline.
> It does not establish that fraud caused the later burden or trust response,
> that agency recovery restored the household, or that any respondent took a
> political action.

## Event chain

```text
retrospective scam exposure
  -> reported money loss, reporting, or agency recovery
  -> later food, energy, work-loss, and institution-specific responses
  -> [open] dated attribution, remedy receipt, trust change, action, or exit
```

## What the linked panel supplies

| Stage | Observed evidence | Still open |
|---|---|---|
| Same-person linkage | 6,564 exact `SCRAMID` matches across April and June files | Attrition-adjusted longitudinal weighting and nonresponse selection |
| Exposure/loss distinction | 5,798 exposure; 184 exposure-plus-loss; 51 loss-plus-report; 11 loss/report/recovery respondents | Dated incident, actor, amount, alternatives, and effort |
| Later material context | June energy-bill difficulty: 10.66% exposure, 43.81% exposure-plus-loss, 44.86% loss-plus-report | Causal effect, household recovery, and reason for later hardship |
| Later institutional response | Federal-statistics trust and Congress-confidence code-1 shares vary by group and are not monotonic | Dictionary interpretation, prior trust, attribution, and trust change |
| Report/recovery route | Reporting and an 11-person recovery subgroup are recorded | Remedy adequacy, receipt, timing, durability, and remaining loss |
| Political action | Institution-specific response fields are available | Contact, complaint, vote, organizing, protest, switching, non-use, and exit |

## Why this matters to the broad atlas

This is the highest-value kind of bridge currently available without acquiring
new files: it preserves a person across a baseline exposure screen and a later
outcome wave. It demonstrates that exposure, realized loss, reporting, and
reported recovery are not interchangeable categories. It also prevents a
single “material pressure causes distrust” story: the later energy pattern is
strongest in the loss groups, while the institution-specific response patterns
are mixed and may reflect prior identity, selection, or different meanings of
statistics and Congress.

The result is therefore a measurement advance, not a causal claim. The same
respondent key closes the linkage arrow, but not the incident-date,
responsibility, remedy, attribution, trust-change, action, or exit arrows.

## Coding consequence

```text
reported exposure           != realized monetary loss
reported recovery           != verified remedy receipt
same-respondent follow-up   != attrition-adjusted causal panel
institutional response      != trust change
confidence                  != political action
```

Code this as **same-respondent weighted descriptive follow-up with a
loss/material gradient and mixed institution-specific responses; attribution,
trust change, recovery, and action open**. Keep the 11-person recovery group
as a boundary cell, not a stable estimate.

## Next decisive test

The smallest useful extension is a dated incident-and-remedy module that
records actor, amount, attempted contact, agency response, payment or correction
receipt, and later trust/action for the same respondent. Until that exists,
retain the HTOPS result as an associative longitudinal surface and use the July
expense-confidence comparison as a separate cross-sectional benchmark.

## Sources and storage boundary

- [Census HTOPS/HPS public-use datasets](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)
- [Committed fraud follow-up audit](../htops-2025-fraud-followup-v1.md)
- [Machine-readable follow-up result](../data/htops-2025-fraud-followup-2025-04-to-06.json)

The analysis uses previously retained compact result artifacts and recorded
input hashes. Raw HTOPS PUFs are not retained in the repository and no new
download was performed.
