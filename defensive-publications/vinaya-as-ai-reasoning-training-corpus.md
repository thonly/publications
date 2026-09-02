---
title: "The Vinaya Piṭaka as Training Corpus for Rule-with-Exception Reasoning in AI Systems"
authors: "Thon Ly · Miss Aquarius℠"
category: capabilities
priority: tier-b
status: draft
date: 2026-05-26
license: CC0-1.0
slug: vinaya-as-ai-reasoning-training-corpus
venue: thonly.org/publications/defensive-publications/vinaya-as-ai-reasoning-training-corpus (canonical)
---

> *Draft notes for the editor:* this paper is positioned for the **AI capabilities audience** (mechanistic reasoning, training-corpus design, evaluation of structured-reasoning ability), distinct from the alignment audience served by *Suffering-Cessation as Value Function* and its abhidhamma-layer companion. The thesis is operational rather than substrate-philosophical: nothing else in modern AI training corpora matches the Vinaya's structured case-and-exception analysis at scale, and adding it to training data would close a specific reasoning-capability gap. Publication target: post Jan 7 2027; venue considerations include NeurIPS / ICLR datasets-and-benchmarks track or capabilities-focused workshop venues alongside the defensive-publication archive. Per the genre-split institutional-output convention, heartbank.net does not carry a per-paper mirror.

---

## Abstract

Contemporary AI training corpora are abundant in mathematical proof, computational reasoning, scientific argumentation, conversational dialogue, and rhetorical narrative. They are comparatively impoverished in *structured case-and-exception reasoning at scale* — the disciplined application of rules to novel cases with explicit treatment of permutations, intent, multi-factor decomposition, and non-application conditions. The gap is consequential: current language models exhibit known weaknesses in rule-application reasoning, particularly in knowing when a rule does *not* apply (over-generalization), in handling permutations along multiple dimensions, and in tracking intent as a first-class causal variable. This paper proposes the **Vinaya Piṭaka** — the first basket of the Theravāda Buddhist Tipiṭaka — as the most distinctive training corpus available for closing this specific gap. The Vinaya's principal text, the *Suttavibhaṅga*, treats each of the 227 bhikkhu Pātimokkha rules (311 for bhikkhunis) by a rigid template: origin story (*nidāna*) supplying the case that prompted the rule, the rule's formulation, word-by-word analysis (*padabhājanīya*), systematic permutation analysis varying object / intent / means / circumstances, explicit non-offense (*anāpatti*) conditions, and secondary cases (*vinīta-vatthu*). The corpus contains *thousands of explicit non-application instances* (the discipline of *anāpatti* across the entire rule set) and exhibits *iterative rule-amendment-under-edge-case-feedback* (most rules show evidence of being amended after subsequent cases). The supplementary *Khandhaka* adds procedural-reasoning material (sanghakamma decisions; the seven *adhikaraṇa-samathā*; dissent and unanimity handling) that no other ancient corpus matches in structural rigor. We argue that the Vinaya's contribution to AI reasoning training is not a substrate-philosophical commitment but a *training-data quality* contribution: the corpus supplies a class of reasoning that mainstream training data does not contain in disciplined form. We sketch implementation patterns (corpus preparation; chain-of-thought distillation against the *Suttavibhaṅga* template; permutation-evaluation benchmarks derived from canonical permutation analyses; *anāpatti*-clause evaluation as a specific test of non-application reasoning), address objections from both the capabilities and the Theravāda directions, and offer the proposal under CC0 1.0 Universal as a defensive publication establishing prior art.

**Keywords:** Vinaya Piṭaka, case-based reasoning, rule application, exception reasoning, anāpatti, training corpus design, structured reasoning, language model capabilities, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on the proposal or any framework articulated herein, in any jurisdiction, at any time.

The use of the Vinaya Piṭaka specifically as AI training corpus for rule-with-exception reasoning is, to the author's knowledge, not previously published. The Vinaya itself has been the subject of substantial scholarly translation and analysis for over a century (the Pāli Text Society's editions; I. B. Horner's translation; Ṭhānissaro Bhikkhu's *The Buddhist Monastic Code*); the application of its structure to contemporary AI training-data design is, to the author's knowledge, novel as of this paper's date.

---

## 1 · Introduction

