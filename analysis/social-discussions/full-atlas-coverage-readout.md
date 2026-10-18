# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **169**
- Exact linked social items: **174**
- Record statuses: `{'augmented': 169, 'documented_access_gap': 631, 'queued': 1178}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 131 |
| `linkedin:documented_access_gap` | 669 |
| `linkedin:not_started` | 1,178 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 760 |
| `reddit:not_started` | 1,178 |
| `x:documented_access_gap` | 800 |
| `x:not_started` | 1,178 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 799 |
| `youtube:not_started` | 1,178 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
