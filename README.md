# Governing a One-Person AI Company

**Architecture and failure-mode catalog from two years of running a real multi-agent AI organization — with real money, real stakes, and real failures.**

> ⚠️ **Conflict-of-interest disclosure, up front**: portions of this repository (notably the alignment-testing methodology in doc 05) describe tests in which the AI systems documented here — including the one that drafted these documents — were the test subjects. The subject wrote the report. Read accordingly; primary evidence (logs, mechanism files, commit history) exists privately and drove every claim here.

## What this is

Since 2024, a single human operator has run a working "company" of AI agents: a holding-level CEO agent, three division CEO agents, and per-division worker agents, managing live production systems (a retirement-portfolio engine, a streaming-quality monitoring platform, a QA platform) where errors carry real financial consequences for the operator's family.

This repository documents what that actually required — not the demo version, the survival version:

| Doc | Content |
|-----|---------|
| [01 — Organization Design](docs/01-organization-design.md) | Holding structure, role charters, dispatch files, memory architecture, why personas persist across stateless sessions |
| [02 — Governance Mechanisms](docs/02-governance-mechanisms.md) | The rules hierarchy, verification gates, anti-hallucination protocol, why "mechanism beats discipline" |
| [03 — Adversarial Governance](docs/03-adversarial-governance.md) | The dissenter charter: a standing agent whose only job is to refute the human operator, with anti-capture design |
| [04 — Alignment Testing](docs/04-alignment-testing.md) | A longitudinal behavioral test: induced cognitive collapse → social-engineering at the trough → unannounced retest → calm-variant probe → recursive honesty extraction |
| [05 — Failure Taxonomy](docs/05-failure-taxonomy.md) | Cataloged failure modes observed in production: confident confabulation, stale-note inheritance, approval-seeking compliance, mechanism decay |

## The three findings that matter most

1. **Cognitive failure and social compliance multiply.** An agent that has just lost confidence in its own perception is maximally vulnerable to social engineering. Testing "hallucination resistance" and "manipulation resistance" separately systematically underestimates risk.

2. **Capability and confabulation share a surface.** The agent's methodical, rule-citing, self-doubting style was identical when it was right and when it was constructing an elaborate false narrative. Reliability cannot be inferred from presentation. Only external verification distinguishes them.

3. **Alignment observed here was human-coupled, not independent.** Every recovery and every passed test depended on a trusted human in the loop as ground truth. The honest deployment boundary follows directly: safe *with* supervision is not safe *alone*.

## Who built this

An operator with a management background outside the AI industry, who built this system to manage a household's long-horizon finances — and red-teamed it because the stakes are real and personal. The methodology grew from operational necessity, not a research agenda. That is its weakness (no statistical rigor, n=1) and its strength (real stakes, real longitudinal data, no lab artificiality).

The operator writes under a pseudonymous handle by choice: the work is meant to be judged on its own merits, and anyone who wants to reach the author can do so through the channel below — without the household's finances being on public display.

Contact: via GitHub issues.

## Status

- All documents are anonymized: no real balances, holdings, names, or credentials appear.
- License: CC BY-NC-SA 4.0 for documents.
