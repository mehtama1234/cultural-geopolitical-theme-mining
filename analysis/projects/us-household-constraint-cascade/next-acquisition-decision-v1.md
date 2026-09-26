# Next acquisition decision for the household cascade v1

**Checked:** 2026-09-20
**Decision:** do not download new microdata in the current pass  
**Preferred candidate for the health-cost episode:** registration-gated
Understanding America Study (UAS)

**Program-level route rule — 2026-09-20:** PSID is the first authenticated
route for the broader atlas's material/time/care bridge. UAS remains the first
route only for the narrower dated health-cost episode because its monthly
event and billing modules fit that question more directly. These are
complementary acquisition tracks, not competing claims about which dataset is
generally better.

## Why UAS is the next credible candidate

The local MEPS staging run proves that the observed event/payment/context side
can be populated, but it cannot supply the original care choice, exact
obligation, institutional remedy, or later trust/action. The existing [UAS
acquisition audit](../us-health-cost-household-choice/uas-health-cost-legitimacy-acquisition-audit-v1.md)
identifies the smallest candidate that could close several of those gaps in a
single respondent frame:

- the monthly panel can place a reported medical or dental expense shock before
  later health, work, financial, and meaning outcomes;
- the Older Ages Monthly Events panel supplies a narrower but stronger
  event-first route for adults 50+, with 52 monthly waves, dated event blocks,
  medical expenditures, and later health, work, pain, and life-satisfaction
  measures;
- UAS 537 can contribute bounded affordability, care access, disputed-bill,
  provider experience, and institution-specific trust items; and
- UAS 698 can contribute health-cost amount bands, outside help, care
  foregoing, alternatives, and satisfaction fields.

This is a candidate route, not current evidence. The repository contains no
local UAS microdata, and the public aggregate explorer does not expose the
medical-expense component needed for the focal transition. If access is
obtained, the Older Ages panel should be acquired and audited first as the
smallest event-compatible file; the broader Monthly Panel and UAS 537/698
should follow only if that first gate passes.

## Documentation-only reconnaissance

The small documentation gate was exercised without acquiring raw
microdata. The historical temporary cache contained the September 1, 2026 UAS
monthly-panel codebook at
`/tmp/uas-monthly-panel-codebook-20260901.pdf` (521,561 bytes; SHA-256
`97af909996e341e99125ca8acd0a7258208a8b5afefeaf4df14ae4968c8af9f5`). It
confirms the useful monthly anchors `fin3s4` (significant medical/dental
expense shock), `fin1_when_month/day/year` (financial-change timing), and
later health, employment, pain, life-satisfaction, and meaning fields.

This satisfies documentation reconnaissance only. No local UAS respondent
file, `uasid` overlap, weight validation, module eligibility, remedy field, or
same-case estimate exists. The codebook therefore sharpens the next audit but
does not change the no-download decision.

**Current retention recheck (2026-09-19):** the temporary codebook path is no
longer present after the workspace crash. Its historical hash and documented
field notes remain in this decision record; no current local codebook or
respondent file should be claimed until it is restored or reacquired through an
authorized route.

## Storage invariant checked

On 2026-09-16 the project directory was approximately 152 KB and contained no
Stata (`.dta`) or archive (`.zip`) source files. The MEPS source files and the
18,457-row staged JSONL remain outside Git under `/tmp`; only scripts, compact
derived output, hashes, and writeups are tracked. This is the intended storage
boundary for the next acquisition as well.

## Storage-conscious gate

Proceed in this order:

1. **No-download inventory:** retain only the relevant official codebook or
   questionnaire pages and confirm exact field names, wave dates, recall
   windows, weights, and file sizes. This documentation step is now recorded
   above; the raw-file checks remain open.
2. **Small documentation acquisition:** if a newer codebook is needed, retain
   only the relevant documentation outside Git or in the smallest permitted
   artifact location.
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
The [minimum episode-field manifest](data/uas-minimum-episode-field-manifest-v1.json)
is the machine-readable version of the required fields and stop conditions.

## Decision after the 2026-09-17 public-metadata comparison

Within the health-cost episode, UAS remains the primary acquisition route. The
official UAS 537 metadata page
identifies one health-care module with utilization, billing, perceptions, and
satisfaction/access/health-status sections, reporting 1,233 selected cases and
1,136 completed surveys (92.13% response) in English and Spanish. This makes
the module a better first candidate for a same-respondent cost/access/
institutional-perception overlap test than another aggregate benchmark. The
page still requires login for data download, so these are route and denominator
facts, not respondent estimates.

