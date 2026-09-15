# SIPP care constraints are measurable, but payment, assistance, and lost work are different stages

**Status:** official-universe Fay-BRR care/work finding · **Checked:** 2026-09-13

## The bounded finding

The SIPP care fields do not describe one single “child-care burden.” After
applying the official status flags and conditional universes, payment,
assistance, prevention of working or working more, and time lost from work
remain separate measures with separate denominators and precision.

The calculation uses 379,215 selected person-record/month rows from the 2025
SIPP public-use file (2024 reference year), of which 378,291 had a positive
final person weight. The replicate archive matched those rows by
`SSUID`, `PNUM`, `SPANEL`, `SWAVE`, and `MONTHCODE`.

## Estimates

| Measure | Estimate | Fay-BRR SE | Approx. 95% interval | Valid records |
|---|---:|---:|---:|---:|
| Paid for child care | 30.083% | 1.168 pp | 27.795–32.371% | 24,549 |
| Received child-care payment assistance | 6.379% | 0.698 pp | 5.010–7.748% | 24,549 |
| Child care prevented working or working more | 3.877% | 0.466 pp | 2.963–4.792% | 31,788 |
| Reported time lost from work due to child-care problems | 16.992% | 4.289 pp | 8.585–25.398% | 1,119 |

These are conditional weighted shares, not household prevalence. Payment and
assistance use the child-care-use universe; work prevention uses the reference
parent/child universe; time lost is conditional on reported work prevention.

## What this adds

The estimates make a useful distinction visible. A larger payment share does
not imply that payment assistance was available to everyone who paid, and a
work-prevention share cannot be read as the share of all parents who lost a
specific number of hours. The time-lost estimate is substantially less precise
because its valid universe is much smaller.

This is exactly the kind of denominator separation needed for the broader
material/time/care program. A care constraint may appear as money, foregone
work, or reported time loss, but the current SIPP layer does not observe the
same person’s full substitution path across those stages.

## End-to-end route under test

```text
care need or arrangement
  -> payment, assistance, schedule alternatives, or unpaid substitution
  -> work/time loss and household resources
  -> health, family routine, recovery, trust, or political action
```

This pass strengthens the measurement and uncertainty stages. It does not
identify the dated care trigger, provider route, employer flexibility,
schedule control, paid-versus-unpaid substitution, protected outcome, or later
meaning/action.

## Method and limits

The full estimate uses `WPFINWGT`. Each replicate uses `REPWGT1` through
`REPWGT240`, with Census’s Fay modified-BRR formula (`G=240`, perturbation
factor `0.5`). The analysis applies `APAY`, `APAYHELP`, `AWORKMORE`, and
`ATIMELOST` status flags and retains the dictionary’s conditional fields. The
raw files and generated calculation output remain outside the repository; the
structured record preserves the source hashes and denominators.

SIPP person weights do not create household weights. These measures are not a
causal child-care, employer, subsidy, or work effect and do not establish
health, trust, political, or cultural consequences. ATUS, SHED, PSID, MEPS,
RECS, administrative, and local-provider sources remain separate layers unless
a valid same-unit design is available.

## Next test

Add income, job, tenure, disability, and child-presence stratification with the
same official-universe and replicate-weight treatment, then define a
one-record-per-household rule before making household claims. The stronger
end-to-end result still requires a dated trigger, alternatives, substitution,
protected and sacrificed outcomes, and follow-up recovery or meaning.

**Evidence status:** reproducible design-based person-weighted descriptive
comparison; causal and complete same-unit societal arrows remain open.

## Sources

- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)
- [2025 SIPP data dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/2025_SIPP_Data_Dictionary.pdf)
- [SIPP replicate-weight dictionary](https://www2.census.gov/programs-surveys/sipp/tech-documentation/data-dictionaries/2025/rw2025_dictionary.txt)
- [Machine-readable result](../../../records/us-sipp-care-work-official-variance-2024.json)
