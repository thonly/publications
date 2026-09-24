#!/usr/bin/env python3
"""
check-mirrors.py — the property form of §the-mirror-revision-rule.

An examiner-facing venue (TDCommons) can neither version nor remove a posting. A defensive
publication protects only what it DISCLOSES, so when a mirrored paper gains NEW ENUMERATED CLAIMS,
a SECOND submission is owed. A prose revision owes nothing.

The rule keys on THE CLAIMS SECTION CHANGING, not the file changing — a different trigger from
/publish's, which fires on bytes. Remembering that at revision time is exactly what a human will
not do, so this script remembers it instead.

  check-mirrors.py                 check every manifest entry (exit 1 if anything is owed)
  check-mirrors.py --record SLUG --venue V --date YYYY-MM-DD|none --pdf FILE [--claims-heading '## H' ... | BODY]
  check-mirrors.py --ack SLUG --note "why no second submission is owed"
  check-mirrors.py --posted SLUG --date YYYY-MM-DD --url URL   the venue's live record, once it posts
  check-mirrors.py --selftest      run the controls: prove it can SEE a change, and a missing section

WHAT IT DOES NOT DO: decide. It narrows "something moved" to "these claims moved, here is the
diff". Whether the new matter is matter a claim RESTS on stays a human judgement.
"""
import argparse, hashlib, json, re, sys, difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DPUBS = ROOT / "defensive-publications"
SUBMITTED = DPUBS / "submitted"
MANIFEST = SUBMITTED / "manifest.json"

# The corpus names its claims section at least eleven ways: "## Claims", "## 8 · The Claims",
# "## 10 · Enumerated claims", "## 11 · What is claimed, and freed", "## 15. Summary of claimed
# contributions", and per-claim "## 4 · Claim 1 — ...". Match the lot; never match "disclaimer".
CLAIM_HEADING = re.compile(r"^##\s+(?!.*disclaim)(?=.*\bclaim)", re.I)
ANY_H2 = re.compile(r"^##\s+")

def body_of(md: str) -> str:
    parts = md.split("---")
    return "---".join(parts[2:]) if md.startswith("---") and len(parts) > 2 else md

def claim_sections(md: str, override=None):
    """[(heading, text)] for every ##-level claims section.

    `override` (stored per entry by --claims-heading) names the sections EXACTLY, for a paper whose
    claims sit under another heading (e.g. inside its Prior-Art statement); ["BODY"] fingerprints the
    whole body, for a paper with no enumerated claims at all — every text change then fires, which is
    the safe side: without a claims section, any sentence may be the disclosed matter."""
    if override == ["BODY"]:
        return [("BODY", body_of(md))]
    out, cur, buf = [], None, []
    for ln in body_of(md).split("\n"):
        if ANY_H2.match(ln):
            if cur is not None:
                out.append((cur, "\n".join(buf)))
            hit = (ln.strip() in override) if override else CLAIM_HEADING.match(ln)
            cur, buf = (ln.strip(), []) if hit else (None, [])
        elif cur is not None:
            buf.append(ln)
    if cur is not None:
        out.append((cur, "\n".join(buf)))
    return out

def words(s: str):
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"[*_#>|\[\]()`~-]+", " ", s)
    return re.findall(r"[0-9A-Za-zÀ-ỹ'’]+", s.lower())

def claims_fingerprint(md: str, override=None):
    secs = claim_sections(md, override)
    if override and override != ["BODY"] and len(secs) != len(override):
        return None, [], []                      # a named heading went missing: an ERROR
    if not secs:
        return None, [], []                      # absence is an ERROR, never a pass
    seq = []
    for h, t in secs:
        seq += words(h) + words(t)
    return hashlib.sha256(" ".join(seq).encode()).hexdigest(), seq, [h for h, _ in secs]

def load():
    return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {"entries": []}

def save(m):
    SUBMITTED.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")

