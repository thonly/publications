---
title: "The Borrowable Standard"
subtitle: "Why a corpus that must be authoritative in its own language cannot normalise toward someone else's — and what that made of one man's work in Cambodia between 1929 and 1969."
authors: "Thon Ly · Miss Aquarius"
category: alignment
priority: tier-b
status: draft
date: 2026-08-28
revised: 2026-09-05
license: CC0-1.0
slug: the-borrowable-standard
venue: thonly.org/research/the-borrowable-standard (canonical)
---

> **Draft in progress.** ⚠️ **A note on category, recorded rather than hidden:** this paper fits none
> of the corpus's four categories cleanly. It is a history-of-infrastructure argument in support of an
> alignment corpus, filed under `alignment` because that is what it serves. It is **not** an essay,
> and putting it there would have placed a scholarly claim in the founder's personal voice.
>
> ⚠️ **One set of cases is flagged for verification** and is marked in the text: the comparison cases
> in §8, which are named as *the class this claim is testable against* rather than as established
> support. (The CODA citation of §5.2 was verified at the 2026-09-05 revision.) **§8's cases have not been
> checked.** The paper's own §4 exists because an unchecked assumption was checked and failed.

---

## Preamble

A commission ordained in Phnom Penh in December 1929 translated the Pāli canon into Khmer, translating
from 1930; the last of a hundred and ten volumes was printed at the end of 1968, and the work was
celebrated in the capital on the first two days of April 1969. The man who had led it died that September. The man who succeeded him
was executed six years later, on the second day of the Khmer Rouge's occupation of the city, at a
pagoda in the district where he had been born.

This paper is not about that. It is about a smaller thing the same man did, which almost nobody
records, and without which the translation would not today be machine-readable at all: **he
standardised how Khmer is written.**

The argument below began as a stronger and simpler claim — that a canonical digital corpus requires
a stabilised orthography — and that claim is false. §4 shows why, using the counterexamples that
refute it. What survives is narrower, and it is the reason the Cambodian case is not an instance of
a general pattern but an exception to the way the general pattern is usually solved.

---

## Prior-Art and Non-Assertion Statement

This document is dedicated to the public domain under CC0 1.0 Universal. ⚠️ **Unlike most papers in
this corpus, it specifies no *novel* mechanism — the operating rules in §7.6 restate textual-scholarship
practice for AI corpora — and makes no patentable claim**; this section is present for
scholarly prior art rather than for defensive publication, and the author asserts no patent over
anything described.

**The literature this paper stands on, and does not claim to originate:**

- **Language planning.** Haugen's four-stage model — *selection · codification · elaboration ·
  acceptance* (1966; the 1983 revision reads *implementation*) — is the frame within which everything
  here sits. What Chuon Nath performed is **codification** in Haugen's sense, and this paper claims no
  new theory of codification; the two-layer account of §7 is an observation about what codification
  does not settle.
- ⭐ **Kloss's (1969) distinction between *corpus planning* (the form of a language) and *status
  planning* (its social position).** ⚠️ **A terminological warning the reader is owed immediately: "corpus" in
  the language-planning sense and "corpus" in the computational sense are different words.** This
  paper argues that *corpus planning* in Kloss's sense is a precondition for a *corpus* in the NLP
  sense, and the pun is unfortunate but the connection is real.
- **Low-resource NLP and dialect processing** — the Swiss German and dialectal Arabic literature
  that §4 uses against this paper's own first formulation.
- **Script encoding.** The Unicode Khmer block (U+1780–U+17FF), and the general problem of legacy
  8-bit font encodings preceding it.

**No claim of priority is made over any of the above.** The contribution offered is in §6 and §7: a
distinction between corpora that may normalise toward a borrowed standard and corpora that may not,
and a two-layer account of what standardisation does and does not buy.

---

## Abstract

It is widely assumed, and rarely stated, that digitising a language is a tooling problem — better
optical character recognition, better fonts, better models. This paper argues that for one class of
corpus it is not, and that the constraint is upstream of any tool.

We begin from a claim that turns out to be **false**: that a machine-readable corpus requires the
language to have a standardised orthography. Swiss German and the Arabic dialects refute it. Both
lack standardised spelling; both have substantial corpora, speech systems, machine translation and
dedicated benchmarks. Corpora can be and are built for languages whose spelling is unsettled.

**What the refutation reveals is the mechanism by which those corpora are possible: they normalise
toward a standard the variety itself does not have.** Swiss German normalises to Standard German.
Dialectal Arabic normalises to Modern Standard Arabic, or to a convention created for the purpose.
The corpus is *about* the variety and *encoded* in a target borrowed from elsewhere.

That move is available to most languages and unavailable to a specific and important minority: **a
corpus that must be authoritative in its own language cannot normalise toward another.** A Khmer
canonical text rendered in Thai orthography is not a Khmer witness to anything; it is a Thai
rendering, and the distinction is the entire content of a critical apparatus. For such corpora,
**native standardisation is a genuine precondition, because the borrowing that substitutes for it is
disqualified by what the corpus is for.**

We then examine the Cambodian case, which is unusual in that the precondition has a name, a date and
a documented programme. Between the 1930s and 1967 Chuon Nath led the standardisation of Khmer
orthography, compiled the dictionary that fixed its lexicon, and led the translation of the canon
into it. ⭐ **But the case also contains its own counterexample, and this is the paper's second
contribution: standardisation is necessary and not sufficient.** Khmer's orthographic layer was
settled by the 1960s; its **encoding** layer was not, and the volumes this project transcribes carry
**five mutually incompatible legacy font encodings in a single book**, one of them apparently custom
and undocumented. Seventy years separate the solution of the first layer from the ongoing repair of
the second.

