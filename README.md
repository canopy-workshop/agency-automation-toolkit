# Agency Automation Toolkit

Takes a state-agency manual process from "someone's inbox and spreadsheet" to a safe, documented automation, with the law, the records rules and the oversight level settled before any code runs. What it sells is upkeep: an agency can build most of these automations; what it cannot afford is keeping them running.

**Status:** scaffold, October 2026. Canon pages marked `canon: true` in their front matter have been reviewed; everything else is a stub to be filled by use.

## How it is organized

Every folder with a `SKILL.md` is an [Agent Skill](https://agentskills.io/). A person reads it as a wiki page; an agent loads it when a task matches its `description`. One source of truth: there is no separate wiki.

| Folder | What lives there |
| --- | --- |
| `method/` | How to run intake, write a process card, and route each step with the decision matrix |
| `capabilities/` | One skill per capability (mailbox, database, office docs, PDF, ...) organized by what it does, not by vendor |
| `adapters/` | The code for one backing technology under a capability: MCP servers, PowerShell modules, CLIs, with fixtures |
| `recipes/` | End-to-end patterns that chain capabilities (inbox-to-case-system, pdf-form-to-database, ...) |
| `controls/` | One skill per law, rule or standard: what triggers it, the checklist, the design constraint |
| `registry/` | The operations registry: schema, example record, and the script that turns records into calendar issues |
| `field-notes/` | What practitioners saw on real engagements; dated, attributed, append-only |
| `agencies/` | Not here. Per-agency material lives in that agency's private repo (see `agencies/README.md`) |

## Quick start: one process, end to end

1. Load `method/intake` and interview the people who do the process. Output: a process card (`method/intake/references/process-card.md`), stored in the agency repo.
2. Load `method/decision-matrix` and route every step: lane, oversight level, exception lane, owner. Output: the step table.
3. Pick the recipe that matches (or start one from `recipes/`) and fill its step table from yours.
4. Check which controls the card triggers (`controls/README.md`) and run their checklists.
5. Register the automation: copy `registry/automations/example-inbox-to-case.yaml`, fill it in, commit it to the agency repo. The calendar workflow opens issues for expiries, reviews and update windows from then on.

## Using it with an agent

Any client that supports Agent Skills can load these folders. In Claude Code, add this repo as a plugin or copy the skill folders you need into `.claude/skills/`. The skills assume the agent also has the capability adapters available as tools (MCP) or on the path (PowerShell, Python).

## Two repos

- **This repo** is the base: method, capabilities, adapters, recipes, controls, registry schema and scripts. Public.
- **One private repo per agency** vendors this one (`git subtree`) and adds the agency layer: process cards, step tables, registry records, deployment config, reports. See `agencies/README.md`.

## Rendering

GitHub renders every page as is, which is enough to start. For a site, MkDocs needs a `docs_dir` that is not the repo root; use the `mkdocs-same-dir` plugin or Docusaurus when the time comes.

## Licensing

Prose is CC BY-SA 4.0; code is MPL-2.0. See `LICENSE.md`, including the pre-existing IP statement for engagements.
