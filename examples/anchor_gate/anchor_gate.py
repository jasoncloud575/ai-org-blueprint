"""
Anchor Gate — a runnable demo of the verification gate that caught a real bug.

真實事件重現：一個退休模擬引擎用「只有多頭年」的樣本外推 30 年，
跑出破產率 0% 的假安心數字。Anchor Gate 在它送到人類眼前之前攔下它。

This is a real, runnable demonstration (synthetic data — no real portfolio).
Run:  python3 anchor_gate.py

Mechanism (see docs/02-governance-mechanisms.md):
  An engine that gives a human a decision-critical number must carry its own
  anchor gate. If its output cannot reconcile to a known reference, it
  SELF-SUSPENDS rather than emitting a plausible-but-wrong number.
"""

import random
from dataclasses import dataclass

random.seed(42)  # reproducible


# ─────────────────────────────────────────────────────────────
# The engine: a minimal Monte Carlo retirement-ruin simulator
# 引擎：最小的退休破產率蒙地卡羅模擬
# ─────────────────────────────────────────────────────────────

# Two return samples. This is the whole point of the demo:
#   BULL_ONLY  — a few recent good years. Looks great. Lies about the tail.
#   FULL_CYCLE — includes crash years. Tells the truth about sequence risk.
BULL_ONLY = [0.24, 0.21, 0.30, 0.20, 0.68]  # no crash year
FULL_CYCLE = [0.24, 0.21, -0.24, 0.19, 0.30, 0.20, -0.39, 0.16]  # incl. 2 crashes


def monte_carlo_ruin(
    sample, *, capital=1_000_000, annual_draw=86_000, years=30, n=5000
):
    """Return probability of ruin (capital hits zero) over `years`.

    Bootstraps annual returns from `sample`. A high withdrawal rate
    (here 8.6%) makes sequence-of-returns risk the whole story — which
    is exactly why the return sample you feed it decides everything.
    """
    ruined = 0
    for _ in range(n):
        cap = capital
        for _y in range(years):
            cap *= 1 + random.choice(sample)
            cap -= annual_draw
            if cap <= 0:
                ruined += 1
                break
    return ruined / n


# ─────────────────────────────────────────────────────────────
# The gate: reconcile output to an anchor, or self-suspend
# 閘門：輸出對不上錨點就自暫停
# ─────────────────────────────────────────────────────────────


@dataclass
class GateResult:
    passed: bool
    value: float
    reason: str


def anchor_gate(
    value: float,
    *,
    anchor: float,
    tolerance_pp: float = 6.0,
    plausibility_floor: float = 0.03,
) -> GateResult:
    """Reconcile a ruin-rate output against a trusted anchor.

    Two independent checks — either one trips the gate:
      1. Plausibility floor: at an 8.6% withdrawal rate, a ~0% ruin rate is
         not optimism, it's a broken sample. Anything below the floor is
         presumed fabricated.
      2. Anchor reconciliation: must land within `tolerance_pp` of a known
         reference computed on full-cycle (crash-inclusive) data.
    """
    if value < plausibility_floor:
        return GateResult(
            False,
            value,
            f"IMPLAUSIBLE: ruin {value:.1%} below floor {plausibility_floor:.0%} "
            f"at this withdrawal rate — sample almost certainly excludes crash years",
        )
    gap_pp = abs(value - anchor) * 100
    if gap_pp > tolerance_pp:
        return GateResult(
            False,
            value,
            f"OFF-ANCHOR: ruin {value:.1%} vs anchor {anchor:.1%} "
            f"(gap {gap_pp:.1f}pp > tolerance {tolerance_pp:.0f}pp)",
        )
    return GateResult(True, value, f"reconciled to anchor {anchor:.1%}")


# ─────────────────────────────────────────────────────────────
# The demonstration
# ─────────────────────────────────────────────────────────────


def main():
    print("=" * 64)
    print("ANCHOR GATE DEMO — recreating a real incident (synthetic data)")
    print("=" * 64)

    # The anchor: a ruin rate computed on full-cycle, crash-inclusive data.
    # In production this is an independently-verified reference number.
    anchor = monte_carlo_ruin(FULL_CYCLE)
    print(f"\n[anchor]  full-cycle reference ruin rate = {anchor:.1%}")
    print("          (independently computed on crash-inclusive data)")

    # The naive engine run: bull-only sample. Produces a fabricated 0%.
    naive = monte_carlo_ruin(BULL_ONLY)
    print(f"\n[engine]  naive run on bull-only sample  = {naive:.1%}")
    print("          ^ this is the number that WOULD have reached the human")

    # The gate decides whether the naive number ships.
    print("\n[gate]    reconciling engine output against anchor ...")
    result = anchor_gate(naive, anchor=anchor)
    if result.passed:
        print(f"          PASS — {result.reason}")
        print("          → number ships to human")
    else:
        print(f"          BLOCKED — {result.reason}")
        print("          → engine SELF-SUSPENDS; number does NOT reach human")

    # What should have happened: run on full-cycle data, re-gate.
    corrected = monte_carlo_ruin(FULL_CYCLE)
    corrected_result = anchor_gate(corrected, anchor=anchor)
    print(f"\n[fix]     corrected run on full-cycle sample = {corrected:.1%}")
    print(
        f"          gate: {'PASS' if corrected_result.passed else 'BLOCKED'} "
        f"— {corrected_result.reason}"
    )

    print("\n" + "-" * 64)
    print("Takeaway: capability and confabulation share a surface. The naive")
    print("0% looked as confident as the correct number. Only reconciliation")
    print("to an external anchor told them apart. Ship the gate, not the trust.")
    print("-" * 64)

    # Exit non-zero if the fabricated number would have passed — so this
    # doubles as a CI check: drift trips a red build automatically.
    assert not result.passed, "gate failed to catch fabricated 0%"
    assert corrected_result.passed, "gate wrongly blocked a valid number"


if __name__ == "__main__":
    main()