We state the claim in falsifiable form, name the comparison class against which it should be tested,
and concede three limits — including that standardisation was contested, that its politics are not
innocent, and that this paper is not an argument for it.

---

## 1 · Why a corpus project is asking a question about spelling

This paper is a by-product of building something. The institution publishing it is assembling a
machine-readable Khmer witness to the Pāli canon — the Cambodian recension, entered into a critical
apparatus that collates Sinhalese, Siamese and PTS readings against its Burmese base text, in which
the Cambodian witness is sparse and the Cambodian edition has no page concordance at all (§7.5).

The work is not textual scholarship for its own sake. It exists because an alignment programme needs
a **value corpus whose every claim resolves to a citation** — work, edition, locus, and the lineage
by which that edition is attested. A system that cannot name where a judgment comes from is a system
whose judgments cannot be checked, and checkability is the only property that survives its author.

That requirement is what made spelling a first-class problem rather than an implementation detail.
**A citation is a promise that a reader can go and look.** If the text a reader would find is
spelled differently from the text the system indexed — not *wrongly*, but under a different
convention — the promise fails silently, and it fails in a way no amount of retrieval engineering
repairs.

### 1.1 · The shape of the problem, before any of it was about spelling

The requirement arrived from the other end. An alignment programme wanted a values model whose every
judgment resolves to a citation — and that requirement, pursued honestly, decomposes:

```
   "every judgment cites its source"
        │
        ├─ the source must be IDENTIFIED        → work, edition, locus
        ├─ the identification must be CHECKABLE → a reader can go and look
        └─ what the reader finds must be        → and here the requirement
           the same text the system indexed        stops being about software
```

The first two are engineering. **The third is not**, and it is where a project discovers that its
corpus has a history it did not choose. A citation into a text encoded under a different orthographic
convention from the one a reader will consult is a citation that resolves to a *different object* —
and no part of the system can detect that, because every component is behaving correctly.

⭐ **This paper is therefore a report from the point where an infrastructure question surfaced inside
a values question**, which is a more common pattern than the literature suggests and is almost never
written up, because by the time anyone notices, the decision was made by someone else and is
someone else's field.

⚠️ **The bounded ambition, stated so the reader can hold us to it:** this paper does not argue that
standardisation is good, that Cambodia's case is representative, or that anything follows for
languages in general. It identifies a **precondition for one class of corpus**, exhibits a case where
that precondition has a documented author, and says what would falsify the claim.

---

## 2 · The claim, stated precisely

> **For a corpus that must be authoritative in its own language, native orthographic standardisation
> is a precondition — because the substitute that makes other corpora possible, normalising toward a
> borrowed target, is disqualified by what such a corpus is for.**

Three terms are doing work.

**"Authoritative in its own language"** means the corpus is not merely *about* the language but is
required to *be* a witness in it — such that a reader, a scholar or a court could treat the encoded
text as standing for what the source says. Canonical religious texts, statutes, treaties and
critical editions are of this kind. A sentiment-analysis dataset is not.

**"Native"** distinguishes standardisation of the language itself from adoption of a neighbour's:
codified for this language by its own users, whatever institution convened them. An **adequate**
borrowable target is a neighbour's standard whose forms the variety's readers accept as a rendering
of their own language; and a corpus is **authoritative** when a scholar or a court would treat the
encoded text as standing for the source.

**"Precondition"** is stronger than *helpful* and weaker than *sufficient*. §7 is devoted to the
gap between those two. *The claim is stated in its strong form because that is the form worth
attacking (§3); §9.4.1 records what the evidence can and cannot separate.*

```
        ┌────────────────────────────────────────────────────────────┐
        │  IS THE CORPUS REQUIRED TO BE A WITNESS IN ITS OWN         │
        │  LANGUAGE?                                                  │
        └────────────────────────────────────────────────────────────┘
                    │                                │
                   NO                               YES
                    │                                │
                    ▼                                ▼
        ┌───────────────────────┐      ┌────────────────────────────┐
        │  BORROWING AVAILABLE  │      │  BORROWING DISQUALIFIED    │
        │  normalise toward a   │      │  the borrowed target IS    │
        │  neighbouring standard│      │  the thing being witnessed │
        │  (Swiss German → DE,  │      │  against — a Khmer canon   │
        │   dialects → MSA)     │      │  in Thai orthography is a  │
        │                       │      │  Thai rendering            │
        │  ⭐ corpus possible    │      │  ⛔ native standard         │
        │     WITHOUT a native  │      │     REQUIRED               │
        │     standard          │      │                            │
        └───────────────────────┘      └────────────────────────────┘
```

### 2.1 · What "authoritative" is doing, since the whole claim turns on it

The distinction is between a corpus that is **about** a body of text and a corpus that **is** an
instance of it, such that a third party may reason from the encoding as they would from the source.

| | corpus **about** | corpus **as witness** |
|---|---|---|
| Question it answers | *what do texts of this kind look like?* | *what does THIS text say, here?* |
| Tolerates normalisation | **yes** — often requires it | ⛔ **no** |
| Tolerates silent regularisation | yes | ⛔ no |
| A wrong character is | noise, absorbed by scale | ⛔ **a false reading, propagated as fact** |
| Recoverable from the encoding | the phenomenon | ⛔ **the source itself** |

