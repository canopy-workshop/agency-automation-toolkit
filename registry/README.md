# Operations registry

The registry answers the question agencies actually have, which is not "can we automate this?" but "who keeps it running?" One YAML record per automation, a schema to validate it, and a script that turns the dates in those records into GitHub issues on a schedule. The calendar is the issues list.

## Where records live

- **This repo** holds the schema, the script, the workflow, and one example record. 
- **The agency repo** holds the real records under `registry/automations/`, and runs the workflow. Records name owners and service accounts, so they stay with the agency.

## Record

See `automations/example-inbox-to-case.yaml` and `schema/automation.schema.json`. The fields, and why each is there:

| Field | Why it is tracked |
| --- | --- |
| `owner` | Nothing runs without a named person; the first thing an auditor asks |
| `credentials[]` with `expires` | Service accounts, scopes and expiry: the most common silent failure, and it goes on the calendar |
| `runtime` | Language, host, scheduler: what a maintainer needs on day one |
| `process_card`, `recipe` | Requirements source and the pattern it implements |
| `lane`, `oversight_level`, `exception_lane` | From the matrix; every change carries evidence |
| `controls[]`, `records` | Which checklists apply; where the log is and its retention series |
| `metrics` | Volume, error rate, time saved, exceptions routed, human-queue age: the earned-autonomy evidence |
| `updates[]` with `next` | Dependency patching, adapter upgrades, the April controls review |
| `review` with `next` and `last_decision` | Calendar-driven; ends in one of three decisions |
| `history[]` | Dated decisions and level changes |

## Review decisions

Every review ends in exactly one: `scale-up`, `keep`, or `wind-down`, recorded with the metrics that drove it. Over time the records are the budget request: volumes, error rates and time saved are already measured when the agency asks for the larger system.

## The calendar

`scripts/registry_to_issues.py` reads every record and opens one issue per upcoming event inside its lead window:

| Event | Lead window | Labels |
| --- | --- | --- |
| Credential expiry | 30 days | `registry`, `credential-expiry` |
| Scheduled review | 14 days | `registry`, `review` |
| Scheduled update | 14 days | `registry`, `update` |

Idempotent: issue titles carry the automation id and the date; an open issue with the same title is not duplicated. Closing the issue is the record that the work was done; the `next` date in the record is then advanced by pull request.

`.github/workflows/registry-calendar.yml` runs it weekly and on any push that touches `registry/automations/`.

Try it locally:

```bash
pip install pyyaml
python registry/scripts/registry_to_issues.py --dry-run --as-of 2027-01-10
```
