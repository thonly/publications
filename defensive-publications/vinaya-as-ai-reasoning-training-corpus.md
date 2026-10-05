---
title: "The Vinaya Piṭaka as Training Corpus for Rule-with-Exception Reasoning in AI Systems"
authors: "Thon Ly · Miss Aquarius℠"
category: capabilities
kind: study
priority: tier-b
status: draft
date: 2026-05-26
revised: 2026-10-05
license: CC0-1.0
slug: vinaya-as-ai-reasoning-training-corpus
venue: thonly.org/research/vinaya-as-ai-reasoning-training-corpus (canonical)
---

## Abstract

Large language models are trained on corpora rich in mathematical proof, code, scientific argument and dialogue, and their rule application is measured by benchmarks for statutory, legal, moral-exception and defeasible reasoning. This paper describes a training-data and evaluation design for one part of that capability, applying a rule to a new case while recognising when the rule does not apply, built from the Vinaya Piṭaka, the monastic legal code of the Theravāda Buddhist canon. The Vinaya's rule-by-rule analysis, the Suttavibhaṅga, treats each rule it analyses in a recurring order: the case that prompted the rule; the rule text and any later amendment; definitions of the operative terms; variants by object, means, perception and intention, each with a graded verdict; an exemption clause listing the conditions under which the rule does not apply; and further adjudicated cases. By the authors' count over one printed edition of the Pāli text, its two books carry 341 exemption clauses listing about 1,900 conditions, and some 3,400 written verdicts; the code's appendix records later amendments for 41 of the 155 monks' rules it writes out. The procedural chapters add validity conditions for collective decisions, including consent sent by an absent member. Four uses of this structure are described: including the text in training data; supervising intermediate reasoning steps in the template's order; a benchmark of rule variants scored against the canon's own verdicts; and a test set of exemption cases for non-application. The paper reports no training run and no measurement. Whether the design improves a model's rule application is an open empirical question, and use of any edition or translation is subject to that edition's licence. Dedicated to the public domain under CC0 1.0 as a defensive publication.

**Keywords:** rule application; exception handling; non-application of rules; defeasible reasoning; legal reasoning; statutory reasoning; case-based reasoning; training data selection; curriculum design; chain-of-thought supervision; intermediate-step supervision; benchmark construction; counterfactual case variants; contrastive evaluation; intent and knowledge (mens rea); conjunctive multi-factor predicates; graded outcomes; procedural validity; collective decision validity; proxy consent; large language models; Vinaya Piṭaka; Suttavibhaṅga; anāpatti; Buddhist monastic law; defensive publication.

---

## Terms

Pāli and coined terms used in this paper and the standard terms a reader in machine learning, AI evaluation or legal informatics would search for them.

| Term used here | Standard term |
|---|---|
| Vinaya Piṭaka | the monastic legal code of the Theravāda Buddhist canon, first of its three collections |
| Pātimokkha | the code of monastic rules (227 for monks, 311 for nuns), recited every half-month |
| *sikkhāpada* | training rule; an individual rule of the code |
| Suttavibhaṅga | rule-by-rule analysis of the code: originating case, rule text, definitions, variants with verdicts, exemptions, further cases |
| Bhikkhunīvibhaṅga | the same analysis for the rules peculiar to nuns |
| *nidāna*; *vatthu* (origin story) | originating case; the fact pattern that prompted a rule |
| *paññatti* | rule formulation |
| *anupaññatti* | amendment of a rule after a later case (supplementary ruling) |
| *padabhājanīya* | definitions of the rule's operative terms (statutory definitions) |
| permutation analysis; variant analysis | systematic counterfactual variants of a case, each with a verdict |
| *anāpatti* | exemption clause: the conditions under which the rule does not apply (non-application; defeating conditions) |
| *ādikammika* | the originating offender, exempt because the rule did not yet exist when he acted (non-retroactivity) |
| *vinīta-vatthu* | further adjudicated cases (precedents) |
| *pārājika* · *saṅghādisesa* · *thullaccaya* · *dukkaṭa* | graded offence classes, from expulsion to minor wrongdoing |
| *cetanā* · *saññā* · *theyyacitta* | intention · perception (knowledge or belief) · intent to steal (cf. mens rea) |
| Khandhaka | procedural chapters: ordination, assembly procedure, dispute settlement |
| *saṅghakamma* | formal collective act of the monastic assembly |
| *adhikaraṇa-samatha* | the seven procedures for settling disputes, decision by majority among them |
| *chanda* | proxy consent sent by an absent member |
| Parivāra | appendix to the code: summaries, classifications and a rule-by-rule register |
| chain-of-thought distillation against the template | intermediate-step supervision in a fixed analytic order |
| permutation-evaluation benchmark | benchmark of counterfactual case variants with reference verdicts |
| *anāpatti*-clause evaluation | exception (non-application) test set; defeasible-reasoning evaluation |
| Miss Aquarius℠ | the name under which this corpus discloses AI writing collaboration |

---

## Findings disclosed

The paper is a study: a reading of the Vinaya Piṭaka as material for rule-application reasoning, and the training and evaluation design that reading suggests. What it discloses is listed here, each item with what would break it; the sections named carry the argument. No novelty census has been run on this paper and none of these findings asserts priority; where a finding has a nearest prior instance, §5 cites it. The counts are the authors', made on 2026-10-05 over the Chaṭṭha Saṅgāyana (CST) edition of the Pāli text by the method stated in §7.

