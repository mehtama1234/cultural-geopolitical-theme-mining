# Australian platform-deactivation case census v1

**Status:** bounded official-bulletin inventory; not a complete FWC database
export
**Checked:** 2026-09-15

## Purpose

The earlier Australian comparison deliberately used three mechanism cases. This
inventory expands the denominator without pretending that a bulletin search is
the same thing as a complete tribunal database. It records identifiable
platform-deactivation proceedings in Fair Work Commission published bulletins
and links them to primary decisions where the decision PDF is identified.

## Search frame and denominator

The frame is FWC Bulletin Volumes 6/25 through 12/25 and Volumes 1/26 through
6/26, supplemented by targeted FWC document-search queries checked on 15
September 2026, searched
for “unfair deactivation” and linked `UDE` matter numbers, with direct checks of
Commission decision PDFs. It captures decisions published from 5 June 2025
through the checked date; it is not a search of every FWC filing, unpublished
direction, order, or later decision after the checked date.

**Inventory denominator:** 15 identifiable proceedings or linked proceeding
surfaces. Hotak is counted once despite multiple Full Bench decisions. Bakar
is counted once despite the eligibility and revocation decisions. Bandameeda
is counted once despite preliminary and merits/order stages.

## Inventory

| ID | Proceeding | Matter / decision | Stage reached | Outcome coding | What remains open |
|---|---|---|---|---|---|
| AU-01 | Jibril v Rasier Pacific | UDE2025/31; [2025] FWC 1289 | Eligibility | `eligibility_dismissal` — recent continuous six-month period not established | Merits, process, and underlying deactivation evidence |
| AU-02 | Bakar v Rasier Pacific | UDE2025/59; [2025] FWC 1874; revocation [2025] FWC 2278 | Eligibility, then settlement/discontinuance | `revoked_after_settlement` — protection initially found, decision later revoked by consent | Settlement terms, merits, responsible operator, payment, restoration |
| AU-03 | Kumar v Portier Pacific | UDE2025/68; [2025] FWC 2275 | Merits | `dismissal_after_compliant_process` — rating threshold and review upheld | Rating correction, downstream impact, generalizability |
| AU-04 | Hotak v Rasier Pacific | UDE2025/53; [2025] FWCFB 151 and [2025] FWCFB 214 | Full Bench procedural and merits | `reactivation_plus_pay_open` — later reactivation did not extinguish jurisdiction; unfair deactivation; formal reactivation ordered | Lost-pay quantum/receipt, durability, negative-review correction |
| AU-05 | Bandameeda v Amazon Commercial Services | UDE2025/62; [2025] FWCFB 182; [2025] FWC 3842 | Preliminary jurisdiction, merits, remedy | `reactivation_plus_12126_31_lost_remuneration` | Payment receipt, continued access, recurrence prevention, anti-retaliation |
| AU-06 | Waheed v Rasier Pacific | UDE2025/160; [2025] FWC 2787 | Timing / case management | `within_time_case_proceeds` — 17 June 2025 date accepted; matter proceeded to case management | Merits, Code compliance, restoration, payment |
| AU-07 | Mansoor v Rasier Pacific | UDE2025/141; [2025] FWC 3111 | Merits and remedy | `reactivation_plus_6073_23_lost_pay` — allegations not proven; notice deficient; reactivation and $6,073.23 ordered | Payment receipt, continued access, recurrence prevention |
| AU-08 | Al Hussein v Rasier Pacific | UDE2025/134; [2025] FWC 3176 | Merits and remedy | `reactivation_plus_pay_open` — serious-misconduct theory not proven; Code non-compliance; reactivation ordered | Lost-pay quantum/receipt, continued access, process change |
| AU-09 | Warraich v Rasier Pacific | UDE2025/108; [2025] FWC 3338 | Merits and remedy | `reactivation_plus_pay_open` — vague warning, weak evidence, inadequate inquiry; reactivation ordered | Lost-pay quantum/receipt, continued access, process change |
| AU-10 | Abukar v Uber | UDE2026/33; [2026] FWC 388 | Eligibility | `eligibility_dismissal` — deactivation occurred before the statutory six-month protection period could be met | Merits, process, and underlying deactivation evidence |
| AU-11 | Khan v Portier Pacific | UDE2025/185; [2026] FWC 48 | Merits and remedy | `reactivation_plus_pay_open` — limited warnings, no valid reason established, reactivation ordered; parties directed to confer on lost pay | Lost-pay quantum/receipt, continued access, process change |
| AU-12 | Mohammed v Rasier Pacific | UDE2025/205; [2026] FWC 365 | Merits | `dismissal_after_compliant_process` — five complaints, valid reason established, Code compliance found, application dismissed | Later appeal, correction, and downstream effects |
| AU-13 | Abdalla v Rasier Pacific | UDE2025/152; [2026] FWC 217 | Merits | `dismissal_despite_code_noncompliance` — Code non-compliance found, but deactivation not unfair; application dismissed | Later appeal, correction, and downstream effects |
| AU-14 | Dar v Portier Pacific | UDE2025/231; [2026] FWC 76 | Merits | `rating_based_dismissal` — low-satisfaction-rating deactivation application dismissed | Rating correction, review quality, and downstream effects |
| AU-15 | Rehman v Portier Pacific | UDE2025/384; [2026] FWC 953 | Merits and remedy | `reactivation_plus_pay_open` — background-check deactivation; later voluntary reactivation did not eliminate formal remedy analysis; parties directed to confer on lost pay | Lost-pay quantum/receipt, continued access, process change |

