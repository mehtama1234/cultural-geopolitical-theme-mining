# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **19**
- Exact linked social items: **22**
- Record statuses: `{'augmented': 19, 'documented_access_gap': 6, 'queued': 1953}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 2 |
| `linkedin:documented_access_gap` | 23 |
| `linkedin:not_started` | 1,953 |
| `reddit:augmented` | 18 |
| `reddit:documented_access_gap` | 7 |
| `reddit:not_started` | 1,953 |
| `x:documented_access_gap` | 25 |
| `x:not_started` | 1,953 |
| `youtube:documented_access_gap` | 25 |
| `youtube:not_started` | 1,953 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
