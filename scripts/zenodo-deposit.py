#!/usr/bin/env python3
"""
Deposit corpus papers to Zenodo, one DOI per paper.

WHY PER-PAPER AND NOT PER-REPO. Zenodo's GitHub integration mints one DOI for a
whole release, which is right for software and wrong for a corpus: an examiner or
a citing author looks for *a paper*, not for a tarball that contains it. Per-paper
records are the discoverable unit. The repo-level route stays available through
.zenodo.json and the two do not conflict.

WHAT THIS ADDS THAT THE CORPUS DOES NOT ALREADY HAVE. Not prior art — the public
render plus the archive snapshots already do that job, and this is not an upgrade
path to it. What a DOI adds is a *third-party institutional registry* (CERN)
carrying the record, a persistent identifier that survives the site moving or
going down, and presence in the indexes academics actually search. It is
deliberately the smallest of the three timestamp/registry layers.

SAFETY. Publishing a DOI is IRREVERSIBLE — a Zenodo record cannot be deleted once
published, only versioned. So:

    (default)      dry run: print exactly what would be sent, touch nothing
    --create       create DRAFT depositions, still unpublished and deletable
    --publish      publish (mints the DOI). Refuses to run without --create too.
    --sandbox      talk to sandbox.zenodo.org instead — fake DOIs, free to break

Always rehearse on --sandbox first. The sandbox is a full copy of the API.

USAGE
    export ZENODO_TOKEN=...            # from zenodo.org/account/settings/applications
    ./scripts/zenodo-deposit.py --sandbox --create --publish        # rehearsal
    ./scripts/zenodo-deposit.py --create                            # real drafts
    ./scripts/zenodo-deposit.py --create --publish                  # real DOIs
    ./scripts/zenodo-deposit.py --only the-zero-employee-institution

State lives in zenodo-dois.json: slug -> {concept_doi, doi, deposition_id, sha256}.
A paper whose SHA-256 has changed since its last deposit is offered as a NEW
VERSION of the existing record rather than a new record, so the concept DOI keeps
resolving to the newest text and every earlier text keeps its own DOI.
"""

import argparse
import hashlib
import json
import mimetypes
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATE = ROOT / "zenodo-dois.json"
DIRS = {
    "defensive-publications": "preprint",
    "essays": "preprint",
}

# Miss Aquarius is listed as a creator deliberately, not as an oversight. The
# standing rule is that AI collaboration is disclosed openly and under the same
# name at every venue; dropping her here to look conventional would break the
# consistency that makes the disclosure meaningful.
#
# `cite_as` is "Family, Given" because that is what DataCite and every reference
# manager expect. Passing the display form "Thon Ly" would leave them to guess
# which half is the surname, and they guess wrong often enough to matter across a
# corpus this size. Family name confirmed as Ly against the ORCID registry.
CREATORS = {
    "Thon Ly": {
        "cite_as": "Ly, Thon",
        "affiliation": "Independent Researcher - Founder, HeartBank(R) - Kampot, Cambodia",
        "orcid": "0009-0009-4503-8575",
    },
    # No ORCID, and this is not an omission to fix later: ORCID identifies human
    # researchers and carries an assertion about a person. Minting or claiming one
    # for an AI co-author would misstate what the identifier certifies. The
    # disclosure is carried by the name, which is the standing convention.
    "Miss Aquarius": {
        "cite_as": "Miss Aquarius",
        "affiliation": "HeartBank(R) - AI co-author (disclosed)",
    },
}


# ── paper parsing ────────────────────────────────────────────────────────────
def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def abstract_of(text):
    m = re.search(r"^##\s+Abstract\s*\n(.*?)(?=^##\s)", text, re.S | re.M)
    body = m.group(1).strip() if m else ""
    # Zenodo renders a restricted HTML subset. Convert the little markdown that
    # actually appears in an abstract; leave everything else as plain text.
    body = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", body)
    body = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", body)
    paras = [p.strip().replace("\n", " ") for p in body.split("\n\n") if p.strip()]
    return "".join(f"<p>{p}</p>" for p in paras)


