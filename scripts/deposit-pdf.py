#!/usr/bin/env python3
"""
deposit-pdf.py — the PDF a Zenodo deposit carries beside its markdown (roadmap A421).

Founder 2026-10-16 ("Approve PDF"; memory project_publication_strategy §zenodo-pdf-10-16): every FIRST Zenodo deposit,
and every revision that already mints a version, uploads a PDF beside the markdown — so Zenodo serves Google Scholar's
`citation_pdf_url`. Never as a batch; never a version minted just for the file. One renderer for both corpora:
`TH/publications/scripts/zenodo-deposit.py` imports it, and `H3/publications/scripts/zenodo-deposit.py` runs it here.

    deposit-pdf.py PAPER.md --concept-doi DOI [--version-doi DOI] [--out DIR]

THE PDF IS A RENDER. The markdown stays the hashed original: its OpenTimestamps proof, the RFC 3161 manifests and
zenodo-dois.json's sha256 are the .md's, never this file's. So the PDF is built at deposit time from the same bytes,
never stored, and it must prove which bytes it renders. It refuses (exit 1, no PDF left behind) unless:
  1. the render loses no word of the markdown (the word-multiset diff on the HTML, as tdc-pdf.py does);
  2. the PDF's OWN extracted text loses no word of the markdown — tdc-pdf.py checks only its HTML, and a word can
     still be lost at print (a clipped line, a broken glyph);
  3. the PDF carries the markdown's SHA-256 in its metadata (XMP dc:source = "sha256:<hex>") and it reads back — so a
     stale PDF is caught by hash, never by eye (`check` below);
  4. the media stamp (IPTC compositeSynthetic, register M-0010, rights from the paper's licence) reads back with the
     page text unchanged.

    deposit-pdf.py --check PAPER.md FILE.pdf    exit 0 only if FILE.pdf declares PAPER.md's current SHA-256
"""
import argparse, hashlib, html as H, importlib.util, re, subprocess, sys, tempfile, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from md2html import convert, words  # noqa: E402

_spec = importlib.util.spec_from_file_location("tdc_pdf", HERE / "tdc-pdf.py")
tdc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tdc)  # CSS, CHROME, front_matter, MEDIA — shared, so the two PDFs look alike

REGISTER = "M-0010"
SOURCE = "composite"  # IPTC compositeSynthetic — ruled 2026-10-01 for corpus documents (never `enhanced`, never `ai`)

# The two corpora: where a paper is canonical, and where its timestamps are explained.
CORPORA = {
    "TH": {"canonical": "https://thonly.org/research/{slug}",
           "timestamps": "github.com/thonly/publications/blob/main/TIMESTAMPS.md"},
    "H3": {"canonical": "https://heartbank.net/{dir}/{slug}",
           "timestamps": "github.com/HeartBank/publications/blob/main/TIMESTAMPS.md"},
}
TYPE = {
    "defensive-publications": "Defensive publication",
    "essays": "Essay",
    "program": "Research program document",
    "positions": "Position",
    "white-papers": "White paper",
    "annual-reports": "Annual report",
}
# The licence a paper's front matter names → (cover words, stamp.py --rights).
LICENCE = {
    "CC0-1.0": ("CC0 1.0 Universal (public domain dedication)", "cc0"),
    "CC-BY (author-voice essay)": ("CC BY 4.0 — attribute to the author", "cc-by"),
}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def corpus_of(md):
    parts = md.resolve().parts
    for i in range(len(parts) - 1):
        if parts[i + 1] == "publications" and parts[i] in CORPORA:
            return parts[i]
    sys.exit(f"{md}: not under TH/publications or H3/publications")


def text_of(pdf):
    # -raw: the text in the order it was DRAWN. Chrome draws a table cell by cell; the default reading-order mode
    # interleaves cells, so a compound broken inside one cell lands lines apart (measured 2026-10-16: default lost 21
    # and 5 words on two papers, -raw lost 0 on all four tested).
    out = subprocess.run(["pdftotext", "-enc", "UTF-8", "-raw", str(pdf), "-"], capture_output=True, text=True, check=True)
    return unicodedata.normalize("NFKC", out.stdout)  # ﬁ → fi: a ligature is not a lost word


