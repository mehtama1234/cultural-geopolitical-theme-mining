# Finding 035: Fraud exposure becomes a household event only when loss is realized

**Status:** exploratory same-respondent follow-up and nonpooled counterexample  
**Checked:** 2026-09-17

## The bounded finding

The April-to-June 2025 HTOPS public-use files provide a storage-light,
same-respondent bridge from retrospective scam exposure to later household
conditions. The exact `SCRAMID` intersection contains 6,564 respondents. It
shows a sharp distinction between three stages that are often collapsed:

```text
retrospective exposure
  -> reported monetary loss
  -> reporting and possible agency recovery
  -> later food, energy, work-loss, and institutional responses
```

Exposure by itself is not a monotonic marker of later hardship. Among linked
respondents, reported loss is the stage at which later food and energy strain
becomes much more visible. The result is descriptive and associative: the
April questions refer to the previous twelve months, not to a dated incident,
and the June survey does not verify the event, remedy, or causal pathway.

## Same-respondent follow-up

| April group | Linked respondents | June food insufficiency | June unable to pay energy bill | June recent household job loss |
|---|---:|---:|---:|---:|
| No reported exposure | 751 | 9.37% | 16.84% | 9.22% |
| Reported exposure | 5,798 | 6.12% | 10.66% | 6.86% |
| Exposure and reported loss | 184 | 23.82% | 43.81% | 8.31% |
| Loss and report to agency | 51 | 12.22% | 44.86% | 11.56% |
| Loss, report, and reported recovery | 11 | 26.57% | 78.80% | 26.03% |

The 11-person recovery cell is retained as a warning and a route for future
work, not as a stable population estimate. Its large energy-bill figure cannot
show failed recovery: recovery is self-reported, may have occurred before the
June interview, and is not linked to a verified payment, correction, or
restored household position.

The institutional measures are similarly conditional. In the broad exposure
group, code-1 shares were 72.43% for trust in federal statistics and 3.93% for
confidence in Congress; in the loss-and-report group they were 70.20% and
0.80%, respectively. These are coding screens preserved from the instrument,
not a generalized trust index or a claim that fraud changed legitimacy.

## The counterexample that changes the interpretation

The linked panel also contains a separate material-pressure comparison. In
that screen, respondents reporting expense difficulty had later food
insufficiency of 12.3%, inability to pay an energy bill of 21.4%, and recent
household job loss of 11.7%, compared with 1.1%, 2.2%, and 2.9% among those
reporting no expense difficulty.

The fraud and material-pressure screens are not rejoined at the respondent
row level and use different April group definitions. They can nevertheless be
read as a carefully bounded counterexample:

```text
exposure label != realized loss
realized loss != general expense difficulty
reported recovery != restored security
later hardship != proven causal effect
```

This prevents the broad atlas from treating every consumer exposure as an
equivalent shock. The conversion step—whether money was actually lost, an
agency was contacted, funds were recovered, and household security was later
restored—must be observed separately.

## What the chain establishes

| Arrow | Evidence status | Safe conclusion |
|---|---|---|
| Same respondent in April and June | Observed | Exact `SCRAMID` linkage yields 6,564 retained respondents |
| Exposure → reported loss | Reported conditional stage | Loss is a distinct reported stage among exposed respondents |
| Loss → later food/energy/work context | Descriptive follow-up | Loss groups show higher later food and energy strain in the selected linked sample |
| Report → agency response | Reported | A subset reported to law enforcement or government; effort, decision, and timing are absent |
| Agency recovery → restored security | Open | No verified amount, receipt date, durability, or household restoration is observed |
| Fraud/loss → trust or political action | Open | Later institutional items exist, but prior trust, attribution, action, and causal timing do not |
| Burden → switching or exit | Open | No customer alternative, continued use, non-use, switching, or exit record exists |

The strongest contribution is therefore not a fraud effect estimate. It is a
measurement rule for consumer and institutional trends: a credible end-to-end
story must distinguish exposure, realized burden, response attempt, remedy,
protected outcome, and later judgment.

## Interpretation limits

- April fraud questions refer to the prior twelve months, so incident date,
  actor, product, channel, and sequence are unknown.
- The linked sample is a retained intersection, not a documented attrition-
  adjusted longitudinal survey universe; April person weights are used, but
  replicate variance is not claimed for the follow-up.
- The no-exposure group is not a randomized control group. Exposure, loss,
  reporting, income, age, health, prior trust, and access to agencies may all
  differ.
- “Reported recovery” is a respondent answer, not an administrative receipt,
  amount recovered, or proof of durable restoration.
- The small recovery cell is too sparse for a reliable subgroup estimate.
- Food, energy, and job-loss outcomes are later context, not necessarily the
  consequence of the scam; other events can intervene.
- Code-1 institutional responses retain survey coding but should not be
  relabeled as high trust or low confidence without the full instrument
  dictionary and item-specific interpretation.

## Why this matters to the broad goal

This is a compact example of how consumer, household, institutional, and
political layers should be connected without forcing them into one causal
claim. The program can now say:

```text
consumer exposure can be linked to later context
  -> realized loss is more informative than exposure alone
  -> reporting is an action attempt, not a remedy
  -> recovery is not restoration unless receipt and durability are observed
  -> institutional response is not legitimacy change without attribution and prior-to-later measures
```

The next decisive artifact is a dated case or lawful recontact record with
the amount, alternative options, report effort, agency decision, verified
payment or correction, and one- to six-month household and trust outcomes.
Until then this finding remains a detailed acquisition-boundary result, not a
claim that fraud caused hardship or political disengagement.

## Reproduction and storage boundary

The analysis reads the retained compact JSON outputs and downloads no new raw
files. The underlying PUFs were used outside the repository and are identified
by hashes in the follow-up output. The [machine-readable canonical record](../../../records/us-htops-fraud-loss-followup-2025.json)
preserves the observation denominators, measures, source hashes, and boundary.

Related local evidence:

- [HTOPS fraud-to-follow-up screen](../htops-2025-fraud-followup-v1.md)
- [Material-pressure versus fraud counterexample](../htops-material-vs-fraud-counterexample-v1.md)
- [Fraud/recovery/trust acquisition gate](../htops-2025-fraud-recovery-trust-acquisition-gate-v1.md)

**Evidence status:** same-respondent descriptive follow-up with an explicit
exposure-to-loss counterexample; remedy receipt, durable recovery, trust
change, political action, switching, and exit remain unobserved.
