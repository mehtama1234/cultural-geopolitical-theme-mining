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
| AG6 | The UK’s 2026 inclusion monitoring survey reports that 89% of certified providers use biometrics; only 49% of those hold demographic-group accuracy information, 49% offer a non-biometric route, 80% collect incomplete-journey data and only 19% of organizations collecting demographic data use it to monitor inclusion. | Current market-level inclusion and measurement gaps. | Named service completion, false rejection, recovery, subgroup outcomes, effectiveness of alternatives and non-digital access. |
| AG7 | The EU requires each Member State to issue a Digital Identity Wallet by the end of 2026; large-scale pilots covered payments, travel, education, social security, e-prescriptions and public services across more than 20 Member States and more than 300 organizations. | Cross-border rollout, use-case breadth and interoperability pathway. | Actual voluntary adoption, accessibility, device loss, revocation, service completion, exclusion, privacy experience or benefit to a named user. |
| AG8 | The EU’s 2026 remote-onboarding regulation specifies reference standards for binding personal-identification data to a wallet and device at substantial/high assurance levels. | Technical onboarding and assurance rule. | Whether remote onboarding works for people without compatible devices, documents, bandwidth, biometric fit or a safe recovery route. |
| AG9 | GOV.UK’s 2026 wallet sandbox accessibility statement records testing with zoom, keyboard, voice control and screen readers for creating, issuing, testing and revoking a digital driving licence. | Named accessibility test surface and lifecycle actions. | Production completion, assistive-technology coverage, authentication recovery, service outcome or user experience outside the sandbox. |
| AG10 | A 2026 EU policy pilot proposes using the Digital Identity Wallet to coordinate support for children in need while emphasizing non-discrimination, accessibility, data protection and non-stigmatising access. | High-stakes social-service use case and stated safeguards. | Whether children and families receive support faster, can refuse or correct records, avoid stigma, and retain a human/non-digital route. |

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

The 2026 UK evidence makes the measurement gap concrete: biometric deployment
is widespread, but less than half of biometric providers report demographic
accuracy information or an alternative route, and only a minority of
organizations collecting demographic data use it to monitor inclusion. A
published accessibility standard therefore cannot stand in for subgroup
completion. The EU wallet programme adds a geopolitical and cross-border layer:
common standards and pilots can create portability across services and states,
but they also make device binding, revocation, certification, relying-party
permissions and recovery shared infrastructure rather than a single agency’s
local problem.

The child-support use case raises the stakes further. A wallet can make an
entitlement portable and visible, yet the same record can stigmatize a child,
expose family circumstances or make a service conditional on a digital route.
The decisive evidence is not the wallet’s ability to present a credential; it
is whether a named child or family can obtain the service, understand what was
shared, correct the record, avoid harmful disclosure and reach a person when
the device, credential or relying party fails.

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
- A market survey can reveal measurement and design gaps without showing which
  provider or subgroup experienced harm.
- A cross-border pilot can demonstrate interoperability while leaving voluntary
  adoption, device loss, revocation, recovery and service completion unobserved.
- Testing a wallet sandbox with assistive technologies is not evidence of
  production accessibility across all devices, languages and service journeys.
- A portable child or social-service credential can reduce repeated proof while
  increasing stigma or data exposure if purpose, access and correction are weak.

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

For the 2026 refresh, add biometric demographic-accuracy evidence, alternative
routes, incomplete-journey reasons, wallet issuance/device binding, revocation,
cross-border relying-party permissions, assistive-technology mode, child/family
stigma risk and non-digital support. Follow one transaction to completed
service or human recovery.

## 2026 refresh sources

- [UK Inclusion monitoring report 2026](https://www.gov.uk/government/publications/inclusion-monitoring-report-2026)
- [European Digital Identity Wallet FAQ](https://digital-strategy.ec.europa.eu/en/faqs/qa-digital-identity)
- [EU Digital Identity Wallet toolbox and pilots](https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-toolbox)
- [EU 2026 remote-onboarding implementing regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R0798)
- [GOV.UK Wallet sandbox accessibility statement](https://www.gov.uk/guidance/accessibility-statement-for-the-govuk-wallet-sandbox)
- [EU children-in-need digital support pilot](https://data.consilium.europa.eu/doc/document/ST-9079-2026-INIT/en/pdf)
