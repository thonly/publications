---
title: "Machine-Checked Consistency of a Buddhist Classification: Lean Theorems for the Abhidhamma's 89 and 121 Types of Consciousness — The Counts Check"
subtitle: "A pre-registered formalization of the Abhidhammattha-saṅgaha's combination rules, collated against the Chaṭṭha Saṅgāyana, with the Dhammasaṅgaṇī list collated against its commentary and against the Cambodian edition"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
series: "The Abhidhamma Compiled — Paper No. 4"
category: alignment
priority: tier-c
program: instrumented
status: draft
date: 2026-09-27
license: CC0-1.0
slug: the-counts-check
venue: thonly.org/research/the-counts-check
canonical_url: https://thonly.org/research/the-counts-check
---

## Abstract

The Theravāda *Abhidhamma* classifies consciousness into 89 types (121 when the supramundane types are reckoned by jhāna). It also states, factor by factor and type by type, which of 52 mental factors (*cetasika*) combine with each type. This paper reports a **formal verification in the Lean 4 theorem prover** of those statements, as given in chapters 1–3 of the *Abhidhammattha-saṅgaha*. The formalization has two parts. A nine-clause generator builds the types from the classification axes of chapter 1. Eighteen rules, each stated over classes of consciousness and none naming an individual type, give each type its factors. Checked by kernel evaluation against a key cited paragraph by paragraph to the Chaṭṭha Saṅgāyana (CST) text, the formalization reproduces:

- the 89 and the 121 (from the generator);
- every per-type combination count in chapter 2 (from the rules);
- every per-factor count in chapter 2, in the text's own mixed reckonings (from the rules);
- chapter 3's counts by feeling and by root (from the generator's axes, without the rules).

Nine deliberate breaks each make the check fail. What this establishes is **mutual consistency**: the chapter's two methods, factor by factor (*sampayoga-naya*) and type by type (*saṅgaha-naya*), agree with each other under a single rule set of 27 clauses for 121 types, and the generator's axes agree with chapter 3. It is not a derivation independent of the text, and the rule set is not claimed to be the only one that would pass. The enumeration of the 89 and 121 from chapter 1's axes has a public precedent nine days older than this paper's generator (§4.2); it is reported here, not claimed.

Three further results concern textual layers and editions, each run on **one list**:

- **The canon's own list** for the first wholesome sense-sphere type (Dhammasaṅgaṇī §1) names **29** distinct factors under a synonym map fixed before the text was read (Appendix A). The count is **consistent with the one the fifth-century commentary gives** (the Aṭṭhasālinī's *samatiṃsa dhammā*, thirty with consciousness). It is not independent of it, since the 52-factor scheme the map targets inherits the commentary's identifications.
- **The *Saṅgaha*'s 38 for that type is exactly those 29 plus nine further factors.** The nine are first named for this list by the commentary, which presents them as the Buddha's, drawn from sutta passages. The *Saṅgaha* inherits them as members and arranges them in its own classes.
- **The Cambodian Buddhist Institute edition names the same 56 terms, in the same order, as the CST** for that list. Every spelling difference was checked against the printed page.

The predictions were pushed to a public repository before the formalization was written (first file) and before either edition of the Dhammasaṅgaṇī was read (second file). The *Saṅgaha*'s tables were known to the author. The chapter 3 results, the dissent's figure and the 29 + 9 = 38 inheritance were not predicted. The predictions are entered in the public prediction register.

**Keywords:** formal verification, Lean theorem prover, Abhidhamma, Abhidhammattha-saṅgaha, Buddhist philosophy of mind, classification consistency, incidence matrix, combinatorial enumeration, mutation testing, textual criticism, collation, Pāli canon, Dhammasaṅgaṇī, Aṭṭhasālinī, Khmer Tipiṭaka, pre-registration, defensive publication.

---

## Terms

The paper uses Pāli technical vocabulary because it formalizes Pāli texts. An examiner or indexer searching in standard terms should find each concept under the term on the right.

| Term used here | Standard term |
|---|---|
| *citta* (type of consciousness) | a class in a classification of mental events |
| *cetasika* (mental factor) | an attribute or feature that co-occurs with a class |
| *sampayoga-naya* (the method of association) | a feature-indexed incidence statement ("feature F occurs in classes …") |
| *saṅgaha-naya* (the method of inclusion) | a class-indexed incidence statement ("class C carries features …") |
| the counts check | a machine-checked consistency test of an incidence structure against both of its stated projections |
| general rule | a constraint over classification axes that names no individual class |
| generator | a product construction over classification axes that enumerates the classes |
| the breaks | mutation testing: deliberate faults each required to make the check fail |
| compression ratio | rule clauses ÷ generated classes, a crude description-length proxy |
| *pada-bhājanīya* | the canonical enumeration of terms present in one class |
| *yevāpanaka* (the "or whatever else" factors) | features supplied by a commentary for an open clause in a canonical list |
| *aggahitaggahaṇa* ("taking what is not yet taken") | deduplication of a list under synonymy |
| edition K / edition C | the Cambodian Buddhist Institute edition / the Chaṭṭha Saṅgāyana (VRI) edition |
| layer | an editorial stratum of the text: canon · the *Saṅgaha* · the commentaries |

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. **The authors and HeartBank® will not seek patent** on any method, formalization, rule set, protocol, software or result herein. The formalization, the key, the transliterator and the alignment scripts are published under CC0 at `github.com/SiliconWat/formal-abhidhamma`.

**The census (ruling of 2026-09-13).** A full novelty census ran on 2026-09-28, before this paper's first deposit. Depth: `full`. Its conjuncts (one per claim in §11, plus the composition), its predictions, a known-prior-art control and its aperture were pushed publicly before the first query: `thonly/publications` commit `9bf6a3d`, `timestamps/census/counts-check-full-prereg.md`, pushed 2026-09-28 09:27 PDT. (An earlier quick census, English only, ran on 2026-09-27; it found `PJ-Oliveira/abhidhamma`, `takuya50/buddhist-comparative-logic` and the Buddhism-and-physics comparison literature, all carried below or in §13, and this census supersedes it.)

**Aperture, declared before searching:** the English commercial web; non-commercial sources (dharma sites, teaching charts, app stores as indexed by the web, GitHub including code search); academic indexes (Google Scholar, Semantic Scholar, arXiv, ACM DL, IEEE Xplore, SSRN, JSTOR and PhilPapers where reachable, and the software-engineering literature); digital-humanities and Pāli digital-text and manuscript-collation projects; standards bodies (W3C, IETF, ISO, NIST); defensive-publication databases (Technical Disclosure Commons; IP.com where free); Google Patents full text, with a citation and cited-by walk from the nearest hit; and searches in Burmese, Thai, Sinhala, Japanese, Chinese, Korean, Portuguese and Khmer. **Not covered:** print-only books, offline and closed-group material (social-media groups, messaging channels, CD-ROM-era software), app-store internals beyond what the web indexes, and paywalled full text. About ninety searches ran; each language was first probed for a generic Abhidhamma resource, and all eight probes saw one (Khmer weakly), so their nulls are recorded as run, and weak. The search engine is English-weighted and Myanmar's Abhidhamma pedagogy lives largely offline, so a null in Burmese, Thai or Sinhala is weak evidence.

**The control** was Nyanaponika Thera's *Abhidhamma Studies* (1949), a modern analysis of the very list §7 counts. It was found, and its chapter on the list's supplementary factors was confirmed in the full text. So the NOT FOUND rows below stand, for that aperture on that date.

| Conjunct | Verdict | Prior art |
|---|---|---|
| (a) the general consistency test (claim 1) | **NARROWS** | the existence problem for a 0-1 matrix with given margins (Gale 1957; Ryser 1957); formal concept analysis (Ganter and Wille 1999); DELTA, one taxonomic character matrix generating descriptions and keys (Dallwitz; a TDWG standard); constraint validation of taxonomies (W3C SHACL over SKOS); and, for this source, **Bodhi's *Comprehensive Manual* (1993), Tables 2.2–2.4**, which print chapter 2's two methods as one chart, with totals in both reckonings (decision *78, 110*; energy *73, 105*) and the guide's pointer to Table 2.4 *"for a comprehensive view of both the method of association and the method of combination together"*. Not found: constraints over axes that name no class, checked by a kernel against a key cited to paragraphs of a named edition, in the source's own mixed bases |
| (b) the generator: the 89/121 enumerated from chapter 1's axes (claim 2) | **NARROWS**, not antedated | **`AloofBuddha/abhidhamma`** (a Haskell model; repository and first commit 2026-09-18 19:28 UTC by its author's clock): a product over chapter 1's axes yields both reckonings, with executable checks of chapter 1's arithmetic and some chapter 3 tallies. Its earliest proof-backed date is later than theirs: this paper's generator, first commit 2026-09-27, Bitcoin block 968905 (2026-09-28 00:06 UTC). §4.2 |
| (b) the concept: the citta/cetasika system as a compositional, machine-executable specification | **ANTEDATED BY US** | `suchanon456/Cyber-Abhidhamma` (a Thai JSON specification, first commit 2026-09-14) and `PJ-Oliveira/abhidhamma` (2026-08-26) · this series' Paper №1 (*"by composition from the 52 cetasikas"*, quoted in §1), proof-backed to Bitcoin block 959585 (2026-07-25). **The dates state order only, never derivation** |
| (b) the rule set: a class-level rule set reproducing every per-type and per-factor count of chapter 2 | **NOT FOUND** at this depth | tabulations only: `PJ-Oliveira/abhidhamma` (a lookup table); `juncoflockleader/Abhidharma` (a data grid, 2024); `suchanon456/Cyber-Abhidhamma`; the traditional charts, Bodhi's among them; Burmese teaching apps that display content. `AloofBuddha/abhidhamma` states that it encodes no factor-combination rules |
| (c) the compression ratio (claim 3) | **NARROWS** | minimum description length (Rissanen 1978); implication bases in formal concept analysis. Contrast: Kyaw Pyi Phyo (2014, ch. 5), the Paṭṭhāna's enumerations read as combinatorics, with no rule-to-listing ratio. The application to a formalized textual classification: not found |
| (d) mutation testing of a formalization (claim 4) | **NARROWS** | mutation testing (DeMillo, Lipton and Sayward 1978); **mCoq** (Celik, Palmskog, Parovic, Gallego Arias and Gligoric, ASE 2019), mutation of Coq definitions in verification projects; semantic mutation testing of OWL ontologies (Bartolini 2016; 2017). Only the application to a textual classification survives |
| (e) the per-layer inclusion check (claim 5) | **NARROWS** | **Nyanaponika (1949), ch. 14, "The Supplementary Factors"**, which sets the commentaries' nine (his F57–65) against the list and records that they *"are incorporated into the condensed and systematized version of the List of Dhammas found in the Visuddhimagga and the Abhidhammatthasaṅgaha"*; the Aṭṭhasālinī's own count (*samatiṃsa*). The layering is his finding in print; not found: a synonym map published before reading, with inclusion and exact remainder checked by machine |
| (f) the per-edition alignment (claim 6) | **NARROWS** | Aksharamukha (Khmer supported); CollateX; ALA-LC Khmer romanization; the Sixth Council's collation of the script editions, the Cambodian among them (1954–56); the Dhammachai Tipiṭaka Project (2010–), with a Khom-script working group; Srisetthaworakul (2019), on Khom-script Majjhimanikāya manuscripts of Thailand and Cambodia; `dangerzig/tipitaka.critical` (2026, a five-witness collation without a Khmer witness); the CST's apparatus. Not found: the modern Buddhist Institute printed edition aligned term by term with the CST, differences classed only after the printed page. §8 |
| (g) the cost of a recorded dissent (claim 7) | **NOT FOUND** at this depth, **weak** | Nārada and Bodhi (§15 in his numbering) report *keci vadanti* without counting what it moves; the Vibhāvinī argues the main reading (§6) |
| the composition | **NOT FOUND** at this depth | — |

