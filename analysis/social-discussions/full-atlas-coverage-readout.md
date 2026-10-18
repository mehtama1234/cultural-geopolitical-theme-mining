# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **93**
- Exact linked social items: **98**
- Record statuses: `{'augmented': 93, 'documented_access_gap': 307, 'queued': 1578}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 55 |
| `linkedin:documented_access_gap` | 345 |
| `linkedin:not_started` | 1,578 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 360 |
| `reddit:not_started` | 1,578 |
| `x:documented_access_gap` | 400 |
| `x:not_started` | 1,578 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 399 |
| `youtube:not_started` | 1,578 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