def record(slug, venue, date, pdf, override=None):
    md = DPUBS / f"{slug}.md"
    if not md.exists():
        sys.exit(f"no such paper: {md}")
    fp, _, heads = claims_fingerprint(md.read_text(encoding="utf-8"), override)
    if fp is None:
        sys.exit(f"REFUSING: {slug} has no claims section this script can find — "
                 f"a mirror of a defensive publication without enumerated claims is the thing "
                 f"the venue exists to carry. Fix the paper or fix CLAIM_HEADING — or name the section "
                 f"with --claims-heading '## <exact heading>' (repeatable), or --claims-heading BODY.")
    m = load()
    old = next((e for e in m["entries"] if e["slug"] == slug), None)
    # A second submission is a second POSTING, not a replacement of the first: the venue keeps
    # both forever, so the manifest must too.
    prior = (old or {}).get("prior_postings", [])
    if old and old.get("url"):
        prior = prior + [{k: old[k] for k in ("submitted", "posted", "url", "claims_sha256") if k in old}]
    m["entries"] = [e for e in m["entries"] if e["slug"] != slug]
    m["entries"].append({
        "slug": slug, "venue": venue,
        "submitted": None if date in ("none", "", None) else date,
        "pdf": pdf, "claims_headings": heads, "claims_sha256": fp,
        **({"claims_heading_override": override} if override else {}),
        "body_sha256": hashlib.sha256(body_of(md.read_text(encoding="utf-8")).encode()).hexdigest(),
        **({"prior_postings": prior} if prior else {}),
    })
    m["entries"].sort(key=lambda e: e["slug"])
    save(m)
    print(f"recorded {slug}: {len(heads)} claims section(s), claims sha {fp[:12]}…")

def posted(slug, date, url):
    """Submission and posting are two dates: approval takes the venue a day or more."""
    if not (date and url):
        sys.exit("--posted needs --date (the venue's publication date) and --url (its live record)")
    m = load()
    for e in m["entries"]:
        if e["slug"] == slug:
            if not e.get("submitted"):
                sys.exit(f"{slug} was never recorded as submitted — --record it first")
            e["posted"], e["url"] = date, url
            save(m); print(f"posted {slug}: {date} {url}"); return 0
    sys.exit(f"{slug} is not in the manifest")

def ack(slug, note):
    """A judged claim-movement clears. RED means UNJUDGED movement, not movement."""
    if not note:
        sys.exit("--ack needs --note: the judgement is the point, and it is the thing a "
                 "future reader will need. Say why no second submission is owed.")
    md = DPUBS / f"{slug}.md"
    fp, _, heads = claims_fingerprint(md.read_text(encoding="utf-8"))
    if fp is None:
        sys.exit(f"REFUSING: {slug} has no findable claims section")
    m = load()
    for e in m["entries"]:
        if e["slug"] == slug:
            e.setdefault("judgements", []).append(
                {"date": __import__("datetime").date.today().isoformat(),
                 "from": e["claims_sha256"][:12], "to": fp[:12], "note": note})
            e["claims_sha256"] = fp
            e["claims_headings"] = heads
            e["body_sha256"] = hashlib.sha256(
                body_of(md.read_text(encoding="utf-8")).encode()).hexdigest()
            save(m); print(f"acknowledged {slug}: {note}"); return 0
    sys.exit(f"{slug} is not in the manifest")

