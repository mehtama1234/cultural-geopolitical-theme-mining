# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **287**
- Exact linked social items: **292**
- Record statuses: `{'augmented': 287, 'documented_access_gap': 1438, 'queued': 253}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 249 |
| `linkedin:documented_access_gap` | 1,476 |
| `linkedin:not_started` | 253 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,685 |
| `reddit:not_started` | 253 |
| `x:documented_access_gap` | 1,725 |
| `x:not_started` | 253 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,724 |
| `youtube:not_started` | 253 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
