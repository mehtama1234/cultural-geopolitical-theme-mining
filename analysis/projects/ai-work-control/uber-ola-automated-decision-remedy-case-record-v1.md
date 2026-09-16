# Uber/Ola automated-decision remedy case record v1

**Status:** official pre-Directive court outcome; information remedy observed; correction and compensation not observed

**Checked:** 2026-09-15

## Why this record matters

This is the first case in the current packet that connects a concrete
platform-worker decision to a court-ordered information remedy. The Amsterdam
Court of Appeal held that Uber and Ola had to provide London drivers with more
information about important decisions made through their driver applications.
The decisions included account deactivation for suspected fraud, trip
allocation, fare determination, and internal scores such as a
`fraud-probability` score.

The case therefore tests the missing middle between algorithmic management and
worker remedy. It does not establish that the drivers received corrected
accounts, compensation, or protection from retaliation.

## Official record

- [Amsterdam Court of Appeal official case summary](https://www.rechtspraak.nl/organisatie-en-contact/organisatie/gerechtshoven/gerechtshof-amsterdam/nieuws/2023/04/uber-en-ola-cabs-moeten-londense-taxichauffeurs-beter-informeren-over-automatische-besluiten)
- [ECLI:NL:GHAMS:2023:793](https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:GHAMS:2023:793)
- [ECLI:NL:GHAMS:2023:796](https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:GHAMS:2023:796)
- [ECLI:NL:GHAMS:2023:804](https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:GHAMS:2023:804)

The official summary is dated 4 April 2023. It identifies the claimants as
London drivers supported by the App Drivers & Couriers Union and states that
the drivers were not heard before account-removal decisions were made.

## Evidence matrix

| Stage | What the official record supports | Boundary |
|---|---|---|
| System function | Uber/Ola applications generated or supported decisions about deactivation, trip allocation, fares, and internal scores | The summary does not provide a reproducible technical specification of each model |
| Exposure | London taxi drivers using the Uber Driver or Ola Driver applications | This is a litigated group, not a representative worker sample |
| Adverse decision | Account removal for suspected fraud; decisions affecting income and potentially taxi-licence consequences | The case does not establish that every decision was made in the same way |
| Automation finding | The Court of Appeal described the challenged decisions as fully automated and without human intervention | This is the court's finding for the decisions before it, not a universal claim about all platform decisions |
| Information remedy | Uber and Ola were required to explain the factors used and provide information needed to understand the reasons | An information order is not itself account restoration, correction, compensation, or reinstatement |
| Worker-rights bridge | The information was intended to allow drivers to exercise GDPR rights, including rectification | The public summary does not show a subsequent successful rectification request |
| Institutional limit | Platforms' trade-secret arguments did not justify a complete refusal of information | The court did not require disclosure of an entire algorithm |
| Timing | Pre-Directive national court outcome, decided in 2023 | It cannot be treated as evidence that the 2024 EU Platform Work Directive had been transposed or applied |

## Remedy coding

| Remedy field | Code | Reason |
|---|---|---|
| Concrete automated decision | `observed` | Deactivation, allocation, fare, and score decisions are identified |
| Explanation of relevant factors | `observed` | Court-ordered information about factors and reasons |
| Human review of decision | `not_observed` | The record concerns information and GDPR rights, not a later human merits review |
| Correction/rectification completed | `not_observed` | Rectification was enabled as a right; a completed correction is not shown |
| Account reinstatement | `not_observed` | No reinstatement outcome is reported in the official summary |
| Compensation | `not_observed` | No compensation outcome is reported |
| Anti-retaliation protection | `not_observed` | No such outcome is reported |
| Trade-secret boundary | `observed` | Full algorithm disclosure was not required, but complete refusal was rejected |

## What happened after the decision?

The public case record does not show a completed correction outcome. In the
underlying Uber proceedings, drivers asked Uber to reverse the deactivations
and allow them to resume work; Uber stated that it would not reverse the
decisions. The appellate ruling then addressed access to personal data and
information about automated decision-making. Its remedy was disclosure, not an
order restoring the accounts.

The current acquisition pass searched the three appellate ECLI records, the
Amsterdam Court of Appeal's official summary, and the linked lower-court Uber
proceeding for a later rectification, reinstatement, compensation, or
anti-retaliation outcome. No such official follow-on outcome was located. This
is a bounded non-observation, not evidence that no later request or settlement
exists.

| Follow-on question | Current status |
|---|---|
| Did Uber/Ola provide the ordered information? | The public appellate record establishes the order; delivery details are not coded here |
| Did a driver obtain rectification? | Not located in the official records searched |
| Was an account restored? | Not located in the official records searched |
| Was compensation awarded? | Not located in the official records searched |
| Was retaliation or adverse treatment addressed? | Not located in the official records searched |

## Interpretation

The case supports a narrower and more useful proposition than “workers won
algorithmic transparency.” A court recognized that platform decisions could
materially affect income and licensing consequences, and it converted that
recognition into an information order specific enough to identify decision
factors. That creates an evidentiary route toward rectification.

The case does not show the final worker outcome. The chain currently reads:

```text
automated platform decision
  -> material effect on income/licensing position
  -> court-ordered information about factors and reasons
  -> ability to exercise rectification rights [supported]
  -> successful correction, restoration, compensation, or anti-retaliation [not observed]
```

This is a stronger remedy record than the Deliveroo and Wolt status cases,
because the requested relief concerns the decision process itself. It remains
pre-Directive and should not be used to infer that the later EU safeguards are
already effective in national practice.

## Decisive follow-up

Locate the post-order implementation record: the information supplied by Uber
or Ola, any driver request for rectification or review, and any later ruling on
whether the information was sufficient. Separately search for a
post-2 December 2026 national case to test whether the Directive changes the
remedy from information access into human review, correction, compensation, or
protection from adverse treatment.

## Boundary

This is a source-grounded case record, not legal advice. It records the
official court summary and linked decisions; it does not infer technical model
architecture, population prevalence, or successful worker correction beyond
what the public record states.
