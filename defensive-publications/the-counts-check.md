---
title: "Machine-Checked Consistency of a Buddhist Classification: Lean Theorems for the Abhidhamma's 89 and 121 Types of Consciousness — The Counts Check"
subtitle: "A pre-registered formalization of the Abhidhammattha-saṅgaha's combination rules, collated against the Chaṭṭha Saṅgāyana, the canon's own list, its commentary, and the Cambodian edition"
authors: "Thon Ly · Miss Aquarius℠"
type: "Defensive Publication"
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

- the 89 and the 121;
- every per-type combination count in chapter 2;
- every per-factor count in chapter 2, in the text's own mixed reckonings;
- chapter 3's counts by feeling and by root.

Nine deliberate breaks each make the check fail. What this establishes is **mutual consistency**: the chapter's two methods, factor by factor (*sampayoga-naya*) and type by type (*saṅgaha-naya*), agree with each other and with chapter 3, under a single rule set of 27 clauses for 121 types. It is not a derivation independent of the text.

Three further results concern textual layers and editions:

- **The canon's own list** for the first wholesome sense-sphere type (Dhammasaṅgaṇī §1) names **29** distinct factors under a synonym map fixed before the text was read. That map **reproduces the count the fifth-century commentary itself gives** (the Aṭṭhasālinī's *samatiṃsa dhammā*, thirty with consciousness).
- **The *Saṅgaha*'s 38 for that type is exactly those 29 plus the nine factors the commentary names** under the canon's open clause *"ye vā pana"*. The *Saṅgaha* inherits the nine; it does not add them.
- **The Cambodian Buddhist Institute edition names the same 56 terms, in the same order, as the CST** for that list. Every spelling difference was checked against the printed page.

Each result was pre-registered, with the predictions pushed to a public repository before any code was written or any text read. The predictions are entered in the public prediction register.

**Keywords:** formal verification, Lean theorem prover, Abhidhamma, Abhidhammattha-saṅgaha, Buddhist philosophy of mind, classification consistency, combinatorial enumeration, textual criticism, Pāli canon, Dhammasaṅgaṇī, Aṭṭhasālinī, Khmer Tipiṭaka, pre-registration, defensive publication.

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
| *pada-bhājanīya* | the canonical enumeration of terms present in one class |
| *yevāpanaka* (the "or whatever else" factors) | features supplied by a commentary for an open clause in a canonical list |
| *aggahitaggahaṇa* ("taking what is not yet taken") | deduplication of a list under synonymy |
| edition K / edition C | the Cambodian Buddhist Institute edition / the Chaṭṭha Saṅgāyana (VRI) edition |
| layer | an editorial stratum of the text: canon · the *Saṅgaha* · the commentaries |

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. **The authors and HeartBank® will not seek patent** on any method, formalization, rule set, protocol, software or result herein. The formalization, the key, the transliterator and the alignment scripts are published under CC0 at `github.com/SiliconWat/formal-abhidhamma`.

