# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **293**
- Exact linked social items: **298**
- Record statuses: `{'augmented': 293, 'documented_access_gap': 1482, 'queued': 203}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 255 |
| `linkedin:documented_access_gap` | 1,520 |
| `linkedin:not_started` | 203 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,735 |
| `reddit:not_started` | 203 |
| `x:documented_access_gap` | 1,775 |
| `x:not_started` | 203 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,774 |
| `youtube:not_started` | 203 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
