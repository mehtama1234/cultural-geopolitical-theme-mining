# SHED care-foregoing paths and health/work context v1

## Question and boundary

Do 2024→2025 care-foregoing paths coincide with different 2025 self-rated
health and employment context for the same recontacted respondents?

This is a weighted descriptive panel transition. It does not identify whether
care foregoing caused health or work changes, whether an observed expense was
the trigger, or whether an outcome was protected or sacrificed by a specific
care decision.

## Results

| 2024 → 2025 care path | Paired respondents | 2025 fair/poor health | 2025 not working |
|---|---:|---:|---:|
| No → No | 2,976 | 12.06% | 36.32% |
| No → Yes (entry) | 327 | 22.28% | 30.04% |
| Yes → No (exit) | 444 | 19.53% | 32.56% |
| Yes → Yes (persistence) | 672 | 30.62% | 35.04% |

The persistent-foregoing group has the highest fair/poor-health share. The
entry group also has a higher fair/poor-health share than the no-to-no group,
while the exit group remains elevated. The work result is not a simple mirror:
the no-to-no group has the highest not-working share, and the entry group the
lowest. Employment status therefore cannot be treated as a universal burden
proxy; labor-force composition, disability, retirement, age, and health
selection remain important alternatives.

Together with the financial-path record, this makes the protected/sacrificed
outcome problem explicit: persistent or newly reported care foregoing aligns
with a different health surface, but the work surface does not move in the
same direction. The panel supports multidimensional outcome tracking, not a
single recovery score.

## Reproduction

```text
python3 scripts/analyze_shed_panel_care_foregoing_paths.py \
  --old /tmp/cgtm-shed/shed2024.zip \
  --new /tmp/cgtm-shed/shed2025.zip \
  --output analysis/projects/us-health-cost-household-choice/data/us-shed-panel-care-foregoing-paths-2024-2025.json
```

## Source

The panel files are maintained on the Federal Reserve [SHED data page](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
Variable definitions are documented in the [2025 SHED codebook](https://www.federalreserve.gov/consumerscommunities/files/SHED_2025codebook.pdf).