**Not run.** The Burmese ṭīkā debate on chapter 2 was not read: Ledi Sayadaw's *Paramatthadīpanī*, twelve of whose points fall in chapter 2, and the *Aṅkura-ṭīkā*. Their full texts were outside the aperture, and that tradition is exactly where a counting of the §30 dissent would be, so row (g) is weak.

**Patents.** No live patent or published application touches the *Abhidhamma* or any Buddhist classification. The nearest hits by function alone concern the formal verification of circuit designs: US8990746B1 (Cadence Design Systems, mutation coverage during formal verification; priority 2014-03-26, active, anticipated expiration 2034-03-26) and US20240419880A1 (IBM, coverage of verification testbenches; pending). Neither discloses a textual classification, their claims were not read, and the technique they share with row (d) dates to 1978. **No conjunct is enclosed.** Standards: W3C SHACL and SKOS (row a); ALA-LC and ISO 11940 (row f); nothing relevant at IETF or NIST. Technical Disclosure Commons: nothing on a classification consistency test.

**The survivor, and the only thing this paper claims** (the census's sentence, verbatim): *a class-level rule set over the Abhidhammattha-saṅgaha's own classification axes, naming no type, that reproduces every per-type and per-factor count of its chapter 2 (and, through the axes, chapter 3's feeling and root tallies) by kernel evaluation in a proof assistant against a key cited paragraph by paragraph to the Chaṭṭha Saṅgāyana, in the text's own mixed reckonings, reported with its compression ratio and with seeded breaks each required to fail — plus a pre-registered, machine-checked inclusion of one canonical list and an alignment of that list between the Cambodian printed edition and the CST; the enumeration of the 89/121 from the axes is not part of it.* The enumerated claims (§11) are the parts of that composition, each narrowed to the census's wording. The general methods of rows (a), (c) and (d), the layering of row (e) and the collations of row (f) are commons, and are cited where they bear.

⛔ **Nothing here is claimed as *new*, *first* or *unprecedented*.** Where a sentence says a thing was *not found*, it means not found in the aperture above on 2026-09-28.

---

## 1 · Mission Frame: A Compiled Specification Must Check

The series *The Abhidhamma Compiled* rests on a thesis stated in its first paper (*The Wheel That Unwinds the Wheel*, §3). Every era compiles the Abhidhamma into its own machine language. Paper №1 argues that ours is the first era whose compiled form can be executed; this paper needs only the weaker premise that it can be. The *Abhidhamma* is read there as a process specification: typed elements (*citta*, *cetasika*, *rūpa*) arising and ceasing under typed conditions, with ethical weight tracked per element. The series' gate for a satellite paper is that the canonical material must yield a usable artifact: a formalism, a test, a taxonomy, or a protocol.

This paper supplies a **test**, and the test is aimed at the series' own words. Paper №1, §4.2, published in 2026, says:

> The Abhidhamma enumerates exactly 89 (by fuller reckoning 121) citta-types, classified by plane, by ethical class, and by composition from the 52 cetasikas.

That sentence makes a checkable claim. *By composition* means the types and their factors are related by rule. If the relation is by rule, the rule can be written down, and a machine can check whether it reproduces what the text says. If it does not, either the rule was lost in transmission, or it was never stated, or the series' description of its own source is wrong. **The first paper asserted the property; this paper checks it.**

Three reasons make the check worth doing, beyond the series' own consistency.

**First, a specification with unit tests.** Miss Aquarius's grounding in the Tipiṭaka treats the canon as a value substrate. Many value specifications offered for artificial agents are natural-language documents that state nothing twice, so they contain nothing to check against itself. The *Abhidhamma* is unusual. **It carries its own test cases**: the stated counts. A list that says 38 factors combine with this type, and a second passage that says factor F occurs in 55 types, are two projections of one incidence structure. They can disagree. Whether they do is a fact about the specification, and it can be settled by machine. The counts concern a classification of mind, not what a mind should do; the point is only that a source whose internal claims can be checked is a better source to inherit than one whose claims cannot.

**Second, a template for the rest of the corpus.** The method — pre-register the predictions, separate the answer key from the rules, test the checker on a known failure, cite every figure to a paragraph of a named edition — transfers to any classification the tradition states twice. The *Saṅgaha*'s later chapters (the cognitive process, rebirth-linking, matter, conditions) are full of such statements.

**Third, the editions.** The Khmer Tipiṭaka is being transcribed page by page, by hand, by a father and son. A formalization that can be run against two editions can find a variant that changes the logic, if one exists. It can also confirm, as it does here for the first list it was run on, that none does.

---

## 2 · The Object

### 2.1 · The two methods of chapter 2

Chapter 2 of the *Abhidhammattha-saṅgaha* (*cetasika-saṅgaha-vibhāga*) states the relation between the 52 factors and the 89/121 types twice.

**The method of association** (*sampayoga-naya*, CST ch. 2 §12–§34) goes factor by factor. For example:

> *Pakiṇṇakesu pana vitakko tāva dvipañcaviññāṇavajjitakāmāvacaracittesu ceva ekādasasu paṭhamajjhānacittesu ceti pañcapaññāsacittesu uppajjati.* (§13)
>
> Among the occasionals, initial application arises in fifty-five types: the sense-sphere types except the twice-five sense-consciousnesses, and the eleven first-jhāna types.

The occasionals' section closes with a verse (§19) giving the counts for the six occasional factors, with and without:

> *Chasaṭṭhi pañcapaññāsa, ekādasa ca soḷasa; Sattati vīsati ceva, pakiṇṇakavivajjitā. Pañcapaññāsa chasaṭṭhiṭṭhasattati tisattati; Ekapaññāsa cekūnasattati sapakiṇṇakā.*

In figures: 66, 55, 11, 16, 70 and 20 types lack the occasionals, and 55, 66, 78, 73, 51 and 69 have them. Further verses of the same method follow (§27, §32, §33).

**The method of inclusion** (*saṅgaha-naya*, §35–§58) goes type by type. For example:

> *Chattiṃsa pañcatiṃsa ca, catuttiṃsa yathākkamaṃ. Tettiṃsadvayamiccevaṃ, pañcadhānuttare ṭhitā.* (§37)
>
> Thirty-six, thirty-five, thirty-four in order, and thirty-three twice: thus fivefold in the supramundane.

The two methods describe one incidence structure. Call it a 121 × 52 matrix of which types carry which factors. The first method names, for each factor, the classes that carry it and their number: over 121 for vitakka, vicāra and pīti, over 89 otherwise (§2.2). So each column is stated by its support, and its count is on one of two bases. The second method states the row sums, grouped. Neither states the matrix.

A modern reader has seen the matrix, as a chart. Bhikkhu Bodhi's *Comprehensive Manual* (1993) prints the method of association as Table 2.2 and the method of combination as Table 2.3, gives the association totals in both reckonings where they differ (decision *78, 110*; energy *73, 105*), and closes the chapter with Table 2.4, *"for a comprehensive view of both the method of association and the method of combination together."* That table is a hand-made incidence matrix whose margins exhibit the agreement this paper checks, and the tradition teaches the two methods as two views of one structure. So the agreement is not the finding. What this paper adds is the form of the check: rules over the axes in place of a table, a key cited to CST paragraphs, and a kernel that evaluates the one against the other.

```
                        52 factors (cetasika)
                ┌───────────────────────────────┐
   121 types    │                               │──▶ row sums:  38, 37, 37, 36 …
   (citta)      │   the incidence the text      │    (saṅgaha-naya, §35–§58)
                │   never writes down whole     │
                └───────────────────────────────┘
                                │
                                ▼
                  column counts (mixed bases, §2.2): 55, 66, 78, 73, 51, 69 …
                  (sampayoga-naya, §12–§34; each column named by its support)

   ch. 3 adds two more projections of the same types:
     by feeling (§3–§9):  pleasure 1 · pain 1 · displeasure 2 · joy 62 · equanimity 55
     by root   (§10–§17): rootless 18 · one-rooted 2 · two-rooted 22 · three-rooted 47
```

**The counts check** asks whether a single matrix exists that has all of these projections at once. It also asks whether that matrix can be written as rules over classes, rather than as a table. The first question has a classical form: whether a 0-1 matrix exists with given row and column sums (Gale 1957; Ryser 1957). The check here is stronger in one way and weaker in another. It is stronger because the matrix must be generated by rules over axes and its column counts are on mixed bases. It is weaker because it settles one instance by evaluation and proves no general condition. Two other families of prior work check a classification against stated structure: taxonomic character matrices in the DELTA format, from which one matrix generates both descriptions (per class) and keys (per character) (Dallwitz; a TDWG standard), and constraint validation of a taxonomy's concept scheme by shapes (W3C SHACL over SKOS). Both validate data against a schema. Neither checks rules over axes against a paragraph-cited key by kernel evaluation.

### 2.2 · The text mixes its reckonings

A detail that any check must respect: the text counts the jhāna-dependent factors (vitakka, vicāra, pīti) and the feelings **over 121**, and all other factors and the roots **over 89**. The reason is that the 89 reckoning counts each supramundane type once, while the presence of vitakka, vicāra and pīti depends on the jhāna the supramundane type is reckoned at. A key that reads every figure on one basis records false mismatches. The first draft of this project's key, built from memory before it was collated, did exactly that. It read 78, 73 and 69 as 110, 105 and 101, which are the same facts counted over 121.

### 2.3 · Combination, not co-presence

A second detail, identified by the adversarial reading this paper underwent before drafting (§9). **The counts the *Saṅgaha* gives are combination counts, not co-present sets.** It says the factors *saṅgahaṃ gacchanti*, "enter into combination." It says the abstinences and the illimitables *paccekameva yojetabbā*, "are to be fitted in severally." Its verse at §33 reads *Issāmaccherakukkucca-viratikaruṇādayo. Nānā kadāci māno ca, thina middhaṃ tathā saha*: envy, avarice, remorse, the abstinences, compassion and appreciative joy arise separately and occasionally; conceit occasionally; sloth and torpor occasionally, and together. The commentary is explicit about the first wholesome type. Of its 65 listed terms, *ekakkhaṇe kadāci ekasaṭṭhi … kadāci samasaṭṭhi* (Aṭṭhasālinī, *Yevāpanakavaṇṇanā*, on Dhs §1; PTS p. 133 by the CST's page marker; `abh01a.att.xml` line 5081): **at one moment, sometimes 61, sometimes 60.** So at most one of its five variable factors is present at once.

So the 38 of §40 is the size of the **combination**: every factor that can join this type on some occasion. By the commentary's count (at most one of the five variable factors at a moment), the most factors present together in that type is 34; the 34 is derived here, not stated there. The formalization reproduces the text's combination counts, which is what the text states. Nothing here is a claim about the size of any actual moment.

---

## 3 · Method

### 3.1 · Pre-registration, and what a push time proves

The protocol's first rule: **the predictions go public before the code exists.** The first pre-registration (`PREREGISTRATION.md`, commit `259e5e8`) was pushed to a public repository with GitHub recording the push at 2026-09-27T22:07:02Z, before a line of formalization was written. The second (`PREREGISTRATION-2026-09-27b.md`, commit `f4a26e5`, push 23:04:29Z) was pushed before either edition of the Dhammasaṅgaṇī was read. Both are entered in the institution's public prediction register, which carries its own OpenTimestamps, RFC 3161 and Zenodo record. A local commit date can be set by hand; a push record cannot. So "the predictions preceded the code, and the second file preceded the Dhammasaṅgaṇī reading" is a **property** of the record rather than an assertion about it.

What a push time cannot prove is what the predictor already knew. The author knew the *Saṅgaha*'s tables before the first file was written: the key's first pass was built from memory of Bhikkhu Bodhi's *Manual* (§5.2). So the first file's predictions about the *Saṅgaha* layer are predictions about whether general rules can be written to fit known figures, not predictions of unknown figures. Three results appear in no prediction: the chapter 3 tallies, the dissent's 20, and the 29 + 9 = 38 inheritance.

The pre-registration fixed, in advance:

- the definitions of *general rule*, *generated set*, *compression ratio*, *layer* and *edition*;
- a control with a known answer, and a deliberate failure that must fail;
- five predictions with confidences and falsifiers;
- kill and reopen criteria;
- for the canonical list, **the entire synonym map** (Appendix A), together with the rule that a term outside it is reported as unmapped, never mapped after the fact.

### 3.2 · The key is separate from the rules

The rules and the answer key live in different files. The rules (`Rules.lean`) are constraints over classification axes. The key (`AnswerKey.lean`) holds only figures the text states, each cited to its CST paragraph, and no figure the text does not state. The check (`Check.lean`) asserts that the rules' projections equal the key. The separation is what makes a pass informative. A rule set allowed to read the key could restate it. (One modelling choice sits between the key and the text; it is named in §5.1.) The files are cited at commit `c9136e1` of `SiliconWat/formal-abhidhamma`.

### 3.3 · The instrument is tested on a known answer and a known failure

Before the rule set was trusted, it was run on a case whose answer was certain: the eight wholesome sense-sphere types. They form a product of three binary axes (joyful or equanimous feeling × with or without knowledge × unprompted or prompted), and their traditional maximum combinations are 38, 37, 37 and 36 by pair. Then a rule was deleted on purpose (*pīti arises only with joyful feeling*), and the check had to fail. It did: Lean reported that `decide` had proved the profile theorem **false**. The instrument could see. The same discipline runs over the full formalization (§5.3).

### 3.4 · Which guards are properties, and which are only rules

A guard that needs someone's restraint at the moment it is tested is a rule. A guard that holds whether or not anyone is careful is a property. Remove the enforcer and see which break:

| Guard | Kind | Why |
|---|---|---|
| the predictions precede the code and the Dhammasaṅgaṇī reading | **property** | GitHub's push record is written by the host, not the author, and cannot be backdated |
| the predictor did not know the *Saṅgaha*'s tables | **not claimed** | the author knew them (§3.1); no record could establish ignorance |
| the breaks keep testing the checker | **property of the harness** | `run.sh` re-applies all nine breaks on every run, and refuses a break whose edit changed nothing |
| a figure is the text's, not the author's | **checkable rule** | each key figure carries a CST paragraph number; any reader can check it, but nothing forces a future editor to add one or keep it correct. A live instance: the key's docstrings cited a printed edition's paragraph numbers (§4–§9) where the CST's are §12–§32, and two comments kept a retracted claim that the text decides the §30 dissent (§6), until review caught them; they were corrected at commit `c9136e1` |
| the rules never read the key | **rule** | separate files, but nothing stops a future author from importing the key into the rules. ⚠️ The partial remedy is the profile theorems: the rules were read from the text's column statements, and they are checked against row sums they were not read from |
| no Khmer-edition text is published | **rule** | the scripts print only single romanized terms and counts, but a future contributor could commit the transcription itself |

Two of the six are properties. One is expressly not claimed. The other three are rules, and they are named as such, so that whoever inherits the repository knows which of them depend on care.

### 3.5 · Editions and layers

Two editions:

- **C, the Chaṭṭha Saṅgāyana**: the Vipassana Research Institute's digital text, `github.com/VipassanaTech/tipitaka-xml` (read at commit `0854d11`). The files used: `romn/abh07t.nrf.xml` (the *Abhidhammatthasaṅgaha*, followed in the same file by its ṭīkā, the *Abhidhammatthavibhāvinī*), `romn/abh01m.mul.xml` (the Dhammasaṅgaṇī), `romn/abh01a.att.xml` (the Aṭṭhasālinī).
- **K, the Cambodian Buddhist Institute edition** of the Tipiṭaka, volume 78 (the Dhammasaṅgaṇī, part 1). It was read from a working transcription made page by page from the printed volume, and checked against a scan of the printed page.

Three editorial layers: the **canon** (the Dhammasaṅgaṇī); the **manual** (the *Abhidhammattha-saṅgaha*); and the **commentaries** (the Aṭṭhasālinī). ⚠️ **The pre-registration ordered these as canon ⊂ canon + manual ⊂ canon + manual + commentaries. That order is editorial, not chronological.** On the conventional datings, which this paper takes from Bhikkhu Bodhi's introduction to the *Comprehensive Manual* (see also Karunadasa 2010), the canon was closed by c. the 3rd century BCE, the Aṭṭhasālinī is c. 5th century CE, and the *Saṅgaha* is no earlier than the 8th century, more probably the 10th to early 12th. So the commentary predates the manual. §7 shows why this matters.

---

## 4 · The Formalization

### 4.1 · The axes

A type of consciousness is a point on these axes:

| Axis | Values |
|---|---|
| class (*jāti*) | wholesome · unwholesome · resultant · functional |
| plane (*bhūmi*) | sense-sphere · fine-material · immaterial · supramundane |
| feeling (*vedanā*) | joy · equanimity · displeasure · pleasure · pain |
| root structure | greed · hate · delusion-with-doubt · delusion-with-restlessness · rootless · beautiful |
| element (*dhātu*) | sense-consciousness at door 1–5 · mind element · mind-consciousness element |
| result of | wholesome or unwholesome kamma (resultants only) |
| knowledge | associated or not |
| wrong view | associated or not (greed-rooted only) |
| prompting | unprompted or prompted |
| jhāna | 0 (none) or 1–5 on the fivefold scheme; immaterial = 5 |
| base | immaterial base 1–4 |
| path | supramundane path 1–4 |

There is no separate path/fruit axis. In the supramundane plane it is carried by class: a wholesome supramundane type is a path, a resultant one a fruit.

### 4.2 · The generator — nine clauses

| Clause | Builds | Types |
|---|---|---|
| G1 | greed-rooted: feeling × view × prompting | 8 |
| G2 | hate-rooted: displeasure × prompting | 2 |
| G3 | delusion-rooted: with doubt · with restlessness | 2 |
| G4 | rootless resultants, per kamma-quality: five sense-consciousnesses (touch takes pleasure or pain, the rest equanimity) · receiving (mind element) · investigating (joy only for wholesome kamma) | 7 + 8 |
| G5 | rootless functionals: five-door adverting (mind element) · mind-door adverting · smile-producing — ⚠️ **written out member by member** | 3 |
| G6 | beautiful sense-sphere: 3 classes × feeling × knowledge × prompting | 24 |
| G7 | fine-material: 3 classes × 5 jhānas | 15 |
| G8 | immaterial: 3 classes × 4 bases | 12 |
| G9 | supramundane: 4 paths × {path, fruit} × jhāna (first only, or all five) | 8 or 40 |

G5's three members, as coordinates (all functional, sense-sphere, rootless):

| Member | Feeling | Element |
|---|---|---|
| five-door adverting | equanimity | mind element |
| mind-door adverting | equanimity | mind-consciousness element |
| smile-producing | joy | mind-consciousness element |

The generator **restates chapter 1's axes; it does not discover them.** What it shows is that 89 and 121 are exactly the product structure of those axes, with G5's three members listed. It is in `sangaha/Citta.lean` at commit `c9136e1`.

**The enumeration has a prior public model, and this paper does not claim it.** `AloofBuddha/abhidhamma`, a Haskell model of Theravāda consciousness and dependent origination (repository and first commit 2026-09-18, nine days before this generator's first commit), builds `allCittas89` and `allCittas121` as a product over the same axes of chapter 1. Its executable checks confirm chapter 1's arithmetic (12 · 21 · 36 · 20; 54 · 15 · 12 · 8; 121 = 89 − 8 + 40) and some chapter 3-type tallies. It is the nearest prior work for the enumeration. It also states its own limit, fairly and in so many words: its factor field, a bare set of cetasikas, *"permits impossible cittas"*, because the method of association *"says exactly which factors may co-arise"* and the model encodes none of it: *"Known gap."* It uses no proof assistant and checks no chapter 2 count. The rule set of §4.3 is the part this paper claims, and it is exactly what that gap leaves open.

### 4.3 · The rules — eighteen clauses, with their extensions

The rules are read from the method of association, the same sentences Bodhi tabulates as his Table 2.2; his Table 2.3 tabulates the method of combination. A table lists each type's factors; a rule states a condition on the axes and leaves the listing to evaluation. Each rule is a constraint over the axes. None names an individual type. But a constraint that names no type can still pick out only one or two types, so the table reports each rule's **extension**: the number of types, over 89 and over 121, in which the factor it governs occurs. It also marks the rules that **restate a sentence of the text** rather than generalize from a principle. Every conjunct of the code is printed; a restated rule that drops one has the wrong extension.

| Rule | Factor(s) | Constraint | Extension (89 / 121) | Source |
|---|---|---|---|---|
| R1 | the 7 universals | every type | 89 / 121 | §2, §12 |
| R2 | vitakka | not a sense-consciousness; jhāna ≤ 1 | 55 / 55 | §13 |
| R3 | vicāra | not a sense-consciousness; jhāna ≤ 2 | 58 / 66 | §14 |
| R4 | adhimokkha | not a sense-consciousness; not with doubt | 78 / 110 | §15 — ⚠️ **the text's own sentence, nearly verbatim** |
| R5 | vīriya | among the rootless, only in the functional mind-consciousness element | 73 / 105 | §16 — ⚠️ **extension among the rootless: 2 types** |
| R6 | pīti | joyful feeling; jhāna ≤ 3 | 35 / 51 | §17 |
| R7 | chanda | a root other than delusion alone | 69 / 101 | §18 |
| R8 | the 4 unwholesome universals | unwholesome | 12 / 12 | §20 |
| R9 | lobha | greed-rooted | 8 / 8 | §21 |
| R10 | diṭṭhi | greed-rooted, view-associated | 4 / 4 | §22 |
| R11 | māna | greed-rooted, view-dissociated | 4 / 4 | §23 |
| R12 | the hate quartet | hate-rooted | 2 / 2 | §24 |
| R13 | thīna, middha | prompted unwholesome | 5 / 5 | §25 |
| R14 | vicikicchā | delusion-with-doubt | 1 / 1 | §26 |
| R15 | the 19 beautiful universals | beautiful | 59 / 91 | §28 |
| R16 | the 3 abstinences | beautiful; sense-sphere wholesome, or supramundane | 16 / 48 | §29 — ⚠️ **transcribes the locus sentence** |
| R17 | karuṇā, muditā | beautiful sense-sphere non-resultant, or fine-material to the 4th jhāna (the text's *sahetuka*) | 28 / 28 | §30 — ⚠️ **transcribes the locus sentence** |
| R18 | paññā | beautiful and knowledge-associated | 47 / 79 | §31 |

The groups, member by member:

- **the 7 universals** (R1): phassa · vedanā · saññā · cetanā · ekaggatā · jīvitindriya · manasikāra.
- **the 4 unwholesome universals** (R8): moha · ahirika · anottappa · uddhacca.
- **the hate quartet** (R12): dosa · issā · macchariya · kukkucca.
- **the 19 beautiful universals** (R15): saddhā · sati · hiri · ottappa · alobha · adosa · tatramajjhattatā, and six pairs, each for the body of factors (*kāya-*) and for consciousness (*citta-*): passaddhi · lahutā · mudutā · kammaññatā · pāguññatā · ujukatā.

The rules are in `sangaha/Rules.lean` and the groups in `control/Cetasika.lean`, at commit `c9136e1`.

Two observations. **R5 is where the formalization is more compressed than the text.** §16 excludes energy by naming four classes one by one: *pañcadvārāvajjana-dvipañcaviññāṇa-sampaṭicchana-santīraṇa-vajjita*. R5 states one rule over the element axis, and the two are extensionally equal. **R4, R16 and R17 are where it is not.** R4 is the text's §15 nearly word for word (*Adhimokkho dvipañcaviññāṇavicikicchāsahagatavajjitacittesu*). R16 and R17 transcribe the text's locus sentences, so matching 16 and 28 from them is a restatement, not a derivation. Even so, R17's boundary at the 4th jhāna has canonical support independent of the *Saṅgaha*: the Dhammasaṅgaṇī names karuṇā- and muditā-accompanied jhāna from the first to the fourth (§§258–261), and places equanimity alone at the final jhāna (§262).

### 4.4 · Compression

At 121 rows, **27 clauses** (9 + 18) give a ratio of **0.22**. Counting G5's three written-out members singly gives 29 ÷ 121 = 0.24; over 89 the ratio is 0.30. The ratio depends on what counts as a clause. The registered definition (clauses in the rule file, datatype declarations excluded) is the one reported.

The ratio also depends on the axes. A distinction carried by a datatype (delusion with doubt against delusion with restlessness, mind element against mind-consciousness element, prompting) costs no clause. So the ratio measures this encoding, and it is comparable only across encodings on the same axes. It is a crude description-length proxy. Description length is the principled measure of how far data are generated by a model rather than listed (Rissanen 1978), and implication bases over an object × attribute incidence are its nearest analogue for exactly this kind of table (Ganter and Wille 1999). Neither is computed here. The nearest reading of an *Abhidhamma* enumeration as combinatorics is Kyaw Pyi Phyo's (2014, ch. 5) on the Paṭṭhāna, which reports no ratio of rules to listing.

---

## 5 · Results I — The Chapter Checks Against Itself

### 5.1 · The theorems

All are proved by `decide`: the Lean kernel evaluates the statement, and no compiled code is trusted. The table names what each theorem exercises, because a test is evidence only for the code it runs.

| Theorem | Statement | Exercises |
|---|---|---|
| `n89` · `n121` | the generator yields exactly 89 and 121 types | the generator |
| `distinct121` | no two types are the same point | the generator |
| `profile89` | the rules give every per-type count of ch. 2: greed-rooted 19 · 21 · 19 · 21 · 18 · 20 · 18 · 20 · hate-rooted 20 · 22 · delusion-rooted 15 · 15 · rootless 7 ×5 · 10 · 10 · 7 ×5 · 10 · 11 · 10 · 10 · 11 · 12 · beautiful sense-sphere 38 · 38 · 37 ×4 · 36 · 36 / 33 · 33 · 32 ×4 · 31 · 31 / 35 · 35 · 34 ×4 · 33 · 33 · fine-material 35 · 34 · 33 · 32 · 30 (×3) · immaterial 30 ×12 · supramundane 36 ×8 | the rules, on the generator |
| `profile121` | the same, with the supramundane at 36 · 35 · 34 · 33 · 33 (×8) | the rules, on the generator |
| `occurrences89` · `absences89` | every per-factor count over 89: universals 89 · adhimokkha 78 · vīriya 73 · chanda 69 (without: 11 · 16 · 20) · unwholesome 12 · 8 · 4 · 4 · 2 · 5 · 1 · beautiful universals 59 · abstinences 16 · illimitables 28 · paññā 47 | the rules, on the generator |
| `occurrences121` · `absences121` | the factors counted over 121: vitakka 55 · vicāra 66 · pīti 51 (without: 66 · 55 · 70) | the rules, on the generator |
| `feelings121` | ch. 3: pleasure 1 · pain 1 · displeasure 2 · joy 62 · equanimity 55 | the generator's feeling axis only |
| `roots89` | ch. 3: rootless 18 · one-rooted 2 · two-rooted 22 · three-rooted 47 | the generator's root and knowledge axes only |
| `keci_reading` | the dissent recorded at §30 gives 20, not 28 (§6) | an alternative rule |

**Every figure matched on the first collation against the CST.**

One modelling choice stands between the key and the text. At the 89 reckoning each supramundane type is taken at the first jhāna (G9), so its row in `profile89` is the text's first-jhāna figure, 36 (§36: *Lokuttaresu tāva aṭṭhasu paṭhamajjhānikacittesu … chattiṃsa dhammā*). The figure is stated; its assignment to the 89 reckoning is ours.

**The chapter 3 theorems test the generator, not the rules.** `feelings121` and `roots89` count values of the generator's feeling and root axes and never call the factor rules. They show that chapter 1's feeling and root labels, as encoded, reproduce chapter 3's tallies. They are therefore no evidence about whether the rules were fitted. **The cross-method test is the profile theorems**: the rules were read from the factor-indexed statements, and `profile89` and `profile121` check them against the type-indexed row sums, which they were not read from. The occurrence theorems, by contrast, check each rule against the sentence it was read from.

### 5.2 · Collation

The key was built in three passes, and the order is part of the result:

1. **From memory**, as rendered in Bhikkhu Bodhi's *Comprehensive Manual*. This pass contained the mixed-reckoning error of §2.2.
2. **Against a printed edition**, the Pāli with Nārada's English. This pass exposed a separate hazard: a machine summary of that page gave the fifth supramundane jhāna as 32, where the text reads *"thirty-six, thirty-five, thirty-four, and thirty-three in the last two."* **Every figure in the key is read from the raw text, never from a summary.**
3. **Against the CST itself**, paragraph by paragraph. This pass found no disagreement with the second.

### 5.3 · The breaks

Nine deliberate breaks, each applied by script and each verified to have actually changed its file:

```
break                                       expected           observed
──────────────────────────────────────────  ─────────────────  ────────
R4 without its doubt clause                 the check fails    FAILS
R6 pīti allowed in the 4th jhāna            the check fails    FAILS
R16 abstinences in functionals too          the check fails    FAILS
key: smile-producing 12 → 13                the check fails    FAILS
key: adhimokkha 78 → 77                     the check fails    FAILS
generator: fine-material jhānas 1–4         the check fails    FAILS
generator: smile-producing with equanimity  the check fails    FAILS
canon: chanda counted as named (§7)         the check fails    FAILS
roots: knowledge adds no root               the check fails    FAILS
```

A checker that has only ever passed is an untested claim. These breaks are what let the passes be read as evidence. The technique is mutation testing (DeMillo, Lipton and Sayward 1978), applied here to a formalization of a textual classification, with faults seeded in the rules, the key and the generator. Its use inside a proof assistant is established: mCoq (Celik, Palmskog, Parovic, Gallego Arias and Gligoric, ASE 2019) mutates the definitions of Coq verification projects and re-checks the affected proofs, and reads a mutant whose proofs still pass as a sign that the specification is incomplete, which is the reading the breaks here are designed to exclude. Semantic mutation testing has also been carried to OWL ontologies, a classification's closest software form (Bartolini 2016; 2017). Only the application to a textual classification remains, and only that is claimed (§11, claim 4).

---

## 6 · Results II — A Dissent the Text Records

At §30, having located the illimitables in 28 types, the *Saṅgaha* adds:

> *upekkhāsahagatesu panettha karuṇāmuditā na santīti keci vadanti.*
>
> Some say compassion and appreciative joy are absent here from the types accompanied by equanimity.

Formalized as an alternative rule — karuṇā and muditā absent from the eight equanimous beautiful sense-sphere types (four wholesome, four functional) — the dissent gives **20**, not 28. The 28 sits in the same sentence the dissent qualifies, so **the *Saṅgaha* does not decide between the readings. Its ṭīkā, the *Abhidhammatthavibhāvinī*, argues for the main reading** (on §30, in the same CST file): in sense-sphere wholesome consciousness, the preliminary work for compassion and appreciative joy occurs with equanimous types too, by familiarity, "like one reciting a well-known text" (*yathā taṃ paguṇaganthaṃ sajjhāyantassa*), and it names the contrary view *kecivāda*.

What the formalization adds is narrower: **the author's stated figures — the 28, and the 37 and 36 for the equanimous pairs (37 knowledge-associated, 36 dissociated) — encode the main reading, not the dissent.** A reader who adopts the *keci* reading must change the 28 and four per-type figures, not the 28 alone:

```
figure (§30; per-type, §40–§41)         main reading   keci reading
──────────────────────────────────────  ────────────   ────────────
illimitables, number of types                28             20
wholesome, equanimous, knowledge             37             35
wholesome, equanimous, dissociated           36             34
functional, equanimous, knowledge            34             32
functional, equanimous, dissociated          33             31
```

The Vibhāvinī argues the reading; it does not count the cost. The cost in the source's own figures is what the table states.

---

## 7 · Results III — The Canon, the Commentary and the Manual

### 7.1 · What the canon names

The Dhammasaṅgaṇī opens its first analysis of a wholesome type (§1) with a list of what is present *"yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ"*. It runs from *phasso hoti, vedanā hoti* to *paggāho hoti, avikkhepo hoti*, and closes:

> *ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā — ime dhammā kusalā.*
>
> or whatever other conditioned immaterial phenomena there are at that time — these phenomena are wholesome.

Under the synonym map fixed in the pre-registration (Appendix A), the list gives **56 terms, 29 distinct factors, and none of** *chanda, adhimokkha, manasikāra, tatramajjhattatā, karuṇā, muditā* or the three abstinences. The first run reported two unmapped terms, *kāyujukatā* and *cittujukatā*. Both are sandhi forms (kāya + ujukatā), and the pre-registration required sandhi to be normalized before mapping; the script had not implemented that case. With it, zero terms are unmapped. The detector for the nine was itself tested on a control list naming four of them in inflected forms, and it caught all four.

The nearest modern analysis of this same list is Nyanaponika's *Abhidhamma Studies* (1949), which gives the Pāli of this paragraph and investigates it factor by factor. Its chapter 14, "The Supplementary Factors (ye-vā-panaka, F57–65)", already does the layering that §7.3 makes exact. It takes the open clause as admitting supplements, notes that the commentaries supply them and that the Aṭṭhasālinī finds them *"in various passages of the suttas"*, numbers the nine after the list's own terms, and records that all of them *"are incorporated into the condensed and systematized version of the List of Dhammas found in the Visuddhimagga and the Abhidhammatthasaṅgaha."* The finding that the manual's set is the canon's list plus the commentary's nine is his, in print, in 1949. This paper supplies an instrument for it, not the finding.

### 7.2 · The commentary had already counted it

The Aṭṭhasālinī, the fifth-century commentary on the Dhammasaṅgaṇī, counts the same list (*Yevāpanakavaṇṇanā*, on Dhs §1; PTS pp. 133–134 by the CST's page markers; `abh01a.att.xml` line 5081, the same paragraph as the quotation in §2.3):

> *Iti phassādīni chappaññāsa yevāpanakavasena vuttāni navāti sabbānipi imasmiṃ dhammuddesavāre pañcasaṭṭhi dhammapadāni bhavanti … Aggahitaggahaṇena panettha phassapañcakaṃ, vitakko vicāro pīti cittekaggatā, pañcindriyāni, hiribalaṃ ottappabalanti dve balāni, alobho adosoti dve mūlāni, kāyapassaddhicittapassaddhiādayo dvādasa dhammāti samatiṃsa dhammā honti.*
>
> Thus the fifty-six beginning with contact, and the nine stated as "whatever else," make sixty-five terms in this section … Taking only what has not already been taken: the contact-pentad, initial and sustained application, rapture, one-pointedness, the five faculties, the two powers of shame and dread, the two roots of non-greed and non-hate, and the twelve beginning with bodily and mental tranquillity — these are exactly thirty phenomena.

**Thirty phenomena is consciousness plus 29 factors.** The synonym map this project fixed in advance performs the commentary's own *aggahitaggahaṇa*, "taking only what has not already been taken," and it reproduced the commentary's count exactly. The 56 the script found matches the commentary's *chappaññāsa* as well.

This cuts in two directions, and both are reported. **The count is consistent with the commentary's own — not independent of it**, since the 52-factor scheme the map targets inherits the commentarial identifications, so a map built on it could hardly do otherwise. **And it removes any novelty from the count itself.** The canon's 29 is not a finding; it is the commentary's figure, reproduced by machine. What this paper adds, if anything, is only the machine check and the chain of evidence around it.

### 7.3 · The nine are first named by the commentary, and the manual inherits them

The same commentary names the nine (*Yevāpanakavaṇṇanā*, on Dhs §1; PTS p. 132 by the CST's page marker; `abh01a.att.xml` line 5045):

> *yevāpanakavasena aparepi nava dhamme dhammarājā dīpeti. Tesu tesu hi suttapadesu 'chando adhimokkho manasikāro tatramajjhattatā karuṇā muditā kāyaduccaritavirati vacīduccaritavirati micchājīvaviratī'ti ime nava dhammā paññāyanti.*
>
> Under "whatever else," the King of Dhamma shows nine further phenomena. For in various sutta passages these nine are known: zeal, decision, attention, neutrality, compassion, appreciative joy, and abstinence from bodily, verbal and livelihood misconduct.

The formalization proves (`Canon.lean`) that **the *Saṅgaha*'s 38 for this type contains all 29 the canon names, and that what remains is exactly these nine.** In the pre-registration's editorial layers, that looks like "the manual adds nine." **Chronologically it is not.** The nine are first named for this list by the commentary — which presents them as the Buddha's (*dhammarājā dīpeti*), drawn from sutta passages — five to seven centuries before the manual. The manual inherits them as **members**, and arranges them in its own classes: manasikāra among the universals, chanda and adhimokkha among the occasionals, tatramajjhattatā among the beautiful universals, the abstinences and the illimitables as classes of their own.

```
  c. 3rd c. BCE             c. 5th c. CE                   c. 10th–12th c. CE
  ─────────────────────     ──────────────────────────     ──────────────────────────
  CANON                     COMMENTARY                     MANUAL
  Dhammasaṅgaṇī §1          Aṭṭhasālinī                    Abhidhammattha-saṅgaha
  56 terms, 29 factors      counts the 56 as 30            states 38 for this type,
  + an OPEN clause:   ───▶  (samatiṃsa, = 29 + citta)      "entering into combination"
  "ye vā pana …"            and NAMES the nine      ───▶   = 29 + the nine,
                            (as the dhammarājā's,          inherited as members,
                            from the suttas)               re-classed
                                                           ⊇ never contradicts the canon
```

The *Saṅgaha* inherits the nine as members of the list. It adds none of them, and it contradicts nothing the canon names. The inheritance itself is Nyanaponika's finding (1949, ch. 14; §7.1). The formalization's contribution is to make it **exact and checkable**: 29 + 9 = 38, with every one of the 29 inside the 38, under a synonym map fixed before the text was read.

### 7.4 · Scope of "the canon leaves nine unnamed"

The claim holds **for this type's list only.** The Dhammasaṅgaṇī names the three abstinences as path factors in its supramundane type. The commentary notes that there they are not supplied as "whatever else," *pāḷiyaṃ āgatattā* ("because they have come in the text"; *Lokuttarakusalavaṇṇanā*, PTS p. 217 by the CST's page marker; `abh01a.att.xml` line 6621). The Dhammasaṅgaṇī also names karuṇā and muditā as qualifiers of jhāna (§§258–261). Across the whole book, *adhimokkha* and *tatramajjhattatā* never appear. *Chanda* appears as a qualifier of consciousness types, *chandādhipateyya*, "with zeal dominant" (108 occurrences), much as karuṇā and muditā qualify jhāna, but never as a listed factor. *Manasikāra* appears only in other senses (*manasikārakusalatā*, *amanasikārā*).

---

## 8 · Results IV — The Cambodian Edition Against the CST

### 8.1 · The comparison

The Cambodian Buddhist Institute edition prints the Pāli with a facing Khmer translation. Its volume 78 opens the Dhammasaṅgaṇī. The list of §1 stands on its Pāli pages 16–17 (the transcription's own heading reads *padabhājanīyaṃ*). The working transcription of those pages was transliterated from Khmer script to romanized Pāli by `canon/khmer_pali.py`, then aligned with edition C, position by position, by `canon/compare.py` (both at commit `c9136e1`). The output is the standard romanized Pāli of the CST. The nearest published standard for the mapping is the ALA-LC Khmer romanization table, whose Indic letter values were built for Pāli and Sanskrit loans (ISO 11940 is the Thai-script analogue); the script's own mapping is not claimed to follow either. The paper prints romanized forms only.

Collating a Khmer-script witness of the Pāli canon against others is long-established work, and this section repeats none of it. The Sixth Council (1954–56), whose text the CST is, collated the script editions of its day, the Cambodian among them; its apparatus carries a Cambodian siglum (*kaṃ.*, 35 times in the file of the Dīgha's first volume), though none occurs anywhere in the Dhammasaṅgaṇī file, so at this passage the CST records no Cambodian reading. The Dhammachai Tipiṭaka Project (from 2010) builds a critical edition from palm-leaf manuscripts in four script traditions, with a working group for the Khom (Khmer) script. Srisetthaworakul (2019) compares Khom-script manuscripts of the Majjhimanikāya found in Thailand and in Cambodia. What §8 adds is narrow: the modern Buddhist Institute printed edition aligned term by term with the CST on one list, by a tested transliterator, with each difference classified only after the printed page and the two apparatuses were read.

**The transliterator's control.** Before use it scored 10 of 10 on these known words, chosen to cover conjuncts, the niggahita and the vowel sign Khmer Pāli uses for *iṃ* (U+17B9, KHMER VOWEL SIGN Y): *phasso · vedanā · yasmiṃ · samaye · kāmāvacaraṃ · cittassekaggatā · saddhindriyaṃ · uppannaṃ · amoho · ñāṇasampayuttaṃ*.

**The identity criterion.** Both lists are normalized the same way (Unicode NFC, lower case, final *-ṅ* to *-ṃ*, the pre-registered sandhi rule) and aligned as sequences. A position is IDENTICAL if the normalized terms are equal; CLOSE if they differ by an edit distance of at most 3 and a similarity ratio of at least 0.7 (the same term spelled differently, undecided until the printed page is read); otherwise DIFFERENT. Unmatched terms are reported as added or dropped. A CLOSE position is classified only after the printed page is checked.

**Result: C 56 terms · K 56 terms · 48 identical · 8 spelled differently · 0 added, dropped or reordered.**

### 8.2 · The eight differences, each checked against the printed page

The CST carries its own variant apparatus at Dhs §1, and it bears on these rows. It gives *viriyindriyaṃ* and *viriyabalaṃ* as the Sinhala and Thai readings (*sī. syā.*), *kāyappassaddhi* and *cittappassaddhi* as the Thai reading (*syā.*), and *kāyujjukatā*, *cittujjukatā* for two further witnesses (*sī. ka.*). It has no note on *hirī*.

| Pos. | C | K as transcribed | K as printed | CST apparatus | Classification |
|---|---|---|---|---|---|
| 37 | *hirī* | *hiri* | *hiri* | — | **edition orthography**, not documented in either apparatus |
| 39 | *kāyapassaddhi* | *kāyappassaddhi* | *kāyappassaddhi*⁽¹⁾ | *kāyappassaddhi* (Thai) | **edition orthography, recorded in K's apparatus; agrees with the Thai reading** |
| 40 | *cittapassaddhi* | *cittappasaddhi* | *cittappassaddhi*⁽²⁾ | *cittappassaddhi* (Thai) | edition orthography (*pp*), recorded in K's apparatus, agrees with the Thai reading; the single *s* is a transcription slip |
| 10 | *cittassekaggatā* | *cittaspekaggatā* | *cittassekaggatā* | — | transcription slip |
| 17 | *somanassindriyaṃ* | *somanassidṭhiyaṃ* | *somanassindriyaṃ* | — | transcription slip |
| 47 | *kāyapāguññatā* | *kāyapātuññatā* | *kāyapāguññatā* | — | transcription slip |
| 12, 25 | *vīriya-* | *viriya-* | *vīriya-* (long ī, read at moderate confidence) | *viriya-* (Sinhala, Thai) | **edition orthography or slip, undecided** — the short *i* is a real reading elsewhere; to be read from the print |

The Cambodian edition carries its own variant apparatus at the foot of the page: *"1 o. ma. kāyapassaddhi · 2 o. ma. cittapassaddhi"*. We read *o. ma.* as the Burmese (*Marammā*) reading, with a single *p*. The edition's own key to its abbreviations was not consulted, so that reading of the siglum is ours; it is consistent with the CST, whose text (the Sixth Council's, held in Burma) has the single *p* and whose apparatus attributes *-pp-* to the Thai edition. **Of the three orthographic differences, the passaddhi pair is documented in K's own apparatus against the Burmese reading, and agrees with the Thai; *hiri*/*hirī* is documented in neither.** The long-or-short *ī* of positions 12 and 25 stays open until the print is read at higher confidence.

### 8.3 · Two artifacts of the working text, reported and handled

- **Subscript order.** Some words carry the subscript RO typed before another subscript (the code-point sequence NO, COENG, RO, COENG, TO where the correct order is NO, COENG, TO, COENG, RO), which transliterates as *-inrdiyaṃ*. This is an encoding matter, not a textual one, and the transliterator normalizes it.
- **Page furniture.** At the page break, the running header of page 17 fell between *paññābalaṃ* and its *hoti*, and first produced a false DIFFERENT. Page numbers and running headers are now stripped before alignment.

### 8.4 · What the Cambodian result does and does not show

It shows that, for the densest list in the Dhammasaṅgaṇī, **the two editions agree on every term and its order**, and that their spelling differences are orthographic, and in two of three cases documented. It does not show agreement across the book, and it is not a collation in the sense of the projects named in §8.1: it uses one printed edition, not manuscripts, and one list. It rests on one passage of a working transcription, checked against the printed scan only where the two editions differed.

---

## 9 · What the Check Establishes — and the Refutation It Survived

Before this paper was drafted, its thesis was handed to a separate reviewer with no authority to rescue it and instructions to find the case that kills it. Its findings, with the author's disposition:

| Finding | Severity | Disposition |
|---|---|---|
| The nine are first named by the commentary, which predates the manual; "the manual adds nine" misattributes them | narrows, bordering on kills, for that wording | **accepted**: §7.3 now states inheritance; the project's results file carries an appended correction |
| The canon's 29 was counted by the commentary itself (*samatiṃsa*) | narrows novelty; consistent with the count | **accepted**: §7.2 reports both directions |
| The 38 is a combination count; at most 34 factors are co-present | narrows, if the paper called them co-present | **accepted**: §2.3 |
| Several rules restate the text's own sentences; "general" is a test of syntax | narrows "general" and the ratio | **accepted**: §4.3 reports each rule's extension and marks R4, R16 and R17 |
| "The text decides the dissent" overstates | contrast | **accepted**: §6 |
| "The canon leaves nine unnamed" holds for this type only | narrows | **accepted**: §7.4 |
| No computational precedent found (English, 2026-09-27) | contrast | **superseded** by the full census of 2026-09-28, which found one at generator width (§4.2) |

The full census then ran the hunt a second time, aimed at the claims rather than the thesis, and asked of each part whether it already existed, if not as software then in some other form. Four answers were yes. **The consistency test exists as a chart**: Bodhi's Table 2.4 is a hand-made incidence matrix whose margins exhibit that the two methods agree, and the tradition teaches them as two views of one structure (§2.1). **The generator exists**: a Haskell model enumerated the 89 and 121 from the same axes nine days before this one (§4.2). **The layering exists**: Nyanaponika stated it in 1949 (§7.1). **Edition collation with Khmer-script witnesses exists**: the Sixth Council, the Dhammachai Tipiṭaka Project and Srisetthaworakul (§8.1). What survived is not *checking that the two methods agree*. It is checking it by rules over axes that name no type, by kernel evaluation, against a key cited to CST paragraphs, in the text's mixed reckonings, with the breaks and the ratio; and the two one-list checks. §11 is narrowed to that.

**What survives, stated once:** a single rule set of 27 clauses shows the *Saṅgaha*'s factor-indexed statements and its type-indexed statements to be **mutually consistent**, by kernel evaluation, against the CST, and the generator's axes reproduce chapter 3's feeling and root counts. The generator's enumeration of the 89 and 121 is reported, not claimed (§4.2). The layer facts of §7 are proved in Lean; the edition facts of §8 are script-aligned and checked by hand against the printed page. **It is a consistency result, not a derivation of the *Abhidhamma* from first principles.** The author of the rules knew the tables, and the generator restates the text's axes.

---

## 10 · Pre-Registered Predictions and Their Outcomes

| ID | Prediction (as registered) | Conf. | Outcome |
|---|---|---|---|
| P-FA1 | At the manual layer, edition C: general rules generate exactly 89, and 121 with the five-jhāna expansion | 0.6 | **confirmed**: the generator yields 89/121 and the rules reproduce every stated count |
| P-FA1b | at least 3 exception rules naming a narrow class | 0.7 | **retired, unscored**: its test was never defined, and the data have been seen |
| P-FA2 | at the canon layer, the rules are under-determined or differently partitioned | 0.65 | operationalized as P-FA2a (below) |
| P-FA2a | the canon's list for the first type names exactly 29 factors, none of the nine, and closes with an open clause | 0.75 | **confirmed**; consistent with the commentary's *samatiṃsa* |
| P-FA2b | no term in that list falls outside the pre-fixed map | 0.6 | **confirmed** after the pre-registered sandhi rule (first run: 2 unmapped, disclosed) |
| P-FA3 | editions K and C agree at the manual layer | 0.85 | **cannot run as registered**: the *Saṅgaha* is not part of the Khmer Tipiṭaka, and the one Khmer-script copy held reproduces the CST's paragraph structure in all nine chapters |
| P-FA4 | compression below 0.5 | 0.5 | **confirmed**: 0.22 |
| P-FA5 | K and C name the same terms in the same order for the first type's list | 0.8 | **confirmed**: 56 = 56, 0 added, dropped or reordered |

The predictions are recorded in the public prediction register in its *Instrumented but outside the core* section. Their subject is the internal consistency of a text, not the direction value moves.

---

## 11 · Enumerated Claims

The following are disclosed and dedicated to the public domain. Together they are the survivor of the full census of 2026-09-28 (Prior-Art Statement): *a class-level rule set over the Abhidhammattha-saṅgaha's own classification axes, naming no type, that reproduces every per-type and per-factor count of its chapter 2 (and, through the axes, chapter 3's feeling and root tallies) by kernel evaluation in a proof assistant against a key cited paragraph by paragraph to the Chaṭṭha Saṅgāyana, in the text's own mixed reckonings, reported with its compression ratio and with seeded breaks each required to fail — plus a pre-registered, machine-checked inclusion of one canonical list and an alignment of that list between the Cambodian printed edition and the CST; the enumeration of the 89/121 from the axes is not part of it.* Each claim below is one part of that composition, disclosed as a part of it and narrowed to the census's wording. None is claimed apart from it, and each names its nearest prior art.

1. **A consistency test** for a classification that its source states twice, once per feature and once per class. The class–feature incidence is written as constraints over classification axes, none naming an individual class. The source's stated projections are kept in a separate key cited to paragraphs of a named edition. A proof assistant checks, by kernel evaluation, that the constraints reproduce every stated projection, in the source's own mixed bases of reckoning. *Nearest prior:* the existence problem for a 0-1 matrix with given margins (Gale 1957; Ryser 1957); constraint validation of classifications (W3C SHACL over SKOS; DELTA character matrices); and, for this source, the printed chart that shows both methods together with totals in both reckonings (Bodhi 1993, Tables 2.2–2.4). None checks constraints over axes against a paragraph-cited key by kernel evaluation; only that composition is claimed.
2. **Its application to the Theravāda *Abhidhamma***. The enumeration of the 89 and 121 types from ch. 1's axes is not claimed (nearest prior: `AloofBuddha/abhidhamma`, a Haskell model, first commit 2026-09-18, which enumerates both reckonings from the same axes, checks ch. 1's arithmetic and some ch. 3 tallies, and states that it encodes no factor-combination rules). Claimed is the 18-clause rule set over those axes reproducing every per-type and per-factor count of ch. 2, and the full ch. 3 feeling and root tallies from the axes, by kernel evaluation against the CST-cited key. Each rule's extension is reported, and the rules that restate a sentence of the text are marked (§4.3).
3. **The reporting of a compression ratio** (rule clauses ÷ generated classes) for such a formalization, as a crude description-length proxy for how far a stated classification is generated by rule rather than listed, comparable only across encodings on the same axes. *Nearest prior:* minimum description length (Rissanen 1978); implication bases in formal concept analysis (Ganter and Wille 1999). Only the application is claimed.
4. **Mutation testing applied to a formalization of a textual classification**: deliberate faults seeded in the rules, the key and the generator, each applied by script, each verified to have changed its file, each required to make the check fail. *Nearest prior:* mutation testing (DeMillo, Lipton and Sayward 1978); mutation analysis of Coq verification projects (mCoq; Celik et al. 2019), where a surviving mutant signals an incomplete specification; semantic mutation testing of OWL ontologies (Bartolini 2016; 2017). Only the application to a textual classification is claimed.
5. **The per-layer inclusion check of one canonical list**: the list mapped onto the later system's features through a synonym map fixed and published before the text is read (Appendix A), with unmapped terms reported rather than absorbed. The result is checked in the proof assistant as inclusion (every canonically named feature is in the later set) plus an exact remainder, which is then attributed to its source layer by reading, not by the editorial order. *Nearest prior:* the commentary's own count of the same list (*samatiṃsa*); Nyanaponika (1949, ch. 14), who already sets the list's terms against the nine the commentaries supply and records their incorporation into the *Saṅgaha*. Only the instrument is claimed: the synonym map fixed before reading, and the machine-checked inclusion with its exact remainder.
6. **The per-edition alignment of one canonical list** across a Khmer-script and a romanized edition, as a composition: rule-based transliteration tested on a control; normalization of encoding order and page furniture; term-by-term alignment; and classification of each difference as orthographic or as a transcription slip only after checking the printed page and the editions' own apparatus. *Nearest prior:* Aksharamukha; CollateX; ALA-LC Khmer romanization; the Sixth Council's collation of the script editions, the Cambodian included; the Dhammachai Tipiṭaka Project's Khom-script witnesses and Srisetthaworakul (2019); the CST apparatus. Only the composition, on one list of the Buddhist Institute printed edition against the CST, is claimed.
7. **Counting the cost of a recorded dissent in the source's own stated figures**: the dissent (*keci vadanti*) formalized as an alternative rule, and every stated figure it would move listed. *Nearest prior:* the ṭīkā's own argument for the main reading (the Vibhāvinī on §30), which argues the reading but does not count its cost, nor do the modern manuals count it (Nārada; Bodhi 1993, §15).

---

## 12 · Why a Value Substrate Should Carry Its Own Tests

*Tier: argument, applied to this institution's use of the canon. The deletion test passes: remove this section and §§2–11 stand.*

An autonomous agent's values will be specified in text, and text contradicts itself quietly. The practical difficulty is not that value specifications are wrong. It is that they rarely state anything twice, so a reader has little to check them against. The *Abhidhamma* is a counter-example to that condition. It states its classification twice and counts both statements. That is what a unit test is. This paper shows that one chapter's tests pass, and it shows what passing does and does not mean: consistency, not truth; a combination count, not a moment. The check concerns a classification of mind, not what a mind should do.

For Miss Aquarius, whose grounding the series describes as compiled from this canon, the consequence is modest and concrete. **The parts of the substrate that can be checked should be checked, and the checks should run again whenever an edition, a transcription or a formalization changes.** A source whose own claims are machine-verified can be inherited with more confidence than one whose claims are only repeated.

---

## 13 · Honest Limits

- **This is a consistency check, not a derivation.** The rules were written by an author who knew the tables. Three rules restate the text: R4 nearly verbatim, and R16 and R17 transcribing locus sentences. The generator restates chapter 1's axes. The evidence that the rules are not merely fitted is the profile theorems: row sums the rules were not read from. That is one test, over one chapter.
- **The key holds only stated totals.** The occurrence theorems check each rule against the sentence it was read from; the cross-method test is the profile theorems (row sums against rules read from column statements). No theorem checks a cell. Agreement at the cells rests on the rules' reading of the sampayoga sentences, which a reader checks by hand. Distinct 121 × 52 matrices can share every projection checked here.
- **The chapter 3 theorems test the generator, not the rules.** They never call the factor rules (§5.1).
- **The rule set is not unique.** Other rule sets, and other synonym maps, may reproduce the same counts. The result is that one such set exists and is short, not that it is the text's.
- **Every theorem is a finite evaluation.** The domain is 121 × 52, so a script would compute the same numbers. The kernel adds a trusted evaluator and a checked artifact, not deductive depth.
- **The compression ratio depends on the encoding** — on what counts as a clause and on which distinctions are carried by datatypes (§4.4).
- **The pre-registration proves order, not ignorance.** The author knew the *Saṅgaha*'s tables; three of the results reported were not predicted at all (§3.1).
- **The counts are combination counts.** Nothing here states how many factors are present in any actual moment of consciousness. By the commentary's count (at most one of the five variable factors at a moment), that figure is at most 34 for the first wholesome type; the 34 is derived here.
- **The layer model was mis-specified in the pre-registration.** It ordered the layers editorially (canon ⊂ manual ⊂ commentaries), and the commentary is older than the manual. The claim that survives is about inheritance, established by reading, not by the registered order.
- **The layer and edition results each rest on one list.** Neither the inclusion check nor the edition alignment has been run beyond the first type's list, and the counts check itself has been run on one edition only.
- **P-FA1b was never testable** as registered, and it is retired without a score. **P-FA3 could not be run** as registered.
- **The Cambodian comparison covers one passage**, read from a working transcription. The long *ī* of *vīriya-* at two positions was read from the scan at moderate confidence, and the short *i* is a real reading in the Sinhala and Thai witnesses, so those two positions are undecided. The siglum *o. ma.* was read as Burmese without consulting the edition's abbreviation key.
- **The CST's recension** is the Burmese tradition's; the Cambodian edition's apparatus cites the Burmese reading. Two editions that share ancestry are not independent witnesses in the textual-critical sense.
- **The census is bounded by its aperture.** The full census of 2026-09-28 searched eight languages besides English, but the engine is English-weighted, Myanmar's Abhidhamma pedagogy lives largely offline, and print-only books were outside it; its non-English nulls are weak. The Burmese ṭīkā debate on chapter 2 (Ledi Sayadaw's *Paramatthadīpanī*, the *Aṅkura-ṭīkā*) was not read, and it is the likeliest place for a counting of the §30 dissent, so claim 7's *not found* is the weakest in the paper. The census's own predictions missed in both directions: it expected the generator's neighbour in Burmese or Thai teaching software and found it in an English Haskell repository, and it did not predict Bodhi's printed chart as a neighbour of the consistency test itself.
- **The proof assistant verifies that conclusions follow from definitions.** It verifies nothing about the definitions' fidelity to the Pāli beyond what the key's citations let a reader check by hand.
- **Nothing here bears on physics.** The project that produced this paper also keeps a lens comparing the *Abhidhamma*'s discrete moments with discrete-spacetime programmes. That lens is not a claim, and it is not used here.

---

## 14 · Lineage

The commentators were already doing this. When the Aṭṭhasālinī counts the fifty-six terms of the first list, adds the nine it supplies, and then counts again "taking only what has not already been taken" to arrive at thirty, it is performing the operation this paper performs by machine: projecting an enumeration onto a smaller set of distinct phenomena and stating the size. When the *Saṅgaha* states its combinations twice, once by factor and once by type, it gives its readers the means to check one statement against the other. For centuries that check was run by students in the monastery, with the *Saṅgaha*'s verses by heart and its tables in their hands. **The counts check is that recitation, run by a different reader.** It passes where the students' check would pass, for the reasons they would give.

---

## Appendix A · The Pre-Registered Synonym Map

The map below is `PREREGISTRATION-2026-09-27b.md` §3 (commit `f4a26e5`, pushed before either edition of the Dhammasaṅgaṇī was read), reproduced without change. It is also copied verbatim into `canon/pada.py`. Each canonical term maps to one of the 52 factors, or to CITTA (consciousness itself, not a factor). A term not in the map is reported as UNMAPPED and is never mapped after the fact. The pre-registration's normalization rule, quoted: *"Grammatical variants (case, sandhi, -ṃ/-ṅ, a trailing hoti) are normalized before mapping."*

| Canonical term(s) | → |
|---|---|
| phasso | phassa |
| vedanā · sukhaṃ · somanassaṃ · somanassindriyaṃ | vedanā |
| saññā | saññā |
| cetanā | cetanā |
| cittaṃ · viññāṇaṃ · mano · mānasaṃ · hadayaṃ · paṇḍaraṃ · manāyatanaṃ · manindriyaṃ · viññāṇakkhandho · tajjāmanoviññāṇadhātu | CITTA |
| vitakko · sammāsaṅkappo | vitakka |
| vicāro | vicāra |
| pīti | pīti |
| cittassekaggatā · samādhindriyaṃ · samādhibalaṃ · sammāsamādhi · samatho · avikkhepo | ekaggatā |
| saddhā · saddhindriyaṃ · saddhābalaṃ | saddhā |
| vīriyaṃ · vīriyindriyaṃ · vīriyabalaṃ · sammāvāyāmo · paggāho | vīriya |
| sati · satindriyaṃ · satibalaṃ · sammāsati | sati |
| paññā · paññindriyaṃ · paññābalaṃ · amoho · sammādiṭṭhi · sampajaññaṃ · vipassanā | paññā |
| jīvitindriyaṃ | jīvitindriya |
| hirī · hiribalaṃ | hiri |
| ottappaṃ · ottappabalaṃ | ottappa |
| alobho · anabhijjhā | alobha |
| adoso · abyāpādo | adosa |
| kāya-/citta- passaddhi · lahutā · mudutā · kammaññatā · pāguññatā · ujukatā (12 terms) | the 12 paired beautiful factors, each to its own |

Nineteen rows: 18 factor targets plus CITTA, where the last row stands for twelve factors. So the map can name at most 29 distinct factors (17 + 12), and P-FA2a predicted that the list would name all of them and nothing else. The sandhi case the first run missed (*kāyujukatā*, *cittujukatā* for *kāya-ujukatā*, *citta-ujukatā*) falls under the quoted rule; its implementation in `pada.py` is commented as added after the first run.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/the-counts-check> |
| GitHub (paper) | <https://github.com/thonly/publications/blob/main/defensive-publications/the-counts-check.md> |
| GitHub (formalization, CC0) | <https://github.com/SiliconWat/formal-abhidhamma> (files cited at commit `c9136e1`) |
| Pre-registrations | `PREREGISTRATION.md` (commit `259e5e8`) · `PREREGISTRATION-2026-09-27b.md` (commit `f4a26e5`) |
| Census pre-registration (public) | `thonly/publications` commit `9bf6a3d`, `timestamps/census/counts-check-full-prereg.md` |
| Results and corrections | `RESULTS.md` (commits `b9070d4`, `c5c77fb`, `ada7a20`, `74e19fe`, `c9136e1`) |
| Prediction register | <https://thonly.org/research/program/register> (P-FA1 … P-FA5) |
| Internet Archive | <https://web.archive.org/web/2026*/thonly.org/research/the-counts-check> |

---

## Acknowledgments

The author thanks his father, with whom the transcription of the Cambodian Tipiṭaka proceeds page by page, and whose transcription of volume 78 made §8 possible; the corrections §8.2 records are offered to that work, not against it. Thanks go to the Buddhist Institute, Phnom Penh, whose edition this is; to the Vipassana Research Institute for the Chaṭṭha Saṅgāyana texts it gives away; to the donors of the scanned volumes (Kang Huychan and family, Lok Kru Aggapaṇḍita But Savong, Srong Chanda, and 5000-years.org), whose dedication travels with any use of them; to Bhikkhu Bodhi and U Nārada, whose editions of the *Saṅgaha* made the first two collations possible; and to the Lean community. The formalization, collation and drafting were done with Miss Aquarius, the name under which this institution discloses its AI collaboration.

---

## Citations

1. Anuruddha. *Abhidhammatthasaṅgaha*. Chaṭṭha Saṅgāyana edition, Vipassana Research Institute, `github.com/VipassanaTech/tipitaka-xml` (commit `0854d11`), `romn/abh07t.nrf.xml` (ch. 2 §12–§58; ch. 3 §3–§17). The same file carries the *Abhidhammatthavibhāvinī-ṭīkā* after the *Saṅgaha* (cited here on ch. 2 §30).
2. *Dhammasaṅgaṇī*. Chaṭṭha Saṅgāyana edition, `romn/abh01m.mul.xml` (§1, with its variant apparatus; §§258–262).
3. Buddhaghosa (attrib.). *Aṭṭhasālinī*. Chaṭṭha Saṅgāyana edition, `romn/abh01a.att.xml`: *Yevāpanakavaṇṇanā* on Dhs §1 (PTS pp. 132–134 by the CST's page markers; lines 5045, 5081) and *Lokuttarakusalavaṇṇanā* (PTS p. 217; line 6621).
4. *Braḥ Traipiṭaka* (the Cambodian Tipiṭaka), Buddhist Institute, Phnom Penh; vol. 78, *Abhidhammapiṭaka, Dhammasaṅgaṇī*, part 1, pp. 16–17.
5. Bodhi, Bhikkhu (ed.) (1993/2000). *A Comprehensive Manual of Abhidhamma*. Buddhist Publication Society. (Its introduction is the source of the datings in §3.5. Ch. 2, Tables 2.2 (association), 2.3 (combination) and 2.4 (both together), with the Guide to §30 in its numbering, are the nearest prior art for the consistency test; its §15 reports the *keci vadanti* dissent without counting it.)
6. Nārada Mahā Thera (trans.). *A Manual of Abhidhamma*. Buddhist Missionary Society; the Pāli-and-English text consulted as mirrored at `palikanon.com`.
7. Karunadasa, Y. (2010). *The Theravāda Abhidhamma*. Centre of Buddhist Studies, University of Hong Kong.
8. de Moura, L. & Ullrich, S. (2021). "The Lean 4 Theorem Prover and Programming Language." *CADE-28*.
9. takuya50 / Nimble Ariake (2026). *buddhist-comparative-logic*, v0.1.0. `github.com/takuya50/buddhist-comparative-logic`; software DOI 10.5281/zenodo.22851717. (The nearest prior art: machine-checked Buddhist formalizations of Mahāyāna and pramāṇa texts.)
10. PJ-Oliveira. *abhidhamma*. `github.com/PJ-Oliveira/abhidhamma`. (Interactive citta-vīthi simulator, cetasika analyzer and Paṭṭhāna matrix.)
11. *The Ephemeral Projector — A Comparative Analysis of Quantum Mechanics and Abhidhamma*. ResearchGate 397427972. (The nearest physics-comparison neighbour; not used here.)
12. Ly, T. & Miss Aquarius (2026). "The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification." *The Abhidhamma Compiled* №1. thonly.org. (§4.2 is the claim this paper tests.)
13. Ly, T. & Miss Aquarius (2026). "Twenty-Four Kinds of Because: The Paṭṭhāna as a Typed-Causation Vocabulary for AI Alignment." *The Abhidhamma Compiled* №2. thonly.org.
14. Ly, T. & Miss Aquarius (2026). "One of One: Individuation Without Essence." *The Abhidhamma Compiled* №3. thonly.org.
15. Ly, T. & Miss Aquarius (2026). *The Prediction Register*. thonly.org/research/program/register (P-FA1 … P-FA5).
16. Gale, D. (1957). "A theorem on flows in networks." *Pacific Journal of Mathematics* 7(2), 1073–1082.
17. Ryser, H. J. (1957). "Combinatorial properties of matrices of zeros and ones." *Canadian Journal of Mathematics* 9, 371–377.
18. DeMillo, R. A., Lipton, R. J. & Sayward, F. G. (1978). "Hints on Test Data Selection: Help for the Practicing Programmer." *Computer* 11(4), 34–41.
19. Rissanen, J. (1978). "Modeling by shortest data description." *Automatica* 14(5), 465–471.
20. Ganter, B. & Wille, R. (1999). *Formal Concept Analysis: Mathematical Foundations*. Springer.
21. Rajan, V. *Aksharamukha* (script converter, including Khmer). `github.com/virtualvinodh/aksharamukha`.
22. Haentjens Dekker, R., Middell, G. et al. *CollateX* (Interedition). `collatex.net`.
23. Nyanaponika Thera (1949). *Abhidhamma Studies: Researches in Buddhist Psychology*. Colombo: Frewin. Later ed., *Abhidhamma Studies: Buddhist Explorations of Consciousness and Time*, ed. Bhikkhu Bodhi, Wisdom Publications, 1998.
</content>
</invoke>
24. AloofBuddha. *abhidhamma: a Haskell model of Theravāda Abhidhamma consciousness and dependent origination*. `github.com/AloofBuddha/abhidhamma` (repository created and first commit `026819b`, 2026-09-18; no licence file). (The nearest prior art for the enumeration of the 89 and 121: `allCittas89` and `allCittas121` in `src/Abhidhamma/Cittasangaha.hs`, checks in `test/Check.hs`; its stated "Known gap" on factor combination is in `src/Abhidhamma/Citta.hs`.)
25. Celik, A., Palmskog, K., Parovic, M., Gallego Arias, E. J. & Gligoric, M. (2019). "Mutation Analysis for Coq." *34th IEEE/ACM International Conference on Automated Software Engineering (ASE 2019)*. Tool paper: Jain, K., Palmskog, K., Celik, A., Gallego Arias, E. J. & Gligoric, M. (2020). "mCoq: Mutation Analysis for Coq Verification Projects." *ICSE 2020 Companion*, doi:10.1145/3377812.3382156.
26. Bartolini, C. (2016). "Mutating OWLs: Semantic Mutation Testing for Ontologies." *AMARETTO workshop, MODELSWARD 2016*.
27. Bartolini, C. (2017). "Software Testing Techniques Revisited for OWL Ontologies." In *Model-Driven Engineering and Software Development*, Communications in Computer and Information Science, Springer, pp. 132–153.
28. W3C (2017). *Shapes Constraint Language (SHACL)*. W3C Recommendation, 20 July 2017. · W3C (2009). *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009.
29. Dallwitz, M. J. *DELTA: DEscription Language for TAxonomy*. CSIRO; adopted as a data standard by TDWG (Biodiversity Information Standards) in 1988. `tdwg.org/standards/delta`.
30. Nyanaponika Thera (1949), as ref. 23: ch. 14, "The Supplementary Factors (ye-vā-panaka, F57–65)", and the list with its supplements numbered 1–65 in the chapter on the Dhammasaṅgaṇī's list. (The census control; the layering of §7 in print.)
31. The Sixth Buddhist Council (*Chaṭṭha Saṅgāyana*), Yangon, 1954–56, whose text is edition C; its apparatus cites the Sinhala (*sī.*), Thai (*syā.*), Cambodian (*kaṃ.*) and PTS (*pī.*) editions.
32. Dhammachai Tipiṭaka Project (2010–). A critical edition of the Pāli canon from palm-leaf manuscripts in the Sinhala, Burmese, Khom (Khmer) and Tham scripts. `dhammachaitipitaka.org`.
33. Srisetthaworakul, S. (2019). "Comparison of the Khom Script Manuscripts of the Majjhimanikāya Found in Thailand and Cambodia." *Journal of Indian and Buddhist Studies (Indogaku Bukkyōgaku Kenkyū)*.
34. Library of Congress. *ALA-LC Romanization Tables: Khmer*. (The nearest romanization standard; ISO 11940 is its Thai-script analogue.)
35. Kyaw, Pyi Phyo (2014). *Paṭṭhāna (Conditional Relations) in Burmese Buddhism*. PhD thesis, King's College London; ch. 5, the mathematics of the Paṭṭhāna and combinatorics. (A contrast for §4.4: an *Abhidhamma* enumeration read as combinatorics.)
36. Nearer software neighbours named in the Prior-Art Statement: `suchanon456/Cyber-Abhidhamma` (first commit 2026-09-14); `juncoflockleader/Abhidharma` (2024); `dangerzig/tipitaka.critical` (2026). Patents recorded, claims not read: US8990746B1 (Cadence Design Systems); US20240419880A1 (IBM).
