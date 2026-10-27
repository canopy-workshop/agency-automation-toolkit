---
name: hipaa
description: HIPAA Privacy, Security and Breach Notification rules (45 CFR Parts 160 and 164) for automations that touch protected health information at a health agency or health-plan program. Load when a process card lists PHI, medical records, claims, eligibility or provider data.
license: CC-BY-SA-4.0
metadata:
  version: 0.1.0
  canon: false
  as_of: 2026-10-16
  jurisdiction: US
---

# HIPAA

## What it is

Federal rules governing protected health information held by covered entities (health plans, including a state Medicaid agency; providers; clearinghouses) and their business associates. Three rules matter here: Privacy (use and disclosure, minimum necessary), Security (administrative, physical and technical safeguards for ePHI), and Breach Notification. 42 CFR Part 2 adds stricter rules for substance use disorder records.

## Why it binds an automation

Any component that creates, receives, maintains or transmits PHI on the agency's behalf, including a model host, an MCP server, a vendor's extraction service, or Canopy Road during a build with real data, is a business associate and needs a business associate agreement. Fixtures exist so that no real PHI is needed during a build.

## Triggers

Process card data classification includes PHI; the agency is a covered entity or the program is a health plan; any system touched holds claims, eligibility, clinical or provider-identifiable patient data.

## Checklist

- [ ] Covered entity and business associate roles identified for every component in the recipe, including the model host and any OCR or extraction service
- [ ] BAA in place for each business associate before any non-fixture data is processed
- [ ] Model host is inside a HIPAA-eligible government cloud boundary or on-prem; PHI never goes to a public endpoint
- [ ] Minimum necessary applied: the agent receives only the fields the step needs, not the whole record
- [ ] Access controls: unique service identity per automation, least privilege, automatic logoff / token expiry recorded in the registry
- [ ] Audit controls: the records log meets Security Rule audit requirements and is retained six years from creation or last effective date (45 CFR 164.316(b)(2))
- [ ] Transmission security: encryption in transit for every hop, including between MCP server and model host
- [ ] Breach response: the recipe's incident runbook names who assesses, who notifies, and the timelines (60 days to individuals; HHS and media thresholds); aligned with `fl-501-171-fipa`
- [ ] 42 CFR Part 2 assessed if the program touches substance use disorder treatment records; consent rules are stricter than HIPAA's
- [ ] Workforce training noted for the human owner and queue reviewers

## Design constraints

- No PHI in prompts logged outside the records system; log hashes, not bodies.
- Fixtures only during build; the first live run happens in the agency tenant.
- De-identification (Safe Harbor or expert determination) is an option for analytics steps, never a shortcut for operational steps.

## References

- 45 CFR Parts 160 and 164: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C
- HHS Security Rule guidance and the Security Risk Assessment tool
- 42 CFR Part 2 (as amended 2024)

## Field notes

None yet.
