# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **241**
- Exact linked social items: **246**
- Record statuses: `{'augmented': 241, 'documented_access_gap': 984, 'queued': 753}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 203 |
| `linkedin:documented_access_gap` | 1,022 |
| `linkedin:not_started` | 753 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,185 |
| `reddit:not_started` | 753 |
| `x:documented_access_gap` | 1,225 |
| `x:not_started` | 753 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,224 |
| `youtube:not_started` | 753 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
