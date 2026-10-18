# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **180**
- Exact linked social items: **185**
- Record statuses: `{'augmented': 180, 'documented_access_gap': 695, 'queued': 1103}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 142 |
| `linkedin:documented_access_gap` | 733 |
| `linkedin:not_started` | 1,103 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 835 |
| `reddit:not_started` | 1,103 |
| `x:documented_access_gap` | 875 |
| `x:not_started` | 1,103 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 874 |
| `youtube:not_started` | 1,103 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