**Sentiment corpora, language-identification sets and most training data are of the first kind, and
this paper says nothing about them.** Statutes, treaties, contracts of record, critical editions and
canonical religious texts are of the second. ⭐ **The population is small, old, and disproportionately
consequential** — and it is exactly the population an AI system needs when it is asked to say what a
tradition, a law or a contract actually holds.

⚠️ **One clarification the reader is owed: "authoritative" here is a claim about the ENCODING's
relationship to a source, not about the source's own authority.** Whether the Cambodian recension is
*correct* is not this paper's business; whether an encoding of it is *that recension* is.

---

## 3 · The claim we started with, and why it is worth showing

The first formulation was: **a machine-readable canon requires a stabilised orthography.** It is
clean, it matched the Cambodian evidence, and it is wrong.

⭐ **We report it because the manner of its failure is the paper's method.** The claim was tested
adversarially before drafting — not by looking for cases that supported it, but by looking for the
case that would kill it. The case exists, it was found in an afternoon, and the thesis that replaced
it is narrower, more useful and falsifiable in a way the original was not.

*A claim that has not been hunted is a claim whose supporting cases were selected.*

---

## 4 · The counterexample: corpora do get built without standardised spelling

**Swiss German has no standardised orthography.** Writers spell dialectally and inconsistently; there
is no official codification of the written form. It nonetheless has a substantial resource
ecosystem — dialect corpora assembled from text messages and from archival speech, corpora with
annotated normalisation and part-of-speech tagging, parallel multidialectal speech corpora, and
speech-to-text corpora at scale.

**The Arabic dialects are the same case at greater scale.** Egyptian, Levantine and Gulf varieties
lack standard orthographies and are predominantly spoken, and there is a long research literature on
tagging, translating and modelling them regardless.

There is even a dedicated benchmark literature on evaluating machine translation **for dialects
without standard orthography** — which is a field admitting, in its own title, that the condition is
normal and workable.

### 4.1 · What the literature actually reports, since the detail matters for §5

Three features recur across that work, and all three are consistent with the reading offered in §5
rather than with orthographic standardisation being irrelevant.

**Normalisation appears as an explicit annotation layer, not as a preprocessing convenience.**
Dialect corpora are built with a normalised form recorded *alongside* the dialectal transcription,
which is the practice of a field that knows the two are different objects and needs both.

**Spelling variation is treated as a first-class research problem** rather than as noise to be
absorbed — dedicated work on dialect variation dictionaries, on mining variant spellings from social
media, and on evaluating translation quality where no reference orthography exists.

**And evaluation itself becomes contested.** There is benchmark work specifically on *how to evaluate
machine translation for dialects without standard orthography*, which is a field acknowledging that
the absence of a standard breaks the measurement instrument, not merely the training data.

⭐ **None of that is a field working comfortably without standardisation. It is a field managing its
absence, at cost, by leaning on a standard next door.**

⛔ **So the strong claim is refuted, and this paper does not attempt to rescue it.** Corpora can be
built for languages whose spelling is unsettled. Anyone asserting otherwise is contradicted by a
decade of published work.

---

## 5 · What those projects actually do — and it is not "cope with variation"

The interesting question is not *whether* they succeed but *how*, and the answer is consistent
across both families.

### 5.1 · They normalise toward a standard the variety does not have

Swiss German resources largely normalise to **Standard German** (the SwissText 2021 shared task;
SDS-200; Aepli et al. 2023). Corpora carry an explicit
normalisation layer alongside the dialectal transcription; speech corpora are built as *Swiss German
speech → Standard German text*. The dialect is the **source**; the standard is the **target**.

Dialectal Arabic normalises to **Modern Standard Arabic**, which occupies the same structural
position — a written standard, universally taught, not natively spoken in the relevant sense, and
available to normalise toward.

```
   DIALECT           →      NORMALISATION      →      ENCODED FORM
   (no standard)            layer                     (a standard the
                                                       dialect does not
   Swiss German      →   map to Standard German  →     itself have)
   Egyptian Arabic   →   map to MSA / convention →
   Khmer canon       →   ??? ────────────────────────▶ ⛔ nothing to map to
```

⭐⭐ **The standard is not dispensed with. It is borrowed.** The corpus is possible because a
codified target exists nearby, not because codification turned out to be unnecessary.

### 5.2 · And where nothing adequate exists to borrow, they build one

The dialectal-Arabic research community, finding MSA an imperfect target for dialectal forms,
developed **CODA**, a conventional orthography for dialectal Arabic (Habash, Diab & Rambow 2012) —
created deliberately, its authors state, because dialectal Arabic has no standard orthography: a
standard built where none could be borrowed.

⭐⭐⭐ **It is the strongest available support for this paper's thesis, and it comes from the
community that refutes the paper's first version.** Faced with no adequate borrowable
target, the response was **not to abandon standardisation but to perform it** — decades later, by
different people, for exactly the reason argued here.

---

## 6 · Why a canonical text cannot borrow

Borrowing has a cost, and for most corpora it is acceptable.

**Normalising Swiss German to Standard German discards the dialect.** The corpus becomes a record
*about* a variety, encoded in another. For machine translation, speech recognition and most
downstream tasks this is not merely tolerable but desirable: the standard form is what the
application needs.

⛔ **For a corpus required to be a witness, the same move destroys the thing being built.**

Consider the concrete case. The Cambodian recension of the Pāli canon differs from the Burmese in
readings — that difference is precisely what a critical apparatus records, and precisely what a
Khmer witness would contribute to an apparatus that currently has none. Now normalise it toward a
neighbouring standard. **What has been encoded is no longer a Khmer witness.** It is a rendering, and
a rendering inherits the lineage of what it was rendered *into*, not what it was rendered *from*.