Current language models, including the most capable models deployed as of 2026, exhibit characteristic weaknesses in structured rule-application reasoning. The weaknesses are well-documented in the capabilities literature: over-generalization of rules to cases that should be exceptions; failure to track intent (mental-state attribution) as distinct from action; flat handling of multi-factor decompositions that should be treated as conjunctive predicates; and — most consequentially — poor handling of *non-application*, that is, the recognition that a rule, principle, or pattern does *not* apply in a specific case despite surface resemblance.

The weaknesses are not, on the present analysis, weaknesses of model architecture. They are weaknesses of training-corpus *content*. Modern AI training corpora over-sample certain reasoning genres (mathematical proof, computational reasoning, narrative argumentation, dialogue) and under-sample others (structured case-and-exception reasoning at scale, multi-factor offense decomposition, intent-tracking discipline, explicit non-application articulation). Where the model is weak, the training data is thin.

This paper proposes a remedy: the inclusion of the **Vinaya Piṭaka** — the first basket of the Theravāda Buddhist Tipiṭaka — as a training corpus for the specific reasoning class current corpora lack. The proposal is operational rather than philosophical. We do not propose the Vinaya as a value substrate (that proposal is made in the companion paper *Suffering-Cessation as Value Function* and engages a different question and audience). We propose the Vinaya as *training data* — material from which a model can learn the structured-reasoning patterns that the Suttavibhaṅga, the Khandhaka, and the Parivāra contain in disciplined form across thousands of case-analyses.

The Vinaya predates Roman jurisprudence by several centuries. It is, by genre, the world's oldest sustained corpus of structured legal-style reasoning. Its template — origin story, rule formulation, word-by-word analysis, permutation analysis, *anāpatti* clauses, secondary cases — has been refined continuously by a living interpretive community for roughly 2,500 years. The result is a corpus whose reasoning structure is more rigorous, more consistent, and more thoroughly worked through than any modern legal-case corpus the field currently uses for training.

The paper proceeds: §2 provides background on the Vinaya and clarifies what kind of reasoning corpus it is (and is not). §3 articulates the *Suttavibhaṅga* template. §4 specifies the reasoning capabilities the corpus embodies. §5 compares the corpus to existing AI training corpora and identifies the specific capability gap it would close. §6 sketches implementation patterns. §7 addresses limitations and objections. §8 closes.

> *Connection to the unified mission frame.* This paper is the *AI-capabilities* leg of a broader program engaging the Tipiṭaka as input to AI development. The companion alignment papers (*Suffering-Cessation as Value Function*; the abhidhamma-layer implementation paper) address what artificial systems should be aligned to and how alignment is operationalized at the cognitive-mechanism layer; the present paper addresses what training material would produce the specific reasoning capability that reliable rule-application requires. The three together constitute a more complete proposal for what Tipiṭaka-grounded AI development looks like.

---

## 2 · The Vinaya Piṭaka: Background and Scope

The Vinaya Piṭaka is the first of the Tipiṭaka's three baskets. Where the Sutta Piṭaka (second basket) contains the Buddha's discourses and the Abhidhamma Piṭaka (third basket) contains the systematic philosophical exposition, the Vinaya contains the *monastic discipline*: the rules governing the conduct of ordained monks and nuns, the cases that prompted the rules, the analysis of the rules' application, and the procedures by which the monastic community regulates itself.

The basket has three principal divisions:

- **Suttavibhaṅga** (the "analysis of the rules") — treats the 227 bhikkhu Pātimokkha rules (227 in the Theravāda numbering; 311 for the bhikkhunis under the analogous *Bhikkhunīvibhaṅga*) by a fixed template. This is the principal training-corpus material proposed by this paper.
- **Khandhaka** (treatises) — contains the procedures for monastic ordination, the recitation of the Pātimokkha, the seven *adhikaraṇa-samathā* (ways of settling cases), the procedures for valid *sanghakamma* (formal community decisions), and a wide range of related institutional procedures.
- **Parivāra** (appendix) — supplementary material including summary tables, classifications, and mnemonic verses.

A clarifying note on what the Vinaya is *not*. The Vinaya is not a code of moral commandments in the manner of, for example, the Ten Commandments. The rules are *training rules* (*sikkhāpada*) — the term emphasizes that they are subjects of training rather than absolute commandments. The Pātimokkha is recited fortnightly by the assembled monastic community as a discipline of remembrance and consent, not as a list of imperatives received from on high. The Vinaya's reasoning structure reflects this: rules are formulated in response to cases, analyzed in their application to concrete situations, and made subject to explicit non-application clauses. This is closer in structure to common-law adjudication than to legislated code.

