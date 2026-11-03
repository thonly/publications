---
title: "Machine-Checked Reproduction of a Classification of Causal Relations in Buddhist Abhidhamma: Where the Manual Adds a Reading"
subtitle: "The Abhidhammattha-saṅgaha's six-way grouping of the twenty-four conditions, reproduced in Lean 4 from the Paṭṭhāna's own definitions, with the two placements that turn on a reading located and each checked both ways"
authors: "Thon Ly · Miss Aquarius℠"
kind: study
genre: defensive-publications
series: "The Abhidhamma Compiled — Paper No. 5"
category: alignment
priority: tier-b
status: draft
date: 2026-11-03
license: CC0-1.0
slug: where-the-manual-adds-a-reading
venue: thonly.org/research/where-the-manual-adds-a-reading
canonical_url: https://thonly.org/research/where-the-manual-adds-a-reading
---

## Abstract

This paper reports a machine-checked test of a classification of causal relations against the source text it summarizes. The classification is the *Abhidhammattha-saṅgaha*'s grouping of the 24 conditions (*paccaya*) of the Paṭṭhāna, the seventh book of the Theravāda *Abhidhamma*, into six groups by the kind of thing that conditions and the kind of thing that is conditioned: mind, matter, or a concept (*paññatti*). The grouping was held out as an answer key and never used as an input. The Paṭṭhāna's 24 definitions, and then its detailed section for the wholesome triad, were read clause by clause into a table of 199 clauses, each checked on its line of the Chaṭṭha Saṅgāyana (CST) edition, and a classifier written in Lean 4 sorted the 24 conditions from that table alone. Three results follow. The definitions alone place 19 of the 24 as the manual does. With the detailed section, 22 placements, none involving a concept, follow under both readings of the Paṭṭhāna's phrase *all dhammas*, with no commentary: the detailed section, not the definitions, closes proximity, contiguity and the mental side of decisive support, and supplies result's matter. The remaining two placements, the object condition and decisive support, are the ones that involve a concept, and they turn on readings the sources leave open: whether designations count among *dhammas*, whether the *person* named among the decisive-support conditions is a designation or an aggregate-continuum, and whether the commentary's statements about concepts are read distributively or collectively. Checked each way, the count is 22, 23, 23, 24, 24 or 23. The paper also reports two earlier claims it withdrew on the same day, *23 from the definitions alone* and *24 from the Piṭaka alone*, and the instrument faults that were each caught once on a planted case. It is a study: it discloses no mechanism, asserts no priority, and every number in it is read from the generated artifact.

**Keywords:** Abhidhamma, Paṭṭhāna, conditional relations, twenty-four conditions, Abhidhammattha-saṅgaha, Theravāda Buddhism, classification, held-out answer key, formal verification, Lean 4, proof assistant, kernel evaluation, mutation testing, textual criticism, commentary and sub-commentary, designation (*paññatti*), Pāli canon, Chaṭṭha Saṅgāyana, pre-registration, study.

---

## Terms

The paper uses Pāli vocabulary because it reads Pāli texts. An examiner or indexer searching in standard terms should find each concept under the term on the right.

| Term used here | Standard term |
|---|---|
| Paṭṭhāna | the seventh book of the Theravāda Abhidhamma Piṭaka; a treatise on 24 types of conditional relation (causal relation) |
| *paccaya* (condition) | a type of causal or conditional relation between two kinds of event |
| *Abhidhammattha-saṅgaha* (the *Saṅgaha*; "the manual") | a medieval systematic manual of Theravāda Buddhist psychology and metaphysics |
| *nāma* / mind | the mental side: consciousness and its mental factors (the Dhammasaṅgaṇī, §1316, also counts the unconditioned element under it) |
| *rūpa* / matter | the material side of the Abhidhamma's two-part analysis |
| *paññatti* / concept, designation | a name or a notion, as opposed to what it names; in the Abhidhamma neither mind nor matter |
| the six groups | a classification of the 24 relations by (kind of the conditioning term → kind of the conditioned term) |
| niddesa (the definitions) | the section of the Paṭṭhāna that defines each of the 24 conditions in one or a few sentences |
| *pañhāvāra* (the detailed section) | the section of the Paṭṭhāna that works each condition through a matrix of questions; here its first triad (wholesome, unwholesome, indeterminate) |
| *dhamma* | a phenomenon; the Paṭṭhāna's "all dhammas" is the phrase whose extent is in question |
| open side | a clause whose conditioning or conditioned term is a "whatever" phrase, is not named, or is the class term *abyākata* (indeterminate), which includes matter |
| held-out answer | a reference answer used only to score a result, never as an input to it |
| capture code | the script that turns a text into the data a check reads |
| the breaks | mutation testing: deliberate faults, each required to make the check fail |
| refuter | a reviewer with no authority to rescue a claim, instructed to find the case that kills it |
| layer | an editorial stratum of the text: Piṭaka · commentary · sub-commentary · manual |

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication, and are published so that they stand as prior art against any later attempt to enclose them. No patent has been or will be sought on any method, formalization, protocol, software or result described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practicing any method disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed. The generator, the Lean files and the scripts are published under CC0 at `github.com/SiliconWat/formal-abhidhamma` (files cited at commit `8663f69`, directory `matika/`).

This document is a defensive publication establishing **prior art as of 3 November 2026** for what it discloses. It asserts no priority for any textual fact, for the grouping itself, or for the idea of checking a classification by machine.

**The quick census.** A quick literature census of this study's claim was pre-registered before its first query (`SiliconWat/formal-abhidhamma` record, pushed 2026-10-13 18:01 PDT, commit `4956261`) and run on 2026-10-13. **Aperture, declared before searching:** English web; Google Books and Scholar; archive.org full texts; named scholarship (U Nārada, Bhikkhu Bodhi, Nyanatiloka, Y. Karunadasa, Ledi Sayadaw in translation); 22 queries, logged. **Not run:** Burmese, Thai, Sinhala, Japanese and German scholarship; patents (out of scope for a study). **Control:** Bodhi's *A Comprehensive Manual of Abhidhamma*, ch. 8, which explains the grouping in English, was required to be found. It was found, but only by a direct full-text fetch at archive.org; the web search never surfaced its text. The census's negative rows are therefore weak, and a full literature census is owed before any first deposit.