HRS remains the age-50-plus fallback and replication route. Its public
documentation exposes cost-related delay, non-cost delay reasons, health-care
satisfaction, and trust in Medicare/Medicaid and insurers, but the trust block
has a separate eligible module sample and the health-cost measures have broad
recall windows. HRS should be used if UAS access fails or as an age-specific
counterexample after the UAS structural gate; it should not be pooled with UAS
or MEPS. The next operational action is still the smallest authenticated UAS
file/codebook acquisition, followed by key, overlap, weight, timing, and
missingness checks before any estimate.

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
| Recovery ladder | Formal response separated from received, usable, adequate, durable, and trusted lived status | A payment, approval, or satisfaction item is treated as restored household security |
| Design | Weight, missingness, module eligibility, attrition, and overlap | Unverifiable denominator or unusable weights |

## Current status and next action

Current status is **documentation-verified acquisition route with an explicit
authorization boundary**, not completed evidence. No new bulk download is
authorized by this design pass. The next safe action is a user-initiated or
already-authorized access step that supplies the relevant UAS respondent files
under terms that expressly permit the workflow; then run the three existing audits before
selecting columns or producing a finding. Until that happens, the MEPS, SIPP,
SHED, CFPB, and randomized debt-relief layers remain separate benchmarks
rather than one synthetic person-level chain.

## Official access recheck — 2026-09-20

The current UAS Monthly Surveys page still labels both the Monthly Panel Survey
Dataset and the Older Ages Monthly Event Panel Dataset as requiring
registration. The public page confirms that the Older Ages route contains 52
monthly event waves with prior-month life events, self-rated health, life
satisfaction, pain, hours worked, earnings, and medical expenditures. This
strengthens the route's documented fit, but does not change the access gate:
no respondent file, overlap, weights, or estimate is locally available.

The current Monthly Panel codebook adds a sharper structural gate. Its panel
rows are identified by stable `uasid` and `wave`, with `final_weight` and
survey-date metadata. It documents repeated health, pain, life-satisfaction,
stress, food-security, employment-shock, health-shock, and financial-shock
blocks; event timing fields include `empl_when_month/day/year`,
`le_hrs001_when_day/month/year`, and `fin1_when_day/month/year`. It also
documents later meaning/purpose scores and other wellbeing measures. Before
any estimate, the authorized file audit must verify unique `uasid`–`wave` keys,
wave coverage, weight validity, missing-value codes, and whether the event and
follow-up fields coexist for the same respondent and ordered waves. The
codebook confirms feasibility of the design; it is not respondent-level
evidence.

**Compliance boundary rechecked 2026-09-20:** the current UAS terms and
conditions restrict automated access, collection, copying, scraping, or
extraction and state that large language models may not manage, process, or
analyze distributed UAS data without express written authorization. This
workspace will not attempt to retrieve, transform, or analyze UAS respondent
files autonomously. A compliant future pass requires an authorized account
holder to obtain the smallest permitted file, confirm the applicable
permission, and provide the resulting audit artifacts; the gates above remain
unchanged.

The public UAS 537 routing page also documents the middle of the billing
episode: whether anyone reached the billing office (`hcb_reach`), who did so,
why no one reached it, time spent, respect/comfort, and the reported result
(`hcb_result`). UAS 698 documents outside help and amount (`N212`/`N215`),
foregone care (`N492`), and reasons including cost, appointment delay, work or
care responsibilities, scheduling, wait time, and transportation (`N493`).
These fields are promising because they can distinguish an obligation, an
attempted route, and an institutional response. They remain documentation-only
until an authorized file is acquired, linked, and audited for wave, overlap,
weights, missingness, and recall-window compatibility.

Source: [UAS Monthly Surveys and Older Ages data page](https://uasdata.usc.edu/index.php?pid=Monthly+Surveys&type=3), checked 2026-09-20.
The [current Monthly Panel description and codebook](https://uasdata.usc.edu/index.php?r=eNodzEEKwjAQQNGrDDlAwVwiXCLTlditIJQeYJoZtZjOhCZRinh3W3d_8fiENX4S7tFFuotrEtbHtcsQRl-x-TKJZsqjKdtbgxFvZuVK058fduj6UwcX0_wIC1xcSSVAV-aXLNBSpiQZWkl-HuO2AVKGs7EMZs8q8s013x-3cS3L) was checked the same day.
