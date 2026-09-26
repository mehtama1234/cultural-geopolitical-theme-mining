# NBER source-reuse audit v1

**Checked:** 2026-09-23  
**Purpose:** distinguish legitimate reuse of one working paper across separate
evidence layers from accidental duplicate promotion of the same observation.

## Rule

The same primary paper may support more than one record when the records keep
different units, estimands, periods, or synthesis roles explicit. Reuse is not
legitimate when two records have the same source unit, title, observation,
retrieval hash, and boundary with only a different filename or trend ID. The
latter must be consolidated into one canonical record.

## Current reviewed reuse

| Paper | Records retained | Decision |
|---|---|---|
| NBER 29836, NYC tenant representation | `us-nber-nyc-tenant-legal-representation-housing-court-2016-2019`; `us-nber-housing-court-legal-representation-tenant-outcomes-2022` | Retain as distinct extraction layers: the first preserves the detailed administrative sample, IV stages, and execution boundary; the second is a compact court-access surface used by the evidence matrix. Both point to the same program but are not identical records. |
| NBER 32315, medical-debt relief | `us-medical-debt-relief-rct-outcome-separation-2018-2020`; `us-medical-debt-relief-randomized-response-2018-2020` | Retain as distinct synthesis layers: one foregrounds outcome separation and the other response/reporting context. The shared experiment arms and boundaries remain explicit; they must not be written as independent studies. |
| NBER 33795, generative-AI work patterns | `us-nber-shifting-work-patterns-generative-ai-2025`; `us-ai-management-bargaining-voice-crosssource-2024-2026` | Retain: the first is a field-experiment record; the second is an explicitly non-pooled cross-source synthesis that places it beside management and voice evidence. |
| NBER 35677, task-level AI adoption | `us-nber-task-level-genai-adoption-2026`; `us-ai-utilization-output-mobility-control-crosssource-2025-2026` | Retain: the first is the task-adoption source record; the second is a non-pooled measurement architecture with BEA, executive, and labor-market stages. |

## Consolidation completed

NBER 35729 had two byte-identical primary records with the same title, source
unit, observation, retrieval hash, and boundary. The duplicate
`comparative-nber-microenterprise-consumer-surplus-2026` was removed; the
canonical `comparative-nber-microenterprise-credit-consumer-surplus-2026`
record remains and is the matrix target.

## Future promotion control

Before adding a record from an NBER paper, search the registry by paper number
and compare source unit, observation measures, retrieval hash, and boundary.
If the new object is a synthesis, label it as non-pooled and link the source
records; if it is identical, extend the canonical record or add a distinct
observation rather than creating a second trend ID.