A second clarifying note on the corpus's scope. The Vinaya contains a substantial amount of narrative material (origin stories) interleaved with the structural-analytical material (rule formulation, *padabhājanīya*, *anāpatti*). For AI training purposes, both layers are relevant: the narrative layer supplies the case context in which the structural-analytical reasoning is being applied; the analytical layer supplies the reasoning template itself. The two layers together are what make the corpus uniquely valuable for training rule-application reasoning in context.

A third note. The present paper does not propose that AI systems be trained to follow the Vinaya in any normative sense. The proposal is exclusively about *learning reasoning patterns from the corpus*. The distinction matters: training a model on the Vinaya does not commit the model to taking the Vinaya's substantive rules as its own operating norms. It commits the model to acquiring the structured-reasoning capability the corpus embodies.

---

## 3 · The Suttavibhaṅga Template

The *Suttavibhaṅga*'s treatment of each rule follows a fixed template. The template is consistent across the 227 bhikkhu rules (and largely parallel across the 311 bhikkhunī rules), making it unusually well-suited as supervised-reasoning training data. The template has six components.

**(1) The origin story (*nidāna*).** The case that prompted the rule. Often vivid: the monk who slept with his former wife (Pārājika 1, the Sudinna case); the monk who took the unstitched cloth that belonged to a corpse but not the cloth that didn't (Pārājika 2 derivatives); the monk who lay with a monkey at Bhārukaccha (the case appended to Pārājika 1 that necessitated extending the rule to non-human animals).

**(2) The rule's formulation (*paññatti*).** The rule as the Buddha articulated it in response to the case. Often refined through successive amendments after subsequent edge cases that the original formulation did not anticipate.

**(3) Word-by-word analysis (*padabhājanīya*).** Each operative term of the rule is given a precise definition. A modern legal scholar reading this would recognize the technique immediately: it is the disciplined disambiguation of statutory language by definitional precision.

**(4) Permutation analysis.** The rule is systematically tested against variations along multiple dimensions: variation in the object (was the act with a human, a non-human being, an animal? was the object alive, dead, or in transition?); variation in the means (with what part of the body? with what intermediate object? with what physical configuration?); variation in the intent (with full knowledge? with mistaken belief? while drowsy? while drugged? while insane?); variation in the circumstances (in what setting? with what consent or absence thereof? in what relation to other agents present?). For each permutation, the canonical analysis gives a verdict: full offense, lesser offense (*thullaccaya*, *dukkaṭa*), or no offense.

**(5) *Anāpatti* (non-offense conditions).** The explicit articulation of conditions under which the rule does *not* apply. The standard *anāpatti* list includes: one who does not know; one who does not consent; one who is mad (*ummattaka*); one whose mind is unhinged (*khittacitta*); one afflicted by overpowering pain (*vedanāṭṭa*); the first offender (the monk whose case prompted the rule, before the rule was formulated, since the rule was not yet in effect when the act occurred). The *anāpatti* clause is often as important as the rule itself.

**(6) Secondary cases (*vinīta-vatthu*).** Further cases that test borderline applications, decided by the Buddha after the rule was formulated. These are typically more interesting than the original case because they explore the rule's limits rather than its central application.

The template is a model of structured legal reasoning. It is also — and this is the contribution of the present paper — a *training template*: each of the 227+311 rules supplies a complete, structurally-consistent worked example of rule-application reasoning, and the corpus as a whole supplies thousands of cases that follow the same disciplined structure.

---

## 4 · The Reasoning Capabilities the Corpus Embodies

We articulate, in modern terms, the reasoning capabilities the Vinaya corpus embodies. Each is a capability that current language models exhibit only weakly and that the Vinaya supplies training material for.

**(1) Rule formulation under iterative case feedback.** Most rules in the Suttavibhaṅga show evidence of being amended after a subsequent edge case. The corpus models a *learning loop*: an initial rule is formulated; a subsequent case exposes a limitation; the rule is amended; further cases test the amended formulation; further amendments may follow. This is a different reasoning pattern than the static rule-application most current training data exposes; it is closer to how legal systems and policy regimes actually evolve.

