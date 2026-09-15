# MEPS 2024 care delay and household adaptation

**Checked:** 2026-09-15  
**Status:** weighted cross-round association; no causal claim  
**Machine record:** [care-delay/adaptation data](data/us-meps-2024-care-delay-adaptation.json)

## Result

MEPS 2024 contains cost-related care-delay measures in R4/2 and a separate
Economic Self-Administered Questionnaire (ESAQ) with payment strategy for a
$500 medical bill, spending and savings sacrifices, work/leave constraints,
and care provided instead of working. The analysis keeps those surfaces
separate but compares them within the same respondent architecture.

Payment-strategy categories are now reported both as raw valid counts and as
ESAQ-weighted shares. This matters because the strategy question has its own
valid universe and because a raw “could not pay” count is not a population
estimate.

For a hypothetical $500 medical bill, care delayers were more likely to report
using a provider payment plan (31.63% weighted) or being unable to pay at all
(21.70%) than non-delayers (20.70% and 7.86%). They were less likely to report
paying immediately with cash, check, or debit (12.74% versus 29.74%). These are
reported strategies under a hypothetical bill, not observed payment records;
they identify constrained alternatives rather than a realized household
transaction.

Among respondents reporting medical-care delay due to cost, 39.76% reported
medical debt, 29.89% missed a loan or credit payment, 23.72% were late or unable
to pay rent, and 38.09% had debt-collector contact in the companion financial
room extract. The ESAQ profile adds whether the household paid cash, used an
HSA/FSA, used credit, borrowed, used a provider plan, or could not pay, plus
the downstream sacrifices and work constraints associated with the same broad
year.

Among respondents reporting medical-care delay due to cost, sacrificed savings
was 23.41%, sacrificed basic spending 33.24%, worked when health needed time
off 37.38%, and could not afford the income loss from taking time off 19.89%.
Among respondents not reporting medical-care delay, the corresponding shares
were 8.57%, 9.84%, 12.99%, and 5.27%. These profiles make the money/time/work
trade-off visible without combining it into one burden score.

## Interpretation boundary

This is a stronger care-choice-to-adaptation bridge, but not a dated episode.
R4/2 care-delay reports and R5/3 ESAQ adaptation reports may concern different
needs. A respondent may have adapted before delaying care, delayed care before
adapting, or experienced both because of an unmeasured health or income shock.
The output therefore supports comparison and acquisition design, not a causal
mediation claim.

The same ESAQ profile now retains the denial/prior-authorization categories,
allowing institutional friction to be compared with payment strategy, spending
and savings sacrifice, work/leave constraints, and family-care substitution.
The denial field still has no claim identifier, decision date, appeal, or
resolution, so this is an institutional-friction association rather than a
remedy result.

Among respondents reporting an insurance denial or prior-authorization delay,
sacrificed savings was 24.50%, sacrificed basic spending 26.09%, and working
when health needed time off 31.23%. Among those reporting no denial or delay,
the corresponding shares were 7.63%, 9.51%, and 12.56%. This is an
institutional-friction-to-adaptation comparison; it does not show that the
denial produced the sacrifice or that an appeal would have reversed it.

```text
cost-related care delay
  -> payment strategy, sacrifice, work/leave, and family-care context
```

The next decisive join remains a dated need or bill, feasible alternative,
payment obligation, care decision, and follow-up outcome in one time-ordered
episode.

## Reproduction

```text
python3 scripts/analyze_meps_care_delay_adaptation.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --output analysis/projects/us-health-cost-household-choice/data/us-meps-2024-care-delay-adaptation.json
```

## Source and fields

The source is AHRQ’s [MEPS 2024 HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256). The analysis uses `DLAYCA42`, `AFRDCA42`, `DLAYPM42`, `AFRDPM42`, `EQPAYB53`, `EQSLEI53`, `EQSBIG53`, `EQSBAS53`, `EQSSAV53`, `EQSLIV53`, `EQWSIK53`, `EQLDEN53`, `EQLUPD53`, `EQLENH53`, `EQLJBSC53`, `EQLSIN53`, `EQCRNW53`, and `ESAQWT24F`.
