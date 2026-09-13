# Material, time, and care linkage acquisition plan v1

**Checked:** 2026-09-12  
**Scope:** US societal trend program; material pressure, time transfer, care,
recovery, and meaning  
**Status:** acquisition and identification plan; no end-to-end result claimed

## Why this pass exists

The program already measures several population-level pieces:

```text
financial pressure / care concern
  -> substitution, reduced use, borrowing, saving cuts, or extra work
work, care, travel, paperwork, and social time
  -> security, health, trust, civic availability, or exit
```

Those pieces come from different source populations and are not silently the
same people. The next pass needs a design that holds a person or household
constant long enough to establish time order and measure alternatives.

## Required minimum record

An acceptable candidate must provide, for the same unit and a defined follow-up
window:

| Stage | Required fields | Current local coverage |
|---|---|---|
| Trigger | dated bill, price, care need, work-rule change, or financial shock | SHED has pressure and care measures; exact dated trigger is missing |
| Alternatives | cash/savings, family help, provider or job alternatives, transport, schedule control | SIPP and SHED provide partial resource context; practical alternatives are missing |
| Immediate response | purchase change, delay, borrowing, extra work, paid/unpaid care, travel, waiting, paperwork | SHED covers several money responses; ATUS covers time allocation; no same-unit join |
| Control | who could refuse, switch, appeal, change schedule, or obtain help | Existing sources identify some institutional stages; individual control is mostly open |
| Protected/sacrificed outcome | food, housing, health, rest, family time, social connection, civic availability, or work | Separate sources measure these outcomes; protected-versus-sacrificed pairing is open |
| Later outcome | recovery, persistence, debt, health, work, trust, action, or exit at 1/6/12 months | SHED panel measures selected persistence/reversal; time, meaning, and action follow-up are missing |
| Interpretation | attribution, fairness, dignity, belonging, legitimacy, and perceived efficacy | ANES/Pew and project-specific layers measure population meaning; same-event attribution is open |

## Existing-source fit test

| Source family | Same-unit strength | What it can deepen | What it cannot establish alone | Decision |
|---|---|---|---|---|
| SHED 2024–2025 panel | Repeated respondent; selected repeated variables | Financial-condition path, adaptation persistence, re-entry, and reversal | Exact event date, hours displaced, care recipient outcome, trust/action after the event | Use for recovery and counterexample cells |
| SHED annual care/health layers | Broad weighted adult samples | Care concern, health, unpaid care, and money adaptations across subgroups and years | Same respondent across years; causal event or time diary | Use for distribution, not linkage |
| ATUS 2024 and ATUS-CPS-linked fields | Person diary with work, care, household, and social-time measures | Time allocation, work location, schedule-related contrasts, and social availability | The price/bill/care event that produced the diary; later recovery or political meaning | Use for time measurement and subgroup design |
| SIPP monthly layers | Person/household month and transitions | Resources, work, benefit entry/exit, and recorded transition context | Detailed minutes, waiting, unpaid care, dignity, attribution, and civic response | Use for event timing and material context |
| NHTS/local-capacity layers | Trip/place or county comparison | Reachability, travel, vehicle access, and supply/replaceability context | Same household's service failure, care need, price response, or meaning | Use as matched-place conditioning |

The immediate conclusion is an acquisition gap, not a null result: the current
bundle can triangulate the societal pattern and identify plausible moderators,
but it does not contain every required field in one same-unit design.

## Priority acquisition routes

1. **Longitudinal household route:** identify a panel with repeated financial,
   work, care, health, time, and subjective/political measures. Verify the
   variable dictionary and timing before downloading or linking records.
2. **Event-ledger route:** collect dated administrative, consumer, employer,
   or service events and pair them with a consented person/household diary at
   baseline and follow-up. This is the strongest route for alternatives,
   control, interpretation, and remedy, but requires privacy, consent, and
   retention controls.
3. **Modular bounded route:** use SHED panel for financial persistence, an
   ATUS/CPS-compatible time module for work and care, and SIPP for monthly
   resources. Report this as three complementary estimates unless identifiers
   and design actually permit a valid join.

## Go/no-go rules

Promote a material/time/care arrow only if the candidate has:

- a stable person, household, case, or valid matched-place unit;
- an observed or reliably dated trigger and a post-trigger measurement;
- explicit alternatives and at least one control variable;
- separate paid time, unpaid time, money, and outcome fields;
- a comparison or counterexample with similar exposure and different room;
- denominator, missingness, attrition, weight, and uncertainty documentation;
- a defined recovery window; and
- direct meaning/action measures, or an explicit statement that that arrow
  remains open.

If any of these fail, retain the output as reported, estimated, compared, or
open. Do not rename a cross-source alignment as a same-household causal result.

## Connection to the broader program

This pass is one lane in the 14-theme program. Its endpoint is not “what one
household did.” The purpose is to learn, across many units and institutions,
how material conditions reorganize time and care, how the burden is distributed,
and when those experiences become trust, cultural meaning, collective action,
consumer exit, firm response, or political demand.

Related: the [broad end-to-end event ledger](../../templates/US-BROAD-EVENT-LEDGER_V1.md),
the [time/work/care/social participation layer](time-work-care-social-participation-layer-v1.md),
the [price-pressure/time-transfer bridge](price-pressure-time-social-participation-cross-source-bridge-v1.md),
and the [next-pass queue](../../US-BROAD-NEXT-PASS-QUEUE_V1.md).