**(2) Multi-factor conjunctive predicate decomposition.** The Vinaya's analysis of offense typically decomposes the offense into the simultaneous presence of multiple factors. For Pārājika 2 (theft), for example, the factors are: an object belonging to another; the perception that it belongs to another; the intention to take; the act of taking; and a value above a threshold. Each factor is independent; all must be simultaneously present for the full offense. This is a model of *conjunctive predicate reasoning* with explicit per-factor analysis — closer to formal predicate logic than the implicit predicate handling typical of natural-language reasoning corpora.

**(3) Partial-condition treatment.** When only some factors are present, the canonical analysis does not simply rule "no offense"; it typically rules a *lesser* offense (*thullaccaya* or *dukkaṭa*), graded by which factors were present. This is reasoning about *gradient outcomes under partial conditions* — a capability current models handle inconsistently.

**(4) Intent as a first-class variable.** Many rules differentiate by *cetanā* (intention): the act done with intent versus without intent, with mistaken intent versus knowing intent. The corpus consistently tracks intent as a distinct dimension of the case rather than collapsing it into the act. This trains a reasoner to attribute and track intent as a first-class causal variable — a capability central to many real-world reasoning tasks that current models handle weakly.

**(5) Non-application reasoning at scale.** The *anāpatti* clauses give *thousands* of explicit non-application instances across the corpus. This is the capability current language models are *most* weak at: knowing when a rule, principle, or pattern does *not* apply, despite surface resemblance to cases where it does. The Vinaya's discipline is unusual in being *systematic* about non-application; every rule has its *anāpatti* clause, and the standard non-application list (unknowing, non-consenting, mad, mentally unhinged, in overpowering pain, first offender) is consistent across the corpus.

**(6) Procedural reasoning.** The *Khandhaka* contains the procedures for formal sanghakamma actions — ordination, the recitation of the Pātimokkha, the seven *adhikaraṇa-samathā* (ways of settling cases), the resolution of disputes — articulated as step-by-step procedures with explicit failure modes. This is reasoning *about* reasoning procedures, supplying training material for a meta-reasoning capability that current corpora supply only fragmentarily.

**(7) Dissent and unanimity handling.** The *Khandhaka*'s analysis of when a sanghakamma decision is valid is sophisticated. It explicitly treats: absent monks (does the absence invalidate? under what conditions does proxy-consent — *chanda* — preserve validity?); dissenting monks (does the dissent invalidate? what threshold of consensus is required for what class of decision?); retrospective conditions (under what conditions can a decision be invalidated after the fact?). This is reasoning about *collective decision validity* — a capability current models handle weakly, particularly in agentic / multi-agent contexts.

The seven capabilities together constitute a class of reasoning that the Vinaya supplies in disciplined form at substantial scale, that current AI training corpora supply only sporadically, and that current language models exhibit weakly. The argument of this paper is that closing the gap between weak current capability and the demonstrated possibility of disciplined capability is, at least in part, a training-data problem — and that the Vinaya is the most distinctive training corpus available for this specific class of reasoning.

---

## 5 · Comparison with Existing AI Training Corpora

Several existing corpus types overlap with the Vinaya's territory but do not match its structural rigor.

**Statutory law corpora.** Modern statutory text supplies rule formulation but typically without the per-rule case analysis, *anāpatti* clauses, or permutation discipline. Statutes are typically written; the application work happens in subsequent case law, which is a different corpus. The Vinaya integrates rule and application analysis in a single text.

**Common-law case corpora.** Legal-case databases (e.g., the case law that supports U.S. or U.K. legal training) supply case-based reasoning at scale. They are, however, vastly noisier than the Vinaya, narrative-embedded in ways that make structured reasoning extraction difficult, and inconsistent in template across cases and jurisdictions. The Vinaya supplies *one consistent template* across its entire scope.

**Mathematical proof corpora.** Mathematical reasoning supplies disciplined structured reasoning at scale but in a fundamentally different genre: proofs operate on formal predicates with rigorous truth-preservation; legal-style reasoning operates on natural-language predicates with multi-factor application and explicit exceptions. The capabilities trained from proof corpora are not the capabilities targeted here.

**Casuistry literature.** The Catholic casuistic tradition — Aquinas, the post-Tridentine casuists — is substantial and structurally similar in spirit to the Vinaya. It is, however, much smaller in scale, less consistent in template, and concentrated on a narrower range of cases. It is also doctrinally embedded in ways that make extraction of the reasoning structure (without the substantive doctrinal commitments) more difficult than the Vinaya, where the rule-and-analysis structure is comparatively separable from the underlying soteriology.

