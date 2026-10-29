# Rotation AG: Digital identity, authentication and usable access

**Date:** 2026-10-29  
**Lane:** digital identity / public services / privacy / accessibility / trust  
**Status:** Tier 1 bounded distinction plus Tier 2 inclusion-and-recovery question

## Research question

When an institution requires identity proofing or multifactor authentication,
what converts an assurance control into an accessible, private, recoverable and
completed public-service encounter?

## Conversion chain

```text
service need
  -> identity evidence and proofing
  -> enrollment and authenticator
  -> login/federation and authorization
  -> completed service transaction
  -> recovery after loss, error, fraud or exclusion
  -> continued trust and use
```

The institution may optimize for assurance while the person experiences a
different system: missing documents, device or connectivity dependence,
biometric mismatch, accessibility barriers, language, privacy concern, fraud
hold, account lockout and an opaque recovery route.

## Evidence packet

| ID | Source and direct observation | Stage closed | Stage still open |
|---|---|---|---|
| AG1 | [NIST SP 800-63-4](https://www.nist.gov/publications/nist-sp-800-63-4-digital-identity-guidelines) separates identity proofing, enrollment, authenticators, management, authentication protocols and federation, and includes security, privacy and customer-experience considerations. | Assurance architecture and control vocabulary | Actual inclusion, service completion, error recovery and distributional effect |
| AG2 | [NIST identity-proofing guidance](https://pages.nist.gov/800-63-4/sp800-63a.html) describes evidence validation, attended/remote proofing and possible biometric comparison pathways. | Defined proofing methods and assurance requirements | Availability of evidence, accessibility, false rejection, privacy and successful enrollment |
| AG3 | [GAO IRS identity-verification report](https://files.gao.gov/reports/GAO-25-107273/index.html) reports that IRS users accessed IAL2 applications more than 150 million times from 2021–2024 and calls for stronger oversight of the identity-proofing program. | Large-scale use and oversight boundary | Who could not complete proofing, service outcome, false rejects and recovery |
| AG4 | [GAO GSA identity-verification report](https://files.gao.gov/reports/GAO-26-109261/index.html) reports that fraudulent accounts passed Login.gov identity-proofing services and that the sophistication of attempts was expected to increase. | Named fraud and technical-risk signal | Fraud-prevention trade-off, excluded legitimate users, appeal/recovery and service continuity |
| AG5 | [Login.gov accessibility information](https://www.login.gov/accessibility/) provides an accessibility statement and an identity-verification report route for users. | Formal accessibility and feedback route | Completion rates by disability, device, language, geography, proofing method and time-to-recovery |

## Stage audit

| Observed signal | Safe interpretation | Prohibited leap |
|---|---|---|
| NIST assurance level | A defined security and proofing requirement exists | The requirement is equally usable or fair for every population |
| Identity-proofing success or scale | Many transactions reached enrollment or authentication | People denied, abandoned, locked out or unable to recover are measured |
| Fraudulent accounts pass proofing | A false-acceptance risk exists | More strict proofing would improve net access or reduce harm without exclusions |
| Accessibility statement | The provider recognizes accessibility duties and offers a route | Real users can complete proofing or recover accounts across disability and device contexts |
| MFA/authentication control | Account security is strengthened in a defined model | The person can authenticate at the needed time and place for the needed service |

## Bounded finding

> Digital identity assurance is not usable access. Proofing, authentication and
> federation can strengthen institutional confidence while creating a separate
> inclusion and recovery problem involving documents, devices, biometrics,
> disability, language, privacy, fraud holds and account repair.

This is not an argument against identity assurance. It is a conversion finding:
net public value requires measuring legitimate completion and recovery alongside
fraud prevention.

## Cultural and geographical interpretation

Identity systems encode a theory of the “real person”: a person with the right
documents, stable address, compatible device, legible face or fingerprint,
reliable connectivity, private space and confidence navigating a digital
workflow. Migrants, unhoused people, older adults, people with disabilities,
people changing names, rural residents and people sharing devices may encounter
different proofing burdens without any change in the underlying legal entitlement
to the service.

The cultural meaning of a digital identity is therefore relational. It can feel
like protection from fraud, a passport to public capability, surveillance, a
test of belonging, or a silent denial. Geography enters through in-person
fallback locations, broadband, document offices, language support, device
repair and the distance to a human recovery route.

## Counterexamples and limits

- Strong identity controls can prevent fraud and protect benefits, tax data or
  health information; difficulty is not proof that the control is unjustified.
- A high transaction count may reflect successful repeat users rather than
  broad population access.
- Fraudulent accounts passing proofing does not show that legitimate users were
  excluded or that a different threshold would improve outcomes.
- An accessibility statement is a policy and feedback signal, not a measured
  completion or equity outcome.
- NIST guidelines are technical guidance; implementation, legal authority and
  service stakes vary by agency and application.

## Promotion decision

Promote the assurance-versus-usable-access distinction to Tier 1. Keep the
mechanism in Tier 2 until a named service links proofing method, legitimate
completion, false rejection/acceptance, accessibility, recovery time and the
person’s actual service outcome across place and subgroup.

## Next test

Create an identity-transaction ledger with proofing route, evidence burden,
device/accessibility mode, language, result, abandonment, fraud flag, appeal,
recovery time and completed service. Compare digital-only, remote-attended and
in-person fallback routes without treating fraud reduction alone as success.
