# Rotation AE: Cyber resilience, critical services and recovery

**Date:** 2026-10-29  
**Lane:** cybersecurity / critical infrastructure / public service continuity / geopolitical risk  
**Status:** Tier 1 bounded distinction plus Tier 2 service-continuity question

## Research question

When a vulnerability is disclosed, cataloged, reported or assessed, what later
stages must be closed before an operator, government or community can claim
protected and continuous service?

## Conversion chain

```text
vulnerability or threat signal
  -> disclosure/advisory/report
  -> owner prioritization and patch/configuration
  -> detection and incident response
  -> containment/recovery and service restoration
  -> user continuity, trust and reduced repeat exposure
```

Cybersecurity evidence often measures the first three stages. Resilience is a
later claim: whether the named service remained available or was restored, who
absorbed the operational burden, and whether the same weakness recurred.

## Evidence packet

| ID | Source and direct observation | Stage closed | Stage still open |
|---|---|---|---|
| AE1 | [CISA lessons learned from a GeoServer incident](https://www.cisa.gov/sites/default/files/2025-09/AA25-266A_advisory_cisa_shares_lessons_learned_from_ir_engagement.pdf) records a vulnerability disclosed June 30, exploited July 11, added to the KEV Catalog July 15, and still unpatched when another server was exploited July 24. | Named vulnerability-to-exploitation timeline and response lesson | Service impact, restoration, user continuity and repeat exposure after remediation |
| AE2 | [FBI 2025 IC3 annual report](https://www.fbi.gov/file-repository/2025_ic3report.pdf) reports cyber threats to critical infrastructure across the 16 critical-infrastructure sectors, including ransomware and data-breach complaints. | Reported complaint volume and sector classification | True incidence, operational downtime, recovery cost and affected-user outcome |
| AE3 | [GAO CrowdStrike outage resilience report](https://www.gao.gov/products/gao-24-107733) identifies challenges in cyber resiliency and recommends implementation of federal requirements intended to improve government and critical-infrastructure response. | Governance and recommendation boundary | Named service restoration, dependency chain, customer harm and learning persistence |
| AE4 | [CISA cyber incident reporting guidance](https://www.cisa.gov/sites/default/files/publications/Law%20Enforcement%20Cyber%20Incident%20Reporting_3.pdf) emphasizes reporting even when complete information is unavailable and requests affected assets, detection, entry vector and status-change data. | Reportable-event fields and information-sharing route | Whether reporting produced timely mitigation, recovery and community protection |
| AE5 | [GAO NASA cybersecurity assessment](https://files.gao.gov/reports/GAO-25-108138/index.html) states comprehensive risk management is critical to protecting systems, detecting suspicious activity and responding to incidents, while assessing implementation gaps in selected projects. | Risk-management and assessment boundary | Operational resilience of the affected mission, user-facing continuity and repeat risk |

## Stage audit

| Observed signal | Safe interpretation | Prohibited leap |
|---|---|---|
| Vulnerability disclosed | A weakness became publicly or operationally knowable | Owners patched it before exploitation or users were protected |
| KEV/catalog inclusion | A vulnerability received elevated remediation attention | Every exposed system was remediated on time |
| Incident reported | An organization or victim entered a reporting channel | Reporting reduced harm or restored service |
| Risk assessment/recommendation | Governance identified a control or implementation gap | The named mission or community experienced continuity |
| Threat complaint count | Reported cyber events are material and sector-relevant | Counts equal total incidence, losses, downtime or causal national impact |

## Bounded finding

> Cyber resilience is not established by disclosure, catalog inclusion, incident
> reporting or risk assessment alone. The stronger claim requires a named asset,
> remediation, detection/response, restoration, user continuity and evidence
> that repeat exposure or residual dependency was reduced.

The CISA GeoServer sequence is a useful conversion case because it closes
disclosure, exploitation and delayed patching in a named timeline. It still
does not close the complete service-to-community outcome chain.

## Cultural and geographical interpretation

Cyber incidents become social events when a hospital, water utility, school,
benefit system, transit service or local government cannot perform a familiar
function. The burden is distributed through waiting, manual workarounds,
privacy risk, travel to another service point, lost wages, delayed care and
uncertainty about whether systems can be trusted again.

Geography matters because smaller or rural operators may share vendors, have
fewer security staff, and have less redundancy. Geopolitical meaning emerges
when a cyber event is attributed to a state, criminal ecosystem or dependency
concentration; attribution and response remain separate from immediate user
recovery.

## Counterexamples and limits

- A vulnerability can be disclosed and patched before exploitation; disclosure
  is not evidence of failure.
- A reported incident can be contained with little user disruption; complaint
  counts do not measure severity.
- A national outage can reveal dependency and still be restored rapidly; outage
  existence is not permanent service failure.
- CISA and GAO materials are designed for risk management and oversight, not
  population estimates of all cyber harm.
- FBI complaint data are reported incidents and losses, subject to reporting
  behavior and classification limits.

## Promotion decision

Promote the disclosure/reporting-versus-resilience distinction to Tier 1. Keep
the service-continuity mechanism in Tier 2 until a named critical service links
technical exposure to user-facing downtime, restoration, workaround burden,
repeat exposure and affected-community trust.

## Next test

Create a service-level ledger for one critical sector with fields for asset,
vulnerability, disclosure, KEV date, patch/configuration, detection, downtime,
manual workaround, restoration, affected users, cost, repeat event and public
attribution. Compare operators with and without a documented remediation path.
