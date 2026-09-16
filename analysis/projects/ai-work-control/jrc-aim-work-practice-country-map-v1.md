# JRC AIM-WORK: practice, outcome, and country map

**Status:** published-analysis extraction with bounded interpretation  
**Checked:** 2026-09-15  
**Unit:** employees in the 27 EU Member States; worker-level survey associations

## The useful question

“Algorithmic management” is too broad to be a useful exposure by itself. The
JRC AIM-WORK analysis separates the management function being automated from
the working condition being measured. That lets the atlas ask which kind of
control is associated with which kind of change, and whether the pattern travels
across countries.

## The exposure map

| Group | Practices in the analysis | What the practice does | Typical prevalence signal |
|---|---|---|---|
| Algorithmic direction | Automatic allocation of time/rosters (`amtime`), automatic task allocation (`amact`), automatic speed setting (`amspeed`), automated instructions (`amdir`) | Directs when, what, how fast, or by which instruction work is performed | Time and task allocation are the most widespread; speed and direct customer-rating allocation are much less common |
| Algorithmic evaluation | Automatic ranking (`perfrank`), points/prizes (`perfpoints`), customer-rating allocation (`ratingtasks`), performance-based cancellation (`perfcancel`) | Scores, compares, rewards, allocates, or withdraws work based on performance signals | Generally more concentrated and more occupation-specific |

The study treats all eight exposures as binary indicators: the worker reports
whether the practice is present in their routine. This is a measure of exposure,
not a vendor, software, employer, or implementation audit.

The [full Table 2 transcription](data/jrc-aim-work-table2-full-v1.json)
preserves the published estimates for all 16 outcomes. The earlier [core
transcription](data/jrc-aim-work-table2-core-v1.json) remains as a smaller
review surface. Both keep the paper's significance markers and model
description, while explicitly omitting standard errors and cell counts that
are not present in the table view.

## The outcome map

The analysis uses 16 working-condition indicators in four families:

1. autonomy, stress, and breaks: control over task order, methods, and speed;
   stress; and the ability to take breaks;
2. communication: contact with managers and peers;
3. working time: schedule control, night work, Saturday work, Sunday work, and
   days longer than ten hours; and
4. place of work: client premises, vehicle, outdoors, and home.

This matters because “job quality” is not one scalar outcome. A practice can
reduce discretion without increasing reported stress, or change working time
without changing formal schedule control.

## What the published analysis reports

### 1. Direct control is the sharpest distinction

The strongest and most consistent negative associations are reported for
practices that directly regulate speed or task execution. These practices are
associated with less autonomy over methods, task order, and speed, fewer
autonomous breaks, and—in the case of automated direction—higher stress. The
result is consistent with a mechanism of work intensification: the system can
reduce discretion and idle time without necessarily increasing the length of
the workday.

### 2. Evaluation is not one thing either

Automatic ranking is associated with lower autonomy and fewer breaks, while
points or prizes show a different pattern in the published estimates, including
some favorable associations with task-order autonomy and lower stress. A
ranking system that compares workers, a bonus system that rewards targets, and
a cancellation rule that threatens future work should therefore not be pooled
as a single “monitoring” treatment.

### 3. Common tools and intense tools differ

Time and task allocation are relatively widespread. Speed control, direct
instructions, and rating-based allocation are less common but more intensive
forms of intervention. The analysis reports an exploratory inverse relationship:
more widespread tools tend to have more moderate associations, while rarer,
more intrusive practices can show larger associations. This is a salience and
concentration result, not proof that rare tools cause harm.

### 4. Bundles can matter, but cumulative pressure is not always synergy

Workers exposed to multiple practices generally show stronger adverse
associations. The paper distinguishes a combined burden from a statistically
significant interaction: many joint negative outcomes can reflect separate
pressures accumulating, while only some pairs show evidence that one practice
amplifies another. The clearest interaction candidates include speed control
with direct instructions, speed control with cancellation, and speed control
with ranking.

### 5. The European average hides country patterns

The published country analysis reports the most consistent negative pattern in
several Eastern European countries, especially Czechia, Poland, Slovenia, and
Slovakia, with Estonia and Lithuania showing a less extensive pattern. Southern
European results are more isolated; several Continental and Scandinavian cases
are mixed. Austria is described as a positive outlier in autonomy, while
Denmark is described as a negative outlier. These are reported associations,
not proof that national institutions caused the differences.

The institutional interpretation is a hypothesis for the next pass: bargaining,
co-determination, regulation, labor-market support, sector composition, and
technology implementation may mediate the same digital practice differently.
The current survey does not identify which mechanism explains each country
contrast.

### 6. Exposure is also stratified by sector and occupation

The paper describes high-tech manufacturing as the highest-intensity industry
grouping, followed by low-knowledge-intensive services, knowledge-intensive
services, and low-tech manufacturing. Operators show the highest exposure
across nearly all practices; clerks and service workers show multiple
evaluation exposures; professionals and managers see less direct speed and
instruction control but continued performance monitoring; agricultural and
elementary occupations show the lowest overall exposure. These are qualitative
figure findings, preserved in the [Figure 1/6 machine record](data/jrc-aim-work-figure1-6-qualitative-v1.json),
not digitized prevalence estimates.

## The bounded chain

```text
management function automated
  -> worker exposure to direction or evaluation
  -> discretion, breaks, stress, communication, time, or place change
  -> possible work intensification or altered job quality
  -> institutional safeguards, bargaining, correction, or exit [open]
```

The first three arrows are supported by cross-sectional survey associations at
different strengths. The final arrow remains open. The dataset does not follow
the same worker through a workplace intervention, appeal, correction, pay
change, health consequence, or later trust judgment.

## What this changes in the atlas

The central theme is not “AI versus workers.” It is the conversion of
managerial judgment into different kinds of automated direction and evaluation,
with effects that depend on the function, bundle, occupation, country, and
institutional setting. This connects the work lane to the broader atlas themes
of time as a price, control and bargaining, infrastructure dependence, and
institutional legitimacy.

## Decisive next test

Acquire or reproduce the country and sector tables with their denominators,
weights, standard errors, and practice definitions. Then pair the worker-side
patterns with one institution-level record per setting: a collective agreement,
consultation rule, appeal mechanism, court decision, or enforcement record. The
test is whether the same practice-outcome relationship changes where workers
have documented voice, correction, or refusal rights.

## Sources and boundaries

- [Official JRC AIM-WORK analysis record](https://publications.jrc.ec.europa.eu/repository/handle/JRC147505)
- [Full Table 2 transcription](data/jrc-aim-work-table2-full-v1.json)
- [Figure 1/6 qualitative extraction](data/jrc-aim-work-figure1-6-qualitative-v1.json)
- [JRC AIM-WORK PDF acquisition audit](jrc-aim-work-pdf-acquisition-audit-v1.md)
- [Core Table 2 transcription](data/jrc-aim-work-table2-core-v1.json)
- [AIM-WORK methodology and source record](jrc-aim-work-source-record-v1.md)
- [Official JRC methodology PDF](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC143933/JRC143933_01.pdf)

The analysis is a weighted, cross-sectional worker survey. It is not a causal
experiment, a firm implementation audit, or evidence that AI alone—rather than
algorithmic management more broadly—produced a worker outcome.

The [source record's model audit](jrc-aim-work-source-record-v1.md#analysis-model-audit)
also preserves an internal estimator-label difference in the publication: the
methods section describes multinomial logit as primary, while the Table 2 note
labels its displayed estimates ordered logistic. This is a reproducibility
qualification, not a reason to merge the table with a different estimand.
