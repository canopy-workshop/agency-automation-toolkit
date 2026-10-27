# Capabilities

Organized by what the agency needs done, not by vendor. "Read a mailbox" is one capability; Exchange on-prem over EWS, Microsoft 365 over Graph, and a shared mailbox through Outlook are adapters under it. That is what makes "regardless of the backing technology" true in practice.

## The capability contract

Every `capabilities/<name>/SKILL.md` has the same sections, so an agent and a person both know where to look:

1. **When to use** (the front-matter `description`, kept specific)
2. **Adapters**: a table of the technologies an agency may run, with the adapter folder, status and auth model
3. **Read tools and write tools**, listed separately. Read-only by default; every write is a separate, named tool that a recipe must call explicitly and that runs behind an approval hook at L2 or higher
4. **Logging**: what every call records to the records log before it returns (who, what, why, input hash, output hash, timestamp)
5. **Controls it triggers**: which `controls/` pages apply whenever this capability is in a recipe
6. **Fixtures**: the synthetic data the adapter ships with, so an agency can see it work before granting real access
7. **Field notes**

## Catalog

| Capability | Adapters an agency may run | Priority | Status |
| --- | --- | --- | --- |
| `mailbox` | Exchange on-prem (EWS, Exchange PowerShell); Microsoft 365 (Graph); shared mailboxes | P1 | stub |
| `database` | SQL Server, Oracle, DB2, PostgreSQL, Access (ODBC) | P1 | planned |
| `office-docs` | OpenXML (python-docx, openpyxl, Open XML SDK); Graph for SharePoint/OneDrive; COM only where desktop Office exists | P1 | planned |
| `pdf` | pypdf, pdfplumber, Tesseract or Azure Document Intelligence (gov cloud), AcroForm fill | P1 | planned |
| `identity` | Entra ID and on-prem AD service principals, scoped Graph permissions, expiring delegated access | P1 | planned |
| `model-gateway` | Azure OpenAI in Azure Government, Bedrock in GovCloud, Anthropic via Bedrock or Vertex, on-prem (vLLM, Ollama) | P1 | planned |
| `files` | Graph, CSOM, SMB shares | P2 | planned |
| `scheduling` | Windows Task Scheduler, cron, Power Automate, GitHub Actions, n8n | P2 | planned |
| `line-of-business` | API where one exists; otherwise RPA (Power Automate Desktop, UiPath) or browser automation with a human watching | P2 | planned |
| `legacy-terminal` | tn3270 and tn5250 libraries, screen-scrape | P3 | planned |

P1 is capped until one recipe runs end to end at an agency.