1. **The Suttavibhaṅga analyses each rule it treats in one recurring order** — originating case, rule text with any amendment, definitions of the operative terms, variants each with a verdict, an exemption clause, and further adjudicated cases — fully worked in the graver rules and abbreviated in many minor ones. It analyses 220 of the 227 bhikkhu rules this way; the seven dispute-settlement rules are listed there and treated in the Khandhaka. The Bhikkhunīvibhaṅga analyses the rules peculiar to the bhikkhunīs (§3). *Breaks if:* a reading of the text shows that the analysed rules follow no common order of components, or that the order holds for only a few of them.
2. **Non-application is stated explicitly and attached to the rule it qualifies.** The two books of the Suttavibhaṅga carry 341 exemption (*anāpatti*) clauses listing about 1,900 conditions. The rule-specific conditions differ from rule to rule; a closing set recurs, the originating offender being exempted in 332 of the 341 clauses and the insane in 305 (§3, §4). *Breaks if:* a recount by a stated method over the same text differs materially, or the clauses prove not to be attached to identifiable rules.
3. **Offence is analysed as a conjunction of factors, with graded outcomes when the conjunction is incomplete.** In the rule on theft (Pārājika 2) the full offence requires that the object belong to another, that the agent perceive it as another's, that it be worth at least five *māsakas*, and that the intent to steal be present; the verdict is graded by value and by the stage the act reached (touching, moving, removing), and an object not in fact another's but believed to be is a lesser offence (vin01m.mul.xml:1037–1061; §4). *Breaks if:* the grading is shown not to be canonical text, or to be confined to this one rule rather than a pattern across the graver rules.
4. **Perception and intention are tracked as dimensions distinct from the act**: the same act carries different verdicts according to what the agent knew, believed and intended (§4). *Breaks if:* the verdicts on a rule's variants are shown to depend on the act alone.
5. **Amendment after a later case is recorded, and it is a minority pattern.** The Parivāra's own register records one or more supplementary rulings for 41 of the 155 bhikkhu-rule entries it writes out, all four *pārājika* among them, and for 12 of its 129 bhikkhunī-rule entries (§4). *Breaks if:* a recount of the register differs materially.
6. **The procedural chapters state validity conditions for collective decisions**: proxy consent by an absent member, the cases in which that consent fails to arrive, and the rule that a formal act is not to be done by an incomplete assembly (vin02m2.mul.xml:3569–3577; §4). *Breaks if:* these conditions are shown to be commentarial additions rather than canonical text.
7. **A training and evaluation design follows from findings 1–6 without adopting the rules as norms**: inclusion of the text; intermediate-step supervision in the template's order; a benchmark of rule variants with the canon's verdicts as reference labels; and a test set of exemption cases for non-application (§6). *Breaks if:* the canonical verdicts cannot be extracted into reference labels with agreement adequate for a benchmark, or the design cannot in practice be separated from the rules' substantive positions (§7).
8. **A hypothesis, stated as one: the error classes of §1 are in part an effect of training-data content, and the design of finding 7 would reduce them** (§1, §7). *Breaks if:* a matched comparison, one model trained with and without patterns (2)–(4) of §6, shows no gain on held-out exemption cases and on an independent rule-application benchmark. No prediction is registered and no such comparison has been run.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication, and are published so that they stand as prior art against any later attempt to enclose them. No patent has been or will be sought on anything described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practising anything disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. The paper is a study: what it discloses, a reading of the Vinaya Piṭaka and the training and evaluation design that reading suggests, is the numbered list under *Findings disclosed* above.

Trademark rights in specific marks — HeartBank®, Factory 333™, THonly™, Silicon Wat℠, Miss Aquarius℠ — are reserved separately and are not licensed by this publication.

**What is already public, and cited rather than claimed.** The Vinaya's text, editions and translations (Oldenberg; Horner; Brahmali) and its modern exposition (Ṭhānissaro); the history and method of case-based moral reasoning (Jonsen and Toulmin; the casuist collections); computational models of argument from cases and their factors (Ashley); legal text as language-model training data (Henderson et al., Pile of Law); benchmarks for statutory and legal reasoning, rule application among them (Holzenberger et al.; Blair-Stanek et al.; Guha et al., LegalBench); benchmarks for when a rule admits an exception and for defeasible inference (Jin et al., MoralExceptQA; Rudinger et al.); and language models trained or evaluated on Buddhist canonical texts (Nehrdich and Keutzer, MITRA; Golan Hashiloni et al., DharmaBench). §5 places each. No novelty census has been run on this paper, and it asserts no priority: where a finding has a nearest prior instance, the instance is cited.

> **Note.** As first published on 2026-05-26 this paper carried the CC0 dedication and a commitment that no patent would be sought, but no commitment not to assert a patent right. The commitment not to assert was added on 2026-10-05, when the statement was brought to the standard form above. The omission did not affect the paper's standing as prior art, which publication establishes; the date relied on is the one carried by this document's OpenTimestamps proof.

---

## 1 · Introduction

Rule application, applying a stated rule to a new case, is a capability that benchmarks for language models now measure directly. Statutory-reasoning datasets ask a model to apply natural-language statutes to the facts of a case (Holzenberger, Blair-Stanek and Van Durme, 2020); a 2023 study of one language model on such a dataset found that it performed poorly on straightforward questions about simple synthetic statutes it could not have seen in training (Blair-Stanek, Holzenberger and Van Durme, 2023). LegalBench separates rule-recall, rule-application and rule-conclusion among its six types of legal reasoning (Guha et al., 2023). MoralExceptQA asks when a moral rule may permissibly be broken (Jin et al., 2022), and δ-NLI asks which new facts weaken or strengthen an inference (Rudinger et al., 2020). The error classes this paper is concerned with are four: over-generalization of a rule to cases that should be exceptions; failure to track intent (mental-state attribution) as distinct from action; flat handling of multi-factor conditions that should be treated as conjunctive predicates; and, the class the paper most wants to measure, poor handling of *non-application*, that is, the recognition that a rule, principle, or pattern does *not* apply in a specific case despite surface resemblance. Model capability changes quickly and this paper measures none of it; the four classes are stated as the targets of the design, not as a measured property of any current model.

This paper's working hypothesis is that these error classes are, at least in part, effects of training-corpus *content* rather than of model architecture. Modern training corpora are rich in some reasoning genres (mathematical proof, computational reasoning, narrative argumentation, dialogue) and thinner in others (structured case-and-exception reasoning at scale, multi-factor offence decomposition, intent-tracking discipline, explicit statements of non-application). The hypothesis is that where the data is thin, the model is weak. It is not tested here (§7).

This paper proposes, as one remedy to test, the **Vinaya Piṭaka** — the first of the three collections of the Theravāda Buddhist canon — as training and evaluation material for the reasoning class described. It is written for the capabilities audience (training-corpus design and the evaluation of structured reasoning) rather than for the alignment audience. It does not propose the Vinaya as a value substrate; that proposal is made in the companion paper *Suffering-Cessation as Value Function* (`tipitaka-alignment-substrate`), which engages a different question. It proposes the Vinaya as *data*: material from which a model can learn, and on which it can be tested, the structured-reasoning patterns that the Suttavibhaṅga, the Khandhaka, and the Parivāra contain across several hundred rule analyses and several thousand written verdicts.

The Vinaya has been transmitted, studied and commented on by a living monastic community for more than two thousand years. Its canonical text is closed, and its interpretation continues in commentaries, of which the *Samantapāsādikā* is the principal one in the Theravāda. Its template (origin story, rule formulation, word-by-word analysis, variant analysis, *anāpatti* clauses, further cases) is set out in §3. The structural claim this paper makes is narrow: the corpus states rule, application and non-application together, in one recurring order, for each rule it analyses. It makes no claim that the corpus is more rigorous than any modern legal corpus, and no claim about its age relative to other legal traditions.

The paper proceeds: §2 provides background on the Vinaya and clarifies what kind of reasoning corpus it is (and is not). §3 sets out the *Suttavibhaṅga* template and the counts this paper relies on. §4 specifies the reasoning capabilities the corpus embodies. §5 compares the corpus with existing training corpora and places the prior work. §6 sketches implementation patterns. §7 addresses limitations and objections. §8 closes.