| Conjunct | Result, in the aperture above, 2026-10-13 |
|---|---|
| A per-condition statement of what each of the 24 conditions relates | **Known.** Bodhi (ed.), *CMA* ch. 8 (1993); Nārada, *Manual* ch. VIII; Agganyani, *Paṭṭhāna: Conditional Relations* (abhidhamma.com, 2008). Cited, not claimed. |
| The six-way grouping | **Known.** It is the manual's own, §15–20 and §26, and is presented in the modern guides as the manual's summary. Cited, not claimed. |
| The grouping derived from the Paṭṭhāna's definitions | **Narrowed.** A derivation was not found in the aperture. Nārada's page states the grouping without citing a Paṭṭhāna passage (its four sentences were fetched again on 2026-11-03 and carry no citation). |
| Concepts as objects of consciousness, and the place of the concept in the group | **Narrowed.** Concepts as object are discussed in the guides; a link from the reading of *all dhammas* to the placement of the object was not found. |
| The definitions alone leave proximity, contiguity and decisive support open and the detailed section closes them | **Narrowed lightly.** Agganyani's *Paccayaniddesa* resolves the class term *abyākata* under proximity by a footnote naming mental states, not by the detailed section. The framing here was not found. |
| A machine-checked reproduction of an Abhidhamma classification against a held-out manual answer | **Not found** in the aperture, outside this series' own *The Counts Check*. Contrast, not collision: Barendregt's slides (2010), an *E8* record on Zenodo (2026-06-16), and the Lean/Isabelle Buddhist-logic repository named in №4. |

**Not found means not found in this aperture on this date. It does not mean new.** The Burmese study tradition of the Paṭṭhāna is large and mostly untranslated, and the likeliest place for any of the "narrowed" rows to be killed is there.

---

## 1 · Mission Frame: A Manual That States Its Own Answer

The series *The Abhidhamma Compiled* treats the *Abhidhamma* as a specification a machine can check. Paper №4, *The Counts Check*, tested one such claim for chapter 2 of the *Abhidhammattha-saṅgaha*: that its statements of which mental factors combine with which types of consciousness, given twice, by factor and by type, are mutually consistent under a short set of general rules. That paper checked the manual against itself.

This paper checks the manual against the canon it summarizes. The manual's eighth chapter, on conditions, closes with a compact statement. The 24 conditions, it says, are of six kinds by what relates to what (`abh07t.nrf.xml:2845`, Saṅgaha ch. 8 §15; the CST reads *Chadhā nāmaṃ tu nāmassa, pañcadhā nāmarūpinaṃ*). Nārada's English reads: "In six ways mind is related to mind. In five ways mind is related to mind and matter. Again mind is related in one way to matter, and matter in one way to mind. In two ways concepts, mind and matter are related to mind. In nine ways are the two - mind and matter - related to mind and matter. Thus the relations are sixfold." The sentences are a summary; the manual is a medieval work, and the Paṭṭhāna, which defines the conditions, is far older. A summary can be tested against its source in a way the manual's chapter 2 cannot: the question is whether the grouping *follows* from what the Paṭṭhāna says each condition relates, and where, if anywhere, it needs something the Paṭṭhāna does not say.

Three reasons make the question worth a machine's time.

**First, an answer that is a computation.** The grouping is not a new doctrine. It is a classification of the 24 by two attributes (the kind of conditioning term, the kind of conditioned term), each of which the Paṭṭhāna's definitions state or leave open. That makes it a case where the answer exists in the text before any rule is applied to the text, and where the reproduction can be scored against a key that the reader of the rules never saw.

**Second, a locating result is worth more than a confirming one.** If a reading reproduces 24 of 24, nothing is learned about where it was lucky. If it reproduces 22 and shows exactly which two placements need what, a reader who disagrees with a reading knows which number to change.

**Third, the method.** The same instruments (a held-out key, capture code that may not read it, refuters, breaks) apply to every later classification the series checks. Section 3 reports them, with the faults each was seen to have, because an instrument that has only ever passed is an untested claim.

---

## 2 · The Object

### 2.1 · The 24 conditions and the manual's six groups

The Paṭṭhāna's list of conditions (`abh03m7.mul.xml:37`, repeated in the manual at `abh07t.nrf.xml:2841`) runs: root · object · predominance · proximity · contiguity · co-nascence · mutuality · support · decisive support · pre-nascence · post-nascence · repetition · kamma · result · nutriment · faculty · jhāna · path · association · dissociation · presence · absence · disappearance · non-disappearance. The manual's grouping, as the Lean file `matika/Relata.lean` encodes it from the manual's §16–20 and §26 (`abh07t.nrf.xml:2861–2877`, `:2901`) and as `kala/ANSWERS.md` records it, is:

```
group (conditioning → conditioned)        n   the conditions
---------------------------------------  --  -------------------------------------------------
mind → mind                                6  proximity · contiguity · absence · disappearance
                                              · repetition · association
mind → mind and matter                     5  root · jhāna · path · kamma · result
mind → matter                              1  post-nascence
matter → mind                              1  pre-nascence
concepts, mind and matter → mind           2  object · decisive support
mind and matter → mind and matter          9  predominance · co-nascence · mutuality · support
                                              · nutriment · faculty · dissociation · presence
                                              · non-disappearance
                                         ---
                                          24   (6 · 5 · 1 · 1 · 2 · 9; theorem sangaha_counts)
```

