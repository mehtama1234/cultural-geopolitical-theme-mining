# Prior authorization: from denial and appeal to care recovery

**Checked:** 2026-10-18  
**Status:** bounded care-access and remedy realization pass  
**Scope:** Medicare Advantage skilled-nursing authorization, denial, appeal,
reversal, admission, substitute care, recovery, caregiver burden, and plan exit

## What we found

The HHS Office of Inspector General reviewed skilled-nursing-facility
admission requests handled by 19 Medicare Advantage organizations in June 2024.
Plans denied 12% of requests. Enrollees or providers appealed 18% of those
denials, and plans overturned 95% of the appealed denials in favor of the
enrollee; denials issued by naviHealth were overturned 97% of the time.

This is a strong administrative signal: the initial access gate and later
review do not agree often enough to treat the denial stage as a simple measure
of medical necessity. But an appeal win is not the same as a timely admission,
and an authorization is not the same as rehabilitation or functional recovery.
The public review does not link a beneficiary to waiting days, interim care,
out-of-pocket cost, caregiver time, health, or later plan choice.

## What this connects to

| Existing finding | New connection | What does not transfer |
| --- | --- | --- |
| Plans denied 12% of reviewed SNF requests. | Prior authorization is an institutional gate that can create a care-delay and appeal route. | The 19-organization review is not a population-wide denial rate or causal health estimate. |
| Only 18% of denials were appealed. | Contestability is selective; the right to appeal is not equal to the capacity to use it. | Non-appeal does not prove acceptance, appropriate denial, or no need. |
| 95% of appealed denials were overturned. | Later review reveals a large mismatch between initial decisions and formal correction. | Reversal does not establish when care began, whether a facility had capacity, or whether recovery followed. |
| Public discussion frames denials as delay, appeal work, financial exposure, and trust loss. | Patient and provider accounts identify the household labor that aggregate administrative records omit. | A selected professional discussion is not a beneficiary outcome sample. |
| The health-cost atlas measures care foregoing, debt, and later health/work surfaces. | Authorization episodes can be connected to those household outcomes if the same case is retained. | Cross-source similarity is not a same-beneficiary longitudinal result. |

## The deeper question

When does an appeal reversal restore timely care, and when does it merely repair
the administrative record after the patient or family has already absorbed delay,
substitute care, cost, or lost recovery time?

## Why this matters

Health plans and regulators can report denial and reversal rates while patients
experience a hospital discharge deadline, a family member making calls, a
facility search, home care, or a worsening condition. A high reversal rate may
show contestability, initial-review failure, or both. The decision value lies in
knowing whether correction arrives before the protected care window closes.

Priority is **high** for decision value, missing-link value, connection value,
and disconfirmation value. Effort is medium and scope risk is high because
request, denial, appeal, reversal, admission, and outcome must remain in one
compatible beneficiary or request unit.

## What we know so far

- The HHS OIG review covers 19 Medicare Advantage organizations and SNF
  admission requests from June 2024.
- Twelve percent of requests were denied; 18% of denials were appealed; 95% of
  appealed denials were overturned in favor of the enrollee.
- The review gives no same-beneficiary admission date, time waiting, interim
  care, substitute provider, patient cost, caregiver burden, function, health,
  work, trust, or plan-switching endpoint.
- Appeals require recognition, documentation, persistence, and available
  patient/provider capacity; the 18% appeal share is therefore not a pure
  measure of medical disagreement.

## What could change the answer

The route would look contestable and protective if request-level records show
that reversals occurred before or soon after the needed admission, patients
entered appropriate facilities, interim care was safe, and later function or
caregiver burden improved.

It would look like delayed or unequal remedy if appeals were rare among people
with fewer resources, reversals came after the post-acute window, patients used
costly home or family care, or authorization did not translate into available
facility admission. A counterexample in which an unappealed denial reflected
appropriate alternative care would prevent overclaiming.

## Challenge checks

- Denial was not treated as wrongful denial or medical harm.
- Appeal was not treated as universal access to remedy.
- Reversal was not treated as admission, treatment, rehabilitation, or
  functional recovery.
- The selected 19-organization review was not generalized to all plans,
  services, or beneficiaries.
- Administrative aggregates and public discussion were not counted as a
  same-person panel.
- Patients, families, providers, facilities, plans, contractors, and discharge
  staff remain distinct actors with different burdens and control.

## Current answer

**Partly answered.** The evidence shows a substantial denial-to-reversal gap in
the reviewed SNF authorization route. It does not yet show whether the appeal
restored timely care or changed health, function, household cost, caregiver
time, trust, or plan choice.

## What to look for next

```text
illness, injury, or surgery
  -> SNF request, notice, documentation, and initial decision
  -> denial, appeal effort, and reversal date
  -> facility search, admission, interim/substitute care, and patient cost
  -> rehabilitation, function, caregiver time, work, and household room
  -> repeat authorization, complaint, trust, plan retention, or exit
```

Build a privacy-protected request-level ledger. Keep non-appealed cases,
appeal wins, appeal losses, and authorization-without-admission cases visible.
The first matching fields are request date, denial date, appeal date, reversal
date, admission date, facility capacity, substitute care, and later functional
outcome.

## Where this came from

- [HHS OIG Medicare Advantage SNF authorization review](https://www.oig.hhs.gov/reports/all/2026/medicare-advantage-organizations-overturned-nearly-all-appealed-prior-authorization-denials-for-skilled-nursing-facility-admission-raising-concerns-about-initial-denials/)
- [Existing bounded finding](findings/us-health-cost-household-choice-014.md)
- [Existing event ledger](data/medicare-advantage-snf-prior-authorization-event-ledger-v1.json)
- [Bounded public discussion of coverage denials](../../social-discussions/records/atlas-batch-0049-coverage-denials-linkedin-001.json)
- [Health-cost end-to-end project](README.md)

## Stopping rule

Stop this pass when one compatible request or beneficiary links denial,
appeal effort, reversal, admission timing, substitute care, patient cost,
functional or health outcome, caregiver burden, and later plan behavior, with a
credible appropriate-denial or no-delay counterexample. If the source stops at
reversal, retain the care-recovery gap instead of calling prior authorization
protective or harmful overall.
