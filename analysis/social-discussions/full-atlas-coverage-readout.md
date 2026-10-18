# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **165**
- Exact linked social items: **170**
- Record statuses: `{'augmented': 165, 'documented_access_gap': 610, 'queued': 1203}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 127 |
| `linkedin:documented_access_gap` | 648 |
| `linkedin:not_started` | 1,203 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 735 |
| `reddit:not_started` | 1,203 |
| `x:documented_access_gap` | 775 |
| `x:not_started` | 1,203 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 774 |
| `youtube:not_started` | 1,203 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