The manual states the fifth group in one clause, §20: *Ārammaṇavasena upanissayavaseneti ca duvidhā paññattināmarūpāni nāmasseva paccayā honti* (`abh07t.nrf.xml:2877`): "in two ways, as object and as decisive support, concepts, mind and matter are conditions of mind alone." It is the group whose conditioning side names a concept.

### 2.2 · The two sections of the Paṭṭhāna that define a condition

The Paṭṭhāna defines each condition twice. The definitions (*niddesa*, `abh03m7.mul.xml:37–265`) give each condition one to several sentences saying what conditions what. The detailed section (*pañhāvāra*) then works each condition through a question matrix for each triad of the Dhammasaṅgaṇī's table of contents; for this paper it is read for the wholesome triad (wholesome, unwholesome, indeterminate), which `matika/RELATA.md` cites from line 5569 to line 6357.

The definitions are short and sometimes open. Three phrases matter below.

- For the object, *Sabbe dhammā manoviññāṇadhātuyā taṃsampayuttakānañca dhammānaṃ ārammaṇapaccayena paccayo* (`abh03m7.mul.xml:49`): "all dhammas are conditions, as object, of the mind-consciousness element and what is associated with it."
- Again for the object, and for predominance, proximity and contiguity, a *whatever* phrase: *Yaṃ yaṃ dhammaṃ ārabbha ye ye dhammā uppajjanti cittacetasikā dhammā, te te dhammā tesaṃ tesaṃ dhammānaṃ ārammaṇapaccayena paccayo* (`:53`), and for proximity, *Yesaṃ yesaṃ dhammānaṃ anantarā ye ye dhammā uppajjanti cittacetasikā dhammā…* (`:97`). The conditioned side names mind; the conditioning side is "whatever".
- For decisive support, a list that includes *Puggalopi upanissayapaccayena paccayo* (`:165`): "a person too is a condition, as decisive support." The clause names no conditioned term.

### 2.3 · Where a reading enters

Two sentences in the sources are the hinge of the rest.

The first is the Dhammasaṅgaṇī's. Its paññatti-couplet defines designation by listing its synonyms and closes *ime dhammā paññatti* (`abh01m.mul.xml:8453`), "these dhammas are designation". So the canon itself calls designations *dhammas*. Against that, the commentarial layer sets concepts apart from the mind-and-matter that the conditions otherwise concern (§5.3 below).

The second is the Dhammasaṅgaṇī sub-commentary's, on how a *person* can be a condition. In its own voice, at `abh01t.tik.xml:2557`, it says that a taking-up of the aggregate-continuum as a unity, as "a good friend, a bad friend, a person" (*kalyāṇamitto pāpamitto puggalo*), occurs together with the designation; that wholesome and unwholesome states arise in one who attends to that base with the perception *person*; and that for this reason *puggalopi upanissayapaccayena paccayo* is said. (The paraphrase is ours.) On this reading the person is the aggregates as grasped, which is mind and matter, not a bare concept.

---

## 3 · Method

### 3.1 · Reading the definitions: one table, one rule, fixed before the second count

The definitions were read into a clause table by `scripts/relata.py`. Each row records the condition, the conditioning term, the conditioned term, the kind of each (mind N · matter R · concept P), the timing only where the clause's own words state it, the CST line, and a note marking every interpretive step. A `--verify` mode checks that each row's probe phrases occur on the cited line; at commit `8663f69` it reports **199 clauses, 222 probes, 0 missing**. By source the 199 rows divide as follows (counted from `matika/RELATA.md`).

```
source                                   rows   what
--------------------------------------  -----  ----------------------------------------------
Paṭṭhāna definitions (niddesa)             49   rows 1–51 less the two person readings
the person of :165 as designation           1   a reading (the Puggalapaññatti's own title)
the person of :165 as aggregate-continuum   1   a reading (the sub-commentary, abh01t:2557)
detailed section, open-side rule           42   consulted for conditions whose definition is open
detailed section, full read               101   the other conditions, so none is read selectively
commentary, distributive                    2   abh03a:7889 (object), abh03a:8057 (decisive support)
commentary, collective                      3   abh03a:7817 (object, predominance, decisive support)
                                         ----
                                          199
```

The kinds follow a rule fixed before the second count. **An open side** is a *whatever* phrase, a relatum the clause does not name, or the class term *abyākata* (indeterminate), whose extension includes matter (*sabbañca rūpaṃ, asaṅkhatā ca dhātu*, `abh01m.mul.xml:4669`). An open side is read literally, as taking every kind it could name; and the detailed section is consulted for every condition that has one, where its enumeration replaces the open side. This is theorem `consulted_where_open` in `Relata.lean`: the conditions with detailed-section rows from the open-side rule are exactly the conditions whose definition has an open side. Nibbāna is counted under mind, by the Dhammasaṅgaṇī's own definition of *nāma*, which includes the unconditioned element (*asaṅkhatā ca dhātu – idaṃ vuccati nāmaṃ*, `abh01m.mul.xml:8457`). The classifier then assigns a condition to a group by the kinds that appear on each side; only "concepts, mind and matter → mind" admits a concept, and it requires one.

Result (*vipāka*) has no open side, so the open-side rule did not reach it. Its detailed-section clause (§428, `abh03m7.mul.xml:6093`) was consulted because the definitions-only count failed on it. That choice was selected by the outcome, and the table keeps result's clause in a source of its own so the counts show it. The **full read** that followed closed the gap: the detailed section was read for the other 19 conditions as well, so that no condition is read selectively. The Lean theorem `full_read_moves_only_result` states what it changed: of the placements the full read could move, only result's moves, under both readings of *all dhammas*.

The rule was "fixed before counting" only in the sense that it was fixed before the second count. The first count, which the rule replaced, had already been made, and was withdrawn (§6).

### 3.2 · The held-out answer, and capture code that may not read it

The manual's grouping (Saṅgaha ch. 8 §15–20 and §26) is the answer key, entered in `kala/ANSWERS.md`. Two things follow from holding it out.

