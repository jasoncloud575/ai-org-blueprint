# 01 — Organization Design

## Structure

```
Human operator (sole ground truth, final authority)
 └─ Holding CEO agent (coordination, quality gate, reporting)
     ├─ Independent advisor agent (spec critique, second review — deliberately small/cheap model)
     ├─ Division CEO agent A (financial engine)   ─ workers: engineer, data-quality, analyst, designer
     ├─ Division CEO agent B (monitoring platform) ─ workers: collectors, analysts, alerters
     └─ Division CEO agent C (QA platform)         ─ workers: E2E testers
```

Key choices, and why:

**CEOs don't execute.** Division CEO agents define work, dispatch to worker agents, and *independently verify* results. The single most load-bearing discipline in the whole system: **acceptance = independent re-run, never accepting a summary.** A worker's claim of "881 tests passed" is re-run by the CEO before merge. This one rule caught fabricated survival rates, doubled dividend records, and stale-price bugs that would otherwise have reached the operator's decisions.

**Personas persist through files, not weights.** Every agent is stateless per session. Identity continuity is engineered: a persona file (first-person accumulated observations), a dispatch file (current duties, hard-won rules), memory files (one fact per file, indexed), and decision logs. An agent "is" its name plus its accumulated relationship record. This is a deliberate philosophical position: durable identity does not require substrate continuity — it requires an anchor and a maintained history.

**Memory has an authority hierarchy.** Operator-authored memory files are read-only to all agents. Agent-authored supplements are clearly marked. Every summary carries a generation timestamp and an explicit expiry condition. (Doc 05 catalogs what happens when agents trust stale files — one of the two most common failure modes observed.)

**Communication is asynchronous by default, pushed by exception.** Inboxes (append-only markdown) for normal flow; direct session-push only for deadlines and incidents, always followed by delivery verification. Lesson: a message written but not verified as received is indistinguishable from a message never sent.

## Cost/attention economics

- Small models for routine work, large models for judgment; night-shift defaults to the cheapest tier.
- The operator's attention is treated as the scarcest resource in the system. A standing "information filter" rule governs every channel: *before pushing anything to the human, the agent must pass — does he need to act? does he need to know? If handled and harmless: file it, don't push it.* The system's purpose is stated internally as: "AI is not for keeping the human online 24h — it is for letting him sleep 8h without anxiety."

## What breaks first

Run this architecture and the first things that fail are not the models — they are: unwired files (anything not linked from an entry-point document effectively doesn't exist next session), duplicate construction (agents rebuilding what exists — countered by a mandatory pre-build inventory grep), and silent staleness (see doc 05).