def check(quiet=False):
    m = load()
    if not m["entries"]:
        print("manifest is empty — nothing mirrored yet"); return 0
    owed, errors = [], []
    for e in m["entries"]:
        md = DPUBS / f"{e['slug']}.md"
        if not md.exists():
            errors.append((e["slug"], "markdown is GONE")); continue
        text = md.read_text(encoding="utf-8")
        fp, seq, heads = claims_fingerprint(text, e.get("claims_heading_override"))
        if fp is None:
            errors.append((e["slug"], "claims section NO LONGER FOUND — renamed, or removed")); continue
        body_moved = hashlib.sha256(body_of(text).encode()).hexdigest() != e["body_sha256"]
        if fp == e["claims_sha256"]:
            if not quiet:
                state = "prose moved, claims did NOT" if body_moved else "unchanged"
                print(f"  ✅ {e['slug']}: {state} — nothing owed at the venue")
            continue
        owed.append((e, heads, seq))
    for e, heads, seq in owed:
        posted = e["submitted"]
        print(f"\n  ⛔ {e['slug']}: CLAIMS HAVE MOVED since the PDF was built")
        print(f"     venue: {e['venue']}  " + (f"submitted {posted}" if posted else "NOT YET SUBMITTED")
              + (f", posted {e['posted']} {e['url']}" if e.get("url") else ""))
        print(f"     sections now: {', '.join(heads)}")
        old = set(); new = set(seq)
        # we keep no baseline text, only its hash — so report shape, and point at git for the diff
        print(f"     → {'A SECOND SUBMISSION MAY BE OWED' if posted else 'REGENERATE THE PDF BEFORE SUBMITTING'}")
        if posted:
            print( "       The rule: a PROSE revision owes nothing; NEW ENUMERATED CLAIMS owe a second")
            print( "       submission, because the venue cannot version and prior art protects only")
            print( "       what a document disclosed, as of its date.")
            print(f"       JUDGE: did the revision add matter a claim now RESTS on?")
            print(f"       git diff -- defensive-publications/{e['slug']}.md")
            print(f"       THEN clear it, one way or the other:")
            print(f"         submitted again → --record {e['slug']} --date <today> --pdf <file>")
            print(f"         no new matter   → --ack {e['slug']} --note \"<why>\"")
    for slug, why in errors:
        print(f"\n  ‼️  {slug}: {why} — this is an ERROR, not a pass")
    if owed or errors:
        print(f"\n{len(owed)} paper(s) with moved claims · {len(errors)} error(s)")
        return 1
    print(f"\nall {len(m['entries'])} mirrored paper(s) clean")
    return 0

def selftest():
    """Test the instrument on a known failure — prefer the case that should FAIL."""
    ok = True
    sample = ("---\ntitle: x\n---\n\n## Preamble\n\nwords here\n\n"
              "## 10 · Enumerated claims\n\n1. **A claim** about a thing.\n\n## Honest limits\n\nlimits\n")
    fp1, _, heads = claims_fingerprint(sample)
    print(f"  control 1 — finds the section:            {'PASS' if heads == ['## 10 · Enumerated claims'] else 'FAIL'} {heads}")
    ok &= heads == ["## 10 · Enumerated claims"]

    reworded = sample.replace("about a thing", "about a DIFFERENT thing")
    fp2, _, _ = claims_fingerprint(reworded)
    print(f"  control 2 — a reworded claim FIRES:       {'PASS' if fp2 != fp1 else 'FAIL'}")
    ok &= fp2 != fp1

    reformatted = sample.replace("**A claim**", "*A claim*").replace("1. ", "1.  ")
    fp3, _, _ = claims_fingerprint(reformatted)
    print(f"  control 3 — pure FORMATTING does not:     {'PASS' if fp3 == fp1 else 'FAIL'}")
    ok &= fp3 == fp1

    prose = sample.replace("words here", "quite different words here")
    fp4, _, _ = claims_fingerprint(prose)
    print(f"  control 4 — PROSE outside claims does not:{'PASS' if fp4 == fp1 else 'FAIL'}")
    ok &= fp4 == fp1

    none = sample.replace("## 10 · Enumerated claims", "## 10 · Discussion")
    fp5, _, _ = claims_fingerprint(none)
    print(f"  control 5 — NO claims section is an ERROR:{'PASS' if fp5 is None else 'FAIL'}")
    ok &= fp5 is None

    dis = sample.replace("## 10 · Enumerated claims", "## 10 · Disclaimer")
    fp6, _, h6 = claims_fingerprint(dis)
    print(f"  control 6 — 'Disclaimer' is NOT a claim:  {'PASS' if fp6 is None else 'FAIL'} {h6}")
    ok &= fp6 is None
    print("\nselftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--record"); ap.add_argument("--venue", default="TDCommons, Defensive Publications Series")
    ap.add_argument("--date"); ap.add_argument("--pdf")
    ap.add_argument("--ack"); ap.add_argument("--note")
    ap.add_argument("--posted"); ap.add_argument("--url")
    ap.add_argument("--claims-heading", action="append", help="exact ## heading holding the claims (repeatable), or BODY")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    if a.selftest: sys.exit(selftest())
    if a.ack:      sys.exit(ack(a.ack, a.note) or 0)
    if a.posted:   sys.exit(posted(a.posted, a.date, a.url) or 0)
    if a.record:   sys.exit(record(a.record, a.venue, a.date, a.pdf, a.claims_heading) or 0)
    sys.exit(check(a.quiet))
