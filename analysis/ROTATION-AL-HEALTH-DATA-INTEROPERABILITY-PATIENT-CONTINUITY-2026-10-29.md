# Rotation AL: Health-data interoperability, patient access and continuity

**Date:** 2026-10-29  
**Lane:** health technology / patient agency / clinical coordination / trust  
**Status:** Tier 1 bounded distinction plus Tier 2 care-continuity question

## Research question

When hospitals, public agencies and health networks exchange electronic health
information or expose patient APIs, what later stages determine whether the
right information is understandable, available at the point of care, acted on,
and converted into safer and more continuous care?

## Conversion chain

```text
record created
  -> data formatted and exchanged
  -> patient/provider can locate and access it
  -> information is understood and trusted
  -> clinician or patient acts on it
  -> coordinated care, correction and health continuity
```

Interoperability is a technical and institutional capability. It is not by
itself proof that data are complete, timely, matched to the right person,
usable by the patient, available to the clinician, or incorporated into a care
decision.

## Evidence packet

| ID | Source and direct observation | Stage closed | Stage still open |
|---|---|---|---|
| AL1 | [ONC hospital API data brief](https://healthit.gov/data/data-briefs/hospital-use-of-apis-to-enable-data-sharing-between-ehrs-and-third-party-technology/) reports that in 2024 about 9 in 10 hospitals enabled patient electronic access via an API, while standards-based API use was lower; patient-generated-data submission was also less universal. | Hospital capability for patient/API access | Patient discovery, comprehension, use, privacy, clinician action and outcome |
| AL2 | [ONC hospital patient-engagement capabilities](https://healthit.gov/data/data-briefs/growth-health-it-enabled-patient-engagement-capabilities-among-us-hospitals-2021/) reports that in 2024 8 in 10 hospitals had all foundational capabilities, 2 in 3 all emerging capabilities, and fewer than half all advanced capabilities. | Capability maturity categories | Patient use, data quality, care coordination and equitable access |
| AL3 | [ONC interoperable exchange report](https://www.healthit.gov/sites/default/files/2024-05/Interoperable-Exchange-of-Patient-Health-Information-Among-U.S.-Hospitals-2023.pdf) reports that 71% of hospitals routinely had necessary external clinical information available electronically in 2023, but only 42% often used that information. | Availability and use distinction at hospitals | Correctness, timeliness, action, patient understanding and continuity |
| AL4 | [ONC health-information-organization survey](https://healthit.gov/data/data-briefs/trends-in-health-information-organizations-experiences-of-perceived-information-blocking-2019-2025/) reports that potential fee/pricing information blocking remained the most reported practice in 2025 and that most HIOs said information blocking affected missingness and exchange operations. | Organizational barrier and missingness signal | Named patient harm, correction, alternative route and clinical outcome |
| AL5 | [GAO VA/DoD health-care sharing report](https://files.gao.gov/reports/GAO-25-107497/index.html) identifies longstanding barriers including inability to exchange comprehensive patient information, access to military bases, inconsistent relationships and billing/reimbursement issues. | Named institutional coordination barriers | Same veteran’s record continuity, care decision, correction and health outcome |

## Stage audit

| Observed signal | Safe interpretation | Prohibited leap |
|---|---|---|
| Patient API exists | A technical access route is enabled | Patients can find, read, download, correct or use the data |
| Standards-based exchange | Data can move through a defined standard | Data are complete, correctly matched, timely or semantically usable |
| External information available | A provider can access information electronically | The provider used it, trusted it or acted on it |
| Information blocking is reported | Organizations perceive a barrier affecting exchange or missingness | A named patient suffered a quantified clinical harm or every barrier is illegal |
| Integrated EHR network exists | Systems and institutions are connected in a formal architecture | Coordination, billing, privacy, patient agency and continuity are solved |

## Bounded finding

> Health-data interoperability is a conversion problem: electronic availability
> is not clinical use, patient understanding or continuous care. The evidence
> must distinguish capability, exchange, access, comprehension, action,
> correction and outcome.

This is not an argument against APIs, FHIR, health-information networks or
shared records. It is a measurement boundary that prevents technical coverage
from being mistaken for patient benefit.

## Cultural and geographical interpretation

The patient experiences interoperability as whether a new clinician knows what
happened before, whether a test is repeated, whether medication or identity is
correct, whether a caregiver can understand the record, and whether a person can
challenge an error. The data architecture can therefore feel like continuity,
surveillance, bureaucratic opacity or a promise that fails at the care boundary.

Geography enters through health-system participation, rural and behavioral-health
providers, broadband and devices, language, disability, portal literacy,
military/federal boundaries and the availability of a human records office.
The same national standard can yield different care continuity depending on the
local network and the patient’s ability to act on the data.

## Counterexamples and limits

- Electronic availability can prevent duplicate testing, support safer care and
  genuinely improve coordination; capability is not useless merely because use
  is incomplete.
- A provider may not use an external record because it is irrelevant, stale or
  clinically inappropriate; nonuse is not automatically a failure.
- ONC hospital estimates are capability surveys, not patient-level outcome
  studies.
- Perceived information blocking is not a legal finding or causal estimate of
  patient harm.
- VA/DoD coordination barriers are institution-specific and should not be
  generalized to all health systems.

## Promotion decision

Promote the capability/exchange/access/use/continuity distinction to Tier 1.
Keep the mechanism in Tier 2 until a named patient or service line links data
availability to clinician/patient action, correction, repeated care, safety and
health outcome across place and subgroup.

## Next test

Build a care-transition ledger with record origin, exchange method, match status,
time, patient access, clinician view/use, correction, duplicate test or missed
information, care decision, follow-up and outcome. Stratify by rural/urban,
behavioral health, disability, language, age, payer and federal/tribal/VA route.
