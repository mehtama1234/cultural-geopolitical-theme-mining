# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **16**
- Exact linked social items: **19**
- Record statuses: `{'augmented': 7, 'in_review': 18, 'queued': 1953}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 2 |
| `linkedin:documented_access_gap` | 5 |
| `linkedin:not_started` | 1,971 |
| `reddit:augmented` | 15 |
| `reddit:documented_access_gap` | 1 |
| `reddit:not_started` | 1,962 |
| `x:documented_access_gap` | 7 |
| `x:not_started` | 1,971 |
| `youtube:documented_access_gap` | 7 |
| `youtube:not_started` | 1,971 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