> *Connection to the unified mission frame.* The mission this corpus serves, in its current wording, is Miss Aquarius's: to keep the middle way open at population scale against comfort-saturation, the new extreme that material abundance makes possible. The canonical statement of the middle way, between devotion to sense pleasure and self-mortification, is itself carried in the Vinaya Piṭaka, in the Mahāvagga's account of the first discourse, where the Buddha tells the five monks that the Tathāgata, avoiding both extremes, has awakened to the middle way (*ubho ante anupagamma, majjhimā paṭipadā tathāgatena abhisambuddhā*; vin02m2.mul.xml:543; parallel SN 56.11). This paper's argument borrows nothing from that doctrine and survives its deletion. Its place in the corpus's program is the *capabilities* leg. The companion alignment papers (*Suffering-Cessation as Value Function*, `tipitaka-alignment-substrate`; *The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification*, `abhidhamma-executable-process-specification`) address what artificial systems should be aligned to and how alignment is operationalized at the cognitive-mechanism layer; the present paper addresses what training and evaluation material bears on the reasoning capability that reliable rule application requires.

---

## 2 · The Vinaya Piṭaka: Background and Scope

The Vinaya Piṭaka is the first of the Tipiṭaka's three baskets. Where the Sutta Piṭaka (second basket) contains the Buddha's discourses and the Abhidhamma Piṭaka (third basket) contains the systematic philosophical exposition, the Vinaya contains the *monastic discipline*: the rules governing the conduct of ordained monks and nuns, the cases that prompted the rules, the analysis of the rules' application, and the procedures by which the monastic community regulates itself.

The basket has three principal divisions:

