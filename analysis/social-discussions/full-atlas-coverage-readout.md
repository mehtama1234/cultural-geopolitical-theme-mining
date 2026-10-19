# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **343**
- Exact linked social items: **355**
- Record statuses: `{'augmented': 341, 'documented_access_gap': 1670, 'in_review': 3}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 304 |
| `linkedin:documented_access_gap` | 1,707 |
| `linkedin:not_started` | 3 |
| `reddit:augmented` | 44 |
| `reddit:documented_access_gap` | 1,967 |
| `reddit:not_started` | 3 |
| `x:documented_access_gap` | 2,011 |
| `x:not_started` | 3 |
| `youtube:augmented` | 3 |
| `youtube:documented_access_gap` | 2,008 |
| `youtube:not_started` | 3 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