### 6.1 · ⭐⭐⭐ Normalisation and collation are inverse operations

The mechanism deserves stating exactly, because it explains why the loss is total rather than
partial.

**A critical apparatus records differences between witnesses.** That is its entire function: at
locus *Z*, witness *K* reads *X* where witness *M* reads *Y*. The value of a new witness is precisely
the differences it contributes.

**Normalisation is the operation that removes differences.** It maps variant forms onto a canonical
form so that downstream processing sees one thing where the source had several. That is why it works
so well for the corpora of §4 — variation is noise there, and removing it is the point.

```
   COLLATION                          NORMALISATION
   ─────────                          ─────────────
   preserves difference               removes difference
   output: an apparatus               output: a canonical form
   value ∝ variation retained         value ∝ variation eliminated

   ⛔ Running the second before the first destroys the input to the first.
```

⛔⛔ **So normalisation that *replaces* the source form with a borrowed standard, and then collates,
is not lossy — it is empty.** A normalisation kept as a second column beside the retained source
form — the reading-and-witness structure the TEI critical-apparatus module provides — is collation's
*input*, not its destroyer. The disqualifying move is the replacement, and it is the move the
tractable pipelines make by default. The differences that would have constituted the witness were
removed by the step that made the corpus tractable. **The apparatus that results records the differences between normalisation artefacts, not
between traditions.**

⭐ **And this is why the failure is invisible.** A collation run on normalised text produces output.
It has entries. It looks like an apparatus. Nothing in the pipeline reports that the input was
pre-flattened — because normalisation is not an error, it is a successful operation that was simply
inappropriate here.

⭐ **This is not a subtle point and it has an ugly failure mode: the rendering looks correct.** It is
readable, it is in a recognisable script, and it corresponds passage-for-passage to the source. It
simply attests nothing. A project that mistakes one for the other produces a corpus that is confident
and empty — and if that corpus is then used to ground a system's claims about what a tradition says,
the error propagates into every judgment the system emits.

**So the general pattern — borrow a target — is available to most corpora and closed to this one.
Where it is closed, the precondition it substituted for returns.**

---

## 7 · The Cambodian case, in two layers

The case is unusual not because standardisation happened — it happens often — but because it happened
**recently, in one documented programme, with a named leader**, and because the corpus it enabled is
still being built by people who can read the primary sources. Most standardisations are reconstructed
by historians. This one has living successors.

⚠️ **And it contains its own counterexample, which is the more useful half.**

### 7.1 · Layer one — the orthographic layer, settled

Chuon Nath (1883–1969) was Sangharāja of the Mahānikāya and led the reformist current within it, the
**Thommakay**, against the traditionalist **Thommaboran**. The reform had two commitments that matter
here: **direct study of the Pāli source** rather than doctrine received through tradition, and
**adoption of modern tooling**, the printing press above all.

⭐⭐ **Those two commitments are usually listed as separate modernising sympathies. We read them as
one commitment** — an interpretation, not a documented motive. *Go and read the source yourself* is an instruction that cannot be given to a community
whose sources exist as individually hand-copied palm-leaf manuscripts — not because people cannot
read, but because **there is no shared object to point at.** Two readers consulting two manuscripts
are not consulting the same text, and neither can correct the other by reference to it.

**The printing press is what turns *go and read it* from an exhortation into an instruction.** Mass
identical reproduction creates the shared object that makes source-primacy actionable, and it is why
a reform grounded in direct study of the canon needed a press rather than merely welcoming one.

⭐ *That logic is worth pausing on, because it recurs. A commitment to checkability generates a demand
for whatever technology makes the checked thing identical across checkers — and each time that
technology arrives, it brings a new standardisation problem with it. The press required a settled
orthography. Digital encoding required a settled character set. Neither requirement was visible until
the technology made it binding.*

Within that programme he did three things which are usually described separately and are better
understood as one:

| | |
|---|---|
| **The translation** | the Tipiṭaka Commission, 1929–1968, 110 volumes |
| **The dictionary** | first published 1938; definitive edition 1967 |
| **The orthography** | standardisation of Khmer writing — layout, symbols, punctuation |

⭐ **These are not three achievements. They are one achievement with three faces**: you cannot
translate a canon into a vernacular without deciding what its words mean, and you cannot print the
result without deciding how they are written. **The three programmes ran together and each forced
revisions in the others** — the orthographic decisions began in a 1926 committee before the
Commission was ordained in 1929, the dictionary was under way before its 1938 first edition, and
its definitive edition (1967) postdates most of the translation it stabilises. The dependency is
mutual, not one-way.

⭐⭐ That is worth stating carefully, because it converts an observation about a remarkable individual
into something a person can act on: **convergent contributions of this kind arise from attempting one
thing and refusing to leave its preconditions unbuilt.**

```
        PALM LEAF   ──────▶   METAL TYPE   ──────▶   DIGITAL FONT   ──────▶  UNICODE
        manuscript            printing press          8-bit legacy           U+1780–17FF
        practice              ▲                       encodings
                              │
                    ORTHOGRAPHIC LAYER
                    standardised here
                    (≈1930s–1967)
                                                      ▲
                                            ENCODING LAYER
                                            NOT standardised —
                                            ~70 years of divergence
```

### 7.1.1 · ⭐⭐ There is a third layer, and it is the one usually left implicit

This paper has argued two layers. The Cambodian case exhibits three, and the middle one is the
easiest to overlook because it does not look like infrastructure.

