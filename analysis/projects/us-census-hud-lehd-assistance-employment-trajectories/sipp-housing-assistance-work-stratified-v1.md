# SIPP assistance/work screen: tenure and resource counterexample v1

**Checked:** 2026-09-25  
**Status:** stratified selection audit; not causal  
**Parent result:** [monthly assistance and next-month work/security screen](sipp-housing-assistance-work-screen-v1.md)

## Why this audit matters

The pooled screen found next-month rent/mortgage difficulty of 9.15% among
monthly-assistance-exposed pairs and 4.17% among unexposed pairs. That pooled
contrast could simply reflect who receives assistance. This pass crosses the
month-t housing-tenure context with the month-t income-to-poverty band before
comparing the same next-month outcome.

The machine-readable compact result is
[sipp-housing-assistance-work-stratified-2024.json](data/sipp-housing-assistance-work-stratified-2024.json).

## Housing-difficulty result

| Month-t context | Exposed pairs | Exposed difficulty | Unexposed pairs | Unexposed difficulty |
|---|---:|---:|---:|---:|
| Renter, below 1× poverty | 2,042 | 8.89% (4.22–13.57) | 12,325 | **15.11% (11.82–18.41)** |
| Renter, 1–2× | 1,216 | 9.78% (3.80–15.76) | 16,131 | **12.40% (9.93–14.87)** |
| Renter, 2–4× | 490 | **11.01% (1.87–20.15)** | 23,478 | 8.09% (6.16–10.02) |
| Renter, 4×+ | 158 | **13.94% (0–38.34)** | 22,667 | 3.92% (2.65–5.18) |
| Owner/buyer, below 1× | 95 | 5.11% (0–11.88) | 12,773 | 6.47% (4.32–8.61) |
| Owner/buyer, 1–2× | 191 | **10.55% (0–23.18)** | 24,437 | 4.84% (3.44–6.25) |
| Owner/buyer, 2–4× | 116 | **10.00% (0–27.51)** | 57,647 | 2.61% (1.93–3.29) |
| Owner/buyer, 4×+ | 135 | 0.00% (0–0) | 115,331 | 1.28% (0.88–1.68) |

Intervals are approximate 95% Fay–BRR intervals. Exposed owner cells are small
and imprecise; the zero estimate in the highest-income owner cell is not proof
of no risk.

## Interpretation

The pooled contrast is composition-sensitive. It does not persist in one
direction across comparable contexts: among renters below 2× poverty, the
exposed cells have lower reported next-month difficulty than the unexposed
cells, while the direction reverses in higher renter resource bands. Owner
cells are too sparse on the exposed side for strong inference and have wide
intervals.

This is a useful counterexample to the tempting story that receiving other
assistance itself caused later housing difficulty. A more plausible set of
possibilities remains open: assistance may be targeted to pre-existing need;
it may protect the lowest-resource renters; it may be too small or mismatched
for higher-resource households with a different housing cost structure; or the
field may combine distinct clothing and housing assistance routes.

The audit therefore strengthens the research design, not the causal claim. It
requires program-specific exposure, amount/adequacy, alternatives, and
institutional response before the project can say what assistance changed.

## Boundary

`ETENURE` is an interview-period tenure context, not a monthly move or tenure
transition. `EOTHAS_MNYN` combines clothing or housing assistance and does not
identify HUD program, amount, adequacy, application, denial, or exit. The
outcome is reported inability to pay rent or mortgage, not arrears, eviction,
homelessness, or verified recovery. No trust or political-action endpoint is
observed.

## Sources and method

- [Parent weighted screen](sipp-housing-assistance-work-screen-v1.md)
- [Compact stratified result](data/sipp-housing-assistance-work-stratified-2024.json)
- [Analysis script](../../../scripts/analyze_sipp_housing_assistance_work_screen.py)
- [Census SIPP variable catalog](https://api.census.gov/data/2025/sipp/variables.html)
