# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **243**
- Exact linked social items: **248**
- Record statuses: `{'augmented': 243, 'documented_access_gap': 1007, 'queued': 728}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 205 |
| `linkedin:documented_access_gap` | 1,045 |
| `linkedin:not_started` | 728 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,210 |
| `reddit:not_started` | 728 |
| `x:documented_access_gap` | 1,250 |
| `x:not_started` | 728 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,249 |
| `youtube:not_started` | 728 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