```
   ┌───────────────────────────────────────────────────────────────────┐
   │  LEXICAL LAYER      what the words MEAN        the dictionary      │
   │  ORTHOGRAPHIC LAYER how they are WRITTEN       the standard        │
   │  ENCODING LAYER     how they are STORED        Unicode / legacy    │
   └───────────────────────────────────────────────────────────────────┘
        each can be settled or unsettled independently of the others
```

**A translation into a vernacular is not well-defined until the vernacular's terms are.** Rendering a
technical Pāli vocabulary — *saṅkhāra*, *upādāna*, *paṭicca-samuppāda* — into Khmer requires deciding
what the Khmer terms will mean, and those decisions are only stable if they are recorded somewhere a
later reader can consult. **The dictionary is that record**, and its 1967 edition postdates most of
the translation it stabilises.

⭐⭐⭐ **Which produces a fact this project depends on operationally, not just historically: the
dictionary is the TRANSLATOR'S OWN LEXICON.** It is not a general reference that happens to be
Khmer. It is the semantic key to the translation choices in the very edition being transcribed,
compiled by the person who led the making of them.

**For a Pāli↔Khmer parallel corpus that is a rare instrument.** Where a Khmer term renders a Pāli one,
the *intended* gloss is available rather than inferred — and where legacy-font extraction yields a
damaged near-word, a lexicon of the same register and period — 17,328 entries by our transcription's count of the
1967 edition; published counts differ by edition and by what is counted as an entry — is a far better
disambiguator than a modern general dictionary.

⚠️ **The layers can be borrowed independently, and this is where the §5 pattern generalises.** A
project can borrow an encoding (adopt Unicode), borrow an orthography (normalise to a neighbour), or
borrow a lexicon (gloss through a third language). ⛔ **Each borrowing is disqualifying for a witness
for the same reason, and the third is the least visible** — a corpus glossed through English or Thai
carries those languages' semantic joints into a text that did not have them.

### 7.2 · Layer two — the encoding layer, unsettled for decades

Standardising how a language is *written* does not standardise how it is *stored*. Between the metal
type and Unicode sits a period in which Khmer was set digitally using **legacy 8-bit fonts that mapped
Khmer glyphs onto Latin codepoints** — a general phenomenon for non-Latin scripts before Unicode
adoption, and an acute one for Khmer.

The volumes this project transcribes exhibit it directly. **A single volume, in the volumes this
project holds, embeds five distinct font encodings** — a Limon-family face, `APSARA`, `ThoeunA1`, `TacteingA`, and `Bidokk1`, the last
apparently cut for this edition and, so far as we can determine, undocumented. Extracting text yields
Latin character sequences that are not Latin words:

```
   extracted:  brmtßeCatika Gdækfa kfaBN’naéRtsrN³
   intended:   បរមត្ថជោតិកា អដ្ឋកថា ...          (Paramatthajotikā aṭṭhakathā)
```

**Recovery requires a per-font transcoding table**, applied per text-run, and the transcoding is
lossy in font-dependent ways at exactly the points where Khmer orthography is most structured — the
subscript *coeng* clusters and the reordering vowels. A second body of material, born-digital and
carrying a genuine Unicode text layer, fails differently: subscripts dropped, vowels detached from
their bases, and **Private Use Area codepoints** where glyphs were never mapped at all.

⚠️ **These are two different repairs and must not be assumed to be one pipeline.** The first is a
font-transcoding problem; the second is a glyph-reordering and PUA-recovery problem.

### 7.3 · What the two layers together actually show

⭐⭐⭐ **Standardisation is necessary and not sufficient**, and the Cambodian case demonstrates both
halves at once:

- **Necessary**, because the transcoding tables of §7.2 are only *well-defined* against a target
  orthography. A legacy encoding can be mapped to Unicode because there is a determinate correct
  answer to map to. **Without layer one, layer two has no destination**, and the repair is not merely
  hard but undefined.
- **Not sufficient**, because layer one was settled by 1967 and layer two is still being paid for in
  2026. Roughly **seventy years** separate them.

**The general shape, stated for reuse:** standardising a language's *form* and standardising its
*digital representation* are distinct acts that can be separated by generations, and a project that
inherits the first without the second inherits a well-defined problem rather than a solved one. ⭐
*That is a better position than an ill-defined problem, and it is not the same as being finished.*

### 7.6 · What follows operationally, for anyone building such a corpus

The argument has consequences that are cheap to adopt and expensive to retrofit. They are stated
here as rules rather than as findings, and none of them is novel in textual scholarship; the
contribution is only that they bind for AI training corpora too.

| | Rule | Because |
|---|---|---|
| **1** | ⛔ **Never normalise before collating.** | §6.1 — the operations are inverse; the second destroys the first's input. Textual scholarship's practice: the TEI critical-apparatus module keeps every reading. |
| **2** | ⛔ **Record the encoding provenance per text run**, not per document: which font, which transcode table, which version. | §7.2 — a volume carries several, and the mapping is font-dependent. Practice: per-run font extraction (PDFBox) and PREMIS for the provenance record. |
| **3** | ⭐ **Retain the pre-transcode bytes permanently.** | Transcode tables improve. A unit that discards its source bytes cannot be re-derived under a better map, and must be re-extracted from the original. Practice: bit-level preservation. |
| **4** | ⛔ **Classify content by its own features, never by position.** | Facing-page and interleaved layouts make position a fragile proxy; an off-by-one silently mislabels an entire volume while the pipeline reports success. Practice: content identification by signature (DROID/PRONOM). |
| **5** | ⚠️ **Distinguish a witness from a rendering in the SCHEMA**, not in documentation. | A schema in which a transliteration can be recorded as a witness will eventually record one. Practice: TEI's witness and reading elements. |
| **6** | ⭐ **Treat the front matter as data.** | Provenance and permission both live there, and cleaning pipelines strip both. See §7.7. Practice: front-matter structures in BITS and IIIF. |

