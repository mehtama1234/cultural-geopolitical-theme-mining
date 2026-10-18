# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **257**
- Exact linked social items: **262**
- Record statuses: `{'augmented': 257, 'documented_access_gap': 1143, 'queued': 578}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 219 |
| `linkedin:documented_access_gap` | 1,181 |
| `linkedin:not_started` | 578 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,360 |
| `reddit:not_started` | 578 |
| `x:documented_access_gap` | 1,400 |
| `x:not_started` | 578 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,399 |
| `youtube:not_started` | 578 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
