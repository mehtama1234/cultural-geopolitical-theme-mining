# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **154**
- Exact linked social items: **159**
- Record statuses: `{'augmented': 154, 'documented_access_gap': 571, 'queued': 1253}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 116 |
| `linkedin:documented_access_gap` | 609 |
| `linkedin:not_started` | 1,253 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 685 |
| `reddit:not_started` | 1,253 |
| `x:documented_access_gap` | 725 |
| `x:not_started` | 1,253 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 724 |
| `youtube:not_started` | 1,253 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
