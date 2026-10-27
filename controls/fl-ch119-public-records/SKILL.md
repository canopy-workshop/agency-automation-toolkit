---
name: fl-ch119-public-records
description: Florida public records law (Chapter 119, F.S.) as it applies to automations and agents. Load for every process card; it governs what the agent's own logs, prompts, drafts and tool calls are, and how outputs must be handled before they leave.
license: CC-BY-SA-4.0
metadata:
  version: 0.1.0
  canon: true
  as_of: 2026-10-16
  jurisdiction: FL
---

# Chapter 119, F.S.: Public Records

## What it is

Florida's public records law. Any material made or received in connection with official agency business is a public record, open to inspection and copying unless a specific statutory exemption applies (Art. I, s. 24, Fla. Const.; s. 119.01, s. 119.07, F.S.). Exemptions are enumerated and construed narrowly; most live in s. 119.071 and in the substantive statutes of each program.

## Why it binds an automation

An agent's prompts, transcripts, drafts, tool calls, and the records log are made in connection with agency business. They are records. So are the spreadsheets, macros and inbox rules found during intake. Design the records log as a records system from day one; it is the audit trail you need anyway.

## Triggers

Always.

## Checklist

- [ ] The records log captures, per action: actor (service identity and approving human), action, purpose, input hash, output hash, timestamp, and the automation id
- [ ] Log storage is inside the agency's systems, retrievable by the records custodian without vendor help
- [ ] Every record in the log carries a retention series (`fl-ch257-records-retention`)
- [ ] Exempt and confidential categories present in the process are listed on the card, with the statutory cite for each exemption
- [ ] Redaction or exemption tagging runs before any output reaches a requester or the public, not after a request arrives
- [ ] Prompts and system instructions used in production are versioned and retained like any other record
- [ ] Any vendor or model host contract preserves the agency's ability to produce records on request (s. 119.0701 contractor requirements)
- [ ] The agency's records custodian knows the automation exists and where its records are

## Design constraints

- Log store = records system. No separate "debug logs" with record content outside it.
- Exemption tagging is a step in the recipe's output path, with its own exception lane to a human.
- Model hosts outside the agency boundary create records the agency may not be able to produce; prefer in-boundary hosting (`model-gateway`).

## References

- Ch. 119, F.S.: https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0119/0119.html
- Government-in-the-Sunshine Manual (Attorney General), current edition
- s. 119.0701, F.S. (contractors acting on behalf of agencies)

## Field notes

None yet.