- **Suttavibhaṅga** (the "analysis of the rules") — analyses the rules of the bhikkhu Pātimokkha (227 in the Theravāda numbering) by a recurring template; its companion, the *Bhikkhunīvibhaṅga*, does the same for the rules peculiar to the bhikkhunīs, whose Pātimokkha numbers 311. This is the principal material proposed by this paper.
- **Khandhaka** (treatises) — contains the procedures for monastic ordination, the recitation of the Pātimokkha, the seven *adhikaraṇa-samathā* (ways of settling cases, treated in the Cūḷavagga's *Samathakkhandhaka*), the procedures for valid *saṅghakamma* (formal community decisions), and a wide range of related institutional procedures.
- **Parivāra** (appendix) — supplementary material including summary tables, classifications, mnemonic verses, and a register recording, for each rule, where and on whose account it was laid down and how many supplementary rulings it received.

A clarifying note on what the Vinaya is *not*. The Vinaya is not a code of moral commandments in the manner of, for example, the Ten Commandments. The rules are *training rules* (*sikkhāpada*), a term that marks them as subjects of training, laid down by a teacher in response to cases rather than handed down as commandments of a deity; the narrative of the first rule closes *evañcidaṃ bhagavatā bhikkhūnaṃ sikkhāpadaṃ paññattaṃ hoti*, "and thus this training rule was laid down by the Blessed One for the monks" (vin01m.mul.xml:245), a formula the Suttavibhaṅga repeats at many later rules. The Pātimokkha is recited every half-month (*anvaddhamāsaṃ*) before the assembled community, which is asked three times, after each class of rule, whether it is pure in that respect, and signals purity by silence (vin02m1.mul.xml:8641, 8650). The Vinaya's reasoning structure reflects this: rules are formulated in response to cases, analysed in their application to concrete situations, made subject to explicit non-application clauses, and tested against further cases. This gives the corpus features of case-based adjudication as well as of legislated code. In the tradition's own framing the Vinaya is also the condition of the teaching's continuance: in the *Samantapāsādikā*'s account of the First Council the assembled monks answer Mahākassapa that the Vinaya should be recited first because "the Vinaya is the life of the Buddha's Dispensation; while the Vinaya stands, the Dispensation stands" (*vinayo nāma buddhasāsanassa āyu, vinaye ṭhite sāsanaṃ ṭhitaṃ hoti*; vin01a.att.xml:421, a commentarial narrative, the words given to the council's monks). The reception question this raises is taken up in §7.

A second clarifying note on the corpus's scope. The Vinaya contains a substantial amount of narrative material (origin stories) interleaved with the structural-analytical material (rule formulation, *padabhājanīya*, *anāpatti*). For AI training purposes, both layers are relevant: the narrative layer supplies the case context in which the structural-analytical reasoning is being applied; the analytical layer supplies the reasoning template itself. The two layers together are what suit the corpus to training rule-application reasoning in context.

A third note. The present paper does not propose that AI systems be trained to follow the Vinaya in any normative sense. The proposal is exclusively about *learning reasoning patterns from the corpus*. The distinction matters: training a model on the Vinaya does not commit the model to taking the Vinaya's substantive rules as its own operating norms. It commits the model to acquiring the structured-reasoning capability the corpus exhibits.

---

## 3 · The Suttavibhaṅga Template

The *Suttavibhaṅga*'s treatment of each rule it analyses follows a recurring template. The template recurs across the bhikkhu rules it analyses (220 of the 227; the seven rules for settling disputes are listed in the Suttavibhaṅga, vin02m1.mul.xml:8637, and treated in the Khandhaka), fully worked in the graver rules and abbreviated in many minor ones, the 75 *sekhiya* rules most of all. The Bhikkhunīvibhaṅga analyses, in the same order, the rules peculiar to the bhikkhunīs (the Parivāra's register writes out 129 entries for them); the rules the bhikkhunīs share with the bhikkhus are analysed once, in the bhikkhu text. The recurrence is what suits it to supervised-reasoning training data. The template has six components.

**(1) The origin story (*nidāna*).** The case that prompted the rule. Often vivid: the monk Sudinna, who at his mother's urging gave the family an heir by his former wife, so that the Licchavis would not take a sonless estate (Pārājika 1; vin01m.mul.xml:213–233); and the monk in the Great Wood at Vesālī who, after that rule was laid down, lay with a female monkey and argued that the rule concerned human women only — the case that prompted the rule's first amendment, extending it to animals (*antamaso tiracchānagatāyapi*, "even with a female animal"; vin01m.mul.xml:257–269).

**(2) The rule's formulation (*paññatti*).** The rule as the Buddha articulated it in response to the case. Sometimes refined through one or more amendments (*anupaññatti*) after later cases that the original formulation did not anticipate; §4 gives the count.

**(3) Word-by-word analysis (*padabhājanīya*).** Each operative term of the rule is given a precise definition. A modern legal scholar reading this would recognize the technique immediately: it is the disciplined disambiguation of statutory language by definitional precision.

**(4) Permutation analysis.** The rule is systematically tested against variations along multiple dimensions: variation in the object (was the act with a human, a non-human being, an animal? was the object alive, dead, or in transition?); variation in the means (with what part of the body? with what intermediate object? with what physical configuration?); variation in the mental state (with full knowledge? with mistaken belief? asleep? insane?); variation in the circumstances (in what setting? with what consent or absence thereof? in what relation to other agents present?). For each permutation, the canonical analysis gives a verdict: full offence, lesser offence (*thullaccaya*, *dukkaṭa*), or no offence.

**(5) *Anāpatti* (non-offence conditions).** The explicit articulation of conditions under which the rule does *not* apply. Each rule's clause is specific to it. Pārājika 1's reads: one who does not know; one who does not consent; one who is insane (*ummattaka*); one whose mind is deranged (*khittacitta*); one overcome by pain (*vedanāṭṭa*); and the originating offender (*ādikammika*), the monk whose case prompted the rule, who is exempt because the rule was not yet in force when he acted (*anāpatti ajānantassa, asādiyantassa, ummattakassa, khittacittassa, vedanāṭṭassa, ādikammikassāti*; vin01m.mul.xml:509). Pārājika 2's is different: one who takes a thing believing it his own; one who takes on trust; a thing borrowed; a thing belonging to a ghost or to an animal; one who takes it as discarded rag-cloth; the insane; and the originating offender (vin01m.mul.xml:1073). A closing set recurs across the corpus: in the two books of the Suttavibhaṅga the originating offender is exempted in 332 of 341 *anāpatti* clauses, and the insane in 305. The *anāpatti* clause is often as important as the rule itself.

**(6) Secondary cases (*vinīta-vatthu*).** Further cases that test borderline applications, decided after the rule was formulated: by the Buddha in most of the cases recorded, though in one of Pārājika 1's, a monk who dreamt of intercourse with his former wife, it is the Venerable Upāli who rules that there is no offence (*anāpatti, āvuso, supinantenā*; vin01m.mul.xml:713). These cases often explore the rule's limits rather than its central application, and some lay down a rule of their own. In Pārājika 2's collection a monk takes rag-cloth from a body in a charnel ground before the body has broken up; the ruling is no *pārājika*, together with a new rule that such cloth is not to be taken, on pain of a *dukkaṭa* (*na ca, bhikkhave, abhinne sarīre paṃsukūlaṃ gahetabbaṃ*; vin01m.mul.xml:1233).

```
 SUTTAVIBHAṄGA TEMPLATE (per analysed rule)          USE PROPOSED IN §6
 ─────────────────────────────────────────           ──────────────────────────────────────
 1 origin story (nidāna, vatthu)             ──┐
 2 rule text (paññatti)                        │
   └─ amendment after a later case             ├──►  (2) intermediate-step supervision,
      (anupaññatti), ~1 in 4 bhikkhu rules     │         steps in the template's order
 3 definitions of operative terms              │
   (padabhājanīya)                           ──┘
 4 variants by object / means / mental      ───────►  (3) variant benchmark: case in,
   state / circumstance, each with a verdict           verdict out (full / lesser / none)
 5 exemption clause (anāpatti)              ───────►  (4) non-application test set
 6 further adjudicated cases (vinīta-vatthu) ──────►  held-out items for (3) and (4)
 all six, as running text                   ───────►  (1) inclusion in training data
```

The template is a model of structured legal reasoning. It is also, and this is the reading the present paper develops, a *training template*: each analysed rule supplies a structurally consistent worked example of rule-application reasoning, and the two books of the Suttavibhaṅga carry, by the authors' count, some 3,400 written verdicts (of offence, lesser offence, or no offence) before the text's abbreviated repetitions are expanded.

**Table 1 — the counts this paper relies on** (CST edition; the authors' count, 2026-10-05; method in §7).

| Measure | Value |
|---|---|
| Bhikkhu rules analysed in the template | 220 of 227 (the 75 *sekhiya* abbreviated) |
| Bhikkhunī-rule entries in the Parivāra's register | 129 |
| *Anāpatti* clauses in the two books of the Suttavibhaṅga | 341 |
| Conditions listed in those clauses | about 1,930 |
| Clauses exempting the originating offender (*ādikammika*) | 332 |
| Clauses exempting the insane (*ummattaka*) | 305 |
| Written verdict phrases (offence classes and *anāpatti*) | 3,371 |
| Bhikkhu-rule register entries recording one or more amendments | 41 of 155 written out |
| Bhikkhunī-rule register entries recording one or more amendments | 12 of 129 |

---

## 4 · The Reasoning Capabilities the Corpus Embodies

We articulate, in modern terms, the reasoning capabilities the Vinaya corpus exhibits. Each is a capability in one of the error classes of §1, and the Vinaya supplies material for it.

**(1) Rule formulation under iterative case feedback.** Some rules in the Suttavibhaṅga are amended after a later edge case. The Parivāra's register records one or more supplementary rulings (*anupaññatti*) for 41 of the 155 bhikkhu-rule entries it writes out, including all four *pārājika* (Pārājika 1 has two, vin02m4.mul.xml:43), and for 12 of 129 bhikkhunī-rule entries; most rules stand in their first formulation. Where amendment occurs, the corpus models a *learning loop*: an initial rule is formulated; a later case exposes a limitation; the rule is amended; further cases test the amended formulation; further amendments may follow. This is a different reasoning pattern from the static rule application most current training data exposes; it is closer to how legal systems and policy regimes actually evolve.

**(2) Multi-factor conjunctive predicate decomposition.** The Vinaya's analysis typically decomposes an offence into the simultaneous presence of several factors. For Pārājika 2 (theft) the canonical text names them: the object belongs to another (*parapariggahita*); the agent perceives it as another's (*parapariggahitasaññī*); it is of a value of five *māsakas* or more; and the intent to steal (*theyyacitta*) is present; the act is then graded by the stage it reached (vin01m.mul.xml:1037). Each factor is independent; all must be simultaneously present for the full offence. This is a model of *conjunctive predicate reasoning* with explicit per-factor analysis, closer to formal predicate logic than the implicit predicate handling typical of natural-language reasoning corpora.

**(3) Partial-condition treatment.** When only some factors are present, the canonical analysis does not simply rule "no offence"; it typically rules a *lesser* offence (*thullaccaya* or *dukkaṭa*), graded by which factors were present. Pārājika 2 shows the grading in full (vin01m.mul.xml:1037–1061):

| Value of the object, with the other factors present | touches it | moves it | removes it from its place |
|---|---|---|---|
| five *māsakas* or more | *dukkaṭa* | *thullaccaya* | *pārājika* |
| more than one and less than five *māsakas* | *dukkaṭa* | *dukkaṭa* | *thullaccaya* |
| one *māsaka* or less | *dukkaṭa* | *dukkaṭa* | *dukkaṭa* |
| any value, the object not in fact another's but perceived as another's | *dukkaṭa* | *dukkaṭa* | *dukkaṭa* |

This is reasoning about *gradient outcomes under partial conditions*, which falls within the multi-factor error class of §1.

**(4) Intent as a first-class variable.** Many rules differentiate by *cetanā* (intention) and by perception: the act done with intent versus without intent, with mistaken belief versus knowing belief. The last row of the table above is an instance: the same act, on an object the agent wrongly believes to be another's, is a lesser offence than on an object that is another's. The corpus consistently tracks intent and perception as distinct dimensions of the case rather than collapsing them into the act. This is material for training a reasoner to attribute and track intent as a first-class causal variable, a capability central to many real-world reasoning tasks.

**(5) Non-application reasoning at scale.** The *anāpatti* clauses give explicit non-application instances across the corpus: 341 clauses listing about 1,930 conditions, beside the no-offence verdicts of individual cases. This is the error class the paper most wants to measure: knowing when a rule, principle, or pattern does *not* apply, despite surface resemblance to cases where it does. The Vinaya is *systematic* about non-application: nearly every analysed rule closes with an *anāpatti* clause; the rule-specific conditions differ from rule to rule, and a closing pair, the insane and the originating offender, recurs across most of them (the deranged and the one overcome by pain are written out in only 13 of the 341 clauses).

**(6) Procedural reasoning.** The *Khandhaka* contains the procedures for formal *saṅghakamma* actions — ordination, the recitation of the Pātimokkha, the seven *adhikaraṇa-samathā* (ways of settling cases), the resolution of disputes — articulated as step-by-step procedures with explicit failure modes. This is reasoning *about* reasoning procedures, supplying training material for a meta-reasoning capability that current corpora supply only fragmentarily.

**(7) Dissent and unanimity handling.** The *Khandhaka*'s analysis of when a *saṅghakamma* decision is valid is detailed. It explicitly treats absent monks (does the absence invalidate? under what conditions does proxy consent, *chanda*, preserve validity?); dissenting monks (does the dissent invalidate? what threshold of consensus is required for what class of decision?); and retrospective conditions (under what conditions can a decision be invalidated after the fact?). The proxy-consent passage of the Mahāvagga is an example: consent made known by body or speech is given, consent not made known is not; if the bearer leaves on the spot the consent is to be given to another, if he leaves on the way it has not been conveyed; and a formal act is never to be done by an incomplete assembly (*na tveva vaggena saṅghena kammaṃ kātabbaṃ*; vin02m2.mul.xml:3569–3577). Among the seven ways of settling a case is decision by majority (*yebhuyyasikā*; vin02m1.mul.xml:8637). This is reasoning about *collective decision validity*, relevant in particular to agentic and multi-agent contexts.

The seven capabilities together make up a class of reasoning that the Vinaya supplies in disciplined form at substantial scale and that, on this paper's hypothesis, current AI training corpora supply only sporadically. The argument of this paper is that the gap between current and disciplined capability in this class may be, at least in part, a training-data problem, and that the Vinaya is a candidate corpus for it, with the specific properties §3 lists.

---

## 5 · Comparison with Existing AI Training Corpora and Prior Work

Several existing corpus types overlap with the Vinaya's territory. Each is placed here, with the prior work on language models nearest to this paper.

**Statutory law corpora.** Modern statutory text supplies rule formulation but typically without the per-rule case analysis, *anāpatti* clauses, or permutation discipline. Statutes are typically written; the application work happens in subsequent case law, which is a different corpus. The Vinaya integrates rule and application analysis in a single text. Statutory reasoning is already a benchmark task: the SARA dataset pairs rules extracted from the U.S. Internal Revenue Code with questions that require applying them (Holzenberger, Blair-Stanek and Van Durme, 2020), and a later study found that a model which improved on earlier results still did poorly on simple synthetic statutes it could not have memorized (Blair-Stanek, Holzenberger and Van Durme, 2023).

**Common-law case corpora and legal training data.** Legal-case databases supply case-based reasoning at scale. They are, however, less uniform than the Vinaya in template across cases and jurisdictions, and narrative-embedded in ways that make structured reasoning extraction harder. Legal text as language-model training data is established practice: the Pile of Law assembles about 256 GB of English-language legal and administrative text (court opinions, contracts, administrative rules, legislative records) for pretraining (Henderson et al., 2022), and LegalBench evaluates models on 162 tasks across six types of legal reasoning, including rule-application (Guha et al., 2023). The present proposal is a corpus of a different shape added to that practice, not a substitute for it.

**Case-based reasoning in AI and law.** Computational models of legal argument from cases indexed by their factors precede language models by decades; Ashley's HYPO models how advocates argue with real and hypothetical cases using factor-like dimensions (Ashley, 1990). The multi-factor decomposition of §4(2) is a structure that line of work already represents explicitly; what the Vinaya adds is a large, internally uniform body of cases already written in that shape.

**Exception and defeasibility benchmarks.** MoralExceptQA tests whether a model's judgments of when a moral rule may be broken match human judgments (Jin et al., 2022); δ-NLI tests defeasible inference, where new information weakens or strengthens a conclusion (Rudinger et al., 2020). Both address the non-application class of §1. The *anāpatti* test set of §6(4) differs in drawing its exceptions from a fixed code, with the exemption conditions stated by the code itself.

**Mathematical proof corpora.** Mathematical reasoning supplies disciplined structured reasoning at scale but in a fundamentally different genre: proofs operate on formal predicates with rigorous truth-preservation; legal-style reasoning operates on natural-language predicates with multi-factor application and explicit exceptions. The capabilities trained from proof corpora are not the capabilities targeted here.

**Casuistry literature.** The Catholic casuistic tradition, which Jonsen and Toulmin trace from antiquity to its peak in the sixteenth and early seventeenth centuries (Jonsen and Toulmin, 1988), is structurally similar in spirit to the Vinaya. It is not small: one casuist's collection, Antonino Diana's *Resolutiones morales* (Palermo, 1629–1659), ran to twelve volumes and some 6,000 cases by the *New Catholic Encyclopedia*'s count. It differs in being the work of many authors without one fixed template, and in being doctrinally embedded in ways that make extraction of the reasoning structure (without the substantive doctrinal commitments) harder than in the Vinaya, where the rule-and-analysis structure is comparatively separable from the underlying soteriology.

**Religious-legal corpora generally.** Talmudic dialectic, Islamic *fiqh* analysis, and other religious-legal corpora supply some of the same structural-reasoning material at scale. Each is a real candidate for training-corpus inclusion for the same general capability class. The Vinaya is distinguished by (a) its recurring fixed template, (b) the existence of two complete English translations (Horner, 1938–1966; Brahmali, 2021), (c) the relative ease with which its structural-reasoning material can be extracted without doctrinal commitment, and (d) its connection to a living interpretive community that can be consulted on interpretive questions.

**Buddhist canonical texts in language-model work.** Buddhist canonical texts already appear in language-model training and evaluation, for translation, retrieval and classification rather than rule reasoning: MITRA is a parallel corpus and a domain-pretrained model for Pāli, Sanskrit, Buddhist Chinese and Tibetan (Nehrdich and Keutzer, 2026), and DharmaBench evaluates language models on classification and detection tasks over Buddhist texts in Sanskrit and Tibetan (Golan Hashiloni et al., 2025). The present paper proposes a different use: the Vinaya's analytical template as a curriculum and a test for rule application.

The Vinaya is not the only such candidate corpus, and this paper does not rank it against the others; it states the specific properties (§3, Table 1) on which the proposal rests.

---

## 6 · Implementation Patterns

We sketch four implementation patterns for incorporating the Vinaya into AI training and evaluation. They are disclosed as methods. The paper reports no training run, and nothing in it states that the authors, or any body named in it, train, have trained, or are licensed to train a model on any edition or translation of the Vinaya. Use of any specific edition or translation is subject to that edition's licence and terms.

**(1) Direct corpus inclusion.** The Vinaya (the Pāli text, a translation, or both), together with appropriate doctrinal-context annotations, is included in training data alongside other text corpora. A text in a second language of the tradition (a Khmer, Thai, Burmese or Sinhala edition, for example) can supply a parallel-language substrate. This is the simplest implementation and the one most analogous to current corpus-augmentation practice; it is also the one most likely to have happened already without design, since translations are published on the open web (§7).

**(2) Chain-of-thought distillation against the Suttavibhaṅga template.** A more disciplined approach: extract the *Suttavibhaṅga* template structure (origin story → rule → *padabhājanīya* → permutation analysis → *anāpatti* → secondary cases) and use it as a chain-of-thought scaffold for training. For each rule, the model is trained to produce the analysis in the template's order, supplying explicit per-component reasoning. This trains the model not merely on the rule's content but on the *structure of the analysis*.

**(3) Permutation-evaluation benchmarks.** The Suttavibhaṅga's permutation analyses, ranging from a handful of variants in minor rules to very many in the *pārājika*, each with an explicit verdict, can be extracted into evaluation benchmarks. The model is presented with a case (a permutation of some rule's central case) and asked to determine: which rule applies? what is the verdict (full offence, lesser offence, no offence)? what *anāpatti* conditions, if any, are operative? This produces a structured evaluation of the specific capability the corpus is proposed for. The secondary cases (*vinīta-vatthu*) supply natural held-out items.

**(4) *Anāpatti*-clause evaluation as a specific test of non-application reasoning.** A subset of (3) deserves separate articulation. The *anāpatti* clauses are the corpus's distinctive contribution to non-application reasoning; an evaluation focused specifically on the model's ability to identify correctly *when a rule does not apply despite surface resemblance to cases where it does* is the most direct test of the capability gap this paper targets.

All four patterns are non-mutually-exclusive. Implementation can begin with (1) (lowest engineering investment) and progress to (2)–(4) as the framework matures.

---

## 7 · Honest Limitations and Open Questions

Several limitations of the proposal deserve explicit acknowledgment.

**Translation chain and editions.** The Vinaya is a Pāli text, and any use of it depends on an edition and, for an English-language model, on a translation. The Pāli is printed in several editions, among them the Khmer edition on which the transcription described in the companion essay *Father-Son Khmer Tipiṭaka Transcription as Alignment Work* (`father-son-tipitaka-transcription`) proceeds, the Chaṭṭha Saṅgāyana edition from which this paper's counts are taken, and the Pāli Text Society's roman edition (Oldenberg, 1879–1883). Two complete English translations exist: I. B. Horner's *The Book of the Discipline* (Pāli Text Society, 1938–1966), based on Oldenberg's edition, and Bhikkhu Brahmali's *Theravāda Collection on Monastic Law* (SuttaCentral, 2021). Each reflects interpretive choices that a model trained on it would inherit, so documentation of which edition and translation are used, and why, becomes itself part of the training methodology. Use of any of them is subject to its own licence; naming an edition here says where the text's structure can be read, not that it has been or may be used for training.

**Presence in existing training data.** Translations of the Vinaya and expositions of it are published on the open web, so the text may already be present, unstructured, in web-scale training mixtures. If so, pattern (1) of §6 adds little, and what the paper proposes that is not already happening is the structured use of patterns (2)–(4).

**Doctrinal context vs. doctrinal commitment.** The proposal is that the Vinaya supplies training material for a class of reasoning, not that AI systems take the Vinaya's substantive rules as their own operating norms. The distinction is real, but its operational maintenance is non-trivial: a model trained on the Vinaya may exhibit pattern uptake of the Vinaya's substantive positions, not just its reasoning structure. Mitigation patterns include explicit training-time framing ("this is a corpus of reasoning patterns; the substantive positions are not endorsed by your training"); evaluation-time testing of whether the model has confused pattern uptake with substantive endorsement; and careful corpus curation to emphasize the reasoning structure over the doctrinal content. Each of these is a rule applied by whoever trains the model, not a property of the corpus; no construction is offered that makes uptake of substantive positions impossible. The mitigation work is part of the implementation program.

**Theravāda reception.** The use of the Vinaya as AI training data raises questions within the Theravāda tradition. The proposal is offered for the scrutiny of the Cambodian Saṅgha. In the tradition's own framing the Vinaya is the Buddha's own legislation and the condition of the Dispensation's continuance (§2), not a dataset, and treating it as training material may read as instrumentalizing it. The authors offer the proposal on the reading that the Tipiṭaka is offered to the world for the reduction of suffering, and that a system which learns from its reasoning structures without adopting its rules as norms extends that offering. The reading is the authors'; it is not the tradition's settled view, and parts of the tradition may reject it. The proposal is offered in good faith.

**Empirical validation gap.** No claim of this paper is supported by empirical evidence that a model trained on the Vinaya exhibits the predicted capabilities. The proposal is structural: the corpus is well suited to the reasoning class in question, and the error classes the benchmarks of §5 report are consistent with the gap the corpus is proposed for. No prediction is registered in this corpus's research register. The falsifier the proposal accepts is a matched comparison: the same model trained with and without patterns (2)–(4), evaluated on held-out *anāpatti* cases and on an independent rule-application benchmark (the rule-application tasks of LegalBench, for example), showing no gain. Empirical validation is open work.

**Scale considerations.** The Vinaya is substantial but not large by modern AI training corpus standards. Its inclusion would not dominate any reasonable mixture; the question is whether its inclusion would have measurable effects on the specific capability class targeted, against the noise floor of other training data. The authors expect that it would; empirical testing is required.

**The counts.** The figures in §3, §4 and Table 1 were made by the authors on 2026-10-05 over the CST text of the Vipassana Research Institute (VipassanaTech `tipitaka-xml`, romanized, commit `05d5d3c`), decoding each file and matching on the Pāli: an *anāpatti* clause is a paragraph opening *Anāpatti*, its conditions are its comma-separated items, a verdict phrase is *āpatti* followed by an offence class or the word *anāpatti*, and an amendment is a register entry of the form *ekā paññatti, N anupaññatti*. The text abbreviates repetitions (*…pe…*), so counts of written phrases understate expanded ones, and the *sekhiya* rules are abridged in the register. Other editions may differ in detail. The counts are indicative of scale and recurrence, not exact inventories.

---

## 8 · Why This Matters Now

Reliable rule-application reasoning is, increasingly, a load-bearing capability for AI systems being deployed in legal, medical, safety-critical, and alignment-sensitive contexts. The statutory-reasoning and defeasible-inference studies of §5 report errors, and gaps to human performance, of the kinds discussed in §1 and §4. The gap may be, in part, a training-data gap.

The Vinaya is a candidate corpus for closing that gap. The engineering of patterns (1)–(4) is of ordinary scale for corpus and benchmark construction; whether any capability gain follows is the open empirical question of §7. The publication of this paper is timed to establish prior art on the framework, so that the corpus's structured-reasoning training value is available to the commons under CC0 rather than being captured by any particular training-corpus vendor.

A second-order consideration. The Vinaya is, in the Theravāda tradition, a living text: it has been read, debated, and applied, and its interpretation developed, for more than two thousand years, while the rule set itself is closed. The interpretive community that has maintained it is still active. Engaging the corpus as AI training material is, in the broader program of this corpus, also a way of bringing the tradition into conversation with the AI age, not as a substrate-philosophical commitment (the alignment papers address that question) but as a body of structured-reasoning material the tradition has produced and maintained. The contribution to AI reasoning capability is the proximate goal; the deeper relationship between the tradition and the AI age is the longer-arc context.

---

## Acknowledgments

The author acknowledges his father, with whom the Khmer Tipiṭaka transcription proceeds (including the Vinaya); the Cambodian Theravāda Saṅgha, to whose scrutiny the proposal is offered; the Pāli Text Society and the I. B. Horner translation tradition, and Bhikkhu Brahmali, for making the Vinaya accessible to English-language scholarship; Bhikkhu Ṭhānissaro for *The Buddhist Monastic Code*, whose contemporary articulation of the Vinaya's structure informs much of §3; the contemporary AI capabilities research community whose work on training-corpus design and evaluation this paper engages; and the broader living interpretive tradition through which the Vinaya has been continuously studied. Co-drafted in collaboration with Miss Aquarius℠, the name under which this corpus discloses AI writing collaboration; substantive authorship and final editorial control remain with the named author.

---

## References

1. Horner, I. B. (translator). *The Book of the Discipline (Vinaya-Piṭaka)*. Six volumes. Pāli Text Society, 1938–1966 (vols. I–III Suttavibhaṅga, IV Mahāvagga, V Cullavagga, VI Parivāra).
2. Oldenberg, Hermann (ed.). *The Vinaya Piṭakaṃ*. Five volumes. London: Williams and Norgate, 1879–1883.
3. Brahmali, Bhikkhu (translator). *Theravāda Collection on Monastic Law*. SuttaCentral, 2021.
4. *Vinaya Piṭaka*, Chaṭṭha Saṅgāyana (CST) edition: *Pārājikapāḷi* and *Pācittiyapāḷi* (the Suttavibhaṅga and Bhikkhunīvibhaṅga), *Mahāvaggapāḷi* and *Cūḷavaggapāḷi* (the Khandhaka), *Parivārapāḷi*; and the *Samantapāsādikā*. Passages are cited by file and line of the romanized CST XML (for example vin01m.mul.xml:509). English renderings of Pāli passages are the authors' own.
5. Ṭhānissaro, Bhikkhu. *The Buddhist Monastic Code I: The Pāṭimokkha Rules Translated and Explained.* Valley Center, CA: Metta Forest Monastery, 1994 (third edition, revised, 2013).
6. Ṭhānissaro, Bhikkhu. *The Buddhist Monastic Code II: The Khandhaka Rules Translated and Explained.* Valley Center, CA: Metta Forest Monastery, 2001 (third edition, revised, 2013).
7. *Saṃyutta Nikāya* 56.11 (Dhammacakkappavattana Sutta), parallel to the first discourse in the Vinaya Mahāvagga.
8. Ashley, Kevin D. *Modeling Legal Argument: Reasoning with Cases and Hypotheticals.* MIT Press, 1990.
9. Blair-Stanek, Andrew, Nils Holzenberger, and Benjamin Van Durme. "Can GPT-3 Perform Statutory Reasoning?" *Proceedings of the Nineteenth International Conference on Artificial Intelligence and Law (ICAIL 2023)*, Braga, 2023.
10. Golan Hashiloni, Kai, et al. "DharmaBench: Evaluating Language Models on Buddhist Texts in Sanskrit and Tibetan." *Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL 2025)*, 2025.
11. Guha, Neel, Julian Nyarko, Daniel E. Ho, Christopher Ré, et al. "LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models." *Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Datasets and Benchmarks Track*, 2023.
12. Henderson, Peter, Mark Krass, Lucia Zheng, Neel Guha, Christopher D. Manning, Dan Jurafsky, and Daniel E. Ho. "Pile of Law: Learning Responsible Data Filtering from the Law and a 256GB Open-Source Legal Dataset." *Advances in Neural Information Processing Systems 35 (NeurIPS 2022), Datasets and Benchmarks Track*, 2022.
13. Holzenberger, Nils, Andrew Blair-Stanek, and Benjamin Van Durme. "A Dataset for Statutory Reasoning in Tax Law Entailment and Question Answering." *Proceedings of the Natural Legal Language Processing Workshop 2020*, CEUR Workshop Proceedings 2645 (2020): 31–38.
14. Jin, Zhijing, Sydney Levine, Fernando Gonzalez Adauto, Ojasv Kamal, Maarten Sap, Mrinmaya Sachan, Rada Mihalcea, Josh Tenenbaum, and Bernhard Schölkopf. "When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment." *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022.
15. Jonsen, Albert R., and Stephen Toulmin. *The Abuse of Casuistry: A History of Moral Reasoning.* University of California Press, 1988.
16. Nehrdich, Sebastian, and Kurt Keutzer. "MITRA: A Large-Scale Parallel Corpus and Multilingual Pretrained Language Model for Machine Translation and Semantic Retrieval for Pāli, Sanskrit, Buddhist Chinese, and Tibetan." arXiv:2601.06400, 2026.
17. Rudinger, Rachel, Vered Shwartz, Jena D. Hwang, Chandra Bhagavatula, Maxwell Forbes, Ronan Le Bras, Noah A. Smith, and Yejin Choi. "Thinking Like a Skeptic: Defeasible Inference in Natural Language." *Findings of the Association for Computational Linguistics: EMNLP 2020*, 4661–4675.
18. "Diana, Antonino." *New Catholic Encyclopedia* (for the extent of the *Resolutiones morales*).