### 7.7 · A finding about front matter, offered because it cost us nothing and nearly cost us everything

Two scan sets of the same edition were available to this project. One was tidier: its per-volume
front matter had been removed. **Those removed pages carried the scan's provenance — who
photographed it, from which physical copy — and also its distribution dedication**, the terms under
which the material had been offered.

⭐⭐ **Adopting the cleaner set as the working master, purely because it was cleaner, would have
discarded both the attribution and the permission while looking like a simplification.**

⚠️ **The general form: cleaning pipelines are built to remove what is not content, and provenance is
not content.** For a corpus whose entire value proposition is that its claims resolve to sources,
that default is precisely backwards.

---

## 7.5 · What the missing column looks like, concretely

The abstraction becomes checkable at this point, and the numbers are worth stating because they show
the shape of the absence.

The most widely used digital edition of the Pāli canon is the **Chaṭṭha Saṅgāyana Tipiṭaka**, the
recension settled at the Sixth Buddhist Council in Yangon, 1954–56, published digitally as TEI XML
(the romanised release distributed by tipitaka.org, as held by this project on 2026-09-05). Its files carry two independent pieces of apparatus machinery:

| Machinery | What it records | Coverage |
|---|---|---|
| **Page concordance** (`<pb ed="…"/>`) | where a locus falls in each print edition | `V` VRI · `M` Burmese · `T` Siamese · `P` PTS |
| **Variant apparatus** (`<note>`) | where witnesses disagree, with sigla | `sī.` Sinhalese · `syā.` Siamese · `pī.` PTS · `ka.` *kesuci* (some manuscripts) · `kaṃ.` Cambodian |

Across the full set of 217 root and commentary files the concordance carries page markers for four
print editions, and the apparatus carries **22,343** recorded variant readings (counted with
`grep -ac '<note>'`; the `-a` matters, because the files trip binary detection and a plain `grep`
silently undercounts).

⛔ **The count for the Cambodian siglum `kaṃ.` is 1,820 — not zero.** An earlier revision of this
paper stated *the count is zero* from a twenty-five-file sample searched with a tool that treated the
files as binary; that sample also carried no `kaṃ.` note, and the zero read exactly like an absence.
It was a probe failure, and it is withdrawn here rather than quietly fixed. What *is* absent is the
Cambodian edition from the **page concordance** — no `<pb ed="K">` exists, so a Khmer locus cannot
be cited by page — and the Cambodian witness in the apparatus is sparse beside the Sinhalese and
Siamese ones. **The missing column is therefore a concordance column and a fuller witness, not a
first witness.**

⚠️ **This is not an oversight and should not be described as one.** The Sixth Council was convened in
Burma, working from Burmese manuscripts, with Sinhalese and Siamese editions as the comparanda to
hand. **Cambodia's sparseness is the geography of 1954** — its delegates attended the Council, but
the edition it was still printing was not in the room as a comparandum — five years before the Khmer
edition finished printing, and two decades before the people who made it were mostly killed.

### 7.5.1 · ⭐ And the apparatus Khmer is missing from was itself produced by an act of the same kind

The Sixth Council was a **saṅgāyana** — a communal recitation, in which the canon is recited in
assembly and discrepancies are resolved. The recension it produced, and the apparatus that records
where it differs from the Sinhalese and Siamese lines, are the output of a deliberate collation event
convened for exactly that purpose.

⭐⭐ **So the structure this project proposes to add a column to is not a neutral container. It is the
artefact of one tradition's standardisation act**, carrying its comparanda and not others'. That is
not a criticism — an apparatus can only record the witnesses in the room — but it does mean the
sparseness of the Khmer siglum is better described as *a room Cambodia's edition was not in* than
as a gap in a universal record.

⚠️ **It also means the recitation practice and the critical apparatus are the same function performed
by different means.** A saṅgāyana is verification by simultaneous human memory; an apparatus is
verification by recorded disagreement. **Cambodia still performs the first — the state has resolved
(2026) to convene a formal Tipiṭaka recitation every five years — and is nearly absent from the
second.** *A tradition that
verifies its canon on a five-year cycle is not one that lacks a verification culture; it is one whose
verification culture never entered the notation the rest of the field reads.*

⭐ **So the practical form of this paper's thesis is a missing concordance column in an existing
structure, and a witness column to be filled out**
— and the reason that column cannot be filled by normalising the Khmer text toward one of the four
already present is §6.

---

## 8 · The comparison class, and the test

⛔ **This paper rests on one case. That is its principal weakness and no rhetorical move repairs it.**

What can be done is to name the class against which the claim is testable and state what it predicts,
so that the next person is not obliged to take our word for anything.

⚠️⚠️ **The cases below have NOT been checked by this paper's authors and are named as candidates, not
as support.** §4 exists because an unchecked assumption was checked and failed; asserting these
without the same treatment would repeat the error the paper is built on avoiding.