Bandameeda's `UDE2025/62` matter number is now confirmed by the primary
decision and the Commission's bulletin index. The remaining Bandameeda gap is
implementation evidence: the public order establishes the amount ordered, not
receipt of payment or durable restoration.

## Stage distribution

The fifteen-row inventory is not a remedy rate because the stages are mixed:

```text
15 identified proceeding surfaces
  ├─ 3 eligibility / threshold endpoints (Jibril, Bakar, Abukar)
  ├─ 1 timing / case-management endpoint (Waheed)
  ├─ 4 merits dismissals (Kumar, Mohammed, Abdalla, Dar)
  ├─ 1 Full Bench + merits restoration (Hotak)
  └─ 6 merits restoration matters (Bandameeda, Mansoor, Al Hussein, Warraich, Khan, Rehman)
```

This is descriptive of the search frame, not representative of all workers or
applications. It must not be reduced to a single “success percentage.”

## What the expanded frame changes

### Restoration is no longer a one-case curiosity

The frame contains seven merits-level reactivation outcomes, with two public
lost-pay amounts ($12,126.31 in Bandameeda and $6,073.23 in Mansoor) and three
matters where lost pay remained to be determined (Hotak, Al Hussein, Warraich,
Khan, Rehman).
This strengthens the claim that the Code can produce restoration while leaving
implementation and durability unverified.

### Complaint evidence is a recurring bottleneck

Mansoor, Al Hussein, and Warraich all involve serious allegations where the
Commission tested the platform's evidentiary basis instead of accepting a
platform belief as sufficient. Warraich adds the clearest warning that a
“human review” label does not establish meaningful inquiry.

### Eligibility and timing are substantive remedy gates

Jibril shows the six-month continuity requirement can end a case before merits.
Bakar shows that settlement and respondent identity can erase a public merits
path. Waheed shows that the date a worker reasonably became aware of
deactivation can determine whether a case proceeds.

### Voluntary restoration does not erase the governance event

Hotak rejected the argument that later platform reactivation automatically
removes jurisdiction, because that could incentivize tactical reinstatement and
leave lost income unexamined. Temporary suspension and later restoration are
therefore measurable events, not invisible non-cases.

## Data-quality flags

- This is a published-bulletin inventory, not a filing-level export.
- Subsequent orders for Hotak, Al Hussein, and Warraich should be searched for
  lost-pay quantum and payment evidence.
- “Reactivation ordered” does not establish actual access, earnings recovery,
  rating correction, or protection from retaliation.
- Deduplication is by matter number where known, not by PDF count.

## Primary-source index

- [FWC Bulletin Volume 6/25 — Jibril](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-05-31.htm)
- [FWC Bulletin Volume 8/25 — Bakar and related decisions](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-07-31.htm)
- [Kumar primary decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc2275.pdf)
- [Hotak primary Full Bench decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwcfb214.pdf)
- [FWC Bulletin Volume 10/25 — Hotak](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-09-30.htm)
- [FWC Bulletin Volume 11/25 — Mansoor and Al Hussein](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-10-31.htm)
- [Mansoor primary decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc3111.pdf)
- [Al Hussein primary decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc3176.pdf)
- [Warraich primary decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc3338.pdf)
- [FWC Bulletin Volume 12/25 — Warraich](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-11-30.htm)
- [FWC Bulletin Volume 1/26 — Bandameeda](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2025-12-31.htm)
- [Bandameeda primary decision and matter number](https://www.fwc.gov.au/documents/decisionssigned/pdf/2025fwc3842.pdf)
- [Abukar primary decision](https://dms-uat.fwc.gov.au/document-view/secure/676878/1772511716.ba92095d941121dc)
- [FWC Bulletin Volume 2/26 — Khan](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2026-01-31.htm)
- [Khan primary decision](https://www.fwc.gov.au/documents/decisionssigned/pdf/2026fwc48.pdf)
- [FWC Bulletin Volume 4/26 — lost-remuneration methodology](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2026-03-31.htm)
- [Mohammed primary decision](https://dms-uat.fwc.gov.au/document-view/secure/676700/1772927855.83da23e091d5ce1e)
- [Abdalla primary decision](https://dms-uat.fwc.gov.au/document-view/secure/802656/1772527699.6ab66611174cf299)
- [Dar primary decision](https://dms-uat.fwc.gov.au/document-view/secure/798388/1772927855.7fccdf0f6effe472)
- [FWC Bulletin Volume 4/26 — Rehman](https://www.fwc.gov.au/documents/bulletin/bulletin-ending-2026-03-31.htm)

## Next decisive acquisition

Recover Bandameeda's matter number and search the FWC document system for
every linked order in these fifteen matters. Then add a second country inventory
using the same fields and compare Australia with Malaysia, where the evidence
reaches a Tribunal hearing, and Cambodia, where it reaches worker-reported
complaint use but not an adjudicated outcome.

## Boundary

This is a bounded source inventory, not a prevalence estimate, legal database,
or claim about the total number of Australian platform workers seeking redress.
Its value is denominator discipline: it makes the search frame, stage-mixing,
exclusions, and missing links explicit before comparative interpretation.
