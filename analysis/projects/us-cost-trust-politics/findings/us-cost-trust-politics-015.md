# Material pressure has several gates before it becomes political action

**Status:** provisional non-pooled end-to-end bridge · **Checked:** 2026-09-14

## The bounded finding

The atlas now has evidence for several adjacent stages of the long-term chain:

```text
resources and work limitation
  -> work and earnings/hours movement
  -> unpaid care and social-time allocation
  -> health status and medical-cost movement
  -> financial worry and institutional interpretation
  -> trust, identity, civic action, or reported vote
```

These stages are not one panel and are not a causal model. Their value is
diagnostic: they show what can currently be measured, what must remain separate,
and where the program's most important open arrow lies.

## Evidence surfaces kept distinct

| Stage | Direct evidence | What it does not establish |
|---|---|---|
| Material/work | In SIPP, the displayed below-one-times-resource hours-change share is 16.882% among people reporting a work-limiting condition and 12.086% among those without one. | Direction of change, accommodation, job quality, care response, or political meaning. |
| Care/time | In ATUS, standardized eldercare providers show +70.702 eldercare minutes, −19.700 work minutes, and −18.385 socializing minutes per diary day relative to nonproviders. | Care onset, recipient outcome, employer response, health effect, or whether less work is voluntary or constrained. |
| Health/cost | In MEPS Panel 27, 21.009% improved and 22.849% worsened in health status from 2022 to 2023; total health expenditure rose $630.83 per person while out-of-pocket expenditure fell $50.50. The paired out-of-pocket interval includes zero under the Taylor-linearized design estimate. | Whether work or care caused the change, or how a household allocated the difference. |
| Work continuity | In the same MEPS panel's separate valid employment universe, 62.08% were employed in both endpoint rounds, 2.77% moved employed→not employed, and 5.05% moved not employed→employed; the paired wage-income change was +$2,012.35 in its own valid universe. | Whether health cost, care, coverage, or another event caused any employment or wage movement; job quality, hours, schedule control, and leave remain unmeasured. |
| Interpretation/trust/vote | ANES financial-worry rows differ in institutional trust and reported vote; the pattern changes with party identity and is not monotonic. | That a particular bill, price, care episode, or job change caused worry or vote choice. |
| Trust/action | CCES joint proxy cells show different combinations of material proxies, institutional trust, and any civic action, including 30.3155% federal-trust/action in the gig-work-plus-student-loan cell. | Event timing, attribution, remedy, prior trust, or causality. |

## What the bridge supports

The evidence supports a cautious architectural conclusion: household room is
made from multiple currencies—cash, hours, health, care capacity, employment
continuity, information,
social time, institutional voice, and practical exit. A change in one currency
can coexist with improvement in another. The MEPS result is a clear example:
total health spending and out-of-pocket spending move in opposite directions
in the displayed mean change, so “health cost” cannot stand in for household
burden without specifying whose cost and which payment layer.

The political layer has another gate. ANES shows that financial worry can sit
beside trust and reported vote, but party identity helps organize the pattern.
CCES shows that material proxies can coexist with both trust and action, or
low trust and action. Therefore action is not a simple endpoint of hardship,
and low trust is not equivalent to withdrawal. People may act because of
identity, efficacy, obligation, anger, social ties, or a specific institutional
encounter; they may also stay silent because action is costly or alternatives
are weak.

## The open arrow the program must pursue

The missing end-to-end test is a same-person or same-case design with:

1. a dated material, work, care, health, price, or service exposure;
2. the immediate cash, time, health, and alternative-option consequence;
3. attribution, fairness, dignity, trust, or legitimacy judgment;
4. consumer, civic, or political action; and
5. a later remedy, exit, recovery, security, or institutional response.

The current cross-source record is useful precisely because it does not fill
that gap by assumption. It gives the acquisition program a measurable schema
for the next longitudinal or linked-case pass.

## Limits and counterexamples

- SIPP, ATUS, MEPS, ANES, and CCES have different people, units, dates,
  weights, missingness, and estimands; no values are pooled here.
- A work-hours change is not automatically lost work; an eldercare time
  contrast is not automatically care-caused employment loss.
- Higher total health expenditure is not necessarily higher out-of-pocket
  burden, and a reported vote is not a direct measure of trust or material
  evaluation.
- Employment continuity is not proof of a good job, free choice, or the absence
  of health-related work loss; the MEPS status fields do not observe the event
  or the household's adjustment around it.
- Joint trust/action percentages can be generated by composition or identity;
  they do not identify a sequence from hardship to politics.
- The strongest counterexample to a simple burden-to-vote story is the
  identity-conditioned ANES pattern: strong partisans' reported votes remain
  concentrated across worry categories while independents vary more visibly.

## Reproduction and source trail

The machine-readable [bridge record](../../../records/us-material-to-trust-action-bridge-2022-2025.json)
preserves the separate denominators, methods, subgroup definitions,
counterinterpretations, and retrieval hashes. Its component records are the
[material/work/care/health record](../../../records/us-material-work-care-health-crosssource-2022-2025.json),
[ANES worry/trust/vote record](../../../records/us-anes-panel-worry-trust-vote-2024.json),
and [CCES trust/action record](../../../records/us-cces-trust-action-joint-material-proxies-2024.json).

**Evidence status:** cross-source architecture and descriptive comparisons;
not a pooled burden index, causal pathway, or political-behavior estimate.