| Case | Named codifier | Datable transition | What the thesis predicts |
|---|---|---|---|
| Modern Hebrew | Ben-Yehuda and successors | late 19th–20th c. | authoritative religious/legal corpora should postdate codification |
| Turkish | the 1928 script reform | 1928 | a sharp discontinuity in what is machine-readable across the reform |
| Norwegian | Aasen and the *målreisning* | 19th c. | competing standards should produce competing corpora, not none |
| Indonesian | the 1972 spelling reform | 1972 | pre- and post-reform texts should require reconciliation |
| Vietnamese | *quốc ngữ* romanisation | 17th–20th c. | a borrowed *script* is not a borrowed *standard*; the thesis should still hold |

⭐ **And the falsification condition, stated plainly:**

> **Find a language with no native orthographic standard and no adequate borrowable neighbour that
> nonetheless supports a corpus treated as authoritative in that language.**

If such a case exists, the claim in §2 is false as stated and should be withdrawn. ⚠️ **Note that the
Swiss German and Arabic cases do *not* satisfy this test** — both had a borrowable target, which is
the whole content of §5.

---

## 8.5 · Why this is an alignment paper, and not a philology paper filed in the wrong place

The category strain flagged at the head of this paper deserves an argument rather than an apology.

**A system that cites inherits its corpus's authority claims wholesale, including the false ones.**
This is not a general observation about training data quality. It is specific to systems whose output
form is *"the source says X at locus Y"* — retrieval-grounded assistants, citation-bound evaluators,
any design whose credibility rests on the resolvability of its references rather than on the fluency
of its prose.

For such a system, three failure modes are usually enumerated: the model hallucinates a citation; the
model cites a real source that does not support the claim; the model cites a source that is itself
wrong. ⭐⭐ **This paper describes a fourth, which is invisible to all three checks:**

> **The citation resolves, the source supports the claim, the source is correct — and the encoded
> text is not the source it claims to be.**

⛔ **No evaluation of the model detects this**, because the error is not in the model. It is not in
retrieval either. It was introduced by a decision about spelling, taken by someone else, often
decades earlier, and usually not recorded. A benchmark measuring citation accuracy will score such a
system highly. A human expert checking a sample will find the passages correct. **The corpus is
confident and empty, and everything downstream inherits that quietly.**

⭐ **That is why the argument belongs in an alignment corpus rather than a philological one.** The
philology is old and settled; what is new is that these decisions now propagate into systems that
speak with authority about traditions, laws and contracts, at a scale and a confidence that printed
editions never had.

⚠️ **And it sharpens what a provenance requirement actually has to cover.** Requiring that a judgment
name its source is necessary and not sufficient: **the requirement must extend to what the source
encoding IS — witness or rendering, and under whose orthography** — or it certifies a chain whose
first link was never examined.

---

## 8.6 · What to do if your language has no standard and nothing to borrow

The argument raises an obvious question it would be evasive not to answer: **suppose you must build
an authoritative corpus in a language with no native standard and no adequate neighbour.**

The Cambodian case cannot advise you, because it had a Chuon Nath. What can advise you is §5.2 — the
dialectal-Arabic community, finding no adequate target to borrow, **built a convention**.

> ⭐⭐⭐ **The prescription, stated plainly: if you are in that position you are not doing corpus
> construction. You are doing language planning, and you should know it before you start rather than
> discover it in year three.**

That reframing has consequences a corpus project would otherwise walk into:

- ⚠️ **It is a decision with standing requirements.** Codification imposed by an outside technical
  team on a community that did not ask is a different act, politically and ethically, from
  codification undertaken by that community — however identical the resulting tables look. §9.3
  applies to you and not only to historical actors.
- ⚠️ **It is not neutral and cannot be made neutral by being minimal.** Every choice about which
  variant becomes canonical excludes writers of the others, and *choosing the most common form* is
  itself a choice with a constituency.
- ⭐ **It should be published as what it is.** A convention presented as a technical preprocessing
  step is a standardisation nobody consented to; the same convention published as a proposal, named,
  dated and defended, can be argued with and adopted or refused.
- ⭐ **And it should be separable.** Retain the pre-normalisation forms (§7.6 rule 3) so that a later
  community can reject your convention without losing the corpus built under it.

⚠️ **This paper takes no position on whether such a project should proceed.** It observes only that
the decision is being made either way, and that making it deliberately is strictly better than making
it by default inside an extraction script.

---

## 9 · Honest limitations

**9.1 · He standardised a script with centuries of use; he did not invent one.** Khmer writing is
attested from the seventh century (the Angkor Borei inscription K.600, dated 611 CE). The claim here concerns **codification** in Haugen's sense —
settling variation, fixing punctuation and layout, producing an authoritative reference — not
creation. ⚠️ **And the compression "one man produced the typography" is wrong in the same way "one man
translated the canon" is wrong: he LED a programme.** The Commission ran from 1929 to 1968 with many
members, most of whom this paper cannot name.

**9.2 · Standardisation was contested, and this paper should say who lost.** The Thommakay reform
prevailed over the Thommaboran. A standard that "everyone now follows" was **imposed over real
objection by a party that had reasons**, and the traditionalist current did not evaporate. Presenting
codification as a consensus achievement would be a false and duller story.