def visible(body):
    """The markdown as a reader sees it — the same normalisation tdc-pdf.py applies before its diff."""
    vis = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
    vis = re.sub(r'(?m)^(\s*)\d+\.\s', r'\1', vis)
    vis = re.sub(r'(?m)^(\s*```)\s*[\w+#.-]+\s*$', r'\1', vis)
    return unicodedata.normalize("NFKC", vis)


def joined(s):
    """Remove every hyphen (and the line break after one) before counting words, on BOTH sides. pdftotext rewrites
    hyphens at line ends unevenly — `weather-␤resistant` → `weatherresistant`, `peer-to-␤peer` → `peerto-peer`,
    `2026-09-␤28` → `2026-0928` — so a compound is compared as its letters and digits alone. Chrome never hyphenates
    (no CSS `hyphens`), so no hyphen in the PDF is one the markdown lacks. Found 2026-10-16 on the first test renders."""
    return re.sub(r"[-‐‑\u00ad]\s*", "", s)


INLINE = re.compile(r"</?(?:em|strong|code|a|sub|sup|b|i)\b[^>]*>")


def rendered_text(htm):
    """The render's text as print shows it: an INLINE tag leaves no gap (`<em>Kośa</em>'s` prints as `Kośa's`), a block
    tag does. Step 1 already proved the render keeps every word of the markdown; step 2 compares the PDF with this."""
    return unicodedata.normalize("NFKC", H.unescape(re.sub(r"<[^>]+>", " ", INLINE.sub("", htm))))


def declared_sha(pdf):
    out = subprocess.run(["exiftool", "-s", "-s", "-s", "-XMP-dc:Source", str(pdf)],
                         capture_output=True, text=True).stdout.strip()
    return out[len("sha256:"):] if out.startswith("sha256:") else None


def check(md, pdf):
    """A PDF matches its markdown only if it declares the markdown's CURRENT SHA-256."""
    want, got = sha256(md), declared_sha(pdf)
    if got != want:
        return f"{pdf.name} declares sha256 {got or '(none)'}; {md.name} is {want}"
    return None


def fail(pdf, msg):
    if pdf:
        Path(pdf).unlink(missing_ok=True)
    sys.exit(f"⛔ {msg} — no PDF written.")


