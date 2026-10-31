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

## Named-case refresh

These cases move the packet from vulnerability and reporting stages into
service dependency, workaround and user-continuity evidence:

### AE6 — CrowdStrike software-update outage

GAO reports that a July 2024 CrowdStrike software update caused Windows systems
to crash and disrupted commercial flights, hospital care and other critical
infrastructure. The incident was not a cyberattack; its importance is that
software supply-chain concentration and testing failure can produce a
cyber-resilience outcome without a hostile intrusion. It closes a named
dependency-to-outage route. It does not provide one uniform recovery time or
fully measure passenger, patient, worker and financial burdens across affected
operators.

### AE7 — Synnovis pathology ransomware, London

NHS and NCSC accounts describe the June 2024 ransomware attack on Synnovis, a
pathology provider serving London NHS organizations. Access to blood-grouping,
antibody-screening and crossmatching systems was disrupted; NHS Blood and
Transplant expanded hours, prioritized urgent cases and relied more heavily on
O-negative blood to preserve emergency and surgical care. The UK government
reports approximately 11,000 postponed outpatient appointments and elective
procedures. This closes a supplier-to-clinical-continuity chain and makes
workaround burden visible. It does not close every patient outcome, full data
exposure, long-run trust effect or recovery for all affected services.

### AE8 — Advanced NHS supplier ransomware

The UK National Data Guardian reports that the 2022 ransomware attack on
Advanced, a software supplier to NHS trusts and care organizations, took some
systems offline, including Adastra systems supporting emergency care and NHS
111. Some systems returned quickly while others remained unavailable for months;
organizations used handwritten clinical notes and experienced backlogs. This
is a strong continuity case because the workaround itself became a source of
labor, clinical-safety and record-quality burden. It does not establish a
complete patient-level harm estimate or prove that all recovery controls failed.

### AE9 — Marks & Spencer third-party impact

The NCSC’s 2025 annual review reports that the ransomware attack affecting
Marks & Spencer and its insurers was estimated to exceed £300 million and uses
it to illustrate that disruptive cyber incidents extend beyond the victim
organization to customers, third parties and wider society. This closes an
enterprise-to-ecosystem impact route. The public account does not provide a
complete customer-level ledger of unavailable services, lost time, workaround,
compensation or trust recovery, so the cost estimate must not be treated as a
complete social-loss measure.

### AE10 — UK Cyber Security Breaches Survey recovery boundary

The UK 2025/26 survey reports that 87% of affected businesses and 91% of
charities said they restored operations within 24 hours after their most
disruptive identified breach or attack. This is useful aggregate recovery
evidence, but also a counterexample to equating “operations restored” with
resilience: the measure is self-reported, excludes organizations unable to
specify an incident, and does not capture data exposure, customer harm, manual
workarounds, uneven service quality or repeat vulnerability.

### Case-ledger conclusion

The refresh closes portions of software-supply-chain outage, supplier
dependency, clinical workaround, ecosystem spillover and reported restoration.
It also sharpens the central boundary: a patch, restart or restored business
process may coexist with patient delay, manual burden, data compromise,
customer loss or residual exposure. The decisive ledger remains:

`asset/dependency → disclosure or failure → prioritization/patch → detection and containment → restoration → user workaround and continuity → repeat exposure, trust and harm`

No case yet closes that route with comparable asset-level downtime, user burden,
recovery quality and repeat-exposure measures across operators.

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

## Sources

- CISA, [Lessons learned from incident-response engagements](https://www.cisa.gov/sites/default/files/2025-09/AA25-266A_advisory_cisa_shares_lessons_learned_from_ir_engagement.pdf): incident-response and resilience context.
- FBI, [Internet Crime Report 2025](https://www.fbi.gov/file-repository/2025_ic3report.pdf): reported cybercrime and loss signals, not a complete harm census.
- U.S. Government Accountability Office, [Cybersecurity oversight](https://www.gao.gov/products/gao-24-107733) and [critical-service risk](https://files.gao.gov/reports/GAO-25-108138/index.html): governance, exposure and continuity context.
- CISA, [law-enforcement cyber incident reporting](https://www.cisa.gov/sites/default/files/publications/Law%20Enforcement%20Cyber%20Incident%20Reporting_3.pdf): reporting and measurement boundary.