def keywords_of(text, fm):
    kws = []
    m = re.search(r"^\*\*Keywords:?\*\*\s*(.+?)$", text, re.M)
    if m:
        kws = [k.strip(" .") for k in m.group(1).split(",") if k.strip(" .")]
    for extra in (fm.get("category"), fm.get("priority")):
        if extra and extra not in kws:
            kws.append(extra)
    return kws[:50]


def build_metadata(path, text, fm, sha):
    slug = fm.get("slug") or path.stem
    title = fm.get("title") or slug
    subtitle = fm.get("subtitle")
    canonical = f"https://thonly.org/research/{slug}"
    raw = ("https://raw.githubusercontent.com/thonly/publications/main/"
           f"{path.parent.name}/{path.name}")

    desc = abstract_of(text) or f"<p>{title}</p>"
    if subtitle:
        desc = f"<p><em>{subtitle}</em></p>" + desc
    desc += (
        "<p><strong>Provenance.</strong> This paper is part of the THonly research "
        "corpus, dedicated to the public domain under CC0 1.0. The canonical "
        f'version is at <a href="{canonical}">{canonical}</a>. Its SHA-256 is '
        f"<code>{sha}</code>, independently timestamped to the Bitcoin blockchain "
        "via OpenTimestamps and signed under RFC 3161 by three trust authorities, "
        "one of them eIDAS-qualified.</p>"
        "<p><strong>AI co-authorship is disclosed.</strong> Miss Aquarius is the "
        "consistent name used for the AI collaboration across all venues.</p>"
    )

    creators = []
    for name in re.split(r"[·,]", fm.get("authors", "Thon Ly")):
        name = name.strip().replace("℠", "").replace("®", "").strip()
        if not name:
            continue
        known = CREATORS.get(name, {})
        c = {"name": known.get("cite_as", name),
             "affiliation": known.get("affiliation", "")}
        if known.get("orcid"):
            c["orcid"] = known["orcid"]      # bare ID, no URL — Zenodo rejects the URL form
        creators.append(c)

    meta = {
        "upload_type": "publication",
        "publication_type": DIRS.get(path.parent.name, "preprint"),
        "title": title,
        "creators": creators,
        "description": desc,
        "access_right": "open",
        "license": "cc-zero",
        "keywords": keywords_of(text, fm),
        "language": "eng",
        "related_identifiers": [
            {"identifier": canonical, "relation": "isIdenticalTo",
             "resource_type": "publication-preprint"},
            {"identifier": raw, "relation": "isSupplementedBy"},
        ],
        # The defensive-publication note is a claim about intent and must not be
        # attached to an essay, which makes no such claim.
        "notes": (
            ("Defensive publication. Published to establish prior art and to place "
             "the mechanism in the public domain; no patent is or will be sought. "
             if path.parent.name == "defensive-publications" else
             "Essay in the author's own voice, part of the THonly corpus. ")
            + f"Document SHA-256: {sha}"
        ),
    }
    if fm.get("date"):
        meta["publication_date"] = fm["date"]
    return meta