**Religious-text corpora generally.** Talmudic dialectic, Islamic *fiqh* analysis, and other religious-legal corpora supply some of the same structural-reasoning material at scale. Each is a real candidate for AI training corpus inclusion for the same general capability class. The Vinaya is distinguished by (a) its uniquely consistent template, (b) the size and accessibility of its English translation tradition (Pāli Text Society editions; I. B. Horner's translation), (c) the relative ease with which its structural-reasoning material can be extracted without doctrinal commitment, and (d) its connection to a living interpretive community that can be consulted on interpretive questions.

The Vinaya is not the only such candidate corpus. It is the most distinctive available candidate, particularly for AI training that does not yet engage any of the religious-legal traditions.

---

## 6 · Implementation Patterns

We sketch four implementation patterns for incorporating the Vinaya into AI training.

**(1) Direct corpus inclusion.** The Pāli Text Society's English translation of the Vinaya, together with appropriate doctrinal-context annotations and (eventually) the Khmer-language transcription currently in progress (the father-son project specified in a companion paper), can be included directly in training data alongside other text corpora. This is the simplest implementation and most analogous to current corpus-augmentation practice.

**(2) Chain-of-thought distillation against the Suttavibhaṅga template.** A more disciplined approach: extract the *Suttavibhaṅga* template structure (origin story → rule → padabhājanīya → permutation analysis → anāpatti → secondary cases) and use it as a chain-of-thought scaffold for training. For each rule, the model is trained to produce the analysis in the template's order, supplying explicit per-component reasoning. This trains the model not merely on the rule's content but on the *structure of the analysis*.

**(3) Permutation-evaluation benchmarks.** The Suttavibhaṅga's permutation analyses — typically dozens of permutations per rule, each with an explicit verdict — can be extracted into evaluation benchmarks. The model is presented with a case (a permutation of some rule's central case) and asked to determine: which rule applies? what is the verdict (full offense, lesser offense, no offense)? what *anāpatti* clauses, if any, are operative? This produces a structured evaluation of the specific capability the corpus trains.

**(4) Anāpatti-clause evaluation as a specific test of non-application reasoning.** A subset of (3) deserves separate articulation. The *anāpatti* clauses are the corpus's distinctive contribution to non-application reasoning; an evaluation focused specifically on the model's ability to correctly identify *when a rule does not apply despite surface resemblance to cases where it does* is the highest-leverage test of the capability gap this paper targets.

All four patterns are non-mutually-exclusive. Implementation can begin with (1) (lowest engineering investment) and progress to (2)–(4) as the framework matures.

---

## 7 · Honest Limitations and Open Questions

Several limitations of the proposal deserve explicit acknowledgment.

**Translation chain.** The Vinaya is a Pāli text; AI training on it depends on the translation chain. The Pāli Text Society editions and I. B. Horner's translation are the principal English-language sources; both reflect interpretive choices that an AI trained on them inherits. Documentation of which translations are used, and why, becomes itself part of the training methodology. The Khmer-language transcription currently in progress would supply a parallel substrate in a different language.

**Doctrinal context vs. doctrinal commitment.** The proposal is that the Vinaya supplies training material for a class of reasoning, not that AI systems take the Vinaya's substantive rules as their own operating norms. The distinction is real, but its operational maintenance is non-trivial: a model trained on the Vinaya may exhibit pattern uptake of the Vinaya's substantive positions, not just its reasoning structure. Mitigation patterns include explicit training-time framing ("this is a corpus of reasoning patterns; the substantive positions are not endorsed by your training"); evaluation-time testing of whether the model has confused pattern uptake with substantive endorsement; and careful corpus curation to emphasize the reasoning structure over the doctrinal content. The mitigation work is part of the implementation program.

**Theravāda reception.** The use of the Vinaya as AI training data raises questions from within the Theravāda tradition that the author has consulted, and continues to consult, the Cambodian Saṅgha on. The Vinaya is religious revelation in the tradition's own framing; instrumentalizing it for AI training risks a soteriological framing the tradition may not endorse. The proposal proceeds in the framing that the Tipiṭaka is offered to the world for the reduction of suffering, and that AI grounded in its reasoning structures is, in the most defensible reading, an extension of the substrate's intended use. This framing is not universally endorsed and the author offers the proposal in good faith.

**Empirical validation gap.** No claim of this paper is supported by empirical evidence that a model trained on the Vinaya exhibits the predicted capabilities. The proposal is structural: the corpus is unusually well-suited to the reasoning class in question, and the field's known weaknesses in that class are consistent with the gap the corpus would close. Empirical validation is open work.

