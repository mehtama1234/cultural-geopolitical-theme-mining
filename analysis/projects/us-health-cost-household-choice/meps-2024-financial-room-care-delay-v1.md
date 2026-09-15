# MEPS 2024 financial room and cost-related care delay

**Checked:** 2026-09-15  
**Status:** weighted same-round association; no causal claim  
**Machine record:** [financial-room/care-delay data](data/us-meps-2024-financial-room-care-delay.json)

## Result

The 2024 MEPS person file permits a direct same-respondent cross-tab between
confidence paying an unexpected expense, medical debt, and reported cost-related
delay or inability to afford medical care and prescriptions. This adds a
practical-room screen before the observed-event layer.

The correct interpretation is comparative, not causal. Financial room and care
access fields are collected in the same broad round but need not refer to the
same bill or need. The source does not identify whether a person delayed care
because of the reported financial condition, whether the delay preceded or
followed an observed event, or what alternative was available.

The combined confidence comparison shows a descriptive gradient: cost-related
medical-care delay was 14.15% among respondents not confident paying an
unexpected expense versus 5.36% among confident respondents. Prescription
delay was 8.39% and 2.41%, respectively. By medical-debt status, medical-care
delay was 16.98% with any medical debt versus 4.57% without debt. These are
same-respondent comparisons, not causal estimates.

## Reading rule

The machine record reports all four confidence categories and combined
“not-confident” versus “confident” groups, plus no-medical-debt versus any-
medical-debt groups. Preserve all categories because collapsing confidence into
a binary can conceal a nonlinear response. Medical debt is also a status, not
an event-specific balance or proof of current foregoing.

```text
financial room / medical debt
  -> cost-related care delay or affordability report
```

This is now a supported same-respondent association arrow. The missing links
remain dated need, quoted price, alternative, care completion, payment timing,
household substitution, institutional remedy, and later trust/action.

## Reproduction

```text
python3 scripts/analyze_meps_financial_room_care_delay.py \
  /tmp/cgtm-meps-2024/h256/h256.dta \
  --output analysis/projects/us-health-cost-household-choice/data/us-meps-2024-financial-room-care-delay.json
```

## Sources and boundary

The source is AHRQ’s [MEPS 2024 HC-256 full-year file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-256). The analysis uses `FWUNEXP42`, `MEDDEBT42`, `DLAYCA42`, `AFRDCA42`, `DLAYPM42`, `AFRDPM42`, and `PERWT24F`.

The result advances the practical-room-to-care-choice stage but does not
complete the health-cost end-to-end goal.