# ── Zenodo API ───────────────────────────────────────────────────────────────
class Zenodo:
    def __init__(self, token, sandbox):
        self.base = ("https://sandbox.zenodo.org/api" if sandbox
                     else "https://zenodo.org/api")
        self.token = token

    def _req(self, method, url, data=None, raw=None, ctype="application/json"):
        if not url.startswith("http"):
            url = self.base + url
        body = raw if raw is not None else (
            json.dumps(data).encode() if data is not None else None)
        req = urllib.request.Request(url, data=body, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        if body is not None:
            req.add_header("Content-Type", ctype)
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                payload = r.read()
                return json.loads(payload) if payload else {}
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:600]
            raise SystemExit(f"\nZenodo {method} {url} -> HTTP {e.code}\n{detail}\n")

    def create(self):
        return self._req("POST", "/deposit/depositions", data={})

    def new_version(self, dep_id):
        r = self._req("POST", f"/deposit/depositions/{dep_id}/actions/newversion")
        return self._req("GET", r["links"]["latest_draft"])

    def set_metadata(self, dep_id, meta):
        return self._req("PUT", f"/deposit/depositions/{dep_id}",
                         data={"metadata": meta})

    def upload(self, dep, path):
        bucket = dep["links"]["bucket"]
        ctype = mimetypes.guess_type(path.name)[0] or "text/markdown"
        return self._req("PUT", f"{bucket}/{urllib.parse.quote(path.name)}",
                         raw=path.read_bytes(), ctype=ctype)

    def publish(self, dep_id):
        return self._req("POST", f"/deposit/depositions/{dep_id}/actions/publish")


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--create", action="store_true",
                    help="actually create depositions (default is a dry run)")
    ap.add_argument("--publish", action="store_true",
                    help="publish them, minting real DOIs. IRREVERSIBLE.")
    ap.add_argument("--sandbox", action="store_true",
                    help="use sandbox.zenodo.org — rehearse here first")
    ap.add_argument("--only", metavar="SLUG", help="a single paper")
    ap.add_argument("--limit", type=int, help="stop after N papers")
    args = ap.parse_args()

    if args.publish and not args.create:
        raise SystemExit("--publish requires --create.")

    papers = sorted(p for d in DIRS for p in (ROOT / d).glob("*.md"))
    if args.only:
        papers = [p for p in papers if p.stem == args.only or
                  frontmatter(p.read_text()).get("slug") == args.only]
        if not papers:
            raise SystemExit(f"no paper matching slug {args.only!r}")

    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    token = os.environ.get("ZENODO_TOKEN")
    if args.create and not token:
        raise SystemExit("ZENODO_TOKEN is not set.")
    api = Zenodo(token, args.sandbox) if args.create else None

    new = revised = unchanged = 0
    done = 0
    for path in papers:
        if args.limit and done >= args.limit:
            break
        text = path.read_text()
        fm = frontmatter(text)
        slug = fm.get("slug") or path.stem
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        prev = state.get(slug)

        if prev and prev.get("sha256") == sha:
            unchanged += 1
            continue

        kind = "NEW VERSION of " + prev["doi"] if prev else "NEW record"
        meta = build_metadata(path, text, fm, sha)
        print(f"\n── {slug}\n   {kind}")
        print(f"   title    {meta['title'][:78]}")
        print(f"   authors  {', '.join(c['name'] for c in meta['creators'])}")
        print(f"   date     {meta.get('publication_date','(none)')}   "
              f"keywords {len(meta['keywords'])}   sha {sha[:16]}…")

        if not args.create:
            done += 1
            new += 0 if prev else 1
            revised += 1 if prev else 0
            continue

        if prev:
            dep = api.new_version(prev["deposition_id"])
            revised += 1
        else:
            dep = api.create()
            new += 1
        api.upload(dep, path)
        api.set_metadata(dep["id"], meta)

        rec = {"deposition_id": dep["id"], "sha256": sha,
               "doi": dep.get("metadata", {}).get("prereserve_doi", {}).get("doi")
                      or dep.get("doi") or "(unpublished draft)",
               "concept_doi": (prev or {}).get("concept_doi"),
               "sandbox": bool(args.sandbox)}

        if args.publish:
            pub = api.publish(dep["id"])
            rec["doi"] = pub.get("doi", rec["doi"])
            rec["concept_doi"] = pub.get("conceptdoi", rec["concept_doi"])
            rec["url"] = pub.get("links", {}).get("html")
            print(f"   ✅ published  DOI {rec['doi']}")
        else:
            print(f"   ✅ draft {dep['id']} created (not published)")

        state[slug] = rec
        STATE.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n")
        done += 1

    print(f"\n{'DRY RUN — nothing sent' if not args.create else 'done'}: "
          f"{new} new, {revised} revised, {unchanged} unchanged "
          f"({len(papers)} paper(s) scanned)")
    if not args.create:
        print("Re-run with --sandbox --create --publish to rehearse for real.")


if __name__ == "__main__":
    main()
