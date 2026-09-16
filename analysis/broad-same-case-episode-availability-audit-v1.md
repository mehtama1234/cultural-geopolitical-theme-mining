# Broad same-case episode availability audit v1

**Status:** stage-availability audit; no synthetic episode or causal estimate
**Checked:** 2026-09-16
**Machine record:** [same-case episode availability audit](data/broad-same-case-episode-availability-audit-v1.json)

## Why this audit matters

The broad program's most important missing middle is not another measure of
pressure. It is the ability to follow one episode through the decision and
consequence chain:

```text
dated exposure
  -> actor and alternatives
  -> effort, money/time trade-off, and adaptation
  -> protected or sacrificed outcome
  -> institutional response and verified remedy
  -> meaning, trust, action, recovery, persistence, or exit
```

This audit tests whether the existing local records can support that route.
It keeps different respondents, complaints, health events, and survey panels
separate.

## Stage coverage

| Local source surface | Strongest stages | Critical missing stages |
|---|---|---|
| CFPB student-loan event ledger (25 rows) | Public route, complaint/event handling | Recipient alternatives, verified remedy, recovery, trust/action, exit |
| Platform remedy dry-run (27 episodes) | Adjudication, reactivation, some lost-remuneration orders | Alternatives, remedy receipt/durability, post-event status, practical exit |
| SHED recontact panel (4,419 respondents) | Adaptation, care/financial persistence, later status | Dated actor/event, institutional response, remedy, meaning/action, exit |
| HTOPS linked panel (6,564 respondents) | Same-ID timing, later material outcomes, institutional confidence | Actor, alternatives, attribution, action, remedy, recovery/exit |
| MEPS bounded event ledger (3 event surfaces) | Person-linked event ordering, payment and later health/work context | Complete route, remedy, trust/action, practical exit |

## Result

No current local source supplies all nine required stages. The platform ledger
comes closest to a response/remedy surface; MEPS, SHED, and HTOPS provide
different kinds of person-level timing or persistence. Those are useful
complements, but they cannot be joined into one consumer or household story.

The safe broad-program conclusion is therefore a measurement result: the atlas
has substantial exposure, adaptation, route, and selected follow-up evidence,
but not a closed same-case event chain. This explains why the program should
prioritize an episode key and stage-specific missingness over additional
cross-sectional pressure measures.

## Next decisive test

Choose one lawful source with a stable episode identifier—consumer complaint,
public-program case, financial account event, health-care episode, or workplace
intervention—and require actor, alternatives, effort, protected/sacrificed
outcome, verified remedy, attributed cause, later trust/action, and exit. A
valid negative result is one that shows which stages remain unavailable.

## Reproduction

```text
python3 scripts/validate_broad_same_case_episode_availability.py
```

The audit uses committed local records and downloads nothing.