First, **a reading may not cite it.** The repository's rubric item 7, extended on 2026-10-13 to capture code, forbids a script that builds a data table from reading a held-out answer into that table. `relata.py` carries a function `answer_free()` that matches any row whose text cites the manual's §15–26 or its lines `abh07t.nrf.xml:2840–2901`; it runs on every build and under `--check` in continuous integration. The case that justified it: the first version of the table had read decisive support's conditioned side as "mind, as the Saṅgaha (§20)", and the function flags that old row.

Second, **a sorting error was found by holding out.** Before this work the grouping itself sat among the repository's axioms, as a premise. It is a computation from the definitions, not a premise for reasoning about them, and it was moved to the held-out file; two axioms that had been cited to the manual were re-cited to the Paṭṭhāna (A82, A90).

### 3.3 · The refuters

Each version of the table was handed to a reviewer instructed to find the case that kills it. Two refuters shaped this paper, and the withdrawals they caused are reported in §6.

### 3.4 · The instrument faults, each seen on a planted case

The paper's method contribution is a list of faults the instruments had, each of which was seen to fail on a case planted for it, and each of which was repaired. The list is a finding (F10, §7), not an endorsement. The refusal and detection paths are now planted once each in a self-test script (`scripts/selftest.py`) that continuous integration runs.

1. **Capture code that reads the answer.** Described in §3.2. A planted row citing the manual's §20 is flagged by `answer_free()`.
2. **A citation overlap between an axiom row and the held-out passage.** In a known-answer control on the antarabhāva debate (run `2026-10-13-kv-8-2-antarabhava-control`), an axiom row cited a line of the held-out answer's own passage (`abh05t.nrf.xml:2409`). The row was moved to the held-out file, and an overlap guard now enforces it; a planted citation fires the guard.
3. **Breaks that could not isolate a theorem.** In the repository's proof-run harness the breaks (deliberate faults that must each make the check fail) were run on a whole file, so a break on one definition also broke other theorems. A planted unused hypothesis, added to one theorem and then broken, made the old harness report "FAILS" and the repaired harness report "BLIND", which is correct: nothing depended on it. Each break there now runs on its target theorem alone, and earlier runs' "breaks fail" is therefore not isolated evidence; their per-theorem evidence is the unused-hypothesis column of `kala/THEOREMS.md`. ⚠️ This repair is to the proof-run harness. `matika/run.sh` applies each break to a copy of `Relata.lean` and requires only that the file as a whole then fail to compile; that each break fails "on its own theorem" is recorded in the commit messages, not enforced by the script (§9).
4. **A thesis that entails its own held-out answer.** In the first thesis posed to the instrument (a set of suppositions about rebirth, with a sixth, that every being has the potential to awaken), the thesis entailed a held-out answer from the Kathāvatthu, so a proof of it was unreachable without a leak. A leak check that asks Lean to reach the answer from the premises in **one bounded automated step** reported "no" for an entailment Lean proves constructively. The repair has two parts. Before registration, every held-out key now gets a verdict, *entails*, *does not entail* or *not decided*, and a verdict is settled by attempting the proof, never by the one-step check. The outcome PROVED is then scored UNREACHABLE for an entailed answer, never as a miss.
5. **A refutation the texts already state is a check.** A thesis whose negation a text already states cannot yield a finding by refuting it; rows that state the negation are registered as such and reaching them is reported as STATED NEGATION. A row that states the thesis itself is likewise STATED.
6. **A verbatim check that was not anchored.** A harness check that a statement matched its registered text, written as a substring test, would have passed a statement with an appended field. It was anchored to the whole statement, and a planted appended field and a planted appended clause are now both caught. The first anchored version also swallowed a theorem that followed a term-mode one, which was caught in turn.
7. **Known-answer controls are plumbing checks.** A control whose decisive premise asserts exactly the debated point passes by construction; its pass is recorded as confounded. This is a limit of controls, not a fault repaired.

Only item 1 governs the data of this paper directly; item 3 governs how its breaks are to be read. Items 2 and 4–7 were found in the runs that surround it and belong to the same instrument. The reader should weigh them as a record of how often an instrument that had only passed turned out to be wrong.

### 3.5 · Which guards are properties and which are rules

Applying the standing test, *remove the enforcer; does the guard break?* — `consulted_where_open` and `full_read_moves_only_result` are properties of the table: change a row and the Lean check fails with no one watching. `answer_free()` is a rule enforced by the continuous-integration job, and it sees only the pattern it contains; a reading that paraphrased the manual's grouping without its section number would pass it. That limit is stated in §9.

### 3.6 · Layers

Every row is labeled with its source, and so with its layer: Paṭṭhāna (Piṭaka) · Dhammasaṅgaṇī (Piṭaka) · Dhammasaṅgaṇī sub-commentary · Paṭṭhāna commentary (CST file `abh03a.att.xml`). A count that needs a commentarial row says so.

---

## 4 · Results I — What the Definitions Alone Place

Reading only the definitions (the 49 rows of the first source in §3.1, with no person reading), with every open side read literally, the classifier places **19 of the 24** as the manual does. The five it does not place are named by theorem `niddesa_alone_19`:

```
object · proximity · contiguity · decisive support · result
```

