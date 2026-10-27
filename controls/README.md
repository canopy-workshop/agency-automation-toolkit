# Controls library

Florida has no comprehensive AI statute for state agencies as of October 2026, and that is the first lesson here: absence of an AI law is not absence of law. Records, due process, cybersecurity and privacy law already govern every automation an agency runs.

Each instrument is a skill: what it is, which process-card fields trigger it, a checklist, and the design constraint it imposes. The agent loads the page when a card mentions the trigger; a person uses it as a review checklist. Pointers and checklists, not legal advice: every process card carries sign-off lines for the agency's general counsel and records management liaison officer.

**Maintenance:** the Florida session runs January through March. Every page gets an update pass each April, and each page carries an `as_of` date in its front matter.

## Index

| Folder | Instrument | Triggered when the card shows | Status |
| --- | --- | --- | --- |
| `fl-ch119-public-records` | Ch. 119, F.S. | Always | page |
| `fl-ch257-records-retention` | Ch. 257, F.S.; GS1-SL schedule | Always | planned |
| `fl-ch120-apa` | Ch. 120, F.S. (Administrative Procedure Act) | Any output is a determination, denial, eligibility or licensing action | planned |
| `fl-ch282-enterprise-it` | Ch. 282, F.S. (incl. 282.206 cloud-first, 282.318 cybersecurity) | Any hosting choice; projects above oversight thresholds | planned |
| `fl-60gg-2-cybersecurity` | Rule 60GG-2, F.A.C. (Florida Cybersecurity Standards) | Always; data classification drives hosting and access | planned |
| `fl-60gg-1-project-oversight` | Rule 60GG-1, F.A.C. | Engagement size crosses project-oversight thresholds | planned |
| `fl-668-50-ueta` | s. 668.50, F.S. (UETA) | Any step signs or executes a record electronically | planned |
| `fl-501-171-fipa` | s. 501.171, F.S. (breach notification) | Personal information in any system touched | planned |
| `fl-ch287-procurement` | Ch. 287, F.S.; Rule 60A-1, F.A.C. | Engagement packaging; category thresholds | planned |
| `fl-ai-disclosure` | HB 919 (2024) and later disclosure statutes | Any public-facing AI-generated output | planned |
| `nist-ai-rmf` | NIST AI RMF 1.0; NIST AI 600-1 | Agentic lane present | planned |
| `nist-800-53` | NIST SP 800-53 rev. 5 | Control mapping for FedRAMP / StateRAMP hosts | planned |
| `omb-m-25-21-22` | OMB M-25-21, M-25-22 | Federal funds flow through the process | planned |
| `hipaa` | HIPAA Privacy, Security and Breach rules; 42 CFR Part 2 where applicable | PHI in any system or message | page |
| `medicaid-431-subpart-f` | 42 CFR Part 431 Subpart F; s. 409.902-level state confidentiality | Medicaid applicant or recipient information | planned |
| `ferpa` | FERPA | Education records | planned |
| `cjis` | CJIS Security Policy | Criminal justice information | planned |
| `irs-pub-1075` | IRS Publication 1075 | Federal tax information | planned |
| `ada-title-ii-web` | ADA Title II web rule (WCAG 2.1 AA); HHS Section 504 rule | Any public-facing web or mobile output | planned |

## Four notes for the front page

1. **Public records is the sleeper.** The first real exposure is a records request for the agent's logs. Design for it and it becomes an asset.
2. **The due-process line is where agencies get sued.** An automated denial without a human decision and a stated basis is the fact pattern to avoid; the matrix makes it structurally impossible below L3.
3. **Exemptions are applied before output, not after.** Redaction sits in the output path of every recipe that produces anything a requester could ask for.
4. **Keep the legislative calendar.** April update pass; watch item for whatever AI bill returns in 2027.