def build(md, concept_doi, version_doi=None, out_dir=None):
    md = Path(md)
    raw = md.read_text(encoding="utf-8")
    fm, body = tdc.front_matter(raw)
    slug = fm.get("slug") or md.stem
    corpus, kind_dir = corpus_of(md), md.parent.name
    canonical = CORPORA[corpus]["canonical"].format(slug=slug, dir=kind_dir)
    lic = fm.get("license", "")
    if lic not in LICENCE:
        sys.exit(f"{md.name}: licence {lic!r} has no mapping here — add it deliberately (cover words + stamp rights)")
    lic_words, rights = LICENCE[lic]
    first = fm.get("date", "")[:10]
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", first):
        sys.exit(f"{md.name}: front matter `date:` is {first!r} — the cover states the first-publication date")
    revised = fm.get("revised", "")[:10]

    # 1. the render loses no word
    htm = convert(body)
    missing = words(visible(body)) - words(unicodedata.normalize("NFKC", htm))
    if missing:
        sys.exit(f"⛔ {sum(missing.values())} word(s) of the markdown missing from the render, e.g. "
                 f"{dict(list(missing.items())[:12])} — no PDF written.")

    e = lambda s: H.escape(s, quote=False)
    authors = fm.get("authors", "Thon Ly · Miss Aquarius")
    names = [n for n in (s.replace("℠", "").replace("®", "").strip() for s in re.split(r"[·,]", authors)) if n]
    if names == ["Miss Aquarius"]:
        if not fm.get("posed_by") or not fm.get("attested_by"):
            sys.exit(f"{md.name}: Miss Aquarius is its sole author, so it needs posed_by and attested_by")
        who = (f'<b>Author:</b> {e(authors)} &nbsp;<i>(the project\'s named AI substrate, disclosed; thesis posed by '
               f'{e(fm["posed_by"])}; the Pāli→Lean encoding attested by {e(fm["attested_by"])})</i>')
    elif "Miss Aquarius" in names:
        who = f'<b>Authors:</b> {e(authors)} &nbsp;<i>(Miss Aquarius is an AI co-author, disclosed)</i>'
    else:
        who = f'<b>Author{"s" if len(names) > 1 else ""}:</b> {e(authors)}'
    dated = f"<b>First published:</b> {first}"
    if revised and revised != first:
        dated += f" &nbsp;·&nbsp; <b>This version:</b> {revised}"
    kind = TYPE.get(kind_dir, kind_dir)
    if kind_dir == "defensive-publications" and fm.get("kind") == "study":
        kind = "Study"
    type_line = f"<b>Type:</b> {kind}"
    if kind == "Defensive publication":
        type_line += " — the authors assert no patent and dedicate the patterns to the public domain."
    doi_line = f"<b>Zenodo (concept DOI, every version):</b> https://doi.org/{concept_doi}"
    if version_doi:
        doi_line += f" &nbsp;·&nbsp; <b>this version:</b> https://doi.org/{version_doi}"
    ts = CORPORA[corpus]["timestamps"]
    cover = f"""<div class="tp">
<h1>{e(fm.get("title", slug))}</h1>
{f'<p class="sub">{e(fm["subtitle"])}</p>' if fm.get("subtitle") else ''}
<div class="meta">
{who}<br>
{dated}<br>
{doi_line}<br>
<b>Canonical:</b> {canonical}<br>
<b>Independent timestamps:</b> OpenTimestamps (Bitcoin) and RFC 3161 proofs of every version's markdown — {ts}.
<i>A timestamp proves this exact text existed no later than its date; it proves nothing about authorship, originality, or the validity of any claim. This PDF is a rendering of that markdown, whose SHA-256 it carries in its metadata.</i><br>
<b>Licence:</b> {lic_words}<br>
{type_line}
</div></div>
"""
    page = (f'<!doctype html><html><head><meta charset="utf-8"><title>{e(fm.get("title", slug))}</title>'
            f"<style>{tdc.CSS}</style></head><body>{cover}{htm}</body></html>")
    out_dir = Path(out_dir) if out_dir else Path(tempfile.mkdtemp(prefix="deposit-pdf-"))
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path, pdf = out_dir / f"{slug}.html", out_dir / f"{slug}.pdf"
    html_path.write_text(page, encoding="utf-8")
    subprocess.run([tdc.CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html_path.as_uri()], check=True, capture_output=True)
    html_path.unlink()
    if not pdf.exists() or pdf.stat().st_size < 10_000:
        fail(pdf, f"Chrome produced no usable PDF at {pdf}")

    # 2. the PDF itself loses no word
    printed = text_of(pdf)
    # the COVER is counted into what the PDF must hold, so the cover's own words cannot mask a word lost from the body
    lost = words(joined(rendered_text(cover + htm))) - words(joined(printed))
    if lost:
        fail(pdf, f"{sum(lost.values())} word(s) of the markdown are missing from the PDF's own text, e.g. "
                  f"{dict(list(lost.items())[:12])}")

    # 4. the media stamp, then 3. the source hash — each must read back, and the page text must not move
    r = subprocess.run(["python3", str(tdc.MEDIA / "scripts/stamp.py"), str(pdf), "--source", SOURCE,
                        "--rights", rights, "--credit", authors, "--disclosure", canonical,
                        "--register", REGISTER], capture_output=True, text=True)
    if r.returncode != 0:
        fail(pdf, f"the media stamp failed (exit {r.returncode}):\n{r.stdout}{r.stderr}")
    md_sha = sha256(md)
    r = subprocess.run(["exiftool", "-q", "-overwrite_original", f"-XMP-dc:Source=sha256:{md_sha}", str(pdf)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        fail(pdf, f"writing dc:source failed: {r.stderr}")
    got = subprocess.run(["exiftool", "-config", str(tdc.MEDIA / "exiftool.config"), "-s", "-s", "-s",
                          "-DigitalSourceType", "-XMP-ma:Register", str(pdf)],
                         capture_output=True, text=True).stdout.split()
    if not (got[:1] and got[0].endswith("/compositeSynthetic") and REGISTER in got):
        fail(pdf, f"the media stamp did not read back: {got}")
    if text_of(pdf) != printed:
        fail(pdf, "stamping moved the page text")
    bad = check(md, pdf)
    if bad:
        fail(pdf, bad)
    return pdf


# ── used by both corpora's zenodo-deposit.py ────────────────────────────────────────────────────────────────────────
def _prefix(sandbox):
    # Zenodo mints under 10.5281; the sandbox under 10.5072. ⚠️ A SANDBOX draft reports its reserved DOI under 10.5281
    # all the same (found 2026-10-16: the first rehearsal printed 10.5281/zenodo.621381 on a record minted as
    # 10.5072/zenodo.621381), so the prefix is never read off the draft.
    return "10.5072" if sandbox else "10.5281"


def concept_doi_for(dep, prev, sandbox=False):
    """The concept DOI to print on the cover. A revision has it already; a FIRST deposit's draft does not, so it is the
    draft's conceptrecid under the environment's prefix — checked against what Zenodo mints (`after_publish`)."""
    if prev and prev.get("concept_doi"):
        return prev["concept_doi"]
    crid = dep.get("conceptrecid")
    if not crid:
        sys.exit("⛔ the draft carries no conceptrecid — cannot print the cover's DOI. Nothing published.")
    return f"{_prefix(sandbox)}/zenodo.{crid}"


def version_doi_for(dep, sandbox=False):
    pre = dep.get("metadata", {}).get("prereserve_doi") or {}
    recid = pre.get("recid") or (pre.get("doi") or "").rsplit(".", 1)[-1]
    if not str(recid).isdigit():
        sys.exit("⛔ the draft carries no reserved record id — cannot print this version's DOI. Nothing published.")
    return f"{_prefix(sandbox)}/zenodo.{recid}"


def md5(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()


def verify_draft(api, dep_id, md, pdf):
    """Before publish: the draft holds EXACTLY the markdown and its PDF, byte for byte (Zenodo's md5), and the PDF
    declares the markdown's SHA-256. A new version starts as a copy of the last one's files, so this is also what
    catches a stale or stray file riding along."""
    files = {f.get("filename") or f.get("key"): (f.get("checksum") or "").removeprefix("md5:")
             for f in api.get(dep_id).get("files", [])}
    want = {Path(md).name: md5(md), Path(pdf).name: md5(pdf)}
    bad = check(Path(md), Path(pdf))
    if files != want or bad:
        sys.exit(f"⛔ draft {dep_id} is not exactly the paper and its PDF — NOT published, left for inspection.\n"
                 f"   draft: {files}\n   want:  {want}" + (f"\n   {bad}" if bad else ""))


def after_publish(rec, cover_concept, cover_version):
    """After publish: the DOIs Zenodo minted are the ones on the cover, and the landing page serves citation_pdf_url
    (the tag Google Scholar reads — the reason the PDF is there). Prints on STDOUT, in order with the rest (a stderr
    line jumped ahead of the buffered output and was cut off by a `tail` in the first rehearsal). Returns False on a
    mismatch, which the deposit run turns into a non-zero exit. It cannot unpublish."""
    import urllib.request
    ok = True
    for what, cover, minted in (("concept", cover_concept, rec.get("concept_doi")), ("version", cover_version, rec.get("doi"))):
        if minted != cover:
            print(f"   ⛔⛔ the cover prints {what} DOI {cover} but Zenodo minted {minted} — the PDF on this published "
                  "record is WRONG; correct it on the next version")
            ok = False
    url = rec.get("url")
    try:
        page = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "deposit-pdf"}), timeout=30)
        tag = 'name="citation_pdf_url"' in page.read().decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001 — a report
        print(f"   ⚠️ could not read {url} to check citation_pdf_url: {e}")
        return ok
    print(f"   {'✓ landing page serves citation_pdf_url' if tag else '⚠️ landing page does NOT serve citation_pdf_url'}")
    if ok:
        print(f"   ✓ the cover's DOIs are the minted ones ({cover_concept} · {cover_version})")
    return ok


