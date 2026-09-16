# Malaysia Gig Workers Act algorithmic-remedy record v1

**Status:** enacted and in force; formal remedy architecture observed; exercised outcomes open

**Checked:** 2026-09-15

## Why this record matters

Malaysia provides a non-European statutory comparator for the algorithmic-
management remedy problem. The Gig Workers Act 2025 (Act 872) is not merely a
policy proposal: the official Ministry of Human Resources states that
enforcement began on 31 March 2026. The Act creates rights to information about
automated monitoring and decision systems, a non-automated review mechanism,
written reasons for deactivation decisions, a right to be heard, and staged
dispute-resolution routes.

This is an important bridge between the EU Directive's prospective architecture
and Uganda's worker-reported practice. It establishes what a national system
has legally promised. It does not yet show that a worker used the mechanism,
that a platform complied, or that a Tribunal awarded a remedy.

## Official records

- [Malaysia Gig Workers Act 2025, Act 872](https://dosh.gov.my/wp-content/uploads/2026/04/Act-872-GIG-WORKERS-ACT-2025.pdf)
- [Ministry of Human Resources implementation notice, 31 March 2026](https://www.mohr.gov.my/pdf/2026/KSM.%20100-2-1-1%20JLD%205_72_31032026.pdf)
- [Ministry Act 872 information portal](https://www.mohr.gov.my/aktapekerjagig2025/jtksm.html)
- [Gig Workers (Conciliation Proceedings) Regulations 2026](https://www.mohr.gov.my/aktapekerjagig2025/assets/documents/PUA146_2026%20-%20PERATURAN%20PEKERJA%20GIG%20%28PROSIDING%20PENDAMAIAN%29.pdf)
- [Gig Workers (Tribunal) Regulations 2026](https://www.mohr.gov.my/aktapekerjagig2025/assets/documents/PUA144_2026%20-%20PERATURAN%20PEKERJA%20GIG%20%28TRIBUNAL%20PEKERJA%20GIG%29.pdf)

The Act received Royal Assent on 16 December 2025 and was gazetted on 31
December 2025. The Ministry's 31 March 2026 notice states that enforcement
began that day and describes the Act as covering more than 1.64 million gig
workers. The population figure is a government estimate, not an independently
audited count in this record.

## Control and remedy matrix

| Act feature | Legal provision / observed architecture | Outcome boundary |
|---|---|---|
| Automated monitoring transparency | Section 8(2)(a): workers must be informed of automated monitoring systems and their consequences | No platform disclosure or worker comprehension record acquired |
| Automated decision transparency | Section 8(2)(b): workers must be informed of automated decision systems affecting service assignment and working conditions | No platform-specific implementation record acquired |
| Non-automated review | Section 8(2)(c): platform providers must provide a non-automated review mechanism | Existence of a mechanism is not evidence of a completed review |
| Rights cannot be waived | Section 8(3): terms purporting to waive these rights are void | No enforcement or contract audit acquired |
| Deactivation grounds | Section 14(1): deactivation may be based on service-agreement terms or misconduct | The Act permits deactivation within a regulated process; it does not prohibit all deactivation |
| Inquiry period | Section 14(3): access may be modified or suspended for up to 14 days for inquiry | No case showing duration or platform compliance acquired |
| Interim payment | Section 14(5): where no grounds for deactivation are found, access must be reactivated and half average daily earnings paid for the modification/suspension period | No payment or reactivation record acquired |
| Right to be heard | Section 14(7): worker must be heard before termination or extended suspension under section 14(6) | No exercised hearing record acquired |
| Written explanation | Section 14(9): platform must give a written explanation for a decision under section 14(6) | No worker-level explanation acquired |
| Internal grievance | Section 17: written complaint route, generally resolved within 30 days; deactivation disputes are handled through the specific section 14 route | Route exists in law; use and resolution are open |
| Conciliation | Section 18 allows a worker dissatisfied with a platform decision under section 14(9), or with unresolved internal grievance, to lodge a complaint for conciliation | No conciliation file or settlement acquired |
| Tribunal | Part V establishes a Gig Workers Tribunal; parties may appear and be heard, and hearings are public | No Tribunal decision acquired |
| Worker representation | Section 10 protects joining, participating in, or establishing a gig-workers association | No association intervention in an algorithmic-decision case acquired |

## Remedy coding

| Remedy field | Code | Reason |
|---|---|---|
| National rule in force | `observed` | Ministry states Act 872 enforcement began 31 March 2026 |
| Automated-system disclosure duty | `observed_rule` | Section 8(2)(a)–(b) |
| Non-automated review duty | `observed_rule` | Section 8(2)(c) |
| Written decision explanation | `observed_rule` | Section 14(9) |
| Right to be heard before adverse outcome | `observed_rule` | Section 14(7) |
| Reactivation/payment consequence | `observed_rule` | Section 14(5) |
| Worker used the mechanism | `not_observed` | No case or administrative file acquired |
| Platform complied | `not_observed` | No platform implementation audit acquired |
| Correction or account restoration completed | `not_observed` | No worker-level outcome acquired |
| Compensation paid | `not_observed` | The statutory interim-payment rule is not evidence of payment in a case |
| Tribunal or conciliation outcome | `not_observed` | Regulations are present; adjudicated outcomes remain open |

## Interpretation

Malaysia changes the comparative sequence from “rights proposed” to “rights
legally in force,” while preserving the distinction between law and lived
remedy:

```text
Act in force
  -> disclosure of automated monitoring and decisions
  -> non-automated review and written explanation
  -> hearing / conciliation / Tribunal route
  -> reactivation, payment, correction, or other worker outcome [open]
```

The architecture is unusually close to the missing remedy chain identified in
the EU and Dutch records. The decisive next acquisition is therefore not
another summary of the Act. It is a Malaysian complaint, conciliation record,
Tribunal award, enforcement action, or platform-facing implementation document
that shows whether section 8 or section 14 was used.

## Implementation-stage check

The Ministry's public implementation materials now expose three relevant
institutional routes:

- an [e-Aduan portal for gig-worker complaints](https://eaduan-gig.mohr.gov.my/eaduan/login);
- a Ministry [Act 872 enforcement and downloads portal](https://www.mohr.gov.my/aktapekerjagig2025/download.html), including the conciliation and Tribunal regulations;
- a public [Act 872 information portal](https://www.mohr.gov.my/aktapekerjagig2025/infokit.html) linking dispute-resolution and Tribunal information.

These are observed implementation artifacts, not evidence that a worker has
obtained a remedy. The current public search found no case-level complaint
register, conciliation settlement, Tribunal award, or enforcement decision
identifying an automated-monitoring or automated-decision dispute. The next
acquisition should test whether those records are non-public, newly emerging,
or available through a formal information request.

The detailed search boundary is maintained in the [Malaysia Act 872 outcome
acquisition audit](malaysia-act872-outcome-acquisition-audit-2026-09-15.md).

## Worker-voice boundary

The Ministry's public Act portal reports **37 engagement sessions, 3,873
participants, and 485 feedback items** during the Act's development. This is
direct evidence that a policy-stage consultation process was reported by the
responsible ministry. It is not evidence that participants controlled the
automated-decision provisions, that gig-worker representatives were equally
represented, or that the resulting rules are now being used in individual
cases.

The distinction is important for the broader atlas:

```text
policy participation -> statutory design -> complaint/review use -> worker outcome
        observed             observed              infrastructure visible       open
```

The next worker-voice acquisition should obtain the consultation submissions,
the identity and composition of participants, and any documented changes made
to sections 8, 14, or the Tribunal design in response to feedback.

## Boundary

This is a legal and administrative source record, not a finding that Malaysian
platforms comply or that gig workers have already received effective remedies.
The Act's stated beneficiary count and the Ministry's implementation claims are
kept separate from observed worker outcomes.
