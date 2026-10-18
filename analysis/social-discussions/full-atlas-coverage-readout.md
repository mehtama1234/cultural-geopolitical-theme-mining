# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **63**
- Exact linked social items: **68**
- Record statuses: `{'augmented': 63, 'documented_access_gap': 137, 'queued': 1778}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 25 |
| `linkedin:documented_access_gap` | 175 |
| `linkedin:not_started` | 1,778 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 160 |
| `reddit:not_started` | 1,778 |
| `x:documented_access_gap` | 200 |
| `x:not_started` | 1,778 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 199 |
| `youtube:not_started` | 1,778 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
