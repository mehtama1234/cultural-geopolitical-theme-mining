# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **298**
- Exact linked social items: **303**
- Record statuses: `{'augmented': 298, 'documented_access_gap': 1502, 'queued': 178}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 260 |
| `linkedin:documented_access_gap` | 1,540 |
| `linkedin:not_started` | 178 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,760 |
| `reddit:not_started` | 178 |
| `x:documented_access_gap` | 1,800 |
| `x:not_started` | 178 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,799 |
| `youtube:not_started` | 178 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
