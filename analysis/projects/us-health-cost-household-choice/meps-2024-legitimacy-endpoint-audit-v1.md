# MEPS 2024 legitimacy-endpoint audit

**Checked:** 2026-09-15  
**Status:** acquisition-boundary result; no legitimacy estimate

## Finding

The MEPS 2024 HC-256 public-use file contains the health-cost, access,
financial-room, employment, time, and adaptation fields used in this lane, but
it does not contain a direct trust, attribution, complaint, provider/insurer
switching, vote, organizing, or public-action endpoint. A field-name and label
scan found no variables for those constructs. The ESAQ fields can show denial,
payment strategy, sacrifice, work constraint, and family-care substitution, but
they cannot show whether the respondent blamed an institution, changed trust,
contacted an official, switched providers, or exited a system.

This is a useful negative result. It prevents the current MEPS care-delay and
adaptation findings from being promoted into a legitimacy claim merely because
the household burden is large. It also makes the next acquisition requirement
precise: a compatible panel or matched design must add prior identity/trust,
post-exposure attribution, an institutional response, and later judgment or
action.

## Supported boundary

```text
health need / cost / coverage
  -> care delay, payment strategy, sacrifice, work and family-care context
  -> [MEPS public-use endpoint ends]
  -> trust, attribution, complaint, switching, vote, organizing, or exit
```

The current [end-to-end finding](findings/us-health-cost-household-choice-end-to-end-001.md)
therefore classifies the final arrow as inferred across sources/open. The
[episode acquisition protocol](health-cost-episode-acquisition-protocol-v1.md)
defines the fields required to close it.

## Audit scope

The audit covered the HC-256 variable names and labels, including the ESAQ
section (`EQ*`), care-access fields (`DLAY*`/`AFRD*`), financial-well-being
fields (`FW*`), medical debt, employment, health, and coverage. It is a
structural field-availability audit, not evidence that respondents lacked
these experiences.

## Next compatible routes

- Acquire a restricted or newly released panel with person/household identity
  preserved across health cost, institutional encounter, trust, and action.
- Use MEPS/SHED for exposure and adaptation and ANES, GSS, or CCES for judgment
  and action only as a clearly labeled cross-source bridge until identifiers
  and timing are compatible.
- Preserve counterexamples: hardship without distrust, distrust without
  withdrawal, complaint without switching, and remedy without restored health.
