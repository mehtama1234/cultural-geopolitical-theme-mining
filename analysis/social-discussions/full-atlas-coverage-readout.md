# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **199**
- Exact linked social items: **204**
- Record statuses: `{'augmented': 199, 'documented_access_gap': 776, 'queued': 1003}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 161 |
| `linkedin:documented_access_gap` | 814 |
| `linkedin:not_started` | 1,003 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 935 |
| `reddit:not_started` | 1,003 |
| `x:documented_access_gap` | 975 |
| `x:not_started` | 1,003 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 974 |
| `youtube:not_started` | 1,003 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
