# Per-agency repos

Nothing agency-specific lives in the base toolkit. Each agency gets one private repository that vendors the base and adds its own layer: constraints, process cards, step tables, registry records, automation deployments, reports. One repo per agency, everything in it.

## Layout

```
<agency>-automation/
  toolkit/              # the base, vendored (git subtree), read-only here
  constraints.md        # agency hosting, identity, data classification and procurement constraints
  process-cards/        # one per process, from method/intake
  step-tables/          # one per process, from method/decision-matrix
  automations/<slug>/   # deployment config and any agency-specific code for one automation
  registry/
    automations/        # real registry records (schema and script come from toolkit/registry)
  reports/              # build reports, review reports
  field-notes/          # drafts before they are generalized and contributed upstream
  .github/workflows/    # copy of toolkit/.github/workflows/registry-calendar.yml, path adjusted
```

## Vendoring the base

```bash
git subtree add --prefix toolkit https://github.com/canopy-workshop/agency-automation-toolkit main --squash
# later
git subtree pull --prefix toolkit https://github.com/canopy-workshop/agency-automation-toolkit main --squash
```

Changes to the base are made upstream and pulled, never edited under `toolkit/`.

## Running the calendar from the agency repo

Copy `toolkit/.github/workflows/registry-calendar.yml` to `.github/workflows/` and point the script at the agency's records:

```yaml
run: python toolkit/registry/scripts/registry_to_issues.py --root registry
```

## What goes back upstream

Generalized method improvements, adapter fixes, controls corrections and field notes, under the base licenses and per the engagement's share-back clause. Process cards, step tables, registry records and reports never do.
