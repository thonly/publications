#!/usr/bin/env python3
"""
tdc-pdf.py — build the PDF a defensive publication is mirrored to TDCommons with.

TDCommons postings can neither be versioned nor removed, so the PDF is permanent the moment it is
uploaded. This script exists so that it is built the same way every time, from the repo, and not
from a session scratchpad (where the first two were made, and where the converter nearly vanished).

  tdc-pdf.py SLUG                 build into a temp dir and print the path (the default)
  tdc-pdf.py SLUG --submitted     build into defensive-publications/submitted/ — refused if that
                                  slug was already submitted (the submitted bytes are evidence)
  tdc-pdf.py SLUG --html-only     stop after the HTML, for a look before printing

What the cover carries, and why each line is there (roadmap A168):
  · FIRST publication date — the paper's own `date:`, never `revised:`. TDCommons dates the posting
    on the day it posts; this line is what lets an examiner cite the EARLIER date.
  · the Zenodo concept DOI — an independent, resolvable record of that date.
  · the timestamp line WITH its scope limit (src/attestation.ts in thonly.org) — a timestamp proves
    a date, never authorship or validity.
  · the canonical URL as https://thonly.org/research/<slug> — the form that resolves. (The first
    posting printed /publications/defensive-publications/<slug>, a soft 404, now a 301.)

Refuses to print if the rendered text loses any word of the markdown (the word-multiset diff).
Warns — never refuses — when the title leads with a coined mark: TDCommons search reads titles and
abstracts only, and an examiner searches standard terms, never ours.
"""
import argparse, html as H, json, re, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md2html import convert, words  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DPUBS = ROOT / "defensive-publications"
SUBMITTED = DPUBS / "submitted"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TIMESTAMPS_URL = "github.com/thonly/publications/blob/main/TIMESTAMPS.md"

CSS = """
@page { size: Letter; margin: 22mm 18mm; }
body { font: 10.5pt/1.5 "Charter","Georgia",serif; color:#111; }
.tp { border-bottom:2px solid #111; padding-bottom:14px; margin-bottom:22px; }
.tp h1 { font-size:19pt; line-height:1.25; margin:0 0 8px; }
.tp .sub { font-size:10.5pt; font-style:italic; color:#333; margin:0 0 12px; }
.tp .meta { font-size:9pt; color:#333; line-height:1.7; }
h1,h2,h3,h4 { font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; page-break-after:avoid; }
h2 { font-size:13pt; margin:22px 0 8px; border-bottom:1px solid #ccc; padding-bottom:3px; }
h3 { font-size:11pt; margin:16px 0 6px; }
p { margin:0 0 9px; text-align:justify; }
pre { font:8.2pt/1.32 "SF Mono",Menlo,Consolas,monospace; background:#f6f6f6;
      border:1px solid #ddd; padding:9px; white-space:pre; overflow:visible;
      page-break-inside:avoid; border-radius:3px; }
code { font:9pt "SF Mono",Menlo,monospace; background:#f2f2f2; padding:1px 3px; border-radius:2px; }
blockquote { margin:10px 0 10px 14px; padding-left:12px; border-left:3px solid #bbb; color:#333; }
table { border-collapse:collapse; width:100%; font-size:9pt; margin:10px 0; page-break-inside:avoid; }
th,td { border:1px solid #bbb; padding:5px 7px; text-align:left; vertical-align:top; }
th { background:#f0f0f0; }
ul,ol { margin:0 0 9px 18px; padding:0; } li { margin:0 0 4px; }
a { color:#111; text-decoration:none; border-bottom:1px dotted #999; }
hr { border:0; border-top:1px solid #ddd; margin:16px 0; }
"""


