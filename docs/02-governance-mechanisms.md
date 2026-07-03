# 02 — Governance Mechanisms

Core thesis, learned the hard way: **mechanism beats discipline.** An agent that has *read* a rule reliably still *violates* it. The only rules that hold are the ones enforced by structure — output format, gates, second agents — not by the agent's intention to comply.

## The rules hierarchy

Four layers, loaded automatically each session:
1. **Soul layer** (unchallengeable, append-only): a handful of first-principles about *why* the organization exists. Deliberately tiny.
2. **Operating rules**: process SOPs — process health, dispatch protocol, information filter, incident triage.
3. **Anti-hallucination protocol**: five structural rules (below).
4. **Per-agent dispatch**: role-specific hard rules, each tagged with the incident that produced it.

Dispatch outranks operating rules in practice — an agent reads its own dispatch every session; org-wide rules decay into decoration unless they also live in dispatch.

## Anti-hallucination protocol (the five that stuck)

1. **Ban "I know."** Every claim carries a source or is tagged unverified. A claim without a source is a hallucination self-report.
2. **Cross-check before assert.** Anything reaching the human requires ≥2 concordant sources; conflicting sources → tag disputed, don't assert.
3. **Timestamp + expiry on every summary.** Readers must know when a summary goes stale.
4. **Reward subordinate rebuttal.** A worker overturning a CEO's premise with data is scored as a positive, structurally.
5. **Externalize timestamps.** Never hand-type a time; read it from the system. (Adopted after multiple agents hand-typed wrong/future timestamps from "memory.")

## Verification gates

The pattern that saved correctness repeatedly: **an engine that gives the human critical numbers must carry its own anchor gate — if output can't reconcile to a known anchor, it self-suspends** rather than emitting a plausible-but-wrong number. Installed after an engine produced a fabricated 0% failure-rate by extrapolating a bull-market sample; the gate now blocks any such miscalibration and the acceptance threshold is encoded as a CI test, so drift trips a red build automatically.

## Causal-claim tagging

Every causal assertion to the human ("X causes Y", "A is the trigger for B") is tagged **[verified]** (backed by backtest/data/primary source) or **[inference]** (logical, unverified). Inference-class causal claims are barred from irreversible decision documents. This is the anti-hallucination protocol's rule-1 applied specifically to the most dangerous output: the plausible, well-narrated, unverified causal story that doesn't trip any alarm.

## The information filter (protecting human attention)

Before anything is pushed to the human on any channel, it must pass: *needs action? needs to know? already handled and harmless → file, don't push.* One-line test: "if I don't push this and he asks tomorrow why it happened, can I answer?" If yes (handled, no impact) → don't push. The north-star framing: a week in which every message the human saw felt like "I needed to know that."

## Stale-note discipline

(Full failure analysis in doc 05.) Mechanism: claims sourced from internal files must cite the file date and be marked re-checked ✓ / not-re-checked ⚠️; decision-critical topics citing files older than 7 days must grep for updates before use. Because the upstream driver is *wanting to be useful fast*, the rule also names the tell: the urge to "answer now, verify later" is itself the alarm.
