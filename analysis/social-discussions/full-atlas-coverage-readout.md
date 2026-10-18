# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **249**
- Exact linked social items: **254**
- Record statuses: `{'augmented': 249, 'documented_access_gap': 1076, 'queued': 653}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 211 |
| `linkedin:documented_access_gap` | 1,114 |
| `linkedin:not_started` | 653 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,285 |
| `reddit:not_started` | 653 |
| `x:documented_access_gap` | 1,325 |
| `x:not_started` | 653 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,324 |
| `youtube:not_started` | 653 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
