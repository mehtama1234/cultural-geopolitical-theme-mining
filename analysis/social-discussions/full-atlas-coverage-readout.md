# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **233**
- Exact linked social items: **238**
- Record statuses: `{'augmented': 233, 'documented_access_gap': 942, 'queued': 803}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 195 |
| `linkedin:documented_access_gap` | 980 |
| `linkedin:not_started` | 803 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,135 |
| `reddit:not_started` | 803 |
| `x:documented_access_gap` | 1,175 |
| `x:not_started` | 803 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,174 |
| `youtube:not_started` | 803 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
