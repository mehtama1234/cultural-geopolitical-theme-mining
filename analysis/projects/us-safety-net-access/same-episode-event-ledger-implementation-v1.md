# Same-episode public-system ledger implementation v1

**Checked:** 2026-09-13  
**Scope:** multi-person, multi-place public-benefit episodes; not a household
case study  
**Status:** executable acquisition and analysis specification; no real episode
data claimed

## Why this is the next bridge

The SIPP layers now connect a SNAP transition, its recorded reason, and a
following material-hardship field. They still cannot observe the route that
produced the transition. This implementation specification turns the missing
middle into linked tables rather than another aggregate receipt statistic.

```text
need or rule exposure
  -> notice and route attempt
  -> effort, decision, delay, correction, or appeal
  -> amount, timing, interruption, or exit
  -> food/work/debt/health/housing result
  -> interpretation, trust, complaint, action, and agency response
```

Every table keeps its own source, date precision, universe, missingness, and
evidence status. A blank is not a zero and an administrative absence is not a
reported absence.

The shared event-ledger schema now makes these controls mandatory at the event
boundary as well: geography, date precision, denominator, method, missingness,
and an explicit counterexample must be recorded before a staged episode can be
used in a cross-source comparison. The [simulated fixture](../../samples/US-BROAD-EVENT-LEDGER-SIMULATED_V1.json)
tests the contract only; it is not evidence.

## Linked record architecture

Use pseudonymous `episode_id`; never put a name, address, case number, or full
date of birth in the research analysis table. Linkage keys are held separately
under the consent and legal-basis record.

### 1. Episode table: `episode`

| Field | Required meaning |
|---|---|
| `episode_id` | Pseudonymous episode identifier |
| `person_or_case_unit` | Adult, child, household, or administrative case; universe documented |
| `program`, `state`, `agency` | Program and administering context |
| `place_stratum` | Coarse place, urban/rural category, or office catchment |
| `episode_type` | New application, renewal, recertification, interruption, appeal, or exit |
| `need_onset_date`, `rule_exposure_date` | Exact, month-only, recalled, or unknown |
| `observation_start`, `observation_end` | Follow-up window and censoring status |
| `consent_linkage_status` | Permission, legal basis, linked sources, retention rule |

### 2. Route table: `route_attempt`

One episode may have many attempts; do not overwrite failed attempts with the
eventual successful channel.

| Field | Required meaning |
|---|---|
| `attempt_id`, `episode_id` | Stable link and attempt order |
| `attempt_date`, `date_precision` | When the contact occurred |
| `channel` | Office, phone, web, mail, text, community navigator, or other |
| `language`, `accommodation` | Language and disability/access accommodation requested or received |
| `notice_received`, `notice_understood` | Separate receipt from comprehension |
| `documents_requested`, `documents_submitted` | Requested and completed items, with unresolved item |
| `hours`, `travel_minutes`, `direct_cost`, `childcare_cost`, `missed_work` | Practical route burden with source and recall flag |
| `human_or_automated_step`, `failure_reason` | Route mechanism and observed failure |

### 3. Decision and benefit table: `decision_result`

| Field | Required meaning |
|---|---|
| `decision_id`, `episode_id` | Stable decision link |
| `decision_date`, `decision_status` | Pending, approved, reduced, denied, interrupted, restored, or exited |
| `stated_reason`, `reason_source` | Agency code, document, respondent report, or unknown |
| `appeal_offered`, `appeal_filed`, `correction_requested` | Separate procedural stages |
| `benefit_expected`, `benefit_received`, `available_date` | Expected versus actual amount and timing |
| `gap_days`, `interruption_days` | Security gap, with exact/reference-period status |
| `agency_correction`, `resolution_date` | Whether and when the institution changed the result |

### 4. Outcome table: `followup_outcome`

Record each outcome at baseline and at one, three, six, and twelve months when
available. Do not use participation or exit as a proxy for these fields.

