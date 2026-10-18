# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **276**
- Exact linked social items: **281**
- Record statuses: `{'augmented': 276, 'documented_access_gap': 1374, 'queued': 328}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 238 |
| `linkedin:documented_access_gap` | 1,412 |
| `linkedin:not_started` | 328 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,610 |
| `reddit:not_started` | 328 |
| `x:documented_access_gap` | 1,650 |
| `x:not_started` | 328 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,649 |
| `youtube:not_started` | 328 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
