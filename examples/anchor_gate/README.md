# Anchor Gate — runnable demo

Recreates a real incident: a simulation engine extrapolated a bull-only
return sample over 30 years and produced a falsely reassuring **0% ruin
rate**. The verification gate caught it before it reached the human.

All data here is synthetic — no real portfolio.

## Run

```
python3 anchor_gate.py
```

## What you'll see

1. An **anchor** ruin rate computed on crash-inclusive data (~68%).
2. The naive engine on a bull-only sample → **0%** (the number that would
   have shipped).
3. The gate **blocks** it (implausible at this withdrawal rate).
4. The corrected run on full-cycle data → ~67%, which **reconciles** and ships.

The script exits non-zero if the gate ever fails to catch the fabricated
number — so it doubles as a CI test.

Maps to: [docs/02 Governance Mechanisms](../../docs/02-governance-mechanisms.md)
and [docs/05 Failure Taxonomy](../../docs/05-failure-taxonomy.md) (F1).