| Domain | Minimum fields |
|---|---|
| Food | Food quantity/variety, skipped meals, food-security measure |
| Work | Hours, earnings, missed shift, commute, job change |
| Money | Debt, late payment, borrowing, savings, family/community help |
| Health/care | Delayed care, medication, stress, unpaid and paid care time |
| Housing/transport | Rent or mortgage, utility status, vehicle/transport, ability to remain housed |
| Recovery | Return, alternative aid, restored security, unresolved loss |

Each value carries `measurement_date`, `source`, `universe`, `missing_code`, and
`evidence_status` (`observed`, `reported`, `estimated`, `compared`, or `open`).
Each follow-up window also carries `protected_outcome` and
`sacrificed_outcome`: what remained secure or was avoided, and what was lost,
delayed, transferred, or put at risk. These fields may be unknown; they must
not be inferred from receipt, exit, or route burden alone.

### 5. Meaning and action table: `meaning_action`

Ask after the material result and preserve the exact question wording.

| Field | Required meaning |
|---|---|
| `perceived_change`, `attribution` | What changed and which actor is credited or blamed |
| `understandable`, `fair`, `respectful`, `arbitrary` | Separate process interpretations |
| `trust_program`, `trust_agency`, `trust_government` | Institution-specific trust |
| `complaint`, `appeal`, `official_contact`, `organizing`, `protest`, `turnout`, `vote`, `no_action` | Actions are separate binary/unknown fields |
| `information_source`, `prior_identity` | Information environment and pre-existing political/institutional identity |

Meaning is not inferred from a denial. A vote is not treated as proof of a
benefit experience.

## Sampling and comparison plan

The pilot should stratify episodes by state, urban/rural place, program, new
application versus renewal, channel, language/accommodation, and result. It
must preserve these comparison cells:

1. similar need, different route or language access;
2. similar eligibility, different notice or deadline;
3. approved without interruption versus delayed or denied;
4. exit with measured improvement versus exit without improvement;
5. eligible non-applicant versus applicant who received help; and
6. same place and period before versus after an office or rule change.

The analysis table must report episode counts, person counts where distinct,
weights, attrition, recall, missingness, date precision, and clustering. Do not
pool cells into one take-up or success score.

## Source-role contract

| Source | Can supply | Cannot supply alone |
|---|---|---|
| Administrative case record | Decision, amount, timing, interruption, correction | Comprehension, effort, alternatives, dignity, trust, unrecorded exits |
| Respondent interview/diary | Route burden, alternatives, meaning, action, unrecorded attempts | Complete administrative history without consent/linkage |
| SIPP | Population transition, reason, monthly resources, selected hardship | Notice, channel, benefit amount, appeal, same-episode meaning/action |
| Agency/office metadata | Channel availability, hours, closure/rule timing | Whether an individual could use or understand the route |
| Follow-up survey | Recovery, trust, action, unresolved loss | Administrative correctness unless linked and verified |

The present SIPP result is therefore a calibration layer, not a substitute for
this ledger. It identifies plausible transition strata and material outcomes
for the pilot while leaving the route fields genuinely open.

## Promotion and stop rules

Promote a public-system arrow only when the unit and time order are explicit,
the comparison or counterexample is retained, and the result distinguishes
administrative, respondent, and researcher evidence. Stop short of a causal
claim when the trigger, alternatives, route effort, remedy, or follow-up is
missing. Never convert a lower caseload, program exit, or recorded explanation
into improved security, trust, or political action.

## First deliverable after acquisition

Release a de-identified codebook, a missingness/date-precision table, and one
stage-by-stage report with these columns:

```text
stage | unit | date | source | denominator | result | uncertainty |
counterexample | evidence_status | remaining_gap
```

This makes the next result compatible with the broader 14-theme program and
prevents the public-system lane from becoming a single-household narrative.

Related: [same-episode event-ledger design](same-episode-event-ledger-design-v1.md),
[SIPP reason × following hardship](sipp-snap-transition-reason-outcome-fay-brr-layer-v1.md),
[safety-net event ledger template](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md),
and the [broad next-pass queue](../../US-BROAD-NEXT-PASS-QUEUE_V1.md).
