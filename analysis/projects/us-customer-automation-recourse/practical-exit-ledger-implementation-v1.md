# Practical-exit episode ledger implementation v1

**Status:** reusable research-design contract; no new estimate  
**Checked:** 2026-09-16  
**Scope:** consumer, public-system, household, worker, housing, insurance,
and place episodes

## Why this contract is needed

The current atlas observes many transitions that are easy to mislabel as exit:
a SNAP case ends, an insurer sends a nonrenewal, a platform account is
reactivated, a complaint receives a response, a firm leaves a place, or a
household remains in its home. Those are different events. The episode ledger
must preserve the user's actual alternatives and the cost of leaving before it
can call an outcome **practical exit**.

```text
problem or exposure
  -> threatened resource and available alternatives
  -> attempted route and effort
  -> decision and verified remedy
  -> continued use, staying, switching, non-use, moving, refusal, or exit
  -> protected/sacrificed outcome and later trust/action
```

The [machine-readable contract](../../../manifests/practical-exit-observation-contract-v1.json)
defines fields and controlled values; it contains no observations.
The [validator](../../../scripts/validate_practical_exit_contract.py) is run
against the [simulated fixture](../../samples/PRACTICAL-EXIT-LEDGER-SIMULATED_V1.json)
to test the contract without presenting fictional data as evidence.

## Episode fields

Every row represents one de-identified episode, not one headline or one
institutional aggregate.

| Field | Required meaning |
|---|---|
| `episode_id` | Pseudonymous stable identifier; direct names, addresses, and account numbers excluded |
| `unit`, `domain` | Person/household/consumer/worker/case/property/firm/place and the relevant domain |
| `event_date`, `date_precision`, `geography` | Timing and coarse place with no false precision |
| `trigger`, `threatened_resource` | Problem, rule, loss, hazard, denial, price, or decision and what money/time/access/status/health/security was at risk |
| `alternatives` | Named possible routes and whether each was available, reachable, usable, affordable, and replaceable |
| `attempted_route`, `effort` | Channels, transfers, documents, waiting, travel, fees, missed work/care, and failed or unsubmitted attempts |
| `decision` | Denial, approval, interruption, restoration, nonrenewal, suspension, correction, dismissal, or other result with authority |
| `remedy_verification` | Ordered, offered, received, or independently verified correction, access, payment, replacement, repair, or no remedy |
| `followup_window` | Start/end, censoring, and observation source; only use windows supported by the source |
| `post_event_status` | `continued_use`, `stayed`, `switched`, `non_use`, `abandoned`, `moved`, `refused`, `institutional_exit`, `access_restored`, or `unknown` |
| `protected_outcome`, `sacrificed_outcome` | What remained secure and what was delayed, transferred, lost, or put at risk |
| `meaning_and_action` | Attribution, fairness, dignity, trust, complaint, appeal, organizing, vote, switching, withdrawal, or unknown |
| `counterexample` | Comparable episode with a different alternative, route, remedy, or outcome |

Unknown values are substantive results. A complaint with no documented
follow-up is not zero exit; a returned account with no alternative-work record
is not autonomy; a policy termination is not a household move.

## Minimum linked tables

### Alternatives

Record each candidate alternative separately:

```text
alternative_type | available | reachable | usable | cost_money | cost_time |
switching_cost | eligibility/access_constraint | source | evidence_status
```

Formal availability is insufficient. A provider can exist but be closed,
unaffordable, too far away, full, unsafe, incompatible with care, or unable to
transfer the relevant record or benefit.

### Route attempts

Never overwrite a failed attempt with the eventual successful channel. Preserve
attempt order, channel, language/accommodation, documents, transfers, waiting,
travel, direct cost, missed work/care, human or automated step, and failure
reason.

### Remedy and follow-up

Separate a decision from an offer, an order from receipt, restoration from
durability, and continued use from free choice. At follow-up, capture the
status, reason for returning/switching/staying/non-use, alternative actually
used, recurrence, and protected/sacrificed outcomes. Trust or political action
must retain exact wording, timing, and prior-identity context where available.

## Promotion rules

| Label | Minimum evidence |
|---|---|
| `institutional_exit` | A program, account, policy, platform, firm, or route changed state |
| `access_restored` | Named account, case, or service is documented as restored or reactivated |
| `continued_use` / `stayed` | Same unit is observed using the route or remaining in place in a defined window |
| `switched` | Same unit is observed moving to an identified alternative |
| `non_use` / `abandoned` | Same unit does not complete or stops using a route, with denominator and opportunity defined |
| `moved` | Same property/household or person-place unit is observed relocating |
| `practical_exit` | Same-unit post-event status plus documented alternative, relevant cost/constraint, and protected or sacrificed outcome |

Market exit, firm exit, insurer nonrenewal, lower caseload, complaint silence,
program exit, and account closure must not be promoted to `practical_exit`
without same-unit evidence and the alternative field.

## Comparison, privacy, and next use

The minimum comparison set is one episode with a constrained alternative and
one comparable episode with a usable alternative or timely remedy. Report
episode counts, distinct units, denominator, follow-up coverage, date
precision, missingness, censoring, and evidence status. Keep linkage keys in a
separate consent or lawful-basis-controlled system; the analysis file uses
pseudonymous IDs and coarse geography.

Do not combine a CFPB complaint, SHED fraud respondent, SNAP transition,
platform proceeding, insurance policy, and local establishment as one person.
They can populate different rows in a cross-domain observability matrix, not a
pooled exit probability.

Apply the contract first to one small existing case family—preferably a
platform-remedy proceeding or public-benefit interruption—using records already
available locally. If alternatives, remedy receipt, or follow-up are missing,
return `unknown` and publish the gap.

**Evidence status:** research-design specification; no new person-level data,
linkage, causal estimate, or exit rate is claimed.

## Contract check

```text
python3 scripts/validate_practical_exit_contract.py
```

The current check passes one simulated episode and confirms that the required
episode fields, alternative fields, status vocabulary, and test-only evidence
label are internally consistent.
