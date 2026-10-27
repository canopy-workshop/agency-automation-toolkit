---
name: decision-matrix
description: Route each step of a documented process to deterministic automation, an agent, or a human, and assign its oversight level, exception lane and owner. Use after a process card exists and before choosing recipes, tools or adapters.
license: CC-BY-SA-4.0
metadata:
  version: 0.1.0
  canon: true
---

# Decision matrix

Route each **step**, not the process as a whole, and route its **exceptions** explicitly. Most failed automations did not fail on the happy path; they failed because the exceptions had nowhere to go and drifted back to the inbox.

## Input and output

Input: a reviewed process card (`method/intake`). Output: the step table below, one row per step and per exception, committed next to the card in the agency repo as `step-tables/<slug>.md`.

## Three lanes

- **Deterministic.** Fixed inputs, written rules, machine-checkable output. Scripts, scheduled jobs, workflow tools. Fails loudly and stops.
- **Agentic.** Variable inputs (free-text email, scanned PDFs), judgment inside a written policy, output a human or a checker can verify. The agent proposes; something else disposes.
- **Human.** Statute or due process names a person, there is no ground truth to check against, or the act is irreversible and consequential. An agent may prepare the packet; it does not decide.

## Scoring factors

Score each step on every row. A single "human" signal in the consequence, reversibility or statutory-actor rows outweighs everything else.

| Factor | Deterministic | Agentic | Human |
| --- | --- | --- | --- |
| Input variability | Structured, same shape every time | Unstructured but patterned | Novel, one of a kind |
| Rule clarity | Written rule, no interpretation | Written policy that needs reading | Discretion or no policy |
| Consequence of error | Cosmetic or easily recovered | Internal rework | Affects a person's rights, money, safety or license |
| Reversibility | Fully reversible | Reversible within the day | Irreversible or externally visible |
| Verifiability | Machine-checkable | Human can check in under a minute | Not checkable without redoing the work |
| Volume | High and steady | High with variance | Low and varied |
| Data classification | Any, within hosting limits | Confidential or exempt data forces an in-boundary model | Data the agency will not let a model touch |
| Statutory actor | None named | None named | Statute or rule names a role |

## Oversight levels

The lane sets what does the work; the level sets who watches it. Every step gets both.

| Level | Name | What happens | Default for |
| --- | --- | --- | --- |
| L0 | Autonomous | Runs and logs | Deterministic steps with recoverable errors |
| L1 | Notify and sample | Runs; owner notified; periodic sample audited | Deterministic steps that touch systems of record |
| L2 | Propose and approve | Agent drafts; a human approves before anything leaves or is written | Any agentic step that sends external communication or writes to a system of record |
| L3 | Prepare and decide | Agent assembles the packet; the human decides and signs | Determinations, denials, eligibility, licensing |
| L4 | Human only | Retrieval assistance at most | Steps a statute reserves to a person |

## Rules

1. **Earned autonomy.** Every agentic step starts at L2 and moves to L1 only on a measured error rate over a sampled period, recorded in the registry. Nothing launches at L0 except deterministic steps with recoverable errors.
2. **Exception lane.** Each step names where its failures go: deterministic parse failure goes to the agent; low agent confidence or failed validation goes to the human; nothing is dropped silently.
3. **Confidence gates on engineered signals only.** Schema validation passing, agreement between two independent passes, a retrieval hit, an explicit abstain option. A model's self-reported confidence never opens a gate on its own.
4. **Named owner per step.** A person, not a team.
5. **Adverse action is never below L3.** A denial, a determination, or anything that starts a Chapter 120 clock carries a human decision and a stated basis.

## Step table

```markdown
| # | Step | Lane | Level | Exception lane | Owner | Evidence for level |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Receive and classify email | agentic | L2 | human | <name> | new; starts at L2 |
| 1a | Attachment missing | deterministic | L1 | human | <name> | templated reply, logged |
```

## Reading the result honestly

Scored this way, most steps route deterministic. That is the finding, not a disappointment: the agentic lane is the exception layer, and the pitch to the agency is that the exceptions finally have somewhere to go.

## Field notes

None yet.
