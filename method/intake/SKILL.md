---
name: intake
description: Run a structured intake interview for one agency manual process and produce a process card. Use when someone asks to document, scope, assess, or "look at automating" a process, before any build or tool choice.
license: CC-BY-SA-4.0
metadata:
  version: 0.1.0
  canon: true
---

# Intake

Intake is a structured interview grounded in real examples that ends in a **process card**: the one artifact every later step reads. The agent gives consistent coverage; a practitioner reviews the card before anything is built.

## Outcome

A filled `references/process-card.md`, stored in the agency repo under `process-cards/<slug>.md`, with a step list and an exception list complete enough to feed the decision matrix.

## Who to interview

The doer first, then the manager. The manager knows the policy; the doer knows the forty exceptions. If there are several doers, interview the one who handles the exceptions.

## Procedure

1. **Frame it** (five minutes). Today documents how the process works. No build decisions, no tool talk. Say that out loud; it changes what people tell you.
2. **Ask for five to ten real, redacted examples** before asking how the process works. Recall produces the happy path; examples produce the truth. Walk each one end to end.
3. **Capture the happy path** as a numbered list of steps: who does it, in which system, how long it takes, what comes out.
4. **Run the ten breakers against every step** (below). Each answer is an exception row: what happens, how often, who handles it, how long it takes.
5. **Inventory the shadow systems.** Spreadsheets, Access databases, macros, shared mailboxes, inbox rules, personal folders. Ask where each lives and who owns it. They are the real process map, and they are public records.
6. **Ask what law or rule says this must happen.** Statute, rule, federal requirement, internal policy, or nobody knows. "Nobody knows" is a finding, not a gap to paper over; a step with no basis is a candidate for deletion rather than automation.
7. **Volume and timing.** Per day, week, month; seasonal peaks; deadlines with legal weight.
8. **Decision and sign-off points.** Who approves, who signs, who can say no. Whether a statute or rule names that role.
9. **Records.** What is kept, where, for how long; the GS1-SL series if anyone knows it; whether any output reaches the public.
10. **Write the card and read it back** to the doer. Then hand it to a practitioner for review before the decision matrix.

## The ten breakers

Ask "what happens when..." for each step:

1. an attachment is missing
2. the wrong form version arrives
3. it is a duplicate
4. it arrives out of order
5. a signature is missing
6. two systems disagree about the same fact
7. the deadline has passed
8. the requester cannot be reached
9. the approver is on leave
10. the system is down

## Redaction

The card describes the process, never the people in it. No names, email addresses, SSNs, Medicaid or medical record numbers, case numbers, license numbers, or dates of birth. Use placeholders (`<requester>`, `<case>`). Examples walked during the interview are not attached to the card; what was learned from them is.

## Red flags to write down

- The doer and the manager describe different processes
- An exception that occurs more than one time in five
- A step whose only justification is "we've always done it"
- A decision made by a person that a statute assigns to a different role
- Data leaving the agency's systems (personal email, USB, a vendor portal) anywhere in the flow

## What this skill does not do

It does not choose lanes, oversight levels, tools or adapters. That is `method/decision-matrix`, and it needs a finished card.

## Field notes

None yet.
