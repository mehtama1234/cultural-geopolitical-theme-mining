# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **82**
- Exact linked social items: **87**
- Record statuses: `{'augmented': 82, 'documented_access_gap': 243, 'queued': 1653}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 44 |
| `linkedin:documented_access_gap` | 281 |
| `linkedin:not_started` | 1,653 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 285 |
| `reddit:not_started` | 1,653 |
| `x:documented_access_gap` | 325 |
| `x:not_started` | 1,653 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 324 |
| `youtube:not_started` | 1,653 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