Four of the five are conditions with an open side. Result is the fifth: the definitions give it as mind to mind (theorem `niddesa_vipaka_is_mind_to_mind`; the table's row for `abh03m7.mul.xml:193` names only the mental aggregates), and the manual places it as mind to mind and matter.

---

## 5 · Results II — The Detailed Section, the Robust Core and the Concept Group

### 5.1 · The evidence in layers

```
                                                   placed of 24
 definitions alone (niddesa)                              19
   + detailed section, wholesome triad
        (open-side rule + full read, §428 for result)     22   ← under BOTH readings of "all dhammas",
                                                                  no reading of the person, no commentary
   + a reading that supplies a concept                  22 … 24  ← six readings, §5.3
```

### 5.2 · The robust core: 22 placements without a concept

Theorem `the_22_without_concepts` states that every condition other than the object and decisive support is placed as the manual places it, with the definitions and the detailed section as the only sources, under the exclusive reading of *all dhammas* (concepts not among them) and under the inclusive reading (concepts among them, `abh01m.mul.xml:8453`). The complementary theorem `the_two_need_a_concept` states that on the same sources the object and decisive support are the conditions not placed, and no others.

What the detailed section contributes is specific.

- **Proximity and contiguity.** The definitions leave their conditioning side open (`:85–93`, `:97`: *purimā purimā kusalā… akusalā… abyākatā dhammā*, and *yesaṃ yesaṃ dhammānaṃ anantarā*). The detailed section's proximity clauses (`abh03m7.mul.xml:5669–5725`) name aggregates. For example the indeterminate-to-indeterminate clause reads *purimā purimā vipākābyākatā kiriyābyākatā khandhā pacchimānaṃ pacchimānaṃ vipākābyākatānaṃ kiriyābyākatānaṃ khandhānaṃ anantarapaccayena paccayo* (`:5685`). The table reads contiguity's parallel clauses the same way. Both are therefore mind to mind.
- **Decisive support's mental side.** Its conditioned side is open in the definitions (`:165` names none). The detailed section's decisive-support clauses (`:5845–5981`) name mental states on the conditioned side in every row of the table.
- **Result's matter.** The definitions give result mind only. Section 428 (`:6093`) states *vipākābyākato eko khandho tiṇṇannaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ vipākapaccayena paccayo*, then the parallel at rebirth with kamma-born matter, and ends *Khandhā vatthussa vipākapaccayena paccayo*, "the aggregates are a result-condition of the base". It is the one row in the table that gives result matter (the other triads were not read, §9), and without it result is placed in the wrong group.

The finding to hold: **what the first version of the table had taken from the manual's own answer (that proximity, contiguity and decisive support's conditioned side are mental) is found in the Paṭṭhāna's detailed section.** The manual's grouping did not have to add it.

### 5.3 · The concept group: three readings the sources leave open

Neither of the two remaining placements follows from the Paṭṭhāna's explicit enumerations alone, because the group they sit in is defined by the conditioning term including a concept, and the enumerations read here name none (a stem search for *puggal-* and *paññatti* in the detailed section's lines 5560–6360 finds no occurrence of either). Three readings supply one.