**The census (ruling of 2026-09-13).** A quick novelty census ran on 2026-09-27. Its predictions and a known-prior-art control were pushed before the first query. Its aperture: the commercial web, non-commercial sources (dharma websites, apps, GitHub, digital-humanities projects), Google Patents by keyword, and arXiv and Google Scholar by keyword. **English only. Burmese, Thai, Sinhala and Khmer were not searched**, and the living Abhidhamma pedagogies of Myanmar are exactly where charts and software would be expected. The control (Rovelli's relational quantum mechanics read alongside Nāgārjuna) was found, so the NOT FOUND rows stand for that aperture on that date. By conjunct:

| Conjunct | Verdict | Prior art |
|---|---|---|
| (a) the citta/cetasika system encoded as a computable structure | **NARROWS** | `PJ-Oliveira/abhidhamma` (a citta-vīthi simulator, a cetasika analyzer comparing factors per type, a Paṭṭhāna matrix); the traditional citta × cetasika combination charts in Abhidhamma teaching |
| (b) such an encoding machine-checked in a proof assistant | **NARROWS** | `takuya50/buddhist-comparative-logic` (Lean 4 and Isabelle/HOL, released 2026-09-20): the Heart Sutra, Madhyamaka, Buddhist epistemology, Yogācāra, with the skandhas, āyatanas, dhātus and nidānas as datatypes. No Theravāda types of consciousness, no factor combinations, no counts |
| (c) the 89/121 derived from general rules as a consistency test | **NARROWS** | the tradition's own expansion of 89 to 121 by the five jhānas; the *Saṅgaha*'s own two methods (the check here is that they agree); **the Aṭṭhasālinī's own count of the first type's list (*samatiṃsa dhammā*), which this paper's canonical count reproduces** |
| (d) the check run per edition and per textual layer | **NOT FOUND** at this depth | — |
| (e) the discrete-moment Abhidhamma compared with discrete-spacetime physics | **NARROWS** | *The Ephemeral Projector — A Comparative Analysis of Quantum Mechanics and Abhidhamma*; the Buddhism-and-physics literature. This paper makes **no** physics claim |
| the composition of (a)–(d) | **NOT FOUND** at this depth | — |

No live patent or published application was found for any conjunct, so **no conjunct is enclosed.** **The survivor, and the only thing this paper claims:** *a machine-checked derivation of the Theravāda citta counts from general cetasika constraints, with its compression ratio, run per edition and per textual layer.* The enumerated claims (§11) are that survivor and nothing wider. A full census runs before this paper's first deposit.

⛔ **Nothing here is claimed as *new*, *first* or *unprecedented*.** Where a sentence says a thing was *not found*, it means not found in the aperture above on 2026-09-27.

---

## 1 · Mission Frame: A Compiled Specification Must Check

The series *The Abhidhamma Compiled* rests on a thesis stated in its first paper (*The Wheel That Unwinds the Wheel*, §3). Every era compiles the Abhidhamma into its own machine language, and ours is the first in which the compiled form can be executed. The *Abhidhamma* is read there as a process specification: typed elements (*citta*, *cetasika*, *rūpa*) arising and ceasing under typed conditions, with ethical weight tracked per element. The series' gate for a satellite paper is that the canonical material must yield a usable artifact: a formalism, a test, a taxonomy, or a protocol.

This paper supplies a **test**, and the test is aimed at the series' own words. Paper №1, §4.2, published in 2026, says:

> The Abhidhamma enumerates exactly 89 (by fuller reckoning 121) citta-types, classified by plane, by ethical class, and by composition from the 52 cetasikas.

That sentence makes a checkable claim. *By composition* means the types and their factors are related by rule. If the relation is by rule, the rule can be written down, and a machine can check whether it produces what the text says. If it does not, either the rule was lost in transmission, or it was never stated, or the series' description of its own source is wrong. **The first paper asserted the property; this paper checks it.**

Three reasons make the check worth doing, beyond the series' own consistency.

**First, a specification with unit tests.** Miss Aquarius's grounding in the Tipiṭaka treats the canon as a value substrate: a specification of what a mind is and what it should do. Most value specifications offered for artificial agents are natural-language documents with no internal checks at all. The *Abhidhamma* is unusual. **It carries its own test cases**: the stated counts. A list that says 38 factors combine with this type, and a second passage that says factor F occurs in 55 types, are two projections of one incidence structure. They can disagree. Whether they do is a fact about the specification, and it can be settled by machine. A value substrate whose internal claims can be checked is a better substrate than one whose claims cannot.

**Second, a template for the rest of the corpus.** The method — pre-register the predictions, separate the answer key from the rules, test the checker on a known failure, cite every figure to a paragraph of a named edition — transfers to any classification the tradition states twice. The *Saṅgaha*'s later chapters (the cognitive process, rebirth-linking, matter, conditions) are full of such statements.

**Third, the editions.** The Khmer Tipiṭaka is being transcribed page by page, by hand, by a father and son. A formalization that can be run against two editions can find a variant that changes the logic, if one exists. It can also confirm, as it does here for the first list it was run on, that none does.

---

## 2 · The Object

### 2.1 · The two methods of chapter 2

Chapter 2 of the *Abhidhammattha-saṅgaha* (*cetasika-saṅgaha-vibhāga*) states the relation between the 52 factors and the 89/121 types twice.

**The method of association** (*sampayoga-naya*, CST ch. 2 §13–§34) goes factor by factor. For example:

> *Vitakko tāva dvipañcaviññāṇavajjitakāmāvacaracittesu ceva ekādasasu paṭhamajjhānacittesu cāti pañcapaññāsacittesu uppajjati.* (§13)
>
> Initial application arises in fifty-five types: the sense-sphere types except the twice-five sense-consciousnesses, and the eleven first-jhāna types.

It closes with a verse (§19) giving the counts for the six occasional factors, with and without:

> *Chasaṭṭhi pañcapaññāsa, ekādasa ca soḷasa; Sattati vīsati ceva, pakiṇṇakavivajjitā. Pañcapaññāsa chasaṭṭhiṭṭhasattati tisattati; Ekapaññāsa cekūnasattati sapakiṇṇakā.*

In figures: 66, 55, 11, 16, 70 and 20 types lack the occasionals, and 55, 66, 78, 73, 51 and 69 have them.

**The method of inclusion** (*saṅgaha-naya*, §35–§58) goes type by type. For example:

> *Chattiṃsa pañcatiṃsa ca, catuttiṃsa yathākkamaṃ. Tettiṃsadvayamiccevaṃ, pañcadhānuttare ṭhitā.* (§37)
>
> Thirty-six, thirty-five, thirty-four in order, and thirty-three twice: thus fivefold in the supramundane.

The two methods describe one incidence structure. Call it a 121 × 52 matrix of which types carry which factors. The first method states its **column sums**; the second states its **row sums**, grouped. Neither states the matrix.

```
                        52 factors (cetasika)
                ┌───────────────────────────────┐
   121 types    │                               │──▶ row sums:  38, 37, 37, 36 …
   (citta)      │   the incidence the text      │    (saṅgaha-naya, §35–§58)
                │   never writes down whole     │
                └───────────────────────────────┘
                                │
                                ▼
                  column sums: 55, 66, 78, 73, 51, 69 …
                  (sampayoga-naya, §13–§34)

   ch. 3 adds two more projections of the same types:
     by feeling (§3–§9):  pleasure 1 · pain 1 · displeasure 2 · joy 62 · equanimity 55
     by root   (§10–§17): rootless 18 · one-rooted 2 · two-rooted 22 · three-rooted 47
```

**The counts check** asks whether a single matrix exists that has all of these projections at once. It also asks whether that matrix can be written as rules over classes, rather than as a table.

### 2.2 · The text mixes its reckonings

A detail that any check must respect: the text counts the jhāna-dependent factors (vitakka, vicāra, pīti) and the feelings **over 121**, and all other factors and the roots **over 89**. The reason is that the 89 reckoning counts each supramundane type once, while the presence of vitakka, vicāra and pīti depends on the jhāna the supramundane type is reckoned at. A key that reads every figure on one basis records false mismatches. The first draft of this project's key, built from memory before it was collated, did exactly that. It read 78, 73 and 69 as 110, 105 and 101, which are the same facts counted over 121.

### 2.3 · Combination, not co-presence

A second detail, identified by the adversarial reading this paper underwent before drafting (§9). **The counts the *Saṅgaha* gives are combination counts, not co-present sets.** It says the factors *saṅgahaṃ gacchanti*, "enter into combination." It says the abstinences and the illimitables *paccekameva yojetabbā*, "are to be fitted in severally." Its verse at §33 lists the factors that arise *nānā kadāci*, "separately and occasionally": envy, avarice, remorse, the abstinences, compassion and appreciative joy, conceit, and sloth-and-torpor. The commentary is explicit about the first wholesome type. Of its 65 listed terms, *ekakkhaṇe kadāci ekasaṭṭhi … kadāci samasaṭṭhi* (Aṭṭhasālinī, CST `abh01a` line 5081): **at one moment, sometimes 61, sometimes 60.** At most one of its five variable factors is present at once.

So the 38 of §40 is the size of the **combination**: every factor that can join this type on some occasion. The most factors ever present together in that type is 34. The formalization reproduces the text's combination counts, which is what the text states. Nothing here is a claim about the size of any actual moment.

---

## 3 · Method

### 3.1 · Pre-registration, as a property

The protocol's first rule: **the predictions go public before the code exists.** The first pre-registration (`PREREGISTRATION.md`, commit `259e5e8`) was pushed to a public repository with GitHub recording the push at 2026-09-27T22:07:02Z, before a line of formalization was written. The second (`PREREGISTRATION-2026-09-27b.md`, commit `f4a26e5`, push 23:04:29Z) was pushed before either edition of the Dhammasaṅgaṇī was read. Both are entered in the institution's public prediction register, which carries its own OpenTimestamps, RFC 3161 and Zenodo record. A local commit date can be set by hand; a push record cannot. So "before any data" is a **property** of the record rather than an assertion about it.

The pre-registration fixed, in advance:

- the definitions of *general rule*, *generated set*, *compression ratio*, *layer* and *edition*;
- a control with a known answer, and a deliberate failure that must fail;
- five predictions with confidences and falsifiers;
- kill and reopen criteria;
- for the canonical list, **the entire synonym map**, together with the rule that a term outside it is reported as unmapped, never mapped after the fact.

### 3.2 · The key is separate from the rules

The rules and the answer key live in different files. The rules (`Rules.lean`) are constraints over classification axes. The key (`AnswerKey.lean`) holds only figures the text states, each cited to its CST paragraph, and no figure the text does not state. The check (`Check.lean`) asserts that the rules' projections equal the key. The separation is what makes a pass informative. A rule set allowed to read the key could restate it.

### 3.3 · The instrument is tested on a known answer and a known failure

Before the rule set was trusted, it was run on a case whose answer was certain: the eight wholesome sense-sphere types. They form a product of three binary axes (joyful or equanimous feeling × with or without knowledge × unprompted or prompted), and their traditional maximum combinations are 38, 37, 37 and 36 by pair. Then a rule was deleted on purpose (*pīti arises only with joyful feeling*), and the check had to fail. It did: Lean reported that `decide` had proved the profile theorem **false**. The instrument could see. The same discipline runs over the full formalization (§5.3).

### 3.4 · Which guards are properties, and which are only rules

A guard that needs someone's restraint at the moment it is tested is a rule. A guard that holds whether or not anyone is careful is a property. Remove the enforcer and see which break:

| Guard | Kind | Why |
|---|---|---|
| predictions precede data | **property** | GitHub's push record is written by the host, not the author, and cannot be backdated |
| the breaks keep testing the checker | **property of the harness** | `run.sh` re-applies all nine breaks on every run, and refuses a break whose edit changed nothing |
| a figure is the text's, not the author's | **checkable rule** | each key figure carries a CST paragraph number; any reader can check it, but nothing forces a future editor to add one |
| the rules never read the key | **rule** | separate files, but nothing stops a future author from importing the key into the rules. ⚠️ The ch. 3 theorems are the partial remedy: a second key the rules were not written against |
| no Khmer-edition text is published | **rule** | the scripts print only single romanized terms and counts, but a future contributor could commit the transcription itself |

Two of the five are properties. The other three are rules, and they are named as such, so that whoever inherits the repository knows which of them depend on care.

### 3.5 · Editions and layers

Two editions:

- **C, the Chaṭṭha Saṅgāyana**: the Vipassana Research Institute's digital text, `github.com/VipassanaTech/tipitaka-xml`. The files used: `romn/abh07t.nrf.xml` (the *Abhidhammatthasaṅgaha*), `romn/abh01m.mul.xml` (the Dhammasaṅgaṇī), `romn/abh01a.att.xml` (the Aṭṭhasālinī).
- **K, the Cambodian Buddhist Institute edition** of the Tipiṭaka, volume 78 (the Dhammasaṅgaṇī, part 1). It was read from a working transcription made page by page from the printed volume, and checked against a scan of the printed page.

Three editorial layers: the **canon** (the Dhammasaṅgaṇī); the **manual** (the *Abhidhammattha-saṅgaha*); and the **commentaries** (the Aṭṭhasālinī). ⚠️ **The pre-registration ordered these as canon ⊂ canon + manual ⊂ canon + manual + commentaries. That order is editorial, not chronological.** The Aṭṭhasālinī (c. 5th century) predates the *Saṅgaha* (c. 10th–12th). §7 shows why this matters.

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

The generator **restates chapter 1's axes; it does not discover them.** What it shows is that 89 and 121 are exactly the product structure of those axes, in nine clauses.

### 4.3 · The rules — eighteen clauses, with their extensions

Each rule is a constraint over the axes. None names an individual type. But a constraint that names no type can still pick out only one or two types, so the table reports each rule's **extension**: the number of types, over 89 and over 121, in which the factor it governs occurs. It also marks the rules that **transcribe a locus sentence of the text** rather than generalize from a principle.

| Rule | Factor(s) | Constraint | Extension (89 / 121) | Source |
|---|---|---|---|---|
| R1 | the 7 universals | every type | 89 / 121 | §2 |
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
| R16 | the 3 abstinences | sense-sphere wholesome, or supramundane | 16 / 48 | §29 — ⚠️ **transcribes the locus sentence** |
| R17 | karuṇā, muditā | sense-sphere non-resultant, or fine-material to the 4th jhāna | 28 / 28 | §30 — ⚠️ **transcribes the locus sentence** |
| R18 | paññā | beautiful and knowledge-associated | 47 / 79 | §31 |

Two observations. **R5 is where the formalization is more compressed than the text.** §16 excludes energy by naming four classes one by one: *pañcadvārāvajjana-dvipañcaviññāṇa-sampaṭicchana-santīraṇa-vajjita*. R5 states one rule over the element axis, and the two are extensionally equal. **R16 and R17 are where it is not**: they transcribe the text's locus sentences, so matching 16 and 28 from them is a restatement, not a derivation. Even so, R17's boundary at the 4th jhāna has canonical support independent of the *Saṅgaha*: the Dhammasaṅgaṇī names karuṇā- and muditā-accompanied jhāna from the first to the fourth (§§258–261), and places equanimity alone at the final jhāna (§262).

### 4.4 · Compression

At 121 rows, **27 clauses** (9 + 18) give a ratio of **0.22**. Counting G5's three written-out members singly gives 29 ÷ 121 = 0.24; over 89 the ratio is 0.30. The ratio depends on what counts as a clause. The registered definition (clauses in the rule file, datatype declarations excluded) is the one reported.

---

## 5 · Results I — The Chapter Checks Against Itself

### 5.1 · The theorems

All are proved by `decide`: the Lean kernel evaluates the statement, and no compiled code is trusted.

| Theorem | Statement |
|---|---|
| `n89` · `n121` | the generator yields exactly 89 and 121 types |
| `distinct121` | no two types are the same point |
| `profile89` | the rules give every per-type count of ch. 2: greed-rooted 19 · 21 · 19 · 21 · 18 · 20 · 18 · 20 · hate-rooted 20 · 22 · delusion-rooted 15 · 15 · rootless 7 ×5 · 10 · 10 · 7 ×5 · 10 · 11 · 10 · 10 · 11 · 12 · beautiful sense-sphere 38 · 38 · 37 ×4 · 36 · 36 / 33 · 33 · 32 ×4 · 31 · 31 / 35 · 35 · 34 ×4 · 33 · 33 · fine-material 35 · 34 · 33 · 32 · 30 (×3) · immaterial 30 ×12 · supramundane 36 ×8 |
| `profile121` | the same, with the supramundane at 36 · 35 · 34 · 33 · 33 (×8) |
| `occurrences89` · `absences89` | every per-factor count over 89: universals 89 · adhimokkha 78 · vīriya 73 · chanda 69 (without: 11 · 16 · 20) · unwholesome 12 · 8 · 4 · 4 · 2 · 5 · 1 · beautiful universals 59 · abstinences 16 · illimitables 28 · paññā 47 |
| `occurrences121` · `absences121` | the factors counted over 121: vitakka 55 · vicāra 66 · pīti 51 (without: 66 · 55 · 70) |
| `feelings121` | ch. 3: pleasure 1 · pain 1 · displeasure 2 · joy 62 · equanimity 55 |
| `roots89` | ch. 3: rootless 18 · one-rooted 2 · two-rooted 22 · three-rooted 47 |
| `keci_reading` | the dissent recorded at §30 gives 20, not 28 (§6) |

**Every figure matched on the first collation against the CST.** The ch. 3 theorems are the strongest of the set. They test the generator's own feeling and root axes against a chapter the generator was not built from, and they pass without any change to the generator.

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

A checker that has only ever passed is an untested claim. These breaks are what let the passes be read as evidence.

---

## 6 · Results II — A Dissent the Text Records

At §30, having located the illimitables in 28 types, the *Saṅgaha* adds:

> *upekkhāsahagatesu panettha karuṇāmuditā na santīti keci vadanti.*
>
> Some say compassion and appreciative joy are absent here from the types accompanied by equanimity.

Formalized as an alternative rule, the dissent gives **20**, not 28. The 28 sits in the same sentence the dissent qualifies, so **the text does not decide between the readings.** What the formalization establishes is narrower and still useful: **the author's stated figures — the 28, and the 37 and 36 for the equanimous knowledge-associated pairs — encode the main reading, not the dissent.** A reader who adopts the *keci* reading must change four stated counts in chapter 2, not one. That is a fact about the dissent's cost that the prose leaves implicit.

---

## 7 · Results III — The Canon, the Commentary and the Manual

### 7.1 · What the canon names

The Dhammasaṅgaṇī opens its first analysis of a wholesome type (§1) with a list of what is present *"yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ"*. It runs from *phasso hoti, vedanā hoti* to *paggāho hoti, avikkhepo hoti*, and closes:

> *ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā — ime dhammā kusalā.*
>
> or whatever other conditioned immaterial phenomena there are at that time — these phenomena are wholesome.

Under the synonym map fixed in the pre-registration, the list gives **56 terms, 29 distinct factors, and none of** *chanda, adhimokkha, manasikāra, tatramajjhattatā, karuṇā, muditā* or the three abstinences. The first run reported two unmapped terms, *kāyujukatā* and *cittujukatā*. Both are sandhi forms (kāya + ujukatā), and the pre-registration required sandhi to be normalized before mapping; the script had not implemented that case. With it, zero terms are unmapped. The detector for the nine was itself tested on a control list naming four of them in inflected forms, and it caught all four.

### 7.2 · The commentary had already counted it

The Aṭṭhasālinī, the fifth-century commentary on the Dhammasaṅgaṇī, counts the same list (CST `abh01a` line 5081):

> *Iti phassādīni chappaññāsa yevāpanakavasena vuttāni navāti sabbānipi imasmiṃ dhammuddesavāre pañcasaṭṭhi dhammapadāni bhavanti … Aggahitaggahaṇena panettha phassapañcakaṃ, vitakko vicāro pīti cittekaggatā, pañcindriyāni, hiribalaṃ ottappabalanti dve balāni, alobho adosoti dve mūlāni, kāyapassaddhicittapassaddhiādayo dvādasa dhammāti samatiṃsa dhammā honti.*
>
> Thus the fifty-six beginning with contact, and the nine stated as "whatever else," make sixty-five terms in this section … Taking only what has not already been taken: the contact-pentad, initial and sustained application, rapture, one-pointedness, the five faculties, the two powers of shame and dread, the two roots of non-greed and non-hate, and the twelve beginning with bodily and mental tranquillity — these are exactly thirty phenomena.

**Thirty phenomena is consciousness plus 29 factors.** The synonym map this project fixed in advance is the commentary's own *aggahitaggahaṇa*, "taking only what has not already been taken," and it reproduced the commentary's count exactly. The pre-registered 56 matches the commentary's *chappaññāsa* as well.

This cuts in two directions, and both are reported. **It corroborates P-FA2a** against an independent key 1,500 years older than the prediction. **It removes any novelty from the count itself.** The canon's 29 is not a finding; it is the commentary's figure, reproduced by machine. What is new, if anything, is only the machine check and the chain of evidence around it.

### 7.3 · The nine are the commentary's, and the manual inherits them

The same commentary names the nine (line 5045):

> *yevāpanakavasena aparepi nava dhamme dhammarājā dīpeti. Tesu tesu hi suttapadesu 'chando adhimokkho manasikāro tatramajjhattatā karuṇā muditā kāyaduccaritavirati vacīduccaritavirati micchājīvaviratī'ti ime nava dhammā paññāyanti.*
>
> Under "whatever else," the King of Dhamma shows nine further phenomena. For in various sutta passages these nine are known: zeal, decision, attention, neutrality, compassion, appreciative joy, and abstinence from bodily, verbal and livelihood misconduct.

The formalization proves (`Canon.lean`) that **the *Saṅgaha*'s 38 for this type contains all 29 the canon names, and that what remains is exactly these nine.** In the pre-registration's editorial layers, that looks like "the manual adds nine." **Chronologically it is not.** The nine are the commentary's, five to seven centuries before the manual:

```
  c. 3rd c. BCE             c. 5th c. CE                   c. 10th–12th c. CE
  ─────────────────────     ──────────────────────────     ──────────────────────────
  CANON                     COMMENTARY                     MANUAL
  Dhammasaṅgaṇī §1          Aṭṭhasālinī                    Abhidhammattha-saṅgaha
  56 terms, 29 factors      counts the 56 as 30            states 38 for this type,
  + an OPEN clause:   ───▶  (samatiṃsa, = 29 + citta)      "entering into combination"
  "ye vā pana …"            and NAMES the nine      ───▶   = 29 + the nine,
                            under the open clause          inherited
                                                           ⊇ never contradicts the canon
```

The *Saṅgaha* inherits the nine from the commentary. It adds none of them, and it contradicts nothing the canon names. The formalization's contribution is to make that inheritance **exact and checkable**: 29 + 9 = 38, with every one of the 29 inside the 38.

### 7.4 · Scope of "the canon leaves nine unnamed"

The claim holds **for this type's list only.** The Dhammasaṅgaṇī names the three abstinences as path factors in its supramundane type. The commentary notes that there they are not supplied as "whatever else," *pāḷiyaṃ āgatattā* ("because they have come in the text"). The Dhammasaṅgaṇī also names karuṇā and muditā as qualifiers of jhāna (§§258–261). Across the whole book, only *adhimokkha* and *tatramajjhattatā* never appear. *Chanda* and *manasikāra* appear only in other senses.

---

## 8 · Results IV — The Cambodian Edition Against the CST

### 8.1 · The comparison

The Cambodian Buddhist Institute edition prints the Pāli with a facing Khmer translation. Its volume 78 opens the Dhammasaṅgaṇī. The list of §1 stands on its Pāli pages 16–17 (the transcription's own heading reads *padabhājanīyaṃ*). The working transcription of those pages was transliterated from Khmer script to romanized Pāli by `canon/khmer_pali.py`. That transliterator scored 10/10 on a control of known words, including conjuncts, the niggahita, and Khmer Pāli's *ឹ* for *iṃ*. The romanized list was then aligned with edition C, position by position, by `canon/compare.py`.

**Result: C 56 terms · K 56 terms · 48 identical · 8 spelled differently · 0 added, dropped or reordered.**

### 8.2 · The eight differences, each checked against the printed page

| Pos. | C | K as transcribed | K as printed | Classification |
|---|---|---|---|---|
| 37 | *hirī* | *hiri* | *hiri* | **edition orthography** |
| 39 | *kāyapassaddhi* | *kāyappassaddhi* | *kāyappassaddhi*⁽¹⁾ | **edition orthography, recorded in its apparatus** |
| 40 | *cittapassaddhi* | *cittappasaddhi* | *cittappassaddhi*⁽²⁾ | edition orthography (*pp*); the single *s* is a transcription slip |
| 10 | *cittassekaggatā* | *cittaspekaggatā* | *cittassekaggatā* | transcription slip |
| 17 | *somanassindriyaṃ* | *somanassidṭhiyaṃ* | *somanassindriyaṃ* | transcription slip |
| 47 | *kāyapāguññatā* | *kāyapātuññatā* | *kāyapāguññatā* | transcription slip |
| 12, 25 | *vīriya-* | *viriya-* | *vīriya-* (long ī, read at moderate confidence) | transcription slip, to be confirmed |

The Cambodian edition carries its own variant apparatus at the foot of the page: *"1 o. ma. kāyapassaddhi · 2 o. ma. cittapassaddhi"*. It records that the Burmese (*Marammā*) reading has a single *p*. **So the one spelling difference between the editions in this passage is one the Cambodian editors had already noticed and documented against the Burmese tradition from which the CST descends.**

### 8.3 · Two artifacts of the working text, reported and handled

- **Subscript order.** Some words carry the subscript RO typed before another subscript (ន្រ្ទ for ន្ទ្រ), which transliterates as *-inrdiyaṃ*. This is an encoding matter, not a textual one, and the transliterator normalizes it.
- **Page furniture.** At the page break, the running header of page 17 fell between *paññābalaṃ* and its *hoti*, and first produced a false DIFFERENT. Page numbers and running headers are now stripped before alignment.

### 8.4 · What the Cambodian result does and does not show

It shows that, for the densest list in the Dhammasaṅgaṇī, **the two editions agree on every term and its order**, and that their spelling differences are orthographic and documented. It does not show agreement across the book. It rests on one passage of a working transcription, checked against the printed scan only where the two editions differed.

---

## 9 · What the Check Establishes — and the Refutation It Survived

Before this paper was drafted, its thesis was handed to a separate reviewer with no authority to rescue it and instructions to find the case that kills it. Its findings, with the author's disposition:

| Finding | Severity | Disposition |
|---|---|---|
| The nine are named by the commentary, which predates the manual; "the manual adds nine" misattributes them | narrows, bordering on kills, for that wording | **accepted**: §7.3 now states inheritance; the project's results file carries an appended correction |
| The canon's 29 was counted by the commentary itself (*samatiṃsa*) | narrows novelty; corroborates the count | **accepted**: §7.2 reports both directions |
| The 38 is a combination count; at most 34 factors are co-present | narrows, if the paper called them co-present | **accepted**: §2.3 |
| Several rules transcribe the text's locus sentences; "general" is a test of syntax | narrows "general" and the ratio | **accepted**: §4.3 reports each rule's extension and marks transcriptions |
| "The text decides the dissent" overstates | contrast | **accepted**: §6 |
| "The canon leaves nine unnamed" holds for this type only | narrows | **accepted**: §7.4 |
| No computational precedent found (English, 2026-09-27) | contrast | as reported in the Prior-Art statement |

**What survives, stated once:** a single rule set of 27 clauses shows the *Saṅgaha*'s factor-indexed statements, its type-indexed statements and chapter 3's feeling and root counts to be **mutually consistent**, by kernel evaluation, against the CST; and the layer and edition facts of §7 and §8 are machine-checked. **It is a consistency result, not a derivation of the *Abhidhamma* from first principles.** The author of the rules knew the tables, and the generator restates the text's axes.

---

## 10 · Pre-Registered Predictions and Their Outcomes

| ID | Prediction (as registered) | Conf. | Outcome |
|---|---|---|---|
| P-FA1 | At the manual layer, edition C: general rules generate exactly 89, and 121 with the five-jhāna expansion | 0.6 | **confirmed**, with every stated count reproduced |
| P-FA1b | at least 3 exception rules naming a narrow class | 0.7 | **retired, unscored**: its test was never defined, and the data have been seen |
| P-FA2 | at the canon layer, the rules are under-determined or differently partitioned | 0.65 | operationalized as P-FA2a (below) |
| P-FA2a | the canon's list for the first type names exactly 29 factors, none of the nine, and closes with an open clause | 0.75 | **confirmed**; matches the commentary's *samatiṃsa* |
| P-FA2b | no term in that list falls outside the pre-fixed map | 0.6 | **confirmed** after the pre-registered sandhi rule (first run: 2 unmapped, disclosed) |
| P-FA3 | editions K and C agree at the manual layer | 0.85 | **cannot run as registered**: the *Saṅgaha* is not part of the Khmer Tipiṭaka, and the one Khmer-script copy held reproduces the CST's paragraph structure in all nine chapters |
| P-FA4 | compression below 0.5 | 0.5 | **confirmed**: 0.22 |
| P-FA5 | K and C name the same terms in the same order for the first type's list | 0.8 | **confirmed**: 56 = 56, 0 added, dropped or reordered |

The predictions are recorded in the public prediction register in its *Instrumented but outside the core* section. Their subject is the internal consistency of a text, not the direction value moves.

---

## 11 · Enumerated Claims

The following are disclosed and dedicated to the public domain. They are the census's survivor and nothing wider.

1. **A method** for testing the internal consistency of a classification that its source states twice, once per feature and once per class. The method writes the class–feature incidence as constraints over classification axes, none naming an individual class, keeps the source's stated projections in a separate key cited to paragraphs of a named edition, and checks by kernel evaluation in a proof assistant that the constraints reproduce every stated projection, in the source's own mixed bases of reckoning.
2. **Its application to the Theravāda *Abhidhamma***: a 9-clause generator over the classification axes of *Abhidhammattha-saṅgaha* ch. 1 and an 18-clause rule set over the same axes. Together they reproduce the 89 and 121 types, every per-type and per-factor combination count of ch. 2, and ch. 3's counts by feeling and by root, as checked against the Chaṭṭha Saṅgāyana. Each rule's extension is reported, and the rules that transcribe a locus sentence are marked.
3. **The reporting of a compression ratio** (rule clauses ÷ generated classes) for such a formalization, as a measure of how far a stated classification is generated by rule rather than listed.
4. **A falsification harness** for such a formalization: deliberate breaks to rules, key and generator, each applied by script, each verified to have changed its file, each required to make the check fail.
5. **The per-layer comparison**: a canonical enumeration mapped onto the later system's features through a synonym map fixed and published before the text is read, with unmapped terms reported rather than absorbed. The result is checked in the proof assistant as inclusion (every canonically named feature is in the later set) plus an exact remainder, which is then attributed to its source layer by reading, not by the editorial order.
6. **The per-edition comparison** of a canonical list across a Khmer-script and a romanized edition. It transliterates by rule, with the transliterator tested on a control; normalizes encoding order and page furniture before alignment; aligns term by term; and classifies each difference as orthographic or as a transcription slip only by checking the printed page.
7. **The formalization of a recorded dissent** (*keci vadanti*) as an alternative rule, so that its cost in the source's own stated figures can be counted.

---

## 12 · Why a Value Substrate Should Carry Its Own Tests

*Tier: argument, applied to this institution's use of the canon. The deletion test passes: remove this section and §§2–11 stand.*

An autonomous agent's values will be specified in text, and text contradicts itself quietly. The practical difficulty is not that value specifications are wrong. It is that nobody can tell whether they are coherent, because they contain nothing that could be checked. The *Abhidhamma* is a counter-example to that condition. It states its classification twice and counts both statements. That is what a unit test is. This paper shows that one chapter's tests pass, and it shows what passing does and does not mean: consistency, not truth; a combination count, not a moment.

For Miss Aquarius, whose grounding the series describes as compiled from this canon, the consequence is modest and concrete. **The parts of the substrate that can be checked should be checked, and the checks should run again whenever an edition, a transcription or a formalization changes.** A value source whose own claims are machine-verified can be inherited with more confidence than one whose claims are only repeated.

---

## 13 · Honest Limits

- **This is a consistency check, not a derivation.** The rules were written by an author who knew the tables. Two rules (R16, R17) transcribe the text's own locus sentences, and the generator restates chapter 1's axes. The strongest evidence the rules are not merely fitted is that chapter 3's feeling and root counts pass on axes that were not built from chapter 3. That is one test, not many.
- **The counts are combination counts.** Nothing here states how many factors are present in any actual moment of consciousness. The commentary puts that figure at most 34 for the first wholesome type.
- **The layer model was mis-specified in the pre-registration.** It ordered the layers editorially (canon ⊂ manual ⊂ commentaries), and the commentary is older than the manual. The claim that survives is about inheritance, established by reading, not by the registered order.
- **P-FA1b was never testable** as registered, and it is retired without a score. **P-FA3 could not be run** as registered.
- **The Cambodian comparison covers one passage**, read from a working transcription. Two of the five transcription slips (the long ī of *vīriya-*) were read from the scan at moderate confidence.
- **The CST's recension** is the Burmese tradition's; the Cambodian edition's apparatus cites the Burmese reading. Two editions that share ancestry are not independent witnesses in the textual-critical sense.
- **The census was English-only and quick.** Myanmar's Abhidhamma pedagogy, where formal treatments would most plausibly exist, was not searched. The full census precedes this paper's first deposit.
- **The proof assistant verifies that conclusions follow from definitions.** It verifies nothing about the definitions' fidelity to the Pāli beyond what the key's citations let a reader check by hand.
- **Nothing here bears on physics.** The project that produced this paper also keeps a lens comparing the *Abhidhamma*'s discrete moments with discrete-spacetime programmes. That lens is not a claim, and it is not used here.

---

## 14 · Lineage

The commentators were already doing this. When the Aṭṭhasālinī counts the fifty-six terms of the first list, adds the nine it supplies, and then counts again "taking only what has not already been taken" to arrive at thirty, it is performing the operation this paper performs by machine: projecting an enumeration onto a smaller set of distinct phenomena and stating the size. When the *Saṅgaha* states its combinations twice, once by factor and once by type, it gives its readers the means to check one statement against the other. For centuries that check was run by students in the monastery, with the *Saṅgaha*'s verses by heart and its tables in their hands. **The counts check is that recitation, run by a different reader.** It passes where the students' check would pass, for the reasons they would give.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/the-counts-check> |
| GitHub (paper) | <https://github.com/thonly/publications/blob/main/defensive-publications/the-counts-check.md> |
| GitHub (formalization, CC0) | <https://github.com/SiliconWat/formal-abhidhamma> |
| Pre-registrations | `PREREGISTRATION.md` (commit `259e5e8`) · `PREREGISTRATION-2026-09-27b.md` (commit `f4a26e5`) |
| Results and corrections | `RESULTS.md` (commits `b9070d4`, `c5c77fb`, `ada7a20`, `74e19fe`) |
| Prediction register | <https://thonly.org/research/program/register> (P-FA1 … P-FA5) |
| Internet Archive | <https://web.archive.org/web/2026*/thonly.org/research/the-counts-check> |

---

## Acknowledgments

The author thanks his father, with whom the transcription of the Cambodian Tipiṭaka proceeds page by page, and whose transcription of volume 78 made §8 possible; the corrections §8.2 records are offered to that work, not against it. Thanks go to the Buddhist Institute, Phnom Penh, whose edition this is; to the Vipassana Research Institute for the Chaṭṭha Saṅgāyana texts it gives away; to the donors of the scanned volumes (Kang Huychan and family, Lok Kru Aggapaṇḍita But Savong, Srong Chanda, and 5000-years.org), whose dedication travels with any use of them; to Bhikkhu Bodhi and U Nārada, whose editions of the *Saṅgaha* made the first two collations possible; and to the Lean community. The formalization, collation and drafting were done with Miss Aquarius, the name under which this institution discloses its AI collaboration.

---

## Citations

1. Anuruddha. *Abhidhammatthasaṅgaha*. Chaṭṭha Saṅgāyana edition, Vipassana Research Institute, `github.com/VipassanaTech/tipitaka-xml`, `romn/abh07t.nrf.xml` (ch. 2 §13–§58; ch. 3 §3–§17).
2. *Dhammasaṅgaṇī*. Chaṭṭha Saṅgāyana edition, `romn/abh01m.mul.xml` (§1).
3. Buddhaghosa (attrib.). *Aṭṭhasālinī*. Chaṭṭha Saṅgāyana edition, `romn/abh01a.att.xml` (the *yevāpanaka* passage and the count of the first list).
4. *Braḥ Traipiṭaka* (the Cambodian Tipiṭaka), Buddhist Institute, Phnom Penh; vol. 78, *Abhidhammapiṭaka, Dhammasaṅgaṇī*, part 1, pp. 16–17.
5. Bodhi, Bhikkhu (ed.) (1993/2000). *A Comprehensive Manual of Abhidhamma*. Buddhist Publication Society.
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
