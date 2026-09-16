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

The validator checks that all four committed source records exist and that each
coverage row states its unit, surfaces, timing, actor boundary, and limitation.
No data is downloaded.