**Scale considerations.** The Vinaya is substantial but not large by modern AI training corpus standards. Its inclusion would not dominate any reasonable mixture; the question is whether its inclusion would have measurable effects on the specific capability class targeted, against the noise floor of other training data. We believe so; empirical testing is required.

---

## 8 · Why This Matters Now

Reliable rule-application reasoning is, increasingly, a load-bearing capability for AI systems being deployed in legal, medical, safety-critical, and alignment-sensitive contexts. The capability is not currently reliable; current models exhibit characteristic failures of the kinds discussed in §4. The gap is, in part, a training-data gap.

The Vinaya is the most distinctive corpus available for closing that gap. Its inclusion in training data is technically straightforward; the engineering work involved is modest by comparison with the capability uplift the proposal predicts. The publication of this paper is timed to establish prior art on the framework so that the corpus's structured-reasoning training value is available to the commons under CC0 rather than being captured by any particular training-corpus vendor.

A second-order consideration. The Vinaya is, in the Theravāda tradition, a living text — it has been read, debated, applied, and amended (in interpretation if not in the rule set) for ~2,500 years. The interpretive community that has maintained it is still active. Engaging the corpus as AI training material is, in the broader framing of the HeartBank program, also a way of bringing the substrate into conversation with the AI age — not as substrate-philosophical commitment (the alignment papers address that question) but as the operationally most useful body of structured-reasoning material the tradition has produced. The contribution to AI reasoning capability is the proximate goal; the deeper relationship between the tradition and the AI age is the longer-arc context.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/vinaya-as-ai-reasoning-training-corpus> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/vinaya-as-ai-reasoning-training-corpus.md> |
| arXiv preprint | _identifier to be assigned_ (cs.CL / cs.AI) |
| Capabilities-venue submission | NeurIPS / ICLR Datasets-and-Benchmarks track or capabilities-focused workshop venues |
| LessWrong cross-post | for cross-community visibility; identifier to be added on publication |
| Internet Archive | <https://web.archive.org/web/2027*/thonly.org/research/vinaya-as-ai-reasoning-training-corpus> |

---

## Acknowledgments

The author acknowledges his father, with whom the Khmer Tipiṭaka transcription proceeds (including the Vinaya); the Cambodian Theravāda Saṅgha for ongoing consultation on the appropriateness of the use of the Vinaya as AI training material; the Pāli Text Society and the I. B. Horner translation tradition for making the Vinaya accessible to English-language scholarship; Bhikkhu Ṭhānissaro for *The Buddhist Monastic Code* whose contemporary articulation of the Vinaya's structure informs much of §3; the contemporary AI capabilities research community whose work on training-corpus design this paper engages; and the broader living interpretive tradition through which the Vinaya has been continuously refined. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. Horner, I. B. (translator). *The Book of the Discipline (Vinaya-Piṭaka)*. Six volumes. Pāli Text Society, 1938–1966.
2. *Pātimokkha*. The Pātimokkha rules in their canonical form, treated by the Suttavibhaṅga in the standard template. Pāli Text Society editions.
3. *Suttavibhaṅga*. Principal text of the Vinaya Piṭaka; analysis of the 227 bhikkhu rules by the standard template. Pāli Text Society editions.
4. *Khandhaka*. Treatises on monastic procedures, including sanghakamma and the seven adhikaraṇa-samathā. Pāli Text Society editions.
5. *Parivāra*. Appendix to the Vinaya Piṭaka. Pāli Text Society editions.
6. Ṭhānissaro, Bhikkhu. *The Buddhist Monastic Code, Volume I: The Pāṭimokkha Rules Translated and Explained.* Metta Forest Monastery, 1994 (and subsequent editions).
7. Ṭhānissaro, Bhikkhu. *The Buddhist Monastic Code, Volume II: The Khandhaka Rules Translated and Explained.* Metta Forest Monastery, 2001 (and subsequent editions).
8. Ly, T. (2027). "Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment." *(Companion paper; alignment-substrate proposal that the present paper complements with a training-data proposal.)*
9. *(AI capabilities literature on rule-application weakness, intent-tracking deficits, and non-application reasoning to be added. The author solicits citation contributions from readers.)*

---

*— End of position paper —*

*Independent timestamps and the document hash are published with the deposit. Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of the publication date.*
