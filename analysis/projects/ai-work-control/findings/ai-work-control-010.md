# Finding 010: The job of the system matters more than the AI label

**Status:** provisional  
**Last checked:** 2026-09-11  
**Project:** AI, work, and control

## Finding

“AI adoption” is too broad to predict what happens to workers. A system that recommends training, assigns shifts, sets work pace, monitors time, evaluates performance, or recommends discipline changes different parts of the work relationship. The worker outcome depends more on that job and its surrounding rules than on the label AI alone.

## What we directly know

- The JRC defines algorithmic management as computer-programmed procedures that coordinate labor, whether or not AI is used. Its functions include assigning shifts, giving instructions, assessing performance, and assigning rewards or penalties. [JRC algorithmic-management project](https://joint-research-centre.ec.europa.eu/scientific-activities/employment/algorithmic-management-and-digital-monitoring-work_en)
- The JRC’s 2026 AIM-WORK analysis reports that different practices have different relationships with working conditions. Direct algorithmic direction of tasks and pace shows the strongest association with lower discretion and greater work intensity, while some forms of platformisation show no significant effect. [JRC AIM-WORK analysis](https://publications.jrc.ec.europa.eu/repository/handle/JRC147505)
- An NBER randomized experiment found no significant average performance effect from digital surveillance, but unexplained changes in surveillance based on worker performance reduced output. [NBER Working Paper 33348](https://www.nber.org/papers/w33348)
- In a separate NBER field experiment, access to a generative-AI tool reduced email time and work outside regular hours without detectable changes in task quantity or composition. [NBER Working Paper 33795](https://www.nber.org/papers/w33795)
- The IBM Germany framework separates lower-risk information and training recommendations from higher-risk personnel recommendations and automatic decisions. [IBM framework source record](../german-ai-works-council-source-record-v1.md)

These sources use different populations and methods. Together they support classification of system functions, not a universal ranking of all AI tools.

## Causal chain under test

```text
system function -> type of decision or constraint -> worker discretion and information
-> pace, time, evaluation, or responsibility -> job quality and bargaining position
```

The system function is the first variable to record. “AI use” is only a starting label.

## Minimum classification

| System function | Immediate question | Main risk or possible gain |
|---|---|---|
| Assistance | Does the tool help a worker complete an existing task? | Time saved, learning, or deskilling. |
| Recommendation | Who sees the recommendation, and can the person reject it? | Better access or hidden ranking. |
| Allocation | Who assigns shifts, tasks, customers, or opportunities? | Better matching or less choice and opaque exclusion. |
| Direction | Who sets task order, method, or pace? | Coordination or work intensification. |
| Monitoring | What is observed, and can it be used for discipline? | Safety and feedback or surveillance and fear. |
| Evaluation | Who is scored, by what data, and with what appeal? | Clearer feedback or bias and status loss. |
| Personnel action | Can the system affect hiring, promotion, pay, or termination? | Administrative speed or high-stakes automated harm. |

Several functions can exist in one system. The project should code each one separately and record whether the same data can move from assistance into evaluation.

## Four-map reading

| Map | What changes when the function is named | Missing evidence |
|---|---|---|
| Material | Time, output, pace, pay, and job continuity can be measured separately. | Long-run pay, margins, workload, and health. |
| Social | The same worker may feel helped by assistance and watched by monitoring. | Within-worker evidence across functions. |
| Institution | Agreements and laws may cover some functions but not others. | Function-specific enforcement and coverage. |
| Power | Control can move through allocation, pace, scores, or access to data. | Ownership, exit, and bargaining by function. |

## Wider social and geopolitical meaning

The classification also matters beyond one workplace. A country may host the workers while another firm owns the model, data, cloud service, or platform rule. The state’s dependence is different when the imported system only assists a worker than when it allocates labor, evaluates people, or controls access to income. This is a research inference, not evidence that every software dependency becomes geopolitical leverage.

## Strongest challenge

Different functions are often bundled together, so separating them may make real systems look cleaner than they are. A tool can assist, monitor, and evaluate at once. The classification is useful only if the project records the links between functions and the data that travel across them.

## What would change our mind

- Evidence that the AI label predicts worker outcomes as well as or better than the system function.
- Evidence that assistance, monitoring, allocation, and evaluation have similar effects after rules, sector, and worker differences are controlled.
- Evidence that workers experience no meaningful difference between systems that help them choose and systems that choose for them.

## Next tests

1. Code every current source by system function, decision affected, data used, and appeal path.
2. Find studies that observe more than one function in the same workplace.
3. Compare the same function across unionized, unorganized, platform, public, and contractor settings.
4. Track when assistance data become performance or personnel data.
5. Map the firms and states that own the models, infrastructure, data, and labor rules.

## Sources

- [JRC algorithmic-management project](https://joint-research-centre.ec.europa.eu/scientific-activities/employment/algorithmic-management-and-digital-monitoring-work_en)
- [JRC AIM-WORK analysis](https://publications.jrc.ec.europa.eu/repository/handle/JRC147505)
- [NBER Working Paper 33348](https://www.nber.org/papers/w33348)
- [NBER Working Paper 33795](https://www.nber.org/papers/w33795)
- [IBM Germany framework source record](../german-ai-works-council-source-record-v1.md)
- [Claims ledger](../claims-ledger-v1.md)
