# Next acquisition decision for the household cascade v1

**Checked:** 2026-09-16  
**Decision:** do not download new microdata in the current pass  
**Preferred candidate:** registration-gated Understanding America Study (UAS)

## Why UAS is the next credible candidate

The local MEPS staging run proves that the observed event/payment/context side
can be populated, but it cannot supply the original care choice, exact
obligation, institutional remedy, or later trust/action. The existing [UAS
acquisition audit](../us-health-cost-household-choice/uas-health-cost-legitimacy-acquisition-audit-v1.md)
identifies the smallest candidate that could close several of those gaps in a
single respondent frame:

- the monthly panel can place a reported medical or dental expense shock before
  later health, work, financial, and meaning outcomes;
- UAS 537 can contribute bounded affordability, care access, disputed-bill,
  provider experience, and institution-specific trust items; and
- UAS 698 can contribute health-cost amount bands, outside help, care
  foregoing, alternatives, and satisfaction fields.

This is a candidate route, not current evidence. The repository contains no
local UAS microdata, and the public aggregate explorer does not expose the
medical-expense component needed for the focal transition.

## Storage invariant checked

On 2026-09-16 the project directory was approximately 152 KB and contained no
Stata (`.dta`) or archive (`.zip`) source files. The MEPS source files and the
18,457-row staged JSONL remain outside Git under `/tmp`; only scripts, compact
derived output, hashes, and writeups are tracked. This is the intended storage
boundary for the next acquisition as well.

## Storage-conscious gate

Proceed in this order:

1. **No-download inventory:** confirm registration/access and inspect the
   official codebook or questionnaire pages for exact field names, wave dates,
   recall windows, weights, and file sizes.
2. **Small documentation acquisition:** retain only the relevant codebooks and
   access metadata outside Git or in the smallest permitted artifact location.
3. **Overlap feasibility:** acquire or receive only the minimum files needed to
   test `uasid` overlap: monthly panel plus UAS 537/698. Run the existing
   inventory and merge audits before any analysis.
4. **Stop if fields fail:** do not retain a large file if the required medical
   cost, date, trust, or weight fields are absent, if respondent-wave keys are
   duplicated, or if usable overlap is too small.
5. **Bounded extraction:** if the gate passes, select only the needed columns,
   hash the source files, write compact derived outputs outside the repository,
   and commit scripts, audit metadata, and small aggregate records only.

The existing tools are [audit_uas_health_cost_legitimacy_files.py](../../../scripts/audit_uas_health_cost_legitimacy_files.py),
[audit_uas_health_cost_legitimacy_merge.py](../../../scripts/audit_uas_health_cost_legitimacy_merge.py),
and [analyze_uas_monthly_medical_expense_followup.py](../../../scripts/analyze_uas_monthly_medical_expense_followup.py).
Their regression guards pass via [test_uas_health_cost_legitimacy_guards.py](../../../scripts/test_uas_health_cost_legitimacy_guards.py).

## Required go/no-go evidence

Do not promote a UAS result into the household cascade until the audit can
show:

| Gate | Required evidence | Stop condition |
|---|---|---|
| Identity | Stable `uasid`; contemporaneous household key handled separately | Missing or duplicated respondent-wave keys |
| Timing | Medical-cost exposure precedes a later panel outcome | Same-wave ambiguity or only annual recall with no ordering |
| Choice | Care received, delayed, skipped, disputed, or alternative reason | Only aggregate cost or satisfaction fields |
| Room/obligation | Amount band, outside help, payment or affordability, and alternatives | Cost concern without an obligation or feasible alternative |
| Remedy/meaning | Provider/insurer experience, trust, satisfaction, complaint, or action | Trust/action only cross-sectionally or no route context |
| Design | Weight, missingness, module eligibility, attrition, and overlap | Unverifiable denominator or unusable weights |

## Current status and next action

Current status is **verified acquisition route**, not completed evidence. No new
bulk download is authorized by this design pass. The next safe action is a
user-initiated or already-authorized access step that supplies the relevant UAS
documentation or files; then run the three existing audits before selecting
columns or producing a finding. Until that happens, the MEPS, SIPP, SHED, CFPB,
and randomized debt-relief layers remain separate benchmarks rather than one
synthetic person-level chain.
