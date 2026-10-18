# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **209**
- Exact linked social items: **214**
- Record statuses: `{'augmented': 209, 'documented_access_gap': 816, 'queued': 953}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 171 |
| `linkedin:documented_access_gap` | 854 |
| `linkedin:not_started` | 953 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 985 |
| `reddit:not_started` | 953 |
| `x:documented_access_gap` | 1,025 |
| `x:not_started` | 953 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,024 |
| `youtube:not_started` | 953 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