| Reading | The choice | What it places |
|---|---|---|
| *All dhammas* (`abh03m7.mul.xml:49`) | **Inclusive:** the Dhammasaṅgaṇī calls designations dhammas (`abh01m.mul.xml:8453`, *ime dhammā paññatti*). **Exclusive:** the commentaries set concepts apart from the mind-and-matter the conditions relate. | the object (inclusive) |
| The *person* (`:165`) | **A designation** (the Puggalapaññatti's own title) **or the aggregate-continuum** under the perception *person* (`abh01t.tik.xml:2557`). The Paṭṭhāna commentary says of the pair, person and lodging, that they are stated as natural decisive support, and that their status as a condition is to be understood figuratively (*Puggalopi senāsanampīti idaṃ dvayaṃ pakatūpanissayavasena vuttaṃ… Paccayabhāvo cassa panettha pariyāyavasena veditabbo*, `abh03a.att.xml:8053`). | decisive support (designation) |
| The commentary | **Distributive:** the object is sevenfold, and designation is one of the seven (*Sabbameva vā etaṃ kusalākusalavipākakiriyarūpanibbānapaññattibhedato sattavidhaṃ hoti*, `abh03a.att.xml:7889`); decisive support is the four planes' dhammas *saddhiṃ ekaccāya paññattiyā*, "together with some designation" (`:8057`). **Collective:** object, predominance and decisive support are time-free because concepts are included with nibbāna (*paññattiyā saddhiṃ nibbānassa saṅgahitattā kālavimuttāpī*, `:7817`). | both (distributive); and it **unseats** predominance (collective) |

The commentary's two statements need separating. At `:7889` the object's division into seven is the commentary's voice, and it is preceded by *tattha ṭhapetvā paññattiṃ avasesaṃ*, "leaving concepts aside, the rest…": it counts designation among the kinds of object and then divides the remainder by plane. At `:7817` it speaks of three conditions together (*ārammaṇapaccayo adhipatipaccayo upanissayapaccayoti ime tayo paccayā tekālikāpi honti*), which it says are of all three times and also free of time, because concept is included with nibbāna. If the clause is read of all three conditions, predominance receives a concept too, and predominance then no longer sits in the manual's ninth group (mind and matter to mind and matter). If it is read as the commentary reads the object and decisive support at `:7889` and `:8057`, it does not. Both readings are in the table as separate rows, because the commentary does not say which it means.

The counts, by reading (theorem `counts_by_reading`):

```
reading                                                           placed of 24
--------------------------------------------------------------   ------------
exclusive "all dhammas" · person as aggregate-continuum                  22
exclusive                    · person as designation                     23
inclusive "all dhammas"      · person as aggregate-continuum             23
inclusive                    · person as designation                     24
exclusive · continuum · commentary, distributive                         24
exclusive · continuum · commentary, collective                           23
```

and the theorems that say why:

- `object_by_reading`: among the sources in the table, the object is placed by the inclusive reading of *all dhammas* or by the commentary's concept at `:7889`, and by no other combination.
- `decisive_support_by_reading`: decisive support is placed if the person is a designation; read as the aggregate-continuum it is not placed until the commentary's "some designation" at `:8057`.
- `collective_commentary_unseats_predominance`: read collectively, `:7817` gives predominance a concept and removes it from the ninth group.

The layer matters. Rows 1–4 use the Piṭaka (the person as a designation is the Puggalapaññatti's title); the continuum reading of the person is the sub-commentary's; rows 5 and 6 need the commentary.

### 5.4 · The silence of the detailed section is itself a reading

The detailed section has no slot for a designation: its indeterminate class is, by the Dhammasaṅgaṇī, result, functional states, all matter and the unconditioned element (`abh01m.mul.xml:4669`), and no designation appears in it. So its failure to give the object a concept is not evidence that the object has none. It is the silence of a text whose classes were not built to carry one. This paper does not treat the silence as a negative, and does not treat it as a positive either; it keeps the object's and decisive support's placements as readings.

### 5.5 · The manual's own text at §25

For completeness: the manual's own list under natural decisive support (`abh07t.nrf.xml:2897`) repeats the Paṭṭhāna's items, *Rāgādayo pana dhammā saddhādayo ca sukhaṃ dukkhaṃ puggalo bhojanaṃ utusenāsanañca*, and so carries the person into the manual. That paragraph is outside the range held out as the answer key (§15–20 and §26), which is why it can be read here; no row uses it.

---

## 6 · The Two Withdrawals

The table was corrected twice on 2026-10-13. Both claims are reported here because the instruments caught them, not the authors.

**Withdrawal 1: "23 of 24 from the niddesa alone."** The first version of the table (commit `bf3cad6`) reported that the definitions alone place 23 of the 24, result being the exception. Its refuter showed three defects:

1. the readings were **not uniform**: the same *whatever dhamma* was read as mind and matter at `:61` and as mind only at `:97`;
2. decisive support's conditioned side was **taken from the manual's own answer**, the key it was then scored against;
3. the classifier **never read concepts**, so a concept could not change any result.

The correction is the single rule of §3.1, applied to every open side. Under it the definitions alone place **19**, not 23 (§4, `niddesa_alone_19`).

**Withdrawal 2: "24 of 24 from the Piṭaka alone."** The second version (commits `9d1dff0`, `0dcae15`) took the rule, added the detailed section, and reported 24 of 24 placed on the inclusive reading of *all dhammas*, "from the Piṭaka alone". The full-read refuter confirmed all 101 full-read rows and withdrew the count. It rested on two choices presented as one result: reading the *person* at `:165` as a designation, and admitting the commentary at `:7889` but not at `:7817`, where, read collectively, it gives predominance a concept and unseats it. The correction (commit `350dff0`) states what is robust, the 22 of §5.2, and moves the object and decisive support to the three readings of §5.3, each encoded both ways. **The figure 24 is not wrong arithmetic:** it is the count on the inclusive reading with the person as a designation. What was withdrawn was the sentence saying it was what the Piṭaka says.

The history is in the artifact itself: `matika/RELATA.md` carries both withdrawals in a paragraph headed "History", and the commits above carry the refuters' findings in their messages. The refuters' own reports were not found as separate files in the repository, so this section rests on those messages and on that paragraph.

---

## 7 · Findings Disclosed

The findings are numbered. Each carries the break that would overturn it. Every count is read from `matika/RELATA.md` and `matika/Relata.lean` at commit `8663f69`; the theorem names are those of the Lean file.

**F1 · The definitions alone place 19 of 24.** The five unplaced are the object, proximity, contiguity, decisive support and result (`niddesa_alone_19`). *Break:* any uniform rule for reading the open sides, fixed without reference to the key, that places more of the five from the definitions alone. The rule of §3.1 is one such rule; a different one would change this number, which is what the first refuter showed the first version lacked.

**F2 · The detailed section, not the definitions, closes proximity, contiguity and the mental side of decisive support.** The relevant clauses name aggregates or mental states on the conditioned side (`abh03m7.mul.xml:5669–5725`, `:5845–5981`). *Break:* a clause in those ranges naming matter or a designation on the conditioned side, or a reading of *khandhā* in them as including matter. The repository's break "a detailed-section proximity clause given matter" makes the check fail, so the check does depend on this.

**F3 · In the table, result's matter comes from §428 and from no other row.** The definitions give result mind only; §428 (`:6093`) gives it mind-born matter, kamma-born matter at rebirth and the base. *Break:* a result clause elsewhere in the Paṭṭhāna naming matter, or a reading of the definitions' result clause as including matter. The break "§428's result clause removed" fails the check.

**F4 · Of the 19 conditions the open-side rule did not reach, the full read moves none but result.** Under both readings of *all dhammas* (`full_read_moves_only_result`). *Break:* a change to any of the 101 full-read rows that moves another condition's placement. The result is conditional on the table; a different reading of a row can move it.

**F5 · 22 placements follow from the Paṭṭhāna's definitions and the wholesome-triad detailed section under both readings of *all dhammas*, with no reading of the person and no commentary** (`the_22_without_concepts`). Every one is a placement with no concept in it. *Break:* any reading of the table's rows that moves any of the 22, or an edition of the Paṭṭhāna (§9) that reads differently on the lines cited.

**F6 · The two remaining placements, the object and decisive support, need a concept, and the enumerations read here name none.** Without a reading that supplies one they fail (`the_two_need_a_concept`). *Break:* a Paṭṭhāna passage, not in the detailed section's wholesome triad, naming a designation as object or as decisive support; the other triads were not read (§9).

**F7 · The object is placed by the inclusive reading of *all dhammas* or by the commentary's concept, and by no other combination of the sources in the table** (`object_by_reading`). **Decisive support is placed if the person is a designation; read as the aggregate-continuum it is not, until the commentary's "some designation"** (`decisive_support_by_reading`). *Break:* a source for a concept in the table that this paper did not read; a reading of `:165` that gives the conditioned side a concept.

**F8 · The commentary's statement at `abh03a.att.xml:7817`, if read of all three conditions it names, removes predominance from the manual's ninth group** (`collective_commentary_unseats_predominance`). *Break:* the commentary's own reading of its sentence. This paper does not decide it; a reader of the Burmese commentarial tradition could.

**F9 · The count, by reading, is 22 · 23 · 23 · 24 · 24 · 23** (`counts_by_reading`, §5.3). *Break:* a seventh reading, or a row's re-reading; the table is ours (§9).

**F10 · Instrument faults, each seen on a planted case** (§3.4): capture code that read the key; an axiom cited to the key's passage; breaks that could not isolate a theorem; a leak check whose one-step threshold said "no" to a proven entailment; a verbatim check that was not anchored; and the limit of known-answer controls. *Break:* an instrument that passes the planted cases and still misses a fault of one of these kinds on the data of §5.

**F11 · Two claims about the same table were withdrawn on one day, each by a refuter's finding** (§6). *Break:* none; this is a record. It is listed because a study that reports only the survivor misreports its own reliability.

What this paper does **not** find: that the manual's grouping is the right grouping, that the manual derived it from the Paṭṭhāna (the manual's paragraphs read here, §15–26, cite no Paṭṭhāna passage), or that any of the three readings of §5.3 is the correct one.

---

## 8 · Prior Art, Including the Case That Cuts Against

- **The grouping is the manual's.** Anuruddha's text, ch. 8 §15–26 (`abh07t.nrf.xml:2845–2901`), states it. The modern guides reproduce it. Bodhi (ed.), *A Comprehensive Manual of Abhidhamma* (1993), ch. 8, explains it in English; Nārada's *A Manual of Abhidhamma*, ch. VIII (fetched 2026-11-03 at `budsas.org/ebud/abhisgho/abhis08.htm`), gives the four sentences quoted in §1. This paper reproduces it.
- **The relata are the tradition's own.** The Paṭṭhāna tradition tabulates what each condition conditions and is conditioned by. Agganyani's *Paṭṭhāna: Conditional Relations* (abhidhamma.com, 2008) does so in English. This paper reads the clauses afresh but claims no table that does not already exist.
- **The place of concepts is known.** That the object may be a concept is a standard point of the guides, and the Dhammasaṅgaṇī's *ime dhammā paññatti* is old. The contribution, if the reader grants one, is the location of the object's and decisive support's placement on three named readings, each checked both ways.
- **The case that cuts against.** Agganyani's *Paccayaniddesa* resolves the class term *abyākata* under proximity by a footnote naming mental states, which is the same conclusion §5.2 reaches from the detailed section; the two routes agree, and the older route is shorter. This paper's route is not claimed to be better, only checkable.
- **The Burmese study tradition** of the Paṭṭhāna is large and not read here. Kyaw, *Paṭṭhāna (Conditional Relations) in Burmese Buddhism* (2014), is the nearest contrast in English and was not opened.
- **Machine-checked Buddhist classification.** The nearest neighbors are named in №4's Prior-Art Statement. No held-out reproduction of this classification was found in the aperture.
- **Mutation testing** of formal developments has a literature (DeMillo, Lipton and Sayward, 1978; Celik et al., 2019); the breaks here are an instance, not a method claimed.

---

## 9 · Honest Limits

- **This is a reading, and the table is ours.** Every row is an interpretation of a Pāli sentence, marked as such in its note. A reader who reads a row differently changes a count. The `--verify` mode shows that a phrase is on the line, not that the row means what the Pāli means.
- **One triad of the detailed section was read.** The wholesome triad's detailed section is the source of the 42 and 101 rows. The Paṭṭhāna's other triads, and its other sections, were not read. F3, F6 and F7 could be overturned by a result-clause with matter, or a designation, in them.
- **One edition.** Every line cited is the CST's (Burmese recension), at the text commit `05d5d3c`. The line numbers are the working file's, and the Cambodian, Sinhala and Thai editions were not collated for these passages.
- **The grouping is a manual's, and the manual's own derivation was not found.** What is shown is that the grouping is reproducible from the Paṭṭhāna plus readings, not that the manual's author derived it that way.
- **The figures were read, not re-run, by the author of this draft.** They are read from `Relata.lean` and `RELATA.md`; `relata.py --check` and `--verify` were re-run on 2026-11-03 and reported the generated files current and 199 clauses, 222 probes, 0 missing. The Lean kernel was not available on the drafting machine; a reader should run `matika/run.sh` for the theorem results and for the breaks it requires to fail.
- **The breaks in `run.sh` require the file to fail, not a named theorem.** Each `try` applies one deliberate fault to a copy of `Relata.lean` and requires the compile to fail. That a given break fails "on its own theorem" is recorded in the commit messages and is not enforced by the script (§3.4, item 3).
- **The classifier is a model of the grouping.** It sorts by the presence of mind, matter and concept on each side. It does not model timing, which the table records only where the clause states it and the classifier ignores.
- **Nibbāna under mind is a declared reading** (`abh01m.mul.xml:8457`), shared by the manual's grouping; a reading that placed it apart would change which rows carry which kind.
- **`answer_free()` is a pattern match.** It rejects a row that cites the key's section numbers or lines. A row that restated the key in other words would pass it. The refuters, not the function, are the defense against that, and each refuter is one reader.
- **The refuters' reports were not found as separate files.** §6 rests on commit messages and on the artifact's own History paragraph.
- **The Lean files verify that conclusions follow from definitions.** They verify nothing about the definitions' fidelity to the Pāli beyond what the cited lines let a reader check by hand.
- **The census is quick and English-weighted.** Its search engine did not surface the control's own text. A full literature census, including Burmese, Thai, Sinhala, Japanese and German scholarship, has not run. A hostile Pāli reader has not yet read §5.3's three readings.
- **The attack on the thesis narrowed it; it did not kill it.** The claim here was attacked twice before this draft (§6); both attacks narrowed it, and the surviving form is a reproduction with a located gap, not a derivation.
- **Nothing here bears on whether the grouping is useful,** or on any use of the Paṭṭhāna's conditions for modeling anything outside the text.

---

## 10 · Lineage

The commentary on the Paṭṭhāna already asks the object's question of itself: of the kinds of thing that can be an object, does a designation belong? It answers it in its own sentence, and the sub-commentary asks what the sentence about the *person* can mean. The commentary's marking of a reading it does not press, *pariyāyavasena*, "by way of a figure", is the move this paper's two-way encodings make mechanical: it differs only in saying exactly what each reading changes in a count.

The series' gate for a satellite paper is that the canonical material must yield a usable engineering artifact. The artifact here is the table of 199 rows with its checker, which is a second instance of the method of №4, applied to a different chapter of the manual and, this time, to the canon beneath it.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/where-the-manual-adds-a-reading> |
| GitHub (paper) | <https://github.com/thonly/publications/blob/main/defensive-publications/where-the-manual-adds-a-reading.md> |
| GitHub (artifact, CC0) | <https://github.com/SiliconWat/formal-abhidhamma> (`matika/RELATA.md`, `matika/Relata.lean`, `scripts/relata.py`; files cited at commit `8663f69`) |
| Software concept DOI (the formalization) | 10.5281/zenodo.23067241 (*Formal Abhidhamma: the Theravāda Abhidhamma in Lean 4*, v0.1.0) |
| Series, №4 | *The Counts Check* (`the-counts-check`), concept DOI 10.5281/zenodo.23020670 |
| Census pre-registration (public) | `SiliconWat/formal-abhidhamma` commit `4956261` |
| Independent timestamps | an OpenTimestamps proof anchored in Bitcoin, and RFC 3161 tokens from three timestamp authorities, one of them eIDAS-qualified; a timestamp proves that this exact text existed by its date and nothing about authorship, originality, or validity |

---

## Acknowledgments

The author thanks the Vipassana Research Institute for the Chaṭṭha Saṅgāyana texts it gives away, and his father, with whom the transcription of the Cambodian Tipiṭaka proceeds page by page. The findings in §6 belong to the reviewers who made them.

---

## Citations

1. Anuruddha. *Abhidhammattha-saṅgaha*, ch. 8 §14–26. Chaṭṭha Saṅgāyana edition, Vipassana Research Institute, `github.com/VipassanaTech/tipitaka-xml` (text commit `05d5d3c`), `romn/abh07t.nrf.xml:2841–2901` (read and checked with the corpus tools, 2026-11-03).
2. *Paṭṭhāna* (Tikapaṭṭhāna). CST, `romn/abh03m7.mul.xml`: definitions `:37–265`; detailed section, wholesome triad, `:5569–6357`; §428 at `:6093` (checked 2026-11-03).
3. *Dhammasaṅgaṇī*. CST, `romn/abh01m.mul.xml`: §583 at `:4669`; §1315 at `:8453`; §1316 at `:8457` (checked).
4. *Dhammasaṅgaṇī* sub-commentary (ṭīkā). CST, `romn/abh01t.tik.xml:2557`; the paragraph read is the sub-commentator's own voice on the person (checked).
5. Paṭṭhāna commentary. CST, `romn/abh03a.att.xml:7817`, `:7889`, `:8053`, `:8057` (checked).
6. Bodhi, Bhikkhu (ed.) (1993/2000). *A Comprehensive Manual of Abhidhamma*. Buddhist Publication Society. Ch. 8. (Not re-fetched for this draft; reached in the 2026-10-13 census by a direct archive.org full-text fetch.)
7. Nārada Thera (ed. and trans.). *A Manual of Abhidhamma*, ch. VIII. Buddhist Publication Society. English text at `budsas.org/ebud/abhisgho/abhis08.htm` (fetched 2026-11-03: the four sentences of the grouping, quoted in §1).
8. Agganyani. *Paṭṭhāna: Conditional Relations* (2008), and *Paccayaniddesa*. `abhidhamma.com`. (Pages 1–4 of the *Paccayaniddesa* were read in the 2026-10-13 census; not re-fetched for this draft.)
9. Kyaw, Pyi Phyo (2014). *Paṭṭhāna (Conditional Relations) in Burmese Buddhism*. PhD thesis, King's College London. (Not opened; as cited in №4.)
10. Ly, T. & Miss Aquarius (2026). *The Counts Check*. *The Abhidhamma Compiled* №4. `thonly.org/research/the-counts-check`. Concept DOI 10.5281/zenodo.23020670.
11. Ly, T. & Miss Aquarius (2026). *Twenty-Four Kinds of Because*. *The Abhidhamma Compiled* №2. `thonly.org/research/patthana-typed-causation-vocabulary`. (The 24 conditions as a typed-causation vocabulary; this paper's table is independent of its paraphrases.)
12. Ly, T. & Miss Aquarius (2026). *The Wheel That Unwinds the Wheel*. *The Abhidhamma Compiled* №1. `thonly.org/research/abhidhamma-executable-process-specification`.
13. `SiliconWat/formal-abhidhamma`: `matika/RELATA.md`, `matika/Relata.lean`, `matika/run.sh`, `scripts/relata.py`, `scripts/selftest.py`, `runs/PROVE-RUBRIC.md`; commits `bf3cad6`, `9d1dff0`, `0dcae15`, `350dff0`, census `4956261`; run `2026-10-13-kv-8-2-antarabhava-control`.
14. de Moura, L. & Ullrich, S. (2021). "The Lean 4 Theorem Prover and Programming Language." *Automated Deduction – CADE 28*, LNCS, Springer, pp. 625–635. (As verified in №4, ref. 8.)
15. DeMillo, R. A., Lipton, R. J. & Sayward, F. G. (1978). "Hints on Test Data Selection: Help for the Practicing Programmer." *Computer* 11(4), 34–41. (As verified in №4, ref. 18.)
16. Celik, A., Palmskog, K., Parovic, M., Gallego Arias, E. J. & Gligoric, M. (2019). "Mutation Analysis for Coq." *ASE 2019*, pp. 539–551. (As verified in №4, ref. 25.)
17. Barendregt, H. (2010 slides), the *E8* Zenodo record of 2026-06-16, and the Lean/Isabelle Buddhist-logic repository named in №4 ref. 9. (Named in the 2026-10-13 census as contrast; not re-opened for this draft.)
