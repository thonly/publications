#!/usr/bin/env python3
"""
mirror-lint.py — what must never reach a TDCommons posting, checked before its packet is built.

A posting can be neither versioned nor removed, and it is read by patent examiners. Wave 1
(2026-09-23) found, in papers already public on the site and Zenodo: draft banners, perma.cc
citations (the venue was retired 2026-09-05), "Mirrors of this document … arXiv, IP.com" lines
naming venues we never deposited at, and novelty language with no census behind it.

  mirror-lint.py SLUG [SLUG ...]   lint these papers (exit 1 if any REFUSE)
  mirror-lint.py --all             every defensive publication, one summary line each
  mirror-lint.py --selftest        the controls: each rule must fire on a planted case

REFUSE — the paper is revised before it is mirrored:
  draft-banner · perma-cc · false-mirror · placeholder
WARN — a human reads each hit (never a refusal, because a regex cannot tell scope):
  novelty — "novel", "revolutionary", "unprecedented", "first to", "no X in the world"…
            A hit on a line that states its aperture ("not found in … on <date>") is skipped.
  therapeutic — a treatment/clinical-use statement; a disclosed USE is fine in a defensive
            publication, a health OUTCOME claim is not.
"""
import re, sys
from pathlib import Path

DPUBS = Path(__file__).resolve().parent.parent / "defensive-publications"

REFUSE = {
    "draft-banner": re.compile(r"\*\*Draft in progress\.?\*\*|founder-voice canonical draft", re.I),
    "perma-cc": re.compile(r"perma\.cc", re.I),
    "false-mirror": re.compile(r"mirrors? of this document", re.I),
    "placeholder": re.compile(r"\b(TODO|TBD|FIXME)\b|to be computed|\[placeholder\]"),
}
WARN = {
    "novelty": re.compile(
        r"\b(novel|novelty|revolutionary|unprecedented|first to|first-ever|"
        r"never (before )?(been|existed)|no (other )?[\w-]+ (product |system )?in the world)\b", re.I),
    "therapeutic": re.compile(
        r"\b(therapeutic(ally)?|treat(s|ing|ment)?|cure[sd]?|clinical(ly)?)\b.{0,60}"
        r"\b(anxiety|ptsd|depression|insomnia|disorders?|addiction|trauma)\b|"
        r"\b(anxiety|ptsd|depression|insomnia|disorders?|addiction|trauma)\b.{0,140}"
        r"\b(therapeutic(ally)?|treat(s|ing|ment)?|cure[sd]?)\b", re.I),
}
SCOPED = re.compile(r"not (found|located) in|census|aperture", re.I)


def lint_text(text):
    body = text.split("---", 2)[2] if text.startswith("---") else text
    lines = body.splitlines()
    off = len(text.splitlines()) - len(lines)
    out = []
    in_fence = False
    for i, ln in enumerate(lines, start=off + 1):
        if ln.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        for k, rx in REFUSE.items():
            if rx.search(ln):
                out.append(("REFUSE", k, i, ln.strip()))
        if in_fence:
            continue
        for k, rx in WARN.items():
            if rx.search(ln) and not (k == "novelty" and SCOPED.search(ln)):
                out.append(("WARN", k, i, ln.strip()))
    return out


def lint(slug):
    return lint_text((DPUBS / f"{slug}.md").read_text(encoding="utf-8"))


def selftest():
    cases = {
        "draft-banner": "> **Draft in progress.** This is the founder-voice canonical draft.",
        "perma-cc": "archived at perma.cc/ABCD-1234",
        "false-mirror": "Mirrors of this document appear at GitHub, arXiv, IP.com.",
        "placeholder": "SHA-256: to be computed at publication",
        "novelty": "This composition is genuinely novel.",
        "therapeutic": "It can address anxiety disorders therapeutically.",
    }
    ok = True
    for rule, line in cases.items():
        hit = {k for _, k, _, _ in lint_text("x\n" + line + "\n")}
        ok &= rule in hit
        print(f"  {'✓' if rule in hit else '✗'} {rule} fires on its planted case")
    clean = lint_text("x\nNot found in Google Patents on 2026-09-23; this composition is novel within that aperture.\n")
    ok &= not clean
    print(f"  {'✓' if not clean else '✗'} a scoped novelty line does not fire")
    fenced = lint_text("x\n```\nnovel treatment for anxiety\n```\n")
    ok &= not fenced
    print(f"  {'✓' if not fenced else '✗'} WARN rules skip fenced code")
    return ok


def main(argv):
    if "--selftest" in argv:
        sys.exit(0 if selftest() else 1)
    slugs = sorted(p.stem for p in DPUBS.glob("*.md") if p.name != "README.md") if "--all" in argv \
        else [a for a in argv if not a.startswith("--")]
    if not slugs:
        sys.exit(__doc__)
    refused = 0
    for s in slugs:
        hits = lint(s)
        r = [h for h in hits if h[0] == "REFUSE"]
        refused += bool(r)
        if "--all" in argv:
            kinds = sorted({f"{h[0][0]}:{h[1]}" for h in hits})
            print(f"{'REFUSE' if r else ('warn  ' if hits else 'clean ')}  {s:52} {' '.join(kinds)}")
            continue
        print(f"== {s}: {len(r)} refuse, {len(hits) - len(r)} warn")
        for lvl, k, i, ln in hits:
            print(f"  {lvl:6} {k:13} L{i}: {ln[:150]}")
    sys.exit(1 if refused else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
