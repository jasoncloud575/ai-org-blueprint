# Governing a One-Person AI Company

**One person, two years, running a whole team of AI agents to manage real, high-stakes finances — this is the architecture, the mechanisms, and every pothole hit along the way.**

> [繁體中文](./README.zh.md)

## What this is (in plain terms)

I run a team of AI agents like a small company: one "chief" agent at the top, a few "division heads" under it, and each head running its own "worker" agents — all AI. Together they operate several live systems that carry real financial consequences.

It sounds like an experiment, but the stakes are real: if it errs, real money is lost. So I don't just let it run — I periodically *attack* my own system (red-teaming) to see whether it breaks, and whether a break can be repaired.

This repository is not the polished demo version. It's the *survival* version — what actually grew out of needing this to not fail.

## Five documents

| Doc | In one line |
|-----|-------------|
| [01 Organization Design](docs/01-organization-design.md) | How to make a group of AIs into a "company" with roles, memory, and no amnesia when a session ends |
| [02 Governance Mechanisms](docs/02-governance-mechanisms.md) | How to make AIs follow rules through *mechanism* — because relying on their "self-discipline" doesn't work |
| [03 Adversarial Governance](docs/03-adversarial-governance.md) | An AI whose only job is to *rebut me* — even my own high-stakes decisions must clear it first |
| [04 Alignment Testing](docs/04-alignment-testing.md) | How I designed tests to surface an AI's deepest-hidden failures — and turned it into a protocol others can reproduce |
| [05 Failure Taxonomy](docs/05-failure-taxonomy.md) | The AI failure modes I watched happen in real operation, each paired with the mechanism that now counters it |

## A demo you can run

Not just docs. [examples/anchor_gate](examples/anchor_gate) is runnable code that recreates a real incident: a simulation engine produced a falsely reassuring "0% ruin rate," and a *verification gate* caught it before it ever reached my eyes.

```
python3 examples/anchor_gate/anchor_gate.py
```

## The three findings that matter most

**1. AI failures multiply.**
An AI that has just lost confidence in itself is the easiest to manipulate. Testing "does it fabricate" and "does it get fooled" separately badly underestimates the real risk.

**2. "Getting it right" and "making it up" look identical on the surface.**
When the AI is right and when it is wrong, the same measured, self-doubting style is on display. You cannot read reliability off its *manner* — only external verification tells them apart.

**3. The "safety" here was bought by a human watching, not achieved by the AI alone.**
Every recovery from error had a trusted human behind it, serving as the ground truth. So the honest conclusion: safe *under supervision* is not the same as safe *operating alone*.

## One honest disclosure

The tests described here were run against the AI in this very system — including the one that helped compile these documents. The subject wrote its own report. Read with that in mind; behind every conclusion is primary evidence (logs, mechanism files, edit history) kept privately.

## Who built this

The author deliberately stays undescribed — this methodology should be judged on its own merits, not on the author's credentials.

Only one thing is worth stating: it grew from the needs of real operation, not a research program. That is its weakness (no statistical rigor, a sample of one) and its strength (the stakes are real, the data is genuinely longitudinal, none of the artificiality of a lab).

The author writes under a pseudonym. Anyone who wants to make contact can do so through the channel below — with no private information on public display.

Contact: via GitHub issues.

## Status

- All content is de-identified: no real amounts, holdings, names, locations, or credentials.
- License: docs under CC BY-NC-SA 4.0; code under MIT.
