# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **184**
- Exact linked social items: **189**
- Record statuses: `{'augmented': 184, 'documented_access_gap': 716, 'queued': 1078}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 146 |
| `linkedin:documented_access_gap` | 754 |
| `linkedin:not_started` | 1,078 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 860 |
| `reddit:not_started` | 1,078 |
| `x:documented_access_gap` | 900 |
| `x:not_started` | 1,078 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 899 |
| `youtube:not_started` | 1,078 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