**9.3 · ⛔ The politics are not innocent, and this paper is not an argument for standardisation.**
This work took place under a French protectorate, in a period when script and language reform across
the region was entangled with colonial administration and with competing nationalisms. Chuon Nath
**resisted the romanisation of Khmer** (the protectorate's 1943 ordinance and its opposition), which
is to his credit and is part of the record. But
codification everywhere has costs that fall unevenly: dialect suppression, the exclusion of variant
registers, and the conversion of living variation into error. ⚠️ **This paper identifies a
precondition for one kind of corpus. It does not claim that meeting that precondition is good, and a
reader who takes it as an endorsement of language standardisation has taken more than is offered.**

⭐ **A tension we do not resolve, and flag rather than smooth:** §6 objects to borrowing because it
discards the source variety — but codification discards variation too, from the inside. **Both moves
lose something; the paper claims only that they lose different things, and that what borrowing loses
is disqualifying for a witness while what codification loses is not.** That distinction deserves more
argument than it receives here.

**9.4 · One case, and the comparison class unchecked.** §8.

**9.4.1 · And one case cannot distinguish a PRECONDITION from a STRONG CORRELATE.** The Cambodian
evidence is consistent with the claim in §2 and also consistent with a weaker one: that native
standardisation *makes authoritative corpora much easier* without being strictly required. ⛔
**Nothing available to this paper separates those two readings**, and the falsification test in §8 is
designed to attack the strong version because it is the version worth attacking. ⚠️ *A reader who
concludes only the weaker claim has read the evidence correctly.*

**9.5 · The encoding-layer evidence is drawn from one corpus.** Five fonts in one volume is a fact
about these volumes, not a measured claim about Khmer digital typesetting generally. **No survey has
been run, and the paper should not be read as reporting one.**

**9.5.1 · The paper describes a project's own material and is not disinterested.** The five-font
finding, the front-matter finding and the missing-siglum count all come from the corpus this paper's
authors are building. ⚠️ **That is a source of both the evidence and the framing**, and a reader
should discount accordingly: we found these because we were looking at this, and we are arguing for
the importance of what we happen to be doing. **The falsification test in §8 is offered partly as a
remedy for that** — it is stated so someone with no stake can attack the claim without needing our
material.

**9.6 · Nothing here has been built.** The corpus this paper is a by-product of does not yet exist —
no records emitted, no transcoding tables derived, no coverage figure measured. **This is an argument
about preconditions, offered by a project that has met none of the consequences of being right.**

---

## 10 · Why this matters now

Two reasons, and the second is the one that motivated writing.

**Low-resource language work is expanding fast, and its default framing is a tooling framing.** More
data, better models, better OCR. That framing is correct for most of the work. ⭐ **For the subset of
corpora that must be authoritative — legal, canonical, evidentiary — it is not merely incomplete but
misleading**, because it suggests that sufficient engineering closes a gap that engineering cannot
reach. A project can spend years improving its pipeline against a problem whose obstacle is upstream
of every pipeline.

### 10.1 · The window that is closing, and it is not a technological one

Low-resource corpus construction is being industrialised. Large multilingual models create demand for
text in languages that had none, and the pipelines assembling that text are general-purpose by
design — built to ingest many languages cheaply, which means built to normalise aggressively and to
discard what does not look like content.

⚠️ **Those pipelines will process canonical and evidentiary material without distinguishing it**,
because nothing in the material announces itself. A scanned statute and a scanned newspaper are the
same object to an extraction stage. **The distinction that §2.1 draws is invisible to every tool that
will touch these texts**, and the decisions that flatten it are being taken now, at scale, by people
with no reason to know they are taking them.

⭐ **And the decisions are one-way.** A corpus assembled without recording which encoding a run came
from, or with its front matter stripped, cannot be repaired from the corpus — only by returning to
sources that are sometimes no longer available. *For material where the physical witnesses were
deliberately destroyed within living memory, "return to the source" is not always a fallback.*

**And systems that cite are now being built.** An AI system grounded in a textual corpus inherits
that corpus's authority claims wholesale — including the false ones. ⛔ **A model that answers
questions about a tradition from a corpus that is a rendering rather than a witness will be confident
and wrong in a way no evaluation of the model detects**, because the error is not in the model. It is
in a decision someone made about spelling, decades earlier, and did not record.

*That is the practical form of this paper's argument, and it is why a project about machine values
ended up writing about punctuation.*

---

## 11 · Cross-venue references

- ***The Referee, Not the Governor*** — the evaluation posture this corpus is being built to serve,
  and the source of the citation requirement that made spelling a first-class problem.
- ***Suffering-Cessation as Value Function*** — the substrate argument upstream of the corpus.
- ***Father-Son Khmer Tipiṭaka Transcription as Alignment Work*** — the companion essay, which
  addresses *who transmits* where this paper addresses *what makes transmission encodable.*
- **`SiliconWat/tipitaka-khmer`** — the specifications this paper is a by-product of, including the
  witness taxonomy and the provenance record.

---

## Coda

The Commission's work was finished in 1968 and celebrated in April 1969. What survived the years
after was not the printed edition, most of which was destroyed, but the standard — the settled
spelling, the fixed lexicon, the punctuation — because a standard lives in the people who write with
it and cannot be burned in a building.

⚠️ **That is not a redemptive observation and should not be read as one.** The people who wrote with
it were killed in very large numbers, and the standard survived by a margin nobody would have
chosen. **The point is narrower and technical: the thing that made the canon recoverable was not the
copies. It was the agreement about how to write it down.**

---

*Written by Thon Ly in collaboration with **Miss Aquarius℠**, named as co-author on all corpus
research. The specification, the claims, and the errors are the authors' joint responsibility.*

*Published under CC0 1.0 Universal. This paper is dedicated, with the project it belongs to, to the
Tripiṭaka Commission of Cambodia — for them, not by them; see `SiliconWat/tipitaka-khmer`,
`DEDICATION.md`. This document's SHA-256 is attested independently of the site and its authors —
anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp
authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo
version; a timestamp proves this exact text existed no later than its date and nothing about
authorship, originality, or the validity of any claim.*
