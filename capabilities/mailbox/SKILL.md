---
name: mailbox
description: Read, triage, extract from, draft and (behind approval) send email in an agency mailbox or shared mailbox, whatever the mail platform. Use when a recipe step starts with an email arriving or ends with a message going out.
license: CC-BY-SA-4.0
metadata:
  version: 0.1.0
  canon: false
---

# Mailbox

## Adapters

| Technology | Adapter | Auth | Status |
| --- | --- | --- | --- |
| Microsoft 365 / Exchange Online | `adapters/m365-graph-mail` | Entra app registration; application or delegated Graph scopes (`Mail.Read`, `Mail.ReadWrite`, `Mail.Send` as separate grants) | planned (fork and harden a community Graph MCP server, vendor it) |
| Exchange on-prem (2016/2019/SE) | `adapters/exchange-ews` | EWS impersonation or Exchange PowerShell with a service account | planned |
| Shared mailbox via a user's Outlook (no COM in New Outlook) | not supported as an adapter | | Use Graph against the shared mailbox instead |

## Read tools

- `mailbox.list(folder, since, filter)`: headers only
- `mailbox.get(message_id)`: body and attachment metadata
- `mailbox.attachments(message_id)`: saves attachments to a working path and returns hashes

## Write tools (each a separate grant, each behind approval at L2 or higher)

- `mailbox.move(message_id, folder)`
- `mailbox.flag(message_id, category)`
- `mailbox.draft(to, subject, body, attachments)`: creates a draft, never sends
- `mailbox.send(draft_id)`: the only tool that sends; requires an approval token from the recipe's hook

## Rules

- Application permissions are scoped to the specific mailbox with an Exchange Online application access policy; never tenant-wide `Mail.Read`.
- Every read is logged with message id, sender domain, subject hash and purpose. Bodies are never logged; they are records already.
- Attachments are written to a path inside the agency boundary and hashed before any model sees them.
- The agent drafts; a person sends, until the registry shows the error rate that earns L1.

## Controls triggered

`fl-ch119-public-records`, `fl-ch257-records-retention`, `fl-60gg-2-cybersecurity`; plus `hipaa` when the mailbox receives PHI, `irs-pub-1075` when it receives FTI.

## Fixtures

`adapters/<adapter>/fixtures/`: a synthetic mailbox of 50 messages covering the ten breakers (missing attachment, duplicate, wrong form, out of order, and so on), with no real names or identifiers.

## Field notes

None yet.
