#!/usr/bin/env python3
"""
Re-register already-published Zenodo DOIs so DataCite ORCID Auto-Update picks them up.

THE PROBLEM THIS SOLVES. Works cannot be added to an ORCID record over the API:
that needs the ORCID Member API and the `/activities/update` scope, which only
paying member organisations get. The free route is DataCite Auto-Update — but it
fires only for DOIs **registered or updated after** you enable it, so records
minted earlier are never backfilled and simply never appear.

A metadata edit re-registers the DOI with DataCite, which makes an existing record
eligible. That is what this does: for each published record it opens an edit,
re-submits the SAME metadata, and republishes.

⚠️ ENABLE AUTO-UPDATE FIRST, or this achieves nothing. Sign in at
https://profiles.datacite.org, and next to "ORCID Auto-Update" choose
"Click to Enable", then authorise DataCite on the ORCID consent screen.
Only then run this.

WHAT IT DOES NOT DO. It does not create a new version, does not change any
metadata value, and does not touch files. The record keeps its DOI, its concept
DOI and its publication date. If a step fails mid-record the edit is DISCARDED
rather than left half-open — a record stuck in 'inprogress' is invisible to
DataCite, which would be a worse outcome than not running at all.

    export ZENODO_TOKEN=...
    ./scripts/zenodo-touch.py --dry-run
    ./scripts/zenodo-touch.py
"""

import argparse
import importlib.util
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("zd", ROOT / "scripts/zenodo-deposit.py")
zd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(zd)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sandbox", action="store_true")
    ap.add_argument("--only", metavar="SLUG")
    args = ap.parse_args()

    state_path = zd.STATE_SANDBOX if args.sandbox else zd.STATE_LIVE
    if not state_path.exists():
        raise SystemExit(f"no {state_path.name}; nothing has been deposited")
    state = json.loads(state_path.read_text())

    targets = {k: v for k, v in state.items()
               if v.get("published") and v.get("doi")
               and (not args.only or k == args.only)}
    print(f"{len(targets)} published record(s) to re-register\n")

    if args.dry_run:
        for slug, v in sorted(targets.items()):
            print(f"  would touch {v['doi']}  {slug}")
        print("\nDRY RUN — nothing sent. Enable auto-update at "
              "https://profiles.datacite.org BEFORE running for real.")
        return

    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        raise SystemExit("ZENODO_TOKEN is not set.")
    api = zd.Zenodo(token, args.sandbox)

    ok = failed = 0
    for slug, v in sorted(targets.items()):
        dep_id = v["deposition_id"]
        try:
            api._req("POST", f"/deposit/depositions/{dep_id}/actions/edit")
        except SystemExit as e:
            # Already open for editing is fine; anything else is not.
            if "403" not in str(e) and "400" not in str(e):
                print(f"  ✗ {slug}: could not open edit"); failed += 1; continue
        try:
            dep = api.get(dep_id)
            api.set_metadata(dep_id, dep["metadata"])   # unchanged, on purpose
            api.publish(dep_id)
            print(f"  ✓ {v['doi']}  {slug}")
            ok += 1
        except SystemExit:
            # Never leave a record open for editing: while 'inprogress' it is not
            # visible to DataCite at all.
            try:
                api._req("POST", f"/deposit/depositions/{dep_id}/actions/discard")
                print(f"  ✗ {slug}: failed, edit discarded")
            except SystemExit:
                print(f"  ✗✗ {slug}: FAILED AND STILL OPEN FOR EDITING — "
                      f"fix by hand at https://zenodo.org/deposit/{dep_id}")
            failed += 1
        time.sleep(0.4)      # be polite to the API

    print(f"\n{ok} re-registered, {failed} failed")
    print("DataCite propagation to ORCID is asynchronous — allow a day, then "
          "check https://orcid.org/0009-0009-4503-8575")


if __name__ == "__main__":
    main()
