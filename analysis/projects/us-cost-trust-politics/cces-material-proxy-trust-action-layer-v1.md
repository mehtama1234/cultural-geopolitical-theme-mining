# CCES material/work proxies, trust, and civic action layer v1

**Checked:** 2026-09-13  
**Source:** 2024 Cooperative Election Study common post-election file  
**Unit:** post-election respondent  
**Weight:** `commonpostweight`  
**Status:** weighted descriptive association; not a causal material-pressure or turnout estimate

## Why this layer matters

The broader program needs a respondent-level bridge between material/work
conditions and cultural-political meaning. This CCES pass uses two available
proxies—not a generic “economic stress” score:

- `gigwork`: whether the respondent earned money through app-mediated work in
  the last year;
- `edloan`: whether the respondent is currently responsible for paying off a
  student loan.

It then compares reported federal trust, state trust, and any of six forms of
civic action during the prior year: attending a local political meeting,
displaying a political sign, campaign work, protest attendance, contacting an
official, or donating money.

```text
work/debt position
  -> institutional trust and civic action
  -> vote or political judgment
```

The first two stages are measured here. The file does not identify a dated
financial shock, employer, debt event, reason for gig work, or causal path.

## Verified calculation

- 60,000 CCES rows were streamed.
- 23,530 respondents had valid positive weights, valid gig-work and student-
  debt proxy values, and valid federal/state trust responses.
- Trust categories 1/2 were grouped as “a great deal or a fair amount”; code 3
  was “not very much.” Missing/NA/skip codes were excluded from the trust
  denominators.
- Civic action was calculated only where all six action items had valid yes/no
  responses; any yes counted as action.
- No design-based standard errors were calculated in this first pass.

## Weighted comparison

Percentages are within each joint proxy group. `n` is the unweighted base for
the trust/action denominator; the cells are not a causal or population-rate
ranking.

| Gig work | Student-loan responsibility | n | Federal trust: great deal/fair amount | State trust: great deal/fair amount | Any civic action |
|---|---|---:|---:|---:|---:|
| No | No | 17,954 | 47.5% | 67.1% | 35.1% |
| No | Yes | 2,853 | 40.1% | 62.9% | 39.9% |
| Yes | No | 2,058 | 46.8% | 62.0% | 38.1% |
| Yes | Yes | 665 | 54.7% | 62.5% | 46.4% |

The joint “gig work + student debt” cell has the highest observed civic-action
share in this descriptive screen, while the “student debt without gig work”
cell has lower federal and state trust than the no-debt/no-gig-work cell. The
pattern is not monotonic: gig work without student debt is close to the
no-gig/no-debt federal-trust level, and the joint cell has higher federal trust
than either single-proxy cell. This is a counterexample to treating material or
work position as a single automatic distrust pathway.

## What this adds to the broad program

1. **Material position can coexist with different meanings.** Debt and gig
   work do not map onto one uniform trust or action response.
2. **Trust and action are separate outcomes.** The highest civic-action cell is
   not the lowest-trust cell, so participation cannot be read as simple
   institutional confidence or withdrawal.
3. **The interaction matters.** A joint proxy can differ from either exposure
   considered alone, which supports measuring combinations of dependence,
   work control, debt, and alternatives.
4. **The cultural arrow needs attribution.** The survey does not say whether
   respondents interpret student debt or gig work as opportunity, necessity,
   exploitation, flexibility, or a policy failure.

## Arrow ledger

| Arrow | Status | Safe conclusion | Missing evidence |
|---|---|---|---|
| Gig work/student debt → trust | Descriptive association | Trust shares differ across joint proxy cells | Reason, timing, income, prior trust, party identity, and design-based uncertainty |
| Gig work/student debt → civic action | Descriptive association | Any-action shares differ and are not monotonic | Desired action, time/control, organizing route, and causal exposure |
| Trust → civic action | Not established | Both are measured separately | Sequence, motivation, efficacy, and repeated-wave change |
| Material/work position → vote | Not promoted | The vote item has a selective valid-response pattern in this extraction | Full universe/weight audit and a preregistered turnout analysis |
| Experience → blame, identity, dignity, or political demand | Open | The proxy fields do not measure attribution or meaning | Direct attribution, identity, fairness, and policy-demand questions |

## Limits

- Gig work and student-loan responsibility are proxies, not measures of income,
  debt burden, financial worry, job quality, or schedule control.
- The comparison is cross-sectional and post-election; it cannot establish
  order or causation.
- Party identity, age, education, race, income, geography, and prior trust may
  explain or condition the observed differences.
- `commonpostweight` is retained, but this pass does not calculate complex-
  design variance or calibrated uncertainty.
- Civic action is an any-action composite for a descriptive screen; the six
  actions should be separated in a fuller instrument.
- The vote field is not used in the headline result because its valid-response
  distribution changes sharply after the proxy/trust filters; a turnout claim
  requires a separate universe audit.

## Reproduction

```text
python3 scripts/analyze_cces_material_trust_action.py \
  --input /tmp/cces24-common.csv \
  --output /tmp/cces-material-trust-action.json
```

Related: [economic adaptation, perception, and public action](economic-adaptation-perception-action-layer-v1.md),
[ANES political judgment](anes-2024-political-judgment-layer-v1.md),
and the [political response measurement specification](political-response-measurement-spec-v1.md).
