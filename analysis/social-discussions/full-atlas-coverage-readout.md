# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **97**
- Exact linked social items: **102**
- Record statuses: `{'augmented': 97, 'documented_access_gap': 328, 'queued': 1553}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 59 |
| `linkedin:documented_access_gap` | 366 |
| `linkedin:not_started` | 1,553 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 385 |
| `reddit:not_started` | 1,553 |
| `x:documented_access_gap` | 425 |
| `x:not_started` | 1,553 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 424 |
| `youtube:not_started` | 1,553 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