def selftest(md):
    """The checks tested on known failures (A421 control): each must FAIL where it should, or a pass means nothing."""
    import shutil
    md = Path(md)
    tmp = Path(tempfile.mkdtemp(prefix="deposit-pdf-selftest-"))
    ok = True
    pdf = build(md, "10.5281/zenodo.0", None, tmp)
    print(f"ok   1. built and passed: {pdf.name} declares sha256 {declared_sha(pdf)[:16]}…")
    stale = tmp / md.name
    shutil.copy(md, stale)
    stale.write_text(stale.read_text(encoding="utf-8") + "\nA sentence added after the PDF was rendered.\n", encoding="utf-8")
    if check(stale, pdf):
        print("ok   2. a STALE PDF (the markdown changed after rendering) is refused by its hash")
    else:
        print("FAIL 2. a stale PDF passed the hash check"); ok = False
    fm, body = tdc.front_matter(md.read_text(encoding="utf-8"))
    htm = convert(body)
    clipped = re.sub(r"<p>.*?</p>", "", htm, count=1, flags=re.S)
    h, p2 = tmp / "clipped.html", tmp / "clipped.pdf"
    h.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{tdc.CSS}</style></head><body>{clipped}</body></html>',
                 encoding="utf-8")
    subprocess.run([tdc.CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={p2}", h.as_uri()],
                   check=True, capture_output=True)
    lost = words(joined(rendered_text(htm))) - words(joined(text_of(p2)))
    if lost:
        print(f"ok   3. a PDF missing one paragraph is refused: {sum(lost.values())} word(s) lost, e.g. {list(lost)[:4]}")
    else:
        print("FAIL 3. a PDF missing a paragraph passed the word check — the check is blind"); ok = False
    class Draft:  # a stand-in for the Zenodo API: only `get` is used
        def __init__(self, files):
            self.files = files

        def get(self, _):
            return {"files": self.files}
    good = [{"filename": md.name, "checksum": md5(md)}, {"filename": pdf.name, "checksum": "md5:" + md5(pdf)}]
    cases = {"the right two files": (good, True),
             "a stray file riding along": (good + [{"filename": "old.pdf", "checksum": "0"}], False),
             "a different PDF": ([good[0], {"filename": pdf.name, "checksum": "0" * 32}], False)}
    for name, (files, should_pass) in cases.items():
        try:
            verify_draft(Draft(files), 0, md, pdf)
            passed = True
        except SystemExit:
            passed = False
        good_result = passed == should_pass
        ok &= good_result
        print(f"{'ok  ' if good_result else 'FAIL'} 4. draft check, {name}: {'passed' if passed else 'refused'}")
    shutil.rmtree(tmp)
    sys.exit(0 if ok else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paper")
    ap.add_argument("pdf", nargs="?")
    ap.add_argument("--check", action="store_true", help="only check that PDF declares PAPER's current SHA-256")
    ap.add_argument("--concept-doi")
    ap.add_argument("--version-doi")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true", help="run the checks on known failures, using PAPER")
    a = ap.parse_args()
    if a.selftest:
        selftest(a.paper)
    if a.check:
        bad = check(Path(a.paper), Path(a.pdf))
        sys.exit(f"⛔ STALE: {bad}" if bad else 0)
    if not a.concept_doi:
        sys.exit("--concept-doi is required (a first deposit learns it from its draft)")
    print(build(a.paper, a.concept_doi, a.version_doi, a.out))


if __name__ == "__main__":
    main()
