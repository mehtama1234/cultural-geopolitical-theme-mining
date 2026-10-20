# Public-benefit episode acquisition gate

**Checked:** 2026-10-19  
**Status:** bounded acquisition audit; no public-benefit route yet qualifies from notice through receipt, correction, persistence, and later security

## Question

Can one person, household, or case be followed through a public-benefit episode
from notice or need, attempted access and effort, decision, actual receipt and
adequacy, correction or appeal, persistence, and later material or political
response?

The required chain is:

```text
need or rule change
  -> notice and route attempt
  -> decision and actual benefit receipt
  -> amount, timing, adequacy, interruption, or substitution
  -> correction, appeal, replacement, or reentry
  -> persistent household security, trust, action, or exit
```

## Candidate-route audit

| Candidate | What the repository has | Missing for qualification |
|---|---|---|
| WBNS SNAP recertification route | Recipient-side reports of interruption, late recertification, notice, time, paperwork, interview, and documentation barriers | Respondent-linked notice date, case decision, gap days, amount, correction/appeal, later receipt, adequacy, and household outcome |
| SIPP SNAP transitions | Same-person adjacent-month entry/exit, recorded reasons, following-month income-to-poverty movement, rent/mortgage and utility hardship | Administrative notice/effort, benefit amount/timing, causal decision sequence, appeal, correction, food quantity, persistence, trust, and action |
| SNAP EBT theft/replacement | GAO replacement-benefit scale, theft-control rules, recipient-protection machinery, and two partial administrative cases | One stolen-benefit case with a complete report-to-receipt clock, unusable-gap duration, food/bill consequence, recurrence, and later trust or exit |
| Disability workforce-program access | Participation, service use, post-exit employment and earnings differences by disability reporting | Accommodation request/receipt, service completion, placement mechanism, retention, hours/wages, and household security for the same participant |
| Housing-assistance verification | Eligibility, identity matching, secondary review, appeal, proration, and possible termination stages | Named household notice, payment or interruption, correction outcome, displacement/staying result, and later security |

## Result

The current public record is strong on program scale, administrative design,
recipient-reported friction, same-person transition context, and selected
post-exit outcomes. It does not join those stages into one privacy-protected
person or case. The safe finding is therefore a source-unit boundary: receipt,
participation, or a following-month hardship measure cannot by itself establish
benefit adequacy, administrative causation, correction, or durable security.

The bounded search did locate one qualifying **partial** case route: the [New
Jersey SNAP EBT replacement hearing finding](findings/us-new-jersey-snap-ebt-theft-hearing-denial-2025-001.md)
preserves a named petitioner, $400.34 in disputed transactions, a replacement
request, agency investigation and denial, an administrative hearing, and a
final affirmed disposition. It advances the route through formal review and a
negative remedy outcome. It does not expose later food or bill substitution,
benefit continuity, household adequacy, correction, trust, or action, so it
does not qualify the full episode.

A contrasting Connecticut decision supplies a positive but still partial remedy
route: the [Connecticut SNAP replacement finding](findings/us-connecticut-snap-ebt-replacement-partial-remedy-2023-001.md)
records a new card and $582.00 replacement credit before a hearing on a larger
residual claim. The hearing denied the additional claim after finding that the
covered loss was $590.16 and the remaining losses were not timely reported. The
record therefore closes the administrative route through an actual replacement
and residual appeal, but not through food access, bill substitution, adequacy,
or later household recovery. Together with the New Jersey case, it establishes
contrasting partial endpoints without qualifying the full episode.

A Washington DSHS replacement procedure adds a more concrete administrative
machinery route, but not a second case. The manual says staff verify the EBT
account and replacement category, forward completed claims to headquarters for
validation, issue an approved replacement within 14 days of the validation
notice, and document the result. It also specifies denial conditions and gives
worked examples, including a named hypothetical claimant whose $500 loss is
denied because the card was not in her possession, and a second hypothetical
claimant whose food and cash allotments are replaced after headquarters confirms
fraudulent use. These examples establish designed decision and timing machinery;
they do not establish an actual claimant's report date, issued credit, food
substitution, or later continuity. The source is therefore added as a procedural
control, not promoted to a qualifying episode: [Washington DSHS replacement
procedure](https://dshs.wa.gov/replacement).

SIPP is the closest lawful same-person route because it holds the person across
adjacent months and preserves uncertainty estimates. It still lacks the notice,
caseworker, amount, appeal, and remedy fields needed to interpret the transition
as an administrative episode. WBNS supplies lived route friction but is
retrospective and not case-linked. A qualifying next source must add the
missing administrative or case-level clock rather than another participation
aggregate.

## Smallest qualifying acquisition

Prioritize one consented, de-identified, or lawfully public episode containing:

1. person/case key, program, state, need or rule trigger, and notice date;
2. route channel, attempts, documents, interview, time/care/work effort, and
   decision authority;
3. expected and actually received amount, timing, duration, gap days, and
   adequacy or substitution;
4. correction, appeal, replacement, reentry, or non-resolution with dates; and
5. later food, housing, utility, health, work, household, trust, complaint,
   political-action, persistence, or exit outcome.

Keep administrative receipt, household outcome, and respondent interpretation
as separate fields even when they occur in the same episode. Retain null and
negative cases, including uninterrupted receipt, successful correction, and
continued hardship despite receipt.

## Stopping rule

Stop this public-benefit pass when one lawful source supplies the minimum fields
above or when the source owner confirms that the missing case join, benefit
amount, correction, or later outcome is not public. Record the exact missing
field and rotate to another thin-middle lane. Do not repeat program counts,
participation rates, processing scores, retrospective barrier percentages, or
same-person transition aggregates as if they close the episode.

## Source controls

- [Public-system route-to-security triangulation](public-system-route-to-security-triangulation-v1.md)
- [WBNS SNAP recertification interruption ledger](data/wbns-snap-recertification-interruption-event-ledger-v1.json)
- [SIPP SNAP transition material-security ledger](data/sipp-snap-transition-material-security-event-ledger-v1.json)
- [SNAP EBT benefit-theft control ledger](data/snap-ebt-benefit-theft-control-event-ledger-v1.json)
- [New Jersey SNAP EBT replacement hearing finding](findings/us-new-jersey-snap-ebt-theft-hearing-denial-2025-001.md)
- [Connecticut SNAP EBT replacement partial-remedy ledger](data/us-connecticut-snap-ebt-replacement-partial-remedy-event-ledger-v1.json)
- [Connecticut SNAP EBT replacement partial-remedy finding](findings/us-connecticut-snap-ebt-replacement-partial-remedy-2023-001.md)
- [Connecticut SNAP replacement partial-remedy finding](findings/us-connecticut-snap-ebt-replacement-partial-remedy-2023-001.md)
- [Accessible work and security synthesis](accessible-work-security-optionality-synthesis-v1.md)
- [Housing-status verification finding](findings/us-safety-net-access-024.md)
- [Same-episode event-ledger design](same-episode-event-ledger-design-v1.md)

**Evidence status:** public-benefit need, route friction, participation, and
following-month material context are established in separate units; same-case
receipt, adequacy, correction, persistence, and later security or action remain
unverified.
