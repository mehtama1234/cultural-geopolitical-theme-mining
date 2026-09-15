# ANES health-cost and legitimacy acquisition audit v1

**Checked:** 2026-09-15  
**Status:** official-codebook acquisition audit; no episode estimate promoted

## Purpose

The health-cost lane needs a later trust, attribution, political-action,
switching, or exit outcome. The current ANES 2016–2020–2024 panel is a
promising respondent-level endpoint source because it contains repeated
political judgments, institutional trust, party identity, and reported vote.
This audit tests whether the current 2024 release also contains enough health
and cost information to connect that endpoint to the MEPS/SHED pathway.

## Available health-cost variables

The May 19, 2026 ANES 2024 Time Series full-release codebook identifies:

| Variable | Codebook question | Useful role | Boundary |
|---|---|---|---|
| `V241571` | Present health insurance | Coverage context | No plan adequacy, premium, deductible, network, or episode timing |
| `V241572` | Concern about losing health insurance in the next year | Coverage insecurity | Anticipation, not an observed loss or claim |
| `V241573` | Concern about paying health-care expenses for the respondent and family in the next year | Health-cost exposure proxy | Forward-looking concern, not a bill, amount, payment, or care decision |
| `V241574a`–`V241574...` | Disabilities or chronic conditions | Need/health context | No particular treatment need, price, or care episode |
| `V242351` | Whether government spending should change to help people pay for health insurance | Health-policy judgment | Policy preference, not remedy receipt or institutional response |
| `V242352`–`V242353x` | Desired amount and direction of government help paying for health care | Policy-demand detail | No episode attribution, trust change, or political action caused by a bill |

The official merged-panel page documents a nine-wave file using the 2016 case
ID, with 2,171 2024 pre-election and 2,070 post-election panel interviews.
This creates a viable repeated-respondent endpoint architecture, subject to
panel selection and weighting rules.

## Missing fields for the stronger join

ANES does not supply the fields needed to claim that a specific health-cost
episode produced a later legitimacy or political response:

- dated medical need, service, bill, or coverage denial;
- amount owed, payment obligation, due date, collection, or remedy effort;
- care received, delayed, substituted, or forgone because of that obligation;
- feasible alternatives, liquid resources, unpaid family care, or work/time
  substitution;
- provider/insurer interaction, complaint, appeal, correction, switching, or
  exit tied to the episode;
- direct attribution of a later trust judgment or vote to the experience.

## Promotion decision

Do not merge ANES health-cost concern with MEPS or SHED care-delay records as
if they were the same respondents. The defensible current bridge is:

```text
health-cost concern / insurance insecurity (ANES)
  -> health-policy judgment and repeated political endpoints (ANES)
```

The stronger chain remains open:

```text
specific health bill or denial
  -> care choice and household sacrifice
  -> institutional remedy
  -> later trust, action, switching, or exit
```

## Next executable test

Acquire the May 19, 2026 merged CSV or use the official SDA interface, then
produce weighted same-respondent tables for `V241573` against federal trust,
perceived concentrated interests, perceived waste, health-policy demand, and
post-election vote/fairness. Condition the results on prior party identity,
insurance status, chronic-condition indicators, income, and panel retention.
Report valid universes, weights, complex-design uncertainty, missingness, and
non-monotonic or null patterns. Promote this as an ANES health-cost concern
layer only; promote it to the health-cost end-to-end finding only if the data
support an explicit respondent-level sequence.

## Sources

- [ANES 2024 Time Series Study](https://electionstudies.org/data-center/2024-time-series-study/)
- [ANES 2024 Full Release User Guide and Codebook, May 19, 2026](https://electionstudies.org/wp-content/uploads/2026/05/anes_timeseries_2024_userguidecodebook_20260519.pdf)
- [ANES 2016–2020–2024 Panel Merged File](https://electionstudies.org/data-center/2016-2020-2024-panel-merged-study/)

**Acquisition note:** the official page and indexed codebook content were
available for inspection on the checked date, but direct PDF/CSV retrieval in
this environment returned a web-challenge HTML response. No local microdata
estimate is claimed by this audit.