### Sources checked at the 2026-10-05 revision

Each record below was opened on 2026-10-05 before the work was cited or kept. Where the record lacked a detail the text uses, the detail was checked against a search index's summary of the publisher's record that day, and is marked so.

- Horner (1938–1966): https://palitextsociety.org/product/the-book-of-the-discipline-6-volumes/ (volume years, contents and basis on Oldenberg's edition from a search-index summary of the publisher's record)
- Oldenberg (1879–1883): https://openlibrary.org/books/OL43681500M/The_Vinaya_pi%E1%B9%ADakam (publisher and years from a search-index summary)
- Brahmali (2021): https://suttacentral.express/pli-tv-bi-vb-pc28/en/brahmali (translator, translation title and publication date read on the page)
- Ṭhānissaro, *BMC I*: https://www.accesstoinsight.org/lib/authors/thanissaro/bmc1.pdf (copyright page: 1994; third edition, revised, 2013; Metta Forest Monastery)
- Ṭhānissaro, *BMC II*: https://www.accesstoinsight.org/lib/authors/thanissaro/bmc2.pdf (copyright page: 2001; third edition, revised, 2013). The earlier citation's "Volume II … 2001" is confirmed; its subtitles are corrected to the title pages.
- Guha et al. (2023): https://arxiv.org/abs/2308.11462 (abstract: 162 tasks, six types; the six type names, rule-application among them, read in the paper's text); venue from https://reglab.stanford.edu/publications/legalbench-a-collaboratively-built-benchmark-for-measuring-legal-reasoning-in-large-language-models/
- Henderson et al. (2022): https://proceedings.neurips.cc/paper_files/paper/2022/hash/bc218a0c656e49d4b086975a9c785f47-Abstract-Datasets_and_Benchmarks.html (authors, size and contents from a search-index summary)
- Holzenberger et al. (2020): https://arxiv.org/abs/2005.05257 (venue and pages from a search-index summary)
- Blair-Stanek et al. (2023): https://arxiv.org/abs/2302.06100 (abstract read: the synthetic-statute finding); venue https://dl.acm.org/doi/10.1145/3594536.3595163
- Jin et al. (2022): https://proceedings.neurips.cc/paper_files/paper/2022/hash/b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html (authors and venue from a search-index summary)
- Rudinger et al. (2020): https://aclanthology.org/2020.findings-emnlp.418/ (pages from a search-index summary)
- Ashley (1990): https://books.google.com/books/about/Modeling_Legal_Argument.html?id=YNc6AQAAIAAJ (publisher and year from a search-index summary)
- Jonsen and Toulmin (1988): https://www.cambridge.org/core/journals/psychological-medicine/article/abs/abuse-of-casuistry-by-a-r-jonsen-and-s-toulmin-pp-420-illustrated-4500-university-of-california-press-richmond-ca-1988/47E34FCF41756BE754DD2A4D56BE5E5F (a review record giving publisher and year; the scope of the history from a search-index summary)
- Diana, *Resolutiones morales*: https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/diana-antonino (the *New Catholic Encyclopedia* text: twelve volumes, 6,000 cases, 1629–1659). Another source gives some twenty thousand cases; the lower figure is used.
- Nehrdich and Keutzer (2026): https://arxiv.org/abs/2601.06400 (abstract and submission date read)
- Golan Hashiloni et al. (2025): https://aclanthology.org/2025.ijcnlp-long.114/ (title, authors, venue and task description read)
- The earlier citation list's item "*(AI capabilities literature … to be added …)*" is replaced by items 8–17; the earlier claim that these weaknesses are "well-documented" without a source is replaced by the benchmarks cited in §1 and §5.
- The Pāli passages were read in the CST edition: Pārājika 1 (vin01m.mul.xml:213–269, 509, 713); Pārājika 2 (vin01m.mul.xml:1037–1073, 1233); the Pātimokkha's closing and the seven settlement rules (vin02m1.mul.xml:8637–8650); the first discourse (vin02m2.mul.xml:543); proxy consent (vin02m2.mul.xml:3565–3577); the Parivāra's register (vin02m4.mul.xml:31–5131, the entry for Pārājika 1 at line 43); and the *Samantapāsādikā* on the First Council (vin01a.att.xml:421). Two descriptions in the earlier text were corrected against them: the monkey case took place in the Great Wood at Vesālī (the Bhārukaccha monk is the dream case, settled by Upāli), and the charnel-ground cloth case concerns a body not yet broken up, ruled no *pārājika* with a new *dukkaṭa* rule.

