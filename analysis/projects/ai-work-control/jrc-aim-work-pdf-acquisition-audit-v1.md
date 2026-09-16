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

## Next acquisition

Seek the underlying AIM-WORK dataset, replication files, or a supplementary
table with exact Figure 1 and Figure 6 values. If those are unavailable, a
versioned manual digitization may be created only with figure-resolution,
calibration points, rounding uncertainty, and a separate `digitized` evidence
class.
