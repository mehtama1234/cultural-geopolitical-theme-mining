# HTOPS 2025 local endpoint observability audit v1

**Checked:** 2026-09-16  
**Status:** local-artifact measurement audit; no new estimate

## Result

The retained local HTOPS panel record exposes 6,564 linked respondents, timed
April-to-June material measures, and selected institutional-judgment measures.
It does not expose the downstream fields needed to follow a complete
material-to-action episode:

```text
material condition → attribution → judgment/meaning → distinct action
  → remedy/recovery → switching, non-use, or exit
```

The absent endpoints are an artifact boundary, not a claim about the Census
PUFs. The raw April and June files and their dictionaries are not retained in
the current workspace, so this audit does not assert that those fields were
absent from the source files.

## Endpoint inventory

| Endpoint | Current local status | What can safely be said |
|---|---|---|
| Timed material condition/follow-up | Exposed | The linked record contains April-to-June expense, food, energy, price, work, and job-loss measures. |
| Institutional judgment | Exposed | Congress confidence and federal-statistics agreement are recorded; they are not attribution or action. |
| Responsible actor/attribution | Not exposed in retained record | No local field identifies whether the respondent blamed a firm, employer, government, price, or another actor. |
| Distinct civic/political action | Not exposed in retained record | No local vote, contact, complaint, appeal, organizing, volunteering, registration, or withdrawal field is represented. |
| Remedy/recovery/switching/exit | Not exposed in retained record | No local later remedy, recovery, switching, non-use, or exit endpoint is represented. |

This narrows the next acquisition gate. If the PUFs are reacquired, the first
task is a dictionary-and-shared-ID field audit, not a new cross-tab. Only a
field with an explicit universe, timing, missing-code rule, and compatible
respondent identifier should be added to the panel design.

## Why this advances the broad goal

The broad atlas is trying to explain how material conditions become social
meaning, institutional judgment, and action. The current HTOPS record can test
temporal material persistence and a bounded judgment counterexample, but it
cannot identify the conversion mechanism. Recording that boundary prevents
confidence, trust, or later hardship from being silently promoted into civic
action or cultural meaning.

The next decisive test remains an event-compatible same-respondent or
same-case record containing a dated exposure, responsible actor, alternative,
perceived fairness or blame, prior judgment, distinct action, institutional
response, and later recovery or exit.

## Reproduction

```text
python3 scripts/audit_htops_2025_local_endpoint_observability.py
```

The machine-readable result is
[htops-2025-local-endpoint-observability-audit.json](data/htops-2025-local-endpoint-observability-audit.json).
The source panel record is
[us-census-htops-material-trust-panel-april-june-2025.json](../../records/us-census-htops-material-trust-panel-april-june-2025.json).

**Evidence status:** local retained-record observability audit; not a complete
source-codebook audit and not a causal or population estimate.
