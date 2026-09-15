# IMF AI adoption and inequality extraction v1

**Checked:** 2026-09-13  
**Source:** [IMF Working Paper 2025/068: AI Adoption and Inequality](https://www.imf.org/en/publications/wp/issues/2025/04/04/ai-adoption-and-inequality-565729)  
**Full-text rendering:** [IMF eLibrary article](https://www.elibrary.imf.org/view/journals/001/2025/068/article-A001-en.xml)  
**Status:** extracted model outputs; not an observed post-adoption estimate

## Extracted outputs

The paper combines household microdata with a calibrated task-based model. In
the baseline AI scenario, the paper compares a 2014 starting distribution with
a modeled 2048 outcome:

| Model output | Reported change | Interpretation |
|---|---:|---|
| Wage Gini | -1.73 percentage points | Wage inequality falls in the baseline AI scenario because high-income task displacement can reduce high-end wages while productivity raises lower-income wages. |
| Wealth Gini | +7.18 percentage points | Wealth inequality rises because higher-income workers and capital owners receive larger capital-income gains. |
| Firm adoption choice | Stronger adoption when firms can choose | Cost savings from automating high-wage tasks increase modeled adoption, making the wealth effect particularly pronounced. |

The paper also emphasizes complementarity: high-income workers’ tasks can be
complementary with AI, which may raise their productivity rather than simply
displace them. Thus the wage-equalizing channel and the wealth-concentrating
channel can operate simultaneously.

## Method and limits

- These are calibrated model outputs, not realized 2048 outcomes.
- The horizon is a scenario comparison from 2014 to 2048, not a time-series
  estimate of actual US inequality.
- The result depends on task displacement, complementarity, capital returns,
  household microdata, and the assumed firm-adoption rule.
- The paper is an IMF working paper and states that it represents research in
  progress and the authors’ views.
- The model does not observe worker bargaining, ownership transfers, taxes,
  public policy, political action, household adaptation, or geopolitical
  response.

## Program implication

The useful finding is not “AI increases inequality” in the abstract. It is a
testable mechanism: the same adoption wave can reduce measured wage inequality
while increasing wealth inequality when capital returns and firm adoption
choices are included. The next empirical test is to compare this mechanism
with observed ownership, wages, firm size, training, and worker outcomes in
compatible US data.
