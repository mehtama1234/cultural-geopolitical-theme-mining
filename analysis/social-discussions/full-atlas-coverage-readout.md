# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **65**
- Exact linked social items: **70**
- Record statuses: `{'augmented': 65, 'documented_access_gap': 160, 'queued': 1753}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 27 |
| `linkedin:documented_access_gap` | 198 |
| `linkedin:not_started` | 1,753 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 185 |
| `reddit:not_started` | 1,753 |
| `x:documented_access_gap` | 225 |
| `x:not_started` | 1,753 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 224 |
| `youtube:not_started` | 1,753 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
