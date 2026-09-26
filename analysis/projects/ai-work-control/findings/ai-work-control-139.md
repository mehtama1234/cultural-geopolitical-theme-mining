# Finding 139: Cloud capacity can grow before control over failure is proven

**Status:** bounded federal cloud-security and provider-accountability finding · **Checked:** 2026-09-22

## The bounded finding

GAO reviewed eight cloud systems across four federal agencies. Only some of
the selected systems fully implemented continuous monitoring, incident
response and recovery, and measurable service-level agreements. Three systems
fully performed continuous monitoring, five fully implemented the service-level
agreement practice, and the remaining three did not consistently define how
performance would be measured or enforced. GAO made 12 recommendations, which
were still open pending confirmation of agency action.

The plain-language route is:

```text
move government work into the cloud
  -> agency and provider share control
  -> monitoring, recovery, and service rules are partly documented
  -> breach, outage, data loss, user effect, and public trust [open]
```

Cloud adoption can make capacity cheaper or more flexible while making
responsibility harder to see. A contract can name a service without proving
that the agency can detect a problem, recover quickly, or enforce the promised
level of service.

## Why it matters for the broader atlas

This adds a digital version of the program's recurring pattern: capability is
visible before practical control. It connects public capacity, private
providers, infrastructure dependence, and trust. The missing question is not
only whether an agency has cloud storage or software; it is who can see a
failure, who can force correction, how long recovery takes, and what happens
to the people or public service relying on the system.

## Limits and counterexamples

- The review covers eight selected systems, not all federal cloud systems.
- System names were withheld for sensitivity.
- Partial implementation does not prove a breach, outage, data loss, or user
  harm.
- A contract without explicit metrics may still perform acceptably.
- Open recommendations show unfinished governance work, not a demonstrated
  cybersecurity incident.

## Next test

For a named cloud system, follow one incident or recovery episode through
detection, provider notification, agency action, restoration time, service
effect, and corrective enforcement. Keep control documentation separate from
actual incident and user outcomes.

## Sources

[GAO-26-108443: Cybersecurity and cloud data](https://www.gao.gov/products/gao-26-108443)

[GAO full report](https://files.gao.gov/reports/GAO-26-108443/index.html)

[Machine-readable trend record](../../../records/us-gao-federal-cloud-security-control-gaps-2026.json)

**Evidence status:** selected-system control implementation and open corrective
recommendations are documented; actual incidents, recovery, data effects, and
public-user consequences remain open.
