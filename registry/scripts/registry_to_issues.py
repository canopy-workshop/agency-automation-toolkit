#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
"""Open GitHub issues for upcoming registry events.

Reads every registry/automations/*.yaml, finds the events inside their lead
windows (credential expiry, scheduled review, scheduled update), and opens one
issue per event. Idempotent: an event's title carries the automation id and the
date, and an open issue with the same title is skipped.

Environment (set automatically inside GitHub Actions):
  GITHUB_TOKEN        token with issues: write
  GITHUB_REPOSITORY   owner/repo

Flags:
  --dry-run           print what would be opened, call nothing
  --as-of YYYY-MM-DD  pretend today is this date (for testing)
  --root PATH         registry folder (default: the folder above this script)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

import yaml

WINDOWS_DAYS = {"credential_expiry": 30, "review": 14, "update": 14}
BASE_LABEL = "registry"
LABEL_COLORS = {
    "registry": "0e8a16",
    "credential-expiry": "d93f0b",
    "review": "1d76db",
    "update": "fbca04",
}


def load_records(root: pathlib.Path):
    for path in sorted((root / "automations").glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        with path.open(encoding="utf-8") as fh:
            record = yaml.safe_load(fh) or {}
        record["_file"] = path.name
        yield record


def as_date(value) -> dt.date | None:
    if value in (None, "", "null"):
        return None
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        return None


def events_for(record: dict, today: dt.date) -> list[dict]:
    aid = record.get("id") or record["_file"].removesuffix(".yaml")
    owner = record.get("owner") or {}
    owner_line = owner.get("github") and f"@{owner['github']}" or owner.get("name", "unassigned")
    lane = f"{record.get('lane', '?')} / {record.get('oversight_level', '?')}"
    found: list[dict] = []

    for cred in record.get("credentials") or []:
        due = as_date(cred.get("expires"))
        if due and (due - today).days <= WINDOWS_DAYS["credential_expiry"]:
            found.append({
                "kind": "credential_expiry",
                "due": due,
                "title": f"[{aid}] credential expires {due}: {cred.get('name', 'credential')}",
                "body": (
                    f"Credential `{cred.get('name')}` ({cred.get('kind', 'unknown kind')}) for `{aid}` "
                    f"expires on **{due}**.\n\n"
                    f"- Rotate it (rotation owner: {cred.get('rotation_owner', 'unassigned')})\n"
                    f"- Update `expires` in the registry record\n"
                    f"- Confirm the next run completed clean\n\n"
                    f"Owner: {owner_line}"
                ),
                "labels": [BASE_LABEL, "credential-expiry"],
            })

    review = record.get("review") or {}
    due = as_date(review.get("next"))
    if due and (due - today).days <= WINDOWS_DAYS["review"]:
        found.append({
            "kind": "review",
            "due": due,
            "title": f"[{aid}] review due {due}",
            "body": (
                f"Scheduled {review.get('cadence', '')} review of `{aid}`.\n\n"
                f"1. Pull metrics for the period (volume, error rate, time saved, exceptions routed, human-queue age)\n"
                f"2. Compare against the current lane/level: {lane}\n"
                f"3. Record one decision in the registry record: `scale-up`, `keep`, or `wind-down`, with the evidence\n"
                f"4. Advance `review.next`\n\n"
                f"Owner: {owner_line}"
            ),
            "labels": [BASE_LABEL, "review"],
        })

    for upd in record.get("updates") or []:
        due = as_date(upd.get("next"))
        if due and (due - today).days <= WINDOWS_DAYS["update"]:
            found.append({
                "kind": "update",
                "due": due,
                "title": f"[{aid}] update window {due}: {upd.get('name', 'update')}",
                "body": (
                    f"Scheduled update `{upd.get('name')}` ({upd.get('cadence', '')}) for `{aid}` is due **{due}**.\n\n"
                    f"When done, advance `next` in the registry record.\n\nOwner: {owner_line}"
                ),
                "labels": [BASE_LABEL, "update"],
            })

    return found


class GitHub:
    def __init__(self, token: str, repo: str):
        self.token = token
        self.repo = repo

    def call(self, method: str, path: str, body: dict | None = None):
        req = urllib.request.Request(
            f"https://api.github.com/repos/{self.repo}{path}",
            method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "Content-Type": "application/json",
                "User-Agent": "registry-calendar",
            },
        )
        with urllib.request.urlopen(req) as resp:
            return json.load(resp) if resp.status != 204 else None

    def ensure_label(self, name: str):
        try:
            self.call("GET", f"/labels/{urllib.request.quote(name)}")
        except urllib.error.HTTPError as err:
            if err.code != 404:
                raise
            self.call("POST", "/labels", {"name": name, "color": LABEL_COLORS.get(name, "ededed")})

    def open_titles(self) -> set[str]:
        titles: set[str] = set()
        page = 1
        while True:
            items = self.call("GET", f"/issues?state=open&labels={BASE_LABEL}&per_page=100&page={page}")
            if not items:
                return titles
            titles.update(i["title"] for i in items if "pull_request" not in i)
            page += 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--as-of")
    parser.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parents[1]))
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.as_of) if args.as_of else dt.date.today()
    root = pathlib.Path(args.root)
    events = [e for rec in load_records(root) for e in events_for(rec, today)]
    events.sort(key=lambda e: e["due"])

    if not events:
        print(f"No registry events inside their windows as of {today}.")
        return 0

    if args.dry_run:
        for e in events:
            print(f"DRY  {e['due']}  {e['title']}")
        return 0

    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("GITHUB_TOKEN and GITHUB_REPOSITORY are required (or use --dry-run).", file=sys.stderr)
        return 2

    gh = GitHub(token, repo)
    for label in LABEL_COLORS:
        gh.ensure_label(label)
    existing = gh.open_titles()
    for e in events:
        if e["title"] in existing:
            print(f"skip {e['title']}")
            continue
        gh.call("POST", "/issues", {"title": e["title"], "body": e["body"], "labels": e["labels"]})
        print(f"open {e['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
