---
name: inbox-to-case-system
description: Turn messages arriving in an agency mailbox into correctly created or updated cases in a line-of-business system, with acknowledgements, exception routing and a full records log. Use when a process card's trigger is "an email arrives" and its main output is a case, ticket, application or complaint record.
license: CC-BY-SA-4.0
metadata:
  version: 0.1.0
  canon: false
  pilot: true
---

# Recipe: inbox to case system

The first pilot recipe. Fields marked `<fill>` come from the agency's process card and step table.

## Capabilities used

`mailbox` (read; `draft`/`send` behind approval), `pdf` (attachments), `database` or `line-of-business` (case create/update), `identity`, `model-gateway` (in-boundary host), records log.

## Default step table

Starting point only; the matrix is run against the agency's own card and overrides this.

| # | Step | Lane | Level | Exception lane | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | Poll mailbox folder; dedupe by message id and content hash | deterministic | L1 | agent | Duplicate goes to step 1a |
| 1a | Duplicate detected | deterministic | L1 | human | Templated reply or silent file, per card |
| 2 | Classify message: in scope / out of scope / needs human | agentic | L2 | human | Gate: schema-valid label plus two-pass agreement; else abstain to human |
| 3 | Extract fields from body and attachments | agentic | L2 | human | Validate against the case system's schema; failed validation to human |
| 3a | Attachment missing, wrong form version, unreadable scan | deterministic | L1 | human | Templated request to sender, drafted; sent at L2 until earned |
| 4 | Match to existing case or person | deterministic (exact) / agentic (fuzzy) | L1 / L2 | human | Fuzzy match never auto-links; it proposes |
| 5 | Create or update the case | deterministic write | L2 | human | Write via approved API or stored procedure only |
| 6 | Acknowledge the sender | deterministic | L2 | human | Draft from template; send on approval |
| 7 | Log: who, what, why, input hash, output hash, retention series | deterministic | L0 | human | Writes before every step returns |
| 8 | Anything that affects a person's eligibility, license or rights | human | L3 or L4 | | Agent prepares the packet only |

## Exception routing

Every exception lands in one of two queues, both visible to the named owner:

- **Agent queue**: parse and format failures the agent can retry with context
- **Human queue**: abstains, failed validation, fuzzy matches, anything from step 8

Nothing is dropped. The human queue's size and age are registry metrics.

## Controls triggered

`fl-ch119-public-records`, `fl-ch257-records-retention`, `fl-60gg-2-cybersecurity`, `fl-ch120-apa` if any output is a determination; `hipaa` and `medicaid-431-subpart-f` when the mailbox or case system holds PHI or Medicaid applicant/recipient data.

## Hosting

Build and test on fixtures anywhere. At runtime the model host is inside the agency boundary (`model-gateway`), and the process card, attachments and case data never leave it.

## Deliverables for a fixed-price engagement

1. **Build report**: process card, step table, controls checklist results, adapter list with licenses (pre-existing IP declared), hosting and identity plan, acceptance criteria
2. **Deployment**: adapters configured in the agency tenant, recipe running at L2, owner trained on the human queue, registry record committed, calendar workflow live

## Acceptance criteria (template)

- `<fill>` messages per `<period>` processed with `<fill>`% reaching the case system without human correction
- Human queue reviewed daily; median age under `<fill>` hours
- Zero messages lost: every message id in the mailbox appears in the log with a disposition
- Records officer confirms log retention series; counsel confirms no step below L3 produces an adverse action

## Field notes

None yet.
