# Contributing

Two kinds of content live here, and they are kept apart on purpose.

| | Canon | Field notes |
| --- | --- | --- |
| What it is | Tested method, capabilities, adapters, recipes, controls | What one practitioner saw on one engagement |
| Bar to enter | A fixture or a checklist, a named maintainer, review | The template below, filled in |
| Changes | Versioned; breaking changes announced | Append-only; corrections are new notes |
| Agent loads it | Yes, by description match | Only when a canon page links to it |

## Field notes

Open an issue with the **Field note** template or add a file under `field-notes/<year>/<slug>.md` by pull request. Dated, attributed, append-only. The template:

```markdown
---
date: YYYY-MM-DD
author: <name or handle>
agency_type: <health | revenue | licensing | education | general>  # never the agency name without permission
touches: [method/intake, capabilities/mailbox]  # canon pages this note bears on
---

## Context
What the process was, roughly, and what the stack looked like.

## What we did
## What broke
## What we would do differently
```

Nothing identifying a person, a case, or a record goes in a field note. If in doubt, generalize.

## Promotion to canon

A field note is promoted into the canon page it touches, with credit, when either:

- two or more engagements cite it, or
- it turns into a fixture, a test, or a checklist item.

Every canon page ends with a **Field notes** section listing the notes that bear on it, so the practitioner voice is one click from the accelerator.

## Canon changes

Pull request, one reviewer, and the page's fixture or checklist updated in the same change. Front matter carries `version`; bump the minor version for additions, the major version for anything that changes how an agent would act.

## Advisory circle

Five to eight people (two agency IT leads, a records management liaison officer, an agency general counsel, two practitioners from outside Canopy Road) review promotions quarterly. They do not gate field notes.

## Licensing of contributions

By contributing you license prose under CC BY-SA 4.0 and code under MPL-2.0 (see `LICENSE.md`).