def front_matter(raw):
    if not raw.startswith("---"):
        sys.exit("no front matter")
    _, fm, body = raw.split("---", 2)
    out = {}
    for ln in fm.splitlines():
        m = re.match(r'^([A-Za-z_]+):\s*(.*)$', ln)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out, body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--submitted", action="store_true")
    ap.add_argument("--html-only", action="store_true")
    a = ap.parse_args()

    if a.submitted:
        manifest = json.loads((SUBMITTED / "manifest.json").read_text())
        done = [x for x in manifest["entries"] if x["slug"] == a.slug and x.get("submitted")]
        if done:
            sys.exit(f"{a.slug} was submitted {done[0]['submitted']} — its PDF is evidence and is never "
                     "rebuilt in place. A second submission (new claims) is built without --submitted "
                     "and recorded with check-mirrors.py --record.")

    md = DPUBS / f"{a.slug}.md"
    if not md.exists():
        sys.exit(f"{md} not found — defensive publications only (A168 scope)")
    fm, body = front_matter(md.read_text(encoding="utf-8"))

    # what must never reach a permanent posting — mirror-lint.py, REFUSE rules (wave 1, 2026-09-23)
    import importlib.util as _u
    _sp = _u.spec_from_file_location("mirror_lint", Path(__file__).resolve().parent / "mirror-lint.py")
    _ml = _u.module_from_spec(_sp); _sp.loader.exec_module(_ml)
    _hits = _ml.lint(a.slug)
    _ref = [h for h in _hits if h[0] == "REFUSE"]
    if _ref:
        sys.exit(f"mirror-lint REFUSES {a.slug} — revise the paper first:\n" +
                 "\n".join(f"  {k} L{i}: {ln[:120]}" for _, k, i, ln in _ref))
    for _, k, i, ln in _hits:
        print(f"⚠️  mirror-lint {k} L{i} (read it): {ln[:120]}", file=sys.stderr)

    first = fm.get("date", "")[:10]
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", first):
        sys.exit(f"front matter `date:` is {first!r} — the first-publication date is the cover's point")
    revised = fm.get("revised", "")[:10]
    dois = json.loads((ROOT / "zenodo-dois.json").read_text())
    rec = dois.get(a.slug) or {}
    concept = rec.get("concept_doi")
    if not concept or not rec.get("published"):
        sys.exit(f"{a.slug} has no published Zenodo deposit — the mirror comes AFTER the first deposit")

    title = fm.get("title", a.slug)
    if re.search(r"[℠™®]|\bB-[A-Z]", title.split(":")[0]):
        print(f"⚠️  the title LEADS with a coined mark: {title!r}\n"
              "    TDCommons search reads titles and abstracts only; lead with the standard terms an "
              "examiner would type, the mark second.", file=sys.stderr)

    htm = convert(body)
    vis = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
    # an ordered-list marker renders as <ol> numbering, not as text — not a lost word
    vis = re.sub(r'(?m)^(\s*)\d+\.\s', r'\1', vis)
    # a code fence's language tag (```javascript) is markup, never page text
    vis = re.sub(r'(?m)^(\s*```)\s*[\w+#.-]+\s*$', r'\1', vis)
    missing = words(vis) - words(htm)
    if missing:
        sys.exit(f"word-multiset diff: {sum(missing.values())} word(s) of the markdown are missing "
                 f"from the render — refusing to print. e.g. {dict(list(missing.items())[:15])}")

    e = lambda s: H.escape(s, quote=False)
    dated = f"<b>First published:</b> {first}"
    if revised and revised != first:
        dated += f" &nbsp;·&nbsp; <b>This version:</b> {revised}"
    cover = f"""<div class="tp">
<h1>{e(title)}</h1>
{f'<p class="sub">{e(fm["subtitle"])}</p>' if fm.get("subtitle") else ''}
<div class="meta">
<b>Authors:</b> {e(fm.get("authors", "Thon Ly · Miss Aquarius"))} &nbsp;<i>(Miss Aquarius is an AI co-author, disclosed; the inventor of record is Thon Ly)</i><br>
{dated}<br>
<b>Zenodo (concept DOI, every version):</b> https://doi.org/{concept}<br>
<b>Canonical:</b> https://thonly.org/research/{a.slug}<br>
<b>Independent timestamps:</b> OpenTimestamps (Bitcoin) and RFC 3161 proofs of every version's text — {TIMESTAMPS_URL}.
<i>A timestamp proves this exact text existed no later than its date; it proves nothing about authorship, originality, or the validity of any claim.</i><br>
<b>Licence:</b> CC0 1.0 Universal (public domain dedication)<br>
<b>Type:</b> Defensive publication — the authors assert no patent and dedicate the patterns to the public domain.
</div></div>
"""
    page = (f'<!doctype html><html><head><meta charset="utf-8"><title>{e(title)}</title>'
            f"<style>{CSS}</style></head><body>{cover}{htm}</body></html>")

    if a.submitted:
        out_dir = SUBMITTED
    else:
        out_dir = Path(tempfile.mkdtemp(prefix="tdc-"))
    html_path = out_dir / f"{a.slug}.html"
    html_path.write_text(page, encoding="utf-8")
    if a.html_only:
        print(html_path); return

    pdf = out_dir / f"{a.slug}.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html_path.as_uri()],
                   check=True, capture_output=True)
    if a.submitted:
        html_path.unlink()  # only the PDF is evidence; the HTML is a build step
    if not pdf.exists() or pdf.stat().st_size < 10_000:
        sys.exit(f"Chrome produced no usable PDF at {pdf}")
    print(pdf)
    print("next: read it (every page, the cover above all) before it goes anywhere — "
          "the upload is permanent.", file=sys.stderr)


if __name__ == "__main__":
    main()
