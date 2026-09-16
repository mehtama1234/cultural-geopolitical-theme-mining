# JRC AIM-WORK PDF acquisition audit v1

**Checked:** 2026-09-15  
**Source:** [official JRC PDF](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC147505/JRC147505_01.pdf)  
**JRC reference:** JRC147505

## Acquisition result

The direct repository PDF was fetched successfully with HTTP status 200.

| Property | Recorded value |
|---|---|
| Filename | `JRC147505_01.pdf` |
| Size | 1,544,792 bytes |
| Page count | 41 |
| SHA-256 | `05d589fe10bc3615d648d7d4da9500cfaf228f3a4514c5c5354135b99f5dd4ba` |
| Text extraction | Successful with `pypdf` |
| Figure rendering | Successful with Ghostscript PNG rendering |

## Page map and extraction status

| PDF page | Content | Current atlas status |
|---:|---|---|
| 16 | Model description and controls | Audited in the source record; multinomial-logit/ordered-logit wording difference preserved |
| 19 | Table 2, first seven outcomes | Fully transcribed into the machine-readable Table 2 record |
| 20 | Table 2, working-time and place outcomes | Fully transcribed into the machine-readable Table 2 record |
| 21 | Table 2 note and interpretation | Significance markers and table-model label preserved |
| 26 | Figure 1: sector and occupation prevalence | Qualitative findings promoted; plotted labels are visible but not yet systematically digitized |
| 40 | Figure 6: country results | Qualitative country pattern promoted; heatmap cells have intensity classes, significance marks, and exclusions but no numeric cell labels |

## Reproduction boundary

The PDF is sufficient to reproduce the published Table 2 transcription and to
inspect the figure structure. It is not sufficient, without manual digitizing
or underlying data, to produce a complete numeric sector/occupation table or
numeric country-by-practice coefficient matrix. No values were inferred from
bar widths or heatmap colors. The existing [qualitative Figure 1/6 record](data/jrc-aim-work-figure1-6-qualitative-v1.json)
therefore remains the appropriate promotion level.

## Underlying-data route audit

| Route | Observed state | Promotion consequence |
|---|---|---|
| [JRC147505 publication metadata](https://publications.jrc.ec.europa.eu/repository/handle/JRC147505) | The accessible record describes the paper but lists no dataset, dataset collection, script, or supporting-file URL | No public replication package is promoted from the repository record |
| [JRC project-page dataset link](https://ec.europa.eu/eusurvey/runner/aim_work_data) | The link opens an EUSurvey “AIM Work Data” form with required fields; it does not directly return a data file in the accessible page | Treat as a request/access route, not as evidence that data were downloaded |
| Author-hosted full text | Public PDF copy is available, but no underlying microdata or code was identified in the accessible publication route | Publication claims remain source-grounded; numeric figure reconstruction is not silently inferred |

This is an access-state observation, not a claim that the underlying data do not
exist or cannot be obtained by an eligible researcher. A valid next step would
be a formal data request to the JRC/Ipsos research route, followed by a record
of eligibility, files received, terms of use, variable dictionary, and any
confidentiality or output-review restrictions.

## Next acquisition

Seek the underlying AIM-WORK dataset, replication files, or a supplementary
table with exact Figure 1 and Figure 6 values. If those are unavailable, a
versioned manual digitization may be created only with figure-resolution,
calibration points, rounding uncertainty, and a separate `digitized` evidence
class.
