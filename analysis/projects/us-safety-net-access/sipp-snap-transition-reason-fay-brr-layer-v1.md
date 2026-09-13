# SIPP SNAP transition × recorded reason: Fay-BRR uncertainty layer v1

**Checked:** 2026-09-12  
**Source:** 2025 SIPP public-use file, 2024 reference year  
**Unit:** identified person, adjacent reference-month pair  
**Weight:** `WPFINWGT` from the first month of each pair  
**Variance:** Fay BRR with 240 replicate weights and perturbation factor 0.5

This is a population-level public-systems layer. It asks what reasons are
recorded around SNAP entry and exit, then estimates uncertainty around the
weighted category shares. It does not treat a recorded reason as a causal
explanation, and it does not reduce the broader program to SNAP or to one
household.

## Results

The transition run identified 437 no-to-yes pairs and 387 yes-to-no pairs.
Only 217 entry pairs (49.7%) and 188 exit pairs (48.6%) had a valid,
classified reason. The category denominators below therefore contain only
reason-classified transitions.

### No → yes: classified entry reasons

| Recorded reason | Pairs | Share | Fay-BRR SE | Approx. 95% CI |
|---|---:|---:|---:|---:|
| Job loss/layoff or wages reduced | 57 | 30.10% | 3.94 pp | 22.38–37.83% |
| Other | 43 | 23.33% | 3.43 pp | 16.62–30.05% |
| Loss or reduction of other income | 35 | 15.72% | 3.13 pp | 9.59–21.84% |
| Became disabled or otherwise unable to work | 22 | 10.67% | 2.56 pp | 5.66–15.69% |
| New child/dependent or pregnancy | 15 | 6.41% | 1.94 pp | 2.61–10.22% |
| No change—decided it was time | 14 | 6.01% | 1.89 pp | 2.31–9.71% |
| No change—heard about the program | 11 | 3.49% | 1.65 pp | 0.26–6.73% |
| Needed to recertify | 13 | 3.21% | 1.15 pp | 0.96–5.45% |
| Separation, divorce, or widowhood | 4 | 1.05% | 0.57 pp | 0.00–2.17% |

### Yes → no: classified exit reasons

| Recorded reason | Pairs | Share | Fay-BRR SE | Approx. 95% CI |
|---|---:|---:|---:|---:|
| Other | 88 | 49.53% | 4.34 pp | 41.02–58.04% |
| Ineligible because income increased | 56 | 32.40% | 4.26 pp | 24.04–40.75% |
| Time limit reached | 11 | 6.21% | 2.14 pp | 2.01–10.40% |
| Ineligible because of family changes | 11 | 3.67% | 1.69 pp | 0.35–6.98% |
| Requirements not met | 8 | 3.52% | 1.45 pp | 0.68–6.37% |
| Still eligible but could not/chose not to collect | 6 | 2.53% | 1.20 pp | 0.18–4.89% |
| Benefits not worth the trouble | 4 | 2.15% | 1.10 pp | 0.00–4.30% |

## What this means for the broader program

At the public-systems level, entry and exit are not single social signals.
Entry is often recorded alongside labor or income disruption, while exit is
often recorded alongside higher income—but nearly half of classified exits
are coded “other.” The result supports a broader societal question: how do
need, rules, administrative burden, work, family change, and public meaning
combine to shape participation and later political or consumer behavior?

The uncertainty intervals are wide enough that this is a directional layer,
not a fine ranking of reasons. The more important finding is the missingness:
about half of observed transitions cannot be assigned a recorded reason. A
proper end-to-end event record must therefore preserve the unknown category
and collect notice, application route, documents, effort, decision timing,
benefit amount, interruption, food/work/debt outcomes, and later trust or
political response.

## Limits and reproduction

- The reason field is a reported or recorded administrative category, not a
  causal estimate or proof of sole cause.
- The replicate-weight calculation estimates survey-design uncertainty for
  the classified shares; it does not repair reason nonresponse or identify
  unmeasured mechanisms.
- The adjacent-month design does not observe the complete application or
  notice episode and cannot distinguish every administrative, household, or
  labor-market pathway.
- Raw files, the derived slice, and JSON output are not committed.

Run:

```text
python3 scripts/analyze_sipp_snap_transition_reason_fay_brr.py \
  --primary /tmp/us-broad-sipp-2025/full-v13/sipp-household-slice.csv \
  --replicate-zip /tmp/us-broad-sipp-2025/rw2025_csv.zip \
  --output /tmp/us-broad-sipp-2025/full-v13/sipp-snap-transition-reasons-fay-brr.json
```

Related: [recorded reason layer](sipp-snap-transition-reason-layer-v1.md),
[transition uncertainty layer](sipp-snap-transition-fay-brr-layer-v1.md),
[transition context uncertainty layer](sipp-snap-transition-context-fay-brr-layer-v1.md),
[public administration layer](public-administration-takeup-security-trust-action-layer-v1.md),
and the [safety-net event ledger](../../templates/US-SAFETY-NET-EVENT-LEDGER_V1.md).
