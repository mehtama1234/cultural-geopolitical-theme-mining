# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **27**
- Exact linked social items: **30**
- Record statuses: `{'augmented': 27, 'documented_access_gap': 6, 'in_review': 17, 'queued': 1928}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 3 |
| `linkedin:documented_access_gap` | 30 |
| `linkedin:not_started` | 1,945 |
| `reddit:augmented` | 25 |
| `reddit:documented_access_gap` | 8 |
| `reddit:not_started` | 1,945 |
| `x:documented_access_gap` | 33 |
| `x:not_started` | 1,945 |
| `youtube:documented_access_gap` | 33 |
| `youtube:not_started` | 1,945 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
