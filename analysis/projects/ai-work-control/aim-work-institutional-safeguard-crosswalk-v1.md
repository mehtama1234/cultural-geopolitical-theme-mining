# AIM-WORK exposure to institutional safeguard crosswalk

**Status:** cross-source governance bridge; implementation and worker outcomes remain open  
**Checked:** 2026-09-15  
**Purpose:** connect worker-side algorithmic-management practices to documented control points without treating rules as observed effects

## Why this bridge is needed

The AIM-WORK survey measures whether workers encounter different kinds of
algorithmic direction and evaluation. The German works-council records and the
SAG-AFTRA agreement describe institutional responses that can constrain or
condition automated systems. They are different units and populations. This
crosswalk joins them by function, not by pretending that the same workers or
workplaces appear in both records.

## Crosswalk

| Worker-side exposure or risk | Documented safeguard record | What the safeguard can plausibly control | Evidence status | Still missing |
|---|---|---|---|---|
| `amtime` / `amact`: automated schedules or task allocation | IBM framework; Deutsche Telekom/works-council AI records | Notice, inspection, human decision-making, and prior consultation around systems that organize work | Direct rule/participation record | A live schedule/task deployment, worker notice, override use, schedule predictability, or remedy |
| `amspeed` / `amdir`: automated pace or instructions | IBM framework risk classification, human-decision principle, correction process, AI Ethics Council | Limits on direct intervention, correction of false recommendations, escalation, and possible exclusion of high-risk systems | Direct rule record; implementation account partly reported | Whether a live pace/instruction system was changed, stopped, or experienced as less intensive |
| `perfrank`: ranking or comparative evaluation | IBM framework transparency, bias/data-quality inspection, and category-5 restriction; BTQ implementation interview | Visibility into data and purpose, challenge to false or discriminatory recommendations, and a stated limit on personnel decisions | Direct agreement plus representative interview | Actual ranking system, worker challenge, retaliation, promotion/discipline consequence, or enforcement |
| `perfpoints` / `perfcancel`: incentives or performance-linked withdrawal | IBM framework correction and human-review rules; risk classification | A route to correct false outputs and prevent automatic personnel action without substantial workforce benefit/harm reduction | Direct rule record | Whether points or cancellation affected pay, hours, access to work, stress, or exit |
| Employee-data monitoring and profiling adjacent to AM | Deutsche Telekom AI manifesto; IBM works-council inspection rights | Data-purpose review, transparency, bias analysis, algorithm/data-quality inspection | Company/union/agreement record | Data inventory, audit result, worker understanding, correction time, or privacy outcome |
| Platform task allocation, evaluation, earnings, status, or account restriction | EU Platform Work Directive 2024/2831, Articles 7–11 | Data limits, impact assessment, worker/representative views, written explanations, human override, review within two weeks, correction or remedy | Direct legal rule; platform scope | National implementation, compliance, review success, retaliation, earnings recovery, or system discontinuation |
| Digital replica or synthetic substitution: a related control/replaceability case | SAG-AFTRA 2023 agreement and union guidance | Notice, consent, compensation, bargaining, and bounded use of a worker’s voice/likeness/performance | Direct collective-bargaining rule | Producer compliance, refusal consequences, hiring effects, substitution rate, or performer outcome |

## What the crosswalk establishes

1. Worker voice becomes analytically useful when it attaches to a control point:
   inspection, notice, consent, correction, human review, bargaining, or a
   refusal/stop condition.
2. The same word—“oversight”—covers different mechanisms. A works council’s
   inspection right is not the same as a worker’s appeal; human decision-making
   is not the same as human authority to reject an output; consent over a digital
   replica is not the same as protection from substitution.
3. The records are strongest on ex ante design and stated procedural rights.
   They do not yet show the frequency of use, resolution time, enforcement,
   worker coverage, or downstream material outcomes.
4. AIM-WORK can test whether exposure is associated with autonomy, stress,
   breaks, working time, and work location. The governance records identify
   candidate moderators, but cannot establish moderation without a compatible
   workplace or worker key.

## The missing same-unit sequence

```text
named system or rule
  -> worker notice and actual exposure
  -> output, error, or burden
  -> correction / appeal / representative intervention
  -> resolved or unresolved outcome
  -> pay, time, health, household, stay/exit, or trust consequence
```

The current evidence supports the existence and shape of several procedural
routes. It does not follow this sequence for the same worker or workplace.

## Acquisition design for the next pass

For one named deployment, collect:

1. the agreement or policy in force and the system’s risk classification;
2. implementation date, affected tasks, vendor/owner, and worker population;
3. notice, training, monitoring, human-review, and opt-out records;
4. the complaint, correction, appeal, or works-council intervention log;
5. resolution date and whether the output or rule changed; and
6. worker-level or workplace-level outcomes with a valid comparison and
   household follow-up where the claim travels that far.

The smallest credible test is not another policy statement. It is one resolved
or unresolved intervention episode tied to one system and one affected worker
or workplace.

## Sources

- [JRC AIM-WORK practice and country map](jrc-aim-work-practice-country-map-v1.md)
- [German works-council AI source record](german-ai-works-council-source-record-v1.md)
- [SAG-AFTRA digital-replica source record](sag-aftra-digital-replica-source-record-v1.md)
- [EU Platform Work Directive algorithmic-management source record](eu-platform-work-directive-algorithmic-management-source-record-v1.md)
- [Worker/workplace event ledger specification](worker-workplace-event-ledger-v1.md)
- [ILO social-dialogue case table](ilo-social-dialogue-case-table-v1.md)

**Evidence boundary:** this is a functional bridge across distinct source
families. It promotes no same-worker causal or implementation outcome.
