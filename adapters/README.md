# Adapters

An adapter is the code for one backing technology under one capability. Each ships in up to three forms, because agencies have three kinds of users:

- an **MCP server** for agents
- a **PowerShell module** or **Python CLI** for the deterministic lane and for admins who will never run an agent
- **fixtures**: synthetic data to prove it works before any real access is granted

## Layout

```
adapters/<name>/
  README.md          # what it talks to, auth model, scopes, install
  mcp/               # MCP server (TypeScript or Python)
  pwsh/              # PowerShell module (optional)
  cli/               # Python CLI (optional)
  fixtures/          # synthetic mailbox / database / documents / PDFs
  tests/
```

## Rules

- **Read-only by default.** Every write is a separate, named tool with its own grant, called explicitly by a recipe behind an approval hook.
- **Fork, harden, vendor.** Community MCP servers exist for Microsoft 365, Graph and SQL Server and are a starting point. Quality is uneven; read the source, pin and vendor every dependency, keep the server small enough for an agency security reviewer to read in an afternoon.
- **Logging is built in.** Every tool call writes who, what, why, input hash and output hash to the records log before it returns.
- **License: MPL-2.0** (file-level share-alike), chosen for code that ships inside agency deliverables.

## Planned P1 adapters

| Adapter | Capability | Notes |
| --- | --- | --- |
| `m365-graph-mail` | mailbox | Application access policy scoped to one mailbox |
| `exchange-ews` | mailbox | On-prem Exchange; EWS impersonation or Exchange PowerShell |
| `mssql` | database | Read via views; writes via approved stored procedures only |
| `openxml-docs` | office-docs | python-docx / openpyxl; templates with content controls |
| `pdf-tools` | pdf | pypdf, pdfplumber, Tesseract; AcroForm fill and flatten |
| `entra-identity` | identity | Service principals, scope inventory, expiry export for the registry |
| `model-gateway` | model-gateway | One config for Azure Government, Bedrock GovCloud, on-prem |
