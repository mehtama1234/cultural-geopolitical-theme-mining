# Material-to-meaning/action endpoint audit v1

**Status:** coverage audit only; no new estimate or pooled causal path  
**Checked:** 2026-09-16  
**Machine record:** [material/meaning/action endpoint audit](data/material-meaning-action-endpoint-audit-v1.json)

## Result

The local atlas has several strong partial bridges, but no source closes the
full chain:

```text
dated material event and responsible actor
  -> alternatives and trade-off
  -> attribution, trust, or meaning
  -> distinct political/civic action
  -> remedy, recovery, or later behavior
```

| Source | Material | Meaning | Action | Time/actor boundary |
|---|---|---|---|---|
| HTOPS April→June | Same selected respondent's material transitions | June Congress confidence and statistics agreement | Not observed | Two-wave timing; no dated actor or attribution |
| CCES 2024 | Gig work and student-loan responsibility proxies | Federal/state trust | Six civic-action indicators | Same-wave joint cells; no dated shock |
| CES 2018/2020 medical affordability | Medical-expense hardship | Responsibility attribution | Targeted political participation | Module-year comparison; no bill/remedy follow-up |
| ANES 2016–2020–2024 panel subset | Pre-election financial worry | Federal trust and party-conditioned judgment | Post-election reported vote | Temporal ordering, but no direct material episode or actor |
| ANES health-cost panel layer | Health-care payment concern | Federal trust and responsibility context | Post-election preference for more government help with health insurance | Adds policy demand with panel ordering; no verified bill, alternative, remedy, or causal action path |

## Policy-demand checkpoint

In the committed ANES record, the share preferring increased government help
with health-insurance costs is 57.5% among respondents not at all concerned
about paying health-care costs and 61.3% among those extremely concerned—a
3.8-point descriptive difference in a 4,650-case valid cross-tab. The concern
gradient is not universal: among strong Democrats the corresponding values are
84.6% and 71.2%, among strong Republicans 30.7% and 50.0%, and among
independents 49.0% and 55.4%.

These cells show that policy demand is an identity-conditioned endpoint, not a
simple monotonic translation of payment concern. They do not identify the
respondent's bill, responsible actor, alternative, or a causal effect of
health-cost exposure.

The CES medical-affordability modules add a more direct action endpoint. In
2018, the weighted turnout share was 41.7% among respondents reporting a
medical-expense crisis versus 57.2% among those without one; official contact
was 23.3% versus 21.4%. In 2020, turnout was nearly equal (61.2% versus
62.3%), while official contact was 28.3% versus 17.9%. Within hardship cases,
federal attribution was reported by 27.6% in 2018 and 22.4% in 2020; the
attribution-conditioned official-contact shares were 26.3% and 42.7%, and
protest shares were 11.1% and 23.6%, respectively.

These figures show why “political response” must remain a menu of distinct
actions: turnout, contact, protest, and attribution do not move together. The
modules support a reported hardship→attribution/action association, not proof
that one bill caused one act or that lower turnout means withdrawal.

## What this means for the broad goal

Material pressure does not translate through one universal political channel.
The local evidence shows persistence, subgroup heterogeneity, attribution, and
action as distinct measurable surfaces. It does not justify a material-stress
score, a generalized distrust claim, or a causal hardship-to-vote story.

The highest-value next record is therefore not another generic trust question.
It is a repeated-respondent or event-compatible observation with a dated
exposure, responsible actor, usable alternative, perceived fairness or blame,
prior judgment, distinct action, institutional response, and later recovery or
exit. The raw HTOPS files are not currently retained locally, so this audit
does not rerun or extend their estimates.

## Reproduction

```text
python3 scripts/validate_material_meaning_action_endpoint_audit.py
```

The validator checks that all five committed source records exist and that each
coverage row states its unit, surfaces, timing, actor boundary, and limitation.
No data is downloaded.
