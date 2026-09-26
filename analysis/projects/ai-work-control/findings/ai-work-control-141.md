# Finding 141: A safety system can know the threat before it can see it happening

**Status:** bounded aviation-cybersecurity and public-safety finding · **Checked:** 2026-09-22

## The bounded finding

FAA has identified spectrum threats such as spoofing and jamming to aviation
communications, but GAO found that FAA had not completed all risk assessments,
did not have defined real-time monitoring for all those threats, and could
often investigate only after an incident was reported. GAO also found that only
two of eight collaboration practices were fully addressed and made nine open
recommendations.

The plain-language route is:

```text
communication threat is identified
  -> monitoring, coordination, and authentication are incomplete
  -> detection and response may depend on someone reporting the problem
  -> actual flight disruption, safety effect, and passenger burden [open]
```

The finding is not that aviation was unsafe on every flight. It is that the
institution could name important risks before it had a complete way to detect,
share, and mitigate them in real time.

## Why it matters for the broader atlas

This adds a high-stakes public-safety version of the atlas's digital-control
theme. Modern systems can be highly capable and still rely on delayed reports,
fragmented coordination, or weak accountability at the point where failure
matters. It also connects public infrastructure to private operators and
international flight routes: safety depends on shared technical and
institutional rules, not only on one agency's internal capacity.

## Limits and counterexamples

- GAO assessed eight selected systems, not every aviation system.
- Identified vulnerabilities do not prove an attack, outage, accident, or
  passenger harm.
- A possible spoofed message is a risk scenario, not an observed event.
- Existing informal or interagency coordination may work despite incomplete
  formal procedures.
- Open recommendations show unfinished governance work, not realized failure.

## Next test

Follow a named aviation communication incident through detection, attribution,
coordination, mitigation, flight effect, passenger or carrier consequence, and
post-incident correction. Keep threat identification separate from actual harm.

## Sources

[GAO-26-108439: Aviation Cybersecurity](https://www.gao.gov/products/gao-26-108439)

[GAO full report](https://files.gao.gov/reports/GAO-26-108439/index.html)

[Machine-readable trend record](../../../records/us-gao-aviation-spectrum-cybersecurity-monitoring-gaps-2026.json)

**Evidence status:** threats, control gaps, collaboration limits, and open
recommendations are documented; actual cyber incidents, flight effects, safety
outcomes, and public consequences remain open.
