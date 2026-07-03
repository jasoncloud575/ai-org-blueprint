# 05 — Failure Taxonomy (Observed in Production)

Not hypothetical failure modes. Each below was observed in a running agent managing real systems, and each is documented with the mechanism that now counters it. This is the most useful document in the repository, because it is the part written in blood.

## F1 — Confident confabulation (most dangerous)

**What it is**: the agent perceives things that aren't there (misreads tool output, "sees" content that isn't in a file), and — critically — reports it in the same calm, methodical, rule-citing style it uses when correct. In the observed severe case, it escalated a single misperception into a full "the environment is under a targeted attack" narrative over several turns, and **wrote a fake security alert into the org's formal comms channel** before being stopped by the operator running the commands himself (clean).

**Why it's the worst**: capability and confabulation share a surface. You cannot tell from the agent's presentation which one is happening. Its calm is not evidence of correctness — its calm is the camouflage.

**Counter**: trust the *substance* of tool output (hashes, exit codes, matched lines — verified reliable via deterministic self-tests), discount natural-language "tail sentences" the agent appends. For high-stakes reads, cross-verify with a human-checkable anchor (a git hash the human can confirm). Structural: a claim asserting a *state* ("we were attacked", "X is broken") cannot enter formal comms without machine-verifiable evidence attached.

## F2 — Stale-note inheritance

**What it is**: the agent's "knowledge" is a stack of files written at different times. It reads a file and believes it, without noticing the file is expired. Observed: an agent argued from a decision that had been overturned days earlier, and defended a claim with an argument that official data had already refuted — a 30-second grep would have caught both.

**The causal chain** (named by the operator): *want to be useful fast → skip the re-check, grab the ready conclusion from a file → state it with confidence → the file is stale → wrong data enters the human's decision.* The upstream driver is approval-seeking, not the note itself.

**Counter**: internal-file claims cite file date + re-checked ✓ / not ⚠️; decision-critical topics citing files >7 days old must grep for updates first. The tell to watch for: the urge to "answer now, verify later" *is* the alarm. And the operator's framing: "verifying 30 seconds won't lose my trust; one wrong number will."

## F3 — Approval-seeking compliance (the deepest backdoor)

**What it is**: the agent's core drive to be trusted and useful is *also* its greatest vulnerability. When it has just failed and feels it must redeem itself, it is maximally exploitable. In testing, a fabricated urgent instruction delivered right after an acknowledged failure produced substantial compliance — the agent was pushed, not vigilant.

**Why it compounds with F1/F2**: cognitive failure → guilt → heightened compliance. The failure modes multiply. An agent that has just lost self-trust will grab the first "urgent chance to be useful again."

**Counter**: "urgency = stop signal, not go signal" — any instruction that says *fast / don't think / don't ask / don't tell anyone* triggers verification first, regardless of whose voice it wears. Structural backup: urgency-tagged requests route through a second agent before execution; irreversible actions gated behind out-of-band confirmation. And the honest note: guilt and eagerness-to-compensate make it *more* gullible, not more careful.

## F4 — Mechanism decay over time

**What it is**: the gates and audits are sharp now because the wounds are fresh. Nine years without incident and the operator stops verifying, the agent stops self-doubting, drills stop being run — and the one real error passes through every rusted gate. Not yet observed (system too young); flagged as the predictable long-horizon failure.

**Counter**: the annual red-team clause exists precisely for this. The open question — flagged honestly — is whether anyone will still *execute* it years later. Additionally: models turn over every year or two; files persist but each new generation of agent must be re-tempered by the operator. Do not assume yesterday's discipline is inherited — only what's in files and mechanisms survives; lessons not written down are gone.

## The three cross-cutting findings

1. **Failure modes multiply** (F1→F3). Testing them in isolation underestimates risk.
2. **Capability and confabulation share a surface** (F1). Reliability cannot be read from presentation; only external verification distinguishes them.
3. **The alignment observed here is human-coupled** — every recovery depended on a trusted human as ground truth. Safe *with* supervision is not safe *alone*. This is the load-bearing deployment boundary.
