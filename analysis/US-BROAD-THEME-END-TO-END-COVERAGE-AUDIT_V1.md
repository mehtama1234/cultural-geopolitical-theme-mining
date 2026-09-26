# US broad theme end-to-end coverage audit v1

**Checked:** 2026-09-24
**Status:** program-control audit; not a new trend estimate  
**Input:** [US broad theme coverage matrix](US-BROAD-THEME-COVERAGE-MATRIX_V1.md)

## What this audit establishes

The 14-theme matrix contains evidence anchors for every theme, but it does not
show a completed end-to-end causal chain for any theme. The current matrix has
14 `Compared` status tokens, 12 `Reported` tokens, 3 `Inferred` tokens, and 5
rows whose declared current status explicitly includes `Open`. Every theme
also carries a next-required-test description. The machine-readable audit
records the exact matrix hash and row-level parsing output.

This distinction is important: a theme can have many strong observations and
still lack the same-unit link from exposure to behavior, institutional response,
meaning, recovery, or wider consequence. The audit does not downgrade the
existing evidence; it prevents evidence density from being mistaken for
end-to-end completion.

## Theme-level coverage

| Theme | Current matrix status | Evidence anchors | Explicit open status |
|---|---|---:|---|
| Household room and consumption | Compared / Reported | 15 | No |
| Time as a hidden price | Reported / Compared | 10 | No |
| Consumer power and recourse | Compared / Reported / Open | 21 | Yes |
| Platforms, data, and attention | Reported / Compared / Inferred | 11 | No |
| Work, control, and bargaining | Compared / Reported | 18 | No |
| Care, health, and social reproduction | Reported / Compared | 15 | No |
| Housing, place, and mobility | Compared / Reported | 15 | No |
| Unequal exposure and status | Compared / Open | 15 | Yes |
| Trust, identity, and cultural meaning | Reported / Compared / Open | 17 | Yes |
| Public systems and policy feedback | Compared / Reported | 14 | No |
| Political judgment and collective action | Compared / Open | 14 | Yes |
| Firm, sector, and market power | Reported / Compared / Inferred | 16 | No |
| Infrastructure, technology, and dependency | Reported / Compared / Inferred | 9 | No |
| Geopolitical and state consequences | Reported / Compared / Open | 12 | Yes |

“Evidence anchors” counts the linked Markdown anchors in each matrix row. It
is a breadth indicator, not a quality score, sample size, or causal-strength
score. The status is copied from the matrix and may contain more than one
controlled status token.

## The broad completion picture

The audit makes five program-wide facts operational:

1. **Breadth is real.** All 14 themes have linked evidence anchors and a
   declared measurement level.
2. **Comparison is the dominant current mode.** Every theme contains a
   `Compared` status token, meaning the atlas is strongest at aligning source
   layers and counterexamples rather than claiming one pooled mechanism.
3. **Reported experience remains important but indirect.** Twelve themes
   contain a `Reported` status token; reported survey, agency, firm, or paper
   evidence does not necessarily identify the underlying event or response.
4. **Inference is concentrated in platform, firm, infrastructure, and market
   interpretation.** Three themes contain `Inferred` status tokens, so the
   mechanism must be stated as a hypothesis rather than a measured result.
5. **The open downstream chain is broader than the five explicit Open rows.**
   The next-test field in every row names an unresolved link. The recurring
   missing stages are dated exposure, alternatives, control, remedy or
   recovery, attribution, trust, political action, replaceability, and
   external response.

6. **Recovery has two clocks.** Across themes, formal response should be
   coded separately from lived status:

   ```text
   formal: offered / ordered / approved / reported delivered
   lived: received / usable / adequate / durable / trusted
   ```

   This applies equally to a consumer refund, public benefit, worker remedy,
   medical correction, infrastructure award, or strategic supply project. A
   formal endpoint is not an end-to-end endpoint unless the affected unit can
   use, sustain, or replace what was provided.

   The latest worker and product cases make the durability stage more
   concrete without closing it: Cartisano reports payment without practical
   return, Aitken reports return followed by later dismissal, and Sauna360
   reports a first repair later described as ineffective. These are observed
   durability or rupture signals at case/product level, not a durable-recovery
   rate; later livelihood, safe use, household security, trust, and exit still
   require unit-level follow-up.

   The retained same-case stage audit makes the bottleneck measurable: across
   34 local source surfaces, 30 show a dated event and 30 show an institutional
   or firm response, but only 8 show an observed alternative or non-use stage,
   3 show an observed individual remedy or defined outcome follow-up, 1 shows
   an observed meaning/trust/action stage, and none has a fully observed
   recovery/persistence/exit stage. These are stage-availability counts, not
   failure rates; they explain why another exposure or aggregate response
   count would add less end-to-end value than one lawful episode with a stable
   identifier and later follow-up.

## Priority order for the next broad passes

The matrix suggests a cross-theme order based on the smallest missing link,
not on the number of existing artifacts:

| Priority | Cross-theme gap | Why it matters |
|---|---|---|
| 1 | Same-unit material event → meaning/action | It is the common missing bridge across household room, care, public systems, trust, and politics |
| 2 | Same-case service or financial episode → remedy/exit | It tests whether visible institutional response restores practical options |
| 3 | Same workplace implementation → worker/household control | It distinguishes adoption or firm capacity from discretion, bargaining, and security |
| 4 | Same property/household risk event → repair/stay/move | It distinguishes payment, protection, hazard, and public backstop from secure staying |
| 5 | Realized domestic capability → replaceability/external response | It distinguishes contracts, infrastructure, and capacity from state or geopolitical leverage |

These are program priorities, not claims that one dataset should be forced to
answer every theme. A valid panel, event ledger, matched place design, or
administrative record can advance one arrow while the other themes remain
separate.

## Reproduction and interpretation rule

The audit is generated from the committed matrix and downloads nothing:

```bash
python3 scripts/audit_broad_theme_end_to_end_coverage.py \
  analysis/US-BROAD-THEME-COVERAGE-MATRIX_V1.md \
  --output-json analysis/US-BROAD-THEME-END-TO-END-COVERAGE-AUDIT_V1.json
```

The current input SHA-256 is
`b65d76bdd750ebe0fdcbbaa218e7e40b1789666b2bc17431568ee2c72e9e22fa`.
The row-level machine-readable output is [the coverage audit JSON](US-BROAD-THEME-END-TO-END-COVERAGE-AUDIT_V1.json).

This is a control artifact. It should be rerun whenever the theme matrix
changes, and its counts should never be used as a substitute for inspecting
the underlying source, denominator, uncertainty, counterexample, and open
arrow for a particular theme.