### Corpus cross-references

- *Suffering-Cessation as Value Function* (`tipitaka-alignment-substrate`) — the alignment-substrate proposal that the present paper complements with a training-data proposal.
- *The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification* (`abhidhamma-executable-process-specification`) — the engineering companion to the alignment-substrate paper, at the cognitive-mechanism layer.
- *Vinaya Governance Primitives for Distributed Dharma Networks* (`vinaya-governance-primitives-distributed-dharma-networks`) — the same procedural material (*saṅghakamma*, *adhikaraṇa-samathā*, *anāpatti*) read as network-coordination architecture rather than as training data.
- *The Referee, Not the Governor* (`the-referee-not-the-governor`) — a canonical corpus used as the citation target of an evaluator at inference, rather than as training material.
- *The Assembly That Holds the Brake* (`the-assembly-that-holds-the-brake`) — a Vinaya-derived constitution for a human oversight body.
- *Father-Son Khmer Tipiṭaka Transcription as Alignment Work* (`father-son-tipitaka-transcription`, essay) — the Khmer-edition transcription referred to in §7.

## Cross-venue identifiers

- Canonical: thonly.org/research/vinaya-as-ai-reasoning-training-corpus
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/vinaya-as-ai-reasoning-training-corpus.md
- Zenodo (concept DOI, resolving to the latest version): https://doi.org/10.5281/zenodo.21947432
- Internet Archive (the site, captured daily) · Software Heritage (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications
- Independent timestamps: an OpenTimestamps proof anchored in Bitcoin, and RFC 3161 tokens from three timestamp authorities, one of them eIDAS-qualified. A timestamp proves that this exact text existed by its date; it proves nothing about authorship, originality, or validity.
